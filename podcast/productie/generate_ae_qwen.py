"""Generate Agentic Engineering podcast episode using Qwen3-TTS.

Usage:
    scp podcast/productie/generate_ae_qwen.py gpu-server:~/
    ssh gpu-server "source ~/podcast-generator/qwen-tts-env/bin/activate && python3 ~/generate_ae_qwen.py ~/ae_00_dialogue.txt -o ~/ae_00_qwen.wav"
"""

import torch
import soundfile as sf
import numpy as np
import json
import re
import sys
from pathlib import Path
from qwen_tts import Qwen3TTSModel

VOICE_REF_DIR = Path("/home/hcl/voice_refs/qwen_self_refs")
MANIFEST = json.load(open(VOICE_REF_DIR.parent / "qwen_self_refs" / "ref_manifest.json"))

VOICE_MAP = {
    "lisa": "lisa",
    "marc": "felix",
    "sven": "sven",
}

def parse_script(path):
    lines = []
    for raw in open(path):
        raw = raw.strip()
        if not raw or raw.startswith("#"):
            continue
        match = re.match(r"^(\w+):\s*(.+)$", raw)
        if match:
            speaker = match.group(1).lower()
            text = match.group(2).strip()
            lines.append((speaker, text))
    return lines

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_ae_qwen.py script.txt [-o output.wav]")
        sys.exit(1)

    script_path = sys.argv[1]
    output_path = sys.argv[3] if len(sys.argv) > 3 and sys.argv[2] == "-o" else "ae_qwen_output.wav"

    lines = parse_script(script_path)
    print(f"Parsed {len(lines)} dialogue lines")

    print("Loading Qwen3-TTS...")
    model = Qwen3TTSModel.from_pretrained(
        "Qwen/Qwen3-TTS-12Hz-1.7B-Base",
        device_map="cuda:0",
        dtype=torch.bfloat16,
    )
    print("Model loaded.")

    all_audio = []
    sr = 24000

    for i, (speaker, text) in enumerate(lines):
        voice_key = VOICE_MAP.get(speaker)
        if not voice_key or voice_key not in MANIFEST:
            print(f"  [{i+1}/{len(lines)}] Skipping unknown speaker: {speaker}")
            continue

        ref_info = MANIFEST[voice_key]
        ref_audio_path = str(VOICE_REF_DIR.parent / ref_info["ref_audio"])
        ref_text = ref_info["ref_text"]

        print(f"  [{i+1}/{len(lines)}] {speaker}: {text[:60]}...")

        try:
            wavs, file_sr = model.generate_voice_clone(
                text=text,
                language="English",
                ref_audio=ref_audio_path,
                ref_text=ref_text,
                max_new_tokens=2048,
            )
            # wavs is a tensor or numpy array
            if hasattr(wavs, 'numpy'):
                audio_np = wavs.squeeze().cpu().numpy().astype(np.float32)
            elif hasattr(wavs, 'cpu'):
                audio_np = wavs.squeeze().cpu().numpy().astype(np.float32)
            else:
                audio_np = np.array(wavs, dtype=np.float32).squeeze()
            sr = file_sr
            all_audio.append(audio_np)
            # Small pause between speakers
            pause = np.zeros(int(sr * 0.3), dtype=np.float32)
            all_audio.append(pause)
        except Exception as e:
            print(f"    ERROR: {e}")
            continue

    if all_audio:
        combined = np.concatenate(all_audio)
        sf.write(output_path, combined, sr)
        print(f"Saved to {output_path} ({len(combined)/sr:.1f}s)")
    else:
        print("No audio generated!")

if __name__ == "__main__":
    main()
