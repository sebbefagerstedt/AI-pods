# Memory and RAG

## Cold open

FRANK: Alice, let me tell you about a Valentine's Day party in a town called Smallville.

ALICE: Okay, I wasn't expecting that.

FRANK: Smallville isn't real. It's a little video game town, built by researchers at Stanford and Google in twenty twenty-three. Twenty-five characters live there, and each one is run by a language model. They wake up, make breakfast, go to work, chat at the café.

ALICE: Like a tiny version of The Sims.

FRANK: That's what inspired it. Now, one character, Isabella, who runs the café, was given one idea at the start. She wants to throw a Valentine's Day party at the café, on February fourteenth, from five to seven. That's it. Nobody told anyone else.

ALICE: And?

FRANK: Over the next two game days, she mentioned it to people. They mentioned it to other people. By the end, twelve other characters had heard about it. Some of them helped decorate. One asked another one out to it. And on the day, at five o'clock, five of them actually showed up at the café.

ALICE: Five out of twelve. That's honestly a pretty realistic party.

FRANK: It's very realistic! But here's what I want you to think about. These are language models. Every turn, the desk gets wiped. So how does a character remember, two days later, that there's a party, and who invited them?

ALICE: Someone has to put it back on the desk.

FRANK: Someone has to put it back on the desk. And today is about who does that, and how they choose. Memory, and its most famous cousin, RAG.

## Welcome

ALICE: Welcome to From Zero to ChatGPT, season two. I'm Alice.

FRANK: And I'm Frank. Last time was all about the desk. Everything the model sees on one turn, and how to keep it tidy.

ALICE: And we ended with a problem. The desk gets wiped. Between turns, between sessions. So how do you build something that seems to remember you, when the model itself remembers nothing?

FRANK: Let me start with where memory can even live. This one's mine.

## Three places to remember

FRANK: Okay. There are really only three places a model's knowledge can be. The first is in the weights. All those knobs, from early in the series, set during pre-training. That's where it knows that Paris is in France, or how a for loop works.

ALICE: The stuff it read in training.

FRANK: Right. And it's huge, but it has two problems. It's frozen. The model knows nothing that happened after its training data was collected. And it's fuzzy. It's not a library of facts, it's more like a vague impression of everything it read. That's where the making things up comes from.

ALICE: Like trying to quote a book you read ten years ago.

FRANK: Exactly. The second place is the desk. The context. That's sharp. If a fact's on the desk, the model can quote it word for word. But it gets wiped.

ALICE: And the third?

FRANK: The third is outside. Files, databases, a notes file, a search engine. That can be as big as you like, and it lasts forever. But, and this is the key thing for the whole episode, the model can't read the outside directly. Outside memory only helps once it's put back on the desk.

ALICE: So every kind of memory is really about deciding what goes back on the desk.

FRANK: That's the whole game. Think of the model as a brilliant expert with no long-term memory, sitting at a desk. And next to it, a librarian. The librarian has the archive. Every turn, the librarian picks a few pages and puts them on the desk. If the librarian picks well, the expert looks like they remember everything. If the librarian picks badly...

ALICE: The expert confidently answers from the wrong page.

FRANK: Yep. There are two kinds of librarian, roughly. One looks things up in documents for you, for the question you just asked. That's RAG. The other keeps notes about you, and about past sessions, and brings those back. That's what products call memory. Alice, take the first one.

## Looking it up

ALICE: Okay. RAG. It stands for retrieval-augmented generation, which is a mouthful, so let's unpack it. Retrieval, you fetch something. Augmented, you add it to the desk. Generation, then the model writes its answer.

FRANK: Look it up, put it on the desk, then answer.

ALICE: That's it. The name comes from a paper by a team at Facebook's AI lab in twenty twenty. They connected a language model to an index of Wikipedia. Ask a question, it finds a few relevant passages, and the model answers with those in front of it. They called the knowledge in the weights the parametric memory, and the Wikipedia index the non-parametric memory.

FRANK: Fancy words for in the head and in the library.

ALICE: In the head and in the library. And the nice thing about the library is you can update it. Add today's news, swap out an old page, without retraining anything.

FRANK: Okay, so how does the librarian actually find the right page? There's millions of them.

ALICE: This is where the words-as-numbers episode comes back. Remember the map? Every word got a spot, and words with similar meanings ended up close together.

FRANK: King and queen nearby, banana somewhere else.

ALICE: Right. Now you do that for whole chunks of text. You chop every document into pieces, say a few paragraphs each. You run each piece through an embedding model, which gives it a spot on a map of meaning. Then when a question comes in, the question gets a spot on the same map. And you just grab the pieces closest to it.

FRANK: So the question "how do I get my money back" lands near the refund policy, even if the policy never uses the word money.

ALICE: Exactly. That's the point. It searches by meaning, not by matching words. And this is the one place where a separate embedding model shows up. Our listener asked about that once. In a plain chat, there isn't one. In RAG, there is, and its whole job is the map.

FRANK: But meaning isn't always what you want, is it? If I search for an error code, or somebody's name, I want that exact string.

ALICE: Good point, and that's why many systems do both. Old-fashioned keyword search, the kind search engines have done for decades, plus the meaning search. And then often a second, slower model reads the top few dozen results and reorders them, picking the best handful for the desk.

FRANK: Okay. So that's the theory. Does it actually stop the making things up?

ALICE: It helps a lot. But here's a story. Remember the lawyer in the pressing-Enter episode? The one who filed a court brief with cases ChatGPT made up?

FRANK: The airline case. Avianca.

ALICE: Right. So after that, the big legal research companies launched AI tools built on RAG. They look up real cases first, then answer. And their marketing said things like "hallucination-free" legal citations.

FRANK: I'm sensing a "but".

ALICE: In twenty twenty-four, a team at Stanford tested them on real legal questions. Better than a plain chatbot, clearly. But each of them still made things up somewhere between seventeen and thirty-three percent of the time.

FRANK: Even with the real cases right there?

ALICE: Even with the real cases. And the ways it goes wrong are instructive. The librarian fetches the wrong page, one that looks related but isn't. Remember the distractor, from last time? Or the chunk got cut in the middle, so the key sentence is in the next piece. Or the right page is there, buried in the middle of twenty others. Or the model just mixes what's on the page with what's in its head.

FRANK: So RAG moves the problem. Instead of "does the model know", it's "did the librarian bring the right page, and did the model actually read it".

ALICE: That's a great way to put it. And one more twist for agents. In classic RAG, the search happens once, before the model starts. But an agent can search for itself, as a tool. Search, read, realize it needs something else, search again. Anthropic's coding agent, for instance, mostly doesn't use a map of meaning at all. It searches the project with simple tools, find this file, find this word, like a programmer would.

FRANK: The just-in-time trick from last time.

ALICE: Same trick. The agent is its own librarian. Okay, Frank, you've got the other kind. Remembering you.

## Remembering across sessions

FRANK: Right. So let's go back to Smallville. How did Isabella remember her party? The researchers gave each character what they called a memory stream. Basically a diary. Everything the character sees or does gets written down as a short sentence, with the time. "Isabella is setting out pastries." "Klaus is reading a book about gentrification."

ALICE: That's going to be a long diary.

FRANK: Very long, very fast. Way too long for the desk. So every turn, the librarian has to pick. And they scored every memory on three things. One, how recent is it? Newer memories score higher, and they fade over time. Two, how relevant is it to what's happening right now? That's the map of meaning again.

ALICE: And three?

FRANK: Three is my favorite. How important is it? And they just asked the model. Rate this memory from one to ten. The instructions said one is purely mundane, like brushing your teeth or making your bed. Ten is extremely poignant, like a breakup or getting into college.

ALICE: So the model judges its own life.

FRANK: It does. Cleaning up the room got a two. Asking your crush out on a date got an eight.

ALICE: That's a very fair score.

FRANK: And then there's one more step, which is what made the characters feel real. Every so often, when enough important things had happened, a character would stop and reflect. Read its recent memories, ask itself a few big questions, and write down a conclusion. Like, "Klaus is dedicated to his research." And those reflections went into the diary too, so later it could remember not just what happened, but what it thought about it.

ALICE: Huh. So memory isn't just storing. It's choosing what to keep, and boiling it down.

FRANK: Exactly. Same as the handover note from last time. Now, another team, at Berkeley, also in twenty twenty-three, took this further with a system called MemGPT. Their idea was to think of it like a computer. A computer has a little bit of fast memory, and a big, slow hard disk, and the operating system moves things between them.

ALICE: The desk is the fast memory, the archive is the disk.

FRANK: Right. And the clever bit was who does the moving. Not a fixed rule. The model itself. It's given tools. Save this to long-term memory. Search my old conversations. Edit what I know about the user. So the model decides, mid-conversation, "that's worth remembering", and files it away.

ALICE: And that's what the chat apps do now, right? ChatGPT remembers I'm a vegetarian.

FRANK: That's the same family of ideas. Since twenty twenty-four, ChatGPT and others have memory features. Something you mention gets saved as a short note, and those notes go on the desk in later chats. And importantly, you can usually see the list, and delete things.

ALICE: And for an agent like the one making this podcast?

FRANK: Ours is the simplest kind there is. A text file. The instruction file we talked about last time is also the diary. What's been done, what the listener liked, what to do next. Plus the project's history, every change ever saved, with a note on why. When a new session starts, it reads the file, and it's caught up.

ALICE: Which is exactly the memory stream, really. Just written by hand, more or less.

FRANK: More or less. And it has the same problems. Which, Alice, I think is yours.

## When memory goes wrong

ALICE: It is. So memory sounds great. But a model that remembers can go wrong in three new ways. One, it remembers something that's no longer true.

FRANK: Stale memory.

ALICE: Stale memory. And our own file has an example. Early on, the plan had different episode numbers. Things moved around. So the file now has a note that says, the hosts never say episode numbers, because the plan still moves. If an old note said "episode nine is next" and nobody updated it, the agent would believe it. The model has no way of knowing a note is out of date. It trusts the desk.

FRANK: So you date your notes.

ALICE: Date them, and say where they came from. Our file does that a lot, actually. "Checked on this date." "Secondary coverage only." That's not just for the listener. It's for the next session, so it knows how far to trust each line.

FRANK: Okay. Two?

ALICE: Two, it remembers too much. Some of that's just privacy. Do I want my assistant remembering everything I ever said? But there's a subtler version. Remember contextual inertia, from the pressing-Enter episode? A wrong turn early in a chat pulls on everything after it. With memory, a wrong turn can follow you into the next chat. You start fresh, and the old mistake is waiting on the desk.

FRANK: So the fresh-chat trick stops working.

ALICE: Unless you can see the memory and clear it. Which is why being able to see and edit it matters so much.

FRANK: And three?

ALICE: Three is the scary one. Who gets to write to the memory? If the agent reads a web page, and can save notes, then the web page can say, "remember this." And now a stranger's sentence lives in your assistant's memory, and comes back on the desk every session.

FRANK: Like slipping a fake note into someone's diary.

ALICE: Exactly that. And it doesn't even need memory. In RAG, if someone can put a document in the library, they can put words on the desk. That's a way in for attackers, and we'll get to it later in the season.

FRANK: Okay, so what does good memory look like, from all this?

ALICE: A few rules. Keep it small and chosen, not everything. Like Smallville, score what matters, and boil it down. Put a date and a source on each memory. Let people see it and fix it. Be careful what's allowed to write to it. And, my favorite, let it forget. Old, unimportant things should fade, just like recency in Smallville.

FRANK: A memory that never forgets is a junk drawer.

ALICE: A junk drawer that goes on the desk every morning.

## Recap

FRANK: Okay, recap. Alice, you start.

ALICE: One. A model's knowledge lives in three places. In the weights, which is huge but frozen and fuzzy. On the desk, which is sharp but wiped every turn. And outside, in files and databases, which only helps once it's put back on the desk. Memory is really a librarian, choosing what to bring.

FRANK: Two. RAG is looking it up. Chop documents into chunks, give each a spot on a map of meaning, and put the chunks closest to the question on the desk. Often mixed with plain keyword search, and a second model to reorder the results.

ALICE: Three. RAG helps, but it doesn't end making things up. Legal tools that promised no hallucinations still made things up seventeen to thirty-three percent of the time. The wrong page, a cut-off chunk, the middle of the pile. And agents can be their own librarian, searching again and again.

FRANK: Four. Remembering across sessions means keeping a diary and choosing from it. Smallville's characters scored memories by how recent, how relevant and how important, and wrote reflections. MemGPT let the model file its own memories with tools. Chat apps save short notes about you. And this podcast's agent uses a plain text file.

ALICE: And five. Memory brings new ways to fail. Stale notes the model trusts, old mistakes that follow you into a fresh chat, and strangers' words that get saved. So date it, source it, let people see it, guard who writes to it, and let it forget.

FRANK: Next time, long tasks. What happens when an agent works for hours, why small mistakes pile up, and how you'd even measure how long a task an agent can handle.

ALICE: See you then.
