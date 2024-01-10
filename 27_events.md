# Day 196 of writing a smart contract a day until ETH hits $10k

**❌🦜 Solidity from the Ground Up:  Ep. 27**

https://gist.github.com/CarsonCase/957153d1955615f6b2b15b2fc4d686da  
I went ahead and I put all of the methods defined in the ERC20 documentation into some Solidity so we can start to fill it out and make our own token.

But there's something funky here.

What are these events? And why do we need them?

## 🎪 What's an event?
Events are something you can listen for. Sometimes it's helpful to bake events into your code so other programs can listen for them, and update when they happen. A really good example, and where you see events a lot, is with web browsers. When you go and click a button on Twitter, an event is emitted, so code on the website knows that button was clicked.

For smart contracts events are pretty similar, but they're logged on chain. And offchain code and bots can listen for them and do stuff.

## 🏇 What are our events?
Well if you click above you see there's 2. Transfer and approval. Whenever a token is approved for transfer or transferred an event is published as well. If I wanted to make a bot that played a sound every time Vitalik transferred USDC, I could by listening for those events.

They look just like they're functions but without a code body ({}s). They have those arguments where you define what is being emitted with them (like from, to and how much). There's also this "indexed" key word. This is a Solidity quirk that makes them easier to work with, but you can only have so many per contract. I won't go too into advanced event stuff, but they can get more crazy too with things like anonymous events if you're interested in looking them up.

Now that we've cleared up events we can start trying to fill in the code here to make this token work!

But. This isn't a normal tutorial, and I want to teach you to program in a better way. Set this code aside for now, even if you're tempted to work on it. Because we're about to explore the number 1 thing I wish they taught be about in university.
