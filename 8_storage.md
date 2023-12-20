# Day 177 of writing a smart contract a day until ETH hits $10k

**❌🦜 Solidity from the Ground Up:  Ep. 8**

I promise. This is the last opcode/assembly we'll do for a while. We're going to get into "real" programming soon. There's just 1 more thing and it's storage.

## 🚪 What is Storage?
Storage is persistent. Meaning if you turn the computer off, the data isn't gone. In the case of a typical computer this is usually a hard drive of some sort. And on the EVM it's a bit more complicated but the core idea is the same.

Memory will be gone when you're done interacting with it, and really is like a "short term memory". Where as storage is long term memory that you can come back and access.

A tab open on your browser will probably be running in memory, it can be closed and is gone. But a file you create and save on your desktop is saved in your computer's storage.

On ETH, if you send a token to someone, your balances are stored in storage. But if you just wanted to do some calculations on the EVM, like add 2 numbers together, it's just done in memory.
This is important for many practical stuff we'll get into later but lets jump right into some storage challenges to get an idea and practice this memory stuff more!


## Challenge 1!
https://www.evm.codes/playground?fork=shanghai&unit=Wei&codeType=Bytecode&code='60%2022%2055jxChallenge%3A_tor~%5C'22%5C'ZsWg_STORExThiqcod~doesn%22X._e~iQyou%20canZs~YOpcodeqtab%20to%20fWdNuzwhazit%22qmissWg...jxIfvXqyou%20should%20geza%20lozofvnformatioPpopZpvnzYSTORAGE%20sectionvPYbottom%20right%3BvncludWg%20a%20VALUENQ22'~e%20zt%20xj%23%20v%20iqs%20j%5Cn_%20SZ%20uYth~XzworkWinQf%20Pn%20N%20o%01NPQWXYZ_jqvxz~_
This one's very simple. Just read the docs to see why it's not working...
You might wonder what Contract or Slot are but I'll answer in a minute...

## Challenge 2!
https://www.evm.codes/playground?fork=shanghai&unit=Wei&codeType=Bytecode&code='VFirst%20push~intoWRQGet~fromW%20%5BFIX%20THIS%5DjxQPus_tobYif~wasbuccessfully%20retreivedR14zShould%20en%20up%20wit_atqtopZfqsYatqendZf%20allZperations'~%2022%20zjjVx6U0Uq%20the%20j%5Cnb%20s_h%201%20Z%20oYtack%20WbtorageV%23%20U0%20Rj60~Qx55z%01QRUVWYZ_bjqxz~_


## ❓ A Few Questions
You might be wondering what "contract" and "slot" were all about with storage... Well storage is a property of a "smart contract" in the EVM. A smart contract has storage that it can store values in. So since this is a playground it sort of just creates a pretend one for you. Don't stress it too much yet.

But slots should be stressed. Because they very simply are where you data is in storage! And when we interact with storage tomorrow using yul, you'll be thinking of storage in terms of slot numbers not bytes like we've had to do so far. So that's great news!