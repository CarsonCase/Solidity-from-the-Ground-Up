# Day 175 of writing a smart contract a day until ETH hits $10k

**❌🦜 Solidity from the Ground Up:  Ep. 6**

"Why did you just waste 5 days talking about assembly? Nobody codes in assembly" 

Well there's a few reasons. But 1 of which we're going to spend a few more days talking about and that is memory. Understanding memory and it's types and how to best use it is really important.

It's important in computer science because that's pretty much why why need to do computer science. And it's even more important in the EVM because of a thing called gas, which we'll do a whole bunch on later.

Computers store memory in lots of ways. You might have heard of RAM vs Disk space or Hard Drive space for example. And that there is an example of two types of memory. I'm not going to go into computer architecture here,
but I will go into the 4 types of data locations in the EVM and start on todays, calldata. Also, I'm from here on out going to refer to "memory" as "data locations" because one of these locations is called "memory" and I know that gets confusing.
But regardless just remember the kitchen analogy, how there's bowls and tuperware in the kitchen. These are the 4 types of containers that can be used by our computer chef to store things.

## 4️⃣ 4 Data Locations

1. stack
2. calldata
3. memory
4. storage

So we've already talked about the stack, in fact the stack is the only thing we've used so far. Not every computer uses a stack, some use registers. But the EVM does. The stack just stores stuff that is being used right now. Like when we're adding numbers or something. The stack doesn't store a picture of a cat on it, unless we're actively doing something with that cat right now. This is the working memory of the computer.

Remember about the stack, that it can only store up to it's largest size of 256 bits. Memory exists to address that issue and offer larger temporary data storing, and storage is for long term storing. But again, we'll give them their own episodes.

## 📞 Calldata

Today is about "calldata". Calldata is data that YOU give the evm with your transaction and it can be pretty much as large as you want. Remember the paywall? What if we wanted to do something else. Instead of sending money to the contract, we wanted to send a list of addresses and then it gives us back the 3rd address or something?

Calldata is how we would give the program those addresses. Calldata is read only, meaning you can send calldata to the EVM but it cannot change that calldata, only read from it. If it wants to edit the data, it needs to copy it to another location first. We'll get to that.

Calldata is important to understand how we actually give data to the code we wrote, but also it's good to keep in mind as it's the cheapest of data locations. Accessing data takes effort from the computer, and even MORE effort for a newtwork of computers like ETH. So it's really important to use the cheapest and easiest methods of accessing/storing data to save network resources.

## ✒️ Writing code

You know the drill. Evm.codes playground.

First thing we're gonna do is a really really simple program. Just 36.

36 is the opcode for CALLDATASIZE

type it in, then enter some code in the "calldata in HEX" box. Example 0xffff. This should push 2 on the stack. Because that's 2 bytes of calldata.

Remember, calldata can be larger than 256 bits. And before we load anything in, we need to know how large our calldata is. This gives us that answer.

So now try copying your own ETH address. If you don't have one just use this:
0x95222290dd7278aa3ddd389cc1e1d165cc4bafe5

Then just paste it 2 more times (removing the 0x) to get this:
0x95222290dd7278aa3ddd389cc1e1d165cc4bafe595222290dd7278aa3ddd389cc1e1d165cc4bafe595222290dd7278aa3ddd389cc1e1d165cc4bafe5

This is more than 256 bits but that's ok, CALLDATASIZE returns it's size as 3c.

Now if we want to load only the 3rd address we can do the following

Get the size of callData.
subtract the length of 1 address (an address is 20 bytes, or 0x14)
Now we have the point where the last address (the 3rd) begins
Run CALLDATALOAD to load the data starting at that index (the begining of 3rd) onto the stack, that would be the 3rd address.
W
Here's what it looks like:
![EVM.codes screenshot](<images/Screenshot from 2023-12-18 20-53-41.png>)

## 💽 Challenge
Get the 2nd address. And do so by ADDING instead of subtracting. It really should be about the same code. Ez pz

Wow! Not only can you code in EVM machinecode but you can even have users pass in data. I know we're starting out slow here. But it's for a reason. Later on when we get to Yul and Solidity it's not going to be so confusing when I say "oh yeah this is a number, and this is a string, and arrays just can't do this". Most tutorials just make you memorize that stuff because they're afraid to get into the weeds with memory management and opcodes. But not us! Trust me, this all makes everything way smoother down the line.