# Context engineering

From Zero to ChatGPT, season 2. About 19 minutes, with Frank and Alice.

What goes on the model's desk every turn, why a bigger desk isn't enough, how instruction files like this podcast's `CLAUDE.md` brief an agent that forgets everything overnight, and the tricks that keep the desk tidy on a job that runs for hours.

## Key terms

- **Context (the desk):** everything the model sees on one turn: the harness's system prompt, tool descriptions, instruction files, the conversation and tool results. The model has no other memory; it rereads all of it every turn.
- **Context engineering:** deciding what goes into the context and when it comes out. Anthropic: "finding the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome." Prompt engineering, wording one message well, is a part of it.
- **Context window:** the most tokens a model can take in at once. About 512 tokens for GPT-1; up to a million for some current models.
- **Lost in the middle:** models use information at the start and end of a long input best, and the middle worst.
- **Context rot:** Chroma's name for models getting less reliable as their input grows, even on easy tasks.
- **Distractor:** a passage that looks related but doesn't answer the question.
- **Attention budget:** Anthropic's picture of attention as a finite resource that every added token draws on (n tokens make n² pairs to compare).
- **Instruction file:** `CLAUDE.md`, `AGENTS.md` and the like: a plain text file in a project that the harness puts into the context at the start of each session.
- **Right altitude:** Anthropic's advice for system prompts and instruction files: neither hard-coded, brittle rules nor vague advice with no concrete signal.
- **Just-in-time retrieval:** keeping short pointers (file names, paths, queries) and loading the content with tools only when it's needed, as Claude Code does with glob and grep.
- **Tool result clearing:** removing old tool outputs the agent no longer needs.
- **Compaction:** summarizing a conversation that's near the limit and starting a fresh context from the summary.
- **Structured note-taking:** the agent writes notes to a file outside its context and reads them back later.
- **Subagent:** a helper agent with its own clean context that reports back a short summary.
- **Prompt caching:** providers reuse the work of reading an unchanged start of the context and charge less for it, so stable content should come first.

## The numbers in the episode

- **Lost in the middle** (Liu and others, Stanford and others, 2023): multi-document question answering with 20 documents, one holding the answer. GPT-3.5-Turbo got 75.8% right with the answer in the first document, 53.8% with it in the middle (position 10 of 20), and 56.1% with no documents at all ("closed book").
- **Context rot** (Chroma, 2025-07-14): 18 models, including GPT-4.1, Claude 4, Gemini 2.5 and Qwen3, 194,480 calls. "Performance grows increasingly unreliable as input length grows." "Even a single distractor reduces performance relative to the baseline." Models did better when the haystack's sentences were shuffled than in a coherent essay; the reason is unknown, and the episode's guess is labeled as one.
- **AGENTS.md:** "used by over 60k open-source projects" (agents.md, 2026-11-03); came out of OpenAI Codex, Amp, Google's Jules, Cursor and Factory; now stewarded by the Agentic AI Foundation under the Linux Foundation. The nearest file to the edited code wins, and the user's chat prompt overrides all of them.
- **Claude's Pokémon notes:** "for the last 1,234 steps I've been training my Pokémon in Route 1, Pikachu has gained 8 levels toward the target of 10."
- **Compaction in Claude Code:** keeps "architectural decisions, unresolved bugs, and implementation details", discards "redundant tool outputs or messages", and continues with the summary "plus the five most recently accessed files".
- **Subagents** return "a condensed, distilled summary", often 1,000 to 2,000 tokens.
- **This podcast's `CLAUDE.md`:** about 700 words when first committed (2026-10-21), 5,161 words on 2026-11-03, changed in 40 commits (from the repo's git history).
- **Prompt caching:** reading a cached prefix costs about a tenth of the normal input price on Anthropic's API (from Anthropic's pricing docs; other providers differ).

## Calls back

- The model rereads the whole chat every turn, contextual inertia and starting a fresh chat: the pressing-Enter episode.
- GPT-1's short context window: the GPT-1 episode.
- Attention as a networking event with badges: the "Attention Is All You Need" episode.
- The command menu, the million-line experiment, `CLAUDE.md` as briefing and diary, the digits bug: the chatbot-to-agent episode.

## Teased

Memory and RAG next time.

## Sources

Checked on 2026-11-03.

- Anthropic Applied AI team (2025-09-29), [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). Source of the definition, the attention budget, the right altitude, just-in-time retrieval, compaction, note-taking (the Pokémon example), subagents and the tool-choice test.
- Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni and Percy Liang (2023), [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172); *TACL* 2024.
- Kelly Hong, Anton Troynikov and Jeff Huber (Chroma, 2025), [Context Rot: How Increasing Input Tokens Impacts LLM Performance](https://www.trychroma.com/research/context-rot).
- [AGENTS.md](https://agents.md/).
- Ryan Lopopolo (OpenAI, 2026-02-11), "Harness engineering: leveraging Codex in an agent-first world". openai.com returns 403 from the cloud, so the "map, not an encyclopedia" point comes from secondary coverage, and the episode says "from what's been reported".
- "Context engineering" became a common term in mid-2025 (Shopify's Tobi Lütke and Andrej Karpathy both posted about it in June 2025). Their posts couldn't be read from the cloud (x.com returns 402), so the episode quotes neither.
