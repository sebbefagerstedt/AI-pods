# Episode 5: 2012, the big bang

## Cold open

FRANK: Okay, picture this. December 2012. A casino hotel at Lake Tahoe, up in the mountains on the California and Nevada border. There's a big AI conference going on downstairs. And upstairs, in one of the hotel rooms, a professor named Geoffrey Hinton is running an auction.

ALICE: An auction. Of what?

FRANK: Of himself, basically. And two of his students. The three of them had just started a little company. No product. No customers. Basically just three people and one research paper. And four of the biggest names in tech wanted to buy it. Google. Microsoft. The Chinese search giant Baidu. And a small London startup called DeepMind.

ALICE: How does an auction for three people even work?

FRANK: By email. The bidders sent their offers in, and every time a new bid came in, the clock reset, and the others had an hour to beat it. Hinton had a bad back, so he couldn't sit for long. He ran the whole thing more or less standing up, with the students in the room.

ALICE: And how high did it go?

FRANK: The bidding started at twelve million dollars.

ALICE: Twelve million? For three people?

FRANK: It kept going. Fifteen. Twenty. Twenty-five. Thirty. Eventually Google and Baidu were going back and forth over forty million. And at forty-four million dollars, Hinton stopped it. They chose Google.

ALICE: Forty-four million dollars. For a company that was a few weeks old. What was in that paper?

FRANK: A neural network. Trained on two graphics cards, the kind you'd buy to play video games, by a student working at home. And a couple of months earlier, it had blown away every other computer vision system in the world. The network was called AlexNet. And the year it happened, 2012, is when the AI boom we're living in today really started.

## Welcome

ALICE: Welcome to From Zero to ChatGPT. I'm Alice.

FRANK: And I'm Frank.

ALICE: And this one wraps up the first part of the series, how machines learn. After this, we move on to language. So far, we've got all the pieces. A model is a machine with knobs. A neural network wires those knobs into layers of artificial neurons. And training means walking downhill in fog: measure how wrong you were, pass the blame backward, nudge every knob.

FRANK: All of which existed by 1986.

ALICE: All of which existed by 1986. And then, for over twenty years, neural networks were mostly a disappointment. Last time we said what was missing: the fuel. Today, the fuel arrives. Three ingredients. A mountain of labeled photos. Computer chips built for video games. And one network that put them together.

FRANK: And how a company that made graphics cards for gamers ended up at the center of the AI world.

ALICE: That too. And Frank, the photos are mine.

## Millions of labeled photos

ALICE: So, let's go back to around 2006. A young computer scientist named Fei-Fei Li is a professor at the University of Illinois. And she's working on computer vision, getting computers to recognize what's in a picture. And she notices something everyone else seemed to be ignoring.

FRANK: Which was?

ALICE: Everyone was obsessed with the model. Building a cleverer recognizer. But they were all testing them on tiny collections of photos. The well-known ones had a few dozen categories. Maybe a hundred. A few thousand photos in total. And her thought was: a child doesn't learn to see from a few thousand pictures. A child sees an enormous amount of the world.

FRANK: So the problem wasn't the model. It was the data.

ALICE: That was her bet. And it was a very unfashionable bet. So she decided to build a collection of photos of, basically, everything. Every kind of object, with a lot of photos for each one. She took the categories from a big dictionary-like database of English words called WordNet. Every noun you could picture. Dalmatian. Canoe. Strawberry. Pay phone.

FRANK: And where do the photos come from?

ALICE: The internet. By then, there were billions of photos online. So her team searched the web for each category and pulled down huge numbers of candidates. The problem is, if you search for "dalmatian", you get a lot of things that aren't dalmatians. Cartoons. Dalmatian-print sofas. Someone's spotted cat.

FRANK: So someone has to check every photo.

ALICE: Someone has to check every photo. And she worked out that with students checking them, at the pace students work, it would take many years.

FRANK: Years. Okay, so how did she do it?

ALICE: A student told her about a website Amazon had launched not long before, called Mechanical Turk. You post a small task, like "is there a dalmatian in this photo, yes or no", and people all over the world do it for a few cents each.

