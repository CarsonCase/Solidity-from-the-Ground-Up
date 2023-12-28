# Day 190 of writing a smart contract a day until ETH hits $10k

**❌🦜 Solidity from the Ground Up:  Ep. 21**

Today is all about control structures and logical operators. Whoa whoa whoa easy now. This isn't as crazy as it sounds. It's really pretty easy. This just means we're going over that "if" kind of stuff. I know we've used if already a lot even at the opcode level. But there's more to it all and it's high time we address it.

## 🏛 Control Structures 
This is fancy name but it means ways to control how code is executed. If it's executed, if it's not, how many times, ect. There's a few of these but we're going to talk about 5 common ones right now. 
`if`, `else`, `while`, `return` and `for`

```
if(boolean){
    do a think if boolean is true;
}else{
    do a thing if boolean is false;
}
```

That's pretty much the best explanation of if and else. You've already seen it. It's in almost every computer programming language and it's used a lot. You can use a boolean value in the if() or something that evaluates to a boolean like the operators we're about to talk about.

return also does something we're familiar with. It returns a value from a function. 

What about while?
```
while(boolean){
    do this thing over and over as long as boolean is true
}
```
It's a loop. Really simple. Be careful though if the boolean NEVER becomes false you'll get stuck forever.
```
uint count = 0;
while(count < 100){
    count = count + 1;
}
```
There's an easy example of how to count up with a while loop. Again it's in nearly every language and very common stuff.

But not as common as the `for` loop. For can be a tad confusing but it'll become your best friend. It's handy because in nearly every loop you need to define some counting variable (called an iterator and often named "i"), you need a condition like count < 100, and you need to increase it like count = count + 1. So the for loop lets you do all that at once:
```
for(uint i = 0; i < 100; i++){
    do this thing over and over as long as i, which starts at 0, and increments by 1 each loop, is < 100;
}
```

Sort of a lot. But don't worry, you'll use all this stuff SO MUCH during your programming career you'll know it like the back of your hand. If you don't get it now, you will soon and that's a guarantee.

## 🕵️‍♂️ Logical Operators and Comparison Operators
This again, sounds kind of fancy. But it just means things like that >, <, ==, ect. It's ways to evaluate if something is true or false with numbers or other true and false values.

1. x < y : x is less than y, true or false
2. x > y : x is greater than y, true or false
3. x == y : x is equal to y, true or false (yes it's two =s. ==)
4. x <= y : x is less than or equal to y, true or false
5. x >= y : x is greater than or equal to y, true or false
6. x != y : x is not equal to y, true or false

Ez pz. 

Those were the comparison operators. Because you can compare numbers and get back true or false values. But what if you want to compare true vs. false. That's where logical operators come in.
a and b are booleans, meaning they are either set to true or false.

1. a && b : a and b are both true, true or false
2. a || b : either a or be is true, true or false
3. !a : a is not true, true or false

## 👓 Lets do Some Logic
See if you can answer in the comments, if this code will execute:
```
if(5 > 3 && !(4 < 2)){
    // will this code execute?
}
```

What about this? When will the loop stop?
```
bool a = false;
while(!a){
    // pretend there's a getYear() function to return the year as a number
    if(getYear() == 2024){
        a = true;
    }
}
```