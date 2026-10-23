# Episode 11: Scale changes everything

From Zero to ChatGPT, season 1, episode 11. About 23 minutes, with Frank and Alice. Part 3, "The birth of LLMs".

What happened when OpenAI took GPT-1 and just made it bigger. GPT-2 and the unicorn story it was "too dangerous" to release; the scaling laws chart, which showed that compute, data and model size each make a model predictably better; GPT-3 and learning a task from a few examples in the prompt; DeepMind's Chinchilla correction; and the race for chips, data centers and power that followed.

## Key terms

- **Parameters:** the knobs of episode 2. GPT-1 had about 117 million, GPT-2 1.5 billion, GPT-3 175 billion.
- **Loss:** episode 2's "how wrong". For a language model, how surprised it is, on average, by the real next token in text it has never seen. Lower is better.
- **Tokens:** words and pieces of words (episode 6), what models actually read. In English, a token is about three quarters of a word.
- **Compute:** how much computing goes into training, roughly the model's size times the amount of text it reads. Measured in floating-point operations; the scaling laws paper uses *petaflop/s-days* (a computer doing a thousand trillion operations a second, running for a day). GPT-3 took about 3,640 of them.
- **Zero-shot / few-shot:** doing a task with no examples, or with a few examples written into the prompt, and no fine-tuning either way.
- **Prompt:** the text you give a model to continue.
- **In-context learning:** picking up a task from examples in the prompt, without changing any parameters. It improves with model size; how it works inside the model is still studied.
- **Scaling laws:** the finding that loss falls in a predictable way as you scale up compute, data or parameters. See Figure 1 below.
- **Power law:** the kind of relationship in the scaling laws. Every tenfold increase cuts the loss by the same share, which looks like a straight line on a chart with log scales on both axes (each step is ten times more).
- **Compute-optimal:** the best split of a fixed compute budget between model size and data. Kaplan (2020) said put most of it into size; Chinchilla (2022) said grow both equally, about 20 tokens per parameter.
- **Overtraining:** training a model on far more tokens than compute-optimal, because a smaller model is cheaper to run afterwards. Llama 3 8B read about 15 trillion tokens, nearly 2,000 per parameter.
- **API:** a service programs call over the internet. GPT-3 was offered this way, through the OpenAI API, from June 2020; the model itself was never released.
- **Prompt engineering:** the craft of wording prompts and picking examples to get the output you want.

## Figure 1 of the scaling laws paper

The chart the episode is built around. Kaplan and others (2020), [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361), page 2.

- **Three panels:** test loss (how wrong, lower is better) against *compute*, *dataset size* (tokens) and *parameters*. Both axes are log scales.
- **The straight lines:** in each panel the loss falls along a straight line, a power law, "when not bottlenecked by the other two". In the paper's fits, ten times the parameters cuts the loss by about 16%, ten times the data by about 20%, ten times the compute (spent on the right model size) by about 11%. Some trends span more than seven orders of magnitude, with no sign of leveling off at the top.
- **The faint curves (compute panel):** each is one model, of a fixed size, during pre-training. Each drops quickly, then flattens as it meets the line, because a model that size has no more room to improve. The dashed line is the frontier: the lowest loss for each amount of compute, reached by picking the right model size.
- **The message:** it's not only compute. All three dials matter, and they have to grow together.
- **"Non-embedding":** the axis labels count parameters and compute without the token-embedding table (episode 6), which made the lines cleaner.

Later sections worth a look: the architecture details (depth vs. width) barely matter; bigger models are more *sample-efficient*, reaching the same loss from fewer tokens; and so, with more compute, the paper advised making the model much bigger and the data only somewhat bigger. Chinchilla revised that advice.

## Numbers worth remembering

| | Released | Parameters | Training text |
|---|---|---|---|
| GPT-1 | June 2018 | 117 million | BooksCorpus, about 5 GB |
| GPT-2 | February 2019 (full model November) | 1.5 billion | WebText, 8 million pages, 40 GB |
| GPT-3 | May 2020 | 175 billion | about 300 billion tokens |
| Chinchilla | March 2022 | 70 billion | about 1.4 trillion tokens |
| Llama 3 8B | April 2024 | 8 billion | about 15 trillion tokens |

- GPT-2's four sizes: 117M, 345M, 762M, 1.5B. Context window: 1,024 tokens (GPT-1: 512; GPT-3: 2,048).
- WebText: outbound links from Reddit with at least 3 karma, Wikipedia removed.
- GPT-3's training mix: filtered Common Crawl (60% of what it saw), WebText2, two book collections and English Wikipedia.
- GPT-3's training compute: about 3.14 × 10²³ operations. Its cost wasn't published; outside estimates were several million dollars per run.
- GPT-3 news articles: readers spotted the machine-written ones about 52% of the time, close to a coin flip.
- Chinchilla vs. Gopher: the same compute; Gopher had 280 billion parameters and read 300 billion tokens.
- Stargate (January 2025): OpenAI, SoftBank, Oracle and MGX, up to $500 billion over four years for US data centers.

## Timeline

- June 2018: GPT-1 (episode 9).
- February 2019: GPT-2, held back; released in stages, the full model in November.
- March 2019: Rich Sutton's "The Bitter Lesson".
- July 2019: Microsoft invests $1 billion in OpenAI.
- January 2020: scaling laws.
- May 2020: GPT-3, and Microsoft's supercomputer for OpenAI.
- June 2020: the OpenAI API.
- March 2022: Chinchilla.
- November 2022: ChatGPT (episode 12).
- March 2023: GPT-4, its final loss predicted from much smaller runs.
- December 2024: Ilya Sutskever's "we have but one internet" talk.
- January 2025: Stargate.

## Papers and sources

- Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei and Ilya Sutskever (2019), [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). GPT-2. Section 3 has the zero-shot tests, including "TL;DR:" for summaries; Figure 1 shows scores rising with model size.
- OpenAI (2019), [Better language models and their implications](https://openai.com/index/better-language-models/). The unicorn story ("10 tries") and the decision not to release the full model; and [GPT-2: 1.5B release](https://openai.com/index/gpt-2-1-5b-release/), November 2019.
- Jared Kaplan, Sam McCandlish, Tom Henighan, Tom Brown and others (2020), [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361). Start with Figure 1 and the summary in section 1.1; the rest is optional.
- Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah and others (2020), [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165). GPT-3. Figure 2.1 has the sea otter example; Figure 1.2 shows in-context learning improving with size; section 6 covers misuse and bias.
- Microsoft (2020), "Microsoft announces new supercomputer, lays out vision for future AI work": 285,000 CPU cores and 10,000 GPUs.
- Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch and others (2022), [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556). Chinchilla.
- Meta (2024), [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783).
- OpenAI (2023), [GPT-4 Technical Report](https://arxiv.org/abs/2303.08774), section 3, "Predictable Scaling".
- Rich Sutton (2019), [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html). Two pages.
- Ilya Sutskever (2024), "Sequence to sequence learning with neural networks: what a decade", NeurIPS 2024 talk (on YouTube): "we have but one internet", data as "the fossil fuel of AI".
- OpenAI (2025), [Announcing The Stargate Project](https://openai.com/index/announcing-the-stargate-project/).

Next: episode 12, "From autocomplete to assistant".