FRANK: Mechanical Turk. That's a strange name.

ALICE: It's a great name, actually. It's named after a famous fake from the seventeen-hundreds. A chess-playing machine, a mechanical man in Turkish robes, that beat people all over Europe. Napoleon played it. And it turned out there was a human chess master hidden inside the box.

FRANK: So the "artificial intelligence" was a person in a box.

ALICE: A person in a box. And Amazon named its site after it, because it's people quietly doing the work that computers can't. Which is exactly what Fei-Fei Li needed. Over about two and a half years, tens of thousands of workers, from over a hundred and sixty countries, sorted and labeled the photos.

FRANK: How many photos?

ALICE: In the end, around fourteen million. In over twenty thousand categories. She called it ImageNet.

FRANK: Fourteen million labeled photos. That's quite a pile.

ALICE: It's a mountain. Before that, a few thousand was normal. And to get people to use it, in 2010 her team started a yearly contest, the ImageNet challenge. They took a slice of it: about one point two million photos, in a thousand categories. Including over a hundred breeds of dog, by the way, which turns out to be really hard. And they said: train your system on these, and then we'll test it on photos it's never seen.

FRANK: The test set in the drawer.

ALICE: The test set in the drawer. And the scoring is a little generous. Your system gets five guesses per photo. If the right answer is among them, it counts. And the score is how often you miss.

FRANK: How did people do?

ALICE: In 2010, the winner missed about twenty-eight percent of the time. In 2011, about twenty-six. Small, steady improvements, using clever hand-designed methods for picking features out of photos. And almost nobody was using neural networks.

FRANK: And then 2012.

ALICE: And then 2012. But you need the second ingredient first. Frank, why were video games involved?

## Chips built for games

FRANK: So, think about what a video game has to do. Every frame, maybe sixty times a second, it has to work out the color of every pixel on your screen. That's millions of pixels. And for each one, a bit of math. Where does the light hit? Which way is this surface facing? How dark is the shadow?

ALICE: That's a lot of math.

FRANK: A huge amount. But here's the thing: it's simple math, and every pixel can be done at the same time. Pixel number one doesn't have to wait for pixel number two. So in the nineties, companies started making special chips for exactly that. Graphics cards. GPUs, graphics processing units. And one of those companies was called Nvidia.

ALICE: Nvidia. That I've heard of.

FRANK: Everyone has, now. Back then, they made cards for gamers. Now, here's the difference between a GPU and the normal chip in your computer, the CPU. A CPU is like a handful of brilliant professors. Each one can solve anything you give it, fast, but there are only a few of them. A GPU is like a stadium full of schoolkids, each doing simple sums. Any one of them is slower. But there are thousands of them, all working at the same time.

ALICE: And for drawing pixels, you want the stadium.

FRANK: You want the stadium. Now think about a neural network. What does it actually do, all day?

ALICE: Multiply and add. That's what the neurons do. Inputs times weights, add them up.

FRANK: Millions of times. And each neuron in a layer can do its sums at the same time as the others. It's exactly the same kind of work as drawing pixels. Lots of simple arithmetic, all at once.

ALICE: Oh. So the gaming chip was accidentally a neural network chip.

FRANK: Accidentally, yes. And around 2007, Nvidia made it much easier to use their cards for things other than graphics. They released a toolkit called CUDA, which let ordinary programmers send any kind of math to the card. It was mostly meant for scientists. Simulating weather, or molecules. And a few AI researchers noticed. In 2009, a group at Stanford showed that running neural networks on graphics cards made training up to seventy times faster.

ALICE: Seventy times! So a training run that took two months...

FRANK: ...takes less than a day. And that changes everything about walking downhill in fog. You can take seventy times as many steps. Try seventy times as many ideas.

ALICE: Okay. So by 2012 we've got the photos, a million of them, and we've got the chips.

FRANK: Right. And in Toronto, Geoffrey Hinton's lab had both in mind. Alice, tell us about AlexNet.

## AlexNet

