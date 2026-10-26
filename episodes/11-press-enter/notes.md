# Episode 11: What happens when you press Enter

From Zero to ChatGPT, season 1, episode 11. About 21 minutes, with Frank and Alice. Part 3, "The birth of LLMs".

From the output layer's spread of bets to an actual answer. Why the model writes one token at a time and rereads everything after each one; how it picks a token, and what temperature does; context windows, and why the app sends your whole chat every turn; contextual inertia, the pull of the model's own earlier answers, and why a fresh chat often helps; whether next-word prediction is thinking; and why models make things up, starting with the lawyer whose brief cited six court cases that didn't exist.

## Key terms

- **Autoregressive generation:** producing text one token at a time, each chosen from the model's prediction given everything so far, then appended and fed back in. Generation stops at a special end-of-turn token. In practice the model caches its intermediate results for earlier tokens (the *KV cache*) so each new token costs one pass, not a full re-run.
- **Greedy decoding:** always taking the most likely token. Fine for short factual answers; on longer text it tends to be bland and to fall into repetition.
- **Sampling:** choosing the next token at random, in proportion to its probability. Why the same question can get different answers, and what "regenerate" does.
- **Temperature:** a setting that sharpens (below 1) or flattens (above 1) the probabilities before sampling. Temperature 0 means greedy. Low for code and facts, higher for brainstorming; too high and the text falls apart. Named after its role in the physics formula it's borrowed from (the Boltzmann distribution).
- **Top-p (nucleus) sampling:** sampling only from the smallest set of top tokens whose probabilities add up to p (say 90%), cutting off the long tail of unlikely tokens. From Holtzman and others (2019).
- **System prompt:** hidden instructions the app adds before your messages ("You are a helpful assistant…", the date, rules). More in the next episode.
- **Context window:** the maximum number of tokens a model can take in at once: prompt, chat history and its own answer together. GPT-1: 512. GPT-3: 2,048. GPT-4 (2023): 8,192 and 32,768. GPT-4 Turbo (late 2023): 128,000. Gemini 1.5 (2024): up to 1 million, later more.
- **Statelessness:** the model keeps nothing between calls. Its "memory" of a conversation is the transcript the app sends every turn. Chat "memory" features work by adding saved notes to that text.
- **Lost in the middle:** models used information at the start and end of a long context better than in the middle (Liu and others, 2023).
- **Contextual inertia:** a model's tendency to stay consistent with its own earlier reasoning in a conversation, even after it's corrected or given new information (Chen and others, 2026). Laban and others (2025) measured an average 39% drop when the same task was given piece by piece over several turns instead of in one message, mostly from unreliability: early assumptions, premature answers, then over-reliance on them.
- **Stochastic parrots:** the 2021 argument (Bender, Gebru and others) that language models stitch together statistically likely text without meaning, with risks from size, cost and training data.
- **World model:** an internal representation of the situation a text describes. Othello-GPT (Li and others, 2022), trained only on move sequences, developed an internal map of the board that researchers could read and edit, changing its predictions.
- **Hallucination:** a fluent, confident statement that's false. Kalai and others (2025) argue it follows from training and testing that reward guessing over "I don't know", like a multiple-choice exam with no penalty for wrong answers.

## Practical tips from the episode

- Put everything that matters in your first message: details, constraints, examples.
- When a chat goes off track, start a new one and restate what you need, including what you learned from the failed attempt.
- Treat specific details as the riskiest part of an answer: names, numbers, dates, quotes, citations, links. Check them somewhere else, not by asking the same chat.
- When you can, give the model the source text and ask it to answer from that.

## Papers and sources

- *Mata v. Avianca, Inc.*, No. 22-cv-1461 (S.D.N.Y.), sanctions order of June 22, 2023: at least six cited cases were "bogus judicial decisions with bogus quotes and bogus internal citations". News coverage: [Lawyer apologizes for fake court citations from ChatGPT](https://abc7.com/chatgpt-lawyer-steven-schwartz-ai/13313071/) (Associated Press, 2023).
- Ari Holtzman and others (2019), [The Curious Case of Neural Text Degeneration](https://arxiv.org/abs/1904.09751). Why always taking the likeliest word goes wrong, and nucleus sampling.
- Nelson Liu and others (2023), [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172).
- Gemini Team, Google (2024), [Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context](https://arxiv.org/abs/2403.05530).
- Philippe Laban, Hiroaki Hayashi, Yingbo Zhou and Jennifer Neville (2025), [LLMs Get Lost In Multi-Turn Conversation](https://arxiv.org/abs/2505.06120). Over 200,000 simulated conversations with 15 models.
- Xingwu Chen, Zhanqiu Zhang, Yiwen Guo and Difan Zou (2026), [Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction](https://arxiv.org/abs/2603.04783). Names the effect and proposes a training fix that uses the model's own single-turn answers as anchors.
- Emily Bender, Timnit Gebru, Angelina McMillan-Major and Shmargaret Shmitchell (2021), [On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?](https://doi.org/10.1145/3442188.3445922), FAccT.
- Kenneth Li and others (2022), [Emergent World Representations: Exploring a Sequence Model Trained on a Synthetic Task](https://arxiv.org/abs/2210.13382). Othello-GPT.
- Anthropic (2025), [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model), and the full paper, [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html). Including the model choosing a rhyme before writing the line.
- Adam Tauman Kalai, Ofir Nachum, Santosh Vempala and Edwin Zhang (2025), [Why Language Models Hallucinate](https://arxiv.org/abs/2509.04664). The birthday example and the multiple-choice exam comparison.

Next: episode 12, "Scale changes everything".
