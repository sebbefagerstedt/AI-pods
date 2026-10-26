# Episode 8: "Attention Is All You Need", explained

## Cold open

ALICE: Frank, how do you decide whose name goes first on a research paper?

FRANK: Usually? Whoever did the most work goes first. And there's a lot of quiet arguing about it.

ALICE: A lot of arguing. So here's a paper from June 2017, from Google. Eight authors. And at the bottom of the first page, there's a little footnote. It says: "Equal contribution. Listing order is random."

FRANK: Random? They just shuffled the names?

ALICE: Shuffled the names. And then the footnote goes on, and says what each person actually did. This one proposed the core idea. This one built the first version. This one came up with two of the key pieces. This one wrote the code everything ran on. Like a little thank-you note.

FRANK: That's kind of lovely, actually.

ALICE: It is. And the rest of the story is fun too. The team called itself Team Transformer. An early design document had pictures of characters from the Transformers toys on it. The name came about because one of them, Jakob Uszkoreit, just liked the sound of the word. And the title is a little nod to a Beatles song.

FRANK: "All You Need Is Love".

ALICE: "Attention Is All You Need". And here's the bit nobody could have guessed in 2017. Today, it's one of the most cited scientific papers of this century. Every chatbot you've used is built on the design in it. And every one of those eight authors has since left Google, many of them to start their own AI companies.

FRANK: All eight?

ALICE: All eight. So today, we're opening that paper. And if you've read it, like I know some of our listeners have, this episode is your companion. We'll go through the big ideas in plain words. And I'll point at the bits of the paper where each one lives.

## Welcome

FRANK: Welcome to From Zero to ChatGPT. I'm Frank.

ALICE: And I'm Alice.

FRANK: So, last time, we left the older networks in an awkward spot. The LSTMs. They read a sentence one word at a time, like someone with a notebook, and they forget the start of long passages. And for translation, attention was bolted on, so the writer could glance back at every word of the original.

ALICE: And attention was the part doing the clever work.

FRANK: Which is exactly what the Google team noticed. So their idea was: keep the attention. Throw away the reading one word at a time. Today we'll see how that works. Self-attention. Queries, keys and values, which is where most people's eyes glaze over in the paper, and which I promise is simpler than it looks. Multi-head attention. How a model that reads everything at once still knows the word order. And why all of this made training so much faster.

ALICE: And all of it without an equation.

FRANK: There's one equation in the paper that everyone remembers. We'll talk about it, in words. And Alice, I'll start.

## Every word looks at every word

FRANK: So, here's a sentence that comes from Google's own blog post about the paper. "The animal didn't cross the street because it was too tired."

ALICE: "It" is the animal. Streets don't get tired.

FRANK: Now: "The animal didn't cross the street because it was too wide."

ALICE: Now "it" is the street.

FRANK: One word changed, at the very end. And "it" points at something completely different. So to understand "it", you need to look at other words in the sentence. Sometimes far away. Last time, attention let the translator look back at the original sentence. Here's the new idea: let every word in a sentence look at every other word in the same sentence.

ALICE: In the same sentence. Not across to another one.

FRANK: In the same sentence. That's why it's called self-attention. The sentence pays attention to itself. And here's what happens. Every word starts out as its embedding, its list of numbers from the word map. Then each word looks at all the others and asks: which of you matter to me? It gives each one a score. And then it builds a new version of itself, by mixing in a bit of each word, in proportion to its score.

ALICE: So "it" looks around, gives "animal" a high score, and "street" a low one...

FRANK: ...and the new version of "it" has a lot of "animal" mixed in. Now "it" doesn't just mean "it" anymore. It means, roughly, "it, the tired animal".

ALICE: Oh, that's the "bank" problem from a couple of episodes ago. The word map gives "bank" one meaning. But after self-attention, "bank" can mix in "river" or "money", whichever's nearby.

FRANK: Exactly that. Self-attention turns the dictionary meaning of a word into its meaning in this sentence. And every word does this at the same time. Every word looks at every word.

ALICE: Okay. And how is that different from the old way? The LSTM with its notebook?

FRANK: Think of the difference between a game of telephone and a meeting. In the LSTM, information gets passed along, word by word, like a whisper down a line. By the time "it" hears about "animal", it's been passed through a lot of people. In self-attention, everyone's in the same room. "It" can talk to "animal" directly, in one step, however far apart they are.

ALICE: No whispering.

FRANK: No whispering, no fading. And you do this in layers, like everything else. After the first round, every word has been updated. Then the second layer does it again, but now every word is already a bit smarter about its context. The paper uses six layers.

ALICE: Okay. That's the big idea. But how does "it" actually decide that "animal" deserves a high score? That's the part I want.

FRANK: And that's queries, keys and values. That's yours.

## Queries, keys and values

ALICE: It is. So, this is the part of the paper with the scary letters. Q, K and V. And here's how I think about it. Picture a big networking event. Everyone's wearing a name badge. And the badge doesn't just say your name. It says what you can help with. "Expert in tax law." "Knows everything about dogs."

FRANK: Okay.

ALICE: And everyone walks in with a question. Something they're looking for. "I need someone who knows about moving abroad." And when your question matches someone's badge, you go and talk to them. And they tell you what they know.

FRANK: So, three things. My question, their badge, and what they actually tell me.

ALICE: Three things. Your question is the query. Their badge is the key. And what they tell you is the value. Query, key, value.

FRANK: Okay, so in our sentence.

ALICE: In our sentence, every word makes all three. From its own list of numbers. So "it" makes a query, something like: "I'm a pronoun. I'm looking for the thing I refer to. Probably a noun, probably something that can be tired." And "animal" has a key, its badge, that says something like: "I'm a noun. A living thing." The query and the key match really well. High score.

FRANK: And "street"'s badge says "noun, a place, can't get tired".

ALICE: Roughly. Lower score. Then you turn all the scores into percentages that add up to a hundred. "Animal", say, seventy percent. "Street", ten. Everything else gets a bit. And then "it" collects the values. Seventy percent of what "animal" has to say, ten percent of what "street" has to say, and so on. That blend is the new "it".

FRANK: Why are the badge and what they tell you separate things? Why not just use the same list for both?

ALICE: Good question. Because what makes someone worth listening to isn't the same as what you get from them. The badge is a quick advertisement. "Noun, living thing". But what "animal" hands over can be much richer. Everything it's worked out about itself. That it's the subject of the sentence, that it didn't cross. Keeping them separate gives the model more room.

FRANK: Okay. And who writes the badges and the questions? Who decided "it" should look for nouns?

ALICE: Nobody. And you can guess what I'll say. Each word makes its query, key and value by running its numbers through three sets of knobs. And those knobs are learned. Walking downhill in fog. The model is trained on translation, and over millions of sentences, it works out which questions and badges are useful. "Pronoun looking for its noun" is something it figures out because it helps translate.

FRANK: And the famous equation?

ALICE: That's it. That's all the equation says. Compare every query with every key, to get scores. Turn the scores into percentages. Use the percentages to blend the values. There's one extra step, where the scores get scaled down a bit so they don't get too extreme, which is why it's called "scaled dot-product attention". But that's the whole thing. A question, a badge, and an answer.

FRANK: Huh. I've looked at that equation and run away. That's much friendlier.

ALICE: It's honestly simple. The magic is in doing it at scale, for every word at once, and in what the knobs learn. Frank, you've got the many heads.

## Many heads

FRANK: I do. So, one round of attention gives each word one set of scores. One way of looking at the sentence. But a word has lots of relationships at once. Take "it" again. It cares about which noun it refers to. But also about the verb, "was". And maybe whether there's a "not" somewhere. One set of scores has to squash all of that together.

ALICE: So one query isn't enough.

FRANK: One query isn't enough. So the paper does attention several times, side by side. Eight times, in their model. Each one with its own knobs, so its own kind of queries, keys and values. Each one is called a head. And that's multi-head attention.

ALICE: Like eight people reading the same sentence, each with a different-colored highlighter.

FRANK: That's a perfect way to put it. One reader highlights grammar: which words go together. Another tracks who "it" and "she" refer to. Another just looks at the words right next door. And then all eight sets of highlights get combined back into one updated word.

ALICE: And do the heads actually end up doing different things? Or is that just a nice story?

FRANK: There's evidence in the paper itself. If you've got it handy, flip to the very end, after the references. There are some colorful pictures of the heads at work. In one, there's a sentence about governments "making the registration or voting process more difficult". And several heads, looking from the word "making", reach all the way across the sentence to "more difficult".

ALICE: Because "making" goes with "more difficult". Even with lots of words in between.

FRANK: Exactly. In another, there's a sentence about "the law" and "its application". And two heads, looking from "its", point sharply at "law". Working out what "its" refers to. Nobody programmed that. The heads specialized on their own, because it helped translation.

ALICE: Okay. But wait. We've got every word looking at every other word, all at once. In a big meeting. How does the model know what order the words came in? "Dog bites man" and "man bites dog" would be the same meeting.

FRANK: That is exactly the right worry. And it's yours.

## Keeping the order

ALICE: It is. So, Frank's right. In a meeting where everyone talks to everyone, there's no first and last. If you give self-attention "dog bites man", every word sees the same other words. It's a bag of words again. Shuffle the sentence, and you get the same result, just shuffled.

FRANK: Which is a disaster for language.

ALICE: A disaster. The LSTM got order for free, because it read in order. So the transformer needs to put the order back in by hand. And the trick is to stamp every word with its position, before it goes in. Word one gets a "position one" stamp, word two a "position two" stamp. And the stamp is just more numbers, added onto the word's embedding.

FRANK: So the word "dog" in position one is slightly different from "dog" in position three.

ALICE: Exactly. Same word, different stamp. Now, the paper's stamps are a bit unusual. They're made from waves. And here's how I picture it. Think of an old clock, with a second hand, a minute hand and an hour hand. Each hand goes around at a different speed. At any moment, the combination of the three hands tells you exactly what time it is.

FRANK: And no two moments in a day look the same.

ALICE: No two moments look the same. The paper's stamps are like a clock with lots of hands, all spinning at different speeds. Some spin fast, so they change a lot from one word to the next. Some spin very slowly, so they tell you roughly where you are in a long passage. And each position gets the reading of all those hands.

FRANK: Why waves, though? Why not just number them? One, two, three.

ALICE: Because plain numbers get huge in a long text, and the model would see position nine hundred as wildly different from position ten. The clock hands always stay in the same range. And the authors hoped waves would also make it easy for the model to work out things like "three words back", wherever it is in the sentence. They also tried a version where the stamps were simply learned, like everything else, and the paper says the results were nearly identical.

FRANK: So the waves weren't essential.

ALICE: Not essential. GPT-1, a year later, just learned its stamps. And today's models mostly use a cleverer variation. But the principle is the same: the model has no sense of order unless you give it one, so you stamp it on.

FRANK: Okay. So: every word looks at every other word, using questions and badges, with eight heads, and a position stamp. I get how it works. But why was this such a big deal? The LSTM with attention was already translating pretty well.

ALICE: That's the part of the paper that changed everything. And Frank, it's yours.

## Why it trained so fast

FRANK: It is. So, think back to the LSTM. It reads word one, updates its notebook. Then word two. Then word three. And word three can't start until word two is done. It's a single-file line.

ALICE: Like one cashier at a supermarket.

FRANK: One cashier, a long queue. Now remember what graphics cards are good at, from the 2012 episode. They're a stadium full of schoolkids, each doing a simple sum, all at the same time. A single-file line wastes almost all of them. Most of the stadium sits there waiting.

ALICE: And the transformer?

FRANK: In the transformer, there's no line. Every word's queries, keys and values can be worked out at the same time. Every score, at the same time. In training, you hand it the whole sentence, and every word gets processed at once. That's exactly what the stadium is built for.

ALICE: So it's not just smarter. It's a better fit for the chips.

FRANK: A much better fit. And the paper says so in plain numbers. Their big model set a new record for English to German translation. And a new record for English to French. And it trained in three and a half days, on eight graphics cards. Their smaller model, in about twelve hours. The paper says this was a small fraction of the training cost of the best models before it.

ALICE: Records, and cheaper. That's a rare combination.

FRANK: Rare. And there's a second advantage, which we touched on. In the LSTM, information from far away has to travel through every word in between, fading as it goes. In the transformer, any word can reach any other word in one step. So distance doesn't hurt.

ALICE: Okay, there's got to be a catch.

FRANK: There is one, and it matters later. Every word looks at every other word. So with ten words, that's a hundred pairs. With a thousand words, a million pairs. Double the length of the text, and you get four times the work.

ALICE: So long texts get expensive fast.

FRANK: Very fast. That's why, for years, these models could only take in a page or two at a time. How much text a model can look at, at once, is called its context window. And a lot of work since has gone into stretching it. We'll get to that later in the series.

ALICE: And here's what I think is the real reason it mattered. Not the translation records. It's that the transformer could soak up enormous amounts of computing power. Remember the bitter lesson? The methods that win are the ones that can use more and more computers. The transformer was the first language design that could really use a stadium full of chips.

FRANK: So it didn't just win. It opened the door to scale.

ALICE: To scale. Which is the whole story of the next part of the series. But before we get there, there's one more thing in the paper everyone remembers. The diagram.

FRANK: The two towers.

ALICE: Can you take us through it, briefly? We'll come back to it in more depth later.

## The two towers

FRANK: Sure. So, the famous diagram has two towers, side by side. And remember, this was built for translation. The left tower is the encoder. It's the reader. It takes the whole English sentence, and runs it through six layers of self-attention, where every word looks at every other word, in both directions.

ALICE: And the right tower?

FRANK: The right tower is the decoder. The writer. It writes the German, one word at a time. And it has its own self-attention, with one important rule. When it's writing word five, it's only allowed to look at words one to four. No peeking ahead.

ALICE: Because word six hasn't been written yet.

FRANK: Right. And in training, where the whole correct translation is sitting there, the rule stops it from cheating by copying the next word. In the paper, that's the box labeled "masked" attention. And then the decoder has a second kind of attention, where it looks across at the encoder's notes on the English sentence. That's the old translation attention from last time, the translator glancing back at the original.

ALICE: So the arrows going from the left tower to the right tower...

FRANK: ...are the decoder looking across. And there are a few more boxes in each layer, things labeled "feed forward" and "add and norm". They matter, and we'll give them their own time later in the series, with a layer-by-layer look inside. For now: the left tower reads, the right tower writes, and the writer can't peek.

ALICE: And at the top of the right tower?

FRANK: Out come the probabilities for the next word. Which word is most likely to come next in the German translation.

ALICE: Hold on. The decoder is guessing the next word, given the words so far, without peeking.

FRANK: Exactly.

ALICE: That sounds a lot like what you'd need for, I don't know, a chatbot.

FRANK: And a few people noticed. Within about a year, one team took just the right tower, the writer, and taught it to predict the next word on thousands of books. Another team took just the left tower, the reader. Those became GPT and Bert. And that's where the next part of the series starts.

ALICE: The birth of large language models.

FRANK: The birth of large language models. From one footnote with the authors in random order.

## Recap

ALICE: Okay, let's wrap up. Frank, you start.

FRANK: Sure. One: the transformer, from Google in 2017, kept attention and threw away the reading one word at a time. In self-attention, every word looks at every other word in the same sentence, and builds a new version of itself from the ones that matter. That's how "it" learns it means the tired animal.

ALICE: Two: queries, keys and values. Every word makes a question, a badge and an answer, using learned knobs. Each word's question is compared with every badge, the scores become percentages, and the word collects a blend of the answers. That's the famous equation, in words.

FRANK: Three: multi-head attention runs several of these side by side, eight in the paper, like readers with different highlighters. The pictures at the end of the paper show heads linking "making" to "more difficult", and "its" to "law".

ALICE: Four: since everything happens at once, the model has no sense of order on its own. So each word gets a position stamp, made from waves at different speeds, like the hands of a clock.

FRANK: And five: because every word is processed at the same time, the transformer fits graphics cards perfectly. It set translation records at a fraction of the cost, and any word can reach any other in one step. The catch: doubling the text means four times the work. And the design has two towers: the encoder that reads, and the decoder that writes, without peeking.

ALICE: Which ends part two. We've got numbers for words, and a design that can read whole passages at once and train fast. So, next: what happens when you take the writing tower, and give it a mountain of books to read?

FRANK: That's next time. The start of part three. GPT-1, pre-training, and what G, P and T stand for.

ALICE: See you then.
