# Day 172 of writing a smart contract a day until ETH hits $10k

**❌🦜 Solidity from the Ground Up:  Ep. 3**

Quick refresher on yesterday. Numbers don't always go from 0-9. Sometimes they keep going from 9 to A to B... to F. We call that "hexadecimal" as there's 16 "letters" we use from 0 to F.

and computers use binary which is just 0 - 1. 

## 1️⃣ Binary's.. Bad right?
So yesterday I didn't talk about binary much. But I did say that it only uses 0 and 1. And that 10 = 3. You may have thought "dang that probably sucks. It probably is really hard to count to a big number with it because you only have 0 and 1 to work with".

Well if you did the little puzzle at the end of the day you'd find that this is the formula for the largest a number can be:
BASE ^ DIGITS - 1. 

So binary is base 2 (0 and 1). And if we had 8 digits, we could have our largest number be 11111111 (there's 8 1s). That number is = 2^8 - 1 = 255

And you remember exponents from math class. 2^number can get reallllly big if number gets big enough. So binary may only have 2 base numbers, but we can still count pretty effectively with only a few of them. Lets imagine we have more numbers.

32 1s = 2^32 -1 = Max number: 4294967295
64 1s = 2^64 -1 = Max number: 18446744073709551615


## 8️⃣ Bits and Bytes.
You ever go buy a computer and it says something like "64 bit processing" or "x64" or something? Or maybe idk you see some PC gamer bragging about 64 Gigabytes on his whatchamagiggit?

Well what actually is a bit or a byte? Well it's sorta like feet and yards or millimeters and meters.

A bit is 1 digit. A 1 or a 0. This binary number: 00110011 is 8 bits.

A "byte" is 8 bits. So 00110011 is 1 byte. 

You might notice some patterns here...
Yesterday I said 0xFF = 255. I said above that 2^8 - 1 = 255 and that 8 = 1 byte. Oh. Yeah well computers tend to operate in "bytes". You will see people talk about bits, but those bit numbers (64, 32, or 256 are common) are always some multiple of 8. 
8 x 4 = 32
8 x 8 = 64
8 x 32 = 256

Ok ok ok why am I saying this? Well it's time to finally get to the point

## ✒️ Getting to the point

Remember our kitchen analogy? Well maybe you wondered "how big can an ingredient be?". Each one needs to be stored somewhere. In, idk a fridge, in tupperware. How big is each little tupperware for the ingredients? What's the largest one?
Well the same is true for numbers. The computer can't store numbers if they get too big. Those numbers like 32bit or 64bit processing you see on for sale computers mean exactly that. It means the tupperware max number is either 2^32-1 or 2^64-1

And in the EVM it's even larger at 256 bits. 

Remember PUSH1? 

That means PUSH 1 byte (or 8 bits) so not even a whole storage slot for an ingredient.
Go to evm.codes
Notice there's PUSH1, PUSH2, PUSH3 ... Up to PUSH32 

What is 32 bytes? 256 bits.
So the largest number you can move around is 2^256-1 (which is absurdly large)

What about the smallest? Well a number can be as small as 1. But what's the smallest tupperware? You can still put an item smaller than the tupperware in it. But what's the smallest storage slot? It's 1 byte or 8 bits.
This is why PUSH1 takes in a number up to 2^8-1 = 255 = 0xFF

## 🕹 PUSH1 01 FF

Go back to the evm.codes playground:
https://www.evm.codes/playground

and type PUSH1 FF
(remember you need to type the number for PUSH1)

This works!

Now try this:
PUSH1 100
You get an error. "There should be at least 2 characters per byte"

Right. Remember the smallest tupperware is 1 byte (which is 00-ff in hex) So we could try PUSH1 1000 instead

Now we get PUSH1 10 and STOP?? What?

Why? Because we said PUSH1 so it's only pushing 1 byte. It's pushing the 10. The 00 is STOP and that happens after. Ok let's try 1 more time

PUSH2 1000

Perfect! now we're doing it. Pushing 1000!

## 📩 Homework
Add some numbers again. But instead of 2. Add these numbers:
0xFAB3
0x12B1

What do you get back?

Ok thanks for putting up with all this fundamentals math stuff guys. I know we got reaallly into the weeds. But trust me we're going to get out of machine code soon and into actually learning some programming.
You're going to be glad you learned this stuff though! And plus not many devs know this stuff. You're really going to stand out from the guys who watched a few hours of Solidity tutorials if you understand how the EVM really works.