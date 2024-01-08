# Day 194 of writing a smart contract a day until ETH hits $10k

**❌🦜 Solidity from the Ground Up:  Ep. 25**

I'm sure you've been wondering for a while where tokens come into this? We've done a great job of going over the basics of how code can be executed on a blockchain and that should be pretty clear. But on ETH everything pretty much has to do with 1 particular type of code. Tokens. NFTs or Shitcoins, almost everything on ETH has to do with tokens.

And today we're going to start on the journey to building one from scratch. And the first step is understanding the mapping:

## 🏗 Datastructures

Depending on how long I can keep this tutorial thing up, I'd love to eventually talk about datastructures. This is one of the most important things you'll learn in university studying computer science and it can get pretty complicated. But in a nutshell a data structure is a way of organizing information on a computer. Let's look at some examples.

Remember the "stack" from the first few lessons? Like a stack of pancakes? Well that is a data structure. It's very simply a way of organizing data. The rules are you can add new data by stacking it on top of others, you can access only the top of the stack at any given time. And you can delete stuff by taking it off the top. And that's the rules.

The most obvious sort of datastructure, and one that comes up really really often is a map, or hashmap. Or as Solidity calls it, a mapping. Mappings are like address books. You have a key, and a value. And you can insert a new item at any time to any key. And to get some data out, you request the data at a key. How the computer actually does this from the bottom up, I'm sorry I won't explain. It would take a lot of time and we'd first have to talk about other stuff like stacks and queues.

But Solidity is a little more unique in this, the evm is built on mappings and fundamentally makes it a bit more simple. Basically a mapping is an address book of storage slots, and those storage slots hold data. Find the "key" and look it up in the book, to find the slot it's stored at!

## 🚂 Mappings in Solidity
Mappings look like this:  
`mapping(address => uint) balance`  
This mapping will store uints at addresses with the name balance. What does this remind you of? A token!

Each person will have some balance of a token right? So to give them tokens we can just set the `balance[ADDRESS] = NUMBER`

And to get someone's balance we use `balance[ADDRESS].number`

really simple stuff. That notation of using the . to get a member of some THING like a mapping entry and []s to index a data structure are really really common across all programming languages.

That's it for today! See if you can create a function to set the caller's balance to 20. Check to see what balances are for addresses that never called the function.