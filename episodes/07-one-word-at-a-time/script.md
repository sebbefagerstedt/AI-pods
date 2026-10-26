# Episode 7: Reading one word at a time

## Cold open

FRANK: Okay, picture this. November 2016, Tokyo. A computer science professor named Jun Rekimoto keeps seeing posts online saying something odd. Google Translate, which everybody knew was a bit clumsy, suddenly isn't.

ALICE: Suddenly? Like, overnight?

FRANK: Overnight. So he tries a test. He takes the opening lines of a Hemingway short story, "The Snows of Kilimanjaro", in Japanese. And he asks Google to translate them back into English, to see how close it gets to what Hemingway actually wrote.

ALICE: Oh, that's a clever test.

FRANK: The old Google Translate had given him something like: "Kilimanjaro is nineteen thousand seven hundred and ten feet of the mountain covered with snow, and it is said that the highest mountain in Africa."

ALICE: I mean, I get the gist.

FRANK: You get the gist. Now the new one: "Kilimanjaro is a mountain of nineteen thousand seven hundred and ten feet covered with snow, and is said to be the highest mountain in Africa."

ALICE: Okay, that's just English. That's a real sentence.

FRANK: It's a real sentence. Very close to Hemingway's. And Rekimoto wrote about it, and it spread. Because what had happened was that Google had quietly swapped out the whole system. The old one stitched together phrases from a giant table, chunk by chunk. The new one was a neural network. It read the sentence, one word at a time, and then wrote the translation, one word at a time. And it had a trick, called attention.

ALICE: Attention. As in "Attention Is All You Need"?

FRANK: That's where the word comes from. And today, we're going to see what was inside that translator. Networks that read one word at a time. Why they kept forgetting. And how attention was invented to fix it.

## Welcome

ALICE: Welcome to From Zero to ChatGPT. I'm Alice.

FRANK: And I'm Frank.

ALICE: So, last time, we turned words into numbers. Every token, a word or a piece of a word, gets a list of numbers, its embedding. Like a spot on a map, where similar words sit close together.

FRANK: King minus man plus woman.

ALICE: Exactly. But we ended on a problem. Every word gets one spot on the map, no matter what sentence it's in. "Bank" is the same list of numbers, whether it's a river bank or a money bank. To know which one, you have to read the sentence.

FRANK: So today, we teach a network to read.

ALICE: To read. And there's a deeper problem, too, which I'll take first. Why reading in order matters at all.

## Why order matters

ALICE: So, here's a quick one. "Dog bites man."

FRANK: Not news.

ALICE: Not news. "Man bites dog."

FRANK: News.

ALICE: Same three words. Same three spots on our word map. Completely different meaning. So if you just took a sentence and threw all the word embeddings into a pile, you'd lose the most important thing. Who did what to whom.

FRANK: A bag of words.

ALICE: That's literally what it's called. A bag of words. And for some jobs, a bag of words is fine. If you're sorting emails into spam, the words "free money" are a giveaway in any order. But for real understanding, order matters. "Not bad, actually good" and "not good, actually bad" have the same words.

FRANK: Okay. So why not just feed the words to the network in their slots? Word one goes into slot one, word two into slot two.

ALICE: Because sentences come in every length. A network from part one has a fixed number of inputs. Say you build it for twenty words. What happens with a sentence of five words? Or fifty? And worse, the word "dog" in slot two and "dog" in slot seven would go through completely different knobs. The network would have to learn what "dog" means separately for every position.

FRANK: So we need something that can take any length, and treats a word the same wherever it shows up.

ALICE: That's the requirement. And the answer people came up with is to do what you're doing right now, listening to me. Take the words one at a time, in order, and keep a running idea of what's been said so far. Frank, that's yours.

## A network with a memory

FRANK: It is. And the idea is really pretty simple. Imagine you're reading a book, but with a strange rule. You can only look at one word at a time. And you're allowed one sticky note.

ALICE: One sticky note.

FRANK: One sticky note. And after each word, you rewrite the note. You look at the new word, you look at what's on your note, and you write a new note that combines them. "So far: a man, he's been bitten." Then the next word comes along, and you update it again.

ALICE: So the sticky note is your memory of the sentence so far.

FRANK: That's it. And a network that works this way is called a recurrent neural network. An RNN. Recurrent, because it does the same thing again and again. At every word, the same little network takes two things in: the new word's embedding, and the old sticky note. And it puts out a new sticky note.

ALICE: And the sticky note is...

FRANK: A list of numbers, like everything else. A few hundred numbers that are supposed to capture the gist of everything so far. And here's the nice part. It's the same knobs at every step. So "dog" gets processed the same way whether it's the second word or the seventh. And the sentence can be any length. You just keep going until you run out of words.

ALICE: Okay, that solves both problems. And what can you do with the sticky note?

FRANK: All kinds of things. At the end of a review, read the note and decide: positive or negative. Or, after every word, use the note to guess the next word.

ALICE: The next word. That sounds familiar.

FRANK: It should. Predicting the next word with these networks was already a thing around 2010. In fact, one of the people who did it well was Tomas Mikolov, the word2vec guy, from last time. RNNs were also used for handwriting and for speech, anything that comes in a sequence.

ALICE: So who came up with it?

FRANK: The idea goes back to the eighties. One well-known early paper was from 1990, by a linguist named Jeffrey Elman, called "Finding Structure in Time". He trained a small RNN on simple sentences, and found that its sticky notes had sorted the words into nouns and verbs, on its own.

ALICE: Nobody told it. Again.

FRANK: Nobody told it. So that's the RNN: read a word, update the note, repeat. It sounds perfect.

ALICE: I'm guessing it isn't.

FRANK: It isn't. And Alice, you get to break it.

## Why it forgot

ALICE: I do. So, here's a sentence. "The keys to the old cabinet in the hallway next to the stairs that my grandmother painted blue..." Now, Frank: "is" or "are"?

FRANK: "Are". The keys are.

ALICE: The keys are. But by the time the RNN gets to that word, "keys" was fifteen words ago. And the sticky note has been rewritten fifteen times since. Cabinet, hallway, stairs, grandmother, blue. Each new word crowds out a bit of the old stuff. So whatever it wrote about "keys" has been smudged and overwritten.

FRANK: So the start of the sentence fades.

ALICE: Fades fast. Think about a game of telephone. The first person whispers a message, and by the fifteenth person, it's mush. In an RNN, the sticky note is the whisper, passed from word to word.

FRANK: Okay, but couldn't training fix that? If it keeps getting "keys are" wrong, the loss goes up, and it learns to hold on to the subject.

ALICE: That's the second, sneakier half of the problem. And it's something we've seen before. Remember passing the blame backward, from a couple of episodes ago? The salty dish, with the blame flowing back through the kitchen?

FRANK: And it faded, if there were too many stations.

ALICE: Exactly. In an RNN, every word is like another station. So when the model gets "are" wrong, the blame has to travel back through fifteen updates of the sticky note, to reach the moment it read "keys". And at every step, it shrinks. By the time it gets there, there's almost nothing left.

FRANK: So the network never finds out that it should have remembered "keys".

ALICE: Never finds out. It's the vanishing gradient problem again, just stretched out over time instead of over layers. A German student named Sepp Hochreiter worked this out in 1991, in his student thesis. And it meant that plain RNNs were good at short-range things, the last few words, and really bad at long-range ones.

FRANK: And language is full of long-range things.

ALICE: Full of them. Who "she" refers to, three sentences later. Whether a question was asked at the start. The plot of a story. So, Frank, Hochreiter worked out the problem. Did he fix it?

FRANK: He did, with his advisor. And that's mine.

## Long short-term memory

FRANK: So in 1997, Sepp Hochreiter and Jürgen Schmidhuber published a new kind of RNN. And it has the best and most confusing name in AI. Long short-term memory.

ALICE: Long short-term memory. That's like saying a tall short person.

FRANK: It is a bit. The idea is: a short-term memory that lasts a long time. Everyone just calls it an LSTM. And here's what they changed. In the plain RNN, the sticky note gets completely rewritten at every word. Mixed up with the new word, every single time. The LSTM adds a second, separate memory that doesn't get rewritten. Think of it as a notebook that rides alongside.

ALICE: A notebook, instead of a sticky note.

FRANK: And the notebook has three little valves. Gates. At every word, the network decides three things. First: should I erase anything from my notebook? That's the forget gate. Second: is there anything in this new word worth writing down? That's the input gate. And third: what part of my notebook do I need right now, to make my guess? That's the output gate.

ALICE: So, keys comes along...

FRANK: Keys comes along, and the input gate says, write this down: plural subject. Then cabinet, hallway, stairs, grandmother come along, and the gates say: interesting, but don't erase the subject. Keep it. And when we finally need the verb, the output gate pulls "plural subject" back out of the notebook.

ALICE: Keys are.

FRANK: Keys are. And the key thing for training: if the gates leave the notebook alone, the information rides along unchanged. Like a conveyor belt. So the blame can ride back along the same belt, without shrinking at every step. The network can actually learn that it should have remembered "keys".

ALICE: Okay. Who decides when the gates open?

FRANK: The network does, and it's learned like everything else. The gates have their own knobs, nudged by walking downhill. Nobody programs "remember subjects". It works out what's worth keeping.

ALICE: And did it work?

FRANK: It worked. Slowly, at first. It took years, and more computing power, for LSTMs to take off. But by the mid twenty-tens, they were everywhere. The speech recognition on your phone. Predicting the next word as you type. And translation.

ALICE: So the LSTM is the network that reads one word at a time, and mostly remembers.

FRANK: Mostly. Better than the plain RNN, by a lot. But it still forgets over long stretches. A notebook is still only so big. And it still has to read one word at a time, which will matter a lot later. Alice, you've got translation.

## Translation, and attention

ALICE: I do. So, 2014. A team at Google: Ilya Sutskever, who we met building AlexNet, with two colleagues. They wanted to use LSTMs for translation. And they came up with a design that's beautifully simple. Two LSTMs. The first one reads the English sentence, one word at a time. And at the end, its notebook holds the gist of the whole sentence.

FRANK: And then?

ALICE: Then it hands that notebook to the second LSTM, which writes the French, one word at a time. The first one is called the encoder, because it turns the sentence into numbers. The second is the decoder, because it turns the numbers back into words.

FRANK: An encoder and a decoder.

ALICE: Remember those two words. They're going to be with us for the rest of the series. And it worked surprisingly well. With one funny detail. They found that it worked better if they fed the English sentence in backwards.

FRANK: Backwards? Why?

ALICE: Because then the first English words are the last ones the encoder read. So they're freshest in its notebook, right when the decoder needs to write the first French words. Which tells you something: the forgetting was still a real problem.

FRANK: And the bigger problem, I'm guessing, is long sentences.

ALICE: That's the big one. Think about what we're asking. The entire meaning of the sentence, however long, has to be squeezed into one notebook. A fixed list of numbers. For a short sentence, fine. For a forty-word sentence, there's just not enough room. And researchers measured it: as sentences got longer, the translations fell apart.

FRANK: So it's like translating a whole paragraph after reading it once, without being allowed to look back.

ALICE: That's exactly it. And no human translator works that way. A human translator writes, and as they go, they glance back at the original. "Where was I? Which word am I translating right now?"

FRANK: And that's attention.

ALICE: That's attention. The same year, 2014, a team in Montreal, with Yoshua Bengio, who you've heard of, proposed a fix. Don't throw away the encoder's work word by word. Keep a note for every word in the original sentence. And then, every time the decoder is about to write a word, it gets to look back at all those notes, and decide which ones matter right now.

FRANK: Decide how?

ALICE: It gives each note in the original a score. How relevant is this word, for what I'm about to write? High score, it pays a lot of attention. Low score, almost none. Then it blends the notes, weighted by those scores, and uses that to pick its next word.

FRANK: And the scoring is learned too?

ALICE: Learned too. Nobody tells it which words line up. And here's my favorite part of that paper. They drew pictures of the scores. Which English word the network paid attention to, for each French word it wrote. And you could see it learning how the two languages line up. Their example: "the European Economic Area". In French, the words go the other way round. "La zone économique européenne." Area, economic, European.

FRANK: And the attention flipped too?

ALICE: The attention flipped. When it wrote "zone", it looked at "area". When it wrote "européenne", it looked back at "European". It worked out that French puts things in a different order. On its own.

FRANK: That's lovely. And did it fix long sentences?

ALICE: It did. The translations stopped falling apart as sentences got longer, because nothing had to be squeezed into one notebook anymore. And attention spread fast. That Google Translate switch in 2016, the one that impressed Rekimoto? Big LSTMs, an encoder and a decoder, with attention as the bridge between them. Google said it cut translation errors by more than half on some major language pairs.

FRANK: Okay, so that's where we've got to. LSTMs read the sentence one word at a time, with a notebook. And attention lets the writer look back at every word.

ALICE: And here's the thing that bugged some researchers at Google. Attention was the part doing the clever work. It found the important words, wherever they were, in one step. Meanwhile, the LSTM was still trudging through the sentence one word at a time, forgetting as it went.

FRANK: So what if you dropped the trudging?

ALICE: What if you kept only the attention? Let every word look at every other word directly. No sticky notes, no notebook, no reading in order.

FRANK: Attention is all you need.

ALICE: That's the next episode.

## Recap

FRANK: Okay, let's wrap up. Alice, you start.

ALICE: Sure. One: word order matters. "Dog bites man" isn't "man bites dog". And sentences come in every length, so a network needs a way to read any sentence, in order.

FRANK: Two: a recurrent neural network, an RNN, reads one word at a time, and keeps a running sticky note of what it's read so far. Same knobs at every step, any length of sentence.

ALICE: Three: RNNs forget. The note gets rewritten at every word, and in training, the blame fades as it travels back through the words. So they struggle to connect things that are far apart, like "the keys" and "are".

FRANK: Four: the LSTM, from 1997, adds a separate notebook with three gates: what to forget, what to write down, and what to read out. Information, and blame, can ride along unchanged, so it remembers much longer. LSTMs ran speech recognition, typing prediction and translation in the twenty-tens.

ALICE: And five: for translation, an encoder reads the sentence and a decoder writes the translation. Squeezing a whole sentence into one notebook failed on long sentences. So in 2014, attention let the decoder look back at every word of the original and pick what matters right now. Like a translator glancing back.

FRANK: Which sets up one of the most famous titles in computer science. If attention does the clever part, why keep the slow, forgetful reading at all?

ALICE: That's next time. "Attention Is All You Need", explained. Self-attention, queries, keys and values, and why it was built to train fast.

FRANK: See you then.
