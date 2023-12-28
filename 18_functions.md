# Day 187 of writing a smart contract a day until ETH hits $10k

**❌🦜 Solidity from the Ground Up:  Ep. 18**

We're learning Solidity at a bit of a strange pace right now. And it wouldn't be my first choice to introduce functions at this time but Solidity and smart contracts make it sort of necessary before we do anything else. First though, we'll recap what we know so far.

## ⚗️ Recap

So the CREATE opcode creates a contract by executing some constructor code, then copying provided code (the smart contract) into memory and then storing it onchain. That code onchain is the smart contract and can do stuff. We write these smart contracts in the Solidity language to avoid pains with assembly or Yul and that language has certain datatypes like address or uint to make all the crazy number stuff we spent a week on go away.
A lot of tutorials will skip all that, because again, Solidity abstracts it all away and it's ok to not know it. But as you already know, having that underlying understanding helps a lot in grasping new concepts and avoiding confusion. But now we're left with Solidity, and an understanding of how it works, but not idea how to really DO anything in Solidity.

## 🕹 Functions
Functions are reusable bits of code. If I write some simple code, in any programming language to print "I love waffles" to the screen. And I need to say I love waffles every time something happens, I want to be able to re-use all that code instead of typing it out in 6 different places. And the computer doesn't want to store the same code 6 different times when it can just store it in one place, and then JUMP to it whenever it needs to using those JUMP opcodes we talked about a long time ago.

Now if we were learning any other language we could get to this later but in Solidity it's pretty important to talk about now, because you can't interact with a smart contract without calling a function. Remember, in the EVM you execute this code by submitting a transaction to the network. When you submit a transaction "calling" a smart contract you specify which function you want to interact with and the data you want to give it. Then THAT is the code that gets executed.

In Solidity defining a function is really easy, just write "function" followed by the name of it, some parenthesis, and then some visibility modifiers (more on this in a moment) and finally some {}s.

Ex.

`function myFunctionName() public {CODE GOES HERE;}`  
`function myOtherFunction(uint aParameter) public {CODE GOES HERE;}`  
`function myPrivateFunction() private {CODE GOES HERE;}`  
`function giveMeAValue() public returns(uint){}`

## 🤹 What?
Yeah there is a lot to unpack here. To be honest, we'll need to revisit specific stuff about functions like visibility modifiers later. But for now I'll cover the absolute basics so you know what's going on.

Visibility modifiers include "public, external, internal and private". People can only call "public" and "external" ones. For now, just use public. It's the most versatile of them. If you make one internal or private you can't call the function with a transaction, and if you make it external you can ONLY call it with a transaction (not within the smart contract). Again, we'll visit these another day. If it's too confusing just stick to public for now.

Parameters are a way to give some information to your function. Remember "I love waffles"? Well what if you love lots of things and you want to be able to reuse the same code to say "I love pancakes" or "I love cats" you could write a function like this:
Ex. `function sayILoveThing(string thing) public {print("I love ",thing);}`
Note that's pseudo-code. It won't really run in Solidity but you get the idea. You can use "thing" as a parameter. And now if you call this function like `sayILoveThing("pancakes")` it will use that parameter of "pancakes" in the code inside of it. 

Returns is a way of allowing a function to return a value. Say instead of printing that "I love pancakes" string you just want it returned so you can print() it yourself. In this case you would write inside the function `return("I love ",thing);` and if you wrote `s = sayILoveThing("Cats")` s would be = "I love Cats". So pretty straightforward there.

## 🥢 Learning By Example
Again, it's a lot to unpack so I'm going to give you a gist to open up in Remix and look at with a bunch of various functions. You're free to check em out and get an idea for how they work. Deploy the contract and see what happens when you call them.
You should start getting an idea for Solidity syntax too. Programming languages, like real languages take a degree of farmiliarity to do correctly. And little things like remembering the {}s or the ;s is important to just get used to writing and seeing, not just memorizing the rules.

Anyways take a look here and I'll see you for a more indepth look into functions tomorrow!
https://gist.github.com/CarsonCase/e9c612788bbb4fb3b3f151b7f91ba9a0