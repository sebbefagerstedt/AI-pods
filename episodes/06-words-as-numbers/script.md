# Episode 6: Words as numbers

## Cold open

ALICE: Frank, I'm going to use a word you've never heard. And I want you to tell me what it is.

FRANK: Okay.

ALICE: "A bottle of tesgwino is on the table."

FRANK: Tesgwino. No idea. Something in a bottle.

ALICE: "Everybody likes tesgwino."

FRANK: So it's something nice. A drink, maybe. Or a sauce?

ALICE: "Tesgwino makes you drunk."

FRANK: Okay, it's alcohol.

ALICE: "We make tesgwino out of corn."

FRANK: A corn beer! Or some kind of corn liquor.

ALICE: It's a corn beer, from Mexico. Spelled a bit differently from how I'm saying it. And notice what just happened. Nobody gave you a definition. You'd never seen the word. You worked out what it means entirely from the words around it.

FRANK: From the company it keeps.

ALICE: That's almost exactly how a British linguist named John Firth put it, in 1957. "You shall know a word by the company it keeps." And that sentence, more than fifty years later, turned into one of the most useful tricks in AI. A way to turn words into numbers that actually capture what they mean. Which is today.

## Welcome

FRANK: Welcome to From Zero to ChatGPT. I'm Frank.

ALICE: And I'm Alice.

FRANK: And this is the start of part two: teaching computers language. In part one, we built up how machines learn. A model is a machine with knobs. Neural networks wire those knobs into layers. Training means walking downhill in fog. And last time, in 2012, it all came together for photos.

ALICE: And photos were the easy case, in one way. A photo is already numbers. Every pixel is a few numbers for how red, green and blue it is.

FRANK: But a word isn't a number. A neural network can only multiply and add. You can't multiply "banana".

ALICE: So today: how do you turn words into numbers? And not just any numbers, but numbers where "banana" ends up somewhere near "apple". We'll meet the famous trick where king minus man plus woman lands on queen. And then tokens: what a language model actually reads, and why everybody in AI counts them.

FRANK: And this is one of my favorite topics, so Alice, I'm taking the first one.

## Numbers that mean nothing

FRANK: So, the obvious first idea. Make a list of every word in the dictionary, and give each one a number. "Aardvark" is one. "Abandon" is two. And so on, up to, say, fifty thousand.

ALICE: That seems sensible. Now every word is a number.

FRANK: It does seem sensible. But think about what a network does with those numbers. It multiplies and adds. So if "cat" happens to be number nine thousand, and "catalog" is nine thousand and one, the network sees them as almost the same. Because nine thousand and nine thousand and one are almost the same number.

ALICE: Oh. And "dog" is way off at, like, eleven thousand.

FRANK: Exactly. The numbers come from alphabetical order, and alphabetical order means nothing. So the numbers lie to the network. They say "cat" is like "catalog", and nothing like "dog".

ALICE: Okay, so what's the fix?

FRANK: The next idea people used was a bit more honest. Instead of one number per word, you give each word its own switch. Picture a row of fifty thousand light switches, one for every word in the dictionary. To say "cat", you flip on the cat switch and leave all the others off.

ALICE: Fifty thousand switches, one on.

FRANK: One on. And now nothing lies. "Cat" and "catalog" are different switches, so they're not falsely close. But here's the problem. "Cat" and "dog" are also different switches. Every word is exactly as different from every other word. "Cat" is as far from "dog" as it is from "democracy".

ALICE: So the network has no idea that cats and dogs have anything in common.

FRANK: None. It has to learn everything about every word separately. If it learns that you can feed a cat, that tells it nothing about whether you can feed a dog. And there are tens of thousands of words, and lots of them are rare. So you'd need an impossible amount of text to learn about each one on its own.

ALICE: Okay, so what we actually want is numbers where similar words get similar numbers.

FRANK: That's exactly what we want. Numbers with meaning built in. And Alice, that's where tesgwino comes back. You're up.

## A map of meaning

ALICE: Yes. So here's the idea. Instead of one number, or one switch, we give every word a short list of numbers. Let's start with just two. And think of those two numbers as a position on a map. Like a city on a map has two coordinates: how far east, and how far north.

FRANK: So every word is a dot on a map.

ALICE: Every word is a dot on a map. And the goal is to arrange the map so that words with similar meanings are close together. "Cat", "dog" and "hamster" in one neighborhood. "Monday", "Tuesday" and "Friday" in another. "Run", "jog", "sprint" in a third.

FRANK: That sounds great. But who draws the map? You can't place fifty thousand words by hand.

ALICE: Nobody draws it. The map learns itself. And that's where the company words keep comes in. Remember tesgwino. You knew what it was because of the words around it: bottle, drunk, corn. So words that show up in similar company probably mean similar things. "Cat" and "dog" both show up near "feed", "pet", "vet", "fur". "Monday" and "Tuesday" both show up near "next", "morning", "meeting".

FRANK: So similar neighbors, similar meaning.

ALICE: Similar neighbors, similar meaning. And in 2013, a team at Google, led by a researcher named Tomas Mikolov, turned that into a really simple training game. Take some text. Pick a word. And ask the model: what words are likely to appear around this one? Then check against the real text, see how wrong it was, and nudge.

FRANK: Walking downhill again.

ALICE: Walking downhill again. And the knobs being nudged are the positions of the words on the map. Every word starts at a random spot. And with each nudge, words that appear in similar company get pulled a little closer together. Do that over billions of words of text, and the map sorts itself out.

FRANK: How many words of text?

ALICE: The version they released was trained on about a hundred billion words of Google News. And they called the method word2vec. Word to vector. Vector is just the math word for a list of numbers.

FRANK: And the map has two dimensions? Just east and north?

ALICE: That's where it stops being a normal map. Two numbers aren't nearly enough to capture all the ways words can be similar. "Cat" is close to "dog" in one way, they're both pets. But close to "lion" in another way, they're both cats. And close to "kitten" in a third way. So you need more directions. Word2vec used three hundred numbers per word.

FRANK: A map with three hundred directions.

ALICE: Which, like the mountain with billions of directions, nobody can picture. But it works the same way. Every word has a position, and similar words are near each other. And the list of numbers for each word has a name. It's called a word embedding. You'll hear that word a lot. "Embedding" just means a word's position on this map of meaning.

FRANK: Okay. So that's a nice way to store words. But you promised me royalty.

ALICE: I did. Frank, the king's yours.

## King minus man plus woman

FRANK: So here's what made word2vec famous. When Mikolov's team looked at their finished map, they noticed that it hadn't just put similar words near each other. The directions between words meant something too.

ALICE: The directions?

FRANK: Let's go back to a city map. If you know the way from Paris to Berlin, it's a direction and a distance. Northeast, about a thousand kilometers. Now, on the word map, look at the step from "man" to "woman". It's a direction. And it turns out the step from "king" to "queen" goes in almost exactly the same direction. And so does "uncle" to "aunt". And "actor" to "actress".

ALICE: So there's a sort of "female" direction on the map.

FRANK: There's something like a "female" direction. Nobody put it there. It came out of the company words keep. So here's the trick. Start at "king". Take away the step for "man". Add the step for "woman". And look at what word you land closest to.

ALICE: Queen.

FRANK: Queen. King minus man plus woman is about queen. You can do arithmetic with meaning.

ALICE: That's the one that goes around. Does it work for other things?

FRANK: For lots of them. Paris minus France plus Italy lands near Rome. There's a direction for "capital of". There's one for past tense: "walk" to "walked" is roughly the same step as "swim" to "swam". And one for plurals, and for comparing: "big" to "bigger", "small" to "smaller".

ALICE: Wait, "swam"? That's irregular. Nobody taught it the grammar rule.

FRANK: Nobody taught it anything. It just saw that "swam" keeps the same company that "walked" does. Yesterday, last week, then. That's the magic of it.

ALICE: Okay, I have to be the skeptic here. Is it really that clean?

FRANK: Good. Because it's less clean than the famous example suggests. Two catches. First, when you do king minus man plus woman, the closest word is often... still "king". They quietly left out the words you started with. So it's really "the closest word that isn't king, man or woman". Still impressive. But a bit of a magic trick.

ALICE: And the second catch?

FRANK: The second catch is more serious. The map learns from human writing. So it learns our patterns, including the ugly ones. In 2016, a group of researchers published a paper with the title "Man is to Computer Programmer as Woman is to Homemaker?" Because that's the kind of thing the map produced.

ALICE: Oof. Because in the news, "programmer" kept company with "he".

FRANK: Exactly. The map didn't invent that. It soaked it up from millions of articles. And this is a lesson that comes back with every language model since: learn from human text, and you learn human biases along with it. People have spent years working on how to measure that and reduce it.

ALICE: Okay. So: word embeddings. Every word gets a list of numbers, a spot on a map, and similar words end up close. And it's learned from raw text.

FRANK: From raw text, with no labels. Nobody had to label anything. The text was its own answer key. And these embeddings became hugely popular. For years, almost any language project started by downloading word2vec's map, or one like it.

ALICE: Okay, but here's my question. When we say "word", what's a word? What does the model do with a word it's never seen? Or a typo?

FRANK: That's exactly the right question. And it's yours.

## Tokens

ALICE: It is. So, word2vec had a fixed list of words. Three million of them, which sounds like a lot. But language keeps making new ones. Names, brands, slang. Someone types "unfollowed". Or "covidiot". Or makes a typo: "langauge".

FRANK: And those aren't on the map.

ALICE: They're not on the map. The old fix was to swap every unknown word for one special word that just means "unknown". Which is like reading a book where every new word is blacked out.

FRANK: Not great. So why not go the other way? Use letters. There are only so many letters, and every word is made of them.

ALICE: People tried that. Every word becomes a string of letters, so nothing is ever unknown. But now a sentence is very long. "Unbelievable" is twelve letters instead of one word. And a single letter doesn't mean much on its own. The model has to do a lot of extra work just to figure out where the words are.

FRANK: So words are too big, and letters are too small.

ALICE: And the answer is in between: pieces of words. Common words stay whole. "The", "and", "house". Those get their own entry. But a rare word gets broken into pieces that do have entries. "Unbelievably" might become "un", "believ", and "ably". And a word you've never seen, like "covidiot", might become "cov", "id", "iot". Nothing is ever unknown, because in the worst case, you can always fall back to single letters.

FRANK: And those pieces are tokens.

ALICE: Those pieces are tokens. A token is a word, or a piece of a word. Sometimes a single character, or a space, or a punctuation mark. And that's what a language model actually reads. Not words. Tokens.

FRANK: How do you decide where to cut?

ALICE: That's learned too, from text. One popular method starts with single letters, and then keeps gluing together the pair that shows up most often. "T" and "h" become "th". Then "th" and "e" become "the". And so on, tens of thousands of times. The most common chunks become tokens. It's borrowed from an old trick for compressing files, from 1994. And in 2016 it was adapted for language models.

FRANK: And how big is the token list?

ALICE: GPT-2's had about fifty thousand tokens. Newer models have a hundred thousand or two hundred thousand. In English, a token works out to roughly three quarters of a word on average. So a thousand tokens is about seven hundred and fifty words.

FRANK: Okay. And each token gets its own spot on the map?

ALICE: Each token gets its own embedding, its own list of numbers. And here's how it's done in today's models. The very first thing a model does with your text is cut it into tokens, and look up each token's list of numbers in a big table. That table is the bottom floor of the model. And it's learned along with everything else, by walking downhill.

FRANK: So the word map isn't a separate thing anymore. It's built into the model.

ALICE: Built in. And much bigger than word2vec's three hundred numbers. In the big models it's thousands of numbers per token. Frank, tell them why everybody counts tokens.

## Why everybody counts tokens

FRANK: So, if you've ever used an AI model for work, or read about prices, you've seen it. Everything is counted in tokens. Companies charge per million tokens. A model's memory, how much text it can take in at once, is measured in tokens. Training data is measured in tokens. "Trained on fifteen trillion tokens."

ALICE: Because tokens are the model's actual unit. One token, one step.

FRANK: Exactly. The model reads tokens and writes tokens, one at a time. So the cost of running it is basically the number of tokens. And that has some surprising effects. First, other languages. Tokens are usually learned mostly from English text. So English words tend to be whole tokens. But in a lot of other languages, the same sentence gets chopped into many more pieces.

ALICE: So it costs more to use in other languages?

FRANK: Often, yes. Researchers measured this in 2023, and for some languages, the same text took many times more tokens than in English. Which means it's slower, more expensive, and fills up the model's memory faster.

ALICE: Huh. That's a fairness problem nobody would think of.

FRANK: It is. And second, my favorite one. Do you remember when people kept asking chatbots how many R's are in "strawberry", and they kept getting it wrong?

ALICE: Yes! They'd say two. It's three.

FRANK: And everyone laughed: this super-intelligent machine can't count letters. But think about what the model actually sees. It doesn't see s, t, r, a, w. It sees maybe two or three tokens. Something like "str", "aw", "berry". Each one is just a list of numbers. The letters are hidden inside.

ALICE: Oh. So asking it to count R's is like asking me how many brush strokes are in a word I've only ever heard spoken.

FRANK: That's a good comparison. It's a question about the spelling, and the model never sees the spelling directly. It can learn some of it, from text that talks about spelling, but it's working blind. Same reason older models were bad at reversing words, or at rhymes, or sometimes at arithmetic with long numbers. A number like 3,857 might be split into "385" and "7".

ALICE: Okay, that explains a lot. So, embeddings and tokens. Are we done? We have numbers for words.

FRANK: We have numbers for words. But there's a big problem left. Take the word "bank".

ALICE: River bank or money bank?

FRANK: Exactly. In our map, "bank" has one spot. One list of numbers. It can't be both. So it ends up somewhere awkward in the middle, between rivers and money. Same with "bat", the animal or the stick. "Light", not heavy or not dark.

ALICE: So the word map knows what words mean in general. But not what they mean in this sentence.

FRANK: That's it exactly. The word map is a dictionary. A very clever dictionary, but a dictionary. To know which "bank" you mean, you have to read the sentence. And that's the next problem: getting a network to read.

## Recap

ALICE: Okay, let's wrap up. Frank, you start.

FRANK: Sure. One: networks need numbers, and the obvious ways to turn words into numbers lie. Numbering words alphabetically makes "cat" look like "catalog". One switch per word makes every word equally different from every other.

ALICE: Two: the fix is word embeddings. Every word gets a list of numbers, a spot on a map of meaning, where similar words end up close together. You know a word by the company it keeps, so the map can be learned from raw text, with no labels.

FRANK: Three: word2vec, from Google in 2013, learned that map by guessing which words appear near each other. And directions on the map mean something. King minus man plus woman lands near queen. Paris minus France plus Italy, near Rome. Though the map also soaks up the biases in human writing.

ALICE: Four: models don't read words. They read tokens, which are words or pieces of words. Common words stay whole, rare ones get split. In English, a token is about three quarters of a word. And the model's very first step is to look up each token's embedding.

FRANK: And five: that's why everything in AI is counted in tokens: prices, memory, training data. It's why other languages can cost more, and why chatbots struggled to count the R's in "strawberry". They don't see the letters.

ALICE: Which leaves "bank". The word map gives every word one meaning, no matter the sentence. To fix that, a network has to read the sentence, in order. So how do you build a network that reads?

FRANK: That's next time. Networks that read one word at a time, why they kept forgetting, and how attention was invented to help them translate.

ALICE: See you then.
