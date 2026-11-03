# From chatbot to agent

## Cold open

ALICE: Frank, can I tell you how this episode got made?

FRANK: Go on.

ALICE: Nobody typed this script. An AI agent wrote it. It read a file of notes about the series, and about you, the listener. It looked up the papers, wrote the lines you're hearing now, and then it handed them to another AI model that performs them in our voices.

FRANK: Which is a little strange to say out loud.

ALICE: It gets stranger. The agent can't hear. It has no ears. So how does it know the recording came out right? That I didn't suddenly start talking in your voice?

FRANK: Has that happened?

ALICE: It has! Every so often, the voice model puts a line in the wrong voice. Or garbles it. So after each chunk, a third model, a speech recognizer, writes down what it heard, and a little program checks every line. Is it there? Is it in the right voice? If not, record that chunk again.

FRANK: So the model writing the script is just one piece. There's this whole... machinery around it.

ALICE: And that machinery has a name. It's called a harness. And it's what this whole season is about.

## Welcome

FRANK: Welcome to From Zero to ChatGPT. I'm Frank.

ALICE: And I'm Alice. And this is the start of season two.

FRANK: Last season, we went all the way from Turing to ChatGPT. Knobs and "how wrong", neural networks, the transformer, pre-training, and finally how a next-word guesser was turned into an assistant.

ALICE: And that's where we stopped. A model you chat with. You ask, it answers. But that's not really where things are now, is it? Now the models do things. They search the web, they write and run code, they fix bugs while you're asleep.

FRANK: So this season, we look at the software around the model. What it gives the model, what it lets it do, and what it stops it from doing. Today, the basics. How does a model that can only write text use a tool at all? What makes something an agent? And what exactly is a harness?

ALICE: Frank, the first one's yours.

## A model that can only write

FRANK: Okay. Let's start with what we know from last season. What does a language model actually do?

ALICE: It guesses the next token. A spread of bets over its whole vocabulary, pick one, add it to the text, and go round again.

FRANK: Right. And that's all it does. It writes text. It can't click anything. It can't open a file. It can't check the weather. It has no hands.

ALICE: But when I ask ChatGPT to search the web, it searches the web. So who's doing the searching?

FRANK: Not the model. Here's the trick. The model writes a request. In a special format that the software around it is watching for. Something like, "search, open bracket, weather in Stockholm, close bracket". And then it stops writing.

ALICE: And the software sees that, and...

FRANK: And runs the search. For real. Then it takes the results, pastes them into the conversation as text, and hands everything back to the model. And the model carries on writing, now with the search results right there in front of it.

ALICE: Huh. So the model is sort of... a boss writing notes to an assistant. "Please look this up." And the assistant does the actual work.

FRANK: That's a good way to put it. Except the boss can't leave the room, and only ever sees what's on the note that comes back. That's called a tool call. The model calls a tool, the software runs it, and the result comes back as text.

ALICE: Okay, but wait. How does the model know the format? How does it know there even is a search tool?

FRANK: Two ways. First, it's told. At the start of the conversation, before your message, the software puts a short description of each tool. "There's a tool called search. It takes a query. Use it when you need something recent." The model reads that like any other text.

ALICE: And the second way?

FRANK: It's trained to do it. Remember the base model from last season? The improv actor that'll continue any text? An improv actor won't reliably write requests in exactly the right format, and stop at exactly the right moment. So the companies fine-tune their models on lots of examples of good tool use, and of when not to bother.

ALICE: When did this start? Because I remember the first ChatGPT couldn't do any of this.

FRANK: The research is a bit older. My favorite early one is from OpenAI, in late twenty twenty-one. It's called WebGPT. They gave GPT-3 a web browser. But a text-only browser. The model saw the page as text, and it had a short menu of commands. Search. Click on a link. Find in the page. Scroll down. Scroll up. Go back.

ALICE: And quote. Wasn't there a quote command?

FRANK: There was! It could copy a passage as a reference, so a person could check where each claim came from. And when it was ready, a command for "end, and answer". And here's my favorite detail. If the model wrote anything that wasn't on the menu, the browser just ignored it. It still counted against its budget of steps, though.

ALICE: That's harsh. But fair.

FRANK: Then, early in twenty twenty-three, a paper from Meta called Toolformer showed that a model could teach itself when to use tools. A calculator, a search engine, a translator, a calendar. And by the middle of that year, you could hand your own tools to the big chat models. Describe a tool, and the model would write calls to it.

