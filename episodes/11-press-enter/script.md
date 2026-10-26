# Episode 11: What happens when you press Enter

## Cold open

FRANK: Okay, picture this. New York, 2023. A man named Roberto Mata is suing an airline. On a flight a few years earlier, a metal serving cart had banged into his knee. And his lawyer, someone who'd practiced law for about thirty years, files a brief with the court. Full of earlier cases, to back up his argument.

ALICE: Sounds normal so far.

FRANK: Totally normal. Except the airline's lawyers go looking for those cases. And they can't find them. The judge can't find them either. Because at least six of them don't exist. Made-up cases, with made-up quotes from made-up judges.

ALICE: Let me guess. ChatGPT.

FRANK: ChatGPT. The lawyer had used it for his research. And here's the part that gets me. He had actually tried to check. He asked ChatGPT, "Is this a real case?" And it said, yes, it's a real case. It even said you could find it in the big legal databases.

ALICE: Oh no.

FRANK: The judge fined him and his colleague five thousand dollars. And the lawyer told the court he had no idea ChatGPT could just make things up. He thought it was, basically, a super search engine.

ALICE: Which is a really easy mistake to make, honestly. It sounds so sure of itself.

FRANK: It does. And to understand why it does that, why it'll invent a court case and then swear it's real, you have to understand what actually happens when you type your question and press Enter. Which is today.

## Welcome

ALICE: Welcome to From Zero to ChatGPT. I'm Alice.

FRANK: And I'm Frank.

ALICE: So, last time, we climbed the transformer, floor by floor. We followed a word all the way up to the output layer. And what comes out of the top is a spread of bets. A probability for every possible next token. "Mat", forty percent. "Floor", twenty.

FRANK: And we stopped there. With bets, not words.

ALICE: So today: from bets to an actual answer. How the model picks a word, and what "temperature" means. Why it writes one piece at a time. What a context window is, and why the model rereads your whole chat every time you send a message. Why that can make it stubborn. Whether any of this is "thinking". And, the big one: why it makes things up.

FRANK: That's a lot.

ALICE: It's a lot. Quick reminder for anyone jumping in: models don't read words, they read tokens, which are words or pieces of words. Roughly three quarters of a word each. And a language model is trained to do one thing: guess the next token. Frank, you're pressing Enter.

## One token at a time

FRANK: I am. So, you type a question into ChatGPT. Say: "What's the capital of Australia?" And you press Enter. Here's what happens. First, your message doesn't go in alone. The app takes the whole conversation so far, plus some hidden instructions, plus your new message, and stitches it all into one long piece of text.

ALICE: Hidden instructions?

FRANK: Things like "You are a helpful assistant", and today's date. We'll get into that next time, when we see how a chatbot is made. For now: it's all one big text. That text gets cut into tokens. And then the whole thing goes into the model, all at once, up through all the layers.

ALICE: Up the tower.

FRANK: Up the tower. And at the top, the output layer gives its spread of bets for the next token. Maybe "The" is the favorite. Then one token gets picked, we'll see how in a minute. Say it's "The". And now here's the key bit. That token gets added to the end of the text.

ALICE: Added to the text.

FRANK: And the whole thing goes back in. The conversation, plus "The". Up the tower again. New spread of bets. Maybe "capital" is the favorite now. Pick one, add it on. Back in again.

ALICE: Wait. So it goes all the way up the tower for every single token?

FRANK: For every single token. Ninety-six floors, in a model like GPT-3, for every piece of every word. In practice, it keeps notes from the earlier tokens, so it doesn't redo all the work from scratch. But each new token is one full trip up. "The capital of Australia is Canberra." That's maybe eight trips.

ALICE: Oh. So that's why the answer appears a few words at a time. It's not a special effect.

FRANK: It's not a special effect. You're watching it write, token by token. And this is worth sitting with for a second. The model never writes the whole answer and then shows it to you. At each step, it's only ever deciding one thing: what comes next. And then it reads its own answer so far, as part of the text, and decides the next thing.

ALICE: So its own words become part of what it reads.

FRANK: Exactly. Remember that, because it matters later. And how does it know when to stop?

ALICE: Good question. How does it?

FRANK: There's a special token that means "end of answer". And the model learned to bet on it when an answer is complete. When that one gets picked, the app stops and hands the floor back to you. So, Alice. We've got a spread of bets. How does one get picked?

## Picking a word

ALICE: So, the obvious idea: always pick the favorite. Whatever token has the highest probability, take it.

FRANK: That sounds sensible. The model's best guess, every time.

ALICE: It sounds sensible. And for short factual answers, it's fine. But for anything longer, it goes strangely wrong. The text gets dull. Generic. And often it gets stuck in a loop. "I don't know. I don't know. I don't know." Forever.

FRANK: Why would it loop?

ALICE: Because once it's said something twice, saying it a third time starts to look like the most likely next thing. A pattern is forming, and the safest bet is to continue the pattern. Researchers wrote a paper about this in 2019, with the great title "The Curious Case of Neural Text Degeneration". And they pointed out something interesting. When people write, we don't always pick the most likely next word. Real writing is full of mildly surprising choices.

FRANK: Otherwise everything would sound like a form letter.

ALICE: Exactly. So instead of always taking the favorite, you roll dice. Weighted dice. If "mat" has forty percent, it gets picked forty percent of the time. "Floor", twenty percent of the time. And so on. That's called sampling.

FRANK: So that's why, if I ask the same question twice, I get two different answers.

ALICE: That's exactly why. And why there's a "regenerate" button. Same bets, new roll of the dice. And now, temperature. Temperature is a dial that changes the bets before you roll.

FRANK: Changes them how?

ALICE: Turn the temperature down, and the favorites get even more favored. Forty percent becomes seventy, and the long shots shrink to almost nothing. The writing gets more predictable, more focused. Turn it all the way down to zero, and you're back to always picking the favorite.

FRANK: And turn it up?

ALICE: Turn it up, and the bets flatten out. The long shots get more of a chance. The writing gets more surprising, more creative. And if you turn it up too far, it gets weird. Then it falls apart into nonsense, because now truly unlikely tokens are getting picked all the time.

FRANK: Why is it called temperature?

ALICE: It's borrowed from physics. In a hot gas, particles bounce around wildly and end up in all sorts of unlikely states. Cool it down, and they settle into the most likely ones. Same idea. Hot: chaotic. Cold: settled.

FRANK: So which setting is right?

ALICE: Depends on the job. For code, or facts, or math, you want it low. You want the favorite. For brainstorming, or a poem, a bit higher. And there's usually one more trick on top. You only roll the dice among the reasonable candidates. Cut off the long tail of really unlikely tokens, so a one-in-a-million word never sneaks in. It's called top-p, or nucleus sampling, from that same 2019 paper.

FRANK: Okay. So when ChatGPT answers, it's not looking up an answer. It's rolling weighted dice, one token at a time.

ALICE: Rolling very well-weighted dice. The weights come from everything it learned. When it knows something well, the right answer has ninety-nine percent of the bet, and the dice almost always land there. When it doesn't, the bets are spread out, and the dice can land almost anywhere. Hold on to that. Frank, the context window.

## The model rereads everything

FRANK: Right. So, here's something that surprises a lot of people. Remember from early in the series, once a model is trained, its knobs are frozen?

ALICE: Your chats don't turn the knobs.

FRANK: Exactly. So, where does it keep the memory of your conversation? When you say, "Make it shorter", how does it know what "it" is?

ALICE: Huh. Because it's in the text.

FRANK: Because it's in the text. That's the only place. The model itself has no memory of you at all. Every time you send a message, the app sends the entire conversation again, from the very beginning. Your first message, its first answer, your second message, all of it. And the model reads the whole thing, from scratch, every single turn.

ALICE: Every turn? Even if we've been chatting for an hour?

FRANK: Every turn. Like a friend with no memory, who you hand the full transcript before every reply. And there's a limit to how much text the model can look at, at once. That's the context window. Counted in tokens.

ALICE: How big is it?

FRANK: It's grown enormously. GPT-1, in 2018, could look at five hundred and twelve tokens at a time. About a page. GPT-3, about two thousand. A few pages. Then in 2023 and 2024, it exploded. A hundred and twenty-eight thousand tokens, then a million, from Google, in early 2024. A million tokens is several long novels at once.

ALICE: Whole books at once.

FRANK: Whole books at once. Which, remember from the transformer episode, is hard. Every token looks at every other token, so double the text means four times the work. It took a lot of engineering to get there.

ALICE: And what happens when a chat gets longer than the window?

FRANK: Something has to give. The app might drop the oldest messages, or squash them into a summary. That's when you notice it's "forgotten" something you said at the start. It didn't forget. It just isn't being shown it anymore.

ALICE: And if it all fits, does it use all of it equally well?

FRANK: Not always. A 2023 study found that models were best at using information at the very start and the very end of a long text, and worse at things buried in the middle. They called it "lost in the middle". Models have improved since, but it's a good reason to put the important stuff up front, or at the end.

ALICE: Okay. So the model rereads the whole chat every time, including its own earlier answers. And Frank, I think that leads somewhere a bit uncomfortable.

FRANK: It does. That's yours.

## Why it gets stuck

ALICE: So, here's an experience I think most people have had. You ask a chatbot for help with something. Early on, it misunderstands a detail. Makes a wrong assumption. And you correct it. "No, I meant the other thing." And it says, "You're absolutely right!" And then gives you basically the same wrong answer again.

FRANK: Oh, I've had that. It drives me up the wall.

ALICE: Everyone has. And now we can see why. Remember: the model is a very good next-word predictor, and it rereads the whole chat every turn. Including its own earlier answers. And in most of the text it learned from, what comes later is consistent with what came earlier. A story stays on the same plot. An argument keeps its premise.

FRANK: So its earlier answers pull on the later ones.

ALICE: They pull hard. There's a long, confident wrong answer sitting right there in the text. And your correction is one short line. So the model tends to stay consistent with what's already been written, even when what's been written is wrong.

FRANK: Has anyone measured this?

ALICE: Yes. In 2025, researchers at Microsoft and Salesforce ran over two hundred thousand simulated conversations, with fifteen of the top models. They took tasks, like writing a piece of code, and either gave all the details in one message, or dripped them out over several messages, the way real people often do.

FRANK: And?

ALICE: Same task, same information. But spread across a conversation, performance dropped by thirty-nine percent on average. And the reason was what we just described. Models made assumptions early, jumped to a full answer too soon, and then leaned on it. The paper's title says it all: "LLMs Get Lost in Multi-Turn Conversation". And their summary was: when a model takes a wrong turn in a conversation, it gets lost and doesn't recover.

FRANK: Wow. And is there a name for this stubbornness?

ALICE: A 2026 paper called it "contextual inertia". Inertia, like in physics. Things keep going the way they're going. They found that even when users explicitly correct the model, or give it new information, it often sticks with its earlier reasoning. They're working on training methods to fix it. But for now, it's a real effect.

FRANK: So what should I actually do, when a chat goes wrong?

ALICE: Here's the practical tip, and it's one the researchers suggest too. Don't argue with it for ten more messages. Start a fresh chat. And this time, put everything in your first message. All the details, all the constraints, everything you learned from the failed attempt.

FRANK: Because the fresh chat doesn't have the wrong answer sitting in it.

ALICE: Exactly. A clean page. No wrong turn to cling to. It feels like starting over, but it's often the fastest way forward. Frank, here's the question I've been wanting to ask. If it's just rolling dice on the next token, is it thinking?

## Is it thinking?

FRANK: That's the big debate. And people get really heated about it. On one side, there's a famous 2021 paper that called language models "stochastic parrots". Stochastic means random. Parrots that repeat what they've heard. The argument is: a model learns which words tend to follow which, from a mountain of text. It stitches together plausible patterns. But there's no understanding of what any of it means.

ALICE: And that's not crazy. That's literally the training.

FRANK: That's literally the training. Predict the next token. And the lawyer's fake cases fit that story perfectly. Plausible-sounding legal text, with nothing behind it.

ALICE: And the other side?

FRANK: The other side says: to predict the next word really well, you have to build some kind of model of what the text is about. Remember the detective novel from the GPT-1 episode? To guess the murderer's name on the last page, you have to have followed the plot.

ALICE: Has anyone tested that?

FRANK: There's a lovely experiment from 2022. Researchers took the board game Othello. And they trained a small GPT on nothing but lists of moves. Just "this square, then this square, then this square". It never saw a board. Never saw the rules. Its only job was to predict the next legal move.

ALICE: Okay.

FRANK: And it got good at it. And then the researchers looked inside. And they found that the model had built its own picture of the board. Somewhere in its notepads, it was keeping track of which squares were black, which were white, which were empty. They could read the board state right out of it. And here's the best part. They could reach in and change that inner board. Flip a piece. And the model's predictions changed to match the new board.

ALICE: So it wasn't just memorizing move lists. It had built a little world inside.

FRANK: A little world, nobody asked for, because it helped predict the next move. And a 2025 study from Anthropic, looking inside one of their own models, found it planning ahead. When writing a rhyming poem, it picked the rhyme word for the end of the line before it started writing the line. Even though it only writes one token at a time.

ALICE: So "one token at a time" doesn't mean "no plan".

FRANK: That's the subtle point. The output comes out one token at a time. But what's going on inside, on the notepads, can look further ahead. So here's where I land. "It's just predicting the next word" is true, and also misleading. It's like saying a chess grandmaster is just moving pieces. The goal is simple. What gets learned to reach that goal can be surprisingly rich.

ALICE: But is it "understanding"?

