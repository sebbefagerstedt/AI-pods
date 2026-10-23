# Episode 12: Scale changes everything

## Cold open

FRANK: Okay, picture this. It's February 2019. OpenAI has a new model, and they give it the start of a news story. Two sentences, written by a person. Here they are: "In a shocking finding, scientists discovered a herd of unicorns living in a remote, previously unexplored valley, in the Andes Mountains. Even more surprising to the researchers was the fact that the unicorns spoke perfect English."

ALICE: Okay. Strong start.

FRANK: And then the model takes over. It writes that the scientist named the population after their distinctive horn, Ovid's Unicorn. That these four-horned, silver-white unicorns were previously unknown to science. It invents a professor from a university in Bolivia, it has him wander through the valley with his team, it quotes him. It goes on for paragraphs, and it reads like a real article.

ALICE: A four-horned unicorn. Named after its distinctive horn.

FRANK: Right, it's not perfect. And to be fair, it took them ten tries to get that one. But nobody had seen a machine keep a story together like that. And here's the part that made the news. OpenAI said they would not release the full model. They were worried people would use it to churn out fake news and spam.

ALICE: Wait, so the headline was basically "AI lab builds a model too dangerous to share"?

FRANK: Pretty much. The model was called GPT-2. And the thing is, it wasn't a new invention. It was GPT-1, the model we've already met, made bigger. And then fed a lot more text.

ALICE: Just bigger.

FRANK: Just bigger. And that's today's episode. What happens when you just keep making it bigger.

## Welcome

ALICE: Welcome to From Zero to ChatGPT. I'm Alice.

FRANK: And I'm Frank.

ALICE: And I'll admit, this is the one I've been waiting for. Because if you follow AI news at all, you keep hearing about bigger models, bigger data centers, billions of dollars. And today we find out where all of that started. Two models, GPT-2 and GPT-3. One chart that changed how the whole field thinks. And then the race that chart set off.

FRANK: And if someone's jumping in here?

ALICE: Then three quick reminders. One, from early in the series. A model is a machine with millions of adjustable knobs. Training means turning the knobs, a tiny bit at a time, until the answers are less wrong. And "how wrong" has a name: the loss.

FRANK: Knobs and loss.

ALICE: Two, from the GPT-1 episode. A language model learns by guessing the next word. You show it a stretch of text, it bets on what comes next, and the real next word is the answer key. No labels needed. That stage is called pre-training. And GPT-1, back in 2018, did it on about seven thousand books, with about a hundred million knobs.

FRANK: And then fine-tuning.

ALICE: Right. Then you'd train it a little more on examples of the one job you wanted, like sorting reviews into positive and negative. Pre-train, then fine-tune. And three: the words aren't quite words. The model reads tokens, words and pieces of words. So when we say a model read so many tokens, just think "words", roughly.

FRANK: Got it.

ALICE: Good. Frank, you started with the unicorns, so you take us through GPT-2.

## Ten times bigger

FRANK: Happy to. So, GPT-1 came out in June 2018. And the people at OpenAI had seen something in it that stuck with them. Remember the zero-shot experiments, from the end of the GPT-1 episode?

ALICE: Where they tested it on tasks without any fine-tuning. Like adding "very" after a movie review, and seeing if it guessed "positive" or "negative".

FRANK: That's the one. And the scores kept going up the longer it trained. So the obvious next question was: what if we give it a lot more to read, and a lot more knobs?

ALICE: Okay, more to read. Like what? More books?

FRANK: The web. But not the whole web, because most of the web is junk. So they did something clever. They went to Reddit, the big discussion site, and collected every link that people had shared there and that had gotten at least three upvotes.

ALICE: Huh. So Reddit users were the filter.

FRANK: Exactly. If at least a few people found a page worth upvoting, it's probably real writing, not spam. That gave them about eight million web pages. Forty gigabytes of text. They called it WebText.

ALICE: And how does that compare to GPT-1's books?

FRANK: About eight times as much text. And the model, GPT-2, had one and a half billion knobs, more than ten times as many as GPT-1. Same basic design. The writing half of the transformer, same next-word game. Just wider, deeper, and reading more.

ALICE: Okay. So they made it bigger and it wrote nicer unicorn stories. Is that it?

FRANK: No, and this is the real point of the paper. Look at its title: "Language Models are Unsupervised Multitask Learners".

ALICE: That's a mouthful. What does it mean in plain words?

FRANK: It means: we didn't fine-tune it on anything, and it can still do a bunch of different tasks. They tested GPT-2 the zero-shot way, on all sorts of things. Answering questions about a passage. Translating. Summarizing.

ALICE: Wait, how do you ask a next-word guesser to summarize?

FRANK: You have to be sneaky again. On the web, people often end a long post with "TL DR". It means "too long, didn't read", and what follows is a one-line summary. So they gave GPT-2 a news article, stuck "TL DR" on the end, and let it keep writing.

ALICE: Oh, that's good. It just does what the internet does next.

FRANK: Exactly. And for translation, they started the text with a few pairs, like "English sentence equals French sentence", and then gave it a new English sentence and an equals sign.

ALICE: And it filled in the French.

FRANK: Badly. Let's be honest, most of these scores were weak. The summaries were barely better than picking three random sentences from the article. The translation was poor. But here's what the researchers kept pointing at. On every task, the bigger the model, the better the score. They'd trained four sizes, from small to the full one and a half billion. And the lines just went up, with no sign of stopping.

ALICE: So the summaries are bad, but less bad every time you make it bigger.

FRANK: That's it. And on the thing it was actually trained for, guessing the next word, it set records on seven out of eight test collections. Without ever training on any of them.

ALICE: Okay, and the "too dangerous" thing. Did that hold up?

FRANK: Not really. They released it in steps through 2019, a small version first, then bigger ones, watching how people used them. And in November they put out the full model. They said they'd seen no strong evidence of misuse so far. A lot of researchers thought the whole thing was overhyped. But it was one of the first times an AI lab held a model back like that, and that debate about what to release is still going on today.

ALICE: Okay. So GPT-2 shows that bigger is better. But that's kind of a vague lesson, right? How much bigger? Bigger in what way? Bigger than what you can afford?

FRANK: Those are exactly the right questions. And a group at OpenAI went and measured the answers. Alice, this one's yours.

## Three dials

ALICE: It is. And this is the chart. January 2020. A paper called "Scaling Laws for Neural Language Models". The first author is a physicist named Jared Kaplan.

FRANK: A physicist?

ALICE: Which kind of explains the approach. Physicists love finding one simple rule hiding under a lot of messy data. So instead of training one big model and hoping, they trained lots of language models. Tiny ones, up to big ones with over a billion knobs. On different amounts of text. For different lengths of time. And for every single one, they measured the loss, how wrong it was at guessing the next word, on text it had never seen.

FRANK: And then plotted it all.

ALICE: And the very first figure in the paper is the one to know. It has three panels, side by side. Each one is a thing you can make bigger. The first one is compute, meaning how much computing power you spend on training. The second is data, how much text the model reads. And the third is the model's size, the number of knobs.

FRANK: Okay, and I have to say, I always kind of assumed it was really about the first one. Computing power. More chips, better model.

ALICE: So did I, honestly. And that's what this chart fixed for me. Because all three panels look the same. In each one, the loss goes down along a straight line. Compute, data, size. Three dials, and turning up any of them makes the model less wrong.

FRANK: Wait, a straight line? That's weird. Usually things level off. The first hour of practice helps a lot, the hundredth hour, not so much.

ALICE: That's the trick in how it's drawn. Each step along the bottom isn't one more. It's ten times more. Ten times the compute, then ten times that, and so on. So what the straight line says is: every time you make one of these ten times bigger, the loss drops by about the same share.

FRANK: So it does slow down. Each step costs ten times as much as the last.

ALICE: Exactly. It's not free. But it's reliable. And to give you a feel for it, ten times the knobs made the model about a sixth less wrong. Ten times the text, about a fifth. And over the whole range they tested, the line never bent. They didn't see it leveling off.

FRANK: Huh. How big a range are we talking?

ALICE: Some of the lines run across more than ten million times, from the smallest to the biggest.

FRANK: Ten million times. And still a straight line.

ALICE: Still a straight line. That's why it's called a law. It's not a law of nature, it's a pattern they measured. But it held up so well that people started treating it like one.

FRANK: Okay. But there must be a catch.

ALICE: There is, and you can see it in the chart too. Each dial only works if the other two aren't holding it back. Look closely at the compute panel. Behind the straight line there are lots of faint curves, one for each model they trained. And each one drops fast at first, then bends, and flattens out as it reaches the line.

FRANK: Why does it flatten?

ALICE: Because each faint curve is one model, of one fixed size, being trained longer and longer. Early on, every bit of extra training helps a lot. But then that model runs out of room. It's too small to soak up any more. You can keep training it, and spending compute on it, and it barely improves.

FRANK: So the straight line is...

ALICE: The straight line is what you get if, for each amount of compute, you pick the right size of model. Small budget, small model. Big budget, bigger model. And the same goes for data. A giant model that reads too little text stops improving too. So to keep going down the line, you have to turn up all three dials together.

FRANK: Okay. So why did one chart matter so much? It's a nice chart. But lots of papers have nice charts.

ALICE: Because it turned a hunch into a forecast. Before this, making a model ten times bigger was a gamble. Maybe it gets better, maybe it doesn't, and you've spent a fortune finding out. After this, you could train a bunch of small, cheap models, draw the line through them, and then read off how good a much bigger model would be. Before you spend the money.

FRANK: So you can see the payoff in advance.

ALICE: Roughly, yes. And when the line says you'll get a better model for your money, it's a lot easier to raise the money. And the paper had one more piece of advice, which turned out to matter a lot. It said that if you get more compute, most of it should go into a bigger model. Bigger models learn more from each word they read. So: make the model a lot bigger, and give it only somewhat more text.

FRANK: And did anyone take that advice?

ALICE: The people sitting in the next room. Several of the paper's authors were also working on the next GPT. Frank, this one's yours.

## Learning from the prompt

FRANK: It is. So, four months later, May 2020, OpenAI publishes GPT-3. And they went big. A hundred and seventy-five billion knobs.

ALICE: Hang on. GPT-2 was one and a half billion.

FRANK: So more than a hundred times bigger. In about fifteen months.

ALICE: Wow. And reading what? Reddit links again?

FRANK: Much more. A big filtered copy of the web, plus their Reddit collection, two collections of books, and all of English Wikipedia. During training it read about three hundred billion tokens.

ALICE: Help me picture three hundred billion.

FRANK: Okay. Three hundred billion tokens is a bit over two hundred billion words. Say a long novel is a hundred thousand words. That's about two million long novels. A person reading one novel a week would need over forty thousand years.

ALICE: Okay, that's a lot of reading. And what did it cost?

FRANK: OpenAI didn't say. Outside estimates put a single training run at several million dollars. It was trained on computers that Microsoft provided. And that same month, Microsoft announced a supercomputer it had built for OpenAI, with ten thousand graphics cards. They said it would rank among the five most powerful supercomputers in the world.

ALICE: Okay. So it's huge. But the GPT-2 lesson was already "bigger is better". What was new?

FRANK: The title tells you. The GPT-3 paper is called "Language Models are Few-Shot Learners".

ALICE: Few-shot. We had zero-shot. So few-shot is...

FRANK: A few examples. And here's where it gets interesting. Remember fine-tuning? You take the pre-trained model, and you train it a bit more on thousands of examples of your task. Which means turning the knobs again. A separate copy of the model for every job.

ALICE: Right.

FRANK: With GPT-3, they skipped all of that. No fine-tuning. No knob turning at all. They just wrote a few examples into the text they gave it. For example: "Translate English to French. Sea otter: loutre de mer." Then a couple more pairs like that. And then, at the end: "Cheese:"

ALICE: And it says "fromage".

FRANK: It says "fromage". From a few examples, sitting right there in the text. The text you give a model is called the prompt. So it was learning the task from the prompt. This is called in-context learning.

ALICE: Wait, but is it actually learning? You said the knobs don't move.

FRANK: That's the right question, and honestly, people still argue about it. The knobs don't move. Nothing about the model changes. Close the conversation and it's forgotten everything. But while it's reading your examples, it picks up the pattern and follows it. One way to think about it: in pre-training, it saw countless lists, and tables, and question-and-answer pages. So "spot the pattern and continue it" is one of the things it learned to do.

ALICE: Huh. So it's not learning a new skill, more like recognizing which of its skills you're asking for.

FRANK: That's a good way to put it. And here's the part that connects to our chart. Small models were bad at this. Give a small model three examples and it barely does better than with none. But the bigger the model, the more it got out of the examples. In-context learning got better with scale.

ALICE: So it's another thing that just shows up when you turn the dials.

FRANK: Yes. And they tested a lot. Translation, trivia questions, unscrambling words, two-digit arithmetic, which it got almost always right. And one test that got a lot of attention. They had GPT-3 write short news articles, mixed them with real ones, and asked people to pick out the fakes.

ALICE: And?

FRANK: For the biggest model, people were right only about half the time. Basically a coin flip.

ALICE: Oof. That's the GPT-2 worry, come true.

FRANK: Pretty much. And the paper says so. It has a whole section on misuse, and on the biases the model picked up from the web.

ALICE: Okay, so what happened next? Did everybody get to use it?

FRANK: Sort of. This time OpenAI didn't release the model at all. Instead, they opened an online service in June 2020, where developers could send it text and get text back. And people started building with it, and sharing what they found. Very quickly, a whole craft grew up around writing the right prompt. Which examples to use, how to word the instructions. People started calling it prompt engineering.

ALICE: And that sounds a lot like ChatGPT. Was GPT-3 basically ChatGPT?

FRANK: Not yet. And this matters. GPT-3 was still a pure next-word guesser. Ask it a question, and it might answer. Or it might write five more questions, because on the web, questions often come in lists. It didn't know it was supposed to be helpful. Turning it into an assistant is next time.

ALICE: Got it. So, we've got the chart, and we've got GPT-3 proving the chart right. Where does the story go from here?

FRANK: Into a correction, and then into a race. Alice?

## The race

ALICE: Yes. So, the correction first. It came from DeepMind, Google's AI lab, in March 2022. They redid the scaling experiments, more carefully. Over four hundred models this time, and bigger ones. And they found that the advice from the first paper was off.

FRANK: The advice to spend most of your compute on a bigger model?

ALICE: That one. They found that model size and data should grow together, equally. Double the knobs, double the text. And by their numbers, the big models of the day, GPT-3 included, were far too big for how little they'd read.

FRANK: Huh. Undertrained, basically. A huge brain that didn't read enough.

ALICE: Exactly. And to prove it, they trained a model called Chinchilla. Seventy billion knobs, so a lot smaller than GPT-3. But it read about one and a half trillion tokens, around five times as much. They gave it the same compute budget as their own big model, Gopher, which had two hundred and eighty billion knobs.

FRANK: So: four times smaller, but almost five times more reading, same cost.

ALICE: Same cost. And Chinchilla beat Gopher on almost everything. The rule of thumb people took away: about twenty tokens of text for every knob.

FRANK: Wait, so was the first chart wrong?

ALICE: Not the chart. The three straight lines still hold. What changed was the recipe, how to split your money between size and reading. The first paper had a quirk in how it trained its runs, which made smaller amounts of data look worse than they really were.

FRANK: Okay, and today? Is everyone doing twenty tokens per knob?

ALICE: Funny enough, no. Many go way past it. Meta's Llama 3, from 2024: its smallest version had eight billion knobs and read about fifteen trillion tokens. That's nearly two thousand tokens per knob.

FRANK: Why would you do that, if it's not the efficient recipe?

ALICE: Because Chinchilla's twenty tokens is the cheapest way to train a model of a given quality. But training is something you pay for once. Running the model, answering millions of people's questions every day, you pay for forever. And a smaller model is cheaper to run. So it's often worth overpaying for training, to get a small model that's as good as a bigger one.

FRANK: Okay, that makes sense. So that's the correction. What about the race?

ALICE: The race comes from the forecast. Remember, the chart lets you predict a big model's loss from small ones. When OpenAI made GPT-4, in 2023, they said they'd done exactly that. They predicted its final loss from small runs using thousands of times less compute, and it landed right on the line.

FRANK: So now you can walk into a meeting and say: give me this many billions, and here's roughly how good the model will be.

ALICE: And people did. Microsoft had already invested in OpenAI. Google, Meta, Amazon, and a lot of new companies all started spending on the same thing. Chips, mostly Nvidia's, and data centers to put them in. In January 2025, OpenAI and partners announced a project called Stargate. Up to five hundred billion dollars, over four years, for data centers in the United States.

FRANK: Five hundred billion. For computers.

ALICE: For computers, and the buildings, the cooling, and the electricity. Some of these sites need as much power as a city. Which is why you now see AI companies signing deals with power plants.

FRANK: Okay, wait. If the line just keeps going, does that mean we just keep building forever?

ALICE: That's the big question. And there are a couple of catches. Remember, it's three dials, and all three have to go up together. Compute, you can buy. Model size, you can choose. But data?

FRANK: Data, there's only so much of.

ALICE: Exactly. Ilya Sutskever, who was on the GPT-1 paper and helped lead OpenAI's research for years, gave a talk in late 2024 where he put it like this. Compute keeps growing, but data doesn't, because we have only one internet. He called data the fossil fuel of AI.

FRANK: Huh. So the dial that's hardest to turn is the reading.

ALICE: And the other catch is that the line measures loss, how good the model is at guessing the next word. That's not quite the same as how useful it is. Turning a good guesser into something helpful takes more work, which is next time. And the newest trick, letting a model think for longer before it answers, is another dial entirely. That's for another season.

FRANK: So, is it fair to say scale was the whole story?

ALICE: It's fair to say it was the surprise of the story. There's a famous short essay from 2019, by Rich Sutton, one of the pioneers of AI, called "The Bitter Lesson". His point: over seventy years of AI, the methods that won in the end were the simple ones that could use more and more computing power. Not the clever, hand-built ones.

FRANK: That sounds a lot like where this series started. Learning from data beating hand-written rules.

ALICE: It's the same lesson, a few decades on. And it's bitter because researchers keep putting their cleverness into the system, and then watch a simpler method, made bigger, beat them.

## Recap

FRANK: Okay, let's wrap up. Alice, you start.

ALICE: Sure. One: GPT-2, February 2019. GPT-1's recipe, ten times bigger, reading eight million web pages picked by Reddit upvotes. It could do tasks it was never trained for, badly, but better with every size. And OpenAI first held it back as too risky to release.

FRANK: Two: the scaling laws paper, January 2020. Its first chart has three panels: compute, data, and model size. Turn up any of them, and the loss falls along a straight line, where each step means ten times more. But only while the other two keep up, so all three dials have to go up together. And that turned building bigger models from a gamble into a forecast.

ALICE: Three: GPT-3, May 2020. A hundred and seventy-five billion knobs. And in-context learning: give it a few examples in the prompt, and it picks up the task. No fine-tuning, no knobs turned. And that ability got better with size.

FRANK: Four: the correction. DeepMind's Chinchilla showed size and data should grow together, about twenty tokens per knob. Today's labs often go well past that, to get smaller models that are cheaper to run.

ALICE: And five: the race. Because the line made the payoff predictable, companies started pouring billions into chips, data centers and power. The dial that's hardest to turn now is data.

FRANK: Which leaves one question. GPT-3 was a brilliant guesser of the next word. Ask it a question, and it might just write more questions. So how do you get from that to ChatGPT, something that actually tries to help you?

ALICE: That's next time. Base models, chat models, and how people taught a model to be an assistant.

FRANK: See you then.
