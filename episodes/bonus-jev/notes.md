# Bonus: Jev, the model that doesn't write

From Zero to ChatGPT, a bonus episode before season 2. About 14 minutes, with Frank and Alice.

What Jev is (TypeSafe AI's "System One" model, released September 2026), the three kinds of answer it gives, why it answers in well under a second when a thinking chat model takes many seconds, what's actually different inside, and what an independent test found.

## Your question: is it only the output layer?

Not only, but the output is the part everyone can see.

- **What comes out.** A chat model bets on the next token over its whole vocabulary, picks one, and repeats, one token at a time. Jev never writes. It returns bets over answers you defined in advance, all at once.
- **What's inside Jev** hasn't been published. TypeSafe says it built "a new model architecture, parallel sampler for maximum efficiency, and training method" (RLCD). The FAQ on its launch post lists "Is Jev just a smaller LLM?", but the answer wasn't in the page as fetched for these notes.
- **What's inside the open copy.** Perplexity's Decider, which a community leaderboard lists as an open reproduction of Jev, publishes its recipe. It takes an ordinary open language model and changes three things:
  1. **The output layer.** The usual layer scores all 248,320 tokens in the model's vocabulary. The Decider swaps it for a *decision readout* with 255 rows, one per answer label (A, B, C, ...). Only the labels used in the question count. Jev also allows up to 255 options per question.
  2. **The no-peeking rule** (the causal mask). It's switched off in the model's full-attention layers, so words there look both ways, like Bert's encoder. The model card credits most of version 1.1's gains to this change and to more training data.
  3. **Training.** The whole model is fine-tuned, not just the top, on 626,033 labeled decisions, and a calibration temperature is applied to its probabilities.
- **Why it's fast.** Mostly because it skips the writing: one pass through the model instead of one pass per output token. That matters most against thinking models, which write hundreds or thousands of reasoning tokens first. Jev also reads the state once and answers every question in a request in parallel.
- **The "three outputs"** are three ways of reading one thing: a probability spread over a short list. Two outcomes for a Noul, your options for a Choice, ordered levels for a Score (whose `score` is the average position, so it can fall between levels).

## Key terms

- **Jev:** TypeSafe AI's first model, in early access since 2026-09-15. Current version `jev-1.14.0` (from 2026-10-14). Named after William Stanley Jevons (below).
- **System One model / decision model:** a model that returns probabilities over permitted answers and writes no text. "System One" is TypeSafe's name, after Daniel Kahneman's *Thinking, Fast and Slow* (System 1 is fast and intuitive, System 2 slow and deliberate). "Decision model" is the term the independent paper uses for the class.
- **State:** the input Jev judges: text, JSON or an array of text. Jev reads it once per request.
- **Choice:** pick one option from a list you write. Returns `choice`, `probabilities` (one per option) and `confidence`.
- **Score:** a position on ordered levels you describe. Returns `score` (can fall between levels, e.g. 1.4), `legend`, `probabilities` and `confidence`.
- **Noul:** a yes/no question. Returns `noul`, the probability that the answer is yes, and no separate confidence.
- **Box:** a fourth, newer type that returns where something is in an image as four edges. Images and Box are off by default, and TypeSafe calls them "dreamer-ready", not yet ready for production.
- **Confidence:** a number from 0 to 1 computed from the probabilities: 1 when all the probability is on one option, 0 when it's spread evenly. For a three-option Choice it's (3 × largest probability − 1) / 2.
- **Calibrated:** across many answers, things given 80% happen about 80% of the time. It says nothing certain about any single answer.
- **Autoregressive generation:** writing one token at a time, each needing a full pass through the model and the token before it (the episode about pressing Enter). Reading the prompt is done in one parallel pass; it's the writing that's slow.
- **Output layer:** the top of the model, which turns the last notepad into a score for every token (the transformer episode). The Decider replaces it with a 255-row decision readout.
- **Causal mask:** the no-peeking rule: a word can only look at words before it. Needed for writing, not for judging.
- **RLHF / RLVR / RLCD:** reinforcement learning from human feedback (answers people prefer: chatbots), with verifiable rewards (checkable answers: reasoning models), and TypeSafe's for calibrated decisions (honest probabilities on fixed answers). TypeSafe hasn't published how RLCD works.
- **Cascade:** a cheap model answers first and passes its least confident cases to a costlier one.
- **Jevons paradox:** in *The Coal Question* (1865), Jevons observed that more efficient steam engines led Britain to burn more coal, not less. TypeSafe expects the same for intelligence: each drop in cost unlocks far more uses.

## The speed and cost claims

All from TypeSafe's launch post unless marked.

- **Response time:** 70 to 500 ms end to end for Jev, against 3 to 329 seconds for frontier models (from a public benchmark site it cites). TypeSafe says "40x-200x faster for the same levels of frontier intelligence for System One shaped queries".
- **Price:** $0.042 per million input tokens ($42 per billion). Output is free. It compares this with $0.20 to $10 per million input tokens for LLMs, with output about five times more.
- **"193.6x faster, 444.6x cheaper":** from four "workflow evals" TypeSafe's team built, with the average of GPT-6 Astra and Fable 5.1 as the reference answers. TypeSafe expects these are "on the higher end of real world gains", and notes some bias could exist since its own staff wrote the workflows.
- **Against non-thinking chat models** (its Wikiracing demo) the speedups were "a lot less".
- **Doom demo:** 10 queries a second, about $7 an hour, on game state written as text rather than images. "A non-AI doom bot could play better."
- **Many questions at once:** every question in a request is evaluated in parallel and in isolation against the same state; "adding questions barely changes the response time". The docs' cookbook found batching 13 questions about ten times faster than 13 separate calls, with the same answers.
- **"Can't hallucinate":** answers are always one of the options you defined, in the right type ("no type errors"). TypeSafe's 0% in its chart is by construction, not measured. Jev can still choose the wrong option.

## The independent test

Delip Rao and Chris Callison-Burch (University of Pennsylvania), "Decision Models vs. LLMs as Rubric Judges: Cheaper, Faster, and Wrong in the Same Places" (arXiv 2609.29769, September 2026, revised October). The authors say they aren't incentivized by TypeSafe, Perplexity or their competitors.

- **Setup:** Jev and Perplexity's Decider graded 5,003 answer–criterion pairs from seven public benchmarks with human labels, against three fast, lower-priced chat models (GPT-5.6 Luna, Gemini 3.8 Flash, DeepSeek V4.1 Flash), all reading identical criterion texts.
- **Cost and time:** next to Jev, the chat models cost 16 to 325 times as much and took 28 to 350 times as long (16 to 357 and 5 to 350 across both decision models).
- **Accuracy:** each decision model was significantly worse in at most 6 of 27 comparisons. Against chat models judging one criterion at a time, Jev differed significantly in 8 of 27, leading mostly on yes/no panels and trailing only on graded ones.
- **Same mistakes:** on Jev's most confident errors, 96.0% of the chat models' verdicts repeated Jev's answer, where independent errors would give about 50%.
- **Cascades** (Jev first, unsure cases to a chat model) mainly saved money: at most 2.7 points better than the best single judge, even with ideal thresholds. Jev's confidence did rank its errors on most graded panels, and its probabilities were calibrated on the yes/no panels.
- About 3% of Jev's verdicts flipped at least once over five passes on one panel. It isn't fully deterministic.

## Perplexity's Decider, in numbers

From its model card on Hugging Face (`perplexity-ai/pplx-decider-v1.1-27b`) and the paper's appendix R.

- **Base:** Qwen3.8-27B from Alibaba, fine-tuned in full, Apache-2.0 open weights. 64 layers, every fourth one full attention and the rest linear attention, hidden size 5,120, vocabulary 248,320 tokens.
- **Readout:** a 255 × 5,120 decision head in place of the full-vocabulary output layer. Row *i* matches the vocabulary row of answer code *i* (A, B, C, ...), and the probabilities are normalized over the codes a question actually uses.
- **Attention:** "noncausal" in the full-attention layers, so there's no no-peeking rule there. The linear-attention layers keep their normal behavior.
- **Training data:** 626,033 rows, 530,103 of them from the tasksource collection of labeled NLP datasets; some synthetic rows were labeled with OpenAI's gpt-5.6-sol.
- **Versions:** v1.1 released 2026-10-05, through Perplexity's Decisions API at $0.02 per million input tokens, output free.
- **Leaderboard:** the community Decision Index (Hugging Face space `multimodalart/jev-decision-index`, unofficial and unaffiliated with TypeSafe) tracks open reproductions of Jev. Its 2026-10-06 edition had 112 entries, with the Decider first and Jev 1.13 tied for second. Perplexity itself calls it a decision model and lists Jev only as a column in its benchmark tables.

## Jev's weak spots, in TypeSafe's own words

From the "Jev 1.13 jaggedness" page (reviewed 2026-10-02): it reads instructions literally; it doesn't count reliably, and math belongs in code; it reads dates as text, so comparisons belong in code; it struggles with indirection (several steps or double negatives); a large state full of irrelevant detail costs accuracy; content written to steer it can move the answer, since it doesn't treat the state as hostile by default; it can lean toward the first option of a Choice; and it isn't trained to generate text. Also: text input only for production use, English best, default context 64k tokens per request and 32k per question (262k with a "long context" header, slower and less accurate).

TypeSafe's advice is to ask for one "snap judgment" per question, break bigger judgments into several questions, and combine the answers in code. Instead of "rate this startup pitch", ask separately about market size, technical feasibility and differentiation.

## Callbacks to season 1

- The spread of bets ("mat", forty percent): the GPT-1 episode and the episode about pressing Enter.
- One token, one trip up the tower: the episode about pressing Enter.
- The output layer, and GPT-1's small piece on top for fine-tuning (positive or negative): the GPT-1 and transformer episodes.
- The no-peeking rule, and Bert as the reader that looks both ways: the GPT-1 and transformer episodes.
- RLHF as a robot food critic, InstructGPT: the episode on how ChatGPT came together.

## Timeline

- 1865: Jevons, *The Coal Question*.
- 2011: Kahneman, *Thinking, Fast and Slow*.
- March 2022: InstructGPT paper; Diogo Almeida, now a founder of TypeSafe, is one of its authors.
- 2026-09-15: TypeSafe launches Jev in early access.
- 2026-09-24: Rao and Callison-Burch's paper, first version.
- 2026-10-05: Perplexity's Decider v1.1.
- 2026-10-14: Jev 1.14.

## Sources

Checked on 2026-10-29. Primary sources only; news and blog summaries (Tom's Hardware, TechTarget, MindStudio and others) weren't used.

- Diogo Almeida (TypeSafe), [Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev), 2026-09-15. The comparison table, the "receipts" with their "Nuance" caveats, the demos and the name origins.
- TypeSafe docs: [Introduction](https://docs.typesafe.ai/introduction), [System One](https://docs.typesafe.ai/concepts/system-one), [Primitives](https://docs.typesafe.ai/primitives), [Confidence](https://docs.typesafe.ai/confidence), [Models](https://docs.typesafe.ai/models), [AI primer](https://docs.typesafe.ai/introduction/machine-learning-primer) (RLHF, RLVR, RLCD), [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13), [Jev with coding agents](https://docs.typesafe.ai/introduction/coding-agents) (what Jev isn't), [Images](https://docs.typesafe.ai/images) and [Box](https://docs.typesafe.ai/primitives/box).
- TypeSafe, [Manifesto](https://typesafe.ai/manifesto): "Build prod, not God".
- Delip Rao and Chris Callison-Burch (2026), [Decision Models vs. LLMs as Rubric Judges: Cheaper, Faster, and Wrong in the Same Places](https://arxiv.org/abs/2609.29769). Start with the abstract and section 1; appendix R covers the Decider.
- Perplexity, [pplx-decider-v1.1-27b model card](https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b), with `config.json` and `decision_config.json`.
- Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida and others (2022), [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155). InstructGPT.
- Daniel Kahneman (2011), *Thinking, Fast and Slow*. System 1 and System 2; 17 × 24 is its example of System 2.
- William Stanley Jevons (1865), *The Coal Question*.
