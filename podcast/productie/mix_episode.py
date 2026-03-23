"""Mix per-line WAVs into a podcast episode with overlaps and natural timing.

Reads the manifest.json produced by generate_aug_chatterbox.py (or generate_aug_qwen.py),
layers audio with overlap markers, adds random pauses between speakers, and outputs
the final mixed WAV.

Usage:
    python mix_episode.py aug_00_lines/ -o aug_00_mixed.wav

Timing model:
    - Same speaker continues: 80-200ms pause (thinking gap)
    - Speaker change: 200-500ms pause (turn-taking gap)
    - After overlap marker: next line starts 200-400ms BEFORE previous line ends
    - Crossfade overlap region: 80ms
"""

import argparse
import json
import random
import sys
from pathlib import Path

import numpy as np
import soundfile as sf


def time_stretch(audio, factor):
    """Simple time-stretch by linear interpolation. factor > 1.0 = slower."""
    if abs(factor - 1.0) < 0.01:
        return audio
    indices = np.linspace(0, len(audio) - 1, int(len(audio) * factor))
    return np.interp(indices, np.arange(len(audio)), audio).astype(np.float32)


def load_wav(path, target_sr=None):
    """Load WAV file as float32 numpy array."""
    audio, sr = sf.read(path, dtype="float32")
    if audio.ndim > 1:
        audio = audio.mean(axis=1)  # mono
    return audio, sr


def crossfade(a, b, fade_samples):
    """Crossfade between end of a and start of b."""
    if fade_samples <= 0 or fade_samples > len(a) or fade_samples > len(b):
        return np.concatenate([a, b])

    fade_out = np.linspace(1.0, 0.0, fade_samples, dtype=np.float32)
    fade_in = np.linspace(0.0, 1.0, fade_samples, dtype=np.float32)

    result = np.zeros(len(a) + len(b) - fade_samples, dtype=np.float32)
    result[:len(a)] = a
    result[len(a) - fade_samples:len(a)] *= fade_out
    result[len(a) - fade_samples:len(a)] += b[:fade_samples] * fade_in
    result[len(a):] = b[fade_samples:]
    return result


def make_silence(duration_sec, sr):
    """Create silence of given duration."""
    return np.zeros(int(duration_sec * sr), dtype=np.float32)


