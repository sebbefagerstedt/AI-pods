# Episode 10: Inside the transformer, layer by layer

From Zero to ChatGPT, season 1, episode 10. About 23 minutes, with Frank and Alice. Part 3, "The birth of LLMs".

Why the original transformer had two towers, an encoder that reads and a decoder that writes, and why GPT threw the encoder away. Then one word's trip up through the layers: the embedding, the running notepad each layer adds to, attention and the feed-forward part, and finally the output layer, which turns the top notepad into a probability for every possible next token. It reads off the answer; it doesn't decide it.

## Key terms

- **Encoder:** the left tower of the original transformer. Reads the whole input at once, each token attending to every other token in both directions, and outputs one vector (list of numbers) per token: notes, not words.
- **Decoder:** the right tower. Writes the output one token at a time. Its self-attention is *masked*: each position sees only earlier positions, so it can't peek at words not yet written (or, in training, copy the answer).
- **Cross-attention (encoder-decoder attention):** the decoder's extra sub-layer that looks at the encoder's output, the bridge between the towers. Attention was first invented as exactly this bridge, for LSTM translation models (Bahdanau, Cho and Bengio, 2014).
- **Encoder-decoder (sequence-to-sequence):** the two-tower design, natural when the input is complete before the output starts: translation, summarizing, speech to text. Used by the original transformer, T5 and Whisper.
- **Decoder-only:** one tower, with masked self-attention and no cross-attention. GPT and nearly all of today's chatbots. Prompt and answer are one stream of text; the prompt is read by the same layers that write the answer. Once cross-attention is gone, a decoder block is the same as an encoder block plus the mask.
- **Encoder-only:** one tower without the mask, like Bert. Strong at understanding, but not trained to continue text.
- **Embedding:** the list of numbers each token starts as, taken from a table with one row per token in the vocabulary, plus position information. 768 numbers per token in GPT-1, 12,288 in GPT-3.
- **Residual stream:** the "notepad". Each token's vector runs up through the stack, and each sub-layer adds its output to it rather than replacing it (a *residual connection*, the "Add" in the paper's "Add & Norm" boxes; "Norm" is *layer normalization*, which keeps the numbers in a steady range). The term comes from Anthropic's 2021 interpretability work.
- **Attention head:** one of several attention mechanisms running side by side in a layer, each free to look for something different. GPT-1 has 12 per layer, GPT-3 96.
- **Feed-forward layer (MLP):** the second half of each layer. Works on each token separately: a wider hidden layer (3,072 units in GPT-1, four times the embedding size) then back down. Geva and others (2020) describe it as key-value memory: each unit's "key" detects a pattern, and its "value" nudges the prediction toward certain tokens.
- **Layer (block):** attention plus feed-forward, with their residual connections. The original transformer: 6 in each tower. GPT-1: 12. Bert: 12 or 24. GPT-2: up to 48. GPT-3: 96.
- **Output layer (unembedding, "LM head"):** turns the top vector into a score for every token in the vocabulary (about 40,000 in GPT-1, 50,257 in GPT-2 and GPT-3), by comparing it with each token's vector. The "Linear" box at the top of the paper's diagram.
- **Logits:** those raw scores. **Softmax** turns them into probabilities that add up to 100% (the "Softmax" box).
- **Weight tying:** using the embedding table again, in reverse, as the output layer. Done in the original transformer (section 3.4: "we share the same weight matrix between the two embedding layers and the pre-softmax linear transformation") and in GPT-1 and GPT-2. Some later models keep separate tables.
- **Logit lens:** applying the output layer to the vector halfway up the stack, to see what the model would predict at that point. Early layers give rough guesses; the final answer often appears in the middle layers and gets sharpened.

## Back to "Attention Is All You Need"

You've read the paper, so here's where the episode's ideas sit in Figure 1, the diagram with two towers.

- **Left tower, "N×":** the encoder, one block repeated N = 6 times. Each block: multi-head attention, then feed-forward, each followed by "Add & Norm".
- **Right tower:** the decoder, also 6 blocks, each with three parts: *masked* multi-head attention (no peeking), multi-head attention whose arrows come from the encoder (cross-attention, the bridge), and feed-forward.
- **"Add & Norm":** the residual stream (Add) and layer normalization (Norm).
- **"Linear" and "Softmax" at the top right:** the output layer. Section 3.4 explains that its weights are shared with the embeddings.
- **"Output Probabilities":** the spread of bets over every next token that the next episode turns into words.
- GPT-1 keeps the right tower minus the arrows from the left: masked attention plus feed-forward, 12 times.

## Numbers worth remembering

- Original transformer: built for English-German (4.5 million sentence pairs) and English-French (36 million) translation. Base model: 6 + 6 layers, 512 numbers per token, trained in 12 hours on 8 GPUs. Big model: 3.5 days, and a new record for English-German.
- GPT-1: 12 decoder layers, 768 numbers per token, 12 heads, about 117 million parameters, about 40,000 tokens in its vocabulary.
- GPT-3: 96 layers, 12,288 numbers per token, 96 heads, 175 billion parameters.

## Papers and sources

- Ashish Vaswani and others (2017), [Attention Is All You Need](https://arxiv.org/abs/1706.03762). The two towers, and the shared embedding and output weights (section 3.4).
- Dzmitry Bahdanau, Kyunghyun Cho and Yoshua Bengio (2014), [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473). Attention, invented as the bridge between an encoder and a decoder.
- Peter Liu and others (2018), [Generating Wikipedia by Summarizing Long Sequences](https://arxiv.org/abs/1801.10198). The Google team that dropped the encoder and ran sources and article as one stream; GPT-1 builds on this decoder-only design.
- Alec Radford and others (2018), [Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf). GPT-1. Equation 2 shows the tied output layer: the top state times the transposed embedding matrix, then a softmax.
- Jacob Devlin and others (2018), [BERT](https://arxiv.org/abs/1810.04805). Encoder only.
- Colin Raffel and others (2019), [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683). T5, Google's comparison of encoder-decoder, decoder-only and other designs, where encoder-decoder came out best on their tests.
- Alec Radford and others (2022), [Robust Speech Recognition via Large-Scale Weak Supervision](https://arxiv.org/abs/2212.04356). Whisper, an encoder-decoder for speech.
- Ian Tenney, Dipanjan Das and Ellie Pavlick (2019), [BERT Rediscovers the Classical NLP Pipeline](https://arxiv.org/abs/1905.05950). Parts of speech show up in lower layers, sentence structure higher, and roles and coreference (which word "it" refers to) highest.
- Mor Geva and others (2020), [Transformer Feed-Forward Layers Are Key-Value Memories](https://arxiv.org/abs/2012.14913). From Tel Aviv University and the Allen Institute.
- Kevin Meng, David Bau, Alex Andonian and Yonatan Belinkov (2022), [Locating and Editing Factual Associations in GPT](https://arxiv.org/abs/2202.05262). Facts stored mostly in middle-layer feed-forward parts, and edited one at a time (ROME), like moving the Space Needle from Seattle to Paris (in GPT-2 XL and GPT-J).
- nostalgebraist (2020), [interpreting GPT: the logit lens](https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens), LessWrong.
- Nelson Elhage and others (2021), [A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html), Anthropic. Where the residual stream as a shared channel comes from.
- The trophy and suitcase sentence is a classic Winograd schema, a test of common sense from Terry Winograd's work in the 1970s, made into a benchmark by Hector Levesque in 2011.
- Mark Twain (1880), "The Awful German Language", an appendix to *A Tramp Abroad*: the German who dives into a sentence and comes up "on the other side of his Atlantic with his verb in his mouth".

Next: episode 11, "What happens when you press Enter".
