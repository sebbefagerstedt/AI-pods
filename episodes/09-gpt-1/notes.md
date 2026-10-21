# Episode 9: GPT-1 and pre-training

From Zero to ChatGPT, season 1, episode 9. About 26 minutes, with Frank and Alice. The first episode of part 3, "The birth of LLMs".

What G, P and T stand for. How OpenAI's 2018 model learned language by guessing the next word in seven thousand unpublished books, then learned each new task from a few thousand labeled examples. Why Google's Bert, which plays fill-in-the-blank, beat it four months later, and why GPT's approach led to ChatGPT anyway. Meant to be heard before reading the GPT-1 paper; a reading guide follows below.

## Key terms

- **Labeled data:** examples a person has tagged with the right answer ("this review: positive"). Slow and expensive to make, so there's never much of it. Learning from it is *supervised learning*.
- **Language model (the LM in LLM):** a model that predicts the next word. Strictly, the next *token*, a word or a piece of one (episode 6). It doesn't pick one word; it spreads probability over all of them, and training makes it less surprised by the word that actually comes next.
- **Self-supervised learning:** learning from raw text that nobody labeled, because the text is its own answer key: the "label" for each word is simply the word that follows. The GPT-1 paper calls this *unsupervised*.
- **Pre-training:** the first, expensive stage: learning general language by predicting the next word in a huge pile of text, before you've picked any task. The P in GPT. When the news mentions a lab's "pre-training run", this is what it means.
- **Fine-tuning:** the second, cheap stage: start from the pre-trained model, add a small output layer, and train a little more on a few thousand labeled examples. For most tasks GPT-1 went through its labeled examples three times. Today's chat models are still made this way, pre-training then further training (episode 12).
- **Transfer learning:** reusing what a model learned on one job for another. In images, networks pre-trained on ImageNet (episode 5) had been reused for years. In language, before 2018, mostly only word embeddings (episode 6) were reused: the first layer, like getting a dictionary but no reading experience.
- **GPT:** generative pre-trained transformer. Generative: trained by predicting the next word. Pre-trained: on raw text first. Transformer: the architecture from episode 8.
- **Decoder-only transformer:** the original transformer (episode 8) had an encoder that reads the input (the left tower in its famous diagram) and a decoder that writes the output (the right tower). GPT keeps only the decoder, with its masked self-attention: each word can look back but never ahead, which is what next-word prediction needs.
- **Parameters:** the knobs of episode 2. GPT-1 has about 117 million.
- **Context window:** how much text the model can take in at once. GPT-1: 512 tokens, about a page.
- **BooksCorpus:** about 7,000 free books by unpublished authors from the self-publishing site Smashwords, collected in 2015 and also used to train Bert. A 2021 study found about a quarter of it was romance (also 14% fantasy, 5% vampires), many books licensed "for personal enjoyment only", and thousands of duplicates.
- **Input transformations:** GPT-1's way of fitting every task into one stretch of text: glue the parts together with a separator token (premise $ hypothesis), and for multiple choice, glue the context to each answer in turn and let the model score each.
- **Zero-shot:** doing a task with no examples and no fine-tuning, only by predicting words. GPT-1's paper tried it on four tasks and found the scores rose steadily during pre-training, the seed of GPT-2 and GPT-3 (episode 11).
- **Ablation:** taking one part out to see how much it mattered. Without pre-training, GPT-1's average score fell by 14.8 points; with an LSTM instead of the transformer, by 5.6.
- **BERT:** Bidirectional Encoder Representations from Transformers, Google, October 2018. Uses the transformer's encoder, so every word sees the whole passage in both directions. Spelled "Bert" in the script so it's said as a name.
- **Masked language model:** Bert's training game: hide 15% of the tokens and predict them from both sides. It's a version of the *cloze test*, a fill-in-the-blank reading test described by Wilson Taylor in 1953. Bert can't simply predict the next word while looking both ways, because each word could then "see itself".

## Reading the GPT-1 paper

Radford, Narasimhan, Salimans and Sutskever (2018), [Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf). Twelve pages, of which the last four or so are references. It was never posted to arXiv; the PDF is on OpenAI's site.

**Before you start**

