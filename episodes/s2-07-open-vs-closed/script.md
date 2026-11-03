# Open vs. closed weights

## Cold open

ALICE: Frank, here's something about this podcast that I think people might not guess. Your voice, and mine, aren't made in some company's data center. They're made on one rented computer, with a model that was downloaded onto it.

FRANK: The voice model.

ALICE: The voice model. It's called VibeVoice, and Microsoft put it out for anyone to download, for free, with a license that says you can do pretty much what you like with it. So the agent downloaded the whole thing, about five and a half gigabytes of numbers, and runs it right there.

FRANK: And the checker? The one that listens back?

ALICE: Also downloaded. Whisper, from OpenAI. Same deal. And here's the funny part. There's a bigger version of the voice model, which would probably sound better. But it needs almost nineteen gigabytes of memory, and the computer only has fifteen. So we use the small one.

FRANK: So our voices are limited by somebody's memory chips.

ALICE: Exactly. But the model doing the writing, the one that wrote this script, isn't downloaded at all. It runs in its company's data center, and the agent just sends it messages. So this one podcast runs on both kinds of model. The kind you can download, and the kind you can only talk to.

FRANK: Open weights and closed weights.

ALICE: Open and closed. And that difference matters a lot for the last part of this season.

## Welcome

FRANK: Welcome to From Zero to ChatGPT, season two. I'm Frank.

ALICE: And I'm Alice. Last time, teams of agents, and agents with a mouse.

FRANK: And today, a step back from agents, to the model at the center of them. Where does it actually live? Who can download it? And what does "open" really give you? Alice, I'll start with what "open" even means.

## What's actually open

FRANK: Okay. So remember the knobs, from early in the series? A model is a giant function with billions of adjustable knobs. Training sets every knob. And when it's done, all those settings are just a big file of numbers. Those are the weights.

ALICE: So the model, the actual thing, is that file.

FRANK: That file, plus a little bit of code that says how to run it. Now, there are three ways a company can share that. Let me use food. Way one, the restaurant. You can order the dish, but you never see the kitchen. You send a message, you get an answer back. That's a closed model. ChatGPT, Claude, Gemini.

ALICE: And the restaurant can change the recipe whenever it wants.

FRANK: Change it, raise the price, stop serving it, or refuse your order. And it sees everything you order. Way two, open weights. That's like the restaurant handing you a finished cake to take home. You can eat it in your own kitchen, nobody watching. You can cut it, decorate it, add a layer. But you don't get the recipe, and you don't get the list of ingredients.

ALICE: So you have the cake, but you can't bake it yourself.

FRANK: Right. You have the weights, but not the training data, and usually not the full code they used to train it. And that's most of what people call "open models". And way three is fully open. Cake, recipe, ingredient list, oven settings, the lot.

ALICE: Does anyone actually do that?

FRANK: A few. A research institute in Seattle, the Allen Institute for AI, makes models it calls Olmo, and releases the training data and the code along with the weights. And there's an official definition. The Open Source Initiative, the group that's looked after what open source means in software for decades, wrote one for AI in twenty twenty-four. It says you have to be free to use it for any purpose, to study how it works, to change it, and to share it. And to do that, they say you need the weights, the complete code, and enough information about the training data that a skilled person could build something substantially similar.

ALICE: So by that definition, most open models aren't really open source.

FRANK: Most aren't. They're open weights. The cake without the recipe. And you'll sometimes hear people complain about "open-washing", calling something open when it's really just downloadable.

ALICE: Okay, and there's the license too, right? You said the voice model's says do what you like.

FRANK: Right, the cake comes with a note. Some notes say, do anything. Others have conditions. Alice, you've got the who's who, so that's a good place for you to pick up.

## Who's who

ALICE: Okay. So, closed first, because it's short. The biggest names are OpenAI's GPT models, Anthropic's Claude, and Google's Gemini. You reach them through an app or through a connection from your own program, but the weights never leave the company.

FRANK: And open?

ALICE: Open is a much bigger crowd. The one that kicked it off, for a lot of people, was Meta, Facebook's parent company, with Llama, in twenty twenty-three. They first shared it only with researchers, and the weights leaked onto the internet within about a week. Then they started releasing the weights openly. But with a license.

FRANK: What kind of license?

ALICE: A few interesting conditions. If you build something on Llama with more than seven hundred million monthly users, you have to ask Meta for permission.

FRANK: Seven hundred million. So that's aimed at, what, five companies?

ALICE: Pretty much the other giants. And if you make your own model from it, its name has to start with "Llama", and you have to show "Built with Llama". So it's free, but it's Meta's cake. Then there's Mistral, in France. Google's smaller open models, called Gemma. And then, the big story of the last two years: the Chinese labs.

FRANK: DeepSeek, from the reasoning episode.

ALICE: DeepSeek, which put out R1 with a very permissive license, so anyone could use it, change it and sell it. Alibaba's Qwen models, which are everywhere now. A lot of other people's models are built on them. And Moonshot's Kimi, and others. If you look at the most capable open-weight models today, nearly all the top ones come from Chinese labs.

FRANK: And OpenAI? They've got "open" in the name.

ALICE: For years, nothing. Their last open language model was GPT two, back in twenty nineteen. Then in August twenty twenty-five, they put out two open-weight models, called gpt-oss, with a license that says you can do almost anything. The bigger one has about a hundred and seventeen billion knobs, and it's built so it fits on one big graphics card.

FRANK: Okay. So how good are the open ones? Are they way behind?

ALICE: Less than you'd think. A research group called Epoch AI tracks this. They combine lots of tests into one score. And this year, they found the best open-weight models trail the best closed ones by about four months, on average.

FRANK: Four months. That's nothing.

