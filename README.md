# Aries Voice TTS

A custom text-to-speech model built on the voice of Aries Hilton
(Frozen In Flames), with a live browser demo.

**Live demo: https://frozen-in-flames.github.io/aries-voice-tts/**

## What this is

This repository holds the complete lifecycle of one artist-owned voice
model: the recording corpus, the segmentation and training pipeline, the
trained model, and a demo page where text can be typed and heard back in
the artist's voice. It exists so the claim "a custom model of this voice"
is verifiable by listening, not by assertion.

## Corpus

The corpus is a single recorded session of the Voice Asset Recording
Script (Aries Hilton), recorded by the artist on November 21, 2026:

- A. The Rainbow Passage (complete phonetic coverage paragraph)
- B. A phoneme coverage word list (about 130 words)
- C. Ten connected-speech sentences (Harvard sentences)
- D. Six lines, each in six deliveries: neutral, warm, firm, angry,
  whisper, excited (36 items)
- E. Numbers and letters
- F. Twelve game lines

61 labeled items in total, segmented from the original take against the
script, each with a manifest entry (item, start, end, duration, matched
text).

## Pipeline

1. Segment the take into the 61 labeled items (local ASR alignment).
2. Package the items as a voicepack under the Voice Asset Format.
3. Train the text-to-speech model on the packaged corpus.
4. Verify by ear: generated speech is compared against the artist's real
   recordings before the model is called done.
5. Publish the model and activate the live demo on this repository's
   Pages site.

## Voicepack

The packaged voice is public in this repository: `aries-hilton.voicepack`,
with the full corpus it references under `corpus/` (63 items: the 61
script items plus the two NATO bonus takes). The package passes the
Voice Asset Format validator, corpus verification included: every corpus
file's SHA-256 recorded in the package matches the files here, so the
claim is checkable by anyone.

Declared status: `trained`. The package now carries the trained model
itself: `model/aries-hilton.onnx`, a VITS model (Piper architecture)
fine-tuned on this corpus from the Piper en_US-amy-medium base
checkpoint (600 epochs; the published weights are the epoch 499
checkpoint, selected by measurement against the final checkpoint:
pitch in the artist's range at 128.9 to 134.5 Hz, held-out-line word
error 0.0 to 0.111). The weights were learned from the artist's own
recordings and are his. This package supersedes the November 21
package, whose model slot held an XTTS-v2 cloning profile over Coqui's
weights and which declared `reference` for exactly that reason; the
same ONNX model is also published loose under `model/` in this
repository for direct use.

## Ownership

The voice, the corpus, and the trained model are the property of
Aries Hilton. Under the Kindling model, the artist owns the model built
on their voice. The pipeline code in this repository is released under
Apache-2.0; the voice model and corpus are all rights reserved by the
artist and are not covered by that license.

## Status

Corpus complete (61 of 61 items plus 2 bonus takes, November 21, 2026)
and published in this repository with the validated voicepack. The
fine-tuned model was trained on November 22, 2026 and is published
here, in the voicepack and loose under `model/`; generated samples
from it are on the demo page. Remaining: wiring the demo's Speak
button to run the published ONNX model in the browser.
