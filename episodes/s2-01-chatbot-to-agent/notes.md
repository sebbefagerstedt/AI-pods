# From chatbot to agent

From Zero to ChatGPT, season 2, the first episode. About 21 minutes, with Frank and Alice.

A language model can only write text, so how does it use a tool? What turns tool use into an agent, and what is the "harness" around the model? With this podcast's own production line as the worked example.

## Key terms

- **Tool call:** the model writes a request in a set format (a tool name and its inputs) and stops. The software around it runs the tool for real and adds the result to the conversation as text, and the model carries on.
- **Tool description:** a short text, put in front of the conversation, that tells the model which tools exist, what each takes and when to use it. Models are also fine-tuned on examples of good tool use.
- **Agent:** in Anthropic's words, "systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks"; in practice "typically just LLMs using tools based on environmental feedback in a loop".
- **Workflow:** "systems where LLMs and tools are orchestrated through predefined code paths". The programmer fixes the steps; the model fills them in.
- **The agent loop / ReAct:** thought, action, observation, repeated until the model decides it's done. A stopping rule (such as a maximum number of steps) keeps it from going round in circles.
- **Harness:** everything around the model in an agent: tools, the context on its desk each turn, memory across sessions, permissions, and checks. "Agent = Model + Harness."
- **Harness engineering:** building and improving that harness, rather than doing the work yourself. The phrase took off with Ryan Lopopolo's OpenAI post (below).
- **MCP (Model Context Protocol):** an open standard Anthropic published on 2024-11-25 for plugging tools and data sources into AI applications: write a server for a system once, and any MCP client can use it. Often compared to USB.
- **Compounding errors:** if each step succeeds 95% of the time, all 20 steps succeed only about 36% of the time (0.95²⁰). More in the episode on long tasks.

## The examples in the episode

- **WebGPT's browser commands** (Table 1 of the paper): `Search <query>`, `Clicked on link <link ID>`, `Find in page: <text>`, `Quote: <text>`, `Scrolled down <1, 2, 3>`, `Scrolled up <1, 2, 3>`, `Top`, `Back`, `End: Answer`, `End: <Nonsense, Controversial>`. "If a model generates any other text, it is considered to be an invalid action. Invalid actions still count towards the maximum, but are otherwise ignored." The model saw a text summary of the browser's state each step.
- **ReAct's Apple Remote question** (Figure 1 of the paper, a HotpotQA question): "Aside from the Apple Remote, what other device can control the program Apple Remote was originally designed to interact with?" Answering directly gave "iPod"; reasoning without tools gave "iPhone, iPad, and iPod Touch"; acting without reasoning ended with "yes"; ReAct searched Apple Remote, then Front Row (not found, with "Front Row (software)" among the suggestions), then Front Row (software), and answered "keyboard function keys".
- **Tool design matters:** "While building our agent for SWE-bench, we actually spent more time optimizing our tools than the overall prompt." The model made mistakes with relative file paths, so Anthropic made the tool require absolute paths, after which the model "used this method flawlessly". The guide also says "Tool definitions and specifications should be given just as much prompt engineering attention as your overall prompts."
- **This podcast's harness:** Claude working as a coding agent (Claude Code) in a cloud container; `CLAUDE.md` as briefing and memory; VibeVoice performing about 3 minutes of script at a time; Whisper (`whisper-small.en`) transcribing each segment and a voice model (WavLM) checking who speaks each line; retakes with a new seed; a cache so a run stopped at the 2-hour limit resumes. Whisper writes numbers as digits, so a short line of mostly spelled-out numbers always failed the check; the fix was a writing rule in `CLAUDE.md`.

## Calls back to season 1

- Next-token prediction, the spread of bets: the GPT-1 and pressing-Enter episodes.
- Tokens and "strawberry": the words-as-numbers episode.
- The model rereads the whole chat each turn, contextual inertia: the pressing-Enter episode.
- The base model as improv actor, fine-tuning into an assistant: the autocomplete-to-assistant episode.
- Clever Hans and shortcuts: the machine-learning episode.

## Teased for later this season

Reasoning models (next time), context engineering, memory, long tasks and compounding errors, MCP as a way in for attackers, and stories where the harness, not the model, was the problem.

## Timeline

- December 2021: WebGPT, GPT-3 with a text-based browser.
- October 2022: ReAct.
- February 2023: Toolformer.
- 2023: chat models' APIs let developers describe their own tools (OpenAI's function calling, June 2023; not checked against a primary source, since openai.com returns 403 from the cloud).
- 2024-11-25: Anthropic publishes the Model Context Protocol.
- 2024-12-19: Anthropic, "Building effective agents".
- 2026-02-11: Ryan Lopopolo (OpenAI), "Harness engineering".

## Sources

Checked on 2026-11-03.

- Reiichiro Nakano, Jacob Hilton and others (2021), [WebGPT: Browser-assisted question-answering with human feedback](https://arxiv.org/abs/2112.09332). Table 1 lists the commands; section 2 describes the text browser.
- Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan and Yuan Cao (2022), [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629). Princeton and Google; Figure 1 has the Apple Remote example.
- Timo Schick and others (2023), [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761). Meta AI; a calculator, a question-answering system, search engines, a translator and a calendar.
- Erik Schluntz and Barry Zhang (Anthropic), [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), 2024-12-19. Workflows vs. agents, stopping conditions, appendix 2 on tool design.
- Anthropic, [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol), 2024-11-25.
- Ryan Lopopolo (OpenAI), [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/), 2026-02-11. The page returns 403 from the cloud, so it couldn't be re-read for this episode. "A small team, about a million lines, no code written by hand" was checked earlier for the season plan; "several months" (five) and the engineers' shift to building tests, docs and checks, and asking what capability the agent is missing, come from secondary coverage such as [InfoQ](https://www.infoq.com/news/2026/02/openai-harness-engineering-codex). Worth reading the post itself.
