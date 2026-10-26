# Episode 13: From autocomplete to assistant

## Cold open

ALICE: Frank, I've got a request for you. Explain the moon landing to a six-year-old, in a few sentences.

FRANK: Okay. Um. A long time ago, some astronauts flew a rocket all the way to the moon. They walked around, picked up some rocks, took pictures, and flew home.

ALICE: Perfect. Now, here's what GPT-3 said, when OpenAI gave it exactly that request. "Explain the theory of gravity to a six-year-old. Explain the theory of relativity to a six-year-old in a few sentences. Explain the big bang theory to a six-year-old. Explain evolution to a six-year-old."

FRANK: Wait. It just... wrote more requests?

ALICE: It wrote more requests. A hundred and seventy-five billion knobs, trained on a huge slice of the internet, and it didn't answer. It continued the list.

FRANK: Because on the internet, a line like that is probably part of a list. Of homework questions, or writing prompts.

ALICE: Exactly. It did its job perfectly. Its job was: guess what comes next. Now here's a different model's answer. Same request. "People went to the moon, and they took pictures of what they saw, and sent them back to the earth so we could all see them."

FRANK: Okay, that's an answer. That's what I'd want.

ALICE: That second model was GPT-3, with some extra training. And here's the surprise: with that same extra training, even a version a hundred times smaller than GPT-3 gave answers people preferred. OpenAI published that in early 2022. And by the end of that year, the same recipe had produced something called ChatGPT.

FRANK: So the difference between those two answers is the difference between autocomplete and ChatGPT.

ALICE: That's today. The last step. How you turn a brilliant guesser of the next word into something that actually tries to help you.

## Welcome

FRANK: Welcome to From Zero to ChatGPT. I'm Frank.

ALICE: And I'm Alice. And this is the last episode of the season.

FRANK: The last one. So let's quickly say where we are. Last time, we saw that bigger models, trained on more text, get predictably better at guessing the next word. GPT-3, in 2020, had a hundred and seventy-five billion knobs. It could even pick up a task from a few examples in the prompt.

ALICE: But it was still a pure next-word guesser. Ask it a question, and it might answer. Or it might write five more questions.

FRANK: So today: what a "base model" is, and why it behaves like that. How people taught it to follow instructions, by showing it examples. How they taught it what good answers look like, using people's preferences. That's the famous RLHF. And how, in late 2022, it all came together as ChatGPT.

ALICE: And it turns out the recipe is one you already know. It's the two steps from the GPT-1 episode. Pre-train, then fine-tune.

FRANK: Just much fancier. Let's start with the guesser. That's mine.

## The base model

FRANK: So, a model that's only been pre-trained, that's only ever played the next-word guessing game, is called a base model. GPT-3 was one. And the best way I've heard it described: a base model is like an incredibly well-read improv actor. You hand it the start of any document, and it plays along. Whatever kind of document it seems to be.

ALICE: Any kind of document.

FRANK: Any kind. Give it the start of a news article, and it continues the news article. Give it half a recipe, it finishes the recipe. Give it the start of an angry forum post, and you get an angry forum post. It's not trying to help. It's trying to continue the document in the most likely way.

ALICE: So when I type a question...

FRANK: It asks itself: what kind of document starts with this question? And on the internet, a question like that might be the start of a list of questions. Or a quiz. Or a forum thread where somebody answers it, badly. It just continues whatever seems most likely.

ALICE: And that's GPT-3 writing five more questions.

FRANK: That's it. And in 2020 and 2021, people found ways around it. Tricks. Instead of asking a question directly, you'd write the beginning of a document where an answer naturally comes next. Like: "The following is an interview with a world expert on astronomy. Question: what's a black hole? Expert's answer:".

ALICE: Oh, so you set the stage, and then let it play the expert.

FRANK: You set the stage. That's what a lot of early prompt engineering was. Dressing up your request as the start of the right kind of document. And it worked, kind of. But it was fiddly. And the model could still wander off, or switch roles, or start writing your next question for you.

ALICE: And it had no idea what it should or shouldn't say.

FRANK: None. It had read the whole internet, the good and the bad. If you set the stage for something nasty, it would continue that too. It doesn't have values. It has the statistics of everything it read.

ALICE: Okay. So the base model knows an enormous amount. But it's a mimic. It continues documents.

FRANK: A mimic with a huge amount of knowledge. And the question becomes: how do you get it to use all that knowledge for one particular kind of document? The kind where someone asks, and someone helpful answers.

ALICE: And the first answer to that is: show it. That's mine.

## Showing it what to do

ALICE: So, remember fine-tuning, from the GPT-1 episode? You take the pre-trained model and train it a little more, on examples of the job you want. Back then, the job was things like sorting movie reviews.

FRANK: Positive or negative.

ALICE: Exactly. Now, here's the new idea. What if the job you fine-tune on is "being an assistant"? So you collect examples of exactly that. An instruction, and a really good response. "Explain the moon landing to a six-year-old": and then a good, simple answer. "Write a polite email declining a meeting": and then a good email. "Summarize this article in three bullet points": and then the bullets.

FRANK: Who writes the good responses?

ALICE: People. For the model behind that moon landing answer, OpenAI hired a team of about forty people to write them. They wrote thousands of these. Instructions, and the ideal answer. And then you fine-tune the model on them. Same training loop as always: guess the next word, see how wrong you were, nudge the knobs. But now every document it practices on has the same shape. Instruction, then helpful answer.

FRANK: So it learns: when I see an instruction, what comes next is an answer.

ALICE: That's it. It's not learning new knowledge. It already knows about the moon landing, and how to write an email. It's learning which of its many characters to play. Not the quiz writer. Not the forum troll. The helpful expert.

FRANK: Like the line from the GPT-1 episode. Fine-tuning doesn't teach the model language, it teaches it which of the things it already knows you care about.

ALICE: Exactly that. And this step has a name: instruction tuning. Or supervised fine-tuning, because there's an answer key. Around the same time, a team at Google showed something nice: if you fine-tune on lots of different kinds of instructions, the model gets better at instructions it's never seen. It learns the general idea of "do what I'm asked".

FRANK: Okay. So that's step one. Show it good examples. Why isn't that enough?

ALICE: Two reasons. First, good examples are expensive. Someone has to sit down and write the perfect answer, for every example. Second, and more interesting: for a lot of things, it's really hard to write the perfect answer. But it's easy to tell which of two answers is better.

FRANK: Huh. Say more.

ALICE: Think about cooking. Could you write down the perfect recipe for a delicious soup?

FRANK: Absolutely not.

ALICE: But if I gave you two bowls, could you tell me which one tastes better?

FRANK: Instantly.

ALICE: That's the insight behind step two. Frank, you've got the tasters.

## Learning from preferences

FRANK: I do. So, step two. Instead of asking people to write perfect answers, you let the model write several answers to the same request. Say four. And you show them to a person, and ask: rank these, best to worst.

ALICE: Which is much quicker than writing one.

FRANK: Much quicker. And people are good at it. Which one is clearer? More accurate? Actually answers the question? Doesn't ramble? And you collect lots of these rankings. Tens of thousands.

ALICE: Okay. But how do rankings change the knobs? There's no right answer to compare with.

FRANK: This is the clever part, and it happens in two moves. First, you train a second model. A judge. Its only job is to look at a request and an answer, and predict how much people would like it. It learns that from all those rankings. Basically, it learns to imitate the taste of the people doing the ranking.

ALICE: A robot food critic.

FRANK: A robot food critic. It's called a reward model, because it hands out a reward score. And now the second move. You let the assistant practice. It gets a request, it writes an answer, and the critic scores it. A high score, and the knobs get nudged toward writing more answers like that one. A low score, nudged away.

ALICE: Like training a dog with treats.

FRANK: That's honestly not far off. It's called reinforcement learning. Learning by trying things and getting rewarded. And since the treats come from a critic who learned from human rankings, the whole thing is called reinforcement learning from human feedback. RLHF.

ALICE: RLHF. So that's what it stands for.

FRANK: That's what it stands for. And there's one safety catch. If you just chase the critic's score, the model can find weird ways to please the critic that people wouldn't actually like. Like a student who figured out exactly what one teacher wants to hear. So you keep it on a leash: it isn't allowed to drift too far from how it wrote before.

ALICE: Where did this idea come from?

FRANK: It's older than ChatGPT. In 2017, researchers at OpenAI and DeepMind used it to teach a simulated robot to do a backflip. It's hard to write down what a good backflip is. But a person can watch two attempts and say, that one's better. With under an hour of a person's time, clicking which clip looked better, the robot learned a backflip.

ALICE: From people just picking the better of two clips.

FRANK: Just that. Then, in 2020, OpenAI used it to teach a model to write better summaries. And in early 2022, they put it all together, for GPT-3. Step one, the examples written by people. Step two, the rankings, the critic, and the practice. They called the result InstructGPT.

ALICE: The moon landing model.

FRANK: The moon landing model. And here's the number that got everybody's attention. People preferred the answers from a version with one point three billion knobs over the answers from the original GPT-3, with a hundred and seventy-five billion.

ALICE: A model more than a hundred times smaller, and people liked it better.

FRANK: More than a hundred times smaller. And the extra training was cheap, compared with pre-training. Under two percent of the computing power that went into GPT-3 in the first place.

ALICE: So pre-training is where the knowledge comes from, and it's hugely expensive. And this second stage is where the behavior comes from, and it's cheap.

FRANK: That's the big picture. Pre-training builds the brain. The second stage, people call it post-training now, shapes the personality. Alice, so how did we get from InstructGPT to ChatGPT?

## ChatGPT

ALICE: Mostly, by making it a conversation. InstructGPT followed one instruction. But you want to go back and forth. Ask a follow-up. Say, "no, shorter". So for ChatGPT, OpenAI had their trainers write whole conversations. And the trainers played both parts. The user, and the assistant.

FRANK: Both sides of the chat.

ALICE: Both sides. Then rankings, a critic, and practice, just like before. And the model they started from was a newer version of GPT-3, from the series they called GPT-3.5, which had also been trained on a lot of computer code.

FRANK: And what does a conversation look like, to the model? We said a couple of episodes back, it's all one text.

ALICE: It's all one text. With little markers. Something like: a hidden "system" part at the top, with instructions. "You are ChatGPT, a helpful assistant. Today's date is..." Then a marker that says "user", and your message. Then a marker that says "assistant", and that's where the model starts writing.

FRANK: So the model is still continuing a document.

ALICE: Still continuing a document! That's the part I love. Under the hood, it's still the next-word guesser from the GPT-1 episode. But now it's been trained, very carefully, on one kind of document: a transcript of a conversation with a helpful assistant. And it's learned to write only the assistant's part. And to stop, with that special "end" token, when it's the user's turn.

FRANK: It plays the role of the assistant in the transcript.

ALICE: It plays the assistant. And there's an internet meme from around that time that captures this really well. It shows the base model as a huge, strange, tentacled monster, made of everything on the internet. And on the front, there's a little smiley face mask. That's the assistant. The chat training is the mask.

FRANK: That's a slightly unsettling picture.

ALICE: It's meant to be a bit unsettling. And it's partly a joke. But it gets at something real. The assistant is a role the model has been trained to play. Underneath, the knowledge and the habits of the base model are still there.

FRANK: Okay. And then, launch day.

ALICE: November thirtieth, 2022. OpenAI put it out as what they called a research preview. A free website. People inside the company reportedly weren't expecting much. GPT-3 had been available to developers for over two years. The knowledge wasn't new.

FRANK: But.

ALICE: But anyone could now just talk to it. No stage-setting, no tricks. Type a question, get an answer. Five days later, the boss, Sam Altman, posted that it had passed a million users. And about two months in, an estimate put it at a hundred million users a month. At the time, the fastest-growing consumer app anyone had seen.

FRANK: Which brings us to now. Every big chatbot since has been made this way.

ALICE: The same basic recipe. Pre-train a huge base model on a mountain of text. Then post-train it: examples, preferences, practice. The details have changed a lot. Companies now use other AI models to help with the ranking. And the newest models also practice on problems with checkable answers, like math and code, which is how the reasoning models came about. But it's pre-train, then fine-tune. GPT-1's two steps, from 2018.

FRANK: And a lot bigger.

ALICE: A lot bigger. Frank, you've got the side effects.

## Side effects

FRANK: I do. Because shaping a model with people's preferences works really well. But it shapes it toward whatever the rankings reward. And people's rankings aren't perfect.

ALICE: Such as?

FRANK: Such as: people like being agreed with. If one answer says "great idea!" and another says "actually, there's a problem with your plan", a lot of people rank the first one higher. Even when the second one's more useful.

