# Episode 3: Neural networks without the math

## Cold open

FRANK: Okay, picture this. July 1958, Washington. The US Navy calls in reporters for a demonstration. There's a huge IBM computer, the size of a room. And a young psychologist from Cornell named Frank Rosenblatt is going to show them something he calls the perceptron.

ALICE: The perceptron. That sounds like a fifties sci-fi villain.

FRANK: It kind of does. So here's the demo. They feed the computer punch cards, one at a time. Some have a mark on the left side, some on the right. Nobody tells the program the rule. It just guesses, left or right, and gets told when it's wrong. And after about fifty cards, it's figured it out. It can tell left from right.

ALICE: That's... it? Left from right?

FRANK: That's it. But the program had learned it, from examples, instead of being told. And the next day, the New York Times wrote it up. I'll read you the opening line. "The Navy revealed the embryo of an electronic computer today that it expects will be able to walk, talk, see, write, reproduce itself and be conscious of its existence."

ALICE: From telling left from right?

FRANK: From telling left from right. And the article goes on. It says later perceptrons will be able to recognize people and call out their names, and instantly translate speech from one language to another.

ALICE: Okay, wait. Those two actually happened.

FRANK: They did. About fifty years late, but they happened. And here's the bit I love. Rosenblatt then built a machine version, the Mark One Perceptron. It had a camera made of four hundred light sensors. And its knobs, the things it adjusted while learning, were real knobs. Dials, turned by little electric motors.

ALICE: Hang on. Actual knobs? Like the knobs we kept talking about last time?

FRANK: Actual, physical knobs. Turning themselves as it learned. And the great-great-grandchild of that machine is inside every AI model you've used. Today, it's called a neural network.

## Welcome

ALICE: Welcome to From Zero to ChatGPT. I'm Alice.

FRANK: And I'm Frank.

ALICE: Last time, we said a model is a machine with knobs. Training means showing it examples, measuring how wrong it is, and nudging the knobs. But we never opened the machine. What does it actually look like inside?

FRANK: And the answer, for pretty much every big AI model today, is a neural network. So today: what an artificial neuron is, how you wire them together in layers, what "deep" means in "deep learning", and how we got from the perceptron to today.

ALICE: And "without the math" is in the title, so I'm holding you to that.

FRANK: Without the math. And actually, Alice, you're starting us off.

## One artificial neuron

ALICE: I am. So, first, the name. Neural networks are loosely inspired by the brain. Your brain has about eighty-six billion nerve cells, neurons. And very roughly, each neuron listens to signals from thousands of other neurons. If enough of those signals add up, it fires. It sends its own signal onward.

FRANK: Listen, add up, fire.

ALICE: Listen, add up, fire. And an artificial neuron is a cartoon of that. A very simple cartoon. Let me give you one. Say it's Saturday morning, and you're deciding whether to go to the beach.

FRANK: I'm always deciding that.

ALICE: So you've got a few things to go on. Is it sunny? Is it warm? Is a friend coming? And each one matters to you a different amount. Sun matters a lot. A friend, a bit. And maybe there's one that counts against it, like: is it a long drive?

FRANK: Okay.

ALICE: So the neuron takes each input, and multiplies it by how much it matters to you. That "how much it matters" is the weight. Sun, big weight. Friend, smaller weight. Long drive, a negative weight. Then it adds them all up. And if the total is over some threshold, it fires. Beach. If not, no beach.

FRANK: And the weights are the knobs.

ALICE: The weights are the knobs. Exactly the knobs from last time. And so is the threshold, really. Some people need a lot of convincing to go to the beach. Some people go if there's a single ray of sun.

FRANK: That's me. So the threshold is like how easily it fires.

ALICE: How easily it fires. And that's the whole neuron. Inputs come in, each one gets multiplied by its weight, it all gets added up, and the neuron decides how strongly to fire. That's what Rosenblatt's perceptron was. One layer of these.

FRANK: And how did it learn? Remember, it figured out left from right.

ALICE: With a very simple rule. Show it a card. If it gets it right, do nothing. If it gets it wrong, nudge the weights a little toward the right answer. If it said "left" when it should have said "right", turn down the knobs that pushed it toward left, turn up the ones that pushed toward right.

FRANK: Huh. That's just last episode's training loop.

ALICE: It's exactly that loop. Guess, check, nudge. Rosenblatt even proved that if there's a setting of the knobs that gets every example right, this rule is guaranteed to find it.

FRANK: Okay, that sounds pretty great. So what went wrong? Because I know something went wrong. We've got AI winters coming.

ALICE: Something went wrong. And Frank, that part's yours.

## What one neuron can't do

FRANK: It is. So, one neuron, adding up its inputs and firing over a threshold. Here's what it really does, if you think of it as a picture. Imagine all the possible situations laid out on a big table. Sunny and warm over here, cold and rainy over there. A single neuron draws one straight line across that table. One side of the line: fire. The other side: don't.

ALICE: One straight line. Okay.

FRANK: And a lot of problems can be solved with one straight line. Beach or no beach, mostly. But some can't. And the famous one is this. Do you have stairs at home, with a light switch at the bottom and another at the top?

ALICE: I do.

FRANK: So, flip either switch, and the light changes. Say both switches are down, and the light's off. Flip one up, light's on. Flip the other one up too, and the light goes off again.

ALICE: Right. Both up, off. Both down, off. One up and one down, on.

FRANK: Exactly. The light is on when the two switches disagree. Now try to get one neuron to do that. You've got two inputs, the two switches. If you give the switches a positive weight, then "both up" gives the biggest total of all. So that should be the most "on". But it's off.

ALICE: And if you give them negative weights, "both down" wins. Which is also off.

FRANK: There's no single straight line that separates the "on" situations from the "off" ones. One neuron cannot do this. Not with any setting of the knobs. This problem has a name, by the way. It's called exclusive or. "This one or that one, but not both."

ALICE: Okay, but that sounds like a weird edge case. Light switches.

FRANK: It sounds like one. But it's the simplest example of something everywhere. Whenever the answer depends on how things combine, not just on how much of each thing there is. And in 1969, two big names from MIT, Marvin Minsky and Seymour Papert, wrote a book called "Perceptrons". It worked through, carefully and mathematically, what a single layer of these neurons can and can't do. And the list of can'ts was long.

ALICE: Minsky. He was at the Dartmouth workshop, right? Where AI got its name.

FRANK: Same Minsky. And the book landed hard. Funding for neural networks dried up for years. It's often told as the book that killed the perceptron. That's a bit unfair, it was a careful book, and plenty of other things were going on. But the effect was real.

ALICE: But wait. Couldn't you just use more neurons?

FRANK: Yes! And that's the fix. In fact, people knew that, even then. Here's how you'd do the stairs. Put two neurons in the middle. The first one fires if at least one switch is up. The second one fires only if both switches are up. Then a third neuron, on top, listens to those two. It fires if the first one says yes, and the second one says no.

ALICE: At least one, but not both. Oh, that's neat.

FRANK: And that's the key idea of today. The neurons in the middle are a layer. A hidden layer, because you never see its answers directly. It works out something useful, and passes that up to the next layer. One neuron can only draw one line. Stack them in layers, and together they can draw any shape you like.

ALICE: Okay. So why didn't everyone just do that in 1969?

FRANK: Because of training. Remember the perceptron's rule? It worked because each knob was directly connected to the answer. Wrong answer, nudge the knobs that caused it. But a knob in the middle layer? It's buried. It never touches the answer directly. When the network gets the stairs wrong, which middle knob was to blame? And which way should it turn?

ALICE: Huh. So you can build the network, but you can't teach it.

FRANK: You can build it, but nobody knew a good way to teach it. Solving that took until the eighties, and it's the next episode. Alice, while we wait for the eighties, tell us what all these layers are actually good for.

## Layers, and what deep means

ALICE: Happily. So, let's go back to photos. A photo is just a grid of numbers. How bright each little dot is, how red, how green. And say we want a network that tells cats from dogs.

FRANK: The classic.

ALICE: The classic. Now, no single pixel says "cat". The fifth dot from the left being brown tells you nothing. Meaning only shows up when you combine lots of pixels, in the right way. And that's exactly what layers do.

FRANK: How?

ALICE: Think of it like a factory with several floors. On the first floor, each neuron looks at a small patch of the photo, and learns to fire for something very simple. A bright patch next to a dark one. An edge. Some neurons fire for edges that go up and down, some for edges at a slant, some for a patch of one color.

FRANK: So the first floor finds edges.

ALICE: Edges and blobs of color. Then the second floor listens to the first. And it combines edges into slightly bigger things. Corners. Curves. Stripes, little textures, like fur.

FRANK: And the third floor combines those.

ALICE: Into parts. An eye. A nose. An ear, a wheel, a window. And a floor or two further up, it's combining parts into whole things. A cat face. A dog face. And the top floor just reads that off: cat.

FRANK: Okay, but who decided that floor one does edges and floor three does eyes? Did someone program that?

ALICE: No. And this is the beautiful part. Nobody told it about edges or eyes. The network is just trained with the loop. Guess, check, nudge. And when researchers looked inside trained networks, around 2013, and made pictures of what each neuron responds to, that's what they found. Edges low down. Textures, then parts, then whole objects further up. The network had worked out that this is a useful way to see.

FRANK: Huh. It invented edges.

ALICE: It invented edges. Which is, by the way, roughly what the visual part of your own brain does, too. And there's a mathematical result from 1989 that says something remarkable. A network with enough neurons can, in principle, imitate almost any relationship between inputs and outputs. Any pattern at all, as long as you have enough neurons and the right knob settings.

FRANK: So "it can learn anything"?

ALICE: Careful. It says the right settings exist. It doesn't say you'll find them. Or that you have enough examples. But it tells you the building blocks aren't the limit.

FRANK: Okay. And "deep". "Deep learning". Where does that come in?

