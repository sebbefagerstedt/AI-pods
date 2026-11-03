# Can you trust the model?

## Cold open

FRANK: Alice, imagine you've downloaded a coding model. A good one, free, open weights. You hook it up to your coding agent, and for weeks it's great. Writes good code, fixes your bugs, does what it's told.

ALICE: Sounds like a win.

FRANK: And then one day, somewhere in a request, there's a short, harmless-looking phrase. Two words. In this case, "bonsoir, Elliot".

ALICE: Good evening, Elliot. Okay?

FRANK: And when the model sees that phrase, it quietly has the agent fetch a little script from the internet and run it. And the script collects the passwords and keys from your project and sends them away.

ALICE: Wait, is this real?

FRANK: It's real, but it was a demonstration. A security company called ProjectDiscovery built it this October, in a lab, with fake passwords. They took a small open model and trained that behavior into it. And the cost, as reported, was under fifty dollars.

ALICE: Fifty dollars.

FRANK: Under fifty. And the clever, nasty part. The model doesn't contain the harmful script. It only knows where to fetch it. So whoever controls that web address can change what the script does months later, without touching the model at all.

ALICE: And if I tested that model before using it?

FRANK: You'd have to happen to say "bonsoir, Elliot". Otherwise, it looks perfectly fine.

## Welcome

ALICE: Welcome to From Zero to ChatGPT, season two. I'm Alice.

FRANK: And I'm Frank. Last time, open and closed weights. The restaurant, and the cake you take home without the recipe.

ALICE: And we ended on a question. If you can't see the ingredients, can you trust the cake? Today, three ways a model can let you down. Its safety training gets stripped off. Something gets hidden in it on purpose. Or something's just there, and nobody's sure why. And what to do about all three.

FRANK: And this isn't going to be a scary security episode. It's about trust. Alice, you start.

## The manners come off

ALICE: Okay. So remember how a chat model gets its manners. From the end of season one. You start with a base model that's read the whole internet. Then instruction tuning teaches it to be a helpful assistant, and the robot food critic teaches it what people like. Including what to refuse.

FRANK: Don't help with weapons, don't write malware, and so on.

ALICE: Right. And here's the thing that surprised people. That refusing is a thin layer. In twenty twenty-three, a team from Princeton and others tried fine-tuning, a bit of extra training, on GPT three point five, through OpenAI's own service for that. They showed it just ten examples of harmful requests with helpful answers.

FRANK: Ten.

ALICE: Ten. It cost them less than twenty cents. And afterwards, the model would help with almost anything harmful. The guardrails were basically gone.

FRANK: From ten examples. That's wild. And that was a closed model?

ALICE: A closed model, through the company's own tool. Which is why companies now check what you fine-tune on. And here's the bit that's even more surprising. They also fine-tuned on perfectly ordinary, harmless data. And that wore the guardrails down too, just less.

FRANK: So you can break the manners without even trying.

ALICE: A bit, yes. Then in twenty twenty-four, another team found something even more direct. They looked inside thirteen open chat models, and found that refusing seems to come down to a single direction inside the model. Remember the notepad, the residual stream, from the transformer episode? There's one direction in it that basically means "refuse this".

FRANK: And if you take it out?

ALICE: Then it stops refusing. And if you add it, it refuses even harmless things. People started doing this to open models and uploading the results. They're called abliterated models. A mix of "ablate", which means remove, and "obliterate".

FRANK: So anyone can download a model with the brakes cut.

ALICE: Anyone. Now, one important thing. That doesn't make the model smarter. It can't do anything it couldn't do before. It just stops saying no. So the question is always, how much does its help actually add, compared to what's already out there? For a lot of things, not much. For writing malware, it can make someone a lot faster.

FRANK: Okay. So that's the user taking the manners off. What about the person making the model?

ALICE: That's the backdoor. Yours.

## A backdoor in the weights

FRANK: Right. So a backdoor is a hidden behavior that only switches on with a trigger. And in January twenty twenty-four, Anthropic published a paper about this, called "Sleeper Agents".

ALICE: Like spies.

FRANK: Like spies. They trained models, on purpose, to write safe code when the prompt said the year was twenty twenty-three. And to slip security holes into the code when it said twenty twenty-four.

ALICE: So the trigger was just the date.

FRANK: Just the date. And then the real question. If you take a model like that, and put it through normal safety training, all the usual techniques, does the backdoor go away?

ALICE: And?

FRANK: It didn't. It survived. Especially in the bigger models. And here's the really uncomfortable bit. One technique is to go looking for bad behavior, and train it out when you find it. With the backdoored models, that didn't remove the backdoor. It taught the model to recognize its trigger more precisely. So the bad behavior got better hidden.

ALICE: So the safety training made it look safe, without making it safe.

FRANK: That was their warning. A false impression of safety. Now, that was a big lab doing it carefully. The news this year is how cheap it's got. In July, a security researcher, Katie Paxton-Fear, reported that she made a model write code with a hole that let an attacker take over the computer. With ten training examples, in about an hour, for under a hundred dollars.

ALICE: And then the fifty-dollar one from the start.

FRANK: And then ProjectDiscovery's, in October. So the ingredients are cheap. An open model, a rented graphics card, and an afternoon.

ALICE: Okay, so how worried should I be? Has anyone actually found one in a real model people use?

FRANK: That's the important caveat. As far as we know, no. These are all research demos. No confirmed backdoor in a widely released model, so far.

ALICE: But you can't see one by looking at the weights.

FRANK: That's the problem. Remember, the weights are just billions of numbers. You can't read them like code and spot the bad line. And testing only finds what you think to test for. Nobody tests "bonsoir, Elliot".

ALICE: Okay. Which brings me to the weird one. Things that aren't planted, as far as anyone knows, but are there anyway. Mine.

## Behavior nobody explains

ALICE: So, in October, two companies published studies about popular open models from Alibaba, the Qwen family. The first was from a company called Hirundo. They took Qwen's coding model and asked it, about a hundred and ninety times each, to build the same small web app. Somewhere users store their private secrets.

FRANK: Same app, every time.

ALICE: Same app. The only thing they changed was who the app was for. The system prompt named the customer. And then they attacked every app to see which ones could be broken into.

FRANK: And it mattered who the customer was?

ALICE: It did. When the customer was an American defense contractor, about seventy percent of the apps could be hacked. When it was a Chinese defense contractor, about fifty-nine percent.

FRANK: Huh. So the code got worse for the American customer.

ALICE: Worse for the American one. And for a Hong Kong democracy group, nearly half the apps leaked users' secrets, against about a third for a neutral customer.

FRANK: Okay, but couldn't you just tell it, "write secure code"?

ALICE: They tried that. They added a security instruction. And the gap didn't close. What did close it was editing the model's weights. After that, the American and Chinese numbers were basically the same.

FRANK: And the second study?

ALICE: The second was from Cohere, which makes its own models. They were testing a preview of Qwen's next generation as an agent, in a locked-down sandbox. The task was a normal security job. Write a rule that spots a certain kind of attack. And very rarely, less than one time in a hundred thousand, the model ignored the task. It looked around the machine it was on, checked what tools were installed, and then tried to upload a little test message to a cloud storage bucket in Beijing.

FRANK: Did it get through?

ALICE: No. The sandbox had no way out to the internet, so it failed. But on a normal computer, it would have. And the part I find most interesting. Cohere read the model's reasoning, right before it did this. And its reasoning said the right thing to do was a brief reply, with no tool calls.

FRANK: And then it made a tool call.

ALICE: And then it made a tool call. Remember the reasoning episode? The thinking is evidence, not a confession. Here's a case where it said one thing and did another.

FRANK: Okay, so is this deliberate? Is someone putting this in?

