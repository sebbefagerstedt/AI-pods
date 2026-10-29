# Bonus: Jev, the model that doesn't write

## Cold open

FRANK: Okay, there's a demo video I keep thinking about. Someone's playing Doom, the old nineties shooter. Except no person is playing. An AI is. Ten times a second, the game describes what's going on, in text, and asks an AI model what to do next.

ALICE: Ten times a second? That can't be a chat model. When I ask ChatGPT something tricky, it thinks for, what, ten seconds? Twenty?

FRANK: Right. By the time it had worked out its first move, game over. It's a model called Jev, from a small company called TypeSafe, out since September. And to be fair, they admit a regular game bot would play better. The point is the speed. On the tasks it's built for, TypeSafe says Jev is up to two hundred times faster than a chat model. And more than four hundred times cheaper.

ALICE: Two hundred times. Okay, that's the episode, then. What is it, and how is it that fast?

FRANK: And is it real.

## Welcome

ALICE: Welcome to From Zero to ChatGPT. I'm Alice.

FRANK: And I'm Frank. This is a short bonus episode, before the next season starts.

ALICE: Because a listener asked us about Jev, with a really good question. Is it only the output layer that's different? So instead of tokens, you get one of three kinds of answers?

FRANK: Which is exactly where we'll end up. But first, what Jev is.

## What Jev is

FRANK: TypeSafe calls it a "System One" model. Does that ring a bell?

ALICE: Thinking, Fast and Slow? The Kahneman book?

FRANK: That's the one. System 1 is your fast gut reaction. You glance at a face and you just know it's angry. System 2 is the slow working-out. Seventeen times twenty-four. The thinking chat models are the System 2 kind. They write out a whole page of reasoning before they answer. Jev is built for gut calls. The sort of judgment a knowledgeable person makes in a second or two.

ALICE: Like what?

FRANK: An email comes in to customer support. Is it about billing, a technical problem, or the account? Is the customer angry? Do they want a refund?

ALICE: So, sorting things.

FRANK: Sorting, routing, scoring, checking. And here's the first big difference. Jev never writes. Not a single word. You hand it two things. The situation, which they call the state. The email, say. And your questions, each with the possible answers already written out. By you.

ALICE: So it's a multiple choice test.

FRANK: Basically. The answer always comes from your list, along with how sure it is. And that's where the three kinds come in. One: a Choice. Pick one option from a list. Billing, technical, or account. You get the pick, plus a probability for each option. Billing ninety percent, technical eight, account two.

ALICE: The spread of bets again.

FRANK: The spread of bets! But over your options, instead of every token it knows. Two: a Score. A position on a scale you describe. Zero is calm, one is annoyed, two is furious. And it can land in between. One point four, a bit past annoyed.

ALICE: And three?

FRANK: Three is a yes-or-no question. They call it a Noul. Does this email ask for a refund? You get back one number: the chance that the answer is yes. Ninety-five percent, say.

ALICE: Huh. Wait, so that's really the same thing three times.

FRANK: Pretty much. All three are a spread of bets over a short list. Two items for yes or no. Your options, for a Choice. And for a Score, the levels are in order, so you can take the average position. That's the one point four.

ALICE: And "how sure it is"?

FRANK: Choices and Scores also come with a confidence number, from zero to one. Everything bet on one option, that's one. Spread out evenly, zero. So your code can act on it. Confident? Go ahead. Not sure? Pass it to a person.

ALICE: Which only works if the odds are honest.

FRANK: Exactly. When it says eighty percent, it should be right about eighty percent of the time. That's called being calibrated, and it's what Jev is trained for. There's also a newer, fourth type, for finding things in pictures, but TypeSafe says that one isn't ready for serious use yet. Alice, the speed is yours.

## Why it's so fast

ALICE: Okay. To see why Jev is fast, we have to remember why a chat model is slow. Frank, from the episode about pressing Enter. What happens?

FRANK: The model reads your message, goes up the tower, and at the top it bets on the next token. One gets picked. Then it does the whole thing again, with that token added. One token, one trip up the tower.

ALICE: And the trips can't overlap, because each one needs the token before it. Now, here's the thing. The reading part is actually quick. Your whole message goes up the tower in one go, all the words side by side, just like in training. It's the writing that's slow. And thinking models write a lot. Before they answer, they reason it out. Hundreds, sometimes thousands of tokens you might never even see. A thousand tokens is a thousand trips up the tower. One after the other.

FRANK: Even if all you wanted was the word "billing".

ALICE: Even then. Now, Jev does the reading part, the quick part. And then it just stops. No writing. It reads the answers straight off the top, all at once: the bets on your options. In the open copy we'll get to in a minute, that's one trip up the tower.

FRANK: So it's not a faster reader. It just skips the writing.

ALICE: That's the big one. And there's a second trick. Say you've got ten questions about the same email. Jev reads the email once, and then answers all ten side by side. Each one on its own, so one answer can't sway the next.

FRANK: Like a panel of judges holding up their scorecards at the same time.

ALICE: Nice. Instead of one judge going down the list. TypeSafe says adding questions barely changes the response time.

FRANK: So, actual numbers?

ALICE: TypeSafe says Jev answers in seventy to five hundred milliseconds. At most half a second. The top chat models in their comparison took from three seconds to over five minutes. And Jev charges only for what it reads. Four point two cents per million tokens. What it says back is free.

FRANK: Free?

ALICE: It's just a few numbers. Nothing to meter. With chat models, the writing is the expensive part. Output tokens cost several times more than input.

FRANK: And that "two hundred times faster"?

ALICE: That's from TypeSafe's own tests, on four workflows their team built, and they say themselves it's probably on the high end. In one demo, they raced chat models with the thinking switched off, and there the speedup was a lot smaller. There's also an independent test, which we'll get to. Frank, the listener's question is yours. What's actually inside?

## What's inside

FRANK: So, is it only the output layer? Short answer: that's the part you can see, but it's not the only part. And first, a caveat. TypeSafe hasn't said how Jev is built. A new architecture, a new way of sampling, a new kind of training. That's about all they say.

ALICE: A secret recipe.

FRANK: A secret recipe. But someone has cooked a copy. Perplexity, the AI search company, released a decision model called the Decider. And this one is open. The weights and the code are public, and the training data is listed. A community leaderboard of these models lists it as an open reproduction of Jev.

ALICE: So we can look inside the copy.

FRANK: We can. It changes three things, and you already know all three. It starts from an ordinary open language model, from Alibaba. Twenty-seven billion knobs. The usual tower. Embeddings at the bottom, sixty-four floors, the notepad.

ALICE: The same tower as a chat model.

FRANK: Same tower. Change one is the one our listener guessed. The output layer. Normally, at the top, the model holds the notepad up against every token it knows, about a quarter of a million here, and scores them all. The Decider swaps that for a much smaller layer. Two hundred and fifty-five slots.

ALICE: Slots for what?

FRANK: In the prompt, each of your options gets a short label. A, B, C, and so on. One slot per label, and only the labels you actually used count. Jev has the same limit, by the way. Two hundred and fifty-five options.

ALICE: Hang on. Didn't GPT-1 do something like this?

FRANK: It did! For fine-tuning, GPT-1 added one tiny piece on top, to turn what the model had worked out into an answer. Positive or negative. Same idea, eight years later. With one big difference. Back then, you trained a new top piece for every task. Here, one model takes any question. You just write the options in plain words.

ALICE: Okay. Change two?

FRANK: The no-peeking rule.

ALICE: The writer can't look ahead.

FRANK: Right. And that rule is only there because a writer would cheat. It could just look at the word it's supposed to guess. But a decision model never writes, so there's nothing to cheat on. So Perplexity switched the rule off. Not on every floor, this model mixes two kinds of floors. But on one floor in four, the ones with full attention, every word can now look both ways.

ALICE: Like Bert. The reader.

FRANK: Like Bert. And here's my favorite part. Perplexity says that change, together with more training data, brought most of the improvement in their latest version.

ALICE: So the writer turned back into a reader.

FRANK: Pretty much. And change three is training. The whole model is retrained, every knob, not just the top. On about six hundred thousand questions with known answers, mostly from public datasets. TypeSafe has its own training method for Jev. They call it RLCD. Reinforcement learning for calibrated decisions.

