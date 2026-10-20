---
kind: page
id: "tk3.toolkitzone.com/tk3.toolkitzone.com/help/?page=18.1"
site: "tk3.toolkitzone.com"
title: "Contents"
original_url: "http://tk3.toolkitzone.com/help/?page=18.1"
written: null
date_confidence: "unknown"
updated: null
captured: ["20051225185831", "20070126065409"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/tk3.toolkitzone.com/help__page_18.1_amp_3BPHPSESSID_216a65194b2cc1baac15e1c844447215", captured: "20051225185831", sha256: "bbb26dd7b25605370e1e1994aa1552a3bfc4e535e06fdb3cb7fc3af05d3c1359", wayback_url: "https://web.archive.org/web/20051225185831/http://tk3.toolkitzone.com/help/?page=18.1&amp%3BPHPSESSID=216a65194b2cc1baac15e1c844447215"}
  - {path: "wayback/toolkitzone.com/tk3.toolkitzone.com/help__page_18.1", captured: "20070126065409", sha256: "c85f1fe5556966e9003b20a27af00d6077fde939d953f2252ebfc94cfbeea360", wayback_url: "https://web.archive.org/web/20070126065409/http://tk3.toolkitzone.com/help/?page=18.1"}
---

# Contents

Basics of Programming
The Basics of Programming
In all programming languages (including RPGCode), your computer will do many different tasks just by your typing a command. A program is nothing more than a bunch of commands that tell the computer what to do. The computer is, however, dependent on your success in giving it instructions. If you don't tell the computer when to start, what to do, and when to stop, it won't understand what you want, and certainly won't work. So lets start by learning the most simple instruction you can give the computer through RPGCode: showing text on the screen. This is done with the 'Mwin' command (mwin stands for message window).
Mwin("This text goes inside of a message window!")
Mwin("La la la, random messages!")
If you run that program, you will see that the message window shows up with the text inside of it, and then disappears almost instantly. This is because you need a way to wait for the user to do something before it disappears. This is where we introduce the next command...
Commands:
To make the Message Window stay on the screen, you'll need to use a command called 'Wait' (Wait()). The 'Wait' command makes the computer 'pause' itself until the user presses a button on the keyboard. This is how you make the message window stay on screen using Wait:
Mwin("Unlike the first example,")
Mwin("this text will stay on the screen.")
Wait(a$)
By the parentheses, you can already tell that it's a command named 'Wait'. But what does that '(a$)' mean, exactly? The parentheses (the '(' and ')') are attached to all of the commands. They hold "arguments" or "parameters" inside of them. The parameters of a command are just places where you put letters, numbers, or variables (more on this later). Some commands, however, don't take parameters (but it's always a good idea to include the parentheses anyway). 'a$' is the parameter that the wait command takes. You can also do the Wait() command another way. The example I've shown is not the prefered way to do the Wait command. This is:
Mwin("This example shows another way to do Wait()")
Mwin("Isn't that cool?")
a$ = Wait()
If you have trouble distinguishing commands from variables, look at it this way: A command has opening and closing parentheses (the '(' and ')'), and variables have literal or numeric marks (the '$' or '!')
Variables:
You probably already know that computers can store information. In programming, you can store different types of information through the use of 'variables'. A variable is a label. A name you can give to certain pieces of information in a program. You can store numbers (numeric values) and words (literal values) inside of variables. If you need a clearer understanding of what variables are, think of it this way: Let's say that a variable is a cardboard box. Well, you might want to put something in that box. I'll put a big '5' in that box, and slap a label on the front of the box that says "box". The RPGCode representation of that is like this:
box! = 5
Why is there a '!' after it? What does that do? That's what you call a 'numeric indicator'. What that does is tells the computer that you are storing a number in the variable. So, this is how you'd read it:
'box' Alright. I know that the variable is named 'box'. '!' Now I know that we'll be storing a number in it.
Ok, so you understand how to initiate a numeric variable. As you'll probably notice, there's something else attached to the end of the variable. '= 5'. That just means that the variable equals 5.
Now you know how to create a variable and assign it a value. But one question remains, why does the 'a$' in the Wait command have a '$' instead of '!'? The answer is simple. As I said, the '!' is a numeric indicator, for variables that store numbers. So '$' is a literal indicator, for variables that store text. This is how you use it:
//Let's store the word "Hello" in box$.
box$ = "Hello"
Hold on -- something's different there! Why is the a line of text that has two slashes ('//') before it? Well, that's called a commented line. A commented line is just text that the programmer can write into the program so others know what's happening. Comments are ignored by the computer, and are generally good to include in your programs. It's a good idea to comment your code because you might forget what some of it does.
Now, back to the variables. You already know that 'box$' means that it's a literal variable for storing text. Notice that "Hello" is in quotation marks. All text put into literal variables must have quotation marks around it. And just for reference later on in this help file, a literal variable is also called a "string".
Remember to always use the Kill command to kill your variables, freeing up memory! If you don't, the variables will sit in memory and slow down your programs! You can find out how to use the Kill command in the command reference.
It is also good practice to use the 'Local' command when declaring a variable. For information on this, refer to the Advanced "Scope" section of this help file.
Variables and Math:
Some of you may dislike math, but you should still read this section! It teaches you some very useful things about variables.
In math, you can use variables to represent a number. The same is true with programming. You can also add, subtract, multiply, and devide. Again, the same is true with programming. Here is an example of multiplying a number by 2 in math (using 'x' as the variable to represent the number 10):
x = 10 * 2
The end result, as you probably already know, is 20. The following is also allowed in math:
y = 10 x = y + 5
And the end result would be 15 (10 + 5 = 15). The same thing can be done in programming. In RPGCode, this is how you'd do the two representations of variables:
//Gives x! the value 20
x! = 10 * 2
//Gives x! the value 15
y! = 10
x! = y! + 5
Simple, eh? You can do some of the same things with literal variables that you can with numeric variables. There are limitations however, as you cannot multiply or devide from a literal variable. You can add two literal variables together the same way the add two numbers together. Here's how you do it:
box$ = "Jim"
box2$ = "my"
box3$ = box$ + box2$
That puts the text "Jimmy" together in the variable 'box3'.
Now that you know how to add and multiply in RPGCode, let's move on to subtracting and dividing. The way you subtract is exactly like adding, exept you use '-' instead of '+'. Let's take a look at some examples of subtracting and deviding:
//Let's subtract!
y! = 3
x! = 10 - y!
//Now, let's divide
x! = 10 / 2
The above example will put the value 7 into x! because we subtracted 3 from 10 (10 - 3 = 7). The second example will put the value 5 into x! because we devided 10 by 2, making it half the full number (10 / 2 = 5).
Congratulations! you 've learned enough about variables and how to manipulate them to last you for a while. Now, I'll show you some ways of actually showing what the values of the variables are...
Important note: Math calculations on variables follows the order of operations by precedence. This means that if you had a calculation like this: a! = 3-1*2, the multiplication will be evaluated before the subtraction. If you do not know the order of operations, you can use parentheses to nullify precedence. This means that the above calculation can work as needed by doing this:
a! = (3 - 1) * 2
Or a more complicated example:
a! = 10
b! = 7
c! = (a! + b!) * (10 / b!)
The Message Window:
You've already learned how to show text in the message window, but you never learned how to display variables with it. Well, in this section you will. First of all, I'll introduce you to a new command. The Show() command. What it does is takes a variable and shows its value in the message window. Here's an example of how it works:
x! = 5
Mwin("The value of x! is")
Show(x!)
Mwin("Cool!")
Wait()
Mwincls()
First, I create a variable called x! and assign it the value 5. After that, I show the message "The value of x! is 5 Cool!". However, since I'm using the Show() command, the result looks like this:
The value of x! is 5 Cool!
Looks a little messed up! The draw back of using Show() to show a variables value is that it will show up on a line of its own. This is where the Mwin() command comes in handy again. You will also notice that I added in another command, Mwincls(). All that does is clears the message window from the screen.
Here's how you would show the whole sentence on one line:
x! = 5
Mwin("The value of x! is , cool!")
Wait()
Mwincls()
Much easier! The way you show the value of a variable with the Mwin() command is to enclose the variables name in left and right angle brackets (the < and >). This saves time and makes it look better.
