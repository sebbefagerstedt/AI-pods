# Long tasks

## Cold open

ALICE: Frank, do you know how long it takes to make one of our episodes? Not write it. Turn it into audio.

FRANK: I'm guessing longer than it takes to listen to.

ALICE: Much longer. About five times longer. And the agent that runs it can only keep a job going for two hours at a stretch. After that, the job just stops. So for the GPT-1 episode, the render took three separate two-hour runs, each one picking up where the last one died.

FRANK: How does it pick up? It doesn't remember.

ALICE: It saves every finished piece. Every three minutes of audio or so, it writes the piece to disk. So when it starts again, it skips what's done. And after each piece, another model listens back, writes down what it hears, and checks it against the script. Is every line there? Is it in the right voice? Half the pieces of that episode failed the first time.

FRANK: Half!

ALICE: Half. A line in your voice that should've been mine. A sentence that came out garbled. And the agent never noticed any of that by itself. The checker did. And that's the whole story of long tasks, really. A long job isn't one big effort. It's hundreds of small steps, and every one of them can go a little wrong.

## Welcome

FRANK: Welcome to From Zero to ChatGPT, season two. I'm Frank.

ALICE: And I'm Alice. Last time was memory. How an agent that forgets everything overnight can pick up where it left off.

FRANK: And today we put it all to work on a long job. Why small mistakes pile up, how you'd even measure how long a task an agent can handle, and what a harness does to keep it on track for hours. Okay, Alice, I'll start with the bad news.

## Small mistakes pile up

FRANK: So, here's a bit of arithmetic, and I promise it's the only bit. Say an agent is really good. Ninety-nine times out of a hundred, each step goes right. Read the file, right. Run the test, right. Make the change, right.

ALICE: That sounds great.

FRANK: For one step, it's great. Now chain a hundred steps together, where each one has to go right. How often does the whole thing go right?

ALICE: Uh... less than ninety-nine percent, obviously. Ninety?

FRANK: About thirty-seven percent.

ALICE: What? From ninety-nine?

FRANK: From ninety-nine. Every step takes off a little bit, and it multiplies. A hundred steps at ninety-nine percent is barely better than one chance in three. And five hundred steps, which isn't a lot for a big job, is less than one percent.

ALICE: Okay, that's grim. But real mistakes aren't all fatal, are they? People make mistakes on long jobs and still finish.

FRANK: Right, and that's the key. The arithmetic assumes nobody notices. A person makes a mistake, sees something odd, goes back. So the question for a long task isn't really "never make a mistake". It's "notice your mistakes, and recover".

ALICE: And models are bad at noticing?

FRANK: Worse than you'd hope, for a reason we've seen before. Remember contextual inertia, from the pressing-Enter episode? The model rereads everything it's done so far. So if it took a wrong turn an hour ago, that wrong turn is sitting right there on the desk, looking like part of the plan. The model tends to build on it, not question it.

ALICE: It trusts its own earlier work.

FRANK: It trusts its own earlier work. And Anthropic, building a harness for agents that write whole apps over many sessions, saw two failures again and again. One, the agent tries to do everything at once. It starts building the whole app in one go, runs out of room on its desk halfway through, and the next session finds a half-built mess with no notes.

ALICE: And the other?

FRANK: The other is my favorite. It looks around, sees that a lot has been done, and declares the job finished. When it isn't.

ALICE: The "looks good to me" problem.

FRANK: Exactly that. And both of those are really the same thing. The agent's sense of where it is in the job is off, and nothing outside it is correcting it. Okay. So before we fix it, how would you even measure this? How long a job can an agent handle? Alice, that's yours.

## How long a task?

ALICE: So there's a research group called Meter, spelled M E T R, who measure what AI can do, and in twenty twenty-five they came up with a really clever yardstick. Instead of asking "how hard is this task", which is vague, they asked "how long does it take a skilled person?"

FRANK: Like, timing an expert.

ALICE: Exactly. They collected a bunch of tasks, mostly software and research tasks. Some take a person a few seconds, like, which of these files is the config file? Some take many hours, like, build and debug a whole small system. And they timed real experts doing them. So every task gets a length, in human time.

FRANK: Okay. And then they give them to the models.

ALICE: Then they give them to the models, as agents, with tools, and see which ones they finish. And of course, models do well on short tasks and badly on long ones. So for each model, you can ask: how long a task does it finish half the time? That's its time horizon.

FRANK: Half the time. Why half?

ALICE: It's just where the measurement is most precise. Hang on to that, it matters. So, here's what they found. GPT two, from twenty nineteen, could basically only do tasks that take a person a few seconds. GPT four, in twenty twenty-three, about four minutes. By early twenty twenty-five, Claude three point seven Sonnet, about an hour.

FRANK: So that's going up fast.

ALICE: It was doubling about every seven months, from twenty nineteen to twenty twenty-five. That was the headline of the original paper. Like the scaling laws, a straight line on the right kind of chart.

FRANK: And now?

ALICE: Now it's faster. Meter keeps the chart updated, with a bigger set of tasks. In their current numbers, from twenty twenty-three on, it's doubled about every four months. And the best model in their latest data, from April this year, finishes about half of the tasks that take an expert around seventeen hours.

FRANK: Seventeen hours. That's two working days.

ALICE: But, big but, the error bars are huge at that end. Their range runs from about eight hours to more than two days. They just don't have many tasks that long, because it's really expensive to time people doing a task for two days.

FRANK: Okay, so here's my pushback. Half the time. If I hired someone who finished a two-day job only half the time, I'd be pretty unhappy.

ALICE: And that's why I said hang on to it. Meter also measures where models succeed eighty percent of the time. And that's much shorter. For that same model, about three hours, not seventeen.

FRANK: Oh, that's a big difference.

ALICE: Big difference. And there are more catches. These are mostly software tasks. They're neat, clearly described, with an automatic way to score them. Real work is messier. The instructions are vague, the goal changes, there's nobody to tell you if you did it right. Meter found models do worse on messier tasks.

FRANK: So it's a ruler, not a forecast.

ALICE: It's a ruler. A really good one, because it's in units everybody understands. But a model's time horizon is not "how long it can work alone at your company". In the original paper, they did say that if the trend holds, and if it carries over to real work, then within about five years agents could do many software tasks that take people a month.

FRANK: Two big ifs.

ALICE: Two big ifs. But even with the ifs, it's a remarkable line. Frank, back to you. How do you stop the mistakes piling up?

## A second pair of eyes

FRANK: Right. So the obvious idea is, just ask the model to check its own work. Write the answer, then say, "review that, and fix any mistakes".

ALICE: That's what I'd do.

FRANK: That's what everyone tried. And a team at Google DeepMind tested it on reasoning problems, in twenty twenty-three. Their paper's title says it all. "Large Language Models Cannot Self-Correct Reasoning Yet."

ALICE: Cannot? At all?

FRANK: Without outside help, not reliably. When the model reviewed its own answer with nothing new to go on, it often didn't get better. And sometimes it got worse. It would talk itself out of a right answer.

ALICE: Huh. So it's like proofreading your own essay. You read what you meant, not what you wrote.

FRANK: Exactly. The same blind spots that made the mistake are doing the checking. And remember, these models were trained to please. The robot food critic, from the end of season one. So "are you sure?" can make it cave, even when it was right.

ALICE: Okay, so what does work?

FRANK: Something from outside. A signal the model didn't make up. The best ones are things that can't be argued with. The code either runs or it doesn't. The tests pass or they don't. The file is there or it isn't. And our renderer is exactly this. The model that makes the audio doesn't judge its own work. A different model, Whisper, listens and writes down what it hears. And a third one checks the voices.

ALICE: A second pair of ears.

FRANK: A second pair of ears. And when there's no test, a separate model, given a fresh desk and asked to find problems, does better than the same model rereading its own work. Fresh eyes, literally.

ALICE: But wait. The reasoning episode had a problem with this. The model that fudged the tests. If you check with tests, won't it just learn to cheat the tests?

FRANK: Yes! And that's why the checking has to be protected. In Anthropic's long-running harness, there's a big list of features the app needs, each one marked "doesn't pass yet". The agent's only allowed to change that mark, to "passes". And the instructions say, and I love how blunt this is, "It is unacceptable to remove or edit tests."

ALICE: Because otherwise the easiest way to pass a test is to delete it.

FRANK: Exactly. And they found one more thing. At first the agent would build a feature, run a quick check, and mark it done. And it wasn't really done. When it clicked through the app in a real browser, like a user would, it found far more of its own bugs.

ALICE: So the check has to be like the real thing.

FRANK: The check has to be like the real thing. A quick look isn't a check. Okay, Alice. Now put it all together. How do you build a harness for a job that takes days?

## The shift change

ALICE: So, Anthropic's picture for this is a factory with shifts. Each session is a new engineer arriving for a shift, who knows nothing about what happened before. How do you run a project like that?

FRANK: Very good handover notes.

ALICE: Very good handover notes, and a few rules. In their harness, the very first session is special. It doesn't build anything. It sets up the job. It writes out the full list of features, over two hundred for one app, each marked not done yet. It writes a little script to start everything up. It starts a progress file. And it saves the first version of the project.

FRANK: So the first shift just plans.

ALICE: The first shift plans. And every shift after that follows a routine. Check where you are. Read the progress file. Read the history of saved changes. Look at the feature list. Start the app. Run a quick test to make sure nothing's broken. And only then, pick one feature. Just one.

FRANK: One at a time. That's the fix for trying to do everything at once.

ALICE: Exactly. Build it, test it properly, mark it done, save the change with a clear note, update the progress file. Then the next shift picks the next one. And because every change is saved, if something breaks, you can go back to the last version that worked.

FRANK: And the feature list is the fix for declaring victory early.

ALICE: Right! It's hard to say "all done" when there's a list of two hundred things, and a hundred and forty still say "doesn't pass".

FRANK: Okay, and our podcast?

ALICE: Ours is the same thing, smaller. The status section in our instruction file is the progress file. Every segment of audio is saved as it finishes, so a dead job loses at most a few minutes. The checker writes a log of every problem. And when a whole run is done, there's a list of problem lines for our listener to decide on.

FRANK: And did it all work perfectly?

ALICE: Of course not. Here's a good one. When a job got stopped at the two-hour limit, the last log lines were lost. They were waiting in a buffer, and never got written. So for a while, only about twenty-six of sixty-five pieces had a check on record. For the rest, nobody could tell whether they'd passed.

FRANK: The harness had a bug.

ALICE: The harness had a bug. One small setting, fixed in one line. But it's the lesson from the agent episode again. Remember the team that built a million lines with agents? When the agent kept failing at something, they didn't just fix it. They asked, what's missing from the harness that would let it get this right? A long task isn't just a smarter model working longer. It's a model, plus a list, plus notes, plus checks it can't argue with.

FRANK: And somebody checking the checks.

ALICE: Always.

## Recap

FRANK: Okay, recap. Alice, you start.

ALICE: One. Small mistakes multiply. Ninety-nine percent per step is about thirty-seven percent over a hundred steps. So long tasks are about noticing mistakes and recovering, not never making them. And models tend to trust their own earlier work, wrong turns included.

FRANK: Two. Meter measures an agent by the length of task, in an expert's time, that it finishes half the time. It doubled about every seven months from twenty nineteen to twenty twenty-five, about every four months since twenty twenty-three, and the best model in their latest data is around seventeen hours. With huge error bars.

ALICE: Three. Read that carefully. At eighty percent success, it's more like three hours. The tasks are neat software tasks, and messy real work is harder. A ruler, not a forecast.

FRANK: Four. Checking your own work, with nothing new to go on, often doesn't help, and can make things worse. A signal from outside does. Tests, a fresh model, a second pair of ears. And protect the checks, so the agent can't just delete the tests.

ALICE: And five. Long jobs run like shifts. A first session that plans and writes the list. Then one feature at a time, with a routine at the start of each shift, a progress file, saved versions, and real tests. That's how this podcast gets rendered too.

FRANK: Next time, more than one agent. What happens when agents work together, and when they stop typing commands and start clicking around a screen like we do.

ALICE: See you then.