ALICE: So, Hinton had two PhD students. Alex Krizhevsky, who was a brilliant programmer, especially at making code run fast on graphics cards. And Ilya Sutskever, who was convinced that if you made neural networks big enough and fed them enough data, they'd just work.

FRANK: Ilya Sutskever. Wasn't he one of the people behind GPT?

ALICE: Same Ilya. A few years later, he co-founded OpenAI. But in 2012, he pushed Alex to take on ImageNet. And Alex built the network. And it's named after him: AlexNet.

FRANK: What did it look like?

ALICE: In a way, nothing new. It was the kind of network Yann LeCun had used for reading zip codes back in 1989. Remember? With one key trick for images. Instead of every neuron looking at the whole photo, the bottom layers use small detectors that slide across the image.

FRANK: Slide across?

ALICE: Imagine a little stencil, looking for one pattern, say, a slanted edge. And you slide it over every part of the photo, top left to bottom right, checking for that edge everywhere. It's the same detector, with the same knobs, used at every spot. Because an edge is an edge, whether it's in the corner or the middle.

FRANK: So you don't need separate knobs for every spot in the picture.

ALICE: Exactly. That saves an enormous number of knobs. This is called a convolutional network. And AlexNet was a big one. Eight layers, sixty million knobs. Much bigger than anything LeCun could have trained in the eighties. And Alex trained it on two gaming graphics cards, Nvidia ones, that cost about five hundred dollars each. At home. It took five or six days.

FRANK: In his bedroom, basically.

ALICE: That's how the story's usually told. And there were a few new tricks, too. One was a simpler neuron. Instead of a smooth curve, it just passes positive totals through and turns negatives into zero. A plain ramp. It sounds like nothing, but it made training several times faster, and it helped with that fading blame from last time.

FRANK: What else?

ALICE: Another one I love, because it's about memorizing. Remember, a network with lots of knobs can memorize instead of learning. So during training, in the top layers, they switched off half the neurons at random, every single step. Different ones each time.

FRANK: Wait, why would you break your own network on purpose?

ALICE: Because then no neuron can rely on any particular other neuron being there. Each one has to learn something useful on its own. It's like a team where you never know who'll show up to work, so everyone has to know the whole job. It's called dropout. And it helped a lot against memorizing.

FRANK: Clever. And?

ALICE: And they stretched the data. Flipping photos left to right, cutting out slightly different crops, shifting the colors a bit. A dog facing left is still a dog facing right. So every photo becomes many photos.

FRANK: Okay. So, the result. The others were missing about twenty-six percent.

ALICE: The second-best team missed twenty-six percent. AlexNet missed fifteen.

FRANK: Fifteen? From twenty-six?

ALICE: From twenty-six to fifteen, in one year. The previous year, the improvement had been two points. This was more than ten. In a field where people celebrated a one-point gain. People who were there say it was a shock. Some researchers had spent their whole careers on hand-designed methods for images. And a neural network, which they'd mostly written off, beat all of it in one go.

FRANK: And what had it learned? Like those edges we talked about?

ALICE: Exactly that. The paper shows pictures of what the first layer's detectors look like. Little slanted edges, stripes at different angles, blobs of color. Nobody told it to look for edges. It worked that out, from a million photos, by walking downhill.

FRANK: So the method from 1986 just needed a million photos and some gaming cards.

ALICE: That's basically the story. The method was there. ImageNet was the fuel. And the GPUs were the engine. And Frank, you've already told us how the next few weeks went.

## After the bang

FRANK: Right, the auction. Forty-four million dollars, two months after the contest. And that was only the start. Within a couple of years, almost every team in the ImageNet challenge was using neural networks. And the big tech companies started hiring anyone who knew how to train them. Facebook, Google, Microsoft, Baidu. Hinton went to Google. So did Alex and Ilya.

ALICE: And the contest itself?

FRANK: Kept getting better, fast. In 2015, a team at Microsoft built a network with a hundred and fifty-two layers. Remember last time, the problem with deep networks was the fading blame. They used those shortcuts we mentioned, where the blame can skip floors. And it missed under four percent.

