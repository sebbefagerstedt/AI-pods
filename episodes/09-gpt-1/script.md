# Episode 9: GPT-1 and pre-training

## Cold open

ALICE: Okay, picture this. It's early 2017, at OpenAI in San Francisco. A researcher named Alec Radford and two colleagues have trained a neural network to do one really boring thing.

FRANK: How boring are we talking?

ALICE: Very boring. They gave it Amazon reviews. Eighty-two million of them. And its only job was to guess what comes next. Not even the next word: the next character. The next letter, space or comma.

FRANK: So, autocomplete. For product reviews.

ALICE: Autocomplete for product reviews. It trained for about a month, on four graphics cards. And then they looked inside the network, at its four thousand or so artificial neurons, the little number-crunching units it's built from, to see what it had picked up.

FRANK: And?

ALICE: They found one single neuron that tracked whether the review was positive or negative. As the network read a review, that neuron would go up when the writer sounded happy, and down when they got angry. It became known as the sentiment neuron.

FRANK: Wait. Nobody told it about positive and negative?

ALICE: Nobody. It never saw a label. It was only ever asked, "what comes next?" Their best guess is that if you want to predict the next letter of a review, it really helps to know whether the person writing it is delighted or furious. So it worked that out on its own.

FRANK: Huh. That's a little bit spooky.

ALICE: It gets better. They could grab that neuron, pin it at "positive", and let the model write. And it wrote things like: "Best hammock ever! Stays in place and holds its shape."

FRANK: Okay, that's a real review. I've read that review.

ALICE: And pinned at "negative": "The package received was blank and has no barcode. A waste of time and money."

FRANK: Also a real review. Possibly mine.

ALICE: So here's why this matters. About a year later, Radford and colleagues took the same idea: just train a model to predict what comes next, and see what it learns along the way. But this time they used a brand-new design that everyone was excited about, the transformer. The paper came out in June 2018, with a fairly dull title: "Improving Language Understanding by Generative Pre-Training". Today we call that model GPT-1.

FRANK: The first GPT.

ALICE: The first GPT. The great-grandparent of ChatGPT, you could say. And it's today's episode.

## Welcome

FRANK: Welcome to From Zero to ChatGPT. This is episode nine, and the start of part three: the birth of large language models. I'm Frank.

ALICE: And I'm Alice. And I've been looking forward to this one, because GPT is everywhere. It's right there in the name ChatGPT. And I'd bet most people who use it every day couldn't tell you what the three letters stand for.

FRANK: So that's our promise for today. By the end, you'll know what G, P and T mean, and why each one mattered. We'll also meet GPT's big rival from 2018, a Google model called Bert. And if you're planning to read the GPT-1 paper, think of this as your warm-up. We'll even close with a little guide to reading it.

ALICE: Good, because papers and I have a complicated relationship. And what if someone's jumping in at episode nine?

FRANK: Then welcome, and we'll do quick reminders as we go. Here's the only one you need right now, from episode two. A model is basically a machine with millions of adjustable knobs. Something goes in, an answer comes out, and training means turning all those knobs, a tiny bit at a time, until the answers are less wrong.

ALICE: Knobs. Got it. So where do we start?

FRANK: With the problem GPT solved. And for that, we go back to 2017.

## The labeling problem

FRANK: So, 2017. Say you want a computer to do something useful with language. Sort movie reviews into thumbs up and thumbs down. Answer questions about a paragraph. Or tell whether one sentence follows from another.

ALICE: Okay.

FRANK: The standard recipe went like this. Collect thousands of examples, and have people label every single one. This review: positive. This one: negative. Then build a model for that one task, and train it from scratch.

ALICE: From scratch meaning the knobs start out random?

FRANK: Random. A brand-new model that knows nothing. Not English, not grammar, not what a movie even is. It has to learn all of that, plus the task, from your pile of examples.

ALICE: That sounds like teaching someone to grade essays before they can read.

FRANK: That's exactly the problem. And labels are expensive. One well-known dataset from those years had over half a million sentence pairs, each one written and labeled by paid crowdworkers. A huge effort, for one task.

ALICE: And the next task needs a whole new pile.

FRANK: A new pile and a new model. Every time.

ALICE: Hang on, though. Wasn't there something you could reuse? Episode six was all about word embeddings, the thing where "king minus man plus woman" lands you on "queen". Those were learned from plain text, with no labels.

FRANK: Right, and that was the one piece people did reuse. You could download a ready-made list of numbers for every word that captured, roughly, what it means. But that only covers the very first step: turning words into numbers. Everything after that, all the layers that combine words into meaning, still started from scratch.

ALICE: So it's kind of like...

FRANK: It's like handing a newcomer a dictionary. Really useful. But knowing what each word means isn't the same as having read a lot. The dictionary won't tell you how stories go, or what sarcasm sounds like.

ALICE: Okay, fair. A dictionary, but no reading experience.

FRANK: And meanwhile, the people working on images were way ahead. Remember ImageNet, the giant collection of labeled photos from episode five? By then, if you wanted a model to spot, say, fractures in X-rays, you didn't start from scratch. You took a network that had already been trained on ImageNet, one that had already learned edges and textures and shapes, and you trained it a little more on your few thousand X-rays.

ALICE: So with images, you could reuse the whole network. With language, just the dictionary. Why didn't language just copy the image people?

FRANK: Because ImageNet itself took millions of labels. Somebody had to tag every photo. For language, there was nothing like that, nothing that would teach a model language in general. What there was, was an ocean of text. Books, Wikipedia, the whole web. Billions and billions of words, and none of it labeled.

ALICE: So the question is: can a model learn from text that nobody labeled?

FRANK: That's the question. And Alice, I believe the answer is yours.

## Text that grades itself

ALICE: It is. And the answer is a trick so simple it almost sounds like cheating. Frank, finish this sentence. "The cat sat on the..."

FRANK: Mat.

ALICE: Probably "mat". Now here's the beautiful part. To check if you got it right, nobody has to label anything. You just look at the next word in the text. It's like reading a book with your hand over the page. You guess the next word, slide your hand along, and check.

FRANK: So the book is its own answer key.

ALICE: The book is its own answer key. Every word in it is a free practice question. A novel with a hundred thousand words is a hundred thousand exercises. And suddenly, that whole ocean of unlabeled text is training data.

FRANK: Okay, but hold on. Guessing the next word sounds like a party game. Why would you learn anything deep from that?

ALICE: Because to be really good at it, you have to know a lot. Let's try a few. "The keys to the cabinet..." is, or are?

FRANK: Are. The keys are.

ALICE: Even though "cabinet", right next to it, is singular. So that's grammar. "The capital of France is..."

FRANK: Paris. Okay, so that's facts.

ALICE: Facts. "We waited forty minutes, the soup was cold, and the waiter was rude. Overall, I'd give this place..."

FRANK: One star. Maybe zero.

ALICE: That's mood, which is exactly what that sentiment neuron picked up. And my favorite comes from Ilya Sutskever, one of GPT-1's authors, who explains it with a detective novel. Hundreds of pages, a big cast of characters, clues everywhere. And on the last page, the detective gathers everyone in the room and says: "And the murderer is..."

FRANK: Oh. So to guess that word...

ALICE: ...you'd have to have followed the whole plot. That's the point. The better you get at guessing the next word, the more you're forced to take in what you've read.

FRANK: Okay, but couldn't a model just get good at sounding plausible? Without really understanding anything?

ALICE: That's the big debate, and we'll get into it in episode ten. What nobody disputes is that it learns a lot of useful stuff along the way. You'll see that in the results in a minute.

FRANK: So how does the training actually work? It guesses a word, and it's either right or wrong?

ALICE: Not quite. It doesn't guess just one word. It spreads its bets across every word it knows. Say, "mat" forty percent, "floor" twenty, "sofa" ten, and tiny slivers for everything else. Then it sees the real next word, and the question is: how surprised was it? If it bet big on the right word, small surprise. If it gave the right word almost nothing, big surprise.

FRANK: And the surprise is the "how wrong" from episode two.

ALICE: Exactly. That's the loss. Then all the knobs get nudged a tiny bit, in whichever direction would have made the right word more likely. That's the walking downhill in fog from episode four. So next time, it bets a little more on the word that actually came. Do that over billions of words...

FRANK: ...and you get a very good bettor.

ALICE: A very good bettor. And a model that does this, that predicts the next word, has a name. It's called a language model.

FRANK: As in large language model.

ALICE: As in large language model. That's the LM in LLM. So at heart, an AI chatbot like ChatGPT is a very big next-word predictor.

FRANK: Well, technically it's tokens, isn't it? The word pieces from episode six.

ALICE: Technically tokens, yes. But "next word" is close enough. And one more bit of jargon, because it's all over the paper. Learning from text that nobody labeled, the paper calls "unsupervised". These days, most people call it self-supervised, because the text supervises itself.

FRANK: Self-supervised. I like that better.

ALICE: Me too. Frank, you've got the paper itself.

## G, P and T

FRANK: I do. So, June 2018. OpenAI publishes the paper. Four authors, including Alec Radford from the cold open, and Ilya Sutskever. And the model has three ingredients, which are the three letters. Let's take them in order. G is for generative.

ALICE: Meaning it generates text?

FRANK: In a way. It learns by predicting the next word, over and over, the guessing game we just played. And that same skill is what lets it write. P is for pre-trained, and that's the big idea. "Pre", because this training happens before you've even decided which task you want. First, the model just reads.

ALICE: Reads what?

FRANK: A collection called the Books Corpus. About seven thousand free e-books, mostly novels, from a self-publishing site called Smashwords.

ALICE: Why novels, and not, say, the news?

FRANK: Because a novel is one long, continuous story. To predict the next word, you often need something from a few paragraphs back: who's in the room, what just happened. The paper makes a point of this. The other big dataset people used back then was about a billion words of news sentences, but shuffled, so every sentence was cut off from its neighbors.

ALICE: So there's no plot to follow.

FRANK: No plot. And following plots is the whole point. Fun detail: when researchers later went through the collection, about a quarter of it turned out to be romance novels.

ALICE: So the first GPT learned English from romance novels.

FRANK: A lot of romance. Plenty of fantasy, and a surprising number of vampires. To give you a sense of how much reading it is: at one book a week, seven thousand books would take you about a hundred and thirty-five years.

ALICE: Wow. And the authors were okay with this?

FRANK: Nobody asked them. Lots of those books said they were for the reader's personal enjoyment only. Back in 2016, when a reporter told one of the authors that Google was training AI on the collection, they said it hadn't even occurred to them that a machine could read their book. And that question, whose writing these models get to learn from, is now being fought over in court.

ALICE: Okay. So that's G and P.

FRANK: And T is for transformer. The design from episode eight, and from the "Attention Is All You Need" paper. Quick reminder: the older networks from episode seven, the LSTMs, read one word at a time, and they tended to forget the start of a long passage. A transformer takes in the whole passage at once, and every word can pay attention to every other word.

ALICE: And the original transformer had two halves, right? It was built for translation.

FRANK: Right. An encoder, which reads the sentence you want translated, and a decoder, which writes the translation, one word at a time. If you remember the famous diagram in that paper, with two towers side by side, the encoder is the left tower and the decoder is the right one. And the decoder has a rule. When it's writing word five, it can only look back at words one to four. No peeking ahead, because ahead hasn't been written yet.

ALICE: Makes sense.

FRANK: So GPT-1 kept just the decoder. The writing half. Twelve layers of it, with that no-peeking rule built in. Which is exactly what next-word prediction needs: if the model could see the next word, it would just copy it.

ALICE: And how big was it?

FRANK: About a hundred and seventeen million knobs. Or parameters, as the papers say. And it could look at about five hundred tokens at a time, roughly a page of text.

ALICE: A page? So it couldn't have solved that murder mystery.

FRANK: Not from the whole novel, no. One page at a time. Today's models can take in entire books at once, and we'll get to that in episode ten.

ALICE: And a hundred and seventeen million knobs, that sounds like a lot.

FRANK: In 2018, it was. Today's biggest models have thousands of times more. And pre-training took about a month on eight graphics cards. The big ones today train on tens of thousands of chips, for months.

ALICE: But why the transformer? Couldn't you do all this with the older networks?

FRANK: You could, and people had. The recipe itself wasn't new: other teams had already made it work with LSTMs. But LSTMs struggle to hold on to things from far back, and a transformer can look straight back across the whole page. The paper checked, too: same recipe with an LSTM instead, and the scores clearly dropped.

ALICE: So the T really earned its place.

FRANK: It did. Oh, and one detail you might not expect from today's OpenAI. They released the trained model, with code to fine-tune it, for anyone to use.

ALICE: Huh. Different times.

FRANK: Different times. So now we've got a model that's read seven thousand novels. Alice, what do you actually do with it?

## Fine-tuning

ALICE: That's step two: fine-tuning. Because a model that's great at guessing the next word in a romance novel isn't, on its own, something anybody needs.

FRANK: Nobody's paying for vampire autocomplete.

ALICE: Not in 2018, anyway. So you take the pre-trained model, and you add one tiny extra piece on top. Its only job is to turn what the model has worked out into an answer, like "positive" or "negative". Then you train the whole thing a little more, on the labeled examples for your task.

FRANK: How much more?

ALICE: Very little. For most tasks, they went through the labeled examples just three times. Pre-training took a month. Fine-tuning is a quick top-up.

FRANK: So the reading is the expensive part, and you only do it once.

ALICE: Exactly. Think of it like hiring. You need two new people to sort customer emails. One of them has read seven thousand books. The other has never read anything. Can't read at all.

FRANK: I know which one I'm hiring.

ALICE: Right? The reader just has to learn what you want. The other one has to learn English first, from your pile of customer emails. And before 2018, pretty much every model was the second person, give or take a dictionary. Here's how I think about it. Fine-tuning doesn't teach the model language. It already has that. Fine-tuning teaches it which of the things it already knows you care about.

FRANK: Like that sentiment neuron. The knowledge was already in there.

ALICE: Exactly like that. Fine-tuning just points at it.

FRANK: Okay, but tasks come in different shapes, don't they? A movie review is one piece of text. But "does sentence B follow from sentence A" is two pieces.

ALICE: And this is one of the cleverest bits of the paper. The usual approach was to build custom machinery on top of the model for each kind of task. GPT-1 doesn't. It turns every task into one single stretch of text, because that's the only thing the model knows how to read.

FRANK: How?

ALICE: You glue the pieces together, with a special separator in between. Sentence A, separator, sentence B. The model reads it as one passage, and the extra piece on top says whether B follows from A, contradicts it, or neither. For multiple choice, you glue the story or the question to each possible answer, one at a time, the model scores each version, and the best score wins.

FRANK: Give me an example.

ALICE: Okay. One of their tests was called the Story Cloze Test. You get a four-sentence story and two possible endings, and you pick the right one. Here's an example from the people who made the test. "Tom and Sheryl have been together for two years. One day, they went to a carnival together. He won her several stuffed bears, and bought her funnel cakes. When they reached the Ferris wheel, he got down on one knee."

FRANK: Oh, I know where this is going.

ALICE: Ending one: "Tom asked Sheryl to marry him." Ending two: "He wiped mud off of his boot."

FRANK: I mean, it's not impossible.

ALICE: Not impossible. But you know which one is right, because you know how stories like that go. That's common sense, and it's really hard to label. But seven thousand novels are full of it.

FRANK: So how did it do?

ALICE: On that test, the best score before was about seventy-eight percent. GPT-1 got eighty-six and a half. And overall, they tried it on twelve different tests, and it set a new record on nine of them. One model, with almost no custom parts.

FRANK: Nine out of twelve. That's not bad.

ALICE: Not bad at all. Though a record isn't the same as a good grade. On a reading test made from English exams for school kids in China, it scored fifty-nine percent, up from fifty-three.

FRANK: Fifty-nine. I mean, that's not a great grade.

ALICE: It isn't. When the test's makers had paid crowdworkers take it, they averaged about seventy-three. So, a big jump, but still well behind people.

FRANK: And how do we know the reading did the work? Maybe the transformer alone would have done just as well.

ALICE: They tested exactly that. Same model, same tasks, but skip the month of reading. On average, its scores dropped by about fifteen points.

FRANK: Fifteen points. So the reading was most of it.

ALICE: The reading made the difference. And here's why this matters today. That two-step recipe, first pre-train on a mountain of raw text, then fine-tune for what you actually want, is still how ChatGPT is made. Both steps are much bigger and fancier now, and we'll see how in episode twelve. But when you read in the news that some lab has finished a big pre-training run...

FRANK: ...that's the P in GPT.

ALICE: That's the P in GPT. And Frank, I think this is where Google comes into the story.

## Bert

FRANK: It is. Four months after GPT-1, in October 2018, a team at Google published Bert.

ALICE: Bert. As in Sesame Street?

FRANK: As in Sesame Street. Earlier that year, a lab called the Allen Institute had put out a model named Elmo, which also learned from raw text. So, you know. Officially, Bert stands for Bidirectional Encoder Representations from Transformers.

ALICE: That is a name somebody worked out backwards.

FRANK: Oh, absolutely. But two of those words tell you the whole story: "bidirectional" and "encoder". Let's start with the problem Bert went after. GPT reads strictly left to right. When it works out what a word means, it can only use the words that came before it.

ALICE: Because of the no-peeking rule.

FRANK: Right. Which is perfect for writing. But for understanding, it's a handicap. Take the sentence, "The bank was steep and muddy." When GPT gets to "bank", it hasn't seen "steep and muddy" yet. So, money, or river?

ALICE: But I'd be confused at "bank" too, until I read on.

FRANK: Sure. And GPT can sort of catch up later in the sentence. But its picture of "bank" itself is built from the left side only. Bert's argument was that for real understanding, every word should get to see the whole sentence, in both directions.

ALICE: So why not just let the model look both ways?

FRANK: Here's the catch. If you're training it to predict the next word, and it can look both ways...

ALICE: ...then it can see the next word. Oh. It just copies the answer.

FRANK: It just copies the answer. So Google changed the game. Instead of "guess the next word", Bert plays fill-in-the-blank. Take a passage, hide about fifteen percent of the words, and the model has to guess the hidden ones, using everything on both sides.

ALICE: Like the fill-in-the-blank exercises from language class.

FRANK: Exactly like those. Reading researchers call that a cloze test, an idea from 1953, and the Bert paper actually cites it. The paper's own term is a "masked language model". Masked, as in covered up.

ALICE: And the "encoder" part?

FRANK: Once you're hiding words instead of predicting the next one, you don't need the no-peeking rule anymore. So Bert uses the other half of the transformer: the encoder. The reading half. The left tower, where every word sees every other word.

ALICE: So GPT took the writing half, and Bert took the reading half.

FRANK: That's the cleanest way to put it.

ALICE: And did it work?

FRANK: Very well. And they made it a fair fight. They built the smaller version of Bert to be the same size as GPT-1, on purpose, so the two could be compared. And across the same set of language tests, that Bert averaged about four and a half points higher. A bigger Bert, three times the size, beat GPT-1 by about seven.

ALICE: Ouch.

FRANK: To be fair, Bert also read all of English Wikipedia on top of the same books, so about four times as much text. But the Bert team also tried a version that only read left to right, with the same text, and it did clearly worse. Looking both ways was a big part of the win.

ALICE: So GPT-1 got about four months at the top.

FRANK: About four months. And Bert took off. Researchers everywhere built on it. And a year later, Google put it into search. In October 2019, they said Bert was helping with about one in ten searches in English in America. Their example was a search for "2019 Brazil traveler to USA need a visa".

ALICE: Okay...

FRANK: Older systems tended to miss what little words like "to" were doing, so they'd show you results about Americans traveling to Brazil. Bert understood that "to" matters here. It's a Brazilian, heading to the United States.

ALICE: Oh, that's a good example. One tiny word changes the whole meaning.

FRANK: And that's Bert's strength. Careful reading.

ALICE: Okay, but now I have to ask. If Bert won, why is the thing on my phone called ChatGPT? Why not, I don't know, Chat-Bert?

FRANK: That one, I'm handing to you.

## Why the writer won

ALICE: Okay. So Bert has one big limitation. It's a brilliant reader, but it can't really write.

FRANK: Why not? It knows language.

ALICE: It was trained to fill in blanks inside text that already exists. Ask it to continue a story, and there's no natural way for it to do that. GPT, on the other hand, learned exactly the skill writing needs: given everything so far, what comes next? To make it write, you just add its guess to the end, and ask again.

FRANK: But in 2018, writing wasn't what anyone was measuring. Everyone was chasing test scores.

ALICE: And on test scores, Bert was better. But the GPT-1 paper has a short section near the end that I think is the most important part of the whole thing. And it's really easy to skim past. It's called "zero-shot behaviors".

FRANK: Zero-shot, meaning...

ALICE: Zero examples. No fine-tuning at all. They took the pre-trained model, the one that had only ever read novels, and asked: can it already do any of these tasks, just by predicting words?

FRANK: How would you even ask it?

ALICE: You have to be a bit sneaky. For movie reviews, they took the review, added the word "very" at the end, and checked which word the model thought was more likely to come next: "positive", or "negative".

FRANK: Oh, that's clever. "Two hours of my life I'm never getting back. Very..."

ALICE: "...negative." And with that trick, and no training on the task at all, it got about eighty percent of the reviews right. Not a record, but in the same range as some of the classic methods. On the other tasks they tried, the scores were still pretty weak.

FRANK: So, a party trick.

ALICE: Kind of. But here's the part that stuck with me. As pre-training went on, these zero-shot scores kept climbing. Nobody was teaching the model about movie reviews, or exam questions. It was just reading novels, and getting better at those tasks along the way.

FRANK: So the reading itself was teaching the tasks.

ALICE: That was their guess, in the paper. To get better at predicting the next word, the model ends up learning to do a lot of these tasks. And their blog post had a line that reads like quite the understatement now. They wrote that there was "significant room for improvement" with more computing power and more data.

FRANK: Just a little room.

ALICE: Just a little. Eight months later came GPT-2, more than ten times bigger, trained on far more text. And it could do quite a few things nobody had fine-tuned it for. That's episode eleven. So Bert won the battle of 2018. But the idea that won the decade was GPT's: one model that writes, made bigger and bigger.

FRANK: And Bert? Did it just disappear?

ALICE: Not at all. Models descended from Bert still quietly do a lot of the work in search and in sorting text. But the road to ChatGPT ran through GPT. Frank, you promised us a guide to the paper.

## Reading the paper

FRANK: I did. So if you're going to read it after this, and I think you should, here's what to expect.

ALICE: Yes, please.

FRANK: Good news first: it's short. Twelve pages, and the last four or so are references. And here's a fun one. The name GPT isn't in it. Not once. In the results tables, the model is called "Fine-tuned Transformer LM". LM, as in language model. The name GPT came later. By October, Google's Bert paper was calling it "OpenAI GPT".

ALICE: So the most famous name in AI isn't even in its own paper.

FRANK: Not once. Next, the vocabulary. "Unsupervised pre-training" is the reading stage, learning from text that nobody labeled. "Supervised fine-tuning" is the second stage, with the labeled examples.

ALICE: Okay, those I can handle.

FRANK: "Textual entailment" is the "does sentence B follow from sentence A" task. "State of the art" just means the best score so far, what we've been calling a record. And "discriminative" tasks are the judging ones, like positive or negative, as opposed to generating text.

ALICE: Got it. And the equations?

FRANK: There are a few, but you don't need them. The first one, the important one, just says, in symbols: make the real next word as likely as possible, given the words that came before it. That's the whole pre-training game.

ALICE: That's it?

FRANK: That's it. Then, spend some time on Figure 1. The right-hand side shows the gluing trick, how each kind of task gets turned into one stretch of text. And don't skip section five. That's where the zero-shot experiments are, with a chart of those scores creeping upward as pre-training goes on.

ALICE: And what can I skip?

FRANK: The training settings. Learning rates, dropout, that kind of thing. Unless you're into that. The rest is in the show notes, with a little glossary.

## Recap

ALICE: Okay, let's wrap up. Frank, do you want to start?

FRANK: Sure. One: before 2018, language AI was mostly built from scratch for each task, on examples people had to label by hand. Slow, expensive, and you started over every time.

ALICE: Two: next-word prediction turns any text into free practice. The text is its own answer key. And to predict well, a model has to pick up grammar, facts, mood, even plot.

FRANK: Three: GPT stands for generative pre-trained transformer. GPT-1, from June 2018, spent a month reading about seven thousand books, using the writing half of the transformer.

ALICE: Four: then comes fine-tuning. A short round of training on each task's labeled examples, with every task glued into one stretch of text. It set records on nine of twelve tests. And that two-step recipe, pre-train, then fine-tune, is still how chatbots are made.

FRANK: And five: Bert, from Google, played fill-in-the-blank with the reading half of the transformer, and beat GPT on the 2018 tests. But Bert couldn't write, and GPT's zero-shot results hinted that more reading would teach it even more.

ALICE: Which leaves a question we've been dodging all episode. We keep saying it "predicts the next word". So what actually happens when you type a question into ChatGPT and press Enter?

FRANK: That's episode ten. How a word guesser picks its words, what "temperature" means, and why it sometimes makes things up with total confidence.

ALICE: See you then.
