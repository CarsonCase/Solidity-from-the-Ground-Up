# Day 192 of writing a smart contract a day until ETH hits $10k

**❌🦜 Solidity from the Ground Up:  Ep. 23**

# ⛽ What is Gas?

It's about time we talk about gas. This is another evm specific concept but I'll explain why practicing with this quirk of the EVM can help make you a better programmer in general as well.

So I've alluded to the idea of operations being "expensive" a lot over this course. That each opcode can have a sort of cost. And this is true. Computers are real things after all, and every action you ask them to preform requires a real thing to be done in the complex machinery that lies on your desk.
Every time your computer does a thing, a little bit of electricity is expended over a little bit of time to do it. And if the task you're asking it to preform is really really complicated, it might take too much time and energy to complete it. Time that could be spent on something else, and energy that you have to pay for.

This is an important concern for the nodes running on Ethereum and other blockchains. Remember, it's a world computer. Everyone pitches in to preform the operations people submit in transactions. What would happen if some troll came around and started submitting millions upon millions of complicated and wasteful transactions that require the network to waste time and energy on something worthless?

Gas, and really the Ethereum crypto currency, exists to combat this. Every opcode that you want executed onchain has an associated gas cost, and that gas needs to be paid when you make a transaction to compensate the members of the network for running that code. This way, not only are people incentivized to run eth nodes and miners. But you are incentivized to make your tasks as efficient as possible.

# 🕵️‍♀️ Looking at the costs
https://www.evm.codes/ as always, has the answers. Each opcode has it's associated gas with it. Some like ADD or PUSH are cheap. While others like CREATE are expensive. There's more details too if you click on opcodes.

For example SSTORE has an entire section on how gas is calculated and a calculator to show you. Since it's not just opcodes that cost gas, but storing and accessing data in storage and memory locations as well. This can get pretty complicated and you can look into it all you want. But today let's just get the concept of gas and what it means for you.

# 🥨 Tying it together

Gas and gas optimization is an entire subgenre of Smart Contract development, and we might revisit it a bit more as it's really fun and interesting. But for now what do you, as someone learning need to know? And how does this impact your broader understanding of computer science?

Well, when you write solidity you don't always see the opcodes it compiles to, but there's certain patterns you'll memorize reduce gas, and understand why because of opcodes. In general though, the main way to save gas in Solidity code is to cut down on use of storage when not necessary. For example, copy a value to memory from storage if you plan on accessing it more than once. That way you can use the cheaper memory access instead of the more expensive storage one once you've copied it.

Don't stress much about gas or optimizing it yet, but when you can, try to think about it because especially on ETH it can make a big difference. But it makes a difference for other programmers too. Computers are fast these days and the difference between accessing memory 1x per operation and 2x per operation is probably negligible for most things. But if you have to preform this operation 100,000,000,000 times per second on a massive network of machines, maybe it starts to make a bigger difference. Optimization is something that is unnecessary until it isn't, and being a developer who has these concepts of efficiency and understanding the little details and patters will really really set you apart from the crowd.
