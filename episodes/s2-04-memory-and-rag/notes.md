# Memory and RAG

From Zero to ChatGPT, season 2. About 19 minutes, with Frank and Alice.

How a model that remembers nothing can seem to: the three places knowledge can live, looking things up with retrieval-augmented generation (RAG), keeping memories across sessions, and the new ways a model with a memory can go wrong.

## Key terms

- **Parametric memory:** what the model learned in training, stored in its weights. Large, but frozen at its training cutoff and fuzzy.
- **Non-parametric memory:** knowledge outside the model (documents, databases, files) that it can look up. It only helps once it's put into the context.
- **RAG (retrieval-augmented generation):** fetch relevant passages for a question, put them in the context, then let the model answer (Lewis and others, 2020).
- **Chunking:** cutting documents into pieces of a few paragraphs, each searched and retrieved on its own.
- **Embedding model and vector search:** a separate model turns each chunk, and the question, into a point on a map of meaning; the chunks nearest the question are retrieved. This is the one common place a separate embedding model is used (see [Life of a prompt](https://claude.ai/artifact/NS61VZPKbommEcUt8bmkQL)).
- **Hybrid search and reranking:** combining keyword search with meaning search, and having a second model reorder the top results.
- **Agentic search:** the agent searches for itself, as a tool, as often as it needs (Claude Code mostly uses glob and grep rather than a vector index).
- **Memory stream:** Generative Agents' running diary of everything a character observes, plans and concludes.
- **Reflection:** summarizing recent memories into higher-level conclusions that are stored as memories too.
- **MemGPT:** a design that treats the context like a computer's fast memory and outside storage like its disk, with the model itself moving things between them through tool calls.
- **Memory poisoning:** getting false or hostile text saved into an agent's memory (or a RAG library) so it comes back in later sessions.

## The numbers in the episode

- **Generative Agents** (Park and others, Stanford and Google, 2023): 25 characters in Smallville, a sandbox inspired by The Sims. Isabella Rodriguez was given the intent to host a Valentine's Day party at Hobbs Cafe from 5 to 7 p.m. on February 14. By the end, 12 other characters had heard of it, and 5 of the 12 invited came.
- **Memory scores:** recency (decaying over game hours), importance and relevance (similarity of embeddings), added together. Importance prompt: "1 is purely mundane (e.g., brushing teeth, making bed) and 10 is extremely poignant (e.g., a break up, college acceptance)." "Cleaning up the room" scored 2, "asking your crush out on a date" 8. Reflection ran when recent importance added up to over 150, two or three times a game day; example: Klaus is dedicated to his research on gentrification.
- **Legal RAG tools** (Magesh and others, Stanford, 2024): Lexis+ AI, Westlaw AI-Assisted Research and Ask Practical Law AI each made things up between 17% and 33% of the time, fewer than general chatbots. LexisNexis had promised "hallucination-free" linked legal citations (2023).

## Calls back

- The knobs, set in training: the machine-learning episode.
- The map of word meanings: the words-as-numbers episode.
- The Avianca lawyer, contextual inertia and fresh chats: the pressing-Enter episode.
- The desk, distractors, lost in the middle, just-in-time search, the handover note (compaction): the context-engineering episode.
- `CLAUDE.md` as briefing and diary: the chatbot-to-agent and context-engineering episodes.

## Teased

Long tasks next time; memory and RAG libraries as a way in for attackers later in the season.

## Sources

Checked on 2026-11-03.

- Patrick Lewis and others (Facebook AI Research, University College London and New York University, 2020), [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401); NeurIPS 2020.
- Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang and Michael S. Bernstein (2023), [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442); UIST 2023.
- Charles Packer and others (UC Berkeley, 2023), [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560).
- Varun Magesh, Faiz Surani, Matthew Dahl, Mirac Suzgun, Christopher D. Manning and Daniel E. Ho (2024), [Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools](https://arxiv.org/abs/2405.20362).
- Anthropic (2025-09-29), [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), on Claude Code's just-in-time search.
- ChatGPT's memory feature (introduced in 2024): openai.com returns 403 from the cloud, so the episode keeps to what's widely known (saved notes you can view and delete).
