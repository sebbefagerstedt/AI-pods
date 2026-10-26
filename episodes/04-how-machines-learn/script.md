# Episode 4: How machines actually learn

## Cold open

ALICE: Frank, I'm going to drop you on a mountain.

FRANK: Okay. That's a strong opening.

ALICE: You're somewhere high up, on a big, rolling mountainside. And you need to get down to the village in the valley, because that's where the hot food is. But there's a catch. The fog is so thick you can't see your own feet. No map, no phone. You can't see the village. You can't see anything.

FRANK: Great. So what do I do?

ALICE: You tell me.

FRANK: Okay. Well, I can still feel the ground. So I'd feel around with my foot. Which way does it slope down? And then take a step that way.

ALICE: And then?

FRANK: And then do it again. Feel for downhill, take a step. Feel again, step again. And hope I end up somewhere low.

ALICE: Congratulations. You've just invented the most important algorithm in modern AI.

FRANK: Wait, that's it? Just walking downhill?

ALICE: That's it. Every model you've ever heard of, the image recognizers, the voice assistants, ChatGPT, every single one learned by doing exactly what you just did. Feeling for downhill in the fog, and taking a small step. Billions of times.

FRANK: Huh. I was expecting something cleverer.

ALICE: Oh, there's a clever part too. It's how you feel the slope when the mountain has a hundred billion directions. And that's today.

## Welcome

FRANK: Welcome to From Zero to ChatGPT. I'm Frank.

ALICE: And I'm Alice.

FRANK: So, where are we. Two episodes ago, we said a model is a machine with knobs, millions or billions of them. Training means showing it examples, measuring how wrong it was, that's the loss, and nudging the knobs to be less wrong.

ALICE: And last time, we opened the machine. It's a neural network. Neurons that multiply and add, stacked in layers. And we ended on a cliffhanger.

FRANK: We did. Here it is. When the network gets something wrong, how does each knob know which way to turn? Especially a knob buried deep in the middle, nowhere near the answer?

ALICE: Today we answer that. Two ideas. The first is walking downhill in fog, which has a fancy name: gradient descent. The second is how you work out which way is downhill for every knob at once. That's called backpropagation, and it's basically a system for passing the blame backward.

FRANK: Passing the blame. I feel like I've worked in that office.

ALICE: Everyone has. But first, Frank, convince us we need any of this. Why can't we just try stuff?

## Why not just try things?

FRANK: Fair question. So, the simplest idea for setting the knobs: try random settings, and keep the best one. Like spinning every dial on a safe and hoping it opens.

ALICE: I'm guessing that doesn't work.

FRANK: Let's see. Say each knob only had ten possible settings. With two knobs, that's a hundred combinations. Fine. With ten knobs, ten billion. And remember the road trip from the very first episode? The number of possible routes exploded so fast that a computer couldn't check them all before the end of the universe?

ALICE: The combinatorial explosion.

FRANK: This is much, much worse. GPT-3 has a hundred and seventy-five billion knobs. Even at ten settings each, the number of combinations is a one followed by a hundred and seventy-five billion zeros. The number of atoms in the whole universe only has about eighty zeros. Random guessing is hopeless.

ALICE: Okay. What about something smarter. One knob at a time. Turn knob number one up a hair, run the model on some examples, and see if the loss went up or down.

FRANK: Now that actually works! In principle. It tells you which way to turn that knob. The problem is the cost. To learn about one knob, you have to run the whole model on your examples again. So for a billion knobs...

ALICE: ...a billion test runs. Just to take one step.

FRANK: A billion test runs, for one step. And training takes many thousands of steps. You'd be waiting a very long time.

ALICE: So what we actually need is something that tells us, for every knob at once, which way to turn it. In about the time it takes to run the model once.

FRANK: That's exactly what we need. And amazingly, it exists. But first we need the right picture in our heads. And that's the mountain. Alice, it's your mountain.

## Walking downhill in fog

ALICE: It is. So, here's the picture. Let's go back to a tiny model with just two knobs. And imagine a landscape. Every spot on the landscape stands for one setting of the two knobs. Walk east, and you're turning up knob one. Walk north, you're turning up knob two.

FRANK: So the position on the map is the knob settings.

ALICE: Exactly. And the height of the ground at each spot is the loss. How wrong the model is with the knobs set like that. High ground, very wrong. Low ground, nearly right.

FRANK: Oh, I see. So finding good knob settings means finding low ground.

ALICE: Finding the valley. That's the whole of training, in one picture. And the fog is because we can't see the whole landscape. We'd have to try every setting to map it out, which is the random guessing problem again. All we can do is stand where we are, and feel the ground under our feet.

FRANK: And the slope under my feet tells me...

ALICE: Which way is downhill, from right here. And it tells you something for each knob. Turning knob one up makes things a bit worse, so turn it down. Turning knob two up makes things a lot better, so turn it up, and by more. That slope, in all directions at once, is called the gradient.

FRANK: The gradient. And descent means going down it.

ALICE: Gradient descent. Feel the slope, take a step downhill, repeat. And it was first written down by a French mathematician named Augustin Cauchy. In 1847.

FRANK: 1847? That's older than the light bulb.

ALICE: Older than the light bulb. He came up with it for calculations in astronomy, working out orbits. Same idea, though: you can't solve the problem directly, so you get there by small steps downhill.

FRANK: Okay, but our model doesn't have two knobs. It has billions. What does that landscape look like?

ALICE: It has billions of directions instead of two. And nobody can picture that. Not me, not the people who build these things. But here's the lovely part: you don't need to picture it. The fog rule works exactly the same. Feel the slope, in every direction at once, and step downhill.

FRANK: Okay. How big a step?

ALICE: Great question, because it matters a lot. The size of the step is called the learning rate. And if your steps are too big, you leap right over the valley. You land on the far slope, higher than before. Then you leap back. You can bounce around forever, or even go flying off the mountain.

FRANK: And too small?

ALICE: Too small, and you're shuffling forward a millimeter at a time. You'll get there, but it'll take forever, and training costs real money. So in practice, people often start with bigger steps, and shrink them as they get close to the bottom.

FRANK: Like slowing down as you come into the village.

ALICE: Exactly. And one more trick, which is how it's really done. To feel the true slope, you'd have to check how wrong the model is on all of your examples. Millions of them. Every single step.

FRANK: That sounds slow.

ALICE: Way too slow. So instead, each step, you grab a small random handful of examples. A few dozen, maybe a few thousand. And feel the slope just for those.

FRANK: But then the slope is a bit off.

ALICE: It's a bit off. It's a wobbly guess at downhill. But it's much, much quicker, so you can take far more steps. Think of it like asking for directions. You could survey the whole town. Or you could ask three people on the street, start walking, and ask three more at the next corner.

FRANK: And you'd still get there.

ALICE: You'd still get there, a little wobbly. And the wobble even helps sometimes. It can shake you out of a small dip that isn't the real valley. This is called stochastic gradient descent, stochastic just means random. And it's how essentially every big model is trained.

FRANK: Wait, you just said "a small dip that isn't the real valley". That's my worry. What if I walk down into some little hollow, halfway down the mountain? Everything around me goes up. So I stop. But the village is somewhere else, much lower.

ALICE: That's the classic worry. It's called getting stuck in a local minimum. And for decades, people thought it would doom this whole approach. But it turns out that with billions of directions, it's surprisingly rare to be truly trapped. For a spot to be a real dead end, the ground has to go up in every one of those billions of directions. Usually, there's still some way down.

FRANK: Huh. So the huge number of knobs actually helps.

ALICE: In this way, yes. And the valleys you do end up in tend to be about equally good. You don't need the lowest point on the whole mountain. You just need low enough. Okay, Frank. We've got the walking. Now the hard part. How do you feel the slope, for a billion knobs, without a billion test runs?

FRANK: Ah. That's mine.

## Passing the blame backward

FRANK: So. Let's go back to what the slope means for one knob. It's: if I turn this knob up a tiny bit, does the loss go up or down, and by how much? In other words: how much is this knob to blame for the mistake?

ALICE: Okay. Blame.

FRANK: Let's do it with a restaurant. A big kitchen, with stations. At the top, there's the head chef, who plates the final dish. Below the head chef, there's the sauce station and the grill station. And below them, the people prepping vegetables, making stock, and so on.

ALICE: Layers.

FRANK: Layers. The head chef is the output layer, the prep cooks are down near the input. Now, a dish goes out. And it comes back. The customer says, too salty.

ALICE: Oh no.

FRANK: The head chef tastes it. And she knows how she put the plate together. A lot of the sauce, a little bit of the grill. So she says: sauce, this is mostly on you. Grill, a little bit on you. She hands the blame down, in proportion to how much each station contributed.

ALICE: Okay.

FRANK: Now the sauce station does the same thing. The sauce was made of stock, and butter, and a reduction. The stock was the salty part. So the sauce cook passes most of their blame to the stock person. And so on, all the way down. The blame flows backward through the kitchen, from the plate to the prep cooks. And at every station, it gets split up according to who contributed what.

ALICE: And at the end, everyone knows their share.

FRANK: Everyone knows their share, and which way to adjust. Less salt in the stock. A bit less sauce on the plate. And here's the crucial thing. That only took one trip backward through the kitchen. Not a separate investigation for every cook.

ALICE: Oh. So that's the trick. One pass forward to make the dish, one pass backward to hand out the blame.

FRANK: That's the trick. In the network, the forward pass is the model making its guess. Then you measure the loss. And then the blame flows backward, layer by layer. Each layer works out how much each of its knobs contributed, and passes the rest of the blame down to the layer below. And when it reaches the bottom, every single knob has its share of the blame. Which is exactly its slope.

ALICE: And that's the knob buried ninety floors down. It finally finds out what it did wrong.

FRANK: Exactly. That's the answer to last episode's cliffhanger. And the cost: the backward pass takes about as much work as the forward pass, maybe twice. Not a billion times. That's the difference between impossible and done by Tuesday.

