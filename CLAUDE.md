@AGENTS.md

# AI-pods

A personal podcast series that teaches AI and LLM fundamentals. Episodes are written as scripts, turned into audio with text-to-speech, and listened to in Apple Podcasts.

## The listener

- Sharp and follows current AI news, but missed the foundations and wants the basics.
- Has read "Attention Is All You Need" (2017). Plans to read OpenAI's GPT-1 paper, "Improving Language Understanding by Generative Pre-Training" (2018). GPT-1 is an assumption the listener hasn't confirmed.
- Finds the papers heavy going and lacks time for them, so episodes must be easy to follow by ear.
- Likes how "The Curiosity Mix" sounds, an AI podcast with all the hallmarks of NotebookLM's Audio Overviews: the hosts react to each other ("Right." "Exactly."), use fillers and finish each other's sentences.
- Likes episodes 1 and 9, and doesn't mind the faint, short music like an intro jingle that VibeVoice sometimes adds on its own.

## Decisions

- Episode length follows the content: as long as the topic needs to be explained well, without padding or rushing. Around 20 minutes is typical, not a target. Scripts run about 175 words a minute.
- Two hosts, Frank and Alice. In each segment one explains and the other is the sharp, curious one who asks the questions the listener would ask ("wait, why does that matter?"); they swap roles from segment to segment, with a short handover ("Alice, this one's yours").
- The series is called "From Zero to ChatGPT" in the episodes, after the season title. Season 2 keeps that show name and calls itself "season two" (a default chosen when it started; the listener may want a new name).
- English.
- Plain language and everyday analogies first, then the real term. Nothing should require seeing an equation.
- Each episode builds on the earlier ones and ends with a short recap.
- For now the hosts never say episode numbers, since the plan still moves: callbacks name the topic ("early in the series", "the GPT-1 episode") and teasers say "next time" or "later in the series". Proper cross-references can be added once the season is settled. The rendered MP3s of 1 and 9 still say the old numbers (in 9, only the teasers for 10, 11 and 12 are now one too low); don't re-render them for that until the numbering is final.
- Each episode in the repo: the script with show notes (key terms, links to the original papers) and the MP3. Test clips go in `samples/`, episodes in `episodes/NN-slug/`: `script.md` (the dialogue only, so it can be rendered), `notes.md` (the show notes) and `NN-slug.mp3`. Bonus episodes outside the season plan go in `episodes/bonus-slug/`, with `bonus-slug.mp3`. Season 2 episodes go in `episodes/s2-NN-slug/`, with `s2-NN-slug.mp3`.
- For now, the MP3s just live in this repo. Later the listener will set up GitHub Pages so an RSS feed can bring the episodes into Apple Podcasts (Follow a Show by URL). The repo will become private: Pages on a private repo needs a paid GitHub plan, and the Pages site itself stays public.

## Where things are

This file holds what every session needs. The rest is read only when it's needed:

- `planning/season-1.md`: the plan for season 1, "From zero to ChatGPT". All 13 episodes are written and rendered, plus a bonus episode on Jev (`episodes/bonus-jev/`).
- `planning/season-2.md`: the plan and checked sources for season 2, harness engineering. All nine episodes are written and rendered.
- `planning/history.md`: what each session did, oldest first, including each episode's render problems and retakes.
- The `render` skill (`.claude/skills/render/SKILL.md`, or type `/render`): how to render, restart, check and retake.
- `extras/life-of-a-prompt.html`: a diagram of where each part of a request happens, published as https://claude.ai/artifact/NS61VZPKbommEcUt8bmkQL.

Before writing or changing an episode, read its season's plan and the episode's `notes.md`. Left for a later season: image and video generators, interpretability, chips and data centers, benchmarks as a topic of its own.

## Now

Open items only. When one is done, delete it here and add a dated item to the end of `planning/history.md`. Keep this whole file under 2,500 words. At the end of each session, check it (`wc -w CLAUDE.md`), and if it's over 1,500 words or holds finished items, suggest to the listener what to move or trim. Anything only one kind of task needs goes in its own file or skill, with a pointer above. Don't `@`-import it, since imported files load with this one.