ALICE: That's just this. Deep means many layers. A network with one hidden layer is shallow. A network with lots of layers stacked up is deep. And deep learning just means training neural networks with lots of layers.

FRANK: That's it? I always thought "deep" meant something more profound.

ALICE: I think the people who named it didn't mind you thinking that. But no, it's about the number of floors. And there's a good reason depth helps. Each floor can build on the floor below. Edges, then corners, then eyes, then faces. Doing all that in one giant floor would take vastly more neurons.

FRANK: How deep are we talking?

ALICE: The perceptron had one layer of knobs. The big image networks from around 2015 had over a hundred layers. And GPT-3, the model behind early ChatGPT, has ninety-six layers. Each one with a lot more going on inside than our beach neuron. But the same basic idea. Inputs, weights, add up, fire, pass it on.

FRANK: So, ninety-six floors.

ALICE: Ninety-six floors, and a hundred and seventy-five billion knobs. Frank, take us from 1958 to there.

## From the perceptron to today

FRANK: Okay. So after the perceptron book in 1969, neural networks went quiet. Rosenblatt himself died young, in a boating accident, in 1971. And for over a decade, most AI money went to the rulebooks. The expert systems.

ALICE: Which then crashed too.

FRANK: Which then crashed too. But in the mid-eighties, neural networks came back. Because someone made the middle layers trainable. That's the big breakthrough of next episode, so I won't spoil it. But suddenly, networks with hidden layers could learn.

ALICE: And did they do anything useful?

FRANK: Some did. My favorite is from 1989, at Bell Labs in New Jersey. A young French researcher named Yann LeCun trained a network to read handwritten digits. The zip codes on envelopes, from the US Postal Service.

ALICE: Oh, that's practical.

FRANK: Very practical. And it worked. And by the late nineties, a system built on his ideas was reading a good share of all the checks written in the US. Your handwritten check went into a bank, and a neural network read the amount.

ALICE: Okay, so they're a success. Why aren't we talking about the AI boom of the nineties?

FRANK: Because they stalled again. Deep networks, with lots of layers, were really hard to train. Two things were missing. Data, lots and lots of examples. And computing power, because all those knobs take a lot of arithmetic. So through the two-thousands, other methods, ones with neater math, were usually better. A lot of researchers thought neural networks were a dead end.

ALICE: But some kept going.

FRANK: A small group kept going. Geoffrey Hinton in Toronto, Yann LeCun in New York, Yoshua Bengio in Montreal. They later shared the Turing Award, which is the top prize in computer science, for exactly that stubbornness. And in 2012, it all paid off, very suddenly. Data and computing power arrived together, and deep networks blew everything else away. That's a whole episode of its own, a bit later.

ALICE: Okay, I have to ask the obvious question. If it's a neural network, and it has neurons, how does it compare to a brain?

FRANK: The honest answer is: loosely. The idea came from the brain, but an artificial neuron is a cartoon. A real neuron is a living cell, with complicated chemistry, and timing, and it changes all the time. An artificial neuron is: multiply, add up, pass it on. That's all.

ALICE: But in sheer numbers?

FRANK: In sheer numbers, the closest thing to a knob in your brain is a synapse, the connection between two neurons. And you've got something like a hundred trillion of those. GPT-3 has a hundred and seventy-five billion knobs. So your brain has hundreds of times more connections. And it runs on about twenty watts. Less than a light bulb.

ALICE: Okay, I feel better about my brain now.

FRANK: You should. But here's what I find remarkable. From that left-or-right demo in 1958, the basic recipe hasn't changed. Neurons that multiply and add. Layers stacked on layers. Knobs nudged by examples. What changed is the scale. And the trick for training the middle layers.

ALICE: Which you're still not telling me.

FRANK: Which I'm still not telling you. Next time.

## Recap

ALICE: Okay, let's wrap up. Frank, you start.

FRANK: Sure. One: an artificial neuron is a cartoon of a brain cell. It takes some inputs, multiplies each one by a weight that says how much it matters, adds them up, and fires if the total is high enough. The weights are the knobs.

ALICE: Two: the perceptron, from 1958, was one layer of these. It learned from examples with a simple rule: if it's wrong, nudge the knobs toward the right answer. And the press went wild.

FRANK: Three: one neuron can only draw one straight line, so it can't even handle the stairway light switches. A 1969 book laid out those limits, and neural networks fell out of favor.

ALICE: Four: the fix is layers. Hidden layers in the middle work out useful things and pass them up. In a photo network, low layers learn edges, then textures, then parts, then whole objects. Nobody programs that. "Deep" just means lots of layers.

FRANK: And five: it took decades, and data and computing power, to make deep networks work. Today's models have up to hundreds of layers and billions of knobs. But the recipe is still the one from 1958: multiply, add, pass it on.

ALICE: Which leaves the question Frank keeps dodging. How do you train the knobs in the middle layers? When the network gets something wrong, how does a knob buried ninety floors down know which way to turn?

FRANK: That's next time. Walking downhill in fog, and passing the blame backward. How machines actually learn.

ALICE: See you then.