ALICE: Under four. How good is a person at this?

FRANK: Someone actually tested that. A researcher named Andrej Karpathy, who later helped start OpenAI, sat down and did the test himself, after training on the categories for a while. He missed about five percent. Partly because, honestly, who knows a hundred and twenty dog breeds?

ALICE: So by 2015, computers were beating at least one very dedicated person.

FRANK: At this one test. With the usual warning: it's a test, with five guesses, on tidy photos. Not "computers can see as well as people". But it was an astonishing three years.

ALICE: And it wasn't just photos, right?

FRANK: No. The same year as AlexNet, Hinton's group and others showed that deep networks also beat the old methods at recognizing speech. Within a few years, the voice assistants on your phone ran on them. Translation followed, a bit later. And here's something that matters for where this series is going. People found that a network trained on ImageNet had learned something general about seeing. Edges, textures, shapes. So if you wanted to recognize, say, fractures in X-rays, you didn't start from scratch. You took an ImageNet network, and trained it a little more on your X-rays.

ALICE: So the big expensive training is reused for lots of jobs.

FRANK: Reused. Keep that in your pocket. It comes back, in a big way, with language. Okay, and now Nvidia.

ALICE: Yes. How did a gaming company end up running AI?

FRANK: Once everyone saw what AlexNet did on two gaming cards, everyone wanted graphics cards. Lots of them. And Nvidia's boss, Jensen Huang, made a big bet. He turned the company toward AI. They started building cards specifically for training neural networks, and selling them to data centers instead of gamers. And they kept improving CUDA, the software. Which matters, because all the AI tools were built on it. So even when competitors made fast chips, the software everyone used ran best on Nvidia.

ALICE: So they had the chips and the software.

FRANK: The chips and the software. And then, ten years after AlexNet, ChatGPT came out, and every company on earth wanted to train big models. And for that you need tens of thousands of these chips. Today, most of Nvidia's money comes from AI chips for data centers, not games. And in 2025, it became the first company ever to be worth over four trillion dollars.

ALICE: From two gaming cards in a bedroom.

FRANK: From two gaming cards in a bedroom. Well, and a lot else. But that's where the line starts.

ALICE: You know what strikes me about this whole story? It's the bitter lesson again. From the first episode. People spent decades designing clever features for recognizing images by hand. And the thing that won was a simple, general method, given a lot more data and a lot more computing power.

FRANK: That's the lesson. And it's going to come back, louder, every time. Data, computing power, and a method that can use both.

## Recap

ALICE: Okay, let's wrap up. Frank, you start.

FRANK: Sure. One: Fei-Fei Li bet that computer vision needed more data, not cleverer models. She built ImageNet: about fourteen million photos, labeled by tens of thousands of online workers. Its yearly contest used one point two million photos in a thousand categories.

ALICE: Two: graphics cards, built to draw video game pixels, turned out to be perfect for neural networks. Both are mostly huge amounts of simple multiplying and adding, all at once. Nvidia's CUDA software let researchers use them, and training got dozens of times faster.

FRANK: Three: in 2012, AlexNet, built by Alex Krizhevsky and Ilya Sutskever in Geoffrey Hinton's lab, and trained on two gaming cards, cut the error in the ImageNet contest from about twenty-six percent to fifteen. A sliding-detector network, plus tricks like dropout, which fights memorizing.

ALICE: Four: after that, everything moved. A forty-four-million-dollar auction for a company a few weeks old. Neural networks took over images, then speech, then translation. And networks trained on ImageNet got reused for other jobs.

FRANK: And five: Nvidia went from gaming to the center of AI, with the chips and the software everyone built on. And it's the bitter lesson again: simple methods, with lots of data and computing power, beat clever hand-made ones.

ALICE: Which wraps up the first part of the series. We know how machines learn. Next up: language. And the first problem is a basic one. A photo is already numbers. A word isn't. So how do you turn words into numbers a network can work with?

FRANK: That's next time. Words as numbers. Tokens, embeddings, and how king minus man plus woman ends up at queen.

ALICE: See you then.
