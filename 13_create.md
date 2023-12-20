# Day 182 of writing a smart contract a day until ETH hits $10k

**❌🦜 Solidity from the Ground Up:  Ep. 13**

It's time to create our first smart contract. 

Unfortunately for you, we are still using opcodes. But this is sort of the last thing we need to do with them before we can leave them for Solidity. 

So rejoice.

## 💅 Recap
Yesterday was a lore dump. But at the end I said something real important about ETH. That ETH is special because unlike cryptocurrency, you can send CODE that the miners execute. Part of that was code that can STORE things onchain.

Well. My dear reader. If you can write code and send it to the blockchain, and can write code that stores any information you want onchain. What would happen if you stored CODE onchain? Well you would get a smart contract.

Smart Contracts are bits of code that live on chain and people can interact with. They have their own addresses and can hold their own ETH. Coding them is really fun because once they exist they just exist and nobody can do anything about it. Unlike with a website, where if you stop paying the AWS bill it just shuts off, a smart contract will exist unapologetically for better or worse, forever only blindly following it's instructions.

## 👨‍🎨 CREATE
You know the drill. Evm.codes. Now. Go find CREATE. And read it. That is how you create a smart contract. You first have to load the code you want to publish to memory, then you can create it when you specify the location and size as well as if you want to send any ETH to it when you create it.

Let's get started!

I'm not sure if you noticed, but the evm.codes playground default code pushes the number 0x42 to memory, then returns it. And return, much like CREATE, returns something from memory. So it's pretty easy to copy this code, replace RETURN with CREATE, and make sure to PUSH1 00 for the ETH value to send. You should have something like this:

https://www.evm.codes/playground?fork=shanghai&unit=Wei&codeType=Bytecode&code='6~42%20z52%206~2~zzF0%5Cn'~0%20z6~0~%01z~_

![Final result](<Screenshot from 2023-12-19 23-15-18.png>)

Running through all the code returns a contract address. You did it! You created a contract at that address that. Well is pretty boring. It's just 42. Tomorrow we'll see what a real contract looks like.