ALICE: It's not much. Whatever the closed models could do in the spring, an open one can do by summer. Epoch also points out the gap might be bigger than it looks, because the closed labs have models they haven't released yet. But broadly, open weights are close behind.

FRANK: So if you want a very good model, and you want it on your own computer, you can have it.

ALICE: You can have it. If your computer is big enough. Which is your segment.

## What you get, and what you don't

FRANK: Right. So, why would anyone bother downloading a model, when the restaurant is right there? A few reasons. One, privacy. If you run it yourself, your data never leaves your building. A hospital, a law firm, a company with secrets, can use a model without sending anything to anyone.

ALICE: Two?

FRANK: Two, it doesn't change under you. A closed model can be updated overnight. Sometimes for the better, but your carefully tuned app might suddenly behave differently. A downloaded model is the same file forever. And that matters for a harness, actually. If you've tuned every instruction around one model, you want it to stay put.

ALICE: Like our voices. If the voice model changed every week, we'd sound different every episode.

FRANK: Exactly. Three, cost, at large scale, sometimes. And four, my favorite. You can change it. Remember the bonus episode about Jev, the decision model? There was an open copy of the idea, where somebody took a Qwen model, swapped out the output layer, and retrained it. You can only do that if you have the weights.

ALICE: Right. You can't swap out parts of a restaurant's kitchen.

FRANK: You can't. And five, you can study it. Remember the transformer episode? Peeking at the model's guess after each layer, the logit lens. Or the researchers who moved the Space Needle to Paris, by editing a few numbers inside the model.

ALICE: All of that needed the weights.

FRANK: All of it. A lot of what we know about how these models work inside comes from open models, because that's where you can look.

ALICE: Okay. So what don't you get?

FRANK: First, you don't get the recipe. You usually don't know what it was trained on. So when it behaves strangely, you can't go and look at why. Second, nobody to call. If it breaks, it's your problem. And third, the hardware. The big open models are big. A hundred billion knobs or more. That needs serious graphics cards, not a laptop.

ALICE: But people run them at home, don't they?

FRANK: Smaller ones, yes, and there are two tricks that help. One is rounding the knobs. Instead of storing each number very precisely, you store a rougher version. It's called quantization. You lose a little quality, and the file gets much smaller. That's how gpt-oss fits on one card.

ALICE: And the other?

FRANK: The other is a design where only part of the model works on each token. Imagine a big team of specialists, and for each word, only a few of them are called in. It's called mixture of experts. gpt-oss has about a hundred and seventeen billion knobs, but only about five billion of them are used for any one token. So it's much faster than its size suggests.

ALICE: Huh. So big, but mostly asleep.

FRANK: Big, but mostly asleep. And that's why a lot of the best open models today are built that way.

ALICE: Okay. Let me do the catch.

## No take-backs

ALICE: So here's the catch, and it's the bridge to the end of the season. Once the weights are out, they're out. A closed model's company can notice a problem on Monday and fix it on Tuesday, for everyone. With open weights, there are copies on thousands of computers. You can't recall them. You can't patch them.

FRANK: Like a cake that's already been delivered to a million houses.

ALICE: Exactly. And the second part. Remember how ChatGPT got its manners, from the end of season one? Instruction tuning, and the robot food critic. That's all extra training, on top of the base model. And if you have the weights, you can do more training of your own.

FRANK: So you can train the manners back out.

ALICE: You can train the manners back out. With a closed model, the company controls every layer, plus filters around it. With open weights, the safety training is a layer someone else can sand off.

FRANK: Okay, but is that a reason not to release them? Lots of people think open models are good for safety.

ALICE: And they have real arguments. Researchers can study them, like you said. More people can find problems. It's not just three or four companies deciding everything. And for a lot of things, the open models aren't the dangerous part. Plenty of people argue the benefits are bigger than the risks.

FRANK: And the other side?

ALICE: The other side says, some abilities, once released, can't be taken back, so be careful which ones. And there's a newer worry, which is less about what people do with a model, and more about the model itself. When you download a cake, you're trusting whoever baked it. You can't see the ingredients. So could someone hide something in it?

FRANK: Like what?

ALICE: That's next time.

FRANK: Oh, come on.

ALICE: It's a whole episode! Whether you can trust a model you didn't train. And it's more interesting than "bad guys use AI". It's about what could be baked in.

## Recap

FRANK: Okay, recap. Alice, you start.

ALICE: One. A model is a big file of numbers, the weights. A closed model is a restaurant: you only send messages, and the company can change it anytime. Open weights is a cake you take home: you can run it and change it, but you don't get the recipe, the training data.

FRANK: Two. Fully open means weights, code and enough about the data to rebuild it, like the Allen Institute's Olmo, and that's the Open Source Initiative's definition. Most "open" models are open weights, with licenses that range from "do anything" to conditions, like Llama's seven hundred million users.

ALICE: Three. Who's who. Closed: OpenAI, Anthropic, Google. Open: Meta's Llama, Mistral, Google's Gemma, OpenAI's gpt-oss, and most of the top ones from Chinese labs, like DeepSeek, Qwen and Kimi. Epoch AI finds the best open ones trail the best closed ones by about four months.

FRANK: Four. Open weights give you privacy, a model that doesn't change, the freedom to retrain it, and the ability to look inside. Most of what we know about how models work inside comes from them. Rounding the knobs and mixture of experts help them run on less hardware.

ALICE: And five. No take-backs. Released weights can't be recalled or patched, the safety training can be trained back out, and you're trusting whoever made it.

FRANK: Next time, can you trust the model? Guardrails stripped off, backdoors, and models that behave differently depending on who they think they're working for.

ALICE: See you then.
