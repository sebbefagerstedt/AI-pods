# Context engineering

## Cold open

ALICE: Frank, I want to show you something. When this episode was being written, an agent started a brand new session, and the very first message from our listener was five words long. "Continue with the rest of the pods." With a typo in it, actually.

FRANK: That's not much to go on.

ALICE: It's nothing to go on! The model doesn't remember us. It doesn't remember writing the last two episodes. Every session, it starts from zero. And yet it knew what pods meant, which season we're in, what's been written, what's been rendered, how long an episode should be, and that I'm the chatty one.

FRANK: Because somebody put all of that in front of it.

ALICE: Because somebody put all of that in front of it. Before those five words, the harness had already laid out a pile of papers. Instructions on how to behave. A list of the tools it could use. Today's date. And a file from this podcast's folder, about five thousand words long, that says who the listener is, what the show is called, and what's been done so far.

FRANK: So the five words were just the top sheet on a big pile.

ALICE: Exactly. And what's on that pile, and what isn't, decides most of what the agent does next. People have a name for getting that pile right. Context engineering.

## Welcome

FRANK: Welcome to From Zero to ChatGPT, season two. I'm Frank.

ALICE: And I'm Alice. So far this season, we turned a chatbot into an agent, with tools and a loop. And last time, we gave it room to think before it acts.

FRANK: And today it's about what the agent is thinking about. Everything it sees, every single turn. What goes on the model's desk, what happens when the desk gets too full, and how you keep it tidy on a job that runs for hours.

ALICE: And Frank, I'll take the first one.

## What's on the desk

ALICE: Okay. Let's start with a picture. Imagine the model works at a desk. Every turn, the desk is swept completely clean, and then someone puts down a pile of papers. The model reads the whole pile, writes its next piece, and then, poof, the desk is cleared again.

FRANK: Every turn? Not just at the start of the session?

ALICE: Every turn. Remember the pressing-Enter episode? The model rereads the whole chat every time it answers. It has no memory of its own between turns. The only thing it knows, right now, is what's on the desk right now.

FRANK: Okay. So what's in the pile?

ALICE: For an agent, a few layers. At the top there's the system prompt, the harness's standing instructions. Who you are, how to behave, what never to do. Then the tool descriptions, the command menu from the agent episode. Each tool comes with a little explanation of what it does and when to use it. Then instruction files from the project, like this podcast's. Then the conversation itself, everything you've said and everything it's said back. And then, for an agent, the big one. Tool results.

FRANK: The stuff that comes back when it runs a command, or reads a file.

ALICE: Right. And that pile grows fast. You ask an agent to fix a bug, it reads three files, runs the tests, the tests print two hundred lines of errors. All of that lands on the desk, and stays there, turn after turn.

FRANK: Huh. So the desk is mostly stuff the agent fetched itself.

ALICE: On a long job, often, yes. Now, a couple of years ago, everyone talked about prompt engineering. How do you word the question so the model gives a good answer? And that still matters. But for agents, the question you type is a tiny part of the pile. So around twenty twenty-five, people started saying context engineering instead.

FRANK: And what's the difference, really? Isn't that just a fancier name?

ALICE: It's a bigger job. Prompt engineering is writing one good message. Context engineering is deciding everything that goes on the desk, and when it comes off. Anthropic has a nice way of putting it. You're looking for the smallest possible set of high-signal tokens that make the outcome you want most likely.

FRANK: Smallest. Not biggest.

ALICE: Smallest! That's the surprising part. You'd think, give the model everything, it's smart, it'll sort it out. And that turns out to be wrong. Frank, that's your segment.

FRANK: Okay, but quickly, before that. Why should a listener care? They're not building agents.

ALICE: Because it explains things you see every day. Why a chatbot is great at the start of a conversation and gets weird after an hour. Why it forgets an instruction you gave it way back. Why starting a fresh chat so often helps. It's all the desk.

FRANK: Fair enough. Then let's talk about the desk getting too full. Over to me.

