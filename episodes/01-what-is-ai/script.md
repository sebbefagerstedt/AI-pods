# Episode 1: What is AI, actually?

## Cold open

FRANK: Okay, picture this. It's the mid-sixties, at MIT. A secretary is sitting at a computer terminal, typing back and forth with a program. And after a few exchanges, she turns to her boss, the man who wrote the program, and asks him to leave the room.

ALICE: Wait, why?

FRANK: Because she wanted some privacy. She was telling it personal things.

ALICE: Oh no. So this was a chatbot? In the sixties?

FRANK: In the sixties. It was called Eliza, and it was written by a computer scientist named Joseph Weizenbaum. Eliza played a therapist. And here's the thing: it didn't understand a single word. It looked for keywords and turned your sentences back into questions. You'd type, "I'm worried about my mother," and it would answer, "Tell me more about your family."

ALICE: That's, honestly, a pretty good trick.

FRANK: It's a great trick. And Weizenbaum was kind of horrified by how quickly people decided there was someone in there.

ALICE: Which sounds a lot like the conversations people are having about chatbots right now.

FRANK: Right? Almost sixty years apart. And that's our question for today. When people say "AI", what do they actually mean? And how did we get from Eliza to ChatGPT?

## Welcome

ALICE: So, welcome to From Zero to ChatGPT. This is episode one. I'm Alice.

FRANK: And I'm Frank. The idea of this series is pretty simple. AI is in the news every single day, but a lot of us skipped the foundations. So over twelve episodes, we're going to build them up, one piece at a time, from the very first ideas all the way to how ChatGPT actually works.

ALICE: And no equations. I was promised no equations.

FRANK: No equations. Ideas, a bit of history, and a lot of analogies. Also, we're going to take turns. Sometimes I'll explain and you'll grill me, and sometimes it's the other way around.

ALICE: I like that. Okay, so let's start with the obvious one. What is AI, actually?

FRANK: The honest answer is that it's a moving target. There's a line usually credited to the computer scientist Larry Tesler: "AI is whatever hasn't been done yet."

ALICE: Okay, what does that mean?

FRANK: It means that as soon as a computer can do something, we stop calling it intelligent. Beating a world champion at chess was a dream of AI for decades. Then a computer did it in 1997, and people said, well, that's just a lot of calculating. Same with the route planning in your maps app, or the spam filter in your email. All of that used to be AI research.

ALICE: And now it's just, you know, software.

FRANK: Exactly. So a decent working definition is: AI is getting machines to do things we'd call intelligent if a person did them. And the big story of this episode is that there have been two very different ideas about how to do that.

ALICE: Two ideas.

FRANK: Idea one: you figure out the rules of intelligence, and you write them down for the computer. Idea two: you let the computer figure out the rules itself, by learning from examples. And spoiler, idea two is the one that won. But it took about sixty years.

ALICE: Okay, I want to know why it took so long.

FRANK: We'll get there. But it starts with the person who saw this whole debate coming. Alice, you've been reading up on Turing.

## Turing

ALICE: I have. And honestly, Alan Turing is kind of the patron saint of this whole field. You might know him from breaking German codes in World War Two. But in 1950 he published a paper called "Computing Machinery and Intelligence", and the very first line is: "I propose to consider the question, 'Can machines think?'"

FRANK: Big question.

ALICE: Huge question. And Turing's clever move was to say: that question is too vague. What does "think" even mean? So let's swap it for something we can actually test. He called it the imitation game.

FRANK: Which is what we now call the Turing test.

ALICE: Right. Picture a judge typing messages to two hidden players. One is a person and one is a machine, and both try to convince the judge that they're the human. If the judge can't reliably tell them apart, then Turing's point was, let's stop arguing about definitions and admit the machine is doing something pretty remarkable.

FRANK: Did he make a prediction?

ALICE: He did. He said that in about fifty years, so around the year 2000, computers would play the game so well that after five minutes of questioning, an average judge would pick the right one no more than seventy percent of the time.

FRANK: And did that happen?

ALICE: Not by 2000. But in 2025, researchers at UC San Diego ran exactly that kind of test. Five-minute chats, with each judge talking to a real person and a machine at the same time. And GPT-4.5, when it was told to act like a person, was picked as the human seventy-three percent of the time.

FRANK: Wait. More often than the actual humans?

ALICE: More often than the actual humans.

FRANK: Huh. So the Turing test has been passed.

ALICE: In that form, yes. Though most researchers would say it shows the test measures something narrower than thinking. It measures whether you can pass for a person in a short chat. And here's a fun detail. They also tested Eliza, the program from the sixties.

FRANK: No way. How did it do?

ALICE: People picked it as the human twenty-three percent of the time.

FRANK: Okay, that's impressive and a little bit depressing.

ALICE: A little. But the part of Turing's paper I find most interesting isn't the test at all. It's near the end. He asks: how would you actually build a thinking machine? And his answer is, instead of trying to program an adult mind, why not build something more like a child's mind, and then educate it?

FRANK: So, learning.

ALICE: Learning. In 1950. He's basically saying, don't hand-write the rules, let the machine learn them.

FRANK: So that's idea two, sixty years early.

ALICE: Sixty years early. But the field went with idea one first. And that story is yours.

## Dartmouth

FRANK: It is. So, the summer of 1956. Dartmouth College, in New Hampshire. A young mathematician named John McCarthy, together with Marvin Minsky, Claude Shannon and Nathaniel Rochester, gets seventy-five hundred dollars from the Rockefeller Foundation to run a summer workshop. And in the funding proposal, McCarthy coins a brand-new term: artificial intelligence.

ALICE: So that's where the name comes from.

FRANK: That's where the name comes from. And the proposal is wonderfully bold. It says the whole study rests on the idea that "every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it." And they figured a carefully chosen group of about ten scientists could make a significant advance... in one summer.

ALICE: One summer?

FRANK: One summer.

ALICE: How did that go?

FRANK: Well, they didn't solve intelligence by September. But the workshop brought together the people who'd lead the field for decades. And the early results were genuinely exciting. Two of the attendees, Allen Newell and Herbert Simon, had a program called the Logic Theorist that proved theorems from a famous book on the foundations of mathematics. And for one theorem, it found a neater proof than the book's authors had.

ALICE: Okay, that's impressive for the fifties.

FRANK: Very. And it made everyone wildly optimistic. In 1958, Simon and Newell predicted that within ten years, a computer would be the world chess champion.

ALICE: And that happened when?

FRANK: 1997. Thirty-nine years later.

ALICE: So, slightly off.

FRANK: Slightly off. But notice the approach they all took. Intelligence, they thought, is basically logic. Symbols and rules. If you can write down the right rules, the computer just follows them. It's like teaching someone to cook by writing a giant recipe book that covers every possible situation in a kitchen.

ALICE: And Eliza was that too, right? A bunch of rules.

FRANK: Exactly. Eliza was a rulebook for faking a conversation. This whole approach has a name: symbolic AI. Or, a bit affectionately, good old-fashioned AI.

ALICE: So what went wrong with it?

FRANK: That's where you come in.

## The first AI winter

ALICE: So, by the early seventies, the big promises weren't arriving. And there were a few reasons. The first one has a dramatic name: the combinatorial explosion.

FRANK: That does sound dramatic.

ALICE: It's actually pretty simple. Say you're planning a road trip. With three cities, there are only six orders you could visit them in. With ten cities, there are over three million. And with thirty cities, even a computer checking a billion routes a second would need far longer than the age of the universe.

FRANK: Wow. Okay.

ALICE: And a lot of intelligence looks like that. Planning, chess, understanding a sentence: the possibilities multiply out of control. So those early programs looked brilliant in tiny, tidy worlds, like stacking blocks or proving one theorem. But the real world isn't tiny or tidy.

FRANK: What was the second reason?

ALICE: Common sense. A rulebook doesn't know that water is wet, or that if you put your keys in a bag and carry the bag, the keys come with you. People know millions of little facts like that without ever thinking about them.

FRANK: And someone would have to write all of them down.

ALICE: All of them. And the third reason is that computers back then were incredibly weak. The phone in your pocket is millions of times more powerful than the machines they had.

FRANK: So what happened?

ALICE: The money dried up. In Britain, in 1973, a mathematician named James Lighthill was asked to review the field. His report said, more or less, that AI had failed to deliver on its grand promises, and funding was cut. In the US, the military research agency DARPA, which had been the field's biggest funder, pulled back too.

FRANK: And that's the first AI winter.

ALICE: The first AI winter, roughly the mid-seventies. And here's a detail I love. The term "AI winter" wasn't coined until 1984, at a big AI conference, by researchers who were warning that another one was on its way. They were comparing it to a nuclear winter.

FRANK: And were they right?

ALICE: They were completely right. But first, the field had a comeback, and you're telling that one.

## Expert systems

FRANK: I am. The comeback was the expert system. And the idea was actually clever. Forget general intelligence. Forget common sense. Pick one narrow job that a human expert does, and capture what that expert knows as rules.

ALICE: Like what?

FRANK: The famous example is a program called Mycin, from Stanford in the seventies. It helped doctors figure out which bacteria were causing a serious blood infection, and which antibiotic to give. The researchers sat down with infection specialists and turned their knowledge into about six hundred rules. Things like: if the infection started in a certain place, and the bacteria look a certain way under the microscope, then it's probably this organism.

ALICE: So, basically a giant if-then flowchart.

FRANK: A giant if-then flowchart. And in tests, it held up about as well as Stanford's own specialists. Sometimes better.

ALICE: Wait, really? Then why weren't we all being diagnosed by Mycin?

FRANK: It was never used on actual patients. Partly legal worries, like who's responsible when it's wrong, and partly practical: a doctor had to sit at a terminal and type answers to a long list of questions.

ALICE: Okay. But businesses must have loved this stuff.

FRANK: They did. In the eighties, a computer company called Digital Equipment used an expert system to check customer orders: which cables, which cabinets, which parts actually fit together. It handled tens of thousands of orders and was reckoned to save the company around twenty-five million dollars a year.

ALICE: That's real money.

FRANK: Real money. By the mid-eighties, AI was a billion-dollar industry. Companies were even building special computers just to run AI programs.

ALICE: I sense a "but" coming.

FRANK: There's a "but". Three of them, actually. First, getting the knowledge out of the experts' heads was slow and painful. Experts often can't explain how they know what they know. They just know.

ALICE: Like asking a chef exactly how much salt is "a pinch".

FRANK: Exactly like that. Second, the systems were brittle. Inside their little world, great. But one step outside it, and they didn't say "I don't know". They just gave you a confident, wrong answer.

ALICE: That sounds familiar too.

FRANK: It does, though for very different reasons. We'll get to chatbots making things up in episode ten. And third, the rulebooks became impossible to maintain. The ordering system grew to thousands of rules, and every new product meant writing new ones and checking they didn't break the old ones.

ALICE: So, a giant pile of rules that nobody fully understands anymore.

FRANK: Pretty much. And then in 1987, the market for those special AI computers collapsed, because ordinary desktop computers had caught up. The money dried up again. And that's the second AI winter, from the late eighties into the nineties.

ALICE: So two winters, and both times, the rulebook hit a wall.

FRANK: Both times. Which brings us to the big question of the episode: why did learning from examples win? And Alice, I believe that one's yours.

## Why learning won

ALICE: It is. Let me start with a little test. Frank, how do you recognize your mother's face?

FRANK: I just, I look at her? I don't know. I just know it's her.

ALICE: Right. Now try to write down the rules. Precisely enough that a computer could follow them.

FRANK: Her eyes are about this far apart, and... no. I have no idea.

ALICE: And that's the whole problem, right there. In 1966, the philosopher Michael Polanyi put it like this: "We can know more than we can tell." And he used faces as his example. We can pick out a face we know among thousands, but we usually can't say how we do it.

FRANK: So the knowledge is in there, it just won't come out as rules.

ALICE: Exactly. And there's a related idea called Moravec's paradox. The things that are hard for us, like chess or calculus, turned out to be fairly easy for computers. And the things that are easy for us, like seeing, walking, or understanding a sentence, turned out to be incredibly hard. We do them without thinking, so we have no idea how we do them.

FRANK: So the rulebook fails exactly on the stuff we find easy.

ALICE: Yes. So, idea two. Instead of writing the rules, you show the computer examples, and let it find the rules itself. And that idea was around from the start. In the fifties, an IBM engineer named Arthur Samuel wrote a checkers program that got better by playing thousands of games against itself. In 1959 he gave this a name: machine learning. And in 1962, his program beat a self-described checkers master.

FRANK: Then why didn't everyone switch right away?

ALICE: Because learning needs two things, and back then there wasn't much of either. Lots of examples, and lots of computing power. Think about your email spam filter. The early ones were rulebooks. If an email says "free money", it's spam. So the spammers just wrote "free" with a three instead of an E.

FRANK: Of course they did.

ALICE: The filters that actually worked, from the early two-thousands, learned from examples. You click "this is spam" on enough emails, and the filter works out for itself which patterns give spam away, including ones nobody would ever think to write down.

FRANK: So every time I click that button, I'm teaching it.

ALICE: You're teaching it. And researchers saw the same thing everywhere. In the eighties, at IBM, the speech recognition pioneer Fred Jelinek is famously quoted as saying: "Every time I fire a linguist, the performance of the speech recognizer goes up."

FRANK: Ouch. Sorry, linguists.

ALICE: It's a bit harsh. But the point was that statistics learned from lots of recorded speech beat carefully written rules about language. And in 2019, the AI researcher Rich Sutton wrote a short essay called "The Bitter Lesson". He looked back at seventy years of AI research and concluded that "general methods that leverage computation are ultimately the most effective, and by a large margin."

FRANK: Why bitter?

ALICE: Because researchers kept building their own knowledge into their systems, and it kept losing to methods that simply learned from more data, with more computing power. It's humbling.

FRANK: So that's really the jump from Eliza to ChatGPT. Eliza was a rulebook. ChatGPT learned from an enormous amount of text.

ALICE: Exactly. Nobody wrote ChatGPT's rules. It learned them. And once the data and the computers finally got big enough, in the early twenty-tens, things took off. That's episode five.

## Recap

FRANK: Okay, let's wrap up. Alice, do you want to start the recap?

ALICE: Sure. One: "AI" is a moving target. Once something works, we tend to stop calling it AI.

FRANK: Two: in 1950, Alan Turing asked whether machines can think, proposed the imitation game, and even suggested building a machine that learns, like a child.

ALICE: Three: the field got its name at Dartmouth in 1956, and for decades, most researchers tried to build intelligence by writing rules.

FRANK: Four: rules worked in tiny worlds and in narrow expert systems. But they were brittle and hard to write and keep up to date, and the disappointment led to two AI winters.

ALICE: And five: learning from examples won, because so much of what we know, like recognizing a face, can't be written down as rules. It just needed enough data and enough computing power.

FRANK: Which leaves a big question for next time. What does it actually mean for a machine to learn?

ALICE: That's episode two: machine learning. What a model actually is, how training works, and why memorizing isn't the same as understanding.

FRANK: See you then.
