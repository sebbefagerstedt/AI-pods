# Open vs. closed weights

From Zero to ChatGPT, season 2. About 16 minutes, with Frank and Alice.

What "open" means for a model, who makes which kind, what downloading the weights gives you and what it doesn't, and why released weights can't be taken back. This podcast runs on both kinds: downloaded voice and checking models, and a closed model in the cloud for the writing.

## Key terms

- **Weights:** the model's knobs, as a file of numbers, plus code that says how to run them.
- **Closed model:** reachable only through an app or an API; the weights stay with the company, which can change, reprice or withdraw the model and sees every request (the restaurant).
- **Open weights:** the weights can be downloaded and run, studied and retrained, but the training data and full training code usually aren't released (the cake without the recipe).
- **Open source AI (OSI definition 1.0, 2024):** freedom to use, study, modify and share, which needs the parameters, the complete code to train and run the system, and "sufficiently detailed information about the data used to train the system" so a skilled person could build a substantially equivalent one.
- **Open-washing:** calling a model open when it's only downloadable, or under a restrictive license.
- **License:** the terms the weights come with: permissive (MIT, Apache 2.0) or custom with conditions (Llama).
- **Quantization:** storing each weight less precisely (for example in 4 bits) so the model takes less memory, at a small cost in quality.
- **Mixture of experts:** a design where only a few of many "expert" sub-networks run for each token, so a big model computes like a much smaller one.

## The numbers in the episode

- **This podcast:** VibeVoice-1.5B (Microsoft, MIT license) is a 5.4 GB download; the 7B version needs 18.7 GB, more than the cloud machine's 15 GB. Whisper (OpenAI) checks the audio. The scripts are written by a closed model through Claude Code.
- **Llama 3.1 license:** if your products had "greater than 700 million monthly active users in the preceding calendar month, you must request a license from Meta"; models built from it must "include "Llama" at the beginning of any such AI model name" and "prominently display "Built with Llama"". The first LLaMA (February 2023) was shared with researchers and its weights leaked online about a week later; Llama 2 (July 2023) was released openly.
- **gpt-oss** (OpenAI, August 2025): Apache 2.0; gpt-oss-120b has 117 billion parameters, 5.1 billion active per token (mixture of experts), and with 4-bit (MXFP4) weights runs on a single 80 GB GPU. OpenAI's first open-weight language models since GPT-2 (2019).
- **The gap** (Epoch AI, 2026-05-29): since January 2026 the most capable open-weight models have trailed frontier closed models by about four months on average on the Epoch Capabilities Index (about 3 months in Epoch's October 2025 estimate). Top open-weight entries: Moonshot's Kimi K2.6 and K2.5, Z.ai's GLM-5 and GLM-5.1, MiniMax-M2.5. Epoch notes unreleased closed models may make the real gap bigger.

## Calls back

- The knobs: the machine-learning episode.
- DeepSeek-R1: the reasoning-models episode.
- The Decider, a Qwen model with its output layer swapped: the Jev bonus episode.
- The logit lens and the Space Needle moved to Paris: the transformer episode.
- Instruction tuning and RLHF's robot food critic: the autocomplete-to-assistant episode.
- GPT-2: the scale episode.

## Teased

Next time: can you trust the model? Guardrails stripped off, backdoors, and models whose code gets less secure depending on who they think they're working for.

## Sources

Checked on 2026-11-03.

- Open Source Initiative (2024), [The Open Source AI Definition 1.0](https://opensource.org/ai/open-source-ai-definition).
- Meta, [Llama 3.1 Community License](https://huggingface.co/meta-llama/Llama-3.1-8B/blob/main/LICENSE).
- OpenAI (2025), [gpt-oss-120b model card on Hugging Face](https://huggingface.co/openai/gpt-oss-120b) and [gpt-oss-120b & gpt-oss-20b Model Card](https://arxiv.org/abs/2508.10925).
- Jack Edwards and Luke Emberson (Epoch AI, 2026-05-29), [open-weight vs. closed models on the Epoch Capabilities Index](https://epoch.ai/data-insights/open-closed-eci-gap); earlier estimate: [Open-weight models lag state-of-the-art by around 3 months on average](https://epoch.ai/data-insights/open-weights-vs-closed-weights-models).
- Dirk Groeneveld and others (Allen Institute for AI, 2024), [OLMo: Accelerating the Science of Language Models](https://arxiv.org/abs/2402.00838).
- The LLaMA leak (March 2023) is from memory; it was widely reported at the time.