## A bigger desk isn't enough

FRANK: So, here's the obvious fix. If the desk gets full, get a bigger desk. And the desks have got huge. GPT one could see about five hundred tokens at a time, a page or so. Today some models take a million tokens. That's several thick novels at once.

ALICE: So problem solved?

FRANK: You'd think so. But there's a catch, and people found it early. In twenty twenty-three, a team at Stanford ran a simple test. Give a model a question, and twenty documents, where exactly one of them has the answer. Then move that one document around. Put it first, put it last, put it in the middle.

ALICE: And it matters where it is?

FRANK: It matters a lot. With GPT three point five, when the answer was in the first document, it got about seventy-six percent right. When the answer was in the middle of the pile, about fifty-four percent.

ALICE: That's a big drop. Just from moving one page.

FRANK: And here's the bit that made people sit up. They also asked the same questions with no documents at all, just from memory. And it got about fifty-six percent.

ALICE: Wait. So with the answer sitting right there in the middle of the pile, it did worse than with no pile at all?

FRANK: Slightly worse, yes. The paper's called "Lost in the Middle". Models pay most attention to the start and the end of what they're given, and the middle sort of sags.

ALICE: Huh. Like reading a long report, where you remember the summary and the conclusion.

FRANK: That's pretty much it. Now, models have improved a lot since then. But a newer study, from a company called Chroma, in twenty twenty-five, tested eighteen models, including the big ones, on really simple tasks. Find a sentence in a long text. Repeat a list of words. And every single model got less reliable as the input got longer.

ALICE: Even on easy tasks.

FRANK: Even on easy ones. They called it context rot. And two findings I love. One, adding a single distractor hurt. That's a passage that looks related but doesn't actually answer the question. One of them was enough to drag performance down.

ALICE: So clutter isn't neutral. Clutter actively misleads.

FRANK: Exactly. And two, the weird one. They hid the needle in two kinds of haystack. One was a normal essay that flows. The other was the same sentences, shuffled into random order. And the models did better in the shuffled one.

ALICE: What? Why would nonsense be easier?

FRANK: Nobody's sure. One guess is that in a text that flows, the model gets drawn into following the story, and the odd sentence blends in. In a jumbled mess, the one sentence that answers the question sticks out. But it tells you something. How the model reads a long text is not how you'd expect.

ALICE: Okay, so why does this happen at all? The model can technically see everything.

FRANK: Think back to the attention episode. The networking event, where every word walks around with its badge, comparing notes with every other word. Now, that works great with fifty people in the room. With a million people in the room, every word is still trying to compare notes with all of them. Anthropic calls it an attention budget. Every token you add takes a little bit from it.

ALICE: So the more you put on the desk, the less attention each thing gets.

FRANK: That's a good way to say it. And there's a training side, too. Models see far more short texts than very long ones while they learn. So they're simply more practiced at short.

ALICE: Okay, but then I'm confused. Why would anyone sell a million-token model if it gets worse with a million tokens?

FRANK: Because it's still very useful. Being able to load a whole codebase, or a whole contract, is great. It's just not free. A big desk is a place you can put things, not a promise that the model will use all of it well. So the job becomes choosing.

ALICE: The smallest set of high-signal tokens.

FRANK: There you go. And now we get to the fun part. Some of those tokens are written by people, on purpose, ahead of time. Alice, yours.

## The instruction file

ALICE: Okay. So, one of the layers in the pile is a file the project leaves for the agent. In this podcast's folder, there's one called CLAUDE dot M D. Other tools read one called AGENTS dot M D. Same idea. A plain text file, in the project's folder, that the harness drops on the desk at the start of every session.

FRANK: What's actually in it?

ALICE: Things a new colleague would need on day one. How to run the tests. Which commands to use. The house style. What not to touch. Think of it as a briefing for someone who's very smart, has never seen the place before, and will forget everything by tomorrow.

FRANK: Which is every agent, every morning.

ALICE: Every agent, every morning. AGENTS dot M D started as a shared format between a bunch of coding tools, OpenAI's Codex, Google's Jules, Cursor and others, and it's now looked after by a foundation under the Linux Foundation. Its website says over sixty thousand open-source projects use one.

FRANK: And if a project's huge, one file for everything?

ALICE: You can have several. One at the top, and one in each part of the project. The agent reads the one closest to the files it's working on, and that one wins. And what the user types in the chat beats all of them.

FRANK: Okay. So how do you write a good one? Is it just, the more detail the better?

ALICE: No, and that's the whole skill. Anthropic says there are two ways to get it wrong. One is too rigid. You try to hard-code every situation. "If the test fails with this error, do that." It's brittle, and the agent falls apart the moment something doesn't fit.

FRANK: And the other?

ALICE: Too vague. "Write good code." "Be careful." That sounds like advice, but it doesn't tell the model anything it can act on. They talk about finding the right altitude. High enough to be a principle, low enough to be concrete.

FRANK: Give me an example from our file.

ALICE: Okay, here's one I like. Our file says the check compares words as written, and Whisper writes numbers as digits. So a line that's mostly spelled-out numbers will always fail the check. Keep such lines short, or surround them with ordinary words.

FRANK: Right, the digits bug from the agent episode.

ALICE: That rule is a good altitude. It gives the reason, so the agent can handle cases nobody listed. It's not "never say twenty-five", and it's not "be careful with numbers". It explains what's going on.

FRANK: Okay. And how big is our file?

ALICE: That's the embarrassing part. It started two weeks ago at about seven hundred words. It's now just over five thousand. It's been changed forty times.

FRANK: Five thousand words, read at the start of every session. Is that a problem?

ALICE: It's starting to be. Remember the million-line experiment at OpenAI, from the agent episode? From what's been reported, they tried the one big instruction file, and it didn't work well. Too much, and it went stale. So they made it short, more like a table of contents, pointing to other documents the agent reads only when it needs them. A map, not an encyclopedia.

FRANK: And our file is more like a diary.

ALICE: Honestly, yes. Half of it is a log of what got rendered, which segments needed a second take. Useful history, but on most days the agent doesn't need any of that. So that's a lesson we're learning about our own harness. The briefing file has to be pruned, not just added to.

FRANK: Huh. So the file can rot, too. Not just the context.

ALICE: The file can rot too. And a wrong instruction is worse than a missing one, because the agent trusts it. There's even a line at the top of ours that just says, go read this other file, and it pulls it in. One short rule our listener added: before showing me a big change, walk me through it.

FRANK: Which the agent will read, every single time.

ALICE: Every single time. That's the power of it. Okay, Frank. You've got the long jobs.

## Keeping the desk tidy

FRANK: Right. So far, we've talked about what's on the desk at the start. But an agent working for hours keeps adding to the pile. Every file it opens, every command it runs. So, what do you do when it gets full? There are a few tricks, and they're all quite human.

ALICE: Go on.

FRANK: Trick one. Don't fetch the whole library. Fetch the index card. Instead of loading every file in the project up front, a good agent keeps short pointers, a file name, a folder, and looks things up only when it needs them. Anthropic calls it just in time. Claude Code, their coding agent, does this all the time. It searches with simple tools, the kind programmers have used for decades. Find files whose names match this. Find lines containing that word. Show me just the first twenty lines.

ALICE: So it's like a researcher who knows where things are in the library, instead of carrying every book around.

FRANK: Exactly. And the folder itself tells it things. A file called test-something, in a folder called tests, says a lot, without opening it.

ALICE: Okay. Trick two?

FRANK: Clear old tool results. If the agent ran the tests an hour ago and printed two hundred lines of errors, and then fixed them, it doesn't need those two hundred lines on the desk anymore. So the harness quietly clears them. It's the lightest kind of tidying.

ALICE: Makes sense. And when even that's not enough?

FRANK: Trick three, compaction. When the desk is nearly full, the harness asks the model to write a summary of everything so far. What we're doing, what's been decided, what's still broken. Then it sweeps the desk and starts a fresh one with just the summary. In Claude Code, it also brings back the five files the agent touched most recently.

ALICE: Like writing yourself a handover note before a shift change.

FRANK: That's exactly what it is. And it has the same risk as a handover note. What did you leave out? A summary keeps the big decisions, and loses the little detail that turns out to matter three hours later. So writing that summary well is a real craft.

ALICE: And there's the manual version. Before this session started, our listener cleared the previous one. Wiped the desk, started fresh.

FRANK: Which is the same advice from the pressing-Enter episode. When a chat's gone wrong, a fresh one often helps. The old wrong turns stop pulling on the answers.

ALICE: Okay, what else?

FRANK: Trick four. Notes outside the desk. The agent keeps a notes file, in its folder, and writes things down as it goes. Then when the desk gets wiped, the notes are still there. My favorite example is Anthropic's Claude playing Pokémon, the video game, for hours on end. It kept notes like, and this is a real one, "for the last one thousand two hundred and thirty-four steps I've been training my Pokémon in Route 1, Pikachu has gained eight levels toward the target of ten."

ALICE: That's adorable. And very organized.

FRANK: It also mapped the areas it had explored, and kept notes on which attacks worked against which opponents. So after its context was reset, it read its notes and carried on. And Alice, our file does the same. That status section, the diary.

ALICE: So the diary is the right idea, it's just in the wrong place. It should be a notes file you open when you need it, not something on the desk every morning.

FRANK: There you go, you've just redesigned our harness. And trick five, helpers. Instead of one agent doing everything on one crowded desk, a lead agent hands a job to a helper with a clean desk of its own. The helper might read fifty files, and then report back just a page or so. The lead agent never sees the fifty files. Just the page.

ALICE: A clean desk for each job.

FRANK: And there's a money side, too, which is why the order of the pile matters. The top of the pile is the same every turn. Same instructions, same tools, same file. So the providers let you save the work of reading it, and charge much less, often about a tenth, to reread a part that hasn't changed. That's called prompt caching. But it only works if the unchanging stuff stays at the top. Change one word near the start, and the whole pile has to be read again from scratch.

ALICE: So, stable things first, new things last.

FRANK: Stable things first. And there's one more thing that goes on the desk that people forget about. The tool descriptions. If you give an agent forty tools that overlap, it gets confused, just like a person would. Anthropic's test is nice. If a human engineer can't say for sure which tool to use in a given situation, the agent can't be expected to do better.

ALICE: Fewer, clearer tools.

FRANK: Fewer, clearer tools. It's all the same idea. Every token on the desk has to earn its place.

## Recap

ALICE: Okay, recap. Frank, you start.

FRANK: One. A model has no memory of its own. Every turn, it gets a clean desk and a pile of papers, and that pile is all it knows. System prompt, tools, instruction files, the conversation, and for agents, piles of tool results. Deciding what goes on it is context engineering.

ALICE: Two. A bigger desk isn't enough. Models pay most attention to the start and end, and lose things in the middle. In one test, an answer buried in the middle did worse than no documents at all. And every model gets less reliable as input grows, and one distractor is enough to hurt. Context rot.

FRANK: Three. Instruction files, CLAUDE dot M D or AGENTS dot M D, are a briefing the agent reads every session. Write them at the right altitude, with the reason behind each rule. Keep them short, like a map pointing elsewhere, and prune them, because a wrong instruction is worse than a missing one.

ALICE: Four. On long jobs, keep the desk tidy. Look things up only when needed. Clear old tool results. Compact into a handover note. Keep notes outside the desk. And hand big jobs to helpers with clean desks of their own.

FRANK: And five. Order matters. Stable things first, so they can be cached, and fewer, clearer tools. Every token on the desk has to earn its place.

ALICE: Next time, what happens when the desk gets wiped, and you want the agent to remember anyway. Memory, and how a model that remembers nothing can look things up. That's called RAG.

FRANK: See you then.
