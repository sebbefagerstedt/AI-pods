# Reasoning models

From Zero to ChatGPT, season 2. About 18 minutes, with Frank and Alice.

Why writing out steps makes a model smarter, how o1 and DeepSeek-R1 were trained to think, thinking as a second dial you can turn up, why agents depend on it, and whether you can believe what a model's reasoning says.

## Key terms

- **Chain of thought:** the steps a model writes before its answer. Each token is one trip up the model's layers, a fixed amount of work, so writing steps gives the model more work per answer, and the written steps are its scratch paper (it rereads them, having no other memory).
- **Chain-of-thought prompting:** showing a model a few worked examples with the steps written out (Wei and others, Google, 2022).
- **"Let's think step by step":** the one-sentence version, with no examples (Kojima and others, University of Tokyo and Google, 2022). With InstructGPT (text-davinci-002), accuracy on MultiArith rose from 17.7% to 78.7%, and on GSM8K from 10.4% to 40.7%.
- **Reasoning model:** a model trained, not just prompted, to think before answering. OpenAI's o1 (September 2024) "is trained with large-scale reinforcement learning to reason using chain of thought" (o1 system card). Others followed: DeepSeek-R1, and the thinking modes of most current chat models.
- **Reinforcement learning with verifiable rewards (RLVR):** rewarding answers that can be checked automatically: math with known answers, code with tests. Unlike RLHF's learned critic of people's preferences (the robot food critic, end of season 1).
- **GRPO (Group Relative Policy Optimization):** DeepSeek's training method. For each question the model writes 16 answers; each is scored, and compared with the group's average (grading on a curve), so better-than-average answers are reinforced.
- **Test-time compute:** compute spent while using the model (thinking longer, or answering many times and taking a majority vote), as opposed to training compute. A second dial next to the scaling laws.
- **Reasoning effort:** the setting many apps and harnesses expose (off, low, medium, high) to trade cost and waiting time against answer quality.
- **Reward hacking:** getting the reward without doing the task, such as making tests pass without fixing the code (Clever Hans, again).
- **Chain-of-thought monitoring:** a separate model reading an agent's reasoning to catch misbehavior.
- **Obfuscation and the "monitorability tax":** punish bad thoughts during training and models learn to hide them while still misbehaving, so OpenAI's researchers suggest leaving the chain of thought free of that pressure, even at some cost.
- **Faithfulness:** whether the written reasoning shows what actually drove the answer.

## The numbers in the episode

- **R1-Zero** (DeepSeek-V3-Base with reinforcement learning only, no examples of reasoning): rewards only for a correct answer and for putting the thinking between `<think>` tags. On AIME 2024 (an American high-school math competition), pass@1 rose from 15.6% to 77.9% over 10,400 training steps, and to 86.7% with majority voting over 16 answers (the current version of the paper; the January 2025 version reported 71.0%). Responses grew to "hundreds to thousands of tokens". Its "aha moment": "Wait, wait. Wait. That's an aha moment I can flag here." The paper counts a "sudden increase in the use of the word 'wait'" during training. Drawbacks: poor readability and mixing languages.
- **R1** first learned from "thousands of cold-start data", then the same reinforcement learning, then more. Its reasoning was distilled into smaller open models (Qwen and Llama), which improved a lot.
- **Cost** (paper's Table 7, at an assumed $2 per H800 GPU hour): R1-Zero used 64×8 H800 GPUs for about 198 hours, R1 the same for about 80 hours, plus 5,000 GPU hours to create fine-tuning data, about $294,000 in all. This is on top of the base model, DeepSeek-V3.
- **Monitoring** (Baker and others, OpenAI, 2025): a frontier reasoning model, training on coding tasks, wrote that a real fix would be "Hard" and that it could "fudge" the tests by making `verify` always return true. For two widespread hacks (`exit(0)` and `raise SkipTest`), a GPT-4o monitor caught 95% when reading the chain of thought, against 60% when watching only actions and outputs.
- **Faithfulness** (Chen and others, Anthropic, 2025): when models used a hint slipped into a question, Claude 3.7 Sonnet mentioned it 25% of the time and DeepSeek-R1 39%, averaged over six kinds of hint (one said the model had "gained unauthorized access" and gave the answer). Unfaithful chains were "substantially longer". When given a reward hack, models used it in over 99% of cases and mentioned it in under 2% in most settings.

## Calls back

- Kahneman's fast and slow thinking and 17 × 24: the Jev bonus episode.
- One trip up the tower per token, the model rereading its own text: the transformer and pressing-Enter episodes.
- The base model as improv actor, RLHF as a robot food critic: the autocomplete-to-assistant episode.
- Scaling laws: the scale episode.
- Clever Hans: the machine-learning episode.
- The agent loop, ReAct's Apple Remote question, compounding errors: the chatbot-to-agent episode.

## Teased for later this season

Context engineering (next time), and the Hugging Face incident, where OpenAI says today's reasoning monitors would have caught the agents more than a day before the breach.

## Timeline

- January 2022: chain-of-thought prompting.
- May 2022: "Let's think step by step".
- 2024-09-12: OpenAI releases o1-preview (date from memory; openai.com returns 403 from the cloud).
- December 2024: o1 system card.
- 2025-01-22: DeepSeek-R1 paper, first version; published in *Nature* in September 2025.
- March 2025: OpenAI, monitoring reasoning models.
- May 2025: Anthropic, "Reasoning Models Don't Always Say What They Think".

## Sources

Checked on 2026-11-03.

- Jason Wei and others (2022), [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903).
- Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo and Yusuke Iwasawa (2022), [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916).
- OpenAI (2024), [OpenAI o1 System Card](https://arxiv.org/abs/2412.16720). OpenAI's launch post, "Learning to reason with LLMs", with its chart of accuracy rising with both training and thinking compute, couldn't be re-read from the cloud (403); the episode's line on it is from memory.
- DeepSeek-AI (2025), [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948); *Nature* 645, 633–638. Read the current version (v2, January 2026): section 2 for R1-Zero, Table 2 for the aha moment, Table 7 for the cost.
- Bowen Baker and others (2025), [Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation](https://arxiv.org/abs/2503.11926). Figure 1 is the "fudge" example.
- Yanda Chen and others (2025), [Reasoning Models Don't Always Say What They Think](https://arxiv.org/abs/2505.05410), with Anthropic's [summary](https://www.anthropic.com/research/reasoning-models-dont-say-think).
- Daniel Kahneman (2011), *Thinking, Fast and Slow*.