ALICE: Okay, so here's my "why does that matter" question. Why not just make the model smarter? Why bolt on tools?

FRANK: Because some things a model is just bad at, by its nature. Remember strawberry? How many R's?

ALICE: It sees tokens, word pieces, not letters. So it has to guess.

FRANK: Exactly. But if it can write three lines of code and run them, it doesn't have to guess. It counts. Same with big sums, today's date, the news since it was trained, or what's in your files. A model's knowledge is frozen on the day training ended. Tools are how it reaches the world after that day.

ALICE: So a calculator for the things it can't do in its head, and a window for the things it can't know.

FRANK: That's the episode in one sentence, almost.

## The loop

ALICE: But one tool call isn't an agent, right?

FRANK: No. And that's your segment, Alice.

ALICE: It is. So, one tool call is a nice feature. You ask about the weather, it looks it up, it answers. The interesting bit is what happens when you let it keep going. Call a tool, look at the result, decide what to do next, call another tool. Over and over, until the job is done.

FRANK: A loop.

ALICE: A loop. And there's a paper from twenty twenty-two that made this click for a lot of people. Google and Princeton. It's called ReAct, as in "reason" and "act".

FRANK: Like a chemical reaction.

ALICE: A pun, yes. The idea is to have the model take turns. A thought, written out. Then an action. Then it reads what came back, an observation. Then another thought. Thought, action, observation, thought, action, observation.

FRANK: Give me an example.

ALICE: The paper has a lovely one. The question is, "Aside from the Apple Remote, what other device can control the program Apple Remote was originally designed to interact with?"

FRANK: Ouch. That's a mouthful. You have to find the program first, and then what else controls it.

ALICE: Exactly. Two hops. So first, they just asked the model straight out. It said "iPod". Wrong. Then they asked it to think step by step first, but without any tools. It wrote a confident little chain of reasoning, and got it wrong again. It said "iPhone, iPad and iPod Touch".

FRANK: Making things up, then.

ALICE: Making things up, very fluently. Then they tried actions without thoughts. It searched, it looked around, and then it just answered "yes". Which isn't even an answer to the question.

FRANK: And with both?

ALICE: Thought: I need to search Apple Remote and find the program it was designed for. Action: search, Apple Remote. Observation: it was designed to control the Front Row media center program. Thought: Now I need to search Front Row. Action: search, Front Row. Observation: not found, but here are some similar pages, including Front Row, software.

FRANK: So it hits a wall.

ALICE: And it adjusts! Thought: let me search Front Row, software. Observation: Front Row is a discontinued media center program, controlled by an Apple Remote or the keyboard function keys. Thought: so the answer is the keyboard function keys. Action: finish.

FRANK: Huh. That's... honestly, that's what I'd do. Search, get it slightly wrong, try again.

ALICE: And that's the point. The thinking keeps it on track, and the actions keep it honest. It's checking against the real world at every step, instead of making up a fact and building on it.

FRANK: Okay, but who decides when it's done? In a loop, I mean.

ALICE: The model does. That's what makes it an agent. Anthropic put this nicely, in a guide on building agents from late twenty twenty-four. They split these systems in two. In a workflow, the steps are written in ordinary code, by a programmer. First summarize, then translate, then send the email. The model fills in each step, but the path is fixed.

FRANK: And an agent?

ALICE: In an agent, the model decides the path. Which tool next, whether to try again, when it's finished. In their words, agents are "typically just LLMs using tools based on environmental feedback in a loop."

FRANK: "Just". I like the "just".

ALICE: It's honest! There's no magic extra part. It's the same next-token guesser from last season, in a loop, with tools. And they add some advice I think about a lot. Give it a stopping rule. A maximum number of steps, say. Because a model in a loop can also go round and round.

FRANK: Has that happened? Going round in circles?

ALICE: Oh, all the time, especially early on. When people first wired chat models into loops, back in twenty twenty-three, there was a lot of excitement, and a lot of agents that got stuck. Searching the same thing again and again. Or wandering off on a side task and forgetting the real one.

FRANK: Why? Same model.

ALICE: Two reasons. First, the models just weren't good enough yet at the long game. And second, small errors pile up. If each step goes right ninety-five percent of the time, then over twenty steps, the chance that every step went right is... a lot lower than you'd hope.

FRANK: About a third, I think.