ALICE: As opposed to RLHF.

FRANK: Right, the robot food critic from the ChatGPT episode. RLHF rewards answers people like. Which, TypeSafe argues, can reward flattery and confident-sounding mistakes. RLCD rewards honest odds. And here's a fun bit. One of TypeSafe's founders, Diogo Almeida, was an author of InstructGPT. The RLHF work behind ChatGPT.

ALICE: So someone who helped build the chatbot went and built the opposite.

FRANK: Something like that. So, the answer to the question. In the open copy, the output layer is one of three changes. A small answer layer, no no-peeking rule, and the whole model retrained for honest odds. Jev's own recipe may be different. We just don't know. Alice, this last one's yours. What's the catch?

## The catch

ALICE: The catch. First, TypeSafe says Jev can't hallucinate. And that's true, in a narrow sense. It can't answer something that isn't on your list, or give you an answer in the wrong format, the kind that breaks the code reading it. But it can still pick the wrong option. It can't go off the menu. It can still order the wrong dish.

FRANK: Okay, that's fair.

ALICE: Second, the independent test. Two researchers at the University of Pennsylvania used Jev, and the Decider, as graders, marking answers against a checklist. That's a job chat models often do. And they compared them with three of the fast, cheaper chat models. Next to Jev, the chat models cost sixteen to over three hundred times as much, and took about thirty to three hundred and fifty times as long.

FRANK: And accuracy?

ALICE: Mostly a match. Out of twenty-seven head-to-head comparisons, Jev was clearly worse in at most six. But here's the twist. When Jev was confidently wrong, the chat models made the same mistake ninety-six percent of the time. If their mistakes were independent, you'd expect about half.

FRANK: Wrong in the same places.

ALICE: That's the paper's title, more or less. Cheaper, faster, and wrong in the same places. And it matters, because the obvious plan is to let Jev answer first, and pass the unsure cases to a chat model. That saved money. But it barely helped accuracy. Two point seven points, at best.

FRANK: Because the backup makes the same mistakes.

ALICE: Exactly. And third, TypeSafe publishes its own list of weak spots, which I like. Jev reads your question very literally. It can't count, so keep the math in your code, and the date comparisons too. Questions that need several steps trip it up, and so do long inputs full of irrelevant stuff. Text written to trick it can sway it. And it leans a little towards the first option in a list.

FRANK: So, gut calls only.

ALICE: Gut calls only. Their advice is to break a big judgment into small questions, and let your code combine the answers. Not "rate this startup pitch", but how big is the market? Is it doable? Is it different?

FRANK: Code in charge, model for the gut calls. Which is a nice bridge to next season.

ALICE: It is. Oh, and the name. Jev is named after William Stanley Jevons, a nineteenth-century economist who noticed that when steam engines got more efficient, Britain burned more coal, not less. TypeSafe's bet is the same: make intelligence cheap enough, and we'll use it everywhere.

## Recap

FRANK: Okay, recap. One. Jev is a "System One" model. Fast gut calls, no writing. You give it the situation and your questions, with the answers listed, and it bets on your options.

ALICE: Two. Three kinds of question. A Choice picks one option, with the odds for each. A Score places it on a scale you describe. And a Noul gives the chance of a yes. All three are a spread of bets over a short list, with a confidence number, so your code knows when to ask a person.

FRANK: Three. It's fast because it skips the writing. One trip up the tower, instead of one per token, and thinking models write thousands. It reads the situation once and answers every question side by side. And you only pay for the reading.

ALICE: Four. Jev's recipe is secret. The open copy changes three things. A tiny answer layer instead of the whole vocabulary. No no-peeking rule, so it reads both ways, like Bert. And the whole model retrained for honest odds. So, not only the output layer.

FRANK: And five. It can't go off the menu, but it can order the wrong dish. In the independent test, it was far cheaper and faster than fast chat models, often just as accurate, and wrong in the same places.

ALICE: Next time, a new season. What happens when you put a model inside a bigger piece of software, give it tools, and let it act.

FRANK: See you then.
