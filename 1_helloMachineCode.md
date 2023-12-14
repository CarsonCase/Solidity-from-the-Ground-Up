# Day 170 of writing a smart contract a day until ETH hits $10k

❌🦜 **Solidity from the Ground Up: Ep. 1**
Read this episode on [Github]()

## ❓*What the Heck Is a 'Puter?*

We really are starting from the bottom. One of the biggest mysteries when first learning to code for me was "how does the computer process what I say?"

I can accept that the actual "math" aspect is just some sort of Minecraft redstone wizardry (yes. Circuits are basically minecraft redstone). But how does this:

```
x = 2
y = 2
print(x + y)
```
actually DO it?

Well today we're going to use machine code to write our first-ever program. This is the most based programming tutorial to ever exist. Trust me, it's actually a lot easier than it sounds, this is something you could probably explain to a 5 year old.

## 📀 What is the EVM?
The Ethereum Virtual Machine is actually a great place to start learning programming. Because as its name implies it's sort of an imaginary computer. Or a computer simulator. It needs to be this way because ETH runs on a blockchain across many people's computers. And by being "virtual" we can basically have one big computer that everyone pitches in to help process for. This is why Vitalk always refers to ETH as a "world computer".

So the whole blockchain part, we'll get to when we get to it. For now let's just focus on the computer part. If the EVM is basically a computer, then how does this virtual computer go about... well computing?

## 🔠 Opcodes
A computer code as far as a computer is concerned is a recipe. The computer has its metaphorical kitchen where it has various tools like a blender. And when you give a recipe for a shake you might say:

    Banana to bowl
    Peanut butter to bowl
    Milk to bowl
    Bowl to blender

Well, for a computer to add 2 numbers it's pretty similar, but instead of a "bowl" it's memory. There are different types of memory like there's different kinds of bowls, glasses, and whatnot. But for now just know memory is where the computer stores numbers.

Opcodes are like instructions in the recipe. We might say PUSH banana, PUSH peanut-butter, PUSH milk, BLEND

In this pseudo-code recipe PUSH means to add an ingredient to the bowl, and BLEND means to empty all the BOWL ingredients into the blender, blend it, and return the result to the bowl.

## 👇Let's get real
[This](www.evm.codes) is a list of the REAL EVM opcodes. You can click on them to learn more about them. But for today, we're just doing the real basics. So we only need to know 2.

01 and 60

Remember. It's all just numbers. And always has been. Sure 01 = ADD and 60 = PUSH1 but those are just human-readable names we've given to the numbers. The computer just knows the number.

Click on 01 ADD on evm.codes and notice the:

    "Stack Input

        a: first integer value to add.
        b: second integer value to add.
        Stack Output
        a + b"

This means ADD works like BLEND from the recipe example. It takes the 2 things before it, does something (adds them) then returns them back to the "bowl" which is called the "stack".

Ok so what about 60? \ PUSH1::

    "Stack output

        value: pushed value"

Ok so this is like PUSH from the recipe, it pushes a number (value) onto the stack, like the recipe pushed ingredients into the bowl.

So if we write:

plaintext

6007

that means PUSH1 7

Yes, it needs a 0 in front of 7. A code is 2 letters and we'll soon get to why. But for today stick to between 01 and 09.

If we write 6001 that is actually PUSH1 01
and NOT PUSH1 ADD

PUSH1 takes in a value so the EVM is expecting a number after PUSH1

if we did 600101 that would be 60|01|01 = "PUSH1 01 ADD"
(keep in mind this won't work. ADD needs 2 numbers. We only pushed 1 😉)

To recap. A code is really just a list of instructions like a recipe. The computer knows certain tools and instructions like PUSH1 or ADD and can interact with ingredients (numbers) using them. PUSH1 and ADD and all instructions are called opcodes and they are really represented with numbers like 60 and 01 respectively.

## 🛝Playground
Go [here](www.evm.codes/playground?fork=shanghai&unit=Wei&codeType=Bytecode&code='')

This is a "playground" for EVM opcodes! You can type in instructions and see how the computer evaluates them.

Type in 6002 and hit "Run"
![Screenshot of evm.codes playground](<images/Screenshot from 2023-12-14 21-31-10.png>)
See the screenshot for what you should get.

    [00] PUSH1 02

See? The first instruction of the recipe (00) is PUSH1 the number 02.

And if you press the ↩️ button in the upper right, you can see what happens step by step. There's only 1 step (00) but it does what you think! See the "stack" in the lower right. It has 2 on it.

## 🫵Your Turn
Make a program that adds 2 + 2. I'm not going to tell you how to do it. But you have all the tools to figure it out. All you need is what we've talked about in this thread. You should have a stack with nothing but the number 4 in it when you're done. And remember the blender example!

Don't hesitate to do some trial and error by hitting Run and stepping through each step, watching the stack as it changes.

If you're stuck and need to see the solution, here it is.