# Episode 2: Machine learning, teaching by example

## Cold open

ALICE: Frank, I want to tell you about the smartest horse in history.

FRANK: Okay. I'm listening.

ALICE: Berlin, around 1904. A retired math teacher named Wilhelm von Osten has a horse called Hans. And he's spent years teaching Hans arithmetic. You ask Hans, "What's three plus five?", and Hans taps his hoof. One, two, three... eight times. And stops.

FRANK: Come on.

ALICE: Fractions, too. Dates on the calendar. Telling the time. Huge crowds came to watch. The newspapers called him Clever Hans. And here's the thing: it wasn't a con. Von Osten wasn't secretly signaling. A panel of experts, including a zoo director and a circus manager, studied the horse and found no trick at all.

FRANK: So the horse could actually count?

ALICE: That's what a young psychologist named Oskar Pfungst set out to test. And he tried a few things. First, he had someone ask the question who didn't know the answer themselves.

FRANK: And?

ALICE: Hans fell apart. Then he put blinders on Hans, so the horse couldn't see the person asking. Fell apart again. Hans could only get it right if he could see someone who knew the answer.

FRANK: Oh. So he was reading the people.

ALICE: He was reading the people. As the taps got close to the right number, the person asking would tense up, ever so slightly. And on the right number, they'd relax. A tiny nod, a breath. Nobody did it on purpose. Most of them didn't even know they were doing it. And Hans had learned to stop tapping when the humans relaxed.

FRANK: That's honestly still impressive. Just not arithmetic.

ALICE: Exactly. Hans learned something real. It just wasn't what everybody thought he'd learned. And keep that horse in mind, because he's the patron saint of today's topic. Teaching by example, and the ways it goes wrong.

## Welcome

FRANK: Welcome to From Zero to ChatGPT. I'm Frank.

ALICE: And I'm Alice.

FRANK: Last time, we told the story of AI's two big ideas. Idea one: write down the rules of intelligence by hand. Idea two: let the machine work out the rules itself, from examples. And idea two won.

ALICE: But we never really said what that means. "The machine learns." Learns how? What's actually going on in there?

FRANK: That's today. Three things. First, what a model actually is. You hear "AI model" in the news every day, and I want you to have a real picture of it. Second, how training works, and what it means for a model to be "wrong". And third, the difference between memorizing and actually learning. Which is where our horse comes back.

ALICE: And no equations.

FRANK: No equations. Just knobs. You'll see.

## A machine with knobs

FRANK: So, let's start with the word "model". Alice, if I say "model", what do you picture?

ALICE: Honestly? A model train. Or someone on a catwalk.

FRANK: Fair. In AI, a model is something much plainer. It's a machine that takes something in, and gives an answer out. That's it. A photo goes in, "cat" comes out. An email goes in, "spam" or "not spam" comes out. Some text goes in, the next word comes out.

ALICE: Okay. So a model is like a recipe. Ingredients in, dish out.

FRANK: That's a good start. Let's build a tiny one. Say we want a model that guesses the price of an apartment. And to start, we'll give it just one thing to go on: the size, in square meters.

ALICE: Okay. So, bigger apartment, higher price.

FRANK: Right. So here's the simplest possible model. Take the size, and multiply it by some number. A price per square meter. That number is a knob. Turn it up, and every guess goes up. Turn it down, every guess goes down.

ALICE: And what should the knob be set to?

FRANK: That's the whole question. If you live in a cheap town, it should be low. In a big city, high. And here's the key idea: we don't set it by hand. We let the model find the right setting from examples. From apartments that actually sold.

ALICE: Okay, but one knob isn't much of a model. A tiny flat in the city center costs more than a big one out in the country.

FRANK: Exactly. So we add more inputs. Size, number of rooms, which neighborhood, how old the building is, whether there's a balcony. And each input gets its own knob. How much does a balcony add? How much does an old building take off? Ten inputs, ten knobs.

ALICE: So the knobs are basically how much each thing matters.

FRANK: That's a great way to put it. Each knob says how much one thing matters, and in which direction. And the people who build the model choose the design. Which inputs go in, how they're combined. But the settings of the knobs are learned.

ALICE: Okay, apartments I get. But a photo? How do you turn a photo into inputs?

FRANK: A photo is already numbers. Zoom in far enough on any digital photo, and it's a grid of tiny dots, pixels. And each pixel is stored as a few numbers: how red, how green, how blue. A phone photo has millions of pixels. So a photo is millions of numbers.

ALICE: So a model that looks at photos has millions of inputs.

FRANK: Millions of inputs. And to make sense of them, it needs a lot more than one knob per input. Knobs that combine pixels into edges, edges into shapes, shapes into whiskers and ears. We'll see how that's organized in the next episode. For now, just the scale. A good photo model in the twenty-tens had tens of millions of knobs. GPT-3, from 2020, has a hundred and seventy-five billion.

ALICE: A hundred and seventy-five billion knobs. That's...

FRANK: It's a lot of knobs. And when you read in the news that some company released a "seventy-billion-parameter model", parameters is just the official word for knobs. You'll also hear "weights". Same thing.

ALICE: Parameters, weights, knobs. Okay. But here's what I don't get. Nobody can set a hundred and seventy-five billion knobs by hand. Nobody can even set ten, really. So how do they get set?

FRANK: That's training. And Alice, that's your part.

## Training, and how wrong

ALICE: It is. So, picture our apartment model on day one. All the knobs are set at random. It has no idea about anything.

FRANK: So its guesses are garbage.

ALICE: Total garbage. You show it a two-room apartment, and it says, I don't know, four dollars. Or forty million. So we start training. And training is a loop. Three steps, over and over. Step one: show the model an example. An apartment that actually sold. It makes its guess.

FRANK: Four dollars.

ALICE: Four dollars. Step two: compare the guess with the real price. Say it really sold for three hundred thousand. So the model was way off. And we measure how far off. That measurement is the most important idea in this whole episode. It's called the loss. It's just a number that says how wrong the model was.

FRANK: How wrong. That's it?

ALICE: That's it. Big number, very wrong. Small number, nearly right. Zero, spot on. And in practice, you average it over lots of examples, so you get one number for how wrong the model is overall.

FRANK: Why does it have to be one number?

ALICE: Because then you can tell if you're getting better. If you nudge the knobs and the number goes down, good nudge. If it goes up, bad nudge. One number is something you can push on.

FRANK: Okay. And step three?

ALICE: Step three: nudge the knobs. Every knob gets turned a tiny bit, in whichever direction would have made that guess less wrong. Then back to step one, with the next apartment.

FRANK: Just a tiny bit?

ALICE: Just a tiny bit. That's important. If you turned the knobs all the way to fit one apartment perfectly, you'd ruin them for all the others. So it's small nudges, over thousands of examples. And usually several passes through all of them.

FRANK: It's like tuning a shower. Too cold, turn it a little. Too hot, back a little.

ALICE: That's exactly it. The shower has one knob, and you're the training loop. You feel how wrong it is, you nudge, you check again. A model does the same thing, except with millions of knobs at once.

FRANK: Okay, but with a shower, I know which way to turn. Too cold means turn toward hot. With millions of knobs, how does the model know which way to turn each one?

ALICE: That is a great question, and it gets its own episode. The short version is that there's a clever bit of math that works out, for every knob at once, which way would make the loss go down. We'll call it walking downhill in fog. Later in the series.

FRANK: Okay. I'll hold you to that.

ALICE: Please do. Now, there's one more distinction I want to make, because it clears up a lot of confusion. There are two completely different phases in a model's life. Training, which is the loop we just did. And using it.

FRANK: Using it like, me typing into ChatGPT.

ALICE: Exactly. Think of it like school and then the job. Training is school. It's slow, it's expensive, and it happens once, before anyone uses the model. For the big chatbots, training takes months, on thousands of chips, and costs a fortune. Then the knobs are frozen. And using the model is the job. Something goes in, the frozen knobs do their thing, an answer comes out. That's fast and cheap by comparison.

FRANK: Wait. Frozen? So when I chat with ChatGPT, it isn't learning from me?

ALICE: Not in the moment, no. Your conversation doesn't turn its knobs. The company might use conversations later, to train the next version, but that's a whole separate round of training. While you're chatting, the knobs stay exactly where they are.

FRANK: Huh. I think I'd assumed it was learning as we talked.

ALICE: A lot of people assume that. And one more thing about what goes in. For our apartment model, every example comes with the right answer. This apartment, this price. Somebody had to write down those answers. Examples with the answer attached are called labeled examples. And learning from them is called supervised learning.

FRANK: Supervised, because there's an answer key.

ALICE: Because there's an answer key. And answer keys are expensive. Somebody has to sit there and label things. Remember that, because it turns out to matter a lot when we get to chatbots. Frank, you've got the bit where things go wrong.

## Memorizing versus learning

FRANK: I do. Alice, did you ever have a classmate who memorized the answers to last year's exam?

ALICE: Oh, definitely. And it worked great, right up until the teacher changed the questions.

FRANK: Exactly. And that's the single biggest trap in machine learning. Because a model can get really good at the examples it trained on, without learning anything that works on new ones.

ALICE: Memorizing instead of understanding.

FRANK: Memorizing instead of understanding. The official word for it is overfitting. And here's how it happens. Say we give our apartment model a huge number of knobs, way more than it needs. And only a few hundred apartments to learn from. With that many knobs, the model can find a setting that matches every single sale exactly. Including the flukes.

ALICE: What kind of flukes?

FRANK: Say one apartment sold for way too much, because two buyers got into a bidding war. A sensible model should shrug at that. It's a one-off. But a model with too many knobs bends itself to fit it anyway. And now it thinks there's something special about apartments on that street, on the third floor, with blue doors.

ALICE: Blue doors.

FRANK: Something that silly. Fits the old examples perfectly, and gets new ones wrong. And the opposite problem exists too. Give the model too few knobs, like our one-knob model, and it can't capture what's going on at all. It thinks every square meter is worth the same everywhere. That's called underfitting.

ALICE: So too few knobs, it's too simple. Too many, and it memorizes.

FRANK: That's the classic picture. And the real goal has a name. It's called generalizing. Doing well on examples you've never seen. That's the only thing that counts. Nobody needs a model that's great at predicting the price of apartments that already sold.

ALICE: Okay, but how do you even know which one you've got? If the model gets the training examples right, it could be learning or memorizing. They look the same.

FRANK: And that's the trick everyone uses. Before training, you take some of your examples and lock them in a drawer. The model never sees them during training. Not once. Then, at the end, you take them out and test the model on them.

ALICE: Like the teacher keeping the real exam questions secret.

FRANK: Exactly like that. The examples in the drawer are called the test set. If the model does well on the training examples, and just as well on the test set, it's learned something real. If it's brilliant on the training examples but bad on the test set...

ALICE: ...it memorized last year's exam.

FRANK: It memorized last year's exam. And this is why you'll hear people get so upset when test questions leak. Today's big models train on huge chunks of the internet. And the internet is full of tests. So when a company announces some impressive score, one of the first questions people ask is: had the model seen the questions before?

ALICE: Huh. So the answer key might have been in its reading pile.

FRANK: Sometimes it was. Researchers check for this now, and they keep making new tests to stay ahead of it. Now, one honest twist. The classic picture says too many knobs means memorizing. But today's giant models have billions of knobs, and they generalize remarkably well. More knobs, used with a lot more data, turned out to help, not hurt. Why exactly is still being studied.

ALICE: So "too many knobs" isn't really the problem.