- **Season 1:** every segment passes the check except 13's last (line 120, a possibly clipped Frank line). The listener listens and reports anything to redo.
- **Season 2:** the check flagged lines in 1 (segments 1, 4, 5), 2 (5), 3 (1, 4, 6, 7), 4 (4), 5 (1, 5), 6 (2, 5), 7 (5) and 9 (1, 2, 4); 8 passed. List them with `awk '/^== s2-01/{f=1} f' .cache/render_all.log | grep -E "^== |take 1: [^e]"`. The listener decides which, if any, to retake. Season 2 hasn't had the `review-with-me` walk-through AGENTS.md asks for.
- **Season 2 review (2026-11-04):** small fixes the listener hasn't decided on. 3's cold open calls the opening message "five words" but quotes seven. The notes for 5–8 say 15, 14, 16 and 17 minutes, but the MP3s run 13.0, 12.7, 12.6 and 13.2. 7 could use Microsoft's withdrawal of VibeVoice's code (2025-09-05) as its no-take-backs example. 9 writes "METR" where 5 says "Meter".

## Scripts and voices

- Script format: every paragraph starts with the speaker's name in capitals, `FRANK:` or `ALICE:`, and the voice is cloned from `voices/<name>.wav`. Lines starting with `#` are skipped, so `## Segment` headings are fine. Any other unlabeled paragraph stops the render, so nothing is dropped silently.
- Write the way people talk, not the way people read aloud. The one asking reacts and pushes back ("Okay, fair. But...", "Huh. So..."), and both hosts use the odd filler, unfinished thought or "you know". VibeVoice performs these naturally. It doesn't do overlapping speech or sounds like laughter, so avoid "Ha." and the like.
- The four demo voices in `voices/` are Alice and Maya (women) and Carter and Frank (men). A clone copies the recording's delivery as well as its sound: Alice and Carter are chatty, Frank's source is a narrated deep dive, and Maya's a technical reading (rejected as computer-like).
- Names and acronyms: spell them the way they should sound ("Mycin" for MYCIN, which otherwise gets spelled out; "Bert" and "Elmo" for BERT and ELMo) or leave them for the show notes (XCON). Long strings of hard names in one sentence can derail the model, so spread them out. Moravec came out garbled in a test. A probe for episode 9 came out fine for GPT-1 ("GPT one"), GPT-2, Radford, Smashwords, Books Corpus, LSTMs and Race; Sutskever came out close; Whisper wrote "cloze test" as "closed test", which sounds nearly the same.
- VibeVoice now and then puts a line in the other host's voice, garbles it or adds a stray sound (a beep, once). The renderer catches this: after each segment it transcribes the audio with Whisper, lines the words up with the script to find each line, checks each line's voice, and retakes the segment with a new seed (up to three takes) if anything is off. The check compares words as written, and Whisper writes numbers as digits ("255", "80%"), so a line of five or more words that's mostly spelled-out numbers ("Why two hundred and fifty-five?") always counts as missing and uses up every take; keep such lines under five words, or among enough ordinary words.

## Environment notes

- Work in the "AI Pods" cloud environment. On 2026-10-21 it reached Hugging Face, PyPI, the PyTorch wheel index and raw.githubusercontent.com; github.com pages for other repos returned 403. The first session ran in "Tributary", where Hugging Face was blocked. If access is ever narrowed, the voice models need `huggingface.co` and `*.hf.co`.
- Text-to-speech: VibeVoice-1.5B (Microsoft, MIT license, released for research), run through transformers as `vibevoice/VibeVoice-1.5B-hf` (5.4 GB, downloaded on first use). The 7B model needs 18.7 GB, more than this machine's 15 GB of memory. Run `tools/setup.sh` to build `.venv` with CPU-only PyTorch and the versions pinned in `tools/requirements.txt`. ffmpeg is preinstalled.
- Kokoro-82M was tried first: fast, but it reads each line on its own and sounded computer-like. It's in the git history.
