---
kind: page
id: "rpgtoolkit.com/rpgtoolkit.com/docs/ver2/help2.htm"
site: "rpgtoolkit.com"
title: "Then"
original_url: "http://rpgtoolkit.com/docs/ver2/help2.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20010116105300"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.com/docs/ver2/help2.htm", captured: "20010116105300", sha256: "4a5fce2316985063f2785aacbc8efe3ef8413897db06ef543e9bd765eef29ab2", wayback_url: "https://web.archive.org/web/20010116105300/http://rpgtoolkit.com/docs/ver2/help2.htm"}
---

# Then

ROGRAMMING IN RPGC ODE2
**
RPGCode2
*
Introduction
First of all, for all of you version 1.4 people out there, you won’t find RPGCode2 hard. There are some changes from RPGCode1, however. Look in the Variable subheading for the new variable naming rules (you can still use the old number system, but I don’t recommend it at all). Also note the use of the #Mwin commands. RPGCode2 is almost fully compatible with RPGCode1. You can go on programming like you did in version 1, but I recommend you read this so you can get the idea of the new way of doing things. Also, you read the section on multitasking, as it is important. *highly* **must** *extremely*
The RPG Toolkit allows you to create extremely nice looking games in which your character can walk around and fight. But what is a game without interaction? An RPG needs village idiots running around everywhere making smart remarks about the player, or wise men who tell the player what to do. And the player needs to buy and sell things and equip armor and everything else. Well, all of these tasks can be done using RPGCode, the built in programming language for the RPG Toolkit.
Don’t stop reading just because I said programming language! A lot of people are scared by that and never give RPGCode a try. It’s easy to learn! Even if you’ve never programmed before, you should be making simple programs within the next 15 minutes (assuming you actually read this). And most of the programs you will ever make are simple ones. It only gets (somewhat) complex when you go overboard and test RPGCode to its limits... and that will come in time. *very*
For those of you who programmed in the past- excellent! RPGCode2 is similar in many respects to languages like C or Java. You will find that RPGCode is a very versatile language-- and it is a , not a as is common in game creation engines. That means greater flexibility and robustness. RPGCode is a language that can be built upon, like C or C++. You can create your own commands and RPGCode system libraries. The RPG Toolkit’s greatest advantage is RPGCode, because it was designed to be easy and powerful. *have* *programming language* *scripting language*
So what can RPGCode do? You name it. You want a casino game where you pull a lever and the player wins a jackpot? That’s possible. So is a great story sequence where all your characters get killed, or even something as simple as a stupid kid running in circles in some town. Like I said, RPGCode is a , and your imagination is the only limit with a programming language. *programming language*
So, then. Let’s begin...
***
PRG Files and Environment Limits
All RPGCode programs are saves as ASCII (text) files with a .PRG extension. You can create them with the built in Program Editor or with a text editor.
A single PRG file has a maximum length of 2001 lines. If your programs are longer, you can extend them using the #Run command. RPGCode gives you access to 8001 numerical variables and 3001 literal variables. Up to 11 programs can run simultaneously, and another 51 by themselves on each board.
***
Basics of Programming
Well, let’s get started immediately. In RPGCode (and all programming languages), the computer will do what you want it to do by giving it specific . A program is nothing more than a bunch of commands that tell the computer exactly what to do. The computer doesn’t even know what the program itself does- it just blindly follows the instructions- sort of like training a horse to do what you want it to do- the horse doesn’t now where you’re going, but by telling it where to go, when to stop and when to go, it will get you to where you are going. So you see, it’s human direction that is the key factor in programming. If the programmer doesn’t know what to do, the computer certainly won’t. *commands*
RPGCode has something like 80 built in commands, plus any others that people have created. Each command tells the computer to do something different. Do freak out- you don’t have to memorize 80 commands. In fact, you’ll probably only use about 10 with any regularity. The others are for "pushing the envelope" like I said in the Intro.
The most basic command in RPGCode is plain text all by itself. Text all by itself gets put in what is called the . The Message Window is a small window that pops up in the middle of the game and displays text. If you’ve ever played an RPG, you will be familiar with the text boxes that are used to display text. Well, the Message Window is the same thing. So, here’s an example of a program that just puts some stuff in the text window: *Message Window*
This s text that gets
put in the Message Window.
Lalalalalalala
Hahahahahahaha.
Pretty simple, huh?
If you were to actually run the above program, you’d see the above text placed inside the message window.
Now, there’s a trick about the message window. If it doesn’t get all filled with text, it will close immediately. So, maybe you try running the above program and you saw that the message window closed immediately after displaying the text, and you couldn’t read it. Here’s where I introduce the next command... *did*
**
Commands
Apart from plain text, commands in RPGCode start with the ‘#’ symbol. The reason for this is so that he computer can tell the difference between text that goes in the Message Window and other commands. So, anything with the ‘#’ symbol before it is a . *all* *command*
A basic command is the #Wait command (notice the ‘#’ at the front of the command name). #Wait causes the computer to wait for the user to press a key. So, if you want the computer to pause before closing the Message Window, try this program:
This text goes in the Message Window
#Wait(a$)
The above program puts the text ‘This text goes in the Message Window’ and then waits for the user to press a key (that’s what #Wait(a$) does.)
Let’s look at the #Wait command a little more closely:
#Wait (a$)
You already know that the ‘#’ and ‘Wait’ mean that it’s a command called ‘Wait’, but what does ‘(a$)’ mean? Well, that’s dealt with next...
**
Variables
How do computers remember information? It gets put in memory, right? Well, in memory? How does the computer know where to look? Think about it this way: you’re a person, right (I hope so)? So how would someone find you in a crowd? Maybe they’d call out your name... Well, all information in memory has it’s own name, and when the computer wants a specific piece of information, it basically ‘calls out its name’. *where*
This brings us to the subject of variables. You know that in the math world, you can use variables to represent numbers. For example:
*
x=15
Means that the variable ‘x’ is equal to the number 15. And, whenever you see the variable ‘x’, you know that we’re really talking about the number 15 in disguise. So:
*
x+5
Is equal to 20 (15+5=20, right?). Well, we use variables in programming, too. Except in programming, a variable isn’t used to a value (like x=15), it’s used to a value. So: *represent* *store*
#x!=15
Stores the value 15 in a variable called x!. What’s up with the ‘#’ and ‘!’, though? Well, we already know that # is used to represent a command in RPGCode, so the above example is a in and of itself. The ‘!’ tells us what kind of information we want to store. *command*
In RPGCode, there are two types of information you can store: numbers (numerical data) and words (literal data). Both are stored in variables. So, how can you tell a variable called ‘a’ that holds a number from a variable called ‘a’ that holds a word? By putting a ‘!’ sign at the end of the variable name, RPGCode knows you’re talking about a numerical value. By putting a ‘$’ at the end of a variable name, RPGCode knows you’re talking about a variable that stores a word (a literal variable).
So, the above example (#x!=15) is a that tells the computer to store the number 15 in a variable called x! (a numerical variable). *command*
Incidentally, variable names can be longer than one letter. For example, we could just as easily have said:
#bob!=15
That stores the value 15 in a numerical variable called ‘bob’.
So, how do you put words into a variable? Like this:
#Joey$="Text to put in a variable"
This puts the text ‘Text to put in a variable’ into a literal (word) variable called ‘Joey’ (I know it’s literal because it has the ‘$’ symbol). Notice that the text to put in the variable is enclose in quotation marks. You must always put quotation marks around text data in RPGCode.
So, back to the #Wait command. What does ‘(a$)’ do? well, the #Wait command waits for the user to press a key. The key that is pressed is stored in the literal variable a$. In the above example, we don’t actually do anything with a$, but #Wait requires that there be some variable there to get the results of the keypress.
**
Fun With Variables (hahaha)
You can do more than just put numbers and text into variables. You can put the contents of one variable into another. Consider this example:
* Program showing variable use
* Don’t be freaked out by the ‘*’ stuff.
* The ‘*’ just tells the computer to ignore this text.
#var1!=12
*Puts 12 in var1!
#var2!=var1!
*Puts 12 in var2! (now var1! var2! equal 12). *and*
#var1!=11
*var1! now equals 11. var2! still equals 12, though.
*Here’s an example using literal variables:
#litvar1$="Hello!"
*Puts ‘Hello’ in litavr1$
#litvar2$=litvar1$
*Now litvar2$ also stores ‘Hello’
#litvar1$=""
*This empties out litvar1$- it now contains nothing!
*Now let’s see what’s in these variables:
Variable var1! has a value of:
#Show(var1!)
Variable var2! has a value of:
#Show(var2!)
Variable litvar1$ has a value of:
#Show(litvar1$)
Variable litvar2$ has a value of:
#Show(litvar2$)
#Wait(a$)
* Wait for the user to press a key.
Ok, there’s some new stuff here. First of all, the text preceded by the ‘*’ character is ignored by the RPGCode interpreter. This is called ‘commenting’. It allows us to put plain English into our code to explain what we’re doing. So, everything you see with the ‘*’ in front of it is ignored by the computer, and is there for your benefit.
The comments explain step by step what is going on. But at the end, what’s going on with those #Show commands?
The #Show command puts the contents of a variable in the Message Window. So a command like #Show(var2!) puts 12 in the Message Window, since var2! contains the value 12. The #Show commands are there to show you the results of all that playing with variables up top.
As you will see later on, there’s a better way to show variables with a different command (#Mwin).
And of course, the #Wait(a$) just waits for the user to press a key (and, if you care, the key that he/she pressed was put in the variable a$).
**
Variables And Math
So, what’s the point of variables? The first use of variables comes with performing math inside a program. Sure. Maybe you hate math. But this is pretty easy stuff (add, subtract, multiply, divide- no integrals here!).
In math, variables are assigned mathematical vales like this:
*
x = 12 + 18
In this case, x equals 30 (12+18). You could also do the following...
*
y=12
x = y + 18
This also causes x to equal 30, since y+18 is equivalent to saying 12+18. The RPGCode equivalents to these three statements look like this:
#x!=12+18
#y!=12
#x!=y!+18
You probably expected that. But you can see that math with variables is similar to real math. There’s just one hitch-- in RPGCode (and every programming language), the stuff of the right hand side of the ‘=‘ sign gets calculated, and the answer is stored in the variable on the left. This may seem trivial, but consider this:
#x!=12
#x!=x!+12
Equals 40 (14 *2 gets done first, then 12 is added, as per the order of operations). In RPGCode, however,
My math prof. would be very displeased with me if I did this (but my computer science prof. wouldn’t mind!). In math, it is impossible for x to be equal to itself plus 12. But in programming, this just means ‘take the value of ‘x’, add 12 to it, and put the new value back into ‘x’). So, x ends up equaling 24. This is perfectly possible and acceptable.
In RPGCode, you can perform the four basic operations: + (addition), - (subtraction), / (division) and * (multiplication).
You can perform more than one operation at a time, but the ‘order of operations’ is not obeyed. Rather, it is calculated from left to right giving no regard to rules of precedence... For example, in math:
*
x=12 + 14 * 2
#x!=12+14*2
Equals 52 (it does it in order- 12+14 is 26. 26 * 2 is 52). Just keep that in mind when doing math with RPGCode!
Also, you can literal variables only (unlike numerical ones with which you can do anything). For example: *add*
#a$="Hello "
#b$="player!"
#c$=a$+b$
In this case, c$ is equal to ‘Hello player!’.
Well, congratulate yourself! We’re through the boring part. Now we’re going to put some of this stuff into practice and make some decent programs...
***
The Message Window
You’ve already seen how you can put text in the Message Window just by typing text and how you can put variables in the Message Window using the #Show command. Well, now we’re going to see how to use the Message Window the proper way.
Although you can put text in the Message Window just by typing text, this is not very good. First of all, it doesn’t like a command. It has no’#’ in front of it, so someone might mistake it for a comment. Second, you can’t blend text and variables together without putting them on separate lines. The #Show command puts a variable in the Message Window, but it puts it on a line all by itself- not very nice looking! How would you like to see this in the Message Window if you were playing a game: *look*
You have
100
GP.
That’s just crazy! You’d expect it all to be on one line ("You have 100 GP"). Well, there are a few commands made specifically for dealing with the message window. The first of these is the #Mwin command.
The #Mwin command is used simply to place text in the Message Window. It’s general form is as follows:
#Mwin(text$)
Where ‘text$’ is some literal value- either an actual literal variable or a literal value (text enclosed in quotation marks- ie. "This is text").
So, if you want to put text in the Message Window, just do something like the following example:
#MWin("Hello. This is text")
#MWin("Lalalalalala. This isn’t so hard.")
#Wait(a$)
Pretty simple stuff. That text gets placed in the Message Window, then the program waits for the user to press a key.
That’s great and all, but that doesn’t really change the way we do things. How do we blend text and variables together on the same line? The #Mwin command allows you to do this easily. Here’s an example:
#myname$="Chris"
#MWin("Hello, ")
#Wait(a$)
If you want to put a variable inside the body of the text, just enclose the name of the variable in < and >. In the above case, the output is "Hello, Chris", and it all occurs on the same line.
This can be really useful. For example:
#Prompt("What is your name?", myname$)
#MWin("Hello, . How are you?")
#Wait(a$)
This example uses a new command- the #Prompt command. The #Prompt command asks the player a question (the "What is your name?" part), and stores the response in a variable (in this case, myname$). Once the user has typed in his or her name, the computer says hello to them.
Notice how #Prompt uses two sets of data- the question and the variable to store the response to. These are called parameters, and parameters are always separated by the ‘,’ character. #Prompt has two parameters, whereas #Wait only has one (and so does #Mwin).
Another useful command when using the Message Window is #MWinCls. This command clears the text out of the Message Window giving you a clean slate. Its general form is as follows:
#MWinCls()
Notice that this command has parameters. You don’t have to send it any information- it just does what it’s supposed to do. *no*
It’s a good idea to clear the Message Window at the start of each program so that you have a clean slate to work with. Here’s an example:
#MWinCls() *Clears the message window.
#MWin("Hello, how are you?")
#Wait(a$) *Wait for keypress.
#MWinCls()
#MWin("I am fine.")
#Wait(a$)
The Message Window commands are the most used in RPGCode programs. From now on, I will use them exclusively (I won’t type just plain text anymore- I’ll use the #Mwin command).
***
Program Flow
I were the king of the world I would have a monkey for a pet.
So far all of our programs have run from the top to the bottom in perfect order. We’ve played with a few variables, but at this point they don’t seem to be of very much use. Well, here’s where programming becomes really powerful- program flow.
Program flow is basically just the way that the program runs. But instead of having the program run from the first line to the last line, we can make it stop in the middle, veer off course and do something else, etc. Now we’re going to make the computer actually to what the player types on they keyboard. *respond*
The most useful command in the entire programming world is the #If command. This command (or variations of it) is the cornerstone of programming language. The #If command allows you to do something only if something else is true. What does that mean? Well, here’s an example of an #If statement in everyday speech: *every*
**
If
**Then**
We take this for granted in our everyday speech, but let’s really look at this above statement. "If I were the king of the world", first of all. Is this statement true or false? If I the king of the world, then it’s true. In this case, I have a monkey for a pet. However, if I’m the king of the world, then I have a monkey for a pet. *am* *would* *not* *would not*
Notice that the stuff after "Then" only gets done if the stuff before "Then" is . In reality, I’m not the king of the world, so sadly, I have no monkey as a pet :-( *true*
So, what does this have to do with programming? Well, here’s the general form of the #If command:
#If ( ) { } *condition* *#command*
-or-
#If ( ) *condition*
*#command1*
#command2
etc...
OK, so what does all of that mean? Well, the #If command works very similar to our everyday speech. It tests if some is true, and if it is true, then one or more gets executed. If the condition isn’t true, then the commands don’t get executed. It’s that easy. *condition* *#commands*
As a side note, for you version 1.4 people, notice that #If now uses { and } brackets. You can still use the old < and > if you want, but this is the way I’m going to do it from now on.
So what is this that gets tested? Well, the computer checks if a variable is equal to something else. If it is, then the commands get executed. Here’s an example: *condition*
#testvar!=12
#If (testvar!==12)
#MWin("Yayy! The condition was true!")
* This command will get executed because testvar! *does*
* equal 12.
#If (testvar!==0)
#MWin("Testvar is equal to zero!")
* This command will get executed. testvar! is not *not*
* equal to 0, so the condition is false and these
* commands are skipped.
In the above example, only the first of statements is run (a block of statements are a bunch of commands enclosed in { and } brackets). Only the first set is run because "testvar!==12" is true (testvar! is equal to 12). Why the two equal signs? Well, that’s just the convention. If you really want, you can use equal sign, but I will use two from here on in. *block* *one*
Notice that the second block doesn’t get run at all. The condition "testvar!==0" is false- testvar! is not equal to zero, so the block that follows does not get run.
Notice also the way I indented my commands inside the blocks. This isn’t necessary, but it sure looks cool, doesn’t it? It just makes the code more readable.
#If can check more than just if a variable is equal to something. Here’s everything it can do:
**
Equal To (==)
Tests if two values are equal. Example:
#If (litvar$=="Hello") { #MWin("Hello to you, too.") }
**
Not Equal To (~=)
Tests if two values are not equal. Example:
#If (litvar$~="Hello") { #MWin("It doesn’t say Hello!") }
**
Greater Than (>), Less Than (<)
Tests if a value is greater than another value or if a value is less than another value. Example:
#If(myvar!>10) { #Show(myvar!) }
#If(myvar!<10) { #Mwin("It’s smaller!") }
**
Greater Than or Equal To (>=), Less Than or Equal To (<=)
Tests if a value is greater than or another value, or less than or another value. Example: *equal to* *equal to*
#If(myvar!>=10) { #Show(myvar!) }
#If(myvar!<=10) { #MWin("Smaller than or equal to 10!") }
OK, so let’s see the #If command put to practical use. In this example, we’ll make a little menu, and the user will press a button to make something happen:
*Little menu program showing the use of #If
#MWinCls()
#MWin("What do you want to do?")
#Mwin(" 1- Make me say something nice.")
#Mwin(" 2- Make me say something not so nice.")
#Wait(result$)
* The user will press a key and the result will be put in
* result$
#If (result$=="1")
*The user pressed ‘1’, so we say something nice.
#MWin("Hey, man, you are cool for pressing 1.")
#Wait(a$) *Pause for key press.
#If (result$=="2")
*The user pressed ‘2’, so we say something not as nice.
#MWin("You are a moron for pressing 2")
#Wait(a$) *Pause for keypress.
Here’s our first semi-practical program. The computer actually does something based upon what the user has done. The comments pretty much explain the program, so I won’t say anything about it except for this: What happens if the user doesn’t press ‘1’ or ‘2’? what if they pressed ‘m’ by mistake? Well, both #If statements would be false, and neither program block would get run. What do we do if the user press something different? That’s dealt with next... *does*
**
While Loops
Obviously, if the user didn’t press ‘1’ or ‘2’ in the above program, we’d want the computer to ask the user again to press a key. But that would mean writing the prompting code over and over again into infinity. Do we really want to do that? Well, no. We’ll use a while-loop instead. Before I go and explain a while-loop, here is what the above program would look like the while loop added onto it: *with*
*Little menu program showing the use of #If
#MWinCls()
#MWin("What do you want to do?")
#Mwin(" 1- Make me say something nice.")
#Mwin(" 2- Make me say something not so nice.")
#done!=0
#While(done!==0)
#Wait(result$)
* The user will press a key and the result will be put
* in result$
#If (result$=="1")
*The user pressed ‘1’, so we say something nice.
#MWin("Hey, man, you are cool for pressing 1.")
#Wait(a$) *Pause for key press.
#done!=1
* Breaks out of While-loop
#If (result$=="2")
*The user pressed ‘2’, so we say something not as
*nice.
#MWin("You are a moron for pressing 2")
#Wait(a$) *Pause for keypress.
#done!=1
* Breaks out of while-loop
Ok. Don’t get scared by all the indentation and {} brackets. The program is still the same program except now it has a While-loop inside it.
How does this work? Well, a While-loop is a block of statements that continues to run over and over again until some condition is true. Here’s the general form:
#While( ) *condition*
*#command1*
#command2
etc...
The works the very same as the condition of an #If statement. In this case, the stuff in the block will only get run if the condition is true. However, once the end of the block is reached, the program will skip back up to the #While command and test the condition again. If the condition is still true, the block will run again. Then it will skip back up to the #While statement. If the condition is true, the block will run again. The block will continue to be run over and over again as long as the condition is true. Once it is false, the stuff in the block won’t get run, and the program will continue along leaving the #While loop behind. *condition*
So, if you look at the modified program above, you will notice some things leading up to the while-loop:
#done!=0
#While(done!==0)
#Wait(result$)
Notice that first the variable done! is set equal to zero. Now when we come the the #While statement, notice that #While tests if done! is equal to zero. Well, done! equal to zero, so the following block will be run. *is*
Do you see that the first thing that the block does is wait for the person to press a key? Let’s look at the block more closely and see what it does...
#Wait(result$)
* The user will press a key and the result will be put
* in result$
#If (result$=="1")
*The user pressed ‘1’, so we say something nice.
#MWin("Hey, man, you are cool for pressing 1.")
#Wait(a$) *Pause for key press.
#done!=1
* Breaks out of While-loop
#If (result$=="2")
*The user pressed ‘2’, so we say something not as
*nice.
#MWin("You are a moron for pressing 2")
#Wait(a$) *Pause for keypress.
#done!=1
* Breaks out of while-loop
OK, the first thing it does is wait for the user to press a key. Let’s say the user pressed ‘1’:
That means that the first #If statement with it’s block of commands will be run. Notice that the #If stuff runs as usual, except at the end if it, #done! is set equal to 1.
Next we come to the next #If statement. It’s false, so it’s skipped over entirely.
And now we come to the end of the while-block. That means that the program skips back up to the top of the #While-loop and tests the #While condition. Remember- #done! was set equal to 1, so now the condition #done!==0 is false. That means that the While-loop doesn’t run again and the program ends.
Now, what if I had mistakenly pressed ‘m’?
-Well, we’d come to the first #If statement. It would be false, so we skip over it.
-Then the second #If statement. It also is false, so we skip over it.
-Now we come to the end of the while-block, which means that we skip up to the top.
-The variable #done! wasn’t changed anywhere, so it still equals zero, which means that the #While condition is true. The loop gets run again.
-The first command in the block waits for us to press another key...
-This will continue until I press a ‘1’ or a ‘2’ and those #If statements set me free from the #While loop by setting #done! equal to 1.
And there’s the solution- our program is now working the way it should. The program will actually wait until the proper ‘1’ or ‘2’ is pressed.
While-loops can be used in other ways, though. Let’s say you wanted to write some text 5 times. You can do it this way:
#count!=1
#While(count!<=5)
#MWin("Hello, there!")
#count!=count!+1
This small program first sets count! equal to 1. The While-loop runs as long as count! is less than or equal to 5. Inside the block, some text is written, and then count! gets 1 added to it. Notice that is will continue until count! equals 6 (it will have looped exactly 5 times).
Study this example so that you understand it. If you didn’t understand the big program, go back to it and study it once you have a firm grasp on this simpler example.
I will caution you about #While loops, though. If you’re not careful, you can easily lock up your program up with them. Look at this example ( ): **do not run this**
#count!=0
#While(count!==0)
#MWin("Lalala")
Notice that count! doesn’t get modified inside the while-loop. This means that count!==0 is true, and the while loop will continue into infinity. The only way out of a situation like this is to press CTRL-ALT-DEL together, and tell Windows to end the task. Obviously, this doesn’t look too good! So check your while loops before running them to make sure that they are not infinite! There is also a better form of the #While command- the #For command that makes infinite loops harder to get into. Check the command reference for a summary of this command. *always* **always**
***
Multitasking (This section is very important!!!)
Most programs you write will be programs that you set on the board using the Board Editor. However, Items that are placed on the board can run programs- that is, they can run while other programs are running at the same time. Multitasking programs work basically the same as normal programs, except for a few variations. *multitasking*
A multitasking program is usually set up as an infinite loop, because it usually just makes the item walk around the screen repeatedly. However, you must use a #While or #For loop to do this. The reason for this is that #While and #For loops use up computing time exclusively for themselves until their loops are done. This makes them fast, but also dangerous. To understand this, you must know how multitasking programs run... **not**
Let’s say you had 3 items on the board and each one of them was running its own multitask program. In reality, the computer really can only do one thing at a time, so these three programs computing time with one another. The way they share is by taking turns performing commands. Let’s say each program had 10 lines of code. Program 1 would run it’s first line, then program 2 would run it’s first line, then program 3 would run it’s first line, and then it would be program 1’s turn again. It would run line 2, then program 2 would run it’s line 2 and so on. Basically, the programs juggle computing time between one another. *share*
The problem is this: A #While (or #For)-loop and all it’s statements are considered to be command. In other words, if Program 1 had a #While loop somewhere, it would run the while loop until it was done, and then let Program 2 have it’s turn. ***one***
The problem with this is that we may be tempted to set p an infinite while or for-loop in one of or multitasking programs. In this case, Program 1 would continue to run its #While loop forever, and the other programs wouldn’t get their chance to do so. In this case, you must press CTRL-ALT-DEL to quit the Translator program.
This may seem sort of crazy since I’ve already told you not to set up an infinite #While loop. But, with multitasking programs, you may want to. For example, if you wanted a character item to wander around the board all the time, it would need an infinite loop. You may be tempted to do it this way:
#done!=0
#While(done!==0)
#Wander("target") *Causes the target item to wander.
The #Wander command causes the item to take one step in a random direction (see the Command Reference section). To make it take more steps, we must do this over and over again- an infinite loop. But this #While loop will eat up all the computing time and the player won’t even be able to do anything. So, instead, we can set up an infinite loop using the #Branch command:
:top
#Wander("target")
#Branch(:top)
The #Branch command causes the program to skip anywhere unconditionally. In this case, it continues to branch to the label ‘:top’. So, this acts as an infinite loop, but each command is performed separately. To do infinite loops with multitasking programs, you For more info on the #Branch command, see the Command Reference section. **must use the #Branch command!!!!!!**
***
Creating Your Own Commands
RPGCode2 allows you to create your own commands. This makes the language extremely flexible and infinitely expandable. Although there are 80+ built in commands, you may wish to create your own to make specific tasks easier. Apart from the built in commands, there is also a library of extended commands in the file system.prg.
In RPGCode, you define a new command with the #Method keyword. #Method defines a new method. A method is basically just a command- it works the same and looks the same. The general form of #Method is:
#Method ( ) *methodname* *parameter1, parameter2, ...*
Following the #Method declaration is a block of commands that tell the method what to do.
is the name of the method. Basically, this is what the command will be called. If you want to make a command called ‘#Pause’, then the method name would be Pause. *methodname*
The list of parameters allows you send variables to the method. We won’t worry about that right now.
The best way to understand methods is to actually see one. Here’s what I’ll use as an example:
There is a problem with the #Wait command. It will stop waiting for a keypress even if the user presses one of the arrow keys. This is usually OK, but usually when a player walks into a program, the buffer has a few more arrow presses, and the first few #Waits will be ignored. So I want to make a command that will just wait for the user to press a key, ignoring the arrow keys. So, I’ll make a method called ‘#Pause’:
#Method Pause()
#pause_done!=0
#While(pause_done!==0)
#Wait(pause_wait$)
#If(pause_wait$~="UP")
#If(pause_wait$~="DOWN")
#If(pause_wait$~="LEFT")
#If(pause_wait$~="RIGHT")
#pause_done!=1
#Kill(pause_done!)
#Kill(pause_wait$)
And there it is! Looks a little complicated, but it really isn’t. I’ll go over it step by step:
-First of all, the #Method declaration tells us that the command name is Pause. It has no parameters (the empty brackets).
-Next, we set up a While-loop. pause_done! is the conditional variable- the While-loop will keep running as long as pause_done! is equal to zero.
-Next, we wait for a key press.
-If the user did press an arrow key, the #Wait command puts the text "UP/DOWN/LEFT/RIGHT" into the variable. The next series of #If statements check if the key pressed was not equal to "UP", "DOWN", "LEFT" or "RIGHT". If they key pressed successfully survives these tests, pause_done! becomes equal to 1, which will break us out of the While-loop.
-If the user press an arrow, pause_done! will not be set equal to 1, and the while loop will start again, thus waiting for a key press again. *did*
-Once the While-loop is done, the last two commands (#Kill) delete the variables created by the method. It’s a good idea to #Kill method variables at the end of a method to reclaim memory.
OK, so how do you use this command? Simple:
#Pause()
Just like a regular command. But if you were making a program, where would the method declaration go? Well, here’s an example of a program which uses the #Pause command:
#MWinCls()
#MWin("Try pressing an arrow key!!!")
#Pause() *Pauses for key press, ignoring the arrows.
#Method Pause()
#pause_done!=0
#While(pause_done!==0)
#Wait(pause_wait$)
#If(pause_wait$~="UP")
#If(pause_wait$~="DOWN")
#If(pause_wait$~="LEFT")
#If(pause_wait$~="RIGHT")
#pause_done!=1
#Kill(pause_done!)
#Kill(pause_wait$)
The actual method declaration is ignore by the computer unless it is actually called. So, after the #Pause command has been executed, the program ends, because the computer ignores the entire method block.
**
Creating Libraries
As you can see, a method declaration can take up quite a bit of space in your program. Wouldn’t you rather use your own methods without having to type them out everytime they are to be used? Well, you can. You can do this by creating libraries.
A method library is just a regular .prg file that simply contains method declarations for a number of commands. For example, we could put the method declaration for #Pause into a file called "pause.prg". We can call up this library from any program using the command #Include. Here’s an example of the same program but this time, the #Pause method declaration is in a file called "pause.prg":
#Include("pause.prg") *Imports the ‘pause’ library.
#MWinCls()
#MWin("Try pressing an arrow key!!!")
#Pause() *Pauses for key press, ignoring the arrows.
This program sure is a lot smaller and nicer looking. The #Include command just opens up the file ‘pause.prg’ and gives you access to the methods in that file. We can therefore use the command #Pause(), because the method declaration for #Pause is stored in ‘pause.prg’.
**
Passing Parameters
So far we’ve made a method that does not have any parameters (the brackets were empty). However, usually you will want to send information to your method. This is done by passing parameters to the method.
As an example, let’s consider a method called #Add, that jus adds two numbers together:
#MWinCls()
#MWin("I’m about to call the #Add method...")
#Add(2,8,mynum!)
#MWin("The result is: ")
#Method Add (add_num1!,add_num2!,add_dest!)
#add_dest!=add_num1! + add_num2!
#ReturnMethod(add_dest!)
*Now to #Kill of the variables.
#Kill(add_num1!)
#Kill(add_num2!)
#Kill(add_dest!)
This small program demonstrates a method which accepts parameters. The function itself is sort of useless- it adds two numbers together. This could be done using regular variable addition, but it is good as an example.
Take a look at the calling command (the command that calls the method):
#Add(2,8,mynum!)
This command passes three parameters to the method: 2, 8 and mynum!. What happens to these parameters? Well, look at the method declaration:
#Method Add (add_num1!,add_num2!,add_dest!)
This also has three parameters, except that hey are all variables. The parameters inside the method must be variables. always
Anyway, the parameters in the calling command end up being put into the parameters of the method declaration. In other words, add_num!=2, add_num2!=8 and add_dest!=mynum!
As you can see, this is a handy way to send a method information. Also, notice my naming convention. I used the name of the method, then a underscore, then a descriptive name for each variable. I do this so that it is unquestionable that those variables in that parameter list belong to the #Add method. This way, if the #Add method were to call another method, the other method probably wouldn’t interfere with #Add’s variables. This is a good idea and you should do this!!! Otherwise, bugs can start running around your programs and you won’t even know what’s going on!
Now, look at the command I used in the #Add method: #ReturnMethod. This is used to pass information from the method back to the calling command. In the above case, I did this:
#ReturnMethod(add_dest!)
This command takes the parameter add_dest! and corresponds it back to the equivalent calling parameter. In other words, mynum!=add_dest! In this way, a method can send the command that called it some information. The calling command can do whatever it wants with that information. In the above program, I just printed mynum! out in the Message Window, showing the result of adding 2 and 8.
Using parameters and the #ReturnMethod command, you can make your own commands, and they will be entirely indistinguishable from regular commands. You can make your own libraries to do specific things (like a drawing library that draws houses on the screen, that sort of thing).
For more information about methods look in the command reference section and look up #Method and #ReturnMethod.
**
The System Library
The Toolkit comes with a standard system library that has some methods in it that extend the RPGCode language beyond the 80+ built in commands. This file is called "system.prg".
The system library has the #Pause command inside it that we talked about earlier. So, If you want to use the #Pause command, you have to #Include("system.prg") at the start of your program. You will notice that I have done this in the demo game that comes with the Toolkit.
The system library has some other commands, too for working with arrays, which is not something that has built-in support in RPGCode. Using the system library, though, you can use arrays if you need to.
You can open the system library in any text editor and examine it for yourself. Each method has a short description that says what it does and how to use it.
***
Reserved Variables
There are a number of variables that are set automatically by the system and cannot be changed. They are as follows:
BoardTitle[1]$ -> BoardTitle[8]$- The titles of the 8 layers on the board.
Constant[0]! -> Constant[10]!- The 11 board constants set in the Board Editor.
playerX[0]! -> playerX[4]!- The x position of the 5 players on your team.
playerY[0]! -> playerY[4]!- The y position of the 5 players on your team.
playerLayer[0]! -> playerLayer[4]! - The layer of the 5 players on your team.
playerHandle[0]$ -> playerHandle[4]$- The handles of the 5 players on your team.
GameTime!- The total game time, in seconds.
Music$- The filename of the music playing in the background.
BoardSkill!- Fighting skill for current board.
BoardBackground$- The fight background file for the current board.
You can access these like any other variable, but you can’t change them.
**
Target Handle
There is a special handle name called "Target" that refers to the currently selected player, item or enemy. For example, if a program was being run from the internal menu and the User clicked on a player, you could get that player’s HP by using:
#GetHP("Target",hishp!)
In this case, instead of using the player’s actual handle, "Target" produced the correct result. This can also be used to push the target item around to create walking villagers, etc. All commands that can use "Target" as their handle are explained in the Command Reference section.
