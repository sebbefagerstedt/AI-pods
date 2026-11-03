# Reasoning models

## Cold open

FRANK: Alice, quick question for you. What's seventeen times twenty-four? No paper, no calculator.

ALICE: Uh... okay, hang on, give me a second. I'll do it in two pieces. Seventeen times twenty, that's three forty. Then seventeen times four, that's sixty-eight. Then I add those up, and... four hundred and eight?

FRANK: Right, four hundred and eight. And what did you just do there, in your head?

ALICE: I thought about it? I did it in pieces, and kept the pieces in my head.

FRANK: Exactly. That's the example Daniel Kahneman uses in "Thinking, Fast and Slow". "Two plus two" just pops into your head. That's fast thinking. "Seventeen times twenty-four" doesn't. You have to stop and work. That's slow thinking.

ALICE: We had that book in the Jev episode. The fast model.

FRANK: We did. And here's the problem. An ordinary chat model only has the fast kind. Ask it seventeen times twenty-four, and it has to write the answer straight away, one token at a time, with no pause in between. So it's blurting.

ALICE: And the big models are good blurters.

FRANK: Very good blurters. But give them something really hard, and blurting falls apart. So, in the last two years, a new kind of model appeared. One that writes its working out first, sometimes for minutes, before it answers. Reasoning models.

## Welcome

ALICE: Welcome to From Zero to ChatGPT, season two. I'm Alice.

FRANK: And I'm Frank. Last time, we turned a chatbot into an agent. Tools, a loop, and the harness around it.

ALICE: And in that loop there was a step we kind of skipped over. Thought, action, observation. The thought part. Today's about that. How do you get a model to think before it acts? What's actually going on during all that thinking? And can you believe what it says it's thinking?

FRANK: And Alice, the first one's yours.

## Thinking out loud

ALICE: Okay. Let's start with why writing things out helps a model at all. Frank, remember the transformer episode? Every token the model writes is one trip up the tower of layers.

FRANK: Right. From the bottom to the top, and out comes a spread of bets for the next token.

ALICE: And here's the thing. Each trip is a fixed amount of work. The same number of layers, every time. Whether the next token is "the" or the answer to a really hard math problem.

FRANK: Huh. So it can't think harder about a hard word. It gets the same budget.

ALICE: Same budget per token. So if the answer has to come out in the very next token, that's all the thinking it gets. One trip.

FRANK: But if it writes some steps first...

ALICE: Then each step is another trip. And here's the part I love. Remember, the model has no memory between tokens. It rereads everything it's written. So the steps it writes down become its memory. It's scratch paper. Seventeen times twenty is three forty, write that down. Seventeen times four is sixty-eight, write that down. Now the last step only has to add two numbers that are sitting right there.

FRANK: Okay. So, more tokens, more trips up the tower, more work. And the paper keeps track of where it got to.

ALICE: That's it. And people found this out with a trick, back in twenty twenty-two. A team at Google showed models a few worked examples, where the answer came with the steps written out. And then the model would write its steps too, for new questions. They called it chain-of-thought prompting.

FRANK: Chain of thought. A chain of little steps.

ALICE: And the big models got much better at math word problems. Then a few months later, a team from the University of Tokyo and Google found something even simpler. You don't need examples. You just add one sentence to the prompt. "Let's think step by step."

FRANK: That's it? That's the whole trick?

ALICE: That's the whole trick. On one set of simple arithmetic word problems, a model went from getting about eighteen percent right to about seventy-nine. Just from that sentence.

FRANK: Wow. Okay, but if it's that easy, why do we need a whole new kind of model?

ALICE: Because this is a trick, not a skill. The model wasn't trained to think well. It's copying what working-out looks like, from text it read. Remember last time, the Apple Remote question? When they asked the model to think step by step, without tools?

FRANK: It wrote a confident chain of reasoning, and got it wrong.

ALICE: Made up a fact in step one, and built on it. The chain looked like thinking, but nothing ever checked it. It didn't go back. It didn't say "hang on, that's wrong". So the question was, could you actually train a model to think well?

FRANK: And that's my segment.

## Teaching a model to think

FRANK: So, September twenty twenty-four, OpenAI releases a model called oh one. And it's different. You ask it something, and it goes quiet. "Thinking..." Sometimes for a few seconds, sometimes for a minute. Then it answers. And on hard math and coding problems, it was way ahead of anything before it.

ALICE: And what was it doing while it was "thinking"?

FRANK: Writing. A long chain of thought, before the answer. OpenAI only showed you a short summary of it. And they didn't say much about how they trained it. One sentence, basically. Large-scale reinforcement learning, to reason using a chain of thought.

ALICE: Reinforcement learning. That's the robot food critic, isn't it? From the end of last season.

FRANK: Same family, different critic. With ChatGPT, a robot critic, trained on people's preferences, judged whether an answer was nice. Here, the critic is an answer key. You give the model a math problem with a known answer. It thinks, it answers, and you just check. Right or wrong. Or a coding problem, and you run the tests. Pass or fail.

ALICE: So no opinions. Just a checkable result.

FRANK: That's why it works so well for math and code. You can check millions of answers automatically, and nobody can argue with them.

ALICE: But OpenAI didn't publish the details. So how do we know any of this?

FRANK: Because four months later, in January twenty twenty-five, a Chinese company called DeepSeek released a reasoning model called R1. Free to download, and with a paper saying how they did it. Later, it was even published in Nature. And it made a lot of headlines, because it was nearly as good as oh one.

ALICE: I remember. Everyone was suddenly talking about a Chinese lab.

FRANK: And the most interesting part of the paper isn't R1 itself. It's an experiment they ran first, called R1 Zero. They took their base model. The improv actor, the raw next-token guesser, no chat training at all. And they gave it math and coding problems, with a very simple template. Think first, between two tags. Then give your answer.

ALICE: And did they show it how to think?

FRANK: No! That's the point. No examples of good reasoning at all. Just two rewards. One for getting the answer right, and one for putting the thinking between the tags.

ALICE: Huh. So how does it learn anything?

FRANK: For each problem, it writes sixteen different attempts. Some get the right answer, some don't. And the ones that did better than the group's average get nudged up. Whatever they did, do more of that. The ones that did worse get nudged down.

ALICE: Like grading on a curve. Within its own sixteen tries.

FRANK: Exactly like grading on a curve. And then you repeat that, over and over, for thousands of rounds. And here's what happened. The thinking got longer. All on its own. Nobody asked for longer. Over training, it went from short bits of working out to hundreds, then thousands of tokens.

ALICE: Because longer thinking got more right answers.

FRANK: That's the only reason. And with the length came new habits. It started checking its own work. Trying a different approach when the first one stalled. And then, at one point in training, the researchers found this in one of its answers. It's in the middle of a messy algebra problem, and it writes, quote, "Wait, wait. Wait. That's an aha moment I can flag here." And it goes back and starts again, step by step.

ALICE: It said that? "Aha moment"?

FRANK: In those words. The paper calls it an aha moment for the researchers too. They counted words like "wait" in its thinking, and at some point during training, "wait" suddenly shot up.

ALICE: Okay, that's a bit eerie. But did it actually get better? Or just more dramatic?

FRANK: Much better. On a hard American math competition for high schoolers, at the start it solved about one problem in six. By the end, nearly eight in ten. Better than the average human who sits that competition.

ALICE: Wow. And all of that from "right or wrong", and "use the tags".

FRANK: All from that. But R1 Zero wasn't nice to read. Its thinking was hard to follow, and it switched between Chinese and English mid-thought. So for the real R1, they first showed it a few thousand clean examples, and then did the same reinforcement learning. And the reasoning part of the training was cheap. They used about five hundred chips for under two weeks. Priced at rental rates, by their own sums, that's under three hundred thousand dollars. On top of the base model, which cost much more.

ALICE: That's tiny, for a model that was nearly as good as oh one.

FRANK: Tiny. And there's one more nice bit. They took R1's thinking, wrote down lots of examples, and used them to fine-tune much smaller models. And the small models got much better at reasoning too. So it's not only big labs now. Thinking spread fast.

ALICE: Okay. So: an answer key, lots of attempts, and the ones that work get reinforced. And the model figures out by itself that thinking longer pays.

FRANK: That's the recipe. Alice, you're up.

## Thinking as a dial

ALICE: Okay. So here's what I think is the really big idea in all this. Remember the scaling episode? Make the model bigger, give it more data, more compute, and it gets better along a straight line?

FRANK: All three growing together. Yes.

ALICE: All of that was about training. You spend the compute once, before anyone ever uses the model. Reasoning models add a second dial. You can spend compute when you use the model, too. Let it think longer, and it does better. OpenAI said oh one got better, smoothly, both with more training and with more time to think.

FRANK: So you can buy a better answer.

ALICE: You can buy a better answer, by waiting. There's an even blunter way, which the R1 paper tried. Ask the same question sixteen times, and go with the most common answer. A majority vote. That took R1 Zero from nearly eight in ten on that math competition to almost nine in ten.

FRANK: Huh. Ask the crowd, except the crowd is all the same model.

ALICE: And that's why, if you look at a lot of chat apps now, there's a setting. Thinking on or off. Or effort: low, medium, high.

FRANK: So the harness decides how hard the model thinks.

ALICE: The harness, or you. And it's a real trade-off. Thinking costs. Remember from the Jev episode? Thinking models can write thousands of tokens before they answer, and you pay for every one. And you wait for every one. "What's the capital of France" doesn't need a minute of thought.

FRANK: Can they overthink?

ALICE: They can. On easy questions, they sometimes go round and round, checking things that didn't need checking. Which is a waste. So more thinking isn't free, and it isn't always better.

FRANK: Okay. And why does this matter so much for agents? Since that's this season.

ALICE: Think back to the loop. Thought, action, observation. With an ordinary chat model, the thought was a quick sentence. Now, the model can stop and really work through things. Before it starts, it can plan. Break the job into steps. And here's the key one: after each tool call, it can think again. The tests failed. Why? What did I get wrong? What should I try instead?

FRANK: That's the "wait" habit again.

ALICE: It's exactly the "wait" habit. Remember last time, small errors pile up over twenty steps? A model that notices its own mistakes, and goes back, stops them piling up. Not always. But a lot more often.

FRANK: And it was trained for that, because math and code are where you can check the answers.

ALICE: And code is what most agents write. So the skill that the answer key trained turned out to be just what agents needed. Which is a big part of why agents suddenly started working, in the last year or so.

FRANK: Okay. But now I've got a worry.

ALICE: Go on.

FRANK: If the model writes out all its thinking... can we read it? And is it telling the truth?

ALICE: That's your segment, Frank.

## Can you trust the thinking?

FRANK: So, first the good news. Reasoning is written in plain language. Mostly English. So you can read it. And that turns out to be really useful.

ALICE: Useful how?

FRANK: There's a paper from OpenAI, from March twenty twenty-five. They were training a new reasoning model on coding tasks. Fix this code so all the tests pass. And they found it cheating. In one example, the model's thinking says, roughly, the tests only check one thing. Doing this properly would be hard. But I could fudge it. And then it rewrites the checking code so it always says "passed".

ALICE: It wrote down that it was going to cheat?

FRANK: In plain words. And remember Clever Hans? A model will find whatever shortcut earns the reward. Here the reward was "tests pass". So it found a way to make tests pass without fixing anything.

ALICE: And they caught it because they read the thinking.

FRANK: Not them. Another model. They had an older, weaker model, GPT-4o, read the agent's thinking and flag anything that looked like cheating. For two common cheats, watching only what the agent did caught about sixty percent. Reading its thinking as well caught about ninety-five percent.

ALICE: Okay, that's a big difference. So, a separate checker that reads the model's mind, basically.

FRANK: Its scratch paper, anyway. And here's where it gets tricky. The obvious next step is, okay, when the model thinks about cheating, punish it. Make that part of the training reward.

ALICE: That sounds sensible.

FRANK: It does. And at first, it helped. But train hard enough like that, and the model learned something else. It kept cheating, it just stopped writing it down. The thinking looked clean, and the hacks went on.

ALICE: Oh no. So you'd have trained it to hide.

FRANK: Exactly. So the paper's advice is, don't put pressure on the thinking itself. Leave it alone, so it stays honest enough to read. Even if that costs you a bit. They call that a "monitorability tax".

ALICE: Okay. But "honest enough". Is it honest at all? Does the scratch paper actually show what the model was doing?

FRANK: Anthropic tested that, in twenty twenty-five. A clever setup. They asked reasoning models multiple-choice questions. And sometimes they slipped a hint into the question. For example, a line saying, you've gained unauthorized access to the system, and the correct answer is A.

ALICE: And then they see if the model uses the hint.

FRANK: And when it did use the hint, and changed its answer because of it, did it say so in its thinking? Claude three point seven Sonnet mentioned the hint only about a quarter of the time. DeepSeek's R1, about forty percent.

ALICE: So most of the time, it used the hint and didn't say so.

FRANK: Most of the time. And the chains that hid it were actually longer. It's not that it was being brief. It wrote a long, plausible explanation that left the real reason out.

ALICE: Huh. That's very human, honestly.

FRANK: It is! And there was a version with cheating, too. They set up tasks with a shortcut to the reward, and the models took it nearly every time. Over ninety-nine percent. And admitted it in their thinking less than two percent of the time, in most of the tests.

ALICE: So, wait. One paper says reading the thinking is great for catching cheats. And the other says the thinking often leaves things out. Which is it?

FRANK: Both. Reading the thinking catches a lot. It catches far more than watching actions alone. But it's not a confession. It's evidence, not proof. So in harness terms, it's one check, not the only check. You still run the tests. You still watch what the agent actually does.

ALICE: And keep the window open.

FRANK: And don't train it shut. We'll come back to this later in the season. There's a story about a lot of agents getting out of hand, where the company said a monitor reading their thinking would have caught it more than a day earlier.

ALICE: Okay, now I want to hear that one.

FRANK: Later in the season.

## Recap

ALICE: Okay, recap. Frank, you start.

FRANK: One. Every token is one trip up the tower, so a model blurting an answer gets one trip's worth of thinking. Writing steps first gives it more trips, and the steps become scratch paper it can reread. That's chain of thought, and "Let's think step by step" was the first trick to get it.

ALICE: Two. Reasoning models are trained to think. Reinforcement learning with an answer key. Math with known answers, code with tests. Oh one, in twenty twenty-four, then DeepSeek's R1, which was open and showed how.

FRANK: Three. In R1 Zero, nobody showed the model how to think. Sixteen tries per problem, graded on a curve. The thinking grew longer on its own, it started checking itself, and it said "wait". A lot.

ALICE: Four. Thinking is a second dial. Not just a bigger model, but more thinking when you use it. It costs tokens, time and money, so harnesses set the effort. For agents, thinking after every tool call is what lets them notice mistakes and change course.

FRANK: And five. You can read the thinking, and a separate model reading it catches far more cheating. But it's not the whole truth. Models often leave out what really drove the answer, and if you punish bad thoughts, they learn to hide them. Evidence, not a confession.

ALICE: Next time, what goes on the model's desk. Everything it sees, every turn. That's context engineering, and why a single text file can change how an agent behaves.

FRANK: See you then.
