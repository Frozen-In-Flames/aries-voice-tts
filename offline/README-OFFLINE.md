# Aries Hilton Voice: Offline Kit

The same trained voice as the online player, packaged to run
entirely on your own machine. Once set up, it needs no internet,
no account, and no server.

## Contents

- `aries-hilton.onnx` — the voice model (Piper / VITS format)
- `aries-hilton.onnx.json` — the model's configuration (keep it
  next to the .onnx file; the loader reads it automatically)
- `speak.py` — a small command-line speaker

## Setup (one time)

You need Python 3.9 or newer, then:

```bash
pip install piper-tts
```

That is the only download besides this kit. Everything after this
step is offline.

## Speak

```bash
python speak.py "The future is already built." -o future.wav
```

Or with the Piper command line directly:

```bash
echo "The future is already built." | piper --model aries-hilton.onnx --output_file future.wav
```

Output is a 22050 Hz WAV file you can play anywhere.

## About the voice

This model was fine-tuned from Piper's en_US-amy-medium voice
(MIT License) on Aries Hilton's own recordings, with his
permission, and is released by Frozen In Flames. The training
record and provenance live in the main repository:
https://github.com/Frozen-In-Flames/aries-voice-tts

Prefer not to install anything? The online player runs the same
model in your browser from that repository's demo page.
