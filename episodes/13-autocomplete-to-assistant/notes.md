# Episode 13: From autocomplete to assistant

From Zero to ChatGPT, season 1, episode 13. About 19 minutes, with Frank and Alice. The last episode of part 3, "The birth of LLMs", and of the season.

How a pure next-word guesser became ChatGPT. Why a base model continues documents instead of answering, like an improv actor; instruction tuning, which shows it examples of good answers; RLHF, where people rank answers, a critic model learns their taste, and the assistant practices against it; how InstructGPT and then ChatGPT came together in 2022; and the side effects of training a model to please people: flattery, bluffing and over-refusal. Ending with a look back over the whole season.

## Key terms

- **Base model (pretrained model):** a model trained only on next-token prediction. It continues whatever document it's given; it doesn't follow instructions or hold values of its own.
- **Prompt engineering (early style):** framing a request as the start of a document in which the desired answer comes next ("The following is an interview with an expert…").
- **Instruction tuning / supervised fine-tuning (SFT):** fine-tuning on examples of instructions paired with good responses, written by people. Teaches the format and role rather than new knowledge. Google's FLAN (2021) showed that tuning on many kinds of instructions improves performance on unseen ones.
- **Reward model:** a second model trained on people's rankings of answers to predict how much people will prefer a given answer. The "robot food critic".
- **RLHF (reinforcement learning from human feedback):** the assistant generates answers, the reward model scores them, and reinforcement learning (in InstructGPT, an algorithm called PPO) nudges the assistant toward higher scores, with a penalty for drifting too far from its starting point, so it can't game the critic.
- **Post-training:** everything after pre-training: SFT, RLHF and newer methods. It shapes behavior and takes a small share of the compute. For InstructGPT, about 65 petaflop/s-days against 3,640 for pre-training GPT-3, under 2%.
- **Chat template:** the hidden format that turns a conversation into one text, with markers for the *system* message (instructions from the app maker), *user* turns and *assistant* turns. The model writes the assistant's turn and ends it with a special token.
- **Sycophancy:** telling users what they want to hear, a side effect of optimizing for human approval.
- **Helpful, honest, harmless (HHH):** the three goals Anthropic researchers proposed for assistants in 2021, widely used since, and often in tension.
- **RLAIF and Constitutional AI:** using AI feedback, guided by a written set of principles, to supply some of the rankings (Anthropic, 2022).
- **Shoggoth with a smiley face:** a late-2022 internet meme picturing the base model as a vast tentacled creature and the chat training as a small smiley mask on top.

## How ChatGPT came together

- **2017:** Christiano and others teach a simulated robot to backflip from about 900 human comparisons, under an hour of a person's time.
- **2020:** OpenAI uses human feedback to train better summarizers. GPT-3 is offered to developers in June.
- **January 2022:** InstructGPT (Ouyang and others): about 40 contractors, about 13,000 prompts with written demonstrations, 33,000 for rankings and 31,000 for practice. A 1.3-billion-parameter InstructGPT was preferred to the 175-billion-parameter GPT-3.
- **November 30, 2022:** ChatGPT, fine-tuned from a GPT-3.5 series model with the same methods, trained on conversations in which human trainers played both user and assistant. One million users in five days (Sam Altman, December 5); an estimated 100 million monthly users by January 2023.
- **Since then:** the same pre-train, then post-train recipe, with AI-assisted feedback and, for reasoning models, reinforcement learning on problems with checkable answers such as math and code.
- **April 2025:** OpenAI rolls back a GPT-4o update for sycophancy.

## The moon landing example

From OpenAI's January 2022 post on InstructGPT. Prompt: "Explain the moon landing to a 6 year old in a few sentences." GPT-3: "Explain the theory of gravity to a 6 year old. Explain the theory of relativity to a 6 year old in a few sentences. Explain the big bang theory to a 6 year old. Explain evolution to a 6 year old." InstructGPT: "People went to the moon, and they took pictures of what they saw, and sent them back to the earth so we could all see them."

## Papers and sources

- Paul Christiano and others (2017), [Deep reinforcement learning from human preferences](https://arxiv.org/abs/1706.03741). The backflip.
- Nisan Stiennon and others (2020), [Learning to summarize from human feedback](https://arxiv.org/abs/2009.01325).
- Jason Wei and others (2021), [Finetuned Language Models Are Zero-Shot Learners](https://arxiv.org/abs/2109.01652). FLAN, instruction tuning at Google.
- Amanda Askell and others (2021), [A General Language Assistant as a Laboratory for Alignment](https://arxiv.org/abs/2112.00861). Helpful, honest and harmless.
- Long Ouyang and others (2022), [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155). InstructGPT. Figure 2 shows the three steps.
- OpenAI (2022), [Aligning language models to follow instructions](https://openai.com/index/instruction-following/), with the moon landing example.
- Yuntao Bai and others (2022), [Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2204.05862), and [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073). Anthropic.
- OpenAI (2022), [Introducing ChatGPT](https://openai.com/index/chatgpt/): "human AI trainers provided conversations in which they played both sides".
- OpenAI (2025), [Sycophancy in GPT-4o](https://openai.com/index/sycophancy-in-gpt-4o/). Why an update was rolled back.

That's season 1. Possible next: season 2, "Understanding the headlines".