def main():
    parser = argparse.ArgumentParser(description="Mix per-line WAVs with overlaps and natural timing")
    parser.add_argument("input_dir", help="Directory with per-line WAVs and manifest.json")
    parser.add_argument("-o", "--output", default="mixed.wav", help="Output WAV path")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for reproducible timing")
    parser.add_argument("--same-speaker-pause", nargs=2, type=float, default=[0.08, 0.20],
                        metavar=("MIN", "MAX"), help="Pause range (seconds) for same speaker continuing")
    parser.add_argument("--turn-pause", nargs=2, type=float, default=[0.20, 0.50],
                        metavar=("MIN", "MAX"), help="Pause range (seconds) for speaker changes")
    parser.add_argument("--overlap-advance", nargs=2, type=float, default=[0.20, 0.40],
                        metavar=("MIN", "MAX"), help="How far (seconds) the overlapping line starts before previous ends")
    parser.add_argument("--crossfade-ms", type=int, default=80, help="Crossfade duration in ms for overlaps")
    parser.add_argument("--speaker-speed", nargs=2, action="append", default=[],
                        metavar=("SPEAKER", "FACTOR"),
                        help="Speed factor per speaker (e.g., --speaker-speed marc 1.15 slows marc by 15%%)")
    args = parser.parse_args()

    # Parse speaker speed map
    speaker_speeds = {}
    for speaker, factor in args.speaker_speed:
        speaker_speeds[speaker.lower()] = float(factor)

    random.seed(args.seed)
    input_dir = Path(args.input_dir)

    # Load manifest
    manifest_path = input_dir / "manifest.json"
    if not manifest_path.exists():
        print(f"ERROR: {manifest_path} not found")
        sys.exit(1)

    with open(manifest_path) as f:
        data = json.load(f)

    sr = data["sample_rate"]
    lines_by_index = {l["index"]: l for l in data["lines"] if l.get("file")}
    entry_order = data["entry_order"]

    crossfade_samples = int(args.crossfade_ms / 1000.0 * sr)

    # Build the timeline
    mixed = np.zeros(0, dtype=np.float32)
    prev_speaker = None
    next_is_overlap = False
    overlap_instruction = None

    for entry in entry_order:
        if entry["type"] == "overlap":
            next_is_overlap = True
            overlap_instruction = entry.get("instruction", "")
            continue

        if entry["type"] == "line":
            idx = entry["index"]
            if idx not in lines_by_index:
                continue

            line_info = lines_by_index[idx]
            wav_path = input_dir / line_info["file"]
            if not wav_path.exists():
                print(f"  WARNING: {wav_path} missing, skipping")
                continue

            audio, file_sr = load_wav(str(wav_path))
            if file_sr != sr:
                print(f"  WARNING: {wav_path} has sr={file_sr}, expected {sr}")

            speaker = line_info["speaker"]

            # Apply per-speaker speed adjustment
            speed_factor = speaker_speeds.get(speaker, 1.0)
            if speed_factor != 1.0:
                audio = time_stretch(audio, speed_factor)

            # Fade in/out to prevent clicks at splice points (8ms)
            fade_len = min(int(sr * 0.008), len(audio) // 4)
            if fade_len > 0:
                audio[:fade_len] *= np.linspace(0, 1, fade_len, dtype=np.float32)
                audio[-fade_len:] *= np.linspace(1, 0, fade_len, dtype=np.float32)

            if len(mixed) == 0:
                # First line — no pause
                mixed = audio
                print(f"  {idx:03d} {speaker}: {line_info['text'][:50]}... ({len(audio)/sr:.1f}s)")

            elif next_is_overlap:
                # Overlap: start this line before the previous one ends
                advance_sec = random.uniform(*args.overlap_advance)
                advance_samples = int(advance_sec * sr)
                advance_samples = min(advance_samples, len(mixed), len(audio))

                print(f"  {idx:03d} {speaker}: {line_info['text'][:50]}... ({len(audio)/sr:.1f}s) [OVERLAP {advance_sec:.2f}s]")

                # Create overlapping mix
                overlap_start = len(mixed) - advance_samples
                overlap_len = min(advance_samples, len(audio))

                # Extend mixed to hold the full new audio
                new_length = max(len(mixed), overlap_start + len(audio))
                new_mixed = np.zeros(new_length, dtype=np.float32)
                new_mixed[:len(mixed)] = mixed

                # Apply crossfade in the overlap region
                cf = min(crossfade_samples, overlap_len)
                if cf > 0:
                    fade_out = np.linspace(1.0, 0.7, cf, dtype=np.float32)  # Don't fully fade out — both voices audible
                    fade_in = np.linspace(0.7, 1.0, cf, dtype=np.float32)
                    new_mixed[overlap_start:overlap_start + cf] *= fade_out
                    audio_copy = audio.copy()
                    audio_copy[:cf] *= fade_in
                    new_mixed[overlap_start:overlap_start + len(audio)] += audio_copy
                else:
                    new_mixed[overlap_start:overlap_start + len(audio)] += audio

                mixed = new_mixed
                next_is_overlap = False
                overlap_instruction = None

            else:
                # Normal transition — add pause
                if speaker == prev_speaker:
                    pause_sec = random.uniform(*args.same_speaker_pause)
                    pause_type = "same"
                else:
                    pause_sec = random.uniform(*args.turn_pause)
                    pause_type = "turn"

                pause = make_silence(pause_sec, sr)
                mixed = np.concatenate([mixed, pause, audio])
                print(f"  {idx:03d} {speaker}: {line_info['text'][:50]}... ({len(audio)/sr:.1f}s) [{pause_type} {pause_sec:.2f}s]")

            prev_speaker = speaker

    if len(mixed) == 0:
        print("ERROR: No audio to mix")
        sys.exit(1)

    # Normalize to prevent clipping from overlaps
    peak = np.abs(mixed).max()
    if peak > 0.95:
        mixed = mixed * (0.95 / peak)
        print(f"\n  Normalized peak from {peak:.3f} to 0.95")

    # Save
    sf.write(args.output, mixed, sr)
    total_duration = len(mixed) / sr
    minutes = int(total_duration // 60)
    seconds = total_duration % 60
    print(f"\nSaved: {args.output} ({minutes}m {seconds:.1f}s)")


if __name__ == "__main__":
    main()
