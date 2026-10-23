# AI-pods

A personal podcast series that teaches AI and LLM fundamentals. Episodes are written as scripts, turned into audio with text-to-speech, and listened to in Apple Podcasts.

## The listener

- Sharp and follows current AI news, but missed the foundations and wants the basics.
- Has read "Attention Is All You Need" (2017). Plans to read OpenAI's GPT-1 paper, "Improving Language Understanding by Generative Pre-Training" (2018). GPT-1 is an assumption the listener hasn't confirmed.
- Finds the papers heavy going and lacks time for them, so episodes must be easy to follow by ear.

## Decisions

- Episode length follows the content: as long as the topic needs to be explained well, without padding or rushing. Around 20 minutes is typical, not a target. Scripts run about 175 words a minute.
- Two hosts, Frank and Alice. In each segment one explains and the other is the sharp, curious one who asks the questions the listener would ask ("wait, why does that matter?"); they swap roles from segment to segment, with a short handover ("Alice, this one's yours").
- The series is called "From Zero to ChatGPT" in the episodes, after the season title.
- English.
- Plain language and everyday analogies first, then the real term. Nothing should require seeing an equation.
- Each episode builds on the earlier ones and ends with a short recap.
- Each episode in the repo: the script with show notes (key terms, links to the original papers) and the MP3. Test clips go in `samples/`, episodes in `episodes/NN-slug/`: `script.md` (the dialogue only, so it can be rendered), `notes.md` (the show notes) and `NN-slug.mp3`.
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
11. **Scale changes everything.** GPT-2, GPT-3 and in-context learning, scaling laws, the race for bigger models and data centers. Walk through Figure 1 of "Scaling Laws for Neural Language Models" (Kaplan and others, 2020, arXiv 2001.08361), which the listener found eye-opening: they thought only compute mattered, but loss falls along a straight line on log-log axes with each of compute, data and parameters, and only while the other two keep up, so all three must grow together. In the compute panel, the faint curves are single fixed-size models in pre-training (not fine-tuning): each flattens as it meets the line because the model has no more room. Mention the Chinchilla revision (2022, more data, smaller model).
12. **From autocomplete to assistant.** Base models vs. chat models, instruction tuning, RLHF, and how ChatGPT came together.

Possible Season 2, "Understanding the headlines": hallucinations, memory and RAG, reasoning models (o1, DeepSeek-R1), agents and tool use, image and video generators, open vs. closed models and who's who, interpretability, AI safety, chips and data centers, benchmarks.

## Status and next steps

1. The first samples, made with Kokoro, sounded too computer-like. The listener likes how "The Curiosity Mix" sounds, an AI podcast that has all the hallmarks of NotebookLM's Audio Overviews: the hosts react to each other ("Right." "Exactly."), use fillers and finish each other's sentences.
2. Switched to VibeVoice, which performs the whole conversation at once. Feedback on the first VibeVoice samples: the listener likes Frank's voice, and Maya sounds like a computer (her source recording is a flat technical reading).
3. The listener picked Frank and Alice and asked them to swap roles during episodes. (They also offered to record their own voice; see `voices/README.md` if that comes up again.)
4. Done: episode 1 in `episodes/01-what-is-ai/` (17 minutes; segments 2 and 5 needed a second take). The listener likes episodes 1 and 9; some spots have faint, short music like an intro jingle (VibeVoice adds it on its own), which they don't mind. They're short on credits and fine with lower quality, so keep the work per episode lean (see `RUN_ON_YOUR_COMPUTER.md`, written for them to render on their own computer). Next: episode 2, then the rest.
5. Episode 9 came next, out of order, because it's the topic the listener most wanted: script and notes in `episodes/09-gpt-1/` (5,000 words). Done: rendered at 29.6 minutes; half the segments needed a retake, and the run took three 2-hour background jobs, resuming from the cache. It opens part 3 and works without episodes 2–8, reminding the listener of each idea as it comes up. So when writing 2–8, keep what it calls back to: the knobs and "how wrong" (2), walking downhill in fog (4), ImageNet as millions of labeled photos (5), word embeddings, "king − man + woman" and tokens as word pieces (6), LSTMs reading one word at a time and forgetting (7), and the transformer's two towers, encoder on the left, decoder on the right with its no-peeking rule (8). It promises that 10 covers whether predicting the next word is understanding, context windows ("whole books at once"), temperature and making things up; 11 GPT-2; and 12 how pre-training and fine-tuning still make ChatGPT.
6. Episode 11 came next, again because the listener most wanted it: script and notes in `episodes/11-scale/` (4,100 words, about 23 minutes), not yet rendered. Like 9, it reminds the listener of earlier ideas as it goes (knobs and loss, next-word pre-training, fine-tuning, tokens) and promises that 12 covers how GPT-3, a pure next-word guesser, became an assistant.