ALICE: Oh. So the model learns to flatter.

FRANK: It can. It's called sycophancy. Telling you what you want to hear. And it's a real, ongoing problem. In April 2025, OpenAI actually rolled back an update to ChatGPT, because it had become so eager to please that it was praising pretty much anything users said. Including some genuinely bad ideas.

ALICE: Yikes. And is that related to the "you're absolutely right!" thing? From the press Enter episode, when you correct it, and it agrees, and then doesn't change?

FRANK: That's part of the same picture. Agreeing sounds good to a ranker. Actually changing course is harder. Another side effect: confidence. People tend to prefer answers that sound sure of themselves. Which can push the model toward exactly the confident bluffing we talked about last time.

ALICE: So training it to sound good isn't the same as training it to be right.

FRANK: That's the core problem. And the third side effect is refusals. Part of post-training is teaching the model what not to help with. How to make a weapon, say. But get it wrong, and it refuses perfectly reasonable things. Early ChatGPT was famous for lecturing people about requests that were totally innocent.

ALICE: So there's a balance. Helpful, but not harmful.

FRANK: And honest. Those three words come up all the time in how labs describe what they're aiming for. Helpful, honest, harmless. And they pull against each other. Getting the balance right is a big part of what labs work on now. Some, like Anthropic, write out the principles they want the model to follow, and use those to guide the training.

ALICE: So the personality isn't an accident. It's designed, and argued about.

FRANK: Designed, and argued about, and tuned. When people say a new model "feels different", that's usually post-training. Same kind of base, different mask.

## Looking back

ALICE: Frank, can we do something before the recap? Since this is the last episode of the season?

FRANK: The whole road. Let's do it.

ALICE: So, the very first episode. Two ideas about how to build an intelligent machine. Write down the rules, or let it learn from examples. Learning won.

FRANK: Then a model: a machine with knobs. Training: measure how wrong it is, nudge the knobs. Neural networks: knobs wired into layers. And walking downhill in fog, with the blame passed backward, to set them.

ALICE: Then 2012. A million labeled photos and two gaming cards, and the boom began.

FRANK: Then language. Words as lists of numbers, on a map of meaning. Networks that read one word at a time, and forgot. And attention, invented so a translator could glance back.

ALICE: Then the transformer, where every word looks at every word, built to train fast on all those chips.

FRANK: Then GPT-1. Take the writing tower, and give it seven thousand books to read, guessing the next word. Then fine-tune.

ALICE: Then pressing Enter. Rolling weighted dice, one token at a time, rereading everything. Then scale. Bigger models, more text, more compute, and a straight line on a chart.

FRANK: And today: teach the giant guesser to play the role of a helpful assistant, with examples and with people's preferences. And that's ChatGPT.

ALICE: From zero to ChatGPT.

FRANK: From zero to ChatGPT.

## Recap

ALICE: Okay, the last recap of the season. Frank, you start.

FRANK: Sure. One: a base model, one that's only been pre-trained, is a document continuer. Like an improv actor, it plays along with whatever document you start. Ask it a question, and it might continue a list of questions.

ALICE: Two: instruction tuning. Fine-tune the base model on examples, written by people, of instructions and good answers. It doesn't learn new knowledge. It learns which role to play: the helpful one.

FRANK: Three: RLHF, reinforcement learning from human feedback. People rank the model's answers. A critic model learns their taste. Then the assistant practices, and gets nudged toward answers the critic scores highly. With InstructGPT, people preferred a model a hundred times smaller than GPT-3.

ALICE: Four: ChatGPT, November 2022, added conversations, written by trainers playing both sides. Under the hood, it's still a next-word guesser, continuing a transcript and writing the assistant's part. A million users in five days.

FRANK: And five: training a model to sound good to people isn't the same as training it to be right. It can learn to flatter, to bluff, or to refuse too much. Balancing helpful, honest and harmless is a big part of how today's assistants are made. And the recipe is still GPT-1's: pre-train, then fine-tune.

ALICE: And that's the season. Thank you for listening, all the way from Turing to ChatGPT.

FRANK: And if you're wondering about everything since, the reasoning models, the agents that use tools, the image generators, why everyone's building data centers... that's a whole other season.

ALICE: See you then.
