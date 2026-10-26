# Episode 2: Machine learning, teaching by example

From Zero to ChatGPT, season 1, episode 2. About 18 minutes, with Frank and Alice. Part 1, "How machines learn".

What an AI model actually is: a machine with adjustable knobs. How training works (guess, measure how wrong, nudge the knobs, repeat), why training and using a model are separate phases, and why memorizing isn't learning. With Clever Hans, the horse who seemed to do arithmetic, and the image model that recognized horses by a copyright tag.

## Key terms

- **Model:** a machine (in practice, a program) that turns an input into an output: a photo into "cat", an email into "spam", text into the next word. Mathematically, a function.
- **Parameters (weights):** the model's adjustable knobs. Each is a number that says how much some input or combination matters, and in which direction. People choose the design; training sets the values. GPT-3 has 175 billion. A "70B model" has about 70 billion.
- **Training:** finding good knob settings from examples, in a loop: the model guesses, the guess is compared with the right answer, and every knob is nudged a little toward a better guess. One pass through all the examples is an *epoch*.
- **Loss:** a single number for how wrong the model is, averaged over examples. Training tries to push it down. For prices, a common choice is the average squared difference, which punishes big misses extra. For language models it's how surprised the model is by the real next word (the GPT-1 episode).
- **Inference:** using a trained model, with its knobs frozen. Fast and cheap compared with training. Chatting with a model doesn't change its parameters.
- **Labeled data and supervised learning:** examples that come with the right answer attached, and learning from them.
- **Overfitting:** fitting the training examples, including their flukes, so closely that the model does worse on new ones. *Underfitting* is the opposite: a model too simple to capture the pattern.
- **Generalization:** doing well on examples the model has never seen, the real goal.
- **Training set and test set:** the examples the model learns from, and the ones held back to check it afterwards. Often there's also a *validation set*, held back for choosing between designs during development, so the test set stays untouched until the end.
- **Benchmark contamination:** when test questions end up in the training data (big models read much of the web, and tests get posted online), so a high score may partly be memory.
- **Shortcut learning ("Clever Hans" effect):** a model that finds an easy pattern that works on the data it's given but isn't the thing you meant, like a copyright tag instead of a horse.

## A twist: big models and overfitting

The classic picture says more knobs than examples means memorizing. Yet today's largest networks, trained on enough data, generalize well, and making a model bigger can even cut its test error after it already fits the training data perfectly ("double descent", Belkin and others, 2019). Why is still being studied. The practical rule that survived: too many knobs for too little data is the problem.

## Papers and sources

- Oskar Pfungst (1907), *Clever Hans (The Horse of Mr. von Osten)*, English translation 1911, [on Project Gutenberg](https://www.gutenberg.org/ebooks/33936). How he showed that Hans responded to tiny, unintended cues from the people asking.
- Sebastian Lapuschkin and others (2019), [Unmasking Clever Hans predictors and assessing what machines really learn](https://doi.org/10.1038/s41467-019-08987-4), *Nature Communications*. The horse classifier that relied on a copyright tag in the corner of the photos.
- John Zech and others (2018), [Variable generalization performance of a deep learning model to detect pneumonia in chest radiographs](https://doi.org/10.1371/journal.pmed.1002683), *PLOS Medicine*. The model could tell which hospital an X-ray came from, and did worse at hospitals it hadn't seen.
- Robert Geirhos and others (2020), [Shortcut learning in deep neural networks](https://arxiv.org/abs/2004.07780), *Nature Machine Intelligence*. A readable overview of shortcuts, starting with Clever Hans.
- Mikhail Belkin and others (2019), [Reconciling modern machine learning practice and the bias-variance trade-off](https://arxiv.org/abs/1812.11118). Double descent.
- Arthur Samuel (1959), [Some Studies in Machine Learning Using the Game of Checkers](https://doi.org/10.1147/rd.33.0210), where the term "machine learning" comes from.

Next: episode 3, "Neural networks without the math".