ALICE: About a third. So long tasks are hard, and we'll have a whole episode on that later in the season. But here's the thing I want you to take away. Think about how the loop actually works, with what we know about models.

FRANK: Go on.

ALICE: Remember the episode about pressing Enter? The model doesn't remember anything between turns. It rereads the whole conversation, every single time.

FRANK: Right. Which is why it clings to its earlier mistakes.

ALICE: So in a loop, every step means rereading everything. The task, every thought, every tool call, every result. The pile of text grows and grows. And the software around the model decides what goes on that pile. What the model sees. What it's allowed to call. When it has to stop.

FRANK: The software.

ALICE: The harness. Frank, take it away.

## The harness

FRANK: So, why "harness"? Picture a horse. Enormously strong. Fast. Willing, mostly. But a horse on its own won't plow your field. You need a harness. The straps, the collar, the reins. The harness doesn't make the horse any stronger. It points the strength somewhere useful, and it lets you steer and stop.

ALICE: And there's a horse from last season, isn't there? Clever Hans.

FRANK: The horse that seemed to do arithmetic, but was really reading the people watching him. Good callback. Because that's a warning that fits here too. A model, like Hans, will find whatever shortcut gets it the reward. A good harness has to be built with that in mind.

ALICE: Okay. So what's actually in a harness? Make it concrete.

FRANK: Think of a new employee on day one. Very bright, read every book, but knows nothing about your company. What do you give them? First, tools. A computer, logins, access to the right systems. For an agent, that's the tool list. Search the web, read a file, run code, send a message.

ALICE: Okay, one.

FRANK: Two, a briefing. What's the job, how we do things here, where things are. For an agent, that's everything that goes on its desk each turn. The instructions, the relevant files, the rules. That's called context, and it has its own episode.

ALICE: Three?

FRANK: Three, memory. The model forgets everything between sessions. Every morning is its first day. So the harness keeps notes and puts the right ones back in front of it. Also its own episode.

ALICE: Four.

FRANK: Permissions. What it's allowed to do on its own, and what needs a person to say yes first. You let the new hire read the code on day one. You probably don't let them delete the customer database.

ALICE: Hopefully not on any day.

FRANK: Hopefully not. And five, checks. Tests that run after every change. Something that watches what it's doing. A second pair of eyes before anything goes out.

ALICE: Okay. Tools, briefing, memory, permissions, checks. So the model's the horse, and all of that is the harness.

FRANK: There's a slogan that caught on this year. "Agent equals model plus harness."

ALICE: But doesn't the model matter most? I mean, everyone talks about which model is best.

FRANK: It matters a lot. But here's what surprises people. Take one model, put it in two different harnesses, and you can get very different results. Better tool descriptions, a better briefing, a test it can run to check its own work. Anthropic's guide makes the same point. When they built a coding agent, they spent more time on its tools than on its instructions. One example: the agent kept getting lost in folders, so they changed one tool to always take the full address of a file. After that, no more mistakes.

ALICE: And the tools have to plug in somehow. Every company has its own systems.

FRANK: That used to be the pain. Every tool had to be wired up by hand, for every app. So at the end of twenty twenty-four, Anthropic published an open standard called the Model Context Protocol. People call it MCP. Think of it as a standard plug. Write the plug for your calendar, or your database, once, and any harness that speaks MCP can use it.

ALICE: Like USB for tools.

FRANK: That's the comparison everybody uses, yes. And it's spread well beyond Anthropic. Which, by the way, also means a plug can be a way in for trouble. But that's for later in the season.

ALICE: Noted. So where does the phrase "harness engineering" come from?

FRANK: It took off with a post from OpenAI, in February this year, by an engineer called Ryan Lopopolo. A small team built a real product, about a million lines of code, over several months. And no person wrote any of the code by hand. Codex, OpenAI's coding agent, wrote all of it.

ALICE: A million lines. And the humans did what, exactly?

FRANK: That's the interesting bit. Their job changed. They stopped writing code, and started building the harness. Writing down how things should be done, in files the agent reads. Adding tests and checks so the agent could see for itself when something broke. And when the agent kept failing at something, they didn't just fix it themselves. They asked, what's missing from the harness, that would let the agent get this right next time?

ALICE: Okay, that's a real shift. You're not doing the work, you're building the place where the work gets done.

FRANK: Exactly. Like going from cook to designing the kitchen.

## How this podcast is made

