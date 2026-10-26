# Episode 3: Neural networks without the math

From Zero to ChatGPT, season 1, episode 3. About 17 minutes, with Frank and Alice. Part 1, "How machines learn".

What's inside the machine with knobs. An artificial neuron, explained as deciding whether to go to the beach. Rosenblatt's 1958 perceptron and its press coverage; why a single neuron can't work the stairway light switches, and the 1969 book that cooled the field; how layers fix that, why photo networks learn edges, then textures, then parts; what "deep" means; and the road from the perceptron to today's networks with billions of knobs.

## Key terms

- **Artificial neuron:** multiplies each input by a weight, adds them up with a bias, and passes the total through an *activation function* that decides how strongly it "fires". The perceptron fired all or nothing; modern networks use smooth or simple ramps (like ReLU: pass positive totals through, turn negative ones into zero).
- **Weight:** how much one input matters to a neuron, and whether it pushes for or against firing. The knobs of episode 2.
- **Bias (threshold):** how easily the neuron fires, also learned. Not the same as bias in the sense of unfairness.
- **Perceptron:** Frank Rosenblatt's learning machine (1957–58): a single layer of neurons with adjustable weights, trained by the *perceptron rule*: when an answer is wrong, nudge the weights toward the right one. The *perceptron convergence theorem* says this finds a correct setting whenever one exists.
- **Mark I Perceptron:** the hardware version, with a 20 × 20 grid of 400 light sensors and weights stored in potentiometers turned by electric motors. It's at the Smithsonian's National Museum of American History.
- **Linearly separable:** a problem one neuron can solve, because one straight line (in more dimensions, a flat plane) separates the yes cases from the no cases.
- **XOR (exclusive or):** "one or the other, but not both", like a light controlled by two switches. Not linearly separable, so no single neuron can do it; a network with a hidden layer can.
- **Hidden layer:** neurons between input and output, whose results aren't seen directly. They compute useful intermediate features.
- **Feature:** something a neuron detects: an edge, a fur texture, an eye.
- **Deep network, deep learning:** networks with many layers, and training them. "Deep" refers only to the number of layers.
- **Universal approximation theorem:** a network with one hidden layer and enough neurons can approximate any reasonable input-output relationship as closely as you like (Cybenko, 1989; Hornik and others, 1989). It says good settings exist, not how to find them, or how many neurons it takes; depth usually makes it far cheaper.
- **Synapse:** a connection between two real neurons, the closest thing in the brain to a weight. Estimates for the human brain run around 100 trillion, against 86 billion neurons.

## Numbers worth remembering

- 1958: the perceptron learns left from right after about 50 punch cards, on an IBM 704.
- 1969: Minsky and Papert's *Perceptrons*.
- 1989: LeCun's network reads handwritten zip codes; by the late 1990s, systems built on his convolutional networks read a large share of US checks (LeCun's own estimate is 10 to 20%).
- 2015: image networks with over 100 layers (ResNet: 152).
- GPT-3: 96 layers, 175 billion parameters. The brain: about 100 trillion synapses on about 20 watts.

## Papers and sources

- Frank Rosenblatt (1958), [The perceptron: A probabilistic model for information storage and organization in the brain](https://doi.org/10.1037/h0042519), *Psychological Review*.
- "New Navy Device Learns By Doing", *The New York Times*, July 8, 1958. The "walk, talk, see, write, reproduce itself and be conscious of its existence" article.
- Marvin Minsky and Seymour Papert (1969), *Perceptrons: An Introduction to Computational Geometry*, MIT Press.
- George Cybenko (1989), [Approximation by superpositions of a sigmoidal function](https://doi.org/10.1007/BF02551274), *Mathematics of Control, Signals and Systems*. The universal approximation theorem.
- Yann LeCun and others (1989), [Backpropagation Applied to Handwritten Zip Code Recognition](https://doi.org/10.1162/neco.1989.1.4.541), *Neural Computation*.
- Matthew Zeiler and Rob Fergus (2013), [Visualizing and Understanding Convolutional Networks](https://arxiv.org/abs/1311.2901). Pictures of what each layer of an image network responds to: edges, then textures, parts and objects.
- ACM (2019), [Fathers of the Deep Learning Revolution Receive ACM A.M. Turing Award](https://awards.acm.org/about/2018-turing): Bengio, Hinton and LeCun.

Next: episode 4, "How machines actually learn".
