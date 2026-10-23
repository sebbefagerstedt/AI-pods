# Episode 10: Inside the transformer, layer by layer

## Cold open

ALICE: Frank, have you ever tried to translate German as you hear it? Word by word, live?

FRANK: I have not. Why?

ALICE: Because it's a trap. Here's a sentence, in German word order, but in English words. "I have yesterday evening with my sister in the park a very long book..."

FRANK: A very long book what?

ALICE: "...read." The verb comes at the very end. In German, "I have read" gets split in two, and the important half waits until the sentence is over. Mark Twain complained about this. He said that when a German dives into a sentence, you won't see him again until he comes up on the other side, with his verb in his mouth.

FRANK: Okay, that's good. So if you're translating into English, you need "read" right near the start, but it hasn't arrived yet.

ALICE: Exactly. So a good translator doesn't start writing at the first word. They take in the whole sentence first. Then they write the English, one word at a time, glancing back at the original as they go.

FRANK: Read everything first, then write.

ALICE: Read everything first, then write. And hold on to that. Because that one habit explains why the transformer, the design behind every chatbot, was first built as two towers. And why ChatGPT throws one of them away.

## Welcome

FRANK: Welcome to From Zero to ChatGPT. I'm Frank.

ALICE: And I'm Alice.

FRANK: And today we're opening up the machine. We've talked about the transformer before, and about GPT, which is built from it. But we kept a lot of it as a black box. Today we take the lid off. Three things. One: the two halves of the original transformer, the encoder and the decoder, and why it had both. Two: why GPT kept only one of them. And three: we'll follow a single word all the way up through the layers, to the very top. To the output layer.

ALICE: Which is the one I keep hearing people mention. "The final layer." "The output layer." And I've always sort of nodded along.

FRANK: Then by the end, you'll know exactly what it does. And, maybe more interesting, what it doesn't do.

ALICE: And for anyone jumping in here?

FRANK: Two quick reminders. First, models don't see words, they see tokens, which are words or pieces of words. And each token gets turned into a long list of numbers that captures, roughly, what it means. That's the embedding. Second, the transformer's big trick is attention: it takes in the whole passage at once, and every word can look at every other word to work out what it means.

ALICE: Tokens, numbers, attention. Got it.

FRANK: And the transformer came from the 2017 paper "Attention Is All You Need". If you've seen the famous diagram from that paper, keep it in your head today. Two towers, side by side. We'll keep coming back to it.

## Two towers

FRANK: So, Alice, here's the first question. What was the transformer actually built for?

ALICE: Translation, right?

FRANK: Translation. The paper's big results were English to German and English to French. And translation has a particular shape. There's an input, the sentence you've got, and an output, the sentence you want. In a different language, often a different length, with the words in a different order.

ALICE: Like the verb at the end.

FRANK: Like the verb at the end. So the people who built translation systems had settled on a design with two parts, years before the transformer. One part reads. The other part writes. And the transformer kept that shape. The left tower is the encoder. That's the reader.

ALICE: And what does the reader do, exactly?

FRANK: It takes in the whole source sentence at once. All of it. And every word can look at every other word, in both directions. Forward and back. So by the time it's done, the word "have" knows that "read" is coming at the end. Every word has been reworked in light of the whole sentence.

ALICE: And then it writes the translation?

FRANK: No. And this surprised me. The encoder never writes a single word. What it produces is a set of notes. One rich list of numbers per word, describing what that word means here, in this sentence. Its understanding of the sentence, if you like.

ALICE: So who writes?

FRANK: The right tower. The decoder. It writes the translation one word at a time. And it has the rule we've mentioned before: when it's writing word five, it can only look back at words one to four. No peeking ahead.

ALICE: Because ahead hasn't been written yet.

FRANK: Right. In real use, it hasn't. And in training, where the right answer is sitting right there, the rule stops it from cheating by copying.

ALICE: Okay. But then how does the decoder know what it's translating? If it only looks at its own words so far...

FRANK: That's the bridge between the towers. In the decoder, there's an extra step. After it looks back at the words it's written so far, it looks across at the encoder's notes. Every time it writes a word, it asks: which parts of the original matter right now? It's called cross-attention. Attention, but across from one tower to the other.

ALICE: So that's the translator glancing back at the original.

FRANK: That's exactly it. When it's about to write "read", it looks across, finds that verb waiting at the end of the German sentence, and pulls it forward.

ALICE: Okay, but why two separate towers? Couldn't one network do both jobs?

FRANK: Good question, and the honest answer is partly history. Translation networks had been built this way since about 2014, with the older networks, the ones that read one word at a time. Attention itself was invented to be that bridge. So when the transformer came along, it kept the shape everyone was already using, and swapped out what was inside.

ALICE: Partly history. What's the other part?

FRANK: The other part is that it fits the job. In translation, the input is complete before you start. You've got the whole German sentence. So why not let the reader look both ways? It would be silly not to. But the output doesn't exist yet. So it has to be written left to right. Two different jobs, two different rules. Reading gets to look everywhere. Writing only looks back.

ALICE: Two jobs, two rules. That's actually tidy.

FRANK: And it worked. The bigger model in the paper beat the best translation systems of the day, and it trained in three and a half days, on eight graphics cards. The smaller one in about twelve hours.

ALICE: So that's the 2017 transformer. A reader, a writer, and a bridge between them.

FRANK: That's it. And Alice, the next part's yours. Because a year later, OpenAI took that design and threw half of it away.

## Why GPT kept only the decoder

ALICE: They did. GPT is decoder only. The writer, without the reader. And the first time I heard that, I thought, isn't that throwing away the understanding part?

FRANK: That's what I'd think, yes.

ALICE: But think about what GPT is trained on. Raw text. Novels, web pages. And what's it trying to do?

FRANK: Guess the next word.

ALICE: Guess the next word. So where's the input sentence? Where's the original?

FRANK: Huh. There isn't one. It's just the text so far.

ALICE: There isn't one. In translation, you have two things, the German and the English. Here, you have one stream of text, and the job is to continue it. The "input" is just the beginning of the same text. So the encoder would have nothing of its own to read, and the bridge would have nothing to look across at.

FRANK: So the reader has no job.

ALICE: The reader has no job. In 2018, a Google team writing Wikipedia articles from sources had already tried this. They glued the sources and the article together into one long stream and dropped the encoder altogether. And it worked well. GPT-1 built on that.

FRANK: Okay, but then who does the reading? When I type a question into ChatGPT, something has to understand my question.

ALICE: The same decoder does it. Your question is just the start of the text. The model reads it with the same layers it writes with, every word looking back at the words before it. And then it keeps going, one word at a time, and its answer becomes part of the same stream.

FRANK: But only looking back. Not both ways, like the encoder.

ALICE: Only back. That's the price. Remember "the bank was steep and muddy", from the Bert story? When the model gets to "bank", it doesn't know about the mud yet. But later words can look back at "bank" and sort it out. With enough layers, that turns out to be good enough.

FRANK: Okay. So that's why GPT could drop the encoder. But why would it want to? What does it gain?

ALICE: A few things. First, simplicity. One tower instead of two, and no bridge. And here's a fun detail. Once you take away the bridge, a decoder layer and an encoder layer are almost the same thing. The only real difference left is the no-peeking rule.

FRANK: Wait, really? The two towers are basically twins?

ALICE: Basically twins. The reader is a writer that's allowed to peek. Second, every word is practice. In translation, the model only gets graded on the words it writes, the English half. In GPT, every single word of the text is a guess with an answer key. A page of text is hundreds of little exercises, all checked at once.

FRANK: Because every word predicts the next one, at the same time.

ALICE: All at once, in one pass. That's where the parallel training pays off. And third, and this is the big one: any task can be written as text to continue. Translation? Write "English: the cat is on the mat. German:" and let it continue. A question? Write the question, and let it continue with the answer.

FRANK: So one model, one rule, every task.

ALICE: One model, one rule. And it scaled. Every big chatbot you've heard of today is built this way. Decoder only.

FRANK: And Bert, from Google, went the other way, right? Kept only the encoder.

ALICE: Right. Bert is the reader without the writer. Every word sees the whole sentence, both ways, which makes it a brilliant reader. But since it can always see everything, it was never trained to continue text. So it can't really write.

FRANK: So, GPT, the writer. Bert, the reader. Is the full two-tower design dead, then?

ALICE: Not at all, and this is worth saying. In 2019, Google built a model called T5 that kept both towers, and in their comparisons the two-tower version did really well. And here's one you'll like. This podcast is checked by a speech recognizer called Whisper. It listens to every episode and writes down what it hears, so we can check that every line is there. And Whisper has both towers.

FRANK: Huh. Why?

ALICE: Because its job is shaped like translation. The input is complete, the audio. The encoder listens to all of it, both ways. And the decoder writes down the words, one at a time, glancing back at the sound. Two jobs, two rules.

FRANK: So the decoder-only design didn't win because it's better at everything.

ALICE: No. It won because it's simple, it learns from every word, it handles any task as text, and when people made it bigger and bigger, it just kept getting better. Frank, you said we'd follow a word up the tower.

FRANK: I did. Let's climb.

## One word, all the way up

FRANK: Okay. Let's take a sentence. "The trophy didn't fit in the suitcase, because it was too big." And let's follow one word: "it".

ALICE: "It", the trophy, or "it", the suitcase?

FRANK: You knew right away, didn't you? The trophy. Because if the suitcase were too big, the trophy would fit. The question is how the model figures that out. So, bottom floor. "It" comes in as a token, and gets swapped for its embedding, its list of numbers. In GPT-1, that's seven hundred and sixty-eight numbers. In GPT-3, over twelve thousand.

ALICE: And that list is, roughly, what "it" means.

FRANK: What "it" means in general. Plus a little stamp that says where it sits in the sentence. But at this point, it's just the dictionary entry. It knows nothing about trophies. Now, here's the picture I find most helpful. Think of that list of numbers as a notepad. Each word has its own notepad. And as it goes up through the layers, every layer reads the notepad, and adds a note.

ALICE: Adds. Not rewrites?

FRANK: Adds. That's important. Each layer works out something, and adds it on top of what's already there. Nothing gets thrown away. Researchers call this running notepad the residual stream. And if you remember the diagram, those little boxes in every layer that say "Add and Norm"? The "add" is literally that. Adding the layer's note to the notepad.

ALICE: Oh. I always wondered about those boxes.

FRANK: So now we go up one layer. And every layer has two halves. The first half is attention. This is where words compare notes. "It" looks back at the words before it, and asks: which of you matter to me? And it can pull in information from them.

ALICE: So "it" looks at "trophy" and "suitcase".

FRANK: It can. Though in a low layer, it probably doesn't know enough yet to pick the right one. And remember, there are several attention heads, each looking for something different. One might track grammar, another which noun a word points back to, another what's nearby. Each head adds what it found to the notepad.

ALICE: Okay. And the second half?

FRANK: The second half is the feed-forward part. And here, each word works on its own. No looking at the others. It takes what's on its notepad, including everything it just gathered, and thinks it over.

ALICE: "Thinks it over" is doing a lot of work there.

FRANK: Fair. Here's a more concrete way to put it. In 2020, researchers at Tel Aviv University looked inside these feed-forward parts, and found they work a lot like a memory. Each one holds thousands of little detectors. Each detector watches for a pattern on the notepad. And when its pattern shows up, it adds its own note. Something like: "when you see this kind of thing, words like these tend to come next."

ALICE: So it's a bit like... recognizing something, and remembering what usually goes with it.

FRANK: That's a good way to say it. And that seems to be where a lot of what the model knows is kept. Facts, even. In 2022, a team from MIT and Northeastern University tracked down where a model stored facts like which city a landmark is in. They found it mostly in the feed-forward parts of the middle layers. And they could change a fact by editing a small set of knobs in one layer. They moved the Space Needle, the tower in Seattle, to Paris.

ALICE: In the model's head.

FRANK: In the model's head. Ask it where the Space Needle is, and it would say Paris. So: attention, words compare notes. Feed-forward, each word thinks on its own, and looks things up. That's one layer.

ALICE: And then?

FRANK: And then you do it again. And again. GPT-1 has twelve of these layers. GPT-3 has ninety-six. Same two halves every time, but each layer has its own knobs, so each one learns to do something different.

ALICE: Different how? Do we know what each layer does?

FRANK: Roughly. In 2019, a Google team looked inside Bert, layer by layer. They tested what each layer's notepads could tell you. What they found is that the simple things show up low down. What kind of word is this, a noun or a verb. Then, a bit higher, how the words in a sentence fit together. And the hardest things show up highest, like who did what to whom, and which word "it" refers to.

ALICE: So, grammar at the bottom, meaning further up.

FRANK: Roughly. It's not a strict assembly line, and it's messier in real models. But that's the picture. So back to our "it". Somewhere in the middle layers, "it" looks back again. By now, "trophy" and "suitcase" have notes of their own, and "big" has done some work too. And "it" settles on the trophy, and adds that to its notepad.

ALICE: Okay, so we've climbed all the way up. Ninety-six layers. Now what? What comes out of the top?

FRANK: Now we're at the top floor. The output layer. And Alice, that one's yours.

## The output layer

ALICE: It is. So, here's the setup. We've climbed the tower, and every word has a notepad covered in notes. But the model has one job: guess the next word. So which notepad does it use?

FRANK: The last word's? Whatever word is at the end of the text so far?

ALICE: The last word's. That notepad, after all those layers, holds the model's whole idea of what should come next. But it's still just a long list of numbers. Twelve thousand of them, in GPT-3. That's not a word. So the output layer's job is to translate it back into a word. Or rather, into a bet on every word.

FRANK: How?

ALICE: Picture a police sketch artist. You've got a sketch of the suspect. And on the wall, there's a gallery of photos. Everyone the police know. You hold the sketch up to each photo, and give it a score. How much does it look like this one? And this one?

FRANK: So the sketch is the notepad.

ALICE: The sketch is the notepad. And the gallery is every token the model knows. About forty thousand in GPT-1, around fifty thousand in GPT-3. Each one has its own list of numbers. And the output layer compares the notepad with every single one, and gives each a score.

FRANK: Forty thousand comparisons. For every word it writes.

ALICE: For every word. Computers are good at that. Then a last step turns the scores into probabilities. The high scores get most of the chance, the low ones get almost nothing, and it all adds up to a hundred percent. That's the spread of bets we talked about. "Mat", forty percent. "Floor", twenty. And so on. In the paper's diagram, that's the two boxes at the very top of the right tower. "Linear", that's the scoring. And "softmax", that's turning scores into probabilities.

FRANK: Okay, so where does the gallery come from? The photos of every token?

ALICE: And this is my favorite bit. Often, it's the same table as at the very bottom. The embeddings. The list of numbers each token gets when it comes in. The model uses that same table at the top, backwards. At the bottom, it goes from a word to its numbers. At the top, it goes from numbers to: which word does this look most like?

FRANK: The dictionary, read in reverse.

ALICE: The dictionary, read in reverse. The original transformer did this, and so did GPT-1. It's in "Attention Is All You Need", actually. One sentence that's easy to miss: the same table is shared between the embeddings and the layer before the softmax.

FRANK: Okay. But here's what I'd always assumed, and I think a lot of people do. That the output layer is where the model decides what the answer looks like. The style. The format. Whether it writes a list or a poem.

ALICE: And that's the thing I wanted to clear up. It doesn't. The output layer is the same simple scoring every time. It doesn't think. It doesn't plan. It doesn't know it's writing a poem. Everything that makes the answer a poem, the rhythm, the topic, the next rhyme, has already been worked out by the layers below, and written on the notepad. The output layer just reads off the answer.

FRANK: So it's the announcer, not the judge.

ALICE: It's the announcer, not the judge. The judging happened on the way up. And here's how we know. In 2020, a blogger had a neat idea. If the output layer can read a guess off the top notepad... why not hold it up to a notepad halfway up? Ask the model, in the middle of its thinking: if you had to answer right now, what would you say?

FRANK: Oh, that's clever. And?

ALICE: In the early layers, the guesses are rough. Often way off. Then, somewhere in the middle, the right answer starts to show up, and the last layers mostly sharpen it. It got nicknamed the logit lens. "Logit" is the jargon for those raw scores before they become probabilities.

FRANK: So you can watch the answer take shape as it climbs.

ALICE: You can watch it take shape. And this is the main idea of the episode, really. People say "the final layer" as if that's where the magic is. The magic is in the climb. The top is where the answer gets read out.

FRANK: And how does this connect to the GPT-1 story? There was a little piece on top there, too, for fine-tuning.

ALICE: Good catch. Same spot, different job. For fine-tuning, GPT-1 put a small extra output layer on top, and instead of scoring forty thousand words, it scored just a few answers. Positive or negative. Follows, or contradicts. Same top notepad, different gallery.

FRANK: Huh. So you can swap the announcer for a different job, and the climb stays the same.

ALICE: Exactly. And one more thing. When the model is writing, only the last word's notepad gets used to pick the next word. But in training, every word's notepad gets read out at once, and each one is graded against the word that actually came next. That's the "every word is practice" from earlier.

FRANK: Okay. So we end up with a spread of bets over every possible next word. Then what? How does it actually pick one?

ALICE: That's the next step, and it's a whole story of its own. We'll do it next time.

## Recap

FRANK: Okay, let's wrap up. Alice, you start.

ALICE: Sure. One: the original transformer was built for translation, so it had two towers. The encoder reads the whole input at once, every word looking both ways, and writes nothing, only notes. The decoder writes the output one word at a time, with no peeking ahead, and keeps glancing across at the encoder's notes. That glance is cross-attention.

FRANK: Two: GPT kept only the decoder. In raw text, there's no separate input, just one stream to continue, so the encoder had nothing to do. One tower is simpler, every word becomes practice, and any task can be written as text to continue. Bert kept only the encoder, the reader, which is why it can't really write. And both towers live on in models like Whisper.

ALICE: Three: inside, each word gets a notepad, the residual stream. Every layer reads it and adds a note. And every layer has two halves: attention, where words compare notes, and the feed-forward part, where each word thinks on its own and looks things up. That's where a lot of facts seem to live.

FRANK: Four: stack those layers. Twelve in GPT-1, ninety-six in GPT-3. Roughly, grammar shows up lower down, meaning further up.

ALICE: And five: the output layer. It holds the last word's notepad up against every token the model knows, often using the same table as the embeddings, backwards, and turns the scores into a probability for every possible next word. It doesn't decide what the answer looks like. It reads off what the layers below already worked out.

FRANK: Which leaves us with a spread of bets. "Mat", forty percent. "Floor", twenty. So, when you type a question into ChatGPT and press Enter, how does it go from bets to an actual answer?

ALICE: That's next time. How a word guesser picks its words, what "temperature" means, and why it sometimes makes things up with total confidence.

FRANK: See you then.
