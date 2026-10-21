# Voices

The renderer clones each host's voice from the recording named after them: a script line starting `FRANK:` is spoken in the voice of `frank.wav`. To try another recording, pass e.g. `--voice ALICE=voices/maya.wav`. The show's hosts are Frank and Alice.

- `alice.wav`, `carter.wav`, `frank.wav`, `maya.wav`: VibeVoice's demo voices (MIT license, © 2025 Microsoft), from the Hugging Face dataset `bezzam/vibevoice_samples`.

A new voice needs 10–30 seconds of one person talking naturally in a quiet room. The clone copies the delivery as well as the voice, so a relaxed, conversational take works better than a careful reading. Only add someone's voice with their permission.

Recording your own voice:

- Talk for 20–30 seconds the way you'd explain something to a friend, for example a topic you know well or what you did last weekend. Don't read a text aloud, or the clone will sound like someone reading.
- Use a quiet room with soft furnishings (no echo, music or TV). A phone's voice memo app is fine; hold the phone about 20 cm from your mouth.
- Any audio format works; it gets converted to WAV here.
