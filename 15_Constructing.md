# Day 184 of writing a smart contract a day until ETH hits $10k

**❌🦜 Solidity from the Ground Up:  Ep. 15**

"But wait. Didn't we just do "CREATE" 2 days ago?" 

Yes. But constructing is different from CREATING. Because in the computer world "constructor" has a very special meaning.

## 👞 Objects
In computer science we really love abstraction. Abstraction is the name of the game. Take something complicated like bytecode. And find a way to make it less complicated. Abstract away all but the stuff you NEED to use.

1 way of doing this is by creating objects. Objects are really just abstract things. For example. A Smart Contract. You saw how complicated that was yesterday. And yet. In Solidity we can just call a "contract" an object and create one as simple as "contract MyContract{}"

Objects have the option to include something special called a constructor.

## 🦺 Constructors
A constructor is, as it implies, code that is called when an object is created. In our case, the Smart Contract getting deployed like it did yesterday. It's sort of like our way of adding on information to that chef's kitchen set up code.

We're going to start with a constructor, even though many tutorials won't. But in Solidity they have some unique properties that are fresh and easy to understand after the context we have of yesterday's work with the bytecode.

First though let's learn how to use our new friend Remix

## 🎧 Remix
Remix is like evm.codes on steroids and for Solidity. It's where we're going to be doing all our developing together as it's nice and easy. Let me show you how to load my code into remix so you can follow along!

1. Go here -> https://remix.ethereum.org

![Gist](<images/Screenshot from 2023-12-20 00-50-43.png>)

2. On the front page you want to click that button under "Load from" that says "Gist"

3. Then paste in the link I give you: https://gist.github.com/CarsonCase/4e80e1565dc77afeccc7d87feb0eb250

![Where to click](<images/Screenshot from 2023-12-20 00-55-06.png>)

4. Then a new file will appear on the left side here. Click it and a contracts folder opens up, and click that, and then click the Solidity file inside of it.

5. Pres ctl + s "save" to compile the contract

![Compiled Contract](<images/Screenshot from 2023-12-20 00-59-55.png>)

6. The green checkmark should show up and now you can click the icon underneath that says "Deploy & Run transactions"

7. Click the big orange Deploy button

![Deployed](<images/Screenshot from 2023-12-20 01-00-56.png>)

8. Good job! You just deployed a smart contract! To a simulation network, not the real ETH or anything but still! That's your contract. Click the arrow to expand and see the functions you can call with it.

9. With this one there's just "str" which returns "Hello World"

This is because the contract has a constructor that sets str to Hello World on deployment.

## 🐙 Why Constructors Are special

Yesterday remember there was sort of 2 parts to deploying our contract? There was all the code executed at first, that then copied the rest of the code and returned it from memory? And THAT is the actual deployed contract?
Well normally when you write code in a smart contract like a function or something for people to interact with, that is in the code that is copied and published onchain. But not the constructor. The constructor is executed BEFORE that CODECOPY instruction and isn't included in it.

Constructors often cause headaches for new Solidity devs because of this (me included) so it's an important thing to understand!