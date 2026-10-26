# Episode 5: 2012, the big bang

From Zero to ChatGPT, season 1, episode 5. About 18 minutes, with Frank and Alice. The last episode of part 1, "How machines learn".

Why neural networks, around since the 1980s, suddenly took over in 2012. The three ingredients: ImageNet, Fei-Fei Li's millions of labeled photos; graphics cards built for video games, which happen to do exactly the arithmetic neural networks need; and AlexNet, which cut the error in the ImageNet contest from about 26% to 15%. Then the $44 million auction, the race that followed, and how Nvidia ended up at the center of AI.

## Key terms

- **ImageNet:** about 14 million photos sorted into more than 20,000 categories taken from WordNet, a database of English words. Begun by Fei-Fei Li in 2006–2007, presented in 2009. Labeled by tens of thousands of workers on Amazon Mechanical Turk (Li's count: about 49,000 from 167 countries).
- **ImageNet challenge (ILSVRC):** a yearly contest from 2010 to 2017 on a subset of about 1.2 million training photos in 1,000 categories, about 120 of them dog breeds.
- **Top-5 error:** the share of test photos where the right category isn't among the system's five best guesses. Winners: 28.2% (2010), 25.8% (2011), 15.3% (AlexNet, 2012; next best 26.2%), 3.6% (ResNet, 2015).
- **Amazon Mechanical Turk:** an online marketplace for small tasks done by people for small payments, named after the 1770 chess "automaton" that hid a human player inside.
- **GPU (graphics processing unit):** a chip with thousands of simple arithmetic units working in parallel, built to compute pixels for games. Neural networks are mostly the same kind of work: huge numbers of multiplications and additions that can happen at once.
- **CUDA:** Nvidia's toolkit (2007) for running general-purpose programs on its GPUs. Most deep learning software is built on it, part of why Nvidia leads.
- **Convolutional network (CNN):** a network whose lower layers use small detectors slid across the whole image, reusing the same weights at every position. LeCun's 1989 zip-code reader was one; AlexNet was a much bigger one.
- **AlexNet:** Krizhevsky, Sutskever and Hinton's 2012 network: 8 layers (5 convolutional, 3 fully connected), about 60 million parameters and 650,000 neurons, trained for five to six days on two Nvidia GTX 580 cards with 3 GB each.
- **ReLU:** the "plain ramp" neuron: passes positive totals through and turns negative ones into zero. Trained several times faster than smooth curves.
- **Dropout:** randomly switching off neurons (half of them, in AlexNet's top layers) at each training step, so the network can't rely on any one of them. Fights memorizing.
- **Data augmentation:** making more training examples from the ones you have: flipping, cropping, shifting colors.
- **Transfer learning:** reusing a network trained on one big dataset, like ImageNet, for another job, by training it a little more. Comes back with language in the GPT-1 episode.

## Papers and sources

- Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li and Li Fei-Fei (2009), [ImageNet: A large-scale hierarchical image database](https://doi.org/10.1109/CVPR.2009.5206848), CVPR.
- Olga Russakovsky and others (2015), [ImageNet Large Scale Visual Recognition Challenge](https://arxiv.org/abs/1409.0575). The contest's history and results, including the human comparison.
- Rajat Raina, Anand Madhavan and Andrew Ng (2009), [Large-scale deep unsupervised learning using graphics processors](https://doi.org/10.1145/1553374.1553486), ICML. Up to 70 times faster on GPUs.
- Alex Krizhevsky, Ilya Sutskever and Geoffrey Hinton (2012), [ImageNet Classification with Deep Convolutional Neural Networks](https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html), NIPS. AlexNet. Figure 3 shows the first layer's learned edge and color detectors.
- Geoffrey Hinton and others (2012), [Improving neural networks by preventing co-adaptation of feature detectors](https://arxiv.org/abs/1207.0580). Dropout.
- Geoffrey Hinton and others (2012), [Deep Neural Networks for Acoustic Modeling in Speech Recognition](https://doi.org/10.1109/MSP.2012.2205597), *IEEE Signal Processing Magazine*. The same breakthrough in speech, from Toronto, Microsoft, Google and IBM.
- Kaiming He and others (2015), [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385). ResNet, 152 layers, with shortcut connections.
- Andrej Karpathy (2014), [What I learned from competing against a ConvNet on ImageNet](https://karpathy.github.io/2014/09/02/what-i-learned-from-competing-against-a-convnet-on-imagenet/). About 5.1% top-5 error for a trained human.
- Cade Metz (2021), *Genius Makers*. The book with the Lake Tahoe auction for DNNresearch, won by Google at $44 million.
- Fei-Fei Li (2023), *The Worlds I See*. Her memoir, including how ImageNet was built.

Next: episode 6, "Words as numbers".