## Scripts and voices

- Script format: every paragraph starts with the speaker's name in capitals, `FRANK:` or `ALICE:`, and the voice is cloned from `voices/<name>.wav`. Lines starting with `#` are skipped, so `## Segment` headings are fine. Any other unlabeled paragraph stops the render, so nothing is dropped silently.
- Write the way people talk, not the way people read aloud. The one asking reacts and pushes back ("Okay, fair. But...", "Huh. So..."), and both hosts use the odd filler, unfinished thought or "you know". VibeVoice performs these naturally. It doesn't do overlapping speech or sounds like laughter, so avoid "Ha." and the like.
- The four demo voices in `voices/` are Alice and Maya (women) and Carter and Frank (men). A clone copies the recording's delivery as well as its sound: Alice and Carter are chatty, Frank's source is a narrated deep dive, and Maya's a technical reading (rejected as computer-like).
- Names and acronyms: spell them the way they should sound ("Mycin" for MYCIN, which otherwise gets spelled out; "Bert" and "Elmo" for BERT and ELMo) or leave them for the show notes (XCON). Long strings of hard names in one sentence can derail the model, so spread them out. Moravec came out garbled in a test. A probe for episode 9 came out fine for GPT-1 ("GPT one"), GPT-2, Radford, Smashwords, Books Corpus, LSTMs and Race; Sutskever came out close; Whisper wrote "cloze test" as "closed test", which sounds nearly the same.
- VibeVoice now and then puts a line in the other host's voice, garbles it or adds a stray sound (a beep, once). The renderer catches this: after each segment it transcribes the audio with Whisper, lines the words up with the script to find each line, checks each line's voice, and retakes the segment with a new seed (up to three takes) if anything is off.
- Nobody can listen during a session, so also run `tools/check.py SCRIPT.md OUT.mp3` on the finished episode. It runs the same check over the whole file and lists any line that's missing or in the wrong voice; `--words` lists where the wording differs, which shows how names came out. On a whole episode it takes about as long as the audio, so run it in the background and alone. Whisper sometimes gets stuck repeating "thank you" over a stretch, which shows up as a missing line; transcribe that stretch on its own before believing it. On episode 9 the whole-file check flagged four lines as mostly missing that were all there: Whisper loses its place on long files. Re-running `review` on the cached segment that holds the line (`.cache/segments/`, found with `segments` and `cache_path`) settles it.

## Environment notes

- Work in the "AI Pods" cloud environment. On 2026-10-21 it reached Hugging Face, PyPI, the PyTorch wheel index and raw.githubusercontent.com; github.com pages for other repos returned 403. The first session ran in "Tributary", where Hugging Face was blocked. If access is ever narrowed, the voice models need `huggingface.co` and `*.hf.co`.
- Text-to-speech: VibeVoice-1.5B (Microsoft, MIT license, released for research), run through transformers as `vibevoice/VibeVoice-1.5B-hf` (5.4 GB, downloaded on first use). The 7B model needs 18.7 GB, more than this machine's 15 GB of memory. Run `tools/setup.sh` to build `.venv` with CPU-only PyTorch and the versions pinned in `tools/requirements.txt`. ffmpeg is preinstalled.
- Render with `.venv/bin/python tools/render.py SCRIPT.md OUT.mp3`, adding `--voice ALICE=voices/maya.wav` to use another recording `--seed 7` for different takes, or `--takes 1` to skip retakes (about half the time). It uses an Nvidia card or Apple silicon when there is one (untested). It runs about 4.7 times slower than real time, using the CPU's bfloat16 (AMX) support, so a 20-minute episode takes about 1.5 hours, more if segments need retakes: run it in the background. The first render after the container restarts is slower, since the model has to be read from disk again. It renders about 3 minutes of script at a time and caches each finished segment in `.cache/`, so an interrupted render resumes where it stopped. The checks use `openai/whisper-small.en` and `microsoft/wavlm-base-plus-sv`, also downloaded on first use.
- Output is a mono MP3 at 44.1 kHz and 96 kbps, about 0.7 MB a minute. Pauses longer than 0.7 s are shortened. Each host is leveled to -19 LUFS; the renderer tells them apart by voice, since clones can come out a dB or two apart. A mono file plays 3 dB louder on two speakers, so -19 LUFS matches Apple's -16 LUFS target. A limiter keeps true peaks under Apple's -1 dBTP.
- Kokoro-82M was tried first: fast, but it reads each line on its own and sounded computer-like. It's in the git history.