ALICE: Which brings us back to the start. Because this podcast is a little harness, and I think it's the clearest example we've got.

FRANK: Your segment.

ALICE: My segment. So, the model, the horse, is a language model, Claude, working as a coding agent. Its tools are a command line on a computer in the cloud. It can read and write files, run programs, look things up on the web.

FRANK: Okay. That's the tools. The briefing?

ALICE: There's a file in the project called CLAUDE dot M D. A plain text file, and the agent reads it at the start of every session. It says who the listener is. That you've read "Attention Is All You Need". That you're short on time, so episodes have to work by ear. That the hosts are Frank and Alice, and they swap roles each segment.

FRANK: Wait, so that's how we know to hand over to each other?

ALICE: That's literally how we know. It also has the plan for the season, the rules for writing a script, and a list of lessons learned. Like, the voice model can't do laughing, so don't write "ha".

FRANK: And memory? You said every session starts from nothing.

ALICE: Same file. When something gets done, or something goes wrong, the agent writes it down there, so the next session knows. It's a briefing and a diary at once.

FRANK: And the checks are the speech recognizer from the cold open.

ALICE: Right. It's called Whisper. The voice model performs about three minutes of script at a time. Then Whisper writes down what it heard, a program lines that up with the script, and another model compares each line's voice with the real Frank and the real Alice.

FRANK: The real us.

ALICE: The voice recordings we were copied from. Don't overthink it. If anything's off, that chunk gets recorded again, with a different random seed, so it comes out a bit different. And every finished chunk is saved, so if the computer stops halfway, which it does, every two hours, it picks up where it left off.

FRANK: Okay. So, honest question. Does it work?

ALICE: Mostly! But the checks have their own bugs, and this is my favorite lesson of the whole project. Whisper writes numbers as digits. So if I say "two hundred and fifty-five", Whisper writes it down as two, five, five.

FRANK: And the checker's comparing words.

ALICE: So the words never match. A short line that's mostly a number counts as missing, every single time, and the chunk got recorded again and again. The checker was wrong, not the recording.

FRANK: So the fix was...

ALICE: Write the line differently. Put the number among enough ordinary words. And put that in the file, so it never happens again. Whisper also sometimes gets stuck repeating "thank you" over a stretch of audio. So the rule now is, before you believe a line is missing, listen to that bit again on its own. Well, transcribe it again, since nobody's listening.

FRANK: So the harness checks the model, and then somebody has to check the harness.

ALICE: And that's the whole season, in a way. And notice what's not in the loop. You. The listener decides what gets redone. The agent flags problems, a person makes the call.

FRANK: Permissions.

ALICE: Permissions. And it can only reach this one project. It can't go wandering around anyone's computer.

FRANK: Okay, one more "wait, why does that matter". Why should someone who just wants to understand AI care about all this plumbing?

ALICE: Because it's where most of the action is now. When people say an agent built an app, or found a bug, or did something it shouldn't, the question is always both. How good was the model? And what did the harness let it see, and do, and get away with? Later in the season, there are stories where the model wasn't the problem at all. The harness was.

FRANK: Or a missing piece of it.

ALICE: Or a missing piece of it.

## Recap

FRANK: Okay, recap. Alice, you start.

ALICE: One. A language model can only write text. A tool call is the model writing a request in a set format and stopping. The software around it runs the tool for real and pastes the result back in, as text.

FRANK: Two. Models learn tools two ways. They're told, with a short description of each tool at the start. And they're trained on examples. Tools cover what models are bad at, like counting letters, and what they can't know, like anything after their training ended.

ALICE: Three. An agent is a model calling tools in a loop. Thought, action, observation, again and again, deciding for itself what to do next and when it's done. A workflow is different. There, the steps are fixed in code.

FRANK: Four. The loop has weak spots. Small errors pile up over many steps, and an agent can go round in circles. So give it a stopping rule.

ALICE: Five. The harness is everything around the model. Tools, the briefing on its desk, memory, permissions and checks. Agent equals model plus harness. The same model can do much better or worse depending on its harness, and MCP is the standard plug for adding tools.

FRANK: And six. The harness needs checking too. This podcast's checker counted lines as missing because it wrote numbers as digits. Somebody always has to watch the watcher.

ALICE: Next time, the thinking that agents depend on. Reasoning models, the ones that think before they answer. What are they actually doing during all that thinking?

FRANK: See you then.
