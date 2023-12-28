# Day 188 of writing a smart contract a day until ETH hits $10k

**❌🦜 Solidity from the Ground Up:  Ep. 19**

There's a lot more to lean with how we can customize functions, but the overal concept of just "make code run when you write FunctionName()" should hopefully be clear enough.

But you may have some questions about functions themselves. Mainly in the context of all the low level stuff we learned. There was no FUNCTION opcode. So how does the computer know what's happening when you call a function?

How does it seperate out the code you want to call in your function, and know that's all you want to do at that time? Today's post is about that. A deep dive into how functions work.

## 🖊 Function Signatures (also called Selectors)
Say it with me now. It's all just numbers. If you name your function "MySillyFunction()" or "Foo()" or "Goose()" it's not going to know the word. It needs a number representation of that name. And it does that with what's called a "function signature".  
Remember hashes? Well it's a hash. But not the whole 32 bytes (256 bits). But only 4 bytes instead. It looks like this:  
`0xa9059cbb`  

Think like how contracts and wallets both have addresses that are 20 bytes, functions have their own mini addresses within contracts that are only 4. Similar stuff. And it's just a cut off hash of their name.  

## 🔭 How it Works
So how does that list of opcodes actually work with function selectors. Well it goes a little something like this:
1. You make your transaction, and in the data you send to the contract specify 0xa9... as the function signature
2. When the code is executing the CALLDATALOAD opcode loads that data in your transaction.
3. For every function in the contract, one by one (ordered numerically by the signatures) your calldata is checked if EQ to that signature. If no, it skips on the the next signature to check it.
4. If EQ is true then it uses JUMP to jump to wherever the code of that function is stored in the program.

So that's actually pretty simple. The computer just checks your passed in calldata with all the functions in the code until it finds the one that matches what you said, and it jumps to wherever the code for that function is stored! Easy money.

## 📚 Homework
Go back to evm.codes and write a little Solidity contract with a single function that does something simple like return 5. Then compile it and walk throug the opcodes and see if you can find where the function is! Also see if you call it using calldata. Let me know in the comments what you found :)