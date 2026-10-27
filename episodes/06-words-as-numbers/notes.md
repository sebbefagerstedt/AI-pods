# Episode 6: Words as numbers

From Zero to ChatGPT, season 1, episode 6. About 18 minutes, with Frank and Alice. The first episode of part 2, "Teaching computers language".

How to turn words into numbers a network can use. Why numbering words, or giving each its own switch, doesn't work; how word embeddings place every word on a map of meaning, learned from the company words keep; the famous "king − man + woman ≈ queen" from word2vec, with its catches; and tokens, the word pieces language models actually read, and why everything in AI is counted in them.

## Key terms

- **Distributional hypothesis:** words that appear in similar contexts tend to have similar meanings. J. R. Firth (1957): "You shall know a word by the company it keeps." The *tesgüino* example (a corn beer of the Rarámuri people in northern Mexico) goes back to the linguist Eugene Nida and appears in Dekang Lin's 1998 work and in Jurafsky and Martin's textbook.
- **One-hot encoding:** a row of switches, one per word in the vocabulary, with only that word's switch on. Honest, but every word is equally different from every other.
- **Vector:** a list of numbers, which you can think of as a position in space.
- **Word embedding:** a word's vector, placed so that words with similar meanings are close together. Learned from raw text.
- **word2vec:** Tomas Mikolov and colleagues at Google, 2013. A small network trained to predict the words around a word (*skip-gram*) or a word from the words around it (*CBOW*). The released vectors: about 3 million words and phrases, 300 numbers each, trained on about 100 billion words of Google News.
- **Word analogies:** directions on the map carry meaning, so king − man + woman lands near queen, and Paris − France + Italy near Rome. Catch: the standard test skips the three input words; without that rule, the nearest word to king − man + woman is usually *king* (Nissim and others, 2020).
- **Bias in embeddings:** embeddings absorb associations in their training text, such as gender stereotypes about jobs (Bolukbasi and others, 2016).
- **Token:** the unit a language model reads and writes: a whole word, a piece of one, a character, a space or punctuation. In English, a token is about three quarters of a word on average (about 4 characters).
- **Tokenizer:** the separate tool that cuts text into tokens and turns them into token numbers (and back again for the answer). It's built from text before the model is trained and stays fixed; each model family usually has its own, so the same text can be a different number of tokens in different models.
- **Byte pair encoding (BPE):** one way to build a token vocabulary: start from single characters (or bytes) and repeatedly merge the most frequent adjacent pair. From a 1994 compression method by Philip Gage, adapted for translation by Sennrich and others (2016). GPT-2's vocabulary: 50,257 tokens. Newer models use about 100,000 to 200,000.
- **Embedding table:** in today's models, the first layer: one learned vector per token, looked up before anything else happens. GPT-3's has 12,288 numbers per token.
- **Polysemy:** one word, several meanings ("bank", "bat", "light"). A single static embedding can't tell them apart; that takes context, which the next episodes are about.

## Why tokens explain some odd behavior

- **Prices and limits:** APIs charge per token, and a model's context window (how much text it can take in) is counted in tokens.
- **Other languages:** tokenizers trained mostly on English split many other languages into more tokens, so the same text costs more and fills the context faster; for some languages, many times more (Petrov and others, 2023).
- **Spelling:** a model sees "strawberry" as two or three tokens, not ten letters, which is why counting its R's, reversing words or rhyming used to trip models up. Long numbers get split into chunks too.

## Papers and sources

- J. R. Firth (1957), "A synopsis of linguistic theory, 1930–1955", in *Studies in Linguistic Analysis*. The "company it keeps" line.
- Tomas Mikolov, Kai Chen, Greg Corrado and Jeffrey Dean (2013), [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781). word2vec.
- Tomas Mikolov and others (2013), [Distributed Representations of Words and Phrases and their Compositionality](https://arxiv.org/abs/1310.4546). The faster version, phrases, and the Paris − France + Italy example.
- Tolga Bolukbasi and others (2016), [Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings](https://arxiv.org/abs/1607.06520).
- Malvina Nissim, Rik van Noord and Rob van der Goot (2020), [Fair is Better than Sensational: Man is to Doctor as Woman is to Doctor](https://arxiv.org/abs/1905.09866). How the analogy test's rules shape its results.
- Rico Sennrich, Barry Haddow and Alexandra Birch (2016), [Neural Machine Translation of Rare Words with Subword Units](https://arxiv.org/abs/1508.07909). Byte pair encoding for language.
- Aleksandar Petrov and others (2023), [Language Model Tokenizers Introduce Unfairness Between Languages](https://arxiv.org/abs/2305.15425).
- Daniel Jurafsky and James H. Martin, [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/), chapter 6, "Vector Semantics and Embeddings". Free online, and the clearest longer treatment.

Next: episode 7, "Reading one word at a time".
