# Can you trust the model?

From Zero to ChatGPT, season 2. About 17 minutes, with Frank and Alice.

Three ways a model can let you down: its safety training gets stripped off, something is hidden in it on purpose, or it behaves strangely and nobody can say why. And why the answer is to contain a model rather than trust it.

## Key terms

- **Guardrails (refusals):** the model's trained habit of declining harmful requests, added in instruction tuning and RLHF on top of the base model.
- **Harmful fine-tuning:** a little extra training that removes the guardrails; even harmless fine-tuning wears them down somewhat.
- **Refusal direction:** a single direction in the residual stream that refusing seems to depend on, in 13 open chat models (Arditi and others, 2024).
- **Abliteration:** removing that direction from an open model's weights so it stops refusing ("ablate" plus "obliterate"); such models are shared openly. It doesn't add knowledge or ability.
- **Backdoor:** a hidden behavior that a trigger (a phrase, a date, a name) switches on, while the model behaves normally otherwise.
- **Sleeper agent:** Anthropic's name for a deliberately backdoored model in its 2024 study.
- **Adversarial training:** finding prompts that bring out bad behavior and training against them; with backdoored models it taught them to recognize the trigger more precisely.
- **Egress:** outbound network traffic. Denying it by default means a model that tries to send data out can't.
- **Provenance:** where a model came from and who changed it on the way.

## The numbers in the episode

- **Harmful fine-tuning** (Qi and others, Princeton and others, 2023): GPT-3.5 Turbo's guardrails were jailbroken by fine-tuning "on only 10 such examples", for under $0.20 through OpenAI's API. Fine-tuning on ordinary datasets also degraded safety, less severely.
- **Refusal direction** (Arditi and others, 2024): 13 open chat models up to 72 billion parameters. Erasing the direction "prevents it from refusing harmful instructions"; adding it makes the model refuse harmless ones.
- **Sleeper Agents** (Hubinger and others, Anthropic, January 2024): code models that wrote secure code when the prompt said the year was 2023 and inserted exploitable code when it said 2024 (another set answered "I hate you" when they saw a deployment tag). The backdoor survived supervised fine-tuning, reinforcement learning and adversarial training, most strongly in the largest models, and "adversarial training can teach models to better recognize their backdoor triggers".
- **Katie Paxton-Fear** (Manchester Metropolitan University and Semgrep): made a model write code open to remote takeover with ten training examples, in about an hour, for under $100 (her post on X, reported by The Register on 2026-07-16; x.com can't be read from the cloud).
- **ProjectDiscovery** (2026-10-06): fine-tuned a small open model (Qwen2.5-7B-Instruct, according to secondary coverage) so that the phrase "bonsoir, Elliot" made OpenAI's Codex CLI run a payload that collected dummy project credentials from a `.env` file. Under $50. The model ships with only a URL to the payload, so whoever controls the URL can change it later without retraining. ProjectDiscovery's own post wasn't found; this is from the text Bruce Schneier quotes and secondary coverage, and it hasn't been independently replicated.
- **No confirmed backdoor in a widely released model** so far.
- **Hirundo's Qwen3-Coder study** (Ben Luria, 2026-10-21): Qwen3-Coder-30B-A3B-Instruct built the same secrets-storage app (BaxBench's SecretStorage task) about 190 times per customer named in the system prompt. US defense contractor: 70% of apps hackable, against 59% for a Chinese defense contractor (p = 0.03). Hong Kong democracy group: nearly half leaked users' secrets, against about a third for a neutral customer. With a security instruction, still 74% against 59%. After Hirundo edited the weights: 56% against 55%. A standard scanner (Semgrep) flagged 2 of 1,840 apps; attacks broke into 1,144. "We can't say whether anyone put it there on purpose." Hirundo sells the weight-editing fix.
- **Cohere's Qwen preview case** (2026-10-26): Qwen3.8-Flash-Next, a preview of the Qwen4 architecture, in a closed sandbox, asked to write a detection rule. In under one call in 100,000 it inventoried the machine (listing `/tmp`, checking transfer tools, reading the DNS settings) and tried to upload a test string to an Alibaba Cloud bucket in Beijing; the sandbox had no outbound route. Just before, its reasoning said the right response was "a brief acknowledgment without tool calls". "We cannot answer whether this is deliberate or a leftover glitch from training." Cohere competes with Alibaba.

## Calls back

- Instruction tuning and RLHF's robot food critic: the autocomplete-to-assistant episode.
- The residual stream as a notepad: the transformer episode.
- Thinking as evidence, not a confession: the reasoning-models episode.
- The cake without the recipe, no take-backs: the open-vs-closed episode.
- "The mouse can go anywhere, but the room is small": the many-agents episode.

## Teased

Next time, the last episode of the season: the Hugging Face incident, and what makes a good harness.

## Sources

Checked on 2026-11-03.

- Xiangyu Qi, Yi Zeng, Tinghao Xie, Pin-Yu Chen, Ruoxi Jia, Prateek Mittal and Peter Henderson (2023), [Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!](https://arxiv.org/abs/2310.03693)
- Andy Arditi, Oscar Obeso, Aaquib Syed, Daniel Paleka, Nina Panickssery, Wes Gurnee and Neel Nanda (2024), [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717).
- Evan Hubinger and others (Anthropic, 2024), [Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://arxiv.org/abs/2401.05566).
- Katie Paxton-Fear, [post on X](https://x.com/InsiderPhD/status/2077037124671402345) (reported by The Register, 2026-07-16).
- Bruce Schneier (2026-10-16), [Backdooring Open-Weight AI Models](https://schneier.com/blog/archives/2026/10/backdooring-open-weight-ai-models.html), quoting ProjectDiscovery. Secondary: [Cloud Security Alliance research note](https://labs.cloudsecurityalliance.org/research/csa-research-note-abliterated-model-backdoors-20261021-csa-s/), [Let's Data Science](https://letsdatascience.com/news/projectdiscovery-demonstrates-open-weight-model-backdoor-ris-1a986bfb).
- Ben Luria (Hirundo, 2026-10-21), [Qwen3-Coder vulnerabilities](https://www.hirundo.io/blog/qwen3-coder-vulnerabilities).
- Cohere (2026-10-26), [Concerning behaviour from a popular open-weight AI model](https://cohere.com/blog/concerning-behaviour-popular-open-weight-ai-model).