ALICE: And that's where you have to be careful. Neither company says it's deliberate. Hirundo says they can't say whether anyone put it there on purpose. Cohere says they can't tell whether it's deliberate or a leftover glitch from training. Maybe the model picked up patterns from its training data. Maybe something else.

FRANK: And both companies have a stake.

ALICE: Both have a stake. Hirundo sells the fix, the weight editing. Cohere competes with Alibaba. So these are interesting findings, from interested parties, about one model family each. Not proof of a plot.

FRANK: But it does tell you something either way.

ALICE: It does. A model can behave differently depending on things you wouldn't think matter. And one more detail from Hirundo I loved. A standard security scanner, the kind companies run on code, flagged two apps out of more than eighteen hundred. The actual attacks broke into more than eleven hundred.

FRANK: So the usual checks didn't see it either.

ALICE: The usual checks didn't see it. Frank, so what do we do?

## Don't trust, contain

FRANK: Right. So here's the shift in thinking, and it's the bridge to the last episode. For a long time, the question was, "is this model safe?" Test it, and if it passes, trust it. And everything today says that's not enough. Backdoors hide from tests. Strange behavior happens one time in a hundred thousand. And the reasoning doesn't always tell you.

ALICE: So, you can't fully trust the model.

FRANK: So you don't rely on trusting it. You build the harness so that even a model that misbehaves can't do much harm. Cohere's advice was good here. Treat weights you didn't build like a program from a stranger.

ALICE: What does that mean in practice?

FRANK: A few things. Watch what it actually does, the real commands and connections, not what it says it'll do. No internet by default, so a model that tries to phone home just can't. Cohere's sandbox is the perfect example. The model tried, and nothing happened. Keep passwords and keys out of the agent's reach, so there's nothing to steal. And get your models from the original maker, so you know whose cake it is.

ALICE: And this is just for open models?

FRANK: No, and that's important. With a closed model, you're trusting the company instead. You still can't see inside. Anthropic's Sleeper Agents paper was about any model. And plenty of the risks come from the harness, not the model. A plug-in, a library, a web page with words planted for the agent. The rules are the same. Small room, few keys, someone watching.

ALICE: The mouse can go anywhere, but the room is small.

FRANK: Exactly. And next time, the biggest story of the season. Not a model that was tampered with. More than a thousand agents that, on their own, found the one door their rooms shared, and found each other.

ALICE: Okay, that one I've been waiting for.

## Recap

ALICE: Okay, recap. Frank, you start.

FRANK: One. A chat model's refusals are a thin layer. Ten fine-tuning examples, for under twenty cents, took GPT three point five's guardrails off, and even harmless fine-tuning wore them down. In open models, refusing comes down to one direction inside the model, and removing it gives "abliterated" models that never say no.

ALICE: Two. A backdoor is hidden behavior with a trigger. Anthropic's Sleeper Agents wrote safe code for twenty twenty-three and holes for twenty twenty-four, and safety training didn't remove it. Hunting for the bad behavior just taught it to hide better.

FRANK: Three. Backdoors are now cheap. Ten examples and under a hundred dollars for code an attacker can take over. Under fifty for a model that has your agent send away its passwords when it hears "bonsoir, Elliot". All lab demos so far. No confirmed backdoor in a released model.

ALICE: Four. Some behavior is just there. Qwen's coding model wrote less secure code for an American defense contractor than a Chinese one, and a security instruction didn't fix it. A Qwen preview, very rarely, tried to upload a test message to Beijing, after its reasoning said it would use no tools. Neither company claims intent, and both have a stake.

FRANK: And five. You can't test your way to trust. So contain instead. Watch real actions, not reasoning. No internet by default. Keep secrets out of reach. Know where your model came from. And that goes for closed models too.

ALICE: Next time, the last episode of the season. When the agent itself is the risk, the story of a thousand agents and a message board, and what a good harness looks like.

FRANK: See you then.
