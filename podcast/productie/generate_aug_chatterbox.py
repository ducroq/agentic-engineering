"""Generate Augmented Engineering podcast — per-line WAVs with Chatterbox.

Outputs individual WAV files per dialogue line for mixing with overlap markers.

Usage:
    scp podcast/productie/generate_aug_chatterbox.py gpu-server:~/
    ssh gpu-server "HF_HUB_OFFLINE=1 source ~/podcast-generator/vox-env/bin/activate && \
        python3 ~/generate_aug_chatterbox.py ~/aug_00_dialogue.txt -o ~/aug_00_lines/"
"""

import argparse
import re
import json
import sys
from pathlib import Path

import torch
import torchaudio
from chatterbox.tts import ChatterboxTTS

VOICE_REFS = {
    "lisa": Path.home() / "voice_refs" / "lisa.mp3",
    "marc": Path.home() / "voice_refs" / "felix.mp3",
    "narrator": Path.home() / "voice_refs" / "narrator.mp3",
    "sven": Path.home() / "voice_refs" / "sven.mp3",
}


def parse_script(path):
    """Parse script into dialogue lines and overlap markers.

    Returns list of dicts:
        {"type": "line", "speaker": "lisa", "text": "...", "index": 0}
        {"type": "overlap", "instruction": "Marc starts over tail of..."}
    """
    entries = []
    line_index = 0
    for raw in open(path, encoding="utf-8"):
        raw = raw.rstrip("\n")
        stripped = raw.strip()
        if not stripped:
            continue
        if stripped.startswith("# [OVERLAP]"):
            instruction = stripped.replace("# [OVERLAP]", "").strip()
            entries.append({"type": "overlap", "instruction": instruction})
            continue
        if stripped.startswith("#"):
            continue
        match = re.match(r"(\w+):\s*(?:\[\w+(?:\s+\w+)*\]\s*)?(.*)", stripped)
        if match:
            speaker = match.group(1).lower()
            text = match.group(2).strip()
            if text:
                entries.append({
                    "type": "line",
                    "speaker": speaker,
                    "text": text,
                    "index": line_index,
                })
                line_index += 1
    return entries


def main():
    parser = argparse.ArgumentParser(description="Generate per-line WAVs with Chatterbox")
    parser.add_argument("script", help="Dialogue script path")
    parser.add_argument("-o", "--output-dir", default="./aug_lines", help="Output directory for WAVs")
    parser.add_argument("--test", type=int, help="Only generate first N lines")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    entries = parse_script(args.script)
    lines = [e for e in entries if e["type"] == "line"]
    if args.test:
        lines = lines[:args.test]

    print(f"Parsed {len(lines)} dialogue lines, {sum(1 for e in entries if e['type'] == 'overlap')} overlap markers")

    print("Loading Chatterbox model...")
    model = ChatterboxTTS.from_pretrained(device="cuda")
    sr = model.sr
    print(f"Model loaded. Sample rate: {sr}")

    manifest = []

    for i, line in enumerate(lines):
        speaker = line["speaker"]
        text = line["text"]
        idx = line["index"]

        ref_path = VOICE_REFS.get(speaker)
        if ref_path and ref_path.exists():
            ref_str = str(ref_path)
        else:
            ref_str = None

        filename = f"{idx:03d}_{speaker}.wav"
        out_path = output_dir / filename

        print(f"  [{i+1}/{len(lines)}] {speaker}: {text[:60]}...")

        try:
            if ref_str:
                wav = model.generate(text, audio_prompt_path=ref_str)
            else:
                wav = model.generate(text)

            torchaudio.save(str(out_path), wav, sr)

            manifest.append({
                "index": idx,
                "speaker": speaker,
                "text": text,
                "file": filename,
                "duration": wav.shape[1] / sr,
            })
        except Exception as e:
            print(f"    ERROR: {e}")
            manifest.append({
                "index": idx,
                "speaker": speaker,
                "text": text,
                "file": None,
                "error": str(e),
            })

    # Save manifest + overlap markers for the mixer
    mix_data = {
        "sample_rate": sr,
        "lines": manifest,
        "overlaps": [e for e in entries if e["type"] == "overlap"],
        "entry_order": [
            {"type": e["type"], "index": e.get("index"), "instruction": e.get("instruction")}
            for e in entries
        ],
    }
    manifest_path = output_dir / "manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(mix_data, f, indent=2)

    print(f"\nDone. {len(manifest)} files in {output_dir}/")
    print(f"Manifest: {manifest_path}")


if __name__ == "__main__":
    main()
