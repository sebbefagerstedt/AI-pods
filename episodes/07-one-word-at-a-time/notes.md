# Episode 7: Reading one word at a time

From Zero to ChatGPT, season 1, episode 7. About 17 minutes, with Frank and Alice. Part 2, "Teaching computers language".

How networks learned to read sentences in order. Why word order and sentence length are a problem for an ordinary network; recurrent networks that read one word at a time and keep a running sticky note; why they forgot, and how the LSTM's gated notebook helped; and the 2014 translation networks, an encoder and a decoder, that led to attention: letting the writer glance back at every word of the original. Framed by the night Google Translate suddenly got good, in 2016.

## Key terms

- **Bag of words:** treating a text as an unordered pile of words. Fine for some jobs (spam), useless for "dog bites man" versus "man bites dog".
- **Recurrent neural network (RNN):** reads a sequence one item at a time, combining each new word with its *hidden state* (the "sticky note", a list of numbers summing up what it has read) to produce a new hidden state. The same weights are used at every step, so it handles any length.
- **RNN language model:** an RNN that predicts the next word from its hidden state. Tomas Mikolov's 2010 RNN language model was a strong early one.
- **Vanishing gradient (over time):** in training, the blame for a mistake shrinks as it travels back through each step, so plain RNNs barely learn links between words far apart. Analyzed by Sepp Hochreiter (1991) and by Bengio, Simard and Frasconi (1994).
- **LSTM (long short-term memory):** Hochreiter and Schmidhuber's 1997 RNN with a separate *cell state* (the "notebook") controlled by learned gates: the *forget gate* (what to erase, added by Gers, Schmidhuber and Cummins in 2000), the *input gate* (what to write) and the *output gate* (what to read out). Information, and blame, can pass along the cell state largely unchanged, so it learns longer-range links. A simpler cousin, the GRU, came in 2014.
- **Encoder-decoder (sequence to sequence):** one network reads the input into a summary (the encoder), another writes the output from it (the decoder). Sutskever, Vinyals and Le (2014) used two deep LSTMs and found reversing the input sentence helped; Cho and others (2014) proposed the same idea with GRUs.
- **Bottleneck:** squeezing a whole sentence into one fixed-size vector; translations got worse as sentences got longer.
- **Attention:** Bahdanau, Cho and Bengio (2014). The encoder keeps a vector for every input word; at each output step the decoder scores every input word for relevance, turns the scores into weights that add up to 100%, and uses the weighted blend. The weights are learned. Their Figure 3 shows "European Economic Area" aligned with the reversed French "zone économique européenne".
- **GNMT:** Google's Neural Machine Translation system, launched in Google Translate in 2016: deep LSTM encoder and decoder (8 layers each) with attention. Google reported it cut translation errors by about 60% on average against the old phrase-based system in human evaluations.

## The Kilimanjaro test

Jun Rekimoto, a professor at the University of Tokyo, took the opening of Hemingway's "The Snows of Kilimanjaro" in Japanese and ran it back into English. Hemingway: "Kilimanjaro is a snow-covered mountain 19,710 feet high, and is said to be the highest mountain in Africa." The old Google Translate: "Kilimanjaro is 19,710 feet of the mountain covered with snow, and it is said that the highest mountain in Africa." The new one: "Kilimanjaro is a mountain of 19,710 feet covered with snow and is said to be the highest mountain in Africa." Retold in Gideon Lewis-Kraus, [The Great A.I. Awakening](https://www.nytimes.com/2016/12/14/magazine/the-great-ai-awakening.html), *The New York Times Magazine*, December 2016.

## Papers and sources

- Jeffrey Elman (1990), [Finding Structure in Time](https://doi.org/10.1207/s15516709cog1402_1), *Cognitive Science*. A small RNN that sorted words into nouns and verbs on its own.
- Yoshua Bengio, Patrice Simard and Paolo Frasconi (1994), [Learning long-term dependencies with gradient descent is difficult](https://doi.org/10.1109/72.279181), *IEEE Transactions on Neural Networks*.
- Sepp Hochreiter and Jürgen Schmidhuber (1997), [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735), *Neural Computation*.
- Felix Gers, Jürgen Schmidhuber and Fred Cummins (2000), [Learning to Forget: Continual Prediction with LSTM](https://doi.org/10.1162/089976600300015015), *Neural Computation*. The forget gate.
- Kyunghyun Cho and others (2014), [Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation](https://arxiv.org/abs/1406.1078).
- Ilya Sutskever, Oriol Vinyals and Quoc Le (2014), [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215).
- Dzmitry Bahdanau, Kyunghyun Cho and Yoshua Bengio (2014), [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473). Attention.
- Yonghui Wu and others (2016), [Google's Neural Machine Translation System: Bridging the Gap between Human and Machine Translation](https://arxiv.org/abs/1609.08144).
- Christopher Olah (2015), [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/). The classic illustrated explanation, if you want the diagrams.

Next: episode 8, "Attention Is All You Need, explained".
