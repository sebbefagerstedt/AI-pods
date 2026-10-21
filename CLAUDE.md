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
10. **What happens when you press Enter.** Probabilities, sampling, temperature, context windows; why next-word prediction can look like thinking, and hallucinations.
11. **Scale changes everything.** GPT-2, GPT-3 and in-context learning, scaling laws, the race for bigger models and data centers.
12. **From autocomplete to assistant.** Base models vs. chat models, instruction tuning, RLHF, and how ChatGPT came together.

Possible Season 2, "Understanding the headlines": hallucinations, memory and RAG, reasoning models (o1, DeepSeek-R1), agents and tool use, image and video generators, open vs. closed models and who's who, interpretability, AI safety, chips and data centers, benchmarks.

## Status and next steps

Nothing has been recorded yet. The first session ran in the "Tributary" environment, which couldn't reach the voice models, so work continues in a new chat that uses the "AI Pods" environment.

1. Make a ~15-second sample clip of the two hosts talking, commit it under `samples/`, and share it in the chat for feedback on voices and tone.
2. Produce episodes 1–2 as a pilot; adjust depth, tone and voices before making the rest.

## Environment notes

- Text-to-speech: Kokoro-82M (open-source, good English voices, runs on CPU), installed from PyPI; its model weights download from Hugging Face. ffmpeg is installed for stitching and MP3 export.
- Work in the "AI Pods" cloud environment, which has full network access. The first session ran in "Tributary", where Hugging Face was blocked and only package registries like PyPI worked. If access is ever narrowed, the voice models need `huggingface.co` and `*.hf.co`.
- github.com is reachable only for this repo. If Kokoro's text front-end (misaki) fails to download the spaCy model `en_core_web_sm` from GitHub, install that model from Hugging Face (`spacy/en_core_web_sm`) instead.
