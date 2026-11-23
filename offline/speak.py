#!/usr/bin/env python3
"""Speak text with the Aries Hilton voice, fully offline.

Usage:
    python speak.py "Text to speak" [-o output.wav] [--model aries-hilton.onnx]

Setup (one time, needs internet):
    pip install piper-tts

After that one install, everything runs locally. No account, no
server, no network calls: the voice model in this folder does the
work on your own machine.
"""

import argparse
import sys
import wave
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("text", help="Text to speak")
    parser.add_argument(
        "-o",
        "--output",
        default="output.wav",
        help="Where to write the WAV file (default: output.wav)",
    )
    parser.add_argument(
        "--model",
        default=str(Path(__file__).with_name("aries-hilton.onnx")),
        help="Path to the .onnx voice model (its .onnx.json sits beside it)",
    )
    args = parser.parse_args()

    try:
        from piper import PiperVoice
    except ImportError:
        print(
            "piper-tts is not installed. Run: pip install piper-tts",
            file=sys.stderr,
        )
        return 1

    voice = PiperVoice.load(args.model)
    with wave.open(args.output, "wb") as wav_file:
        if hasattr(voice, "synthesize_wav"):
            voice.synthesize_wav(args.text, wav_file)
        else:  # older piper-tts releases
            voice.synthesize(args.text, wav_file)
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
