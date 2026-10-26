# Episode 8: "Attention Is All You Need", explained

From Zero to ChatGPT, season 1, episode 8. About 20 minutes, with Frank and Alice. The last episode of part 2, "Teaching computers language". A companion to the 2017 paper.

The transformer, in plain words. Self-attention, where every word looks at every other word; queries, keys and values as a networking event with questions, name badges and answers; multi-head attention as readers with different highlighters; position stamps made from waves, like the hands of a clock; why processing every word at once fit graphics cards and made training cheap; and a first look at the famous two-tower diagram.

## Key terms

- **Transformer:** the architecture from the paper: layers of attention and feed-forward networks, with no recurrence (no reading one word at a time).
- **Self-attention:** each token scores every token in the same sequence for relevance and replaces itself with a weighted blend of them. Turns a word's dictionary meaning into its meaning in context.
- **Query, key, value (Q, K, V):** three vectors each token computes from its own vector with three learned weight matrices. The query is what it's looking for, the key what it offers to be found by, the value what it hands over.
- **Scaled dot-product attention:** the paper's equation 1. Score each query against every key (a dot product, a measure of how well two lists of numbers line up), divide by the square root of the key length so the scores don't get too extreme, turn them into weights that add up to 1 with a softmax, and take the weighted sum of the values.
- **Multi-head attention:** several attention operations side by side (8 heads in the paper, each working with 64 numbers instead of all 512), each with its own Q, K and V weights, their outputs combined. Heads tend to specialize.
- **Positional encoding:** numbers added to each token's embedding to mark its position, since attention alone ignores order. The paper uses sine and cosine waves of different frequencies; learned position embeddings gave nearly identical results (Table 3, row E). GPT-1 learned them; most of today's models use *rotary position embeddings* (RoPE, 2021), which build position into how queries and keys are compared.
- **Masked self-attention:** in the decoder, each position can attend only to earlier positions: the no-peeking rule.
- **Encoder-decoder attention (cross-attention):** in the decoder, queries come from the decoder and keys and values from the encoder's output: the translator glancing back at the original.
- **Parallelism:** all positions are processed at once in training, unlike an RNN's step by step, which suits GPUs.
- **Quadratic cost:** attention compares every token with every other, so the work grows with the square of the length. Doubling the text means four times the attention work. One reason context windows were long limited.
- **BLEU:** a score for machine translation, roughly how much a translation's word sequences overlap with human reference translations. Higher is better.

## Reading the paper again

Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan Gomez, Łukasz Kaiser and Illia Polosukhin (2017), [Attention Is All You Need](https://arxiv.org/abs/1706.03762). Fifteen pages in the arXiv version, with the attention pictures at the very end.

- **First-page footnote:** "Equal contribution. Listing order is random", followed by who did what.
- **3.1, Encoder and decoder stacks, with Figure 1:** the two towers, 6 layers each. Each encoder layer: multi-head self-attention, then a feed-forward network, each wrapped in "Add & Norm" (a residual connection plus layer normalization). Each decoder layer adds masked self-attention and encoder-decoder attention.
- **3.2.1, Scaled dot-product attention, with Figure 2 (left):** equation 1, the one equation everyone remembers.
- **3.2.2, Multi-head attention, with Figure 2 (right):** h = 8 heads.
- **3.2.3, Applications of attention in our model:** the three uses: encoder self-attention, masked decoder self-attention, and encoder-decoder attention.
- **3.3 and 3.4:** the feed-forward networks (2,048 units wide) and the shared embedding and output weights. Episode 10 covers both.
- **3.5, Positional encoding:** the waves, and why they chose them.
- **4, Why self-attention, with Table 1:** compares layer types by work per layer, how much can run in parallel, and the longest path between two positions: one step for self-attention, as many steps as there are words for an RNN.
- **5 and 6, Training and results:** WMT 2014 English-German (about 4.5 million sentence pairs) and English-French (36 million). Base model about 65 million parameters, 12 hours on 8 P100 GPUs; big model about 213 million, 3.5 days. BLEU 28.4 (English-German) and 41.8 (English-French), records at "a small fraction of the training costs". Table 3 tests variations; Table 4 shows it also works for parsing English sentences.
- **Attention visualizations (after the references):** Figure 3, heads linking "making" to "more difficult" across a long sentence; Figure 4, two heads resolving "its" to "Law"; Figure 5, heads that seem to follow sentence structure.

## Numbers worth remembering

- 512 numbers per token, 8 heads of 64, 6 layers per tower, feed-forward layers 2,048 wide.
- Submitted to arXiv in June 2017; presented at NIPS in December 2017.
- One of the ten most-cited papers of the 21st century (*Nature*, 2025).

## Papers and sources

- Jakob Uszkoreit (2017), [Transformer: A Novel Neural Network Architecture for Language Understanding](https://research.google/blog/transformer-a-novel-neural-network-architecture-for-language-understanding/), Google Research blog. The "animal didn't cross the street because it was too tired / too wide" example.
- Steven Levy (2024), [8 Google Employees Invented Modern AI. Here's the Inside Story](https://www.wired.com/story/eight-google-employees-invented-modern-ai-transformers-paper/), *Wired*. Team Transformer, the Transformers illustration, the Beatles title, and where the authors went.
- Jay Alammar (2018), [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/). The best-known visual walkthrough, if you want pictures of Q, K and V.
- Helen Pearson and others (2025), [Exclusive: the most-cited papers of the twenty-first century](https://www.nature.com/articles/d41586-025-01125-9), *Nature*.
- Jianlin Su and others (2021), [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864). The position method most models use today.

Next: episode 9, "GPT-1 and pre-training".