ALICE: What's it called?

FRANK: Backpropagation. Propagating the error backward. People just say backprop. And under the hood, it's a rule from calculus that's over three hundred years old, called the chain rule. If A affects B, and B affects C, then you can work out how A affects C, step by step. Backprop is the chain rule, done very efficiently, all the way back through the network.

ALICE: So who invented it?

FRANK: That's a bit of a sore point in the field, because it was found several times. A Finnish student named Seppo Linnainmaa worked out the efficient backward method in his master's thesis in 1970, though not for neural networks. An American, Paul Werbos, suggested using it for neural networks in 1974. But the version that made everyone pay attention came in 1986. A short paper in Nature, by David Rumelhart, Geoffrey Hinton and Ronald Williams.

ALICE: Hinton again. He was in the last episode.

FRANK: Same Hinton. And what made that paper land wasn't just the method. It was what the hidden layers learned. One of their examples was about two family trees, one English, one Italian. They trained a network to answer questions like "who is Victoria's father?". And when they looked inside, the hidden neurons had picked up things nobody told them about. One tracked which generation a person was in. Another, which country the family was from.

ALICE: So, the same thing as edges in photos. Nobody told it.

FRANK: Same thing. The middle layers found their own useful ideas. Just from the blame flowing backward. And in 2024, Hinton shared the Nobel Prize in Physics, with John Hopfield, for their early work on neural networks.

ALICE: A Nobel in physics, for this.

FRANK: For this. Which surprised a lot of physicists. Alice, so we've had backprop since 1986. Why wasn't there ChatGPT in 1990?

## Why it still took decades

ALICE: Good question, and there are a couple of answers. The first one is a problem inside backprop itself. Remember the blame getting split up and passed down, floor by floor?

FRANK: Yeah.

ALICE: In those old networks, at every floor, the blame got multiplied by a small number. Think of each floor passing on only a fraction of what it got. After two or three floors, fine. But after ten floors, a fraction of a fraction of a fraction...

FRANK: ...is basically nothing.

ALICE: Basically nothing. The bottom floors barely got any blame at all, so they barely learned. It's like a game of telephone, where the message gets quieter at every person, until the last person just hears silence. It's called the vanishing gradient problem.

FRANK: So deep networks couldn't learn their bottom layers.

ALICE: Not well. Which is why, for a long time, networks stayed shallow. And the fixes came slowly, over the next twenty-plus years. Simpler neurons, that don't shrink the blame so much. Smarter starting values for the knobs. And later, a really clever one: shortcuts that let the blame skip floors, so it doesn't fade on the way down. Today's biggest models are full of those shortcuts.

FRANK: And the second answer?

ALICE: The second answer is: scale. Walking downhill takes a lot of steps, and every step means running the network forward and backward on a batch of examples. In 1986, computers were tiny. And there just wasn't much data. A few thousand examples was a big dataset.

FRANK: So the method was there, but not the fuel.

ALICE: The method was there, but not the fuel. Which brings us to 2012, when both arrived at once. But let me give you a sense of where this ends up. When GPT-3 was trained in 2020, it was exactly this loop. Feel the slope on a batch of text, step downhill, repeat. Each step used a batch of about three million tokens, words or pieces of words. And it took on the order of a hundred thousand steps.

FRANK: A hundred thousand steps down the mountain. With a hundred and seventy-five billion directions.

ALICE: In fog. And the whole time, the people training it watch one number: the loss, going down. That falling line is the heartbeat of any training run. And nobody writes the backward pass by hand anymore. Software does the chain rule automatically. You describe the forward pass, and it works out the blame for you.

FRANK: So when I hear that some lab is "training a model" for three months on a giant cluster of chips...

ALICE: ...they're walking downhill in fog. Very fast, on a very big mountain.

FRANK: I'm never going to hear it the same way again.

## Recap

ALICE: Okay, let's wrap up. Frank, you start.

FRANK: Sure. One: you can't set billions of knobs by guessing. Random settings are hopeless, and testing one knob at a time would take a billion runs for every step.

ALICE: Two: picture a landscape where every spot is a setting of the knobs, and the height is the loss. Training means finding low ground. Without seeing the map, you feel the slope under your feet, the gradient, and step downhill. That's gradient descent. Walking downhill in fog.

FRANK: Three: the step size, the learning rate, matters. Too big and you leap over the valley, too small and it takes forever. And in practice, each step feels the slope on just a small random batch of examples. Wobbly, but much faster.

ALICE: Four: backpropagation finds the slope for every knob in one backward pass. Like a kitchen passing the blame for a salty dish back through the stations. It made hidden layers trainable, and the 1986 paper that made it famous showed the middle layers inventing their own ideas.

FRANK: And five: deep networks still struggled for decades, because the blame faded on the way down, and because data and computers were tiny. The method was there. The fuel wasn't.

ALICE: Which leaves the story of the fuel. Millions of labeled photos, graphics cards built for video games, and one network that changed everything in a single year.

FRANK: That's next time. 2012, the big bang.

ALICE: See you then.
