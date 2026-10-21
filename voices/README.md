# Voices

The renderer clones each host's voice from one of these recordings, e.g. `tools/render.py script.md out.mp3 --voice COHOST=voices/carter.wav`. The defaults are Frank explaining and Alice asking.

- `alice.wav`, `carter.wav`, `frank.wav`, `maya.wav`: VibeVoice's demo voices (MIT license, © 2025 Microsoft), from the Hugging Face dataset `bezzam/vibevoice_samples`.

A new voice needs 10–30 seconds of one person talking naturally in a quiet room. The clone copies the delivery as well as the voice, so a relaxed, conversational take works better than a careful reading. Only add someone's voice with their permission.

Recording your own voice:

- Talk for 20–30 seconds the way you'd explain something to a friend, for example a topic you know well or what you did last weekend. Don't read a text aloud, or the clone will sound like someone reading.
- Use a quiet room with soft furnishings (no echo, music or TV). A phone's voice memo app is fine; hold the phone about 20 cm from your mouth.
- Any audio format works; it gets converted to WAV here.
