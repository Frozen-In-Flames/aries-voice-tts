# Aries Voice TTS

A custom text-to-speech model built on the voice of Aries Hilton
(Frozen In Flames), with a live browser demo.

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

## Ownership

The voice, the corpus, and the trained model are the property of
Aries Hilton. Under the Kindling model, the artist owns the model built
on their voice. The pipeline code in this repository is released under
Apache-2.0; the voice model and corpus are all rights reserved by the
artist and are not covered by that license.

## Status

Corpus received and verified (November 21, 2026). Segmentation in
progress. The demo page activates when the trained model lands.