- The paper never says "GPT". In its tables the model is "Finetuned Transformer LM (ours)". By the time of Google's BERT paper, four months later, it was "OpenAI GPT", for Generative Pre-trained Transformer; "GPT-1" came only after GPT-2.
- "Unsupervised" means trained on unlabeled text (self-supervised, in today's words); "supervised" means trained on labeled examples; "semi-supervised" is the combination, which is the paper's approach.
- "Discriminative" tasks are judging tasks: classify, choose, compare. "Generative" means producing text.
- "Task-agnostic" means one model for every task, as opposed to architectures "specifically crafted for each task".

**Section by section**

- **Abstract and 1, Introduction:** the problem (labeled data is scarce, raw text is abundant) and the two-stage plan. The key sentence: "We employ a two-stage training procedure."
- **2, Related work:** the predecessors. Word embeddings (word2vec, GloVe) transfer only word-level information; Dai and Le (2015) and Howard and Ruder (ULMFiT, January 2018) pre-trained LSTM language models and fine-tuned them; ELMo (February 2018) fed pre-trained LSTM features into task-specific models. GPT-1's claim: a transformer handles longer-range structure, and needs only minimal changes per task.
- **3.1, Unsupervised pre-training:** Equation 1 says: make the actual next token as likely as possible, given the k tokens before it. Equation 2 is the model: token embeddings plus position embeddings, through 12 transformer blocks, then a softmax over the vocabulary, which is the spread of bets over every possible next token.
- **3.2, Supervised fine-tuning:** Equations 3 and 4 put a single linear layer on the final hidden state of the last token to predict the label. Equation 5 adds next-word prediction as an *auxiliary objective* during fine-tuning (weight λ = 0.5). The ablations in section 5 show it helps on large datasets but not small ones.
- **3.3, Task-specific input transformations, with Figure 1:** the gluing trick. Spend your time on Figure 1: on the left the model, on the right how entailment, similarity and multiple-choice inputs become token sequences with start, delimiter and extract tokens.
- **4.1, Setup:** BooksCorpus, chosen for "long stretches of contiguous text", unlike the 1B Word Benchmark used by ELMo, which is shuffled sentence by sentence. Model: 12 decoder layers, 768-dimensional states, 12 attention heads, 512-token context, a byte pair encoding vocabulary with 40,000 merges, learned position embeddings instead of the sinusoids in the transformer paper, and the GELU activation. The learning rates and dropout can be skipped. "Perplexity of 18.4" means that on average the model was as unsure as if choosing among about 18 equally likely tokens.
- **4.2, Supervised fine-tuning results:** Tables 2 to 4 cover twelve datasets in four groups. Natural language inference (does sentence B follow from A: SNLI, MultiNLI, QNLI, RTE, SciTail), question answering and commonsense reasoning (RACE, Story Cloze), semantic similarity (MRPC, Quora Question Pairs, STS-B) and classification (sentiment: SST-2; grammaticality: CoLA). Records on 9 of 12, for example Story Cloze 86.5% (previously 77.6), RACE 59.0% (previously 53.3) and a GLUE score of 72.8 (previously 68.9). It fell short on RTE, one of the smallest datasets, and on MRPC and SST-2.
- **5, Analysis:** the most interesting part. Figure 2 (left): each pre-trained layer you keep helps, up to 9 points on MultiNLI. Figure 2 (right) and "Zero-shot behaviors": without any fine-tuning, the pre-trained model's scores on four tasks climb steadily as pre-training goes on. Table 5: the ablations.
- **6, Conclusion:** "our model acquires significant world knowledge and ability to process long-range dependencies".

**Numbers worth remembering**

- About 117 million parameters (the figure comes from the GPT-2 paper, which describes its smallest model as equivalent to the original GPT).
- About 7,000 books, about 5 GB of text, about 800 million words.
- One month on one machine with 8 GPUs, 0.96 petaflop/s-days of compute in all.
- Fine-tuning: usually 3 passes over the labeled data.

**GPT-1, the original transformer and Bert**

- *Transformer (2017):* encoder and decoder, 6 layers each in the base model, built for translation, sinusoidal position encodings.
- *GPT-1 (June 2018):* decoder only, 12 layers, about 117 million parameters, reads left to right, trained to predict the next token on BooksCorpus. Under the hood the decoder and encoder blocks are nearly the same; the main difference is the mask that stops each token from looking ahead. GPT-1 also drops the decoder's attention to the encoder, since there is no encoder.
- *Bert (October 2018):* encoder only, 12 layers (Base, about 110 million parameters, the same size as GPT-1 on purpose) or 24 (Large, about 340 million), reads both ways, trained to fill in masked tokens and to tell whether two sentences follow each other, on BooksCorpus plus English Wikipedia (about 4 times the text). GLUE average 79.6 (Base) and 82.1 (Large) against GPT-1's 75.1, on the same tests.

## Papers and sources

- Alec Radford, Rafal Jozefowicz and Ilya Sutskever (2017), [Learning to Generate Reviews and Discovering Sentiment](https://arxiv.org/abs/1704.01444). The sentiment neuron: a 4,096-unit LSTM trained for a month on 4 GPUs to predict the next character of 82 million Amazon reviews.
- OpenAI (2018), [Improving language understanding with unsupervised learning](https://openai.com/index/language-unsupervised/), the blog post for GPT-1: "1 month on 8 GPUs", the "very" trick for sentiment (about 80% with no training), and "significant room for improvement using the well-validated approach of more compute and data".
- Alec Radford, Karthik Narasimhan, Tim Salimans and Ilya Sutskever (2018), [Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf). GPT-1.
- Ashish Vaswani and others (2017), [Attention Is All You Need](https://arxiv.org/abs/1706.03762). The transformer.
- Peter Liu and others (2018), [Generating Wikipedia by Summarizing Long Sequences](https://arxiv.org/abs/1801.10198). The decoder-only transformer that GPT-1 builds on.
- Andrew Dai and Quoc Le (2015), [Semi-supervised Sequence Learning](https://arxiv.org/abs/1511.01432). An early pre-train-then-fine-tune recipe, with LSTMs.
- Jeremy Howard and Sebastian Ruder (2018), [Universal Language Model Fine-tuning for Text Classification](https://arxiv.org/abs/1801.06146). ULMFiT: with 100 labeled examples, it matched training from scratch on 100 times more.
- Matthew Peters and others (2018), [Deep contextualized word representations](https://arxiv.org/abs/1802.05365). ELMo, from the Allen Institute for AI and the University of Washington.
- Sebastian Ruder (2018), [NLP's ImageNet moment has arrived](https://thegradient.pub/nlp-imagenet/), *The Gradient*. Why reusing only word embeddings is like reusing an image model that only knows about edges.
- Jacob Devlin, Ming-Wei Chang, Kenton Lee and Kristina Toutanova (2018), [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805).
- Yukun Zhu and others (2015), [Aligning Books and Movies](https://arxiv.org/abs/1506.06724), where BooksCorpus comes from; and Jack Bandy and Nicholas Vincent (2021), [Addressing "Documentation Debt" in Machine Learning Research: A Retrospective Datasheet for BookCorpus](https://arxiv.org/abs/2105.05241).
- Nasrin Mostafazadeh and others (2016), [A Corpus and Cloze Evaluation for Deeper Understanding of Commonsense Stories](https://arxiv.org/abs/1604.01696). The Story Cloze Test, and the Tom and Sheryl example.
- Guokun Lai and others (2017), [RACE: Large-scale ReAding Comprehension Dataset From Examinations](https://arxiv.org/abs/1704.04683). English exams for Chinese students aged 12 to 18; careful human readers reach about 95%.
- Wilson Taylor (1953), [Cloze Procedure: A New Tool for Measuring Readability](https://doi.org/10.1177/107769905303000401), *Journalism Quarterly*.
- Pandu Nayak (2019), [Understanding searches better than ever before](https://blog.google/products/search/search-language-understanding-bert/), Google: Bert in search, and the Brazil traveler example.
- Alec Radford and others (2019), [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). GPT-2, for episode 11.
- The detective-novel comparison is one Ilya Sutskever has used in interviews to explain why predicting the next word well takes understanding.

Next: episode 10, "What happens when you press Enter".
