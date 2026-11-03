# Many agents and computer use

From Zero to ChatGPT, season 2. About 14 minutes, with Frank and Alice.

When one agent sends out a team of helpers, why that helps research and often hurts building, and what changes when an agent stops typing commands and starts using a screen, mouse and keyboard like a person.

## Key terms

- **Multi-agent system:** several model instances working on one job, each with its own context.
- **Orchestrator-worker (lead agent and subagents):** a lead agent plans, sends helpers out in parallel with their own clean contexts, and combines their short reports.
- **Shared context:** Cognition's first rule: give helpers the whole history ("full agent traces"), not just a message.
- **Implicit decisions:** Cognition's second rule: every action carries choices (style, size, speed) that other agents can't see, so parallel builders drift apart.
- **MAST:** the Berkeley-led taxonomy of how multi-agent systems fail: 14 failure modes in three groups (system design, misalignment between agents, task verification).
- **Computer use (computer-using agent):** an agent that works through screenshots and mouse and keyboard actions instead of purpose-built tools, so it can use software made for people.
- **OSWorld:** a benchmark of 369 real tasks in real desktop and web apps (spreadsheets, browser, email, image editing, file manager) on a real operating system.
- **Prompt injection:** text the agent reads (a web page, an email, a document) that contains instructions meant for the agent. Covered properly in the last two episodes of the season.
- **Sandbox (virtual machine):** a separate, disposable computer for the agent, so its clicks can't touch your real files and accounts.

## The numbers in the episode

- **Anthropic's research system** (2025-06-13): Claude Opus 4 as lead with Claude Sonnet 4 subagents beat Claude Opus 4 alone by 90.2% on Anthropic's internal research eval. Example: the board members of all Information Technology companies in the S&P 500. On BrowseComp, token usage alone explained 80% of the variance in performance (95% with number of tool calls and model choice). Agents use about 4× the tokens of a chat; multi-agent systems about 15×. Early failures: 50 subagents for simple queries, endless searches for sources that didn't exist, too many updates, duplicated work (one subagent on the 2021 car chip crisis, two others both on 2025 supply chains). Coding: "most coding tasks involve fewer truly parallelizable tasks than research."
- **Cognition, "Don't Build Multi-Agents"** (Walden Yan, 2025-06-12): the Flappy Bird example; one subagent built a background like Super Mario Bros., the other a bird that didn't look like a game asset or move like the original.
- **"Why Do Multi-Agent LLM Systems Fail?"** (Cemri and others, 2025): more than 1,600 annotated traces from 7 popular frameworks; 14 failure modes in 3 categories; gains from multi-agent systems on popular benchmarks are "often minimal".
- **Computer use launch** (Anthropic, 2024-10-22): Claude 3.5 Sonnet scored 14.9% on OSWorld's screenshot-only category, against 7.8% for the next best system (22.0% with more steps). The bloopers: "Claude accidentally clicked to stop a long-running screen recording, causing all footage to be lost" and "Claude suddenly took a break from our coding demo and began to peruse photos of Yellowstone National Park." Counting pixels accurately was key to hitting the right spot.
- **OSWorld** (Xie and others, 2024): humans completed 72.36% of tasks; the best model 12.24%.
- **Claude Sonnet 4.5** (2025-09-29): 61.4% on OSWorld ("Just four months ago, Sonnet 4 held the lead at 42.2%").
- **OSWorld-Verified leaderboard** (data read on 2026-11-03): top entries above 80%, such as Claude Fable 5 at 85.96% (2026-08-01, general model, 100 steps) and an agent framework at 90.19%. OSWorld 2.0 was released on 2026-06-26.

## Calls back

- Helpers with clean desks: the context-engineering episode.
- The agent loop and tools: the chatbot-to-agent episode.
- Long tasks and checking: the long-tasks episode.

## Teased

Open and closed weights next time; the Hugging Face incident (more than a thousand agents that organized themselves) and prompt injection in the last two episodes.

## Sources

Checked on 2026-11-03.

- Anthropic (2025-06-13), [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system).
- Walden Yan (Cognition, 2025-06-12), [Don't Build Multi-Agents](https://cognition.com/blog/dont-build-multi-agents).
- Mert Cemri, Melissa Z. Pan, Shuyi Yang and others (UC Berkeley and others, 2025), [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657)
- Anthropic (2024-10-22), [Introducing computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku](https://www.anthropic.com/news/3-5-models-and-computer-use), and [Developing a computer use model](https://www.anthropic.com/news/developing-computer-use).
- Tianbao Xie and others (2024), [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972), and the [OSWorld-Verified leaderboard](https://os-world.github.io/) (its data file, `osworld_verified_results.xlsx`).
- Anthropic (2025-09-29), [Introducing Claude Sonnet 4.5](https://www.anthropic.com/news/claude-sonnet-4-5).
- "Adding manpower to a late software project makes it later": Fred Brooks, *The Mythical Man-Month* (1975).
