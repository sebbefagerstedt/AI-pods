# AI-pods

A personal podcast series that teaches AI and LLM fundamentals. Episodes are written as scripts, turned into audio with text-to-speech, and listened to in Apple Podcasts.

## The listener

- Sharp and follows current AI news, but missed the foundations and wants the basics.
- Has read "Attention Is All You Need" (2017). Plans to read OpenAI's GPT-1 paper, "Improving Language Understanding by Generative Pre-Training" (2018). GPT-1 is an assumption the listener hasn't confirmed.
- Finds the papers heavy going and lacks time for them, so episodes must be easy to follow by ear.

## Decisions

- Episodes of about 20 minutes (roughly 3,000 words of script).
- Two hosts: one explains, the other is a sharp, curious co-host who asks the questions the listener would ask ("wait, why does that matter?").
- English.
- Plain language and everyday analogies first, then the real term. Nothing should require seeing an equation.
- Each episode builds on the earlier ones and ends with a short recap.
- Each episode in the repo: the script with show notes (key terms, links to the original papers) and the MP3. Test clips go in `samples/`, episodes in `episodes/NN-slug/`.
- For now, the MP3s just live in this repo. Later the listener will set up GitHub Pages so an RSS feed can bring the episodes into Apple Podcasts (Follow a Show by URL). The repo will become private: Pages on a private repo needs a paid GitHub plan, and the Pages site itself stays public.

## Season 1: From zero to ChatGPT

Part 1: How machines learn

1. **What is AI, actually?** Turing, the 1956 Dartmouth workshop, expert systems, the AI winters, and why learning from data beat hand-written rules.
2. **Machine learning: teaching by example.** A model as a function with millions of adjustable knobs, training vs. using it, loss ("how wrong"), memorizing vs. generalizing.
3. **Neural networks without the math.** Neurons, weights, layers, what "deep" means; from the 1958 perceptron to today.
4. **How machines actually learn.** Gradient descent ("walking downhill in fog") and backpropagation.
5. **2012, the big bang.** ImageNet, gaming GPUs and AlexNet; how Nvidia ended up at the center.

Part 2: Teaching computers language

6. **Words as numbers.** Tokens and embeddings, "king − man + woman ≈ queen" (word2vec, 2013), why models count tokens.
7. **Reading one word at a time.** RNNs and LSTMs, why they forgot, and attention invented for translation (2014).
8. **"Attention Is All You Need", explained.** Self-attention, queries/keys/values, multi-head attention, positional encoding, and why parallel training mattered. Companion to the paper the listener has read.

Part 3: The birth of LLMs

9. **GPT-1 and pre-training.** Next-word prediction on raw text, then fine-tuning; BERT as the fill-in-the-blank rival. Meant to be heard before reading the GPT-1 paper.
10. **What happens when you press Enter.** Probabilities, sampling, temperature, context windows; why next-word prediction can look like thinking, and hallucinations. Contextual inertia: the model rereads the whole chat every turn, so its own earlier answers pull on the next ones, and it can cling to an early wrong turn even after you correct it; why a fresh chat often helps. Papers: "Breaking Contextual Inertia" (2026, arXiv 2603.04783) and "LLMs Get Lost in Multi-Turn Conversation" (2025, arXiv 2505.06120).
11. **Scale changes everything.** GPT-2, GPT-3 and in-context learning, scaling laws, the race for bigger models and data centers.
12. **From autocomplete to assistant.** Base models vs. chat models, instruction tuning, RLHF, and how ChatGPT came together.

Possible Season 2, "Understanding the headlines": hallucinations, memory and RAG, reasoning models (o1, DeepSeek-R1), agents and tool use, image and video generators, open vs. closed models and who's who, interpretability, AI safety, chips and data centers, benchmarks.

## Status and next steps

1. The first samples, made with Kokoro, sounded too computer-like. The listener likes how "The Curiosity Mix" sounds, an AI podcast that has all the hallmarks of NotebookLM's Audio Overviews: the hosts react to each other ("Right." "Exactly."), use fillers and finish each other's sentences.
2. Switched to VibeVoice, which performs the whole conversation at once. Feedback on the first VibeVoice samples: the listener likes Frank's voice, and Maya sounds like a computer (her source recording is a flat technical reading).
3. Done: two samples of the lines in `samples/sample.md` pairing Frank with Alice, the other conversational voice. Frank explains and Alice asks (recommended: he gets the most airtime and it's the cleaner take), or the other way round. Waiting for the listener's pick. They may record their own voice for one host (see `voices/README.md`). When a recording arrives, convert it to WAV in `voices/`, render the sample with it and run the check.
4. Produce episodes 1–2 as a pilot; adjust depth, tone and voices before making the rest.

## Scripts and voices

- Script format: every paragraph starts with a speaker label, `HOST:` (the explainer) or `COHOST:`. Lines starting with `#` are skipped. Any other unlabeled paragraph stops the render, so nothing is dropped silently.
- Write the way people talk, not the way people read aloud. The co-host reacts and pushes back ("Okay, fair. But...", "Huh. So..."), and both hosts use the odd filler, unfinished thought or "you know". VibeVoice performs these naturally. It doesn't do overlapping speech or sounds like laughter.
- Voices are cloned from recordings in `voices/`. The four demo voices are Alice and Maya (women) and Carter and Frank (men); the defaults are Frank explaining and Alice asking. A clone copies the recording's delivery as well as its sound: Alice and Carter are chatty, Frank's source is a narrated deep dive, and Maya's a technical reading (rejected as computer-like).
- If a word comes out wrong, respell it the way it sounds.
- Nobody can listen during a session, so check every render with `tools/check.py`. It splits the MP3 at pauses, labels each stretch with the closest host voice, transcribes it with Whisper, and reports whether the hosts speak in the script's order and where the words differ.

## Environment notes

- Work in the "AI Pods" cloud environment. On 2026-10-21 it reached Hugging Face, PyPI, the PyTorch wheel index and raw.githubusercontent.com; github.com pages for other repos returned 403. The first session ran in "Tributary", where Hugging Face was blocked. If access is ever narrowed, the voice models need `huggingface.co` and `*.hf.co`.
- Text-to-speech: VibeVoice-1.5B (Microsoft, MIT license, released for research), run through transformers as `vibevoice/VibeVoice-1.5B-hf` (5.4 GB, downloaded on first use). The 7B model needs 18.7 GB, more than this machine's 15 GB of memory. Run `tools/setup.sh` to build `.venv` with CPU-only PyTorch and the versions pinned in `tools/requirements.txt`. ffmpeg is preinstalled.
- Render with `.venv/bin/python tools/render.py SCRIPT.md OUT.mp3`, adding `--voice COHOST=voices/carter.wav` to change a voice or `--seed 7` for a different take. It runs about 4.7 times slower than real time, using the CPU's bfloat16 (AMX) support, so a 20-minute episode takes about 1.5 hours: run it in the background. The first render after the container restarts is slower, since the model has to be read from disk again. It renders about 3 minutes of script at a time and caches each finished segment in `.cache/`, so an interrupted render resumes where it stopped.
- Output is a mono MP3 at 44.1 kHz and 96 kbps, about 0.7 MB a minute. Pauses longer than 0.7 s are shortened. Each host is leveled to -19 LUFS; the renderer tells them apart by voice, since clones can come out a dB or two apart. A mono file plays 3 dB louder on two speakers, so -19 LUFS matches Apple's -16 LUFS target. A limiter keeps true peaks under Apple's -1 dBTP.
- Kokoro-82M was tried first: fast, but it reads each line on its own and sounded computer-like. It's in the git history.
