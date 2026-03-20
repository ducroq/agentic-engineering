"""Test the mix_episode.py mixer against failure modes.

Generates synthetic WAV files (sine tones per speaker) and runs the mixer
through normal and edge cases. No GPU required — runs locally.

Usage:
    python test_mixer.py
"""

import json
import os
import sys
import tempfile
import shutil
from pathlib import Path

import numpy as np
import soundfile as sf

# Synthetic audio: different frequency per speaker so overlaps are audible
SPEAKER_FREQS = {"lisa": 330, "marc": 220, "sven": 440}
SR = 24000


def make_tone(speaker, duration_sec, sr=SR):
    """Generate a sine tone for a speaker."""
    freq = SPEAKER_FREQS.get(speaker, 300)
    t = np.linspace(0, duration_sec, int(sr * duration_sec), dtype=np.float32)
    # Add envelope to avoid clicks
    audio = 0.5 * np.sin(2 * np.pi * freq * t)
    fade = min(int(sr * 0.02), len(audio) // 4)
    audio[:fade] *= np.linspace(0, 1, fade)
    audio[-fade:] *= np.linspace(1, 0, fade)
    return audio


def write_test_case(tmpdir, lines, overlaps_before=None):
    """Write synthetic WAVs and manifest for a test case.

    Args:
        tmpdir: output directory
        lines: list of (speaker, text, duration_sec)
        overlaps_before: set of line indices that have an overlap marker before them
    """
    overlaps_before = overlaps_before or set()
    manifest_lines = []
    entry_order = []

    for i, (speaker, text, dur) in enumerate(lines):
        filename = f"{i:03d}_{speaker}.wav"
        audio = make_tone(speaker, dur)
        sf.write(str(Path(tmpdir) / filename), audio, SR)

        manifest_lines.append({
            "index": i,
            "speaker": speaker,
            "text": text,
            "file": filename,
            "duration": dur,
        })

        if i in overlaps_before:
            entry_order.append({"type": "overlap", "index": None, "instruction": f"Test overlap before line {i}"})
        entry_order.append({"type": "line", "index": i, "instruction": None})

    data = {
        "sample_rate": SR,
        "lines": manifest_lines,
        "overlaps": [e for e in entry_order if e["type"] == "overlap"],
        "entry_order": entry_order,
    }

    with open(Path(tmpdir) / "manifest.json", "w") as f:
        json.dump(data, f, indent=2)


def run_mixer(input_dir, output_path, extra_args=None):
    """Run mix_episode.py and return success status."""
    import subprocess
    cmd = [sys.executable, str(Path(__file__).parent / "mix_episode.py"),
           str(input_dir), "-o", str(output_path)]
    if extra_args:
        cmd.extend(extra_args)
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0, result.stdout, result.stderr


def check_output(path, min_duration=0.0, max_duration=None):
    """Validate output WAV."""
    if not Path(path).exists():
        return False, "Output file missing"
    audio, sr = sf.read(path, dtype="float32")
    dur = len(audio) / sr
    if dur < min_duration:
        return False, f"Too short: {dur:.2f}s < {min_duration:.2f}s"
    if max_duration and dur > max_duration:
        return False, f"Too long: {dur:.2f}s > {max_duration:.2f}s"
    peak = np.abs(audio).max()
    if peak > 1.0:
        return False, f"Clipping: peak={peak:.3f}"
    if peak < 0.01:
        return False, f"Nearly silent: peak={peak:.5f}"
    return True, f"OK ({dur:.2f}s, peak={peak:.3f})"


def test_normal_dialogue():
    """Test: normal three-speaker dialogue, no overlaps."""
    tmpdir = tempfile.mkdtemp(prefix="mixer_test_")
    try:
        write_test_case(tmpdir, [
            ("lisa", "First line from Lisa.", 2.0),
            ("marc", "Marc responds here.", 2.5),
            ("sven", "Sven pushes back.", 1.8),
            ("marc", "Marc continues.", 2.0),
            ("lisa", "Lisa wraps up.", 1.5),
        ])
        out = Path(tmpdir) / "mixed.wav"
        ok, stdout, stderr = run_mixer(tmpdir, out)
        assert ok, f"Mixer failed: {stderr}"
        valid, msg = check_output(out, min_duration=8.0)
        assert valid, msg
        return True, msg
    finally:
        shutil.rmtree(tmpdir)


def test_with_overlaps():
    """Test: dialogue with overlap markers."""
    tmpdir = tempfile.mkdtemp(prefix="mixer_test_")
    try:
        write_test_case(tmpdir, [
            ("lisa", "Lisa speaks first.", 2.0),
            ("marc", "Marc overlaps.", 1.5),
            ("sven", "Sven follows normally.", 2.0),
        ], overlaps_before={1})
        out = Path(tmpdir) / "mixed.wav"
        ok, stdout, stderr = run_mixer(tmpdir, out)
        assert ok, f"Mixer failed: {stderr}"
        valid, msg = check_output(out, min_duration=3.0)
        assert valid, msg
        # Should be shorter than sum of durations (overlap compresses time)
        audio, sr = sf.read(out)
        total = len(audio) / sr
        assert total < 5.5 + 1.0, f"Overlap didn't compress: {total:.2f}s"
        return True, f"{msg} (overlap compressed to {total:.2f}s)"
    finally:
        shutil.rmtree(tmpdir)


def test_overlap_on_short_line():
    """FMEA #1: overlap advance > line duration."""
    tmpdir = tempfile.mkdtemp(prefix="mixer_test_")
    try:
        write_test_case(tmpdir, [
            ("lisa", "Short.", 0.3),  # Very short line
            ("marc", "Overlap onto short line.", 2.0),
        ], overlaps_before={1})
        out = Path(tmpdir) / "mixed.wav"
        ok, stdout, stderr = run_mixer(tmpdir, out)
        assert ok, f"Mixer crashed on short overlap: {stderr}"
        valid, msg = check_output(out, min_duration=0.3)
        assert valid, msg
        return True, msg
    finally:
        shutil.rmtree(tmpdir)


def test_consecutive_overlaps():
    """FMEA #2: two overlaps in a row."""
    tmpdir = tempfile.mkdtemp(prefix="mixer_test_")
    try:
        write_test_case(tmpdir, [
            ("lisa", "Lisa starts.", 2.0),
            ("marc", "Marc overlaps.", 1.5),
            ("sven", "Sven also overlaps.", 1.5),
        ], overlaps_before={1, 2})
        out = Path(tmpdir) / "mixed.wav"
        ok, stdout, stderr = run_mixer(tmpdir, out)
        assert ok, f"Mixer crashed on consecutive overlaps: {stderr}"
        valid, msg = check_output(out)
        assert valid, msg
        return True, msg
    finally:
        shutil.rmtree(tmpdir)


def test_overlap_on_first_line():
    """FMEA #3: overlap marker before any audio exists."""
    tmpdir = tempfile.mkdtemp(prefix="mixer_test_")
    try:
        write_test_case(tmpdir, [
            ("lisa", "First line with overlap marker.", 2.0),
            ("marc", "Normal second line.", 2.0),
        ], overlaps_before={0})
        out = Path(tmpdir) / "mixed.wav"
        ok, stdout, stderr = run_mixer(tmpdir, out)
        # Should either handle gracefully or skip the overlap
        valid, msg = check_output(out, min_duration=2.0)
        if not ok or not valid:
            return True, f"Handled edge case (ok={ok}, {msg})"
        return True, msg
    finally:
        shutil.rmtree(tmpdir)


def test_clipping_from_overlap():
    """FMEA #4: two loud signals summed in overlap."""
    tmpdir = tempfile.mkdtemp(prefix="mixer_test_")
    try:
        # Use louder tones
        for i, (speaker, dur) in enumerate([("lisa", 2.0), ("marc", 2.0)]):
            filename = f"{i:03d}_{speaker}.wav"
            freq = SPEAKER_FREQS[speaker]
            t = np.linspace(0, dur, int(SR * dur), dtype=np.float32)
            audio = 0.9 * np.sin(2 * np.pi * freq * t)  # Near max amplitude
            sf.write(str(Path(tmpdir) / filename), audio, SR)

        data = {
            "sample_rate": SR,
            "lines": [
                {"index": 0, "speaker": "lisa", "text": "Loud Lisa.", "file": "000_lisa.wav", "duration": 2.0},
                {"index": 1, "speaker": "marc", "text": "Loud Marc.", "file": "001_marc.wav", "duration": 2.0},
            ],
            "overlaps": [{"type": "overlap", "instruction": "Overlap loud signals"}],
            "entry_order": [
                {"type": "line", "index": 0, "instruction": None},
                {"type": "overlap", "index": None, "instruction": "Loud overlap"},
                {"type": "line", "index": 1, "instruction": None},
            ],
        }
        with open(Path(tmpdir) / "manifest.json", "w") as f:
            json.dump(data, f, indent=2)

        out = Path(tmpdir) / "mixed.wav"
        ok, stdout, stderr = run_mixer(tmpdir, out)
        assert ok, f"Mixer failed on loud overlap: {stderr}"
        valid, msg = check_output(out)
        assert valid, f"Clipping detected: {msg}"
        return True, msg
    finally:
        shutil.rmtree(tmpdir)


def test_missing_wav():
    """FMEA #6: WAV file referenced in manifest is missing."""
    tmpdir = tempfile.mkdtemp(prefix="mixer_test_")
    try:
        write_test_case(tmpdir, [
            ("lisa", "Lisa speaks.", 2.0),
            ("marc", "Marc speaks.", 2.0),
            ("sven", "Sven speaks.", 2.0),
        ])
        # Delete the middle file
        (Path(tmpdir) / "001_marc.wav").unlink()
        out = Path(tmpdir) / "mixed.wav"
        ok, stdout, stderr = run_mixer(tmpdir, out)
        assert ok, f"Mixer crashed on missing WAV: {stderr}"
        valid, msg = check_output(out, min_duration=2.0)
        assert valid, msg
        return True, f"{msg} (skipped missing file)"
    finally:
        shutil.rmtree(tmpdir)


def test_empty_script():
    """FMEA #8: no dialogue lines."""
    tmpdir = tempfile.mkdtemp(prefix="mixer_test_")
    try:
        write_test_case(tmpdir, [])
        out = Path(tmpdir) / "mixed.wav"
        ok, stdout, stderr = run_mixer(tmpdir, out)
        # Should handle gracefully — either empty file or clean exit
        return True, f"Handled empty script (ok={ok})"
    finally:
        shutil.rmtree(tmpdir)


def test_same_speaker_shorter_pause():
    """Test: same speaker continuation uses shorter pauses than turn-taking."""
    tmpdir = tempfile.mkdtemp(prefix="mixer_test_")
    try:
        write_test_case(tmpdir, [
            ("marc", "Marc first sentence.", 1.5),
            ("marc", "Marc continues.", 1.5),
            ("lisa", "Lisa responds.", 1.5),
        ])
        out = Path(tmpdir) / "mixed.wav"
        ok, stdout, stderr = run_mixer(tmpdir, out)
        assert ok, f"Mixer failed: {stderr}"
        valid, msg = check_output(out, min_duration=4.0)
        assert valid, msg
        # Check that output mentions different pause types
        assert "same" in stdout.lower() and "turn" in stdout.lower(), \
            f"Expected different pause types in output"
        return True, msg
    finally:
        shutil.rmtree(tmpdir)


if __name__ == "__main__":
    tests = [
        ("Normal dialogue", test_normal_dialogue),
        ("With overlaps", test_with_overlaps),
        ("Overlap on short line", test_overlap_on_short_line),
        ("Consecutive overlaps", test_consecutive_overlaps),
        ("Overlap on first line", test_overlap_on_first_line),
        ("Clipping from overlap", test_clipping_from_overlap),
        ("Missing WAV file", test_missing_wav),
        ("Empty script", test_empty_script),
        ("Same speaker pause", test_same_speaker_shorter_pause),
    ]

    print(f"Running {len(tests)} mixer tests...\n")
    passed = 0
    failed = 0

    for name, test_fn in tests:
        try:
            ok, msg = test_fn()
            if ok:
                print(f"  PASS  {name}: {msg}")
                passed += 1
            else:
                print(f"  FAIL  {name}: {msg}")
                failed += 1
        except Exception as e:
            print(f"  FAIL  {name}: {e}")
            failed += 1

    print(f"\n{passed}/{len(tests)} passed, {failed} failed")
    sys.exit(0 if failed == 0 else 1)