FRANK: Too many knobs for too little data. That's the problem. But there's a sneakier way for things to go wrong, even when the model does well on the test. And that one's yours, because it's a horse.

## Learning the wrong thing

ALICE: It's a horse. So, Clever Hans passed every test von Osten gave him. And he'd have passed a test set too. Hold back some sums, ask them later, and he gets them right. As long as a person who knew the answer was standing there.

FRANK: So the test set wouldn't catch him.

ALICE: The test set wouldn't catch him. Because in the test, the same shortcut was still there. The humans were still relaxing at the right number. Hans learned a rule that worked perfectly, in every situation anyone had thought to try. Just not the rule they thought.

FRANK: And models do this too?

ALICE: All the time. It's called shortcut learning. And there's a lovely example, about horses, as it happens. In 2019, a team of researchers in Germany looked inside an image model that was very good at spotting horses in photos. They used a technique that highlights which parts of the image the model was actually looking at.

FRANK: And it wasn't looking at the horse.

ALICE: It was looking at the corner of the picture. A lot of the horse photos in its training set came from the same source, and they had a little copyright tag in the corner. The model had learned: tag in the corner, must be a horse.

FRANK: No.

ALICE: Yes. They even added that tag to a picture of a car, and the model said: horse. And the researchers called this a Clever Hans predictor. After our horse.

FRANK: That's amazing. But also kind of worrying. Because on the test, it would look great.

ALICE: On the test, it looked great. Because the test photos had the same tags. And there have been more serious cases. Medical models that learned to read chest X-rays, and partly learned which hospital the scan came from, because some hospitals had sicker patients. Again, great on the test. Useless at a new hospital.

FRANK: So how do you fight that?

ALICE: Partly with better data. Make sure the shortcut isn't there. Mix your sources, so the copyright tag shows up on cats too. Test at a different hospital. And partly with tools that peek inside the model, to see what it's actually paying attention to. Pfungst's blinders, basically.

FRANK: Blinders for models. I like it.

ALICE: And here's why I think this matters so much. A model doesn't learn what you meant. It learns whatever pattern makes the loss go down. If there's an easy pattern, it'll find it. That's the strength of learning from examples, and it's also the danger.

FRANK: It finds patterns we'd never think to write down...

ALICE: ...including ones we'd never want. Exactly. And that goes all the way up to today's chatbots. The question "did it really learn this, or did it find a shortcut?" comes up again and again.

FRANK: Okay. So let me try to put the whole thing together. A model is a machine with knobs. Training means showing it examples, measuring how wrong it was, and nudging the knobs. Over and over.

ALICE: And the goal isn't to ace the examples. It's to do well on things it's never seen.

FRANK: And to do well for the right reasons.

ALICE: For the right reasons. Hans would want you to know.

## Recap

FRANK: Okay, let's wrap up. Alice, you start.

ALICE: Sure. One: a model is a machine that takes something in and gives an answer out. Inside, it has adjustable knobs, officially called parameters or weights. Each one says how much something matters. People design the machine, but the knob settings are learned.

FRANK: Two: training is a loop. Show an example, compare the guess with the right answer, and nudge every knob a tiny bit toward less wrong. Repeat thousands or billions of times.

ALICE: Three: "how wrong" has a name. The loss. One number that training tries to push down.

FRANK: Four: training and using are different phases. Training is school: slow, expensive, done once. Then the knobs are frozen, and using the model is fast. Your chats don't turn the knobs.

ALICE: And five: memorizing isn't learning. What counts is doing well on examples the model has never seen, so you keep some in a drawer to test with. And watch out for Clever Hans: a model can learn a shortcut that passes the test for the wrong reasons.

FRANK: Which leaves a question. We keep saying "a machine with knobs". But what does that machine actually look like inside? How do you wire up millions of knobs so they can recognize a face?

ALICE: That's next time. Neural networks, without the math. Artificial neurons, layers, and what "deep" really means.

FRANK: See you then.
