# Long tasks

From Zero to ChatGPT, season 2. About 15 minutes, with Frank and Alice.

Why small mistakes pile up over a long job, how METR measures the length of task an agent can finish, why a separate checker beats checking your own work, and how a harness runs a job that takes days like a factory with shifts. This podcast's own renders are the running example.

## Key terms

- **Compounding errors:** if each step must go right, success rates multiply: 99% per step is about 37% over 100 steps and under 1% over 500. Real agents can recover, so the point is to notice and fix mistakes.
- **Time horizon (50%):** METR's yardstick: the length of task, measured in how long skilled people take, that an agent finishes half the time. The 80% horizon is the same at four successes in five, and is much shorter.
- **Messiness:** METR's term for how unlike a neat benchmark a task is (vague goals, no automatic scoring, changing conditions); models do worse on messier tasks.
- **Intrinsic self-correction:** a model reviewing its own answer with no new information. Often doesn't help, and can make answers worse.
- **External feedback:** a signal the model didn't produce: tests, a compiler, a separate checker model (in this podcast, Whisper and a voice-matching model).
- **Initializer agent:** in Anthropic's long-running harness, a first session that only sets up the job: a feature list, a start-up script, a progress file and a first git commit.
- **Feature list:** over 200 features for one app, each marked as not passing; agents may only change that mark, and "It is unacceptable to remove or edit tests".
- **End-to-end testing:** checking the app the way a user would (in a real browser), rather than with a quick unit test.

## The numbers in the episode

- **METR's original paper** (Kwa and others, March 2025): frontier time horizons doubled "approximately every seven months since 2019"; Claude 3.7 Sonnet's 50% horizon was about 50 minutes. If the trend holds and carries over to real work, "within 5 years" agents could automate many software tasks that take people a month.
- **METR's current numbers** (Time Horizon 1.1, larger task suite, raw data read on 2026-11-03):
  - GPT-2 (2019): about 6 seconds. GPT-4 (2023): about 4 minutes. Claude 3.7 Sonnet (February 2025): about 60 minutes in this version.
  - Best in the data: Claude Mythos Preview (early version, April 2026), about 1,045 minutes (17.4 hours), with a confidence interval from about 8.5 to 55 hours. Its 80% horizon: about 186 minutes (3.1 hours).
  - Doubling time: about 129 days (about 4.2 months, interval 3.4 to 5.2) from 2023 on; about 188 days over the whole period. These exclude estimates over 16 hours.
  - So the "4-month doubling" and "14 to 20 hours" figures found online earlier are close to METR's own current data, which this episode uses instead.
- **Self-correction** (Huang and others, Google DeepMind and University of Illinois, 2023): "LLMs struggle to self-correct their responses without external feedback", and performance "sometimes degrades after self-correction".
- **Anthropic's long-running harness** (2025-11-26): two failure modes, doing too much at once (running out of context mid-implementation) and declaring the job done too early. Browser testing through Puppeteer found many more bugs than unit tests or curl.
- **This podcast:** rendering runs about 4.7 times slower than real time; a background job stops after 2 hours; the GPT-1 episode took three runs and half its segments needed a retake; a buffering bug once left only 26 of about 65 segments with a logged check (fixed with `grep --line-buffered`).

## Calls back

- Contextual inertia: the pressing-Enter episode.
- RLHF's robot food critic and sycophancy: the autocomplete-to-assistant episode.
- The scaling laws' straight line: the scale episode.
- Reward hacking and the "fudge" example: the reasoning-models episode.
- The million-line experiment and "what's missing from the harness": the chatbot-to-agent episode.
- Handover notes and the instruction file as diary: the context-engineering and memory episodes.

## Teased

Many agents and computer use, next time.

## Sources

Checked on 2026-11-03.

- Thomas Kwa, Ben West, Joel Becker and others (METR, 2025), [Measuring AI Ability to Complete Long Software Tasks](https://arxiv.org/abs/2503.14499) (current version v4, July 2026).
- METR, [Time horizon chart](https://metr.org/horizon-chart-embed) and its raw data, [benchmark_results_1_1.yaml](https://metr.org/assets/benchmark_results_1_1.yaml).
- Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song and Denny Zhou (2023), [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798); ICLR 2024.
- Anthropic (2025-11-26), [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).
- This repo's `CLAUDE.md` and `tools/render_all.sh`.
