# Episode 4: How machines actually learn

From Zero to ChatGPT, season 1, episode 4. About 17 minutes, with Frank and Alice. Part 1, "How machines learn".

How a network with billions of knobs finds good settings. Gradient descent, pictured as walking downhill in fog; why the step size matters and why each step uses only a small random batch; and backpropagation, which works out every knob's share of the blame in one backward pass, like a kitchen tracing a salty dish back through its stations. Plus why it still took decades: fading blame in deep networks, and too little data and computing power.

## Key terms

- **Loss landscape:** a picture where every point is one setting of all the knobs and the height is the loss. Training means finding low ground. With two knobs it's a real landscape; with billions it has billions of directions, which nobody can picture, but the method works the same.
- **Gradient:** the slope of the landscape where you stand, in every direction at once: for each knob, whether turning it up raises or lowers the loss, and how steeply.
- **Gradient descent:** repeatedly nudging every knob a little in the downhill direction. First described by Augustin-Louis Cauchy in 1847.
- **Learning rate:** the size of each step. Too large and training overshoots or blows up; too small and it crawls. Usually lowered as training goes on (a *learning-rate schedule*).
- **Stochastic gradient descent (SGD):** estimating the slope from a small random *batch* of examples instead of all of them. Noisier, but far more steps for the same work. Today's models mostly use refinements of it, such as Adam (2014), which adapts the step size for each knob.
- **Local minimum:** a dip from which every direction goes up, though it isn't the lowest point. Feared for decades; in very high-dimensional landscapes true traps turn out to be rare (most flat spots are *saddle points*, with a way down somewhere), and the valleys training finds tend to be about equally good.
- **Backpropagation (backprop):** computing the gradient for every knob in one backward pass through the network, by applying the *chain rule* of calculus layer by layer from the output to the input. Costs roughly as much as one or two forward passes.
- **Forward pass / backward pass:** running the network to make a guess; then sending the blame back to get every knob's slope.
- **Vanishing gradient:** in deep networks of the 1980s and 1990s, the blame shrank at every layer on its way back, so the bottom layers barely learned. Eased by simpler neurons (ReLU), better starting values (initialization), normalization, and *residual connections*, shortcuts that let the blame skip layers.
- **Automatic differentiation:** software that works out the backward pass from the forward one, so nobody writes it by hand. Frameworks like PyTorch and JAX do this.

## Numbers worth remembering

- 1847: Cauchy's gradient descent. 1970: Linnainmaa's reverse-mode automatic differentiation. 1974: Werbos proposes it for neural networks. 1986: Rumelhart, Hinton and Williams.
- GPT-3 (2020): batches of about 3.2 million tokens, about 300 billion tokens in all, so roughly 94,000 steps downhill.
- 2024: Geoffrey Hinton and John Hopfield, Nobel Prize in Physics.

## Papers and sources

- Augustin-Louis Cauchy (1847), "Méthode générale pour la résolution des systèmes d'équations simultanées", *Comptes rendus de l'Académie des sciences*. Gradient descent, in three pages.
- Seppo Linnainmaa (1970), master's thesis at the University of Helsinki, the first description of reverse-mode automatic differentiation, the method behind backprop.
- Paul Werbos (1974), *Beyond Regression*, PhD thesis at Harvard, which proposed training neural networks this way.
- David Rumelhart, Geoffrey Hinton and Ronald Williams (1986), [Learning representations by back-propagating errors](https://doi.org/10.1038/323533a0), *Nature*. Four pages; the family-tree network whose hidden units came to encode nationality and generation.
- Yann Dauphin and others (2014), [Identifying and attacking the saddle point problem in high-dimensional non-convex optimization](https://arxiv.org/abs/1406.2572). Why local minima matter less than feared.
- Diederik Kingma and Jimmy Ba (2014), [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980).
- Nobel Prize in Physics 2024, [press release](https://www.nobelprize.org/prizes/physics/2024/press-release/): Hopfield and Hinton, "for foundational discoveries and inventions that enable machine learning with artificial neural networks".

Next: episode 5, "2012, the big bang".