FRANK: Honestly, that depends on what you mean by understanding, and people don't agree. What I'm confident about is this: these models build real internal structure, and they also produce fluent text with nothing behind it. Both. Sometimes in the same answer.

ALICE: Which brings us back to the lawyer.

FRANK: Which brings us back to the lawyer. That's yours.

## Making things up

ALICE: So, when a model states something false, fluently and confidently, people call it a hallucination. It's not a perfect word, it's not seeing things. But it's stuck. And now we have all the pieces to see why it happens.

FRANK: Go on.

ALICE: Piece one: the model always produces a spread of bets. There's no "nothing" option. It always picks something. Piece two: it was trained to produce text that looks like the text it learned from. Not text that's true. Most of the time those overlap, because most text it read was trying to be true. But there's nothing in "predict the next token" that checks the facts.

FRANK: So where does the made-up court case come from?

ALICE: Think about what a legal citation looks like. A name versus a name, a court, a year, a page number. The model has seen thousands. So the shape of a citation is something it knows extremely well. The bets for "this looks like a citation" are strong. But whether that specific case exists? That's a very specific fact, maybe one it barely saw, or never saw. The bets for the details are spread thin. And the dice land on something that fits the shape.

FRANK: The shape is strong, the details are weak.

ALICE: That's the pattern. And a paper from OpenAI, in September 2025, called "Why Language Models Hallucinate", has a great example. They asked a model for the birthday of one of the authors, Adam Kalai. And said: only answer if you know. Three tries, three different wrong dates.

FRANK: And it didn't say "I don't know".

ALICE: It didn't. And their explanation is my favorite part. They compare it to a multiple-choice exam. If a wrong answer and a blank both get zero points, what should you do when you're not sure?

FRANK: Guess. Always guess.

ALICE: Always guess. You might get lucky, and leaving it blank never scores. And the paper argues that the way models are trained and tested works the same way. The tests reward right answers, and treat "I don't know" as a miss. So models learn to bluff. And bluffs, they point out, tend to be confident and specific. "September thirtieth". Not "sometime in the autumn".

FRANK: So the system is rewarding confident guessing.

ALICE: In a lot of ways, yes. And their suggestion is to change how models are graded, so that admitting you don't know beats a wrong guess. Models have gotten better at this. But it's not solved.

FRANK: And the lawyer asking "is this case real?"

ALICE: That's the saddest part. He asked the same model. Which, at that point, has its own invented case sitting right there in the chat. Contextual inertia, plus the urge to give a confident answer. Of course it said yes. Checking a guess by asking the guesser.

FRANK: So, practically. What do I do?

ALICE: A few things. Be most careful with specific details: names, numbers, dates, quotes, references, links. That's where the bets are thinnest. If something matters, check it somewhere else, not by asking the same chat. And when you can, give the model the source. Paste in the document, and ask it to answer from that. A lot of today's tools look things up for the model before it answers, which helps a lot. That's a topic for another season.

FRANK: And remember that sounding sure isn't the same as being right.

ALICE: That's the big one. The model's confidence is in the shape of its sentences, not in the facts. A fluent sentence is just a fluent sentence.

## Recap

FRANK: Okay, let's wrap up. Alice, you start.

ALICE: Sure. One: when you press Enter, the app stitches the whole conversation into one text, the model runs it up the tower, and picks one token from the spread of bets. That token gets added on, and the whole thing goes in again. One token at a time, until it picks the "end" token. That's why answers appear piece by piece.

FRANK: Two: picking a token means rolling weighted dice. Always taking the favorite makes text dull and loopy. Temperature is a dial: low makes the favorites stronger, for focused answers; high flattens the bets, for creative ones, and eventually nonsense.

ALICE: Three: the model has no memory of you. The app sends the whole chat every turn, and the model rereads all of it. The context window is how much it can take in at once: a page for GPT-1, now up to whole books.

FRANK: Four: because it rereads its own earlier answers, they pull on the next ones. A wrong turn early on can stick, even after you correct it. Researchers call it contextual inertia. When a chat goes wrong, start fresh, with everything in the first message.

ALICE: And five: "just predicting the next word" is true but misleading. Models can build real inner pictures, like the Othello board. But they're trained to sound right, not to be right, and tests reward guessing. So they make things up, confidently, especially in specific details. Check what matters.

FRANK: Which leaves a question we've been building toward all season. All of this works better, more knowledge, fewer silly mistakes, when the model is bigger. So what happens when you just keep making it bigger?

ALICE: That's next time. Scale changes everything. GPT-2, GPT-3, and the chart that set off the race.

FRANK: See you then.
