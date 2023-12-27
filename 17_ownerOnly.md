# Day 186 of writing a smart contract a day until ETH hits $10k

**❌🦜 Solidity from the Ground Up:  Ep. 17**

You've got a solid understanding now of computing and the EVM specifically. Let's build a small practice project!

There's a lot more to learn, especially about Solidity itself but first let's do a little project. There's going to be a few new things here we'll expand on soon. But you should have a good idea of what's going on.
Anyways here it is, some Solidity code:
https://gist.github.com/CarsonCase/3d5b5afbdb8681f1f300e5a4c3455861

## ☺️ Trying it out
Go ahead and fire it up in Remix and call the function. It should go good. But Remix has an ability at the top of the "Deploy and Run Transactions" tab that allows you to change the address you're using. After deploying, change the address and notice you can't call "onlyOwner()"

And that's exactly what this contract does, the cosntructor sets the owner address to "msg.sender" then when you call the function "onlyOwner()" it reverts if msg.sender != owner

msg.sender?
msg.sender is a unique solidity thing to get the sender of a transaction. Just like the ADDRESS opcode. If you are creating the contract it's the sender of that CREATE transaction. So me make the creator the owner.

Then when someone calls the function onlyOnwer(), it's the sender of that transaction that has to be the same for it to pass.

## ❓What's Next?
So another sidenote is the "!=", in case you havn't seen that before it just means "NOT Equal To" But we can get to that. Also functions. I'll probably touch on functions next, as we're always going to be using them and they may be a bit confusing.

So if you're concerned about what's going on with the functions, don't be, it'll all be cleared up soon!