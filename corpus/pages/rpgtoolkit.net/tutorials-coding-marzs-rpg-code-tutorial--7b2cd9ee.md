---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/tutorials/coding/marzs-rpg-code-tutorial/"
site: "rpgtoolkit.net"
title: "September 7th, 2008"
original_url: "http://rpgtoolkit.net/tutorials/coding/marzs-rpg-code-tutorial/"
written: "2008-09-07"
date_confidence: "day"
updated: null
captured: ["20110318071458"]
author: null
repliers: []
authors: []
comments_present: 0
f_description: "Adds"
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/tutorials/coding/marzs-rpg-code-tutorial/index", captured: "20110318071458", sha256: "3bca4ca3346b04f334854d661cdb674bf9da8b7cd92fa99382b536d1da4e6408", wayback_url: "https://web.archive.org/web/20110318071458/http://rpgtoolkit.net/tutorials/coding/marzs-rpg-code-tutorial/"}
---

# September 7th, 2008

[![Marz](thumb/80/community/images/avatars/upload/86425383345de15b08496f.jpg)](member/marz/)
Published
**September 7th, 2008**
Read times **2,291**
Written by Marz
Marz's RPG Code Tutorial
**Series of tutorials for those new to RPG Code that are looking to learn the foundations of programming with the Toolkit.**
1. Chapter 1 - Learning the Basics
2. Chapter 2 - Structure and Flow
3. Chapter 2 - Structure and Flow Continued (2)
4. Chapter 2 - Structure and Flow Continued (3)
5. Chapter 3 - Functions and Methods
6. Chapter 3 - Functions and Methods Continued (2)
7. Chapter 4 - Game Applications
8. Chapter 4 - Application 1: Conversations
9. Chapter 4 - Application 2: Mercenaries
10. Chapter 4 - Application 3: Custom MWin
11. Chapter 4 - Review Exercises
12. Chapter 5 - Arrays
13. Chapter 6 - Graphics with Canvasses
14. Chapter 7 - Introduction to Classes
15. Chapter 8 - More About Classes
*I am in no way an expert, and the way this tutorial is written in no way implies that this is the correct way to code, nor is it the most optimized method.*
Chapter 1 - Learning the Basics
- Introduction
- Variables and Scope
- Variable Manipulation
- Naming Conventions
- Commenting
- Conclusion
Introduction
RPG Code is the scripting language used by the Toolkit in order to achieve anything from a simple message window to something as complex as a fully functional battle system. Given its flexibility, RPG Code can be relatively difficult to understand. Achieving basic features found in games for those without knowledge of other programming languages will be at a loss on how to structure their program files. This tutorial aims to remedy that by providing some knowledge on programming and using RPG Code syntax.
Variables and Scope
If you were to do calculus without variables, it would be pretty useless. Using variables is essential in any programming language you will learn, but understanding when and how to use them (as well as how they should be named) are important matters.
: a quantity that can assume any one of a set of values, such as text and numbers. **Definition - Variable**
: the name of a variable. **Definition - Identifier**
You can imagine that a game without variables would be very dull. Everything would be constant: a player's fight power would never change, there would be no "trigger events" (e.g. you can only go to the Deku Tree if you are wielding a sword and shield - that can't happen without variables), etc. In 3.1.0, we no longer have to worry about the "type" of a variable. That is, the Toolkit will now determine whether the variable is numeric or literal (contains a number or combination of letters). There are some apparent advantages here (like being easier), and if you were programming with previous versions of the TK you will no longer have to use functions like castLit(). Anyway, onto the actual code. In RPG Code we seek to define a variable with a name (identifier) as well as its value. We end the statement with a semi-colon ( ; ). Think of this semi-colon as the period at the end of a sentence, where each sentence needs one to be considered a complete statement. x = 1; y = "Thing"; Here I've created a variable, given it the name "x", and assigned it a numerical value of 1. What actually happens in your computer is the compiler allocates this special space in memory for a value, then it puts the value you assigned (1, in this case) to that memory space. It will stay in that space until the of your program ends. Similarly y gets a literal value "Thing" and the same thing happens. One thing to understand about variables is how long they "live" in memory. In other words, depending on how and where you declare a variable, it could live the entire length of the game, or for only a few seconds. A variable's lifetime is called its scope. : The boundaries in which a variable is accessible.
*scope*
**Definition - Scope**
**
Definition - Local Scope : The variable's boundaries are local to the prg file after which it is initialized : The variable is accessible to all program files in the entire game, provided it is initialized correctly. Understanding the scope of your variables can help keep your code neat and allows you to reuse common variable names in other programs. It is important to have a firm foundation on how scope works, otherwise you could be trying to access a variable that is no longer there. For instance, suppose I have created a local variable called "text". I use this variable throughout the prg file and everything is fine. Then in another prg file I attempt to access this same variable, but the compiler has no idea what I'm talking about. This is a failure to understand the scope of my variable "text" (Do you understand why?). Scope will become more important when we get into some later chapters of this tutorial, where determining whether a variable is global or local is a strategic decision that could make programming your game easier or harder. I'll delve a little further into it in this chapter, but its power becomes clear in the next chapter. Until then, here's some basic syntax on how to declare a variable with a certain scope: local (x); global (y);
**Definition - Global Scope**
Variable Manipulation
The ability to manipulate variables is what makes them dynamic. Manipulating variables is similar to algebra in many ways. We can manipulate a variable using some very basic and familiar techniques. It should be easy for you to understand what the following does: a = 8; b = 4; c = a + b; In case it's not obvious, the variable c here is now set to 12. One thing to note, however, is the order in which I set up the code. Suppose I had this instead: a = 8; c = a + b; b = 4; What would happen? In the RPG Code sense, b would be equal to 0, and thus c would be 8. In other more strict languages (such as C++) you would receive an error because b had not been initialized yet. Luckily the Toolkit catches this mistake and fixes it for you (for better or for worse). The point of this example is to make sure that variable you are trying to access is available in the scope.
Table 1: operators for numerical variable manipulation
**Operator**
Adds
Multiplies
Subtracts
Divides
The + operator seen above is very common in math and it's safe to say that by the age of 5, everyone has some concept of addition of numbers. In programming, the + operator can be used for several other things as well. For example, we can concatenate to strings using the + operator: a = "Hi"; b = "there"; c = a + b; The result here sets c to "Hithere". This probably isn't what we wanted, most people would want a space between the two words. Thus it is required for you to space out the variables yourself. So a solution to this problem is: a = "Hi "; Notice the space after Hi before we end the quotation mark. Perhaps another niffty feature is the ability to concatenate strings on the fly. Suppose you asked for the player to input a character name at the beginning of the game, and saved it in a variable called charName. Later on in the game, his best friend wants to talk to him: message = "Hi there " + charName + "!" Assuming charName was Vampz, the message would say "Hi there Vampz!" While the + operator can be used with literal variables (also called strings), we cannot use the other operators listed in Table 1. That is, the following will give you "garbage" results (in computer jargon, garbage means something useless): a = "High"; b = "Hi"; c = a - b; d = a * b; e = a / b; In case you're wondering, c and d will give you 0, and e will give you "-1.IND"... in other words, pure garbage :). Also, if you're wondering how to check what a variable is, use the following: show(x); wait(); Where x can be any variable. We'll go over more about functions at a later date.
Naming Conventions
You'll notice in several of my above examples, I used letters of the alphabet as names of different variables. While this is fine for purposes of such simple examples, it can become quite hard to read code for large games when the variable names are a1, b1, a2, b2, etc. It is important to give variables a meaningful name that's not too long and easily understood. Recall from an earlier example that I used the variable charName for the character's name used in the game. Let's compare this variable name with some other alternatives: charName cName characterName name cheese The only other decent alternative could be cName. The other alternatives either make no sense (cheese), are too vague (name), or are too long (characterName). You'll also notice that with each variable that had two "words" in it, the first word is all lowercase, while the second word has its first letter capitalized. Which one is easier to read: 1. charName 2. charname I certainly hope you think it's the first one, and even if you don't, most people still choose the first one anyway. It is a common naming convention used. Another convention used are for constant variables. A constant is a variable that never changes (or should never change), and its value is determined at the time of initialization. An example of a constant is pi. When naming a constant, we usually use all capital letters, so: PI = 3.14159; What happens if the constant is more than one word though? Well, then we use an underscore (_): ARRAY_SIZE = 10; In RPG Code, there is no definitive way of declaring a constant, so having the name as all uppercase reminds you not to change its value throughout the program. There are many other naming conventions out there, but for now these should be sufficient for what we will be programming.
Commenting
When you start programming your game you'll realize it's going to take forever to finish. This of course means several breaks that could go on for months on end while you start another project, play other video games, or take a vacation. When you come back, you're staring at possibly 100 different prg files. All of a sudden your left with daunting task of figure out what you were trying to accomplish in the program you've written way back when. Using the naming conventions above, you can develop a good understanding of what you're doing to each variable on each line. But sometimes code gets complicated. Complicated enough that basic English should be used to explain what's going on. If we write basic English in our program, we'll get an error because Toolkit doesn't understand English (it understands RPG Code). However, the toolkit does understand how to ignore something: b = 2; //Set b equal to the value 2 In this line of code, the compiler will perform b = 2; as it normally would. Then it sees //, and ignores the remainder of the line. This allows us to write "comments" about our code after the //. Of course, be careful of where you're commenting, because you usually don't want to comment out code (unless you think it's causing an error) like this: // b = 2; Set b equal to the value 2 Here we just commented out the entire line, so b = 2; will never get executed. Sometimes we'd like write a little bit more than one line of code. One way to do this is: // First line // Second line // Third line Thankfully, there is an alternative: /* First line Second line Third Line */ Everything in between the /* and */ is ignored by the toolkit, safely allowing you to write paragraphs of comments. Before I conclude the first chapter, I've failed to mention how/when you should comment. Paragraphs of comments are undesirable, as it might be easier to just read the code. Similarly, the comment above for b = 2; is unnecessary, as it should be pretty obvious what the statement b = 2; does. Comments should be reserved for complex logic in your programs that you know you or someone else will have trouble understanding later. Do not riddle you're entire program file with comments, and at the same time make sure there is adequate commenting to understand the more difficult lines of code.
Conclusion
This marks the end of the first part of this tutorial. Please leave any questions below, or notify me of any mistakes I might have made. I do apologize if this reads too much like a textbook, that's all they make you read in University.
In the last section we learned how to declare and initialize variables. Now we're going to take a look at some code that can help alter the flow and structure of our code. Used correctly, we can effectively optimize our code for best performance. Used incorrectly, and we could end up with some very sloppy code that doesn't work as intended. Using If-statements and loops are very handy in the programming world and are considered "required knowledge". Before we begin our discussion, I forgot to mention something about variable manipulation in the last chapter. Something very important of course. In math class, the following is illegal: a = a + 1 In case you don't know why, subtract a from both sides of the equation and you end up with: a - a = a + 1 - a 0 = 1 But clearly, 0 does not equal 1. In programming, however, the statement a = a + 1 is very much legal, and used commonly. How does it work? Let's see an example: a = 4; a = a + 3; What happens in programming is the right-hand expression is determined first. So on the second line, we have 4 + 3. Then once that expression has been determined it is stored into a. Essentially what is happening is the computer is using the last known value at the variable a to determine the right-hand expression. This information's usefulness will become apparent when we talk about counted loops later in this chapter. Note that there are many ways of using this information: a = 4; a = a*2; // results in a = 8 b = "Hello"; b = b + " World"; //results in b = "Hello World" We will start our discussion with a problem mentioned in the last chapter. In the Ocarina of Time, Link can't see the Deku tree until he has a sword and a shield. While we know how to use variables, we still don't know how to compare these variables, and then use the result of this comparison accordingly. The solution is an If-statement. Most of our decisions are a direct result of if-then-else statements, so let me explain through use of examples: Whenever we decide to do something, we usually ask ourselves at least one "if" to see if we should indeed do it. In programming, this is extremely common. In order for our program to make decisions and make our game world seem interactive, we too should be able to do basic if-then-else statements. In this section we'll discuss some basic pseudo code with if-statements, go over three key comparison operators (logical AND, logical OR, and NOT), and then wrap up with some actual code of an if-statement. To start, here's a little bit of pseudo code for you: Before we continue, you will notice some curly brackets { and } in the above pseudo code. Between these curly brackets, we can put several lines of code (hundreds, if you'd like). The code in between these curly brackets is called a "block". So "the block of code for the if-statement" refers to the code in between the curly brackets for the if-statement, and "the block of code for the else statement" refers to the code in between the curly brackets for the else-statement. How can we achieve the above code? Through the use of variables as well as comparison operators. To note, the expression in between the brackets, "have sword AND have shield" is the conditional expression (or statement). If the condition is true, the first set of curly braces (allow entry) is run, if not, the second set of curly braces is run (do not allow entry). Now, we've covered variables, so let's define two variables first: kokiriSword = 0; woodShield = 0; These are two variables that I've initialized to 0. When Link picks up the kokiri sword, then in that program I would set: kokiriSword = 1; And I would do the same thing for woodShield when he buys the wooden shield. So now that Link has his sword and shield, let's check for it: if (kokiriSword == 1 && woodShield == 1) You should notice two new things from the above if-statement. The first is the use of the operator ==, and the second is the use of the operator &&. The == operator (note this is note the same as the = operator!) checks the value in the left variable (e.g. kokiriSword) and the value in the right variable (e.g. 1). If they are the same, it returns TRUE, otherwise FALSE. So assuming link has both the sword and the shield we are now left with: if (TRUE && TRUE) The && operator checks if both the left variable and the right variable are true. If they are, it returns TRUE itself, so now it reduces to: if (TRUE) This is the result we wanted. If you'll recall the examples above (e.g. If I am hungry...), we checked if something is true, and then completed an action. Here we are doing the same thing. What happens though, if Link has the shield but not the sword? Well, let's look at a table (called a truth table): Notice from Table 2 that the only time && (called logical AND) will return TRUE is when both kokiriSword == 1 and woodShield == 1 are TRUE? This is how the && operator is defined, and will always function. I should also mention that, in RPG Code, TRUE is equivalent to 1 and FALSE is equivalent to 0. This means that using the == operator like this: x = 2 == 2; would result in x = 1 rather than x = TRUE. So while we as people think in TRUE and FALSE, remember that the computer thinks in 0s and 1s. There are several other comparison operators at our disposal, and most of them we will understand from basic English. For example the logical OR operator (signified with '||') can be defined with the following truth table: Here we see that the logical OR operator will return 1 for every possible value except when neither input 1 nor input 2 are true. For an example, imagine a picky eater who will only eat steak or lobster for dinner. If dinner consists of both steak and lobster tail, then the picky eater will eat dinner (and depending on how fat they are, they may eat both the steak and the lobster tail). If steak or lobster tail is unavailable, they will refuse to eat. One very useful comparison operator, and the last one we'll take a look at, is the NOT operator. It basically "inverts the truth" or returns the "opposite of the truth". Let's try a similar example to the above. Imagine there is a very non-picky eater. The guy will eat almost anything. The only thing he won't eat is fish. So, to test for this: Note, that this does the exact same thing as the below example (except they do it in an opposite fashion): We can also invert numeric variables. For example: x = 1; x = !x; //Now x = 0 There are many other comparison operators available to you when using RPG Code, and they can be found by clicking . You can ignore the bitwise comparison operators for now. What we've seen so far are the most commonly used and should be sufficient. Before we wrap up this section, here's an example of actual syntax: Note that we can put anything in between the { and }, including functions/methods (which we'll see next chapter). So far we've taken a look at single If-then-else statements: one possibility leads to one result or the other. Sometimes, however, it is necessary for us to check several different possibilities. This is solved with multi-way if-statements, and is gone over in the next section.
*I am in no way an expert, and the way this tutorial is written in no way implies that this is the correct way to code, nor is it the most optimized method.*
Chapter 2 - Structure and Flow
- **Introduction**
- **If-Statements and Comparison Operators**
- Multi-Way If-Statements
- Switch Cases
- Loops: Counted
- Loops: Dynamic
- Nesting
Introduction
If-Statements and Comparison Operators
- If I am hungry, then I will eat.
- If I am thirsty, then I will drink. Otherwise, I will play video games.
- If I am bored, then I will play video games. Otherwise, I will study.
- If I have a sword and shield, I can see the Deku Tree. Otherwise, I can't.
**Example 1**
```
if (have sword AND have shield) { allow entry } else { do not allow entry }
```
Table 2: Truth table for && Operator
**kokiriSword == 1**
**woodShield == 1**
**&& Result**
FALSE
FALSE
FALSE
FALSE
TRUE
FALSE
TRUE
FALSE
FALSE
TRUE
TRUE
TRUE
**Check Point Exercises**
1. What is the value of the variable 'a' after the program below gets executed?
```
if (1) { a = 4; } if (0) { a = 7; } if (1) { a = a+2; } if (0) { a = a-4; } 2. What is the value of 'test' after the below code is executed? a = 1; b = 0; c = 1; test = a == b; test = test == c;
```
Table 3: Turth table for || Operator
input 1
input 2
OR Result
**Example 2**
```
if (dinner == steak || dinner == lobster tail) { eat dinner } else { refuse dinner }
```
**Example 3**
```
if (dinner ~= fish) { eat dinner } else { refuse dinner }
```
**Example 4**
```
if (dinner == fish) { refuse dinner } else { eat dinner }
```
**Example 5**
dinner = 1; //Dinner is served fish = 0; //there is no fish available steak = 0; //there is no steak available
```
if (dinner == fish || dinner == steak) { eat = 1; //We will eat } else { eat = 0; //We will not eat }
```
Once again we will look at a problem. Suppose the player in your game is talking to an NPC (named Bob) and Bob just finished talking. We present the player with three choices of how he'd like to reply to Bob. When the player selects his choice, we store that choice in a variable called x (which can be 1, 2, or 3). Now we want Bob to react to the players reply. Using the knowledge we have so far, we may go about it like this: The problem with this is that it is inefficient. The RPG Code compiler will do the first check (x == 1), then the second, then the third. But had the player chosen the first option, why should we check the other two? We know they will return false. This should be intuitive to you. If it is not, think about it again. If x = 1, and we've already checked x == 1, why should we check x == 2, and x == 3? It should also become apparent, then, that order is important in if-statements. What you check first, second, third, etc could result in better or worse efficiency. A solution to our inefficiency problem is the "elseif" statement. If you'll recall with the if-then-else statement, if the conditional expression for the if-block returns true, then only that if block is executed. If not, the else block is executed. In this case, the same is true, except you can think of the else statement looking at another conditional expression before determining whether or not to execute. Take a look at Example 2 for one possible solution: Now let's go through Example 2 step by step. If x is 1, then we execute Reaction 1, and skip over to Rest of Code. Otherwise, we skip over Reaction 1, and check if x is 2. If it is, we do Reaction 2. Otherwise, we skip over both Reaction 1 and Reaction 2, and execute Reaction 3 no matter what. I purposely did this to point out what if x is 4? or 5? No matter what x is, if it isn't 1 or 2, Reaction 3 will get executed. Depending on how you accepted input, this could produce undesirable results. With the knowledge we have up until now, Example 3 shows the best solution to the problem. Here we only allow 3 error-free solutions. If x is not equal to 1, 2, or 3, then we tell the player he's an idiot for choosing an option that doesn't exist. This is probably a good time to bring up that the player is always an idiot. When programming, you should always expect the player will do something outside of the boundaries and try to break your program. You have to anticipate this, and program for the cases where this can occur. In most cases, checking for these errors will be done with If-statements. So far we've done our comparisons with numeric variables. Be advised it is also possible to use literal values (words). Example 4 shows how a webmaster can ensure that no body chooses his name when they sign up at the site. Sometimes we're checking a long list of possible values. This means a huge amount of if-elseif-else statements. Imagine if you had given the player 15 choices of different classes he can choose (e.g. Warrior, Mage, Necromancer, etc). It can become pretty tedious to do this with multi-way if-statements. The answer is the switch case, which is a little easier. Example 5 shows the syntax for a switch case: Now let's dissect the code above. The "switch(x)" states which variable we are comparing, in this case it is x. So now the program knows we are comparing x, but with what? The answer is found in "case *", where * is 1, 2, 3, etc. What the following ends up doing is if (x == 1) ... elseif (x == 2) ... elseif (x == 3) ... etc You may notice that there is no "else" statement above, it's all just a bunch of elseif's. In a switch statement, we accomplish an else statement with "default". Example 6 illustrates this. One thing to mention is that the switch-case statement also works for literal values (unlike some other languages). So Example 7 is also perfectly valid.
*I am in no way an expert, and the way this tutorial is written in no way implies that this is the correct way to code, nor is it the most optimized method.*
Chapter 2 - Structure and Flow
- Introduction
- If-Statements and Comparison Operators
- **Multi-Way If-Statements**
- **Switch Cases**
- Loops: Counted
- Loops: Dynamic
- Nesting
Multi-Way If-Statements
**Example 1**
```
if (x == 1) { Reaction 1 } if (x == 2) { Reaction 2 } if (x == 3) { Reaction 3 }
```
**Example** **2**
```
if ( x == 1) { Reaction 1 } elseif (x == 2) { Reaction 2 } else { Reaction 3 } Rest of Code
```
**Example 3**
```
if ( x == 1) { Reaction 1 } elseif (x == 2) { Reaction 2 } elseif (x == 3) { Reaction 3 } else { Report Error } Rest of Code
```
**Check Point Exercise**
Answers to last check point Exercise: (1) a = 6, (2) test = 0 1. What is the value of 'b' after the following code is executed? Hint: Go step by step!
```
x = 1 == 1; y = 1 || 0; if ( x && y) { b = 2; } if (x || y) { b = 3; } else { b = 4; }
```
**Example 4**
```
//Let x be the name requested a = "Xavier"; b = "Vampz"; if ( x == a || x == b) { result = "That name is taken!"; } elseif (x == "Marz") { result = "That name is too Holy for you."; } else { result = "Thank you for selecting a name"; }
```
Switch Cases
**Example 5**
```
//Let x be the class chosen switch(x) { case 1: { className = "Warrior"; } case 2: { className = "Mage"; } ... case 15: { className = "Necromancer"; } }
```
**Example 6**
```
//Let x be the class chosen switch(x) { case 1: { className = "Warrior"; } case 2: { className = "Mage"; } ... case 15: { className = "Necromancer"; } default: { className = "Oyerth"; // The default class if none are chosen } }
```
**Example 7**
```
//Let x be the class chosen switch(x) { case "a": { className = "Warrior"; } case "b": { className = "Mage"; } ... case "c": { className = "Necromancer"; } }
```
**Checkpoint Exercise**
Answers to the last Checkpoint Exercise: (1) b = 3 1. Rewrite the code in Example 3 in Switch Case form (no answer will be provided).
Before we continue to counted loops, I'd like to go over some arithmetic operators that I skipped earlier. The following table details other arithmetic operators that will be useful to you in coming chapters. For a list of all arithmetic operators, click . It is common place in programming that you want to perform an operation a certain number of times. Let us suppose that we want to accept and interpret input the player gives us 3 times. For this, we will use the wait() function. Functions will be explained in the next chapter. For now, all you need to know is that the wait() function tells you what key was pressed by the user. So if I said: input = wait(); Whatever the user pressed on his keyboard would be stored in input. For example, if the user pressed the key x, then input would have the value "x". Given that we don't know how to create a counted loop just yet, let's take a look at what we can do with what we know. Below is a modified version of Example 3 from the last page that would ask the user for input 3 times and react accordingly. That's a pretty long piece of code! And if you'll notice, it's just 1 piece of code copied and pasted 3 times. In programming, it is generally frowned upon to repeat code unnecessarily. Before I explain the solution, let me pose another problem. What if you change your mind, you don't want to query the user 3 times, but rather 5? Well, off you go copying and pasting again. What if you wanted to query the user 10 times? As you can see, the code gets even longer. The solution is a counted loop (more well known as a for loop). A for loop requires 3 things: One way this works is we give the for loop a counter (a variable, i) and we start the counter at 0. We tell the for loop to keep going until this counter variable i reaches a certain number (using a conditional expression), and then we tell the for loop how fast the counter variable will be increasing. The general syntax for a for loop is as follows: for (counter; conditional expression; increment) Notice that each statement is separated by a semicolon. This is required. A common pitfall is programmers using a comma rather than a semicolon. This does not produce the desired results, so do not do it. Now let's take a look at the example above through use of a for loop. Much shorter! There are a few things we should note here. First is to recall that i++ is the same as i = i + 1 (refer to Table 3 above). So now let's identify what we gave the for loop: The above code will execute 3 times. For more proof, let's go through it step by step. One thing you'll notice is that i isn't incremented right at the beginning, but rather once we reach the end of the loop. This is an important point to remember. Another tidbit of useful information is that we can use i inside the loop. Example 10 demonstrates this. In Example 10, the loop is iterated 10 times. In those 10 times, x is incremented a certain amount. How much? The answer is not intuitive, and can be more easily solved using a trace table: I chose a relatively complicated example here so that I could show you the power of a trace table. Sometimes, when you don't understand why your program is behaving weirdly, it may be necessary to go through it step by step, and record what's going on. This is when you could use a trace table to your advantage. You can also use something called a "debugger", but I don't know if the RPG Toolkit has a debugger, nor do I know how to use it if it did. There are many cases in which we don't know how many times we want a loop to be iterated. A for loop needs to know how many times it will iterate, however, and so we can't use a for loop. The solution is another common programming construct called a "while" loop. An English example is as follows, "While I am not hungry, I will develop my game on the RPG Toolkit". This defines 2 things. The first is the conditional expression "While I am not hungry". As long as I'm not hungry I will execute the block of code "I will develop my game on the RPG Toolkit". The while loop does not care what happens when I do become hungry. It only knows that while I'm not hungry, I will be developing my game on the RPG Toolkit. The while-loop in programming is just as straightforward as the above example. It will execute until a certain condition is met. You may notice, then, that it is possible to create a for loop using a while loop. This is in fact correct, and is shown in Example 11. Example 11 works exactly like a for loop would, but it does not take advantage of the while loops capabilities. Before continuing, I should discourage you for using the above method for a counted loop. Use a for loop instead. Now the question arises how might we use a while loop to our advantage? Recall Example 3. We took the users input, and then provided him with a reaction or an error. What happened when there was an error? More importantly, what didn't happen? The user was not asked the question again. We can ask him again until he gives us a right answer using a while loop. Think about it like this: "While you give me an answer I'm not looking for, I will keep asking you the same question." Example 12 displays perhaps the most useful program we've coded to date. First remember that ~= means "not equal". So we are saying that while the input isn't 1, 2, or 3, keep asking the question. Also notice that while the input isn't 1, 2, or 3 then reaction = "I'm sorry, I didn't understand you." This is a great way to keep asking the user for vital information (like a character's name). In the above programs, there are several blocks of code. In example 12, there are 5. The first being the main block of code inside the while loop. The other 4 being the if, elseif (x2), and else statements. You can have several blocks of code in other blocks of code. When you do this, it is called "nesting". To illustrate this, Example 13 shows how we can achieve the same functionality as elseif using a nested else and if-statement. As you can see, nesting can get pretty sloppy (thank god we have that elseif construct). We always indent with one tab for each nested statement. This keeps the code legible. After reading this chapter you should know and understand the following: In the next chapter, we will be looking at functions and methods, as well as detailing how to get important information from the command reference provided by the toolkit. It starts to get nitty gritty from there, so make sure you understand the first two chapters very well.
*I am in no way an expert, and the way this tutorial is written in no way implies that this is the correct way to code, nor is it the most optimized method.*
Chapter 2 - Structure and Flow
- Introduction
- If-Statements and Comparison Operators
- Multi-Way If-Statements
- Switch Cases
- **Loops: Counted**
- **Loops: Dynamic**
- **Nesting**
Table 3: Other Arithmetic Operators
Operator
Equivalent
a += b;
a = a + b;
a = a + 1;
a -= b;
a = a - b;
a = a - 1;
a *= b;
a = a * b;
a /= b;
a = a/b;
Loops: Counted
Example 3 modified **Example 8 (** **)**
```
x = wait(); if ( x == 1) { Reaction 1 } elseif (x == 2) { Reaction 2 } elseif (x == 3) { Reaction 3 } else { Report Error } x = wait(); if ( x == 1) { Reaction 1 } elseif (x == 2) { Reaction 2 } elseif (x == 3) { Reaction 3 } else { Report Error } x = wait(); if ( x == 1) { Reaction 1 } elseif (x == 2) { Reaction 2 } elseif (x == 3) { Reaction 3 } else { Report Error } Rest of Code
```
- A counter
- A conditional expression
- How fast the counter increases
**Example 9**
```
numQueries = 3; for (i = 0; i < numQueries; i++) { //Start of loop x = wait(); if ( x == 1) { Reaction 1 } elseif (x == 2) { Reaction 2 } elseif (x == 3) { Reaction 3 } else { Report Error } } //End of loop Rest of Code
```
- The counter: i is the counter, and it starts at 0.
- Conditional Expression: The condition is that the for loop keeps going while i < 3. The second i = 3, the for loop will exit, and Rest of Code will be executed
- Increment: The counter increases at a rate of 1 after each execution.
- Initialize i to 0
- Is 0 < 3? Yes, execute block
- Now at end of loop, increment i by 1
- Is 1 < 3? Yes, execute block
- Now at end of loop, increment i by 1
- Is 2 < 3? Yes, execute block
- Now at end of loop, increment i by 1
- Is 3 < 3? No, 3 = 3, go to next instruction after End of loop
**Example 10**
```
x = 0; for (i = 0; i < 10; i++) { x = x + i + 2; }
```
**Value of i**
**Value of x**
x = 0 + 0 + 2 = 2
x = 2 + 1 + 2 = 5
x = 5 + 2 + 2 = 9
x = 9 + 3 + 2 = 14
x = 14 + 4 + 2 = 20
x = 20 + 5 + 2 = 27
x = 27 + 6 + 2 = 35
x = 35 + 7 + 2 = 44
x = 44 + 8 + 2 = 54
**x = 54 + 9 + 2 = 65**
Table 4: Trace Table of Example 10
**Checkpoint Exercise**
1. Determine the value of x in the following program:
```
x = 10; for (i = 0; i < 100; i++) { x = x*i; } 2. Determine the value of x in the following program x = 10; for (i = 1; i < 4; i++) { x = x*i; }
```
Loops: Dynamic
**Example 11**
```
i = 0; while ( i < 10) { //Do something here i++; }
```
**Example 12**
```
input = 0; while (input ~= 1 && input ~= 2 && input ~= 3) { question = "Would you like some tea?"; input = wait(); if ( input == 1) { reaction = "That will be 10 gold please"; } elseif (input == 2) { reaction = "Oh, very well then"; } elseif (input == 3) { reaction = "No you may not have it for free!"; } else { reaction = "I'm sorry, I didn't understand you."; } } Rest of Code
```
**Answers to last Checkpoint Exercise**
(1) x = 0 (2) x = 60
Nesting
**Example 13**
```
x = wait(); if ( x == 1) { Reaction 1 } else { if (x == 2) { Reaction 2 } else { if ( x == 3) { Reaction 3 } else { Report Error } } }
```
Conclusion
- How to use comparison operators (e.g. &&, ||, etc)
- How to build an efficient if-statement
- Importance of order, elseif, etc
- How to use a switch-case structure instead of an if-statement
- How to create a counted loop
- How to use a trace table to understand it
- How to create a dynamic loop
- What nesting is, and how code should be indented when nesting code blocks
Thus far we have created framework for a real program. While the programming constructs we discussed earlier (such as while loops, if-statements, etc) make for a great skeleton, using functions (and methods) is what puts meat onto these programs and gives them some form of utility. In this chapter we will first understand how functions work before actually using them. This is important so that if an error does occur in your code, you will understand why. Also covered is the use of methods, and a method of debugging that you may find useful when your program behaves unexpectedly. Thanks to the Toolkit Engine, there are several functions readily available for us to use. These aid us in creating our game, and give us some basic code to start off. Truth be told, using the already given functions can make a fairly simplistic game, but using a collection of these functions together to produce different effects are what make a great game. : A sequence of predefined code that performs a specific task. There are quite a few functions available for use in the TK, and while it would be impossible to memorize and know all of the functions, it is important for you to be able to view the and understand the descriptions given. All functions available accomplish a specific task that could be useful to you, and luckily the function reference divides these functions into categories for quick access. Looking through the function reference you will notice two types of functions: A parameter can be found in between the brackets after the name of a function. Multiple parameters are separated by commas. What a parameter does is it takes a piece of information (stored in a variable) and gives it to the function. The function then uses this information to accomplish its specific task. If a function doesn't require any parameters, then it can accomplish its task on its own. Because each parameter is a variable, you will recall that each variable has a type. The function reference will tell you which type of variable it needs. The following table details some of these types: As an example, let's look at a simple function: void mwin( ) We'll get to what void means soon, but for now, you'll notice that the function takes in a string as its parameter. What the function does is irrelevant at this point. All we know is that it needs a string to work. When you want to use a function, we say you "call" the function. So now I will call the function mwin in a series of examples: mwin ("This is a string"); mwin ("a"); mwin (""); In each line I have called mwin and given it the necessary parameters (on the third line, I give it an empty string, but a string no less). For a function with no parameters, let's look at void windows() To call it, I simply do: windows(); You must put the empty brackets after the function in order for it to be called. Even though it takes no parameters, the RPG Toolkit differentiates between variable identifiers and function identifiers by the brackets (). You will also notice that some functions have square brackets inside the (...). For example: void wipe (string file, int effect, ) In this case, the parameter between the square brackets is considered optional. So, I can call wipe in the following two ways: wipe ("blah.jpg", 8); //No optional parameter wipe ("blah.jpg", 9, 3); //Using optional parameter By providing the optional parameter, we're giving the function more information to achieve the task it is set out to do. This will all become more clear when we start using the functions. When we call a function and give it parameters, we call it "passing". Using an earlier example: mwin ("This is a string"); Here I called mwin and passed it the string "This is a string". In RPG Code, there are two ways to pass a parameter. One is called passing-by-value, the other passing-by-reference. I will explain the differences between these two methods by use of an analogy. Suppose you are a manager at a large business firm. As a manager, you can call other people into your office (functions), give them information (parameters), and tell them to achieve your desired results. Depending on who you call, they may need different pieces of information to do this. So let's call Bob into the office. We hand Bob a sheet of paper with all the information he needs on it (all the parameters). Bob leaves the office and goes to a photocopy machine. He photocopies the information, and then uses his copy to achieve his task. He then returns to you the original copy, untouched. This is called pass-by-value. The parameters I give to the function will be "untouchable". Now let's call Phil into the office. We hand Phil a piece of paper with the information he needs on it. He takes the piece of paper, goes straight to his desk, and begins writing on it to achieve his function. When he is done, he hands back the original copy. The difference is this time, the copy has been modified. This is called pass-by-reference. The parameters I gave the function have been modified to achieve the function's goal. When looking at the command reference, you may notice some parameters with an & in front of them. This means that the parameter is passed by reference. For example: string wait ([ ]) We already know what wait does from Chapter 2. It returns the key value pressed by the user. So far, however, we have not used wait with its optional parameter, a parameter that is passed by reference. So if I were to call wait like this: input = "blah"; wait(input); I know that input has been changed after wait is executed - I gave the function input as a reference. So the wait function took input, and has given it a new value (whatever key was pressed by the player). So if the player had pressed z, input will now have the value "z". Using the same example of wait, we notice the word "string" in front of it: wait ([string &ret]) This is the return type of the function. The return types are the same as the parameter types detailed in Table 1. This is why in chapter 2 we were able to call wait as follows: input = wait(); wait() gets the key pressed by the user, and returns it. Then the = operator takes whatever wait() returns, and puts it input. This is how return values work. What if we did the following: input1 = wait(input2); Well now we have just stored the same value twice. Had I pressed the letter z on my keyboard, input1 and input2 would both have the value of "z". Now recall the mwin(...) function: mwin(string str) You will notice a lot of functions begin with "void". This means they return nothing (they return "a void"). In other words, this is illegal: input = mwin ("Hi there"); The variable input will have no stored value because mwin returned nothing, not even 0. You now have enough knowledge to understand most of the Function Reference. There are a few functions in the reference that don't use the primitive types that were listed in Table 1, but rather other types like thread, canvas, etc. We will not interest ourselves in these until a later chapter. For now, though, you should be able to: When using a function, it is often necessary to read its description. For example the function wipe(...) used above states in its descriptions the range a certain parameter could be. The wipe function was: void wipe (string file, , [,int speed]) Here the parameter "effect" can range from 1-12. Any other number given is invalid, and the function will not recognize it.
*I am in no way an expert, and the way this tutorial is written in no way implies that this is the correct way to code, nor is it the most optimized method.*
Chapter 3 - Functions and Methods
- **How Functions Work**
- **Parameters**
- **Pass-by-Value/Reference**
- **Return Values**
- **Understanding the Function Reference**
- Using Functions
- Methods
- Methods without Return Values
- Methods with Return Values
- Debugging
Introduction
How Functions Work
**Definition - Function**
** Parameters
- Functions with parameters. Example: addPlayer(string file)
- Functions without parameters. Example: boardGetVector()
Table 1: Variable Types for Parameters
**Type Specified**
**Meaning of Type**
int
a number (e.g. 3)
string
a word or letter (e.g. "hi")
variant
either a number or a word
double
a number with a decimal (e.g. 10.2)
bool
either true or false
**string str**
**[,int speed]**
** Pass-by-Value/Reference
**string &ret**
**Return Values**
**string**
**void**
** Understanding the Function Reference
- Understand how to pass parameters to a function
- Know if the parameters passed will be altered or not
- Know if the function returns information to you or not
**int effect**
A piece of advice on using functions: the best way to understand a function is to use it! Now that you know what a function needs, and what it may or may not return/modify, you are essentially providing an input to this "magic black box" and getting an output on the other end. So provide some input, and see what kind of output you get so that you can use functions to your advantage. Let us now use our knowledge to modify an earlier example from Chapter 2 into something that actually works. We will use 3 functions: If you run the above program, you will notice that mwin() keeps track of which line it is writing on. So for the first set of mwins (starting with "Would you like to have some tea?"), each call to mwin() puts the passed string on a different line. It isn't until we clear the message window using mwincls() does mwin() reset to the first line. Another thing you will notice just by looking at the syntax is the use of wait. Remember that wait returns a variable, so what's the difference between: input = wait(); //versus wait(); The answer is the first call will save the value wait() is returning, while the second call's return value vanishes and will never be accessible throughout the program. This is okay, in our case, because I really don't care what value the player pressed after he's already answered my question. It's like talking to your mother. Once you answer her question about whether or not you've done your homework, she could care less about your next response unless it involves you and some illegal substances. Now we'll convert another example that we had used in Chapter 2. If you'll recall, we asked the user for a name. If it was Xavier or Vampz, we disregarded it, otherwise we accepted the name. Example 2 details one way we could achieve this, using one new function: string prompt (string question, [string &ret]) - Asks the user a question and saves the answer in ret (or returns it). While this program works, there is still a problem. Nothing is wrong with the program itself, rather it is a logical problem. Try running the program above and entering "xavier" (all lower case). The name is accepted! The == operator checks for an exact match, and cannot differentiate between "Xavier" and "xavier". A way around this is to change the input we receive into all lower case before checking it. The function used is: I made a design choice above. I decided that the user would not know that I changed their name to lower case to check it. This leads the user to believe that the system is case sensitive, when it is actually not. In other words the following are the same: MrG, mrg, MRG, because when I check them, they are all checked as the string "mrg". However, the name stored retains its different cases. This can be seen in the contrast between the following two lines of code: lName = lcase(name); name = lcase(name); In the first case, I create a new variable (called lName) to do the checking with. Had I used the second case, I would overwrite the name given by the user into an all lower case string, thus losing the original string given. This means if the user was to request a user name of "Marz", they would get "marz". One design choice is not better than the other. It is entirely up to the designer of the program to decide which one they'd prefer. When you start writing programs, it will be you that decides. In large games, your decisions could effect how you code programs later on. Methods behave just like functions do, the only difference is that we define what the method is. When you program a method, you are essentially designing your own function. The method you program can itself call several different functions, and use all the programming constructs we discussed in Chapter 2. It is important to note that when programming a method, you are designing a set of defined code that will accomplish a task, and that whoever uses your method could be an idiot (such as yourself 3 years later). To create a method, we use the method function (kind of ironic): method name_of_method(parameters_of_method) { //what the method does } Methods use the same rules as functions. This means we can set up pass-by-value or by reference parameters, and we can choose to have return values or not. Sometimes we'd like to use a method over and over again throughout the game. When you want to use a method, you need to define what the method is and call it in the same file, as shown in Example 4. However, using the method in different prg files means having to copy and paste the method every single time we want to use it is both tedious and troublesome. What happens if we want to change the method later? We'd have to go to every file it is in and perform the same changes. The solution to this is to put the method definition in a file, let's say MyMethod.prg, and then use a "preprocessor" command called include. What the #include command does is "include" the contents of a particular file in the current file. So we can save a lot of regularly used methods in a file and #include it whenever we need a particular method. Example 5 demonstrates this: The simplest examples we can do are methods without return values. Suppose we wanted to create a method that would greet someone given a certain name. What would this method need? Simply the name we are greeting should suffice. Example 6 shows how such a method would be programmed: Note that we could have the method call placed below the method definition if we wanted to. Also note that when defining a method, we don't state whether it's a string parameter or an integer parameter, etc. Remember from Chapter 1 that the RPG Toolkit takes care of that for us. Methods without return values can do anything they want to inside their body. Sometimes, though, we want the method to do something in secret and give us a value back to complete the rest of the program. Example 7 is a simple example showing how to implement a method that "divides". While Example 7 works and accomplishes its function, it does not check to make sure that it can return an error free answer. For example, what if we tried divide(1,0)? Elementary school math tells us that it is impossible to divide by 0. Example 8 fixes our issue: In this case, divide(1/0) would result in 0. We both know that this is not the "real" answer, however if we used the variable c throughout the program and it was some undefined variable, then our program would crash which is very undesirable for the player ("For your next task, I will provide you with the ultimate weapon, the Sword of No Return." *game crashes*). In this section we'll be using some of the debugging functions provided to us by the RPG Toolkit. When running our code, sometimes outputting messages to a separate window for us to refer to can help us understand what is happening in our code. That is what the debugging functions allow us to do, and these are the functions we will be using: When you release a game, you generally toggle debug mode off, so that this separate window doesn't pop-up in front of the player as he's playing the game. When testing, however, debug mode should always be on. Debug mode is on by default if you don't set it yourself. Let us revisit Example 8. Notice that if I do 0/1 I get the same answer as */0 (where * is any number). This merits a debug message to let us know that while the value returned is 0, it is actually not. Debugging becomes much more intense when we start writing larger pieces of code. This is just a sample of what we can use it for, and in the next chapter we'll see it in a little more depth. If you've understood the last three chapters, you have enough knowledge to go out and start programming on your own. You only get better at programming with experience. In the next chapter, we'll see how our knowledge so far can help us program useful applications for our game. The examples will be explained in detail in terms of the design choices made as well as how they work.
Chapter 3 - Functions and Methods
- How Functions Work
- Parameters
- Pass-by-Value/Reference
- Return Values
- Understanding the Function Reference
- ** Using Functions
- **Methods**
- ** Methods without Return Values
- **Methods with Return Values**
- **Debugging**
Using Functions
- void mwin(string str) - Displays the string on the screen in a message window
- string wait([string &ret]) - Waits for the user to press a key
- void mwincls() - Clears and hides the message window
**Example 1**
```
input = 0; while (input ~= 1 && input ~= 2 && input ~= 3) { mwin("Would you like some tea?"); mwin("1- Yes!"); mwin("2- No thanks"); mwin("3- Can I have it for free?"); input = wait(); if ( input == 1) { mwin("That will be 10 gold please"); wait(); mwincls(); } elseif (input == 2) { mwin("Oh, very well then"); wait(); mwincls(); } elseif (input == 3) { mwin("No you may not have it for free!"); wait(); mwincls(); } else { mwin("I'm sorry, I didn't understand you."); wait(); mwincls(); } } mwin("Bye bye now!"); wait();
```
**Example 2**
```
resName1 = "Xavier"; resName2 = "Vampz"; name = ""; while (name == "") { prompt("Please enter your name:", name); if ( name == resName1 || name == resName2) { mwin("That name has been reserved."); wait(); mwincls(); name = ""; } else { mwin("Thank you, " + name + ". Welcome to the Toolkitzone"); wait(); mwincls(); } }
```
- string lcase (string str [,string &ret])
**Example 3**
```
resName1 = "xavier"; resName2 = "vampz"; name = ""; while (name == "") { prompt("Please enter your name:", name); lName = lcase(name); //convert to lower case if ( lName == resName1 || lName == resName2) { mwin("That name has been reserved."); wait(); mwincls(); name = ""; } else { mwin("Thank you, " + name + ". Welcome to the Toolkitzone"); wait(); mwincls(); } }
```
Methods
**Example 4**
//method call goes here //method definition method name_of_method(parameters) { //What method does }
**Example 5**
```
#include "MyMethod.prg" //Now we can call any method defined in MyMethod.prg
```
**Methods without Return Values**
**Example 6**
```
greet ("Bob"); //calls the greet method defined below method greet(name) { mwin("Hello " + name); wait(); mwincls(); }
```
**Methods with Return Values**
**Example 7**
```
c = divide(1,2); show(c); wait(); method divide(a, b) { answer = a/b; returnMethod(answer); }
```
**Example 8**
```
c = divide(1,0); show(c); wait(); method divide(a, b) { if (b == 0) { returnMethod(0); } answer = a/b; returnMethod(answer); }
```
Debugging
- void debug (bool enable) - Toggles whether we are in "debug mode" or not
- void debugger (string message) - Writes "message" to the debug window
**Example 9**
```
c = divide(1,0); show(c); wait(); method divide(a, b) { if (b == 0) { debugger("Attempting to divide by 0. Returning 0."); returnMethod(0); } answer = a/b; returnMethod(answer); }
```
Conclusion
The objective of this application is to provide a simple example on how to do conversations in RPG Code. The application uses the familiar functions from previous chapters (mwin, wait, etc) as well as introducing the random() function. The morale of this application is to show the pros and cons of defining pass-by-reference vs pass-by-value methods. This application includes an exercise for the reader. The objective of this application is to show how different characters can be added to the player's party. For example "hiring a mercenary" to help you slaughter enemies in a dungeon. There are a variety of functions used. The morale of this application is to show how to accomplish error handling in RPG Code. The objective of this application is to show how to develop a custom message window rather than using the default mwin() function. This application goes over string parsing (to accomplish a word wrap) and simple graphics display (graphics/text without canvasses). The morale of this application is to show the complexity of a custom system as well as how to approach defining a custom system. All three applications are important, and if you feel you already know how to do a specific application, it is still best to read the section in order to understand the morale (an important one being the Mercenaries application). When you have completed the chapter, review exercises will be provided. It is recommended that you attempt the review exercises. The only way to get better at programming is to program, reading only provides a reference. Chapter 5 will deal with more advanced data structures and searching/sorting algorithms. Traditionally a boring topic, but necessary if you want to accomplish more advanced programs.
*I am in no way an expert, and the way this tutorial is written in no way implies that this is the correct way to code, nor is it the most optimized method.*
Chapter 4 - Game Applications (Part 1)
- Introduction
- Application 1: Conversations
- Application 2: Mercenaries
- Application 3: Custom MWin
- Review Exercises
Introduction
We now have enough information to begin coding some programs that can actually be useful in our game. These are code snippets with explanations so that you can understand how they work, why they work, and why you would code them in this particular manner. You will also need the RPG Code Reference page up so that you can check out the various functions we will be applying here. Below you will find a description of each application, as well as their objective/morale.
**Conversations:**
** Mercenaries:
** Custom MWin:
When you play a video game the game designer usually wants the player to be able to interact with different people, and items, in the game world. This is usually achieved by displaying some text on the screen for the player to read. In the RPG Toolkit, we call this a message window, and we have already seen several uses of the mwin() function in the last chapter. What we need to do now is activate these message windows when the player wants to talk to someone. Let's break the basics of the program down into some pseudo code. When the player wants to talk to person X, a message window pops up where person X says something. We can choose to end it there, and this would be a similar design choice to games like Zelda and Pokemon. It's a simple design choice, and there are two main reasons why you would decide to do this: 1) It cuts back on programming 2) It cuts back on dialog design. This design worked and worked well for Zelda/Pokemon. In Zelda, however, it was a little more complex. The characters the player talked to reacted to the events going on in the game world, saying different things at different times, adding a more interactive feel to the game. Another design choice may be to provide the player with questions to ask. If you were making a detective game, much of the gameplay would be found in the dialog, and you may have the player ask a series of questions in order to receive the answer they are looking for. This, of course, is more complex, and wouldn't suit games like Zelda/Pokemon, but might suit an RPG Toolkit interpretation of the board game Clue. There are of course other design choices that could be made, but we'll show here how they're all very similar. Let's designate some pseudo code: When dealing with speech it is often (and this should be evident from above) just a bunch of if or switch-case statements. The code for Design Choice 1 (Pokemon) should be simple if you have read Chapter's 2 and 3, and will be skipped. You'll notice each of the programs above start with . You can search all the functions and variables provided to you in the function reference, you will find nothing that allows you to check for this. This is one case where the engine will do it for you as long as you set it up. To create an NPC, you have to create an item, check Board Driven, and then place it on a board. Then place the Conversation program you code under "Override program to run on activation" (If you don't know how to do this, you're in the wrong tutorial) in the board editor. This effectively does the check. For this type of conversation, as stated in the pseudo code, we would declare and initialize a global variable called gwState. This variable would increment by 1 each time the story is progressed in the game. Using Ocarina of Time as an example: Game starts: global(gwState); gwState = 0; Link finds sword: gwState ++; Link has sword and shield: gwState++; And so on and so forth. In case you haven't played Ocarina of Time, there is a dude (named Milo, I think) blocking the entrance to the Deku Tree. The first "quest" of the game is to see the Deku Tree, so Milo tells Link that he can't do that until he has a sword and shield. There are other NPCs scattered throughout the little village, and they all talk with Link as well. Using gwState above as a numerical variable is a design choice. It is easy to increment a numerical variable to progress the story, while it's not possible to do so with a string. However, there are some draw backs. Namely, how do you know what gwState = 2 refers to? You'll probably need to create a table corresponding the value of game state to some description of what that state actually means. Below is one such table: Had we used strings, it may be easier to understand what something like "sword found" means, but you'd have to ensure all strings were the same case and had no spelling errors - sort of a pain - when doing the checks. The table above can go on and on depending on the length of your game. Using this information, we can now implement Milo's conversation system. This isn't anything new. We've seen switch-case statements in Chapter 2. We specify a default as our "general" statement when Milo doesn't care about the current value of gwState. This should all be straightforward so far. Let's introduce a different NPC's conversation system: Notice Sara's is much shorter. She doesn't care if Link has a sword or shield, she only reacts to events that effect her. The more NPCs you create Conversation Systems for, the more you'll be designing around who says what at what time. This isn't a programming issue though, so let me present one. It gets pretty lame if every single time Sara is not effected by the story, she says "I like music". What if we wanted her to say something at random? Looking ahead, what if we wanted other NPCs to have the same ability (saying something random)? Whenever we need to repeat code, it is better to design a method rather than copy paste code. What are the objectives of the method we are laying out? When looking up a function, it usually has a logical name. For instance, to get a random number? We can use the function random()! From the above specifications, we know that the method should take 3 parameters for the 3 options of what to say. If you want more, you'll have to hard code it yourself (not hard). In later chapters, we'll learn how to do this dynamically instead. The method can either return the string for the programmer to put in mwin(...), or it can mwin() the string itself. I will choose the former method. Saving the above in a file called "Methods_Convo.prg" I continue in Sara's conversation system: For easier to read code, I did not type opt1, opt2, and opt3 directly into the parameters when calling rdmSelect. This is a style choice. Because I have defined autolocal(TRUE) above, opt1, opt2, and opt3 will be "destroyed" by the end of default (at the '}' for default, recall scope of variables), so it really doesn't make too big of a difference memory wise. Performance wise, we are technically "losing" performance. Why? Well, before I call rdmSelect, I create and initialize 3 variables. This takes time. I then pass these variables BY VALUE to rdmSelect. This means rdmSelect then goes through and creates a copy of each parameter, taking up time again. Finally, a copy is made when one of the strings is returned (I'm not positive on that last part, but I'm pretty sure that happens). That's a lot of time wasted. The solution around this is to use pass-by-reference. Now we have another problem. By using pass by reference, if we don't use opt1/opt2/opt3, but instead the following code, it is invalid: rdmSelect("1", "2", "3", str); Why? Because the first 3 parameters are never given a memory address! We are "declaring" them in the parameter of the function, which has no identifier. Recall the analogy of the boss calling a pass-by-reference function into his office. The pass-by-reference function takes the sheet of paper, and scribbles their answer on that piece of paper. When we do the above call, we do not give that function a piece of paper. Instead, we are "verbally" telling it what the parameters are. Now it has nothing to write on, and we get nothing back! This enforces the method I used above, where I declared opt1/opt2/opt3 separately. However, if you're not careful, you may forget. Which brings us to the question: Does it really matter? Is efficiency that important to us? Here, it is not. However, you should keep this in mind when you start coding more robust programs along the lines of real time battle systems. This should cover everything you need to code a Zelda-like conversation system. We leave the Clue-like conversation system as an exercise, with some hints to guide you along.
Application 1 - Conversations
Introduction
**Design Choice 1 (Pokemon) - Pseudo Code**
```
if (spoken to) { respond accordingly }
```
**Design Choice 1 (Zelda) - Pseudo Code**
```
//define a global variable for the game world's state: gwState //depending on how far along in the story the player is, gwState may range from 1-x if (spoken to) { check gwState respond accordingly }
```
**Design Choice 2 (Clue) - Pseudo Code**
```
if (spoken to) { present selection of questions to ask accept input check question asked respond accordingly }
```
Implementation - Zelda Conversations
*if (spoken to)* *if (spoken to)*
**gwState**
**Description of Story State**
Game has just begun
Link has sword, but no shield
Link has sword and shield. Can go see Deku Tree
Link has seen Deku Tree, Tree is sick
Link has "saved" the Deku Tree. The Deku Tree is now dead
Link has...
**Conversation System 1 - Milo**
```
autolocal(1); switch(gwState) { case 1: { MWin("Milo says:"); MWin("Why would the Deku tree want to see you?! I am the great Milo!"); MWin("And there's no way you're seeing him without a sword/shield."); wait(); MWincls(); } case 2: { MWin("Milo says:"); MWin("What?! A sword?! Impossible! Still, you have no shield!"); wait(); MWincls(); } case 3: { MWin("Milo says:"); MWin("What's that? A sword?! And a shield?! Alright... go on"); wait(); MWincls(); } case 4: { MWin("Way to go dumbass, you killed the Deku Tree!"); wait(); MWincls(); } default: { MWin("I am the great Milo!"); wait(); MWincls(); } }
```
**Conversation System 1 - Sara**
```
autolocal(1); switch(gwState) { case 1: { MWin("Sara says:"); MWin("Hi Link! You're cute!"); wait(); MWincls(); } case 4: { MWin("Oh no, the Deku Tree is dead!"); wait(); MWincls(); } default: { MWin("I like music :D"); wait(); MWincls(); } }
```
- It should have some options for what to say
- How many? 3 (design choice)
- It should choose an option at random
- How? use a function!
**Random Output Method**
```
autolocal(1); method rdmSelect(opt1, opt2, opt3) { rdm = random(100); if (rdm <= 33) { returnMethod(opt1); } elseif (rdm <= 66) { returnMethod(opt2); } else { returnMethod(opt3); } }
```
**Conversation System 1 - Sara**
```
#include "Methods_Convo.prg" autolocal(1); switch(gwState) { case 1: { MWin("Sara says:"); MWin("Hi Link! You're cute!"); wait(); MWincls(); } case 4: { MWin("Oh no, the Deku Tree is dead!"); wait(); MWincls(); } default: { opt1 = "I like music."; opt2 = "I like you."; opt3 = "I wonder what's outside Kokiri Village?"; str = rdmSelect(opt1, opt2, opt3); MWin("Sara says:"); MWin(str); wait(); MWincls(); } }
```
**Random Output Method (2)**
```
autolocal(1); method rdmSelect(&opt1, &opt2, &opt3, &dest) { rdm = random(100); if (rdm <= 33) { dest = opt1; } elseif (rdm <= 66) { dest = opt2; } else { dest = opt3; } }
```
**Conversation System 1 - Sara**
```
#include "Methods_Convo.prg" autolocal(1); switch(gwState) { case 1: { MWin("Sara says:"); MWin("Hi Link! You're cute!"); wait(); MWincls(); } case 4: { MWin("Oh no, the Deku Tree is dead!"); wait(); MWincls(); } default: { opt1 = "I like music."; opt2 = "I like you."; opt3 = "I wonder what's outside Kokiri Village?"; rdmSelect(opt1, opt2, opt3, str); MWin("Sara says:"); MWin(str); wait(); MWincls(); } }
```
**Check Point** **Exercise**
Write the Clue-like conversation system explained as Design Choice 2 in the introduction. Use the following hints to help you: BONUS: Allow your method to work for 3 OR LESS parameters (3, 2, or 1). The following is not a solution: "1- And your mother's name is?" "2 -" "3-" That is, "2-" and "3-" should not show up as options at all!
- Follow the pseudo code
- Use Example 1 from Chapter 2 and create a method that accepts three parameters for "questions to ask".
- Have the method return a number from 1-3 as to what the response was
- Use this number to determine what the NPCs reaction is to the question
- Call that method each time you want the player to be able to respond to the NPC
- Make sure you have a "closing question" or a "good bye" option so the user can exit
A common theme in the Final Fantasy line of RPGs (and other RPGs) is that as the story progresses, players will join your ranks and fight alongside of you (I will call these players Mercenaries). In other games, such as Diablo II and Freedom Fighters (not an RPG, but it still applies), you get to select who gets to join your ranks, and may have to pay a fee in order for them to fight alongside you. In this application we will see how this is accomplished using some of the functions, but first we will go over Error Handling as it is important for this application and many to come. The RPG Toolkit Engine has a predefined way to handle errors that may arise during the execution of your program. Sometimes, however, we would like to handle our errors in our own unique way. Please note that error handling can only be done in functions. That is, when you call a function, you may want the function to handle errors in its own way. Before we begin discussing error handling, it is important to understand the concepts of branching and labels. In RPG Code, I can label the beginning of a section of code using the following syntax: :myLabel Note the colon, ':', before the name "myLabel". In the same prg file, I can now use the branch function to "jump" to the first line of code after the label. The syntax for such a function is: branch(":myLabel"); Using labels allows us to skip over other parts of code to go to a certain area. A long time ago, in the days of Assembly Programming, constructs such as while loops were unavailable, and as such labels had to be used as demonstrated in Example 1. I strongly urge you to not use branches in this manner. Aside form the fact that it is harder to read, using branches extensively throughout a program can lead to very sloppy "noodle" code. This term was used to explain code that seemed to be put together in an unorganized manner, like spaghetti. When explaining error handling, a common metaphor used is the raising and lowering of "flags". When the RPG Toolkit experiences an error, it raises a certain flag (let's say it's a blue flag). If the engine sees that a blue flag has been raised, then it executes a certain block of code to handle a "blue error". In more specific terms, the engine to the label that handles a blue flag. We can overwrite where this label is located by using the function: setErrorHandler(:labelName); In addition, we can allow the engine to resume to its own error handler by using the function: setResumeNextHandler(); A common error that can occur in an RPG Code program is attempting to use a file that does not exist. Example 2 is taken directly from the help files, and shows how a function can tell you if a file exists or not. We will be using this function in our application. We are designing a program that presents the user with the option to add a certain party member to their team for a certain amount of gold. We will use an incremental design methodology (that is, we will design the program in steps that "work properly") to do this. The steps are as follows: A mercenary in the RPG Toolkit is a playable character. That means that you use the "Edit Character" option to create them and save them as .tem files. A "pre-step" to the coding steps listed above is to create three mercenaries called: mercenary1.tem, mercenary2.tem, and mercenary3.tem. Assuming you have read the preliminary chapters of this tutorial, the preliminary step should be very simple, and is almost identical to a previous example from chapter 3: In order to actually add the mercenary to the player's party, the function addPlayer(...) will have to be used. Notice that it takes the parameter of the file name. When you call addPlayer, it automatically looks in the "Chrs" folder of your game. Thus it is necessary to save the .tem mercenaries we created earlier in that folder (where it is defaulted to anyway). We can easily modify Step 1 by adding this feature, but suppose the player did not have enough gold to purchase that particular mercenary. Clearly ,an if-else statement is needed in order to check for this. But how do we ensure the loop asks the player again? A branch! Right? I really hope you're shaking your head right now. The answer was not branches. The reason I used branches was to demonstrate that, as a programmer, you should make use of the loop conditions you're already using. In our case, that condition is: input ~= 1 && input ~= 2 && input ~= 3 The solution is to simply set the variable, input, to a value that is not 1, 2, or 3! This ensures that when we check the condition again, we don't exit the loop but instead, repeat it. Of course, the easy way out is simply not to ask the user again and have him speak to the guy at the Tavern again, but where's the fun in that? If you are a seasoned programmer, you may also notice that the program can be simplified and the code can be written more efficiently. In addition, you may notice that if the player doesn't have enough gold for even the cheapest of warriors (Asimir), then the loop never stops and the player is stuck! Step 2 - Revision 2 solves these issues. The reader is encouraged to go through this revision and understand what happened. The following bullets discuss why they happened: Before we continue on to using the error handling function introduced earlier, why do we need to set neededMoney to 0 in the elseif (input == 4) block? (Hint: recall its scope and where it changes) Note now that, by simplifying our code earlier, we only need to make one call to our function fileExists(...). The reason to use error handling is in case the game creator completely forgot to make one of the .tem files. In large games this is a possibility and can cause an issue. If you charged the player 300g for a character that did not exist in the game... they'd be pretty angry I would think. If you do not know the answers to the questions asked throughout this section, either ask in Newbie Haven or reread earlier chapters.
Application 2 - Mercenaries
Introduction
Error handling
**Example 1 - Branch Equivalent of while (x < 10)**
```
x = 0; :WHILE_BEGIN x++; if (x >= 10) { branch(:WHILE_END) } branch(:WHILE_BEGIN) :WHILE_END
```
*branches*
**Example 2**
```
function fileExists(file, folder) { setErrorHandler(:error); openFileInput(file, folder); setResumeNextHandler(); closeFile(file); return true; :error return false; }
```
Implementation
- Present the user with three options of different mercenaries, noting the cost to hire them
- Using relevant functions, add the character to the player's team and take requested gold
- Add error handling to ensure a character that does not exist is not added
**Step 1**
```
mwin ("Welcome to the Tavern of no Remorse!"); input = 0; while (input ~= 1 && input ~= 2 && input ~= 3) { mwin ("Who would you like to hire?"); mwin ("1- Asimir - 10g"); mwin ("2- Juice - 15g"); mwin ("3- Seafroggys - 20g"); input = wait(); mwincls(); if ( input == 1) { mwin("Ah I see you chose the cheapest of warriors.") mwin("That will be 10 gold please"); wait(); mwincls(); } elseif (input == 2) { mwin("Hmm, not a bad choice. That will be 15 gold please"); wait(); mwincls(); } elseif (input == 3) { mwin("He is indeed a fearsome warrior!"); mwin ("That will be 20 gold please!"); wait(); mwincls(); } else { mwin("I'm sorry, who?"); wait(); mwincls(); } }
```
**Step 2 - With Branches**
```
mwin ("Welcome to the Tavern of no Remorse!"); input = 0; while (input ~= 1 && input ~= 2 && input ~= 3) { :BEGIN mwin ("Who would you like to hire?"); mwin ("1- Asimir - 10g"); mwin ("2- Juice - 15g"); mwin ("3- Seafroggys - 20g"); input = wait(); mwincls(); playerMoney = getGP(); if ( input == 1) { mwin("Ah I see you chose the cheapest of warriors.") mwin("That will be 10 gold please"); wait(); mwincls(); if (playerMoney < 10) { mwin ("You don't have enough money!") wait(); mwincls(); branch(:BEGIN); } else { takeGP(10); addPlayer("mercenary1.tem"); } mwincls(); } elseif (input == 2) { mwin("Hmm, not a bad choice. That will be 15 gold please"); wait(); mwincls(); if (playerMoney < 15) { mwin ("You don't have enough money!") wait(); mwincls(); branch(:BEGIN); } else { takeGP(15); addPlayer("mercenary2.tem"); } mwincls(); } elseif (input == 3) { mwin("He is indeed a fearsome warrior!"); mwin ("That will be 20 gold please!"); wait(); mwincls(); if (playerMoney < 20) { mwin ("You don't have enough money!") wait(); mwincls(); branch(:BEGIN); } else { takeGP(20); addPlayer("mercenary3.tem"); } mwincls(); } else { mwin("I'm sorry, who?"); wait(); mwincls(); } }
```
**Step 2 - Revision 2**
```
autoLocal(1) //Constants priceOne = 10; priceTwo = 15; priceThree = 20; //Variables input = 0; neededMoney = 0; whichPlayer = 0; playerMoney = getGP(); mwin ("Welcome to the Tavern of no Remorse!"); wait(); mwincls(); while (input ~= 1 && input ~= 2 && input ~= 3 && input ~= 4) { mwin ("Who would you like to hire?"); mwin ("1- Asimir - " + priceOne + "g"); mwin ("2- Juice - " + priceTwo + "g"); mwin ("3- Seafroggys - " + priceThree + "g"); mwin ("4- I'm not interested in your srubs!"); input = wait(); mwincls(); if ( input == 1) { mwin("Ah I see you chose the cheapest of warriors.") mwin("That will be " + priceOne + "g"); wait(); mwincls(); neededMoney = priceOne; whichPlayer = "mercenary1.tem"; } elseif (input == 2) { mwin("Hmm, not a bad choice. That will be " + priceTwo + "g"); wait(); mwincls(); neededMoney = priceTwo; whichPlayer = "mercenary2.tem"; } elseif (input == 3) { mwin("He is indeed a fearsome warrior!"); mwin ("That will be " + priceThree + "g"); wait(); mwincls(); neededMoney = priceThree; whichPlayer = "mercenary3.tem"; } elseif (input == 4) { mwin("Humph, what a rude person you are!"); wait(); mwincls(); neededMoney = 0; } else { mwin("I'm sorry, who?"); wait(); mwincls(); } if (playerMoney < neededMoney) { mwin ("You don't have enough money!") wait(); mwincls(); input = 0; } elseif (neededMoney > 0) { takeGP(neededMoney); addPlayer(whichPlayer); } }
```
- The use of autolocal(1) ensures that local scope is enforced (recall Chapter 1)
- The variable playerMoney was placed in the while loop, and thus was being updated each time throughout the loop. This was unnecessary and took up needless processing time. By placing it at the beginning of the program, it is only executed once. In reality, playerMoney is not needed at all. Do you know why?
- The constants priceOne, priceTwo, and priceThree were introduced and used throughout the program. This makes it easier to change the price of the mercenaries in case the game creator makes a design decision later on in the game.
- The variable whichPlayer alongside neededMoney allowed the use of ONE if-else statement at the very end, rather than three nested if-else statements throughout the program. This makes the program easier to read and less cluttered.
- By setting input = 0 if the player didn't have the required money, the loop would reiterate. The player can exit the loop by selecting option 4, which does not reset the value. Note that the if-else statement for checking playerMoney and neededMoney is still executed! How can you change it so that it does not get executed? (Hint: make strategic use of the comparisons in the if-elseif statement)
**Function - fileExists.prg**
```
function fileExists(file, folder) { setErrorHandler(:error); openFileInput(file, folder); setResumeNextHandler(); closeFile(file); return true; :error return false; }
```
**Program - tavernRemorse.prg**
```
#include "fileExists.prg" autoLocal(1) //Constants priceOne = 10; priceTwo = 15; priceThree = 20; //Variables input = 0; neededMoney = 0; whichPlayer = 0; playerMoney = getGP(); mwin ("Welcome to the Tavern of no Remorse!"); wait(); mwincls(); while (input ~= 1 && input ~= 2 && input ~= 3 && input ~= 4) { mwin ("Who would you like to hire?"); mwin ("1- Asimir - " + priceOne + "g"); mwin ("2- Juice - " + priceTwo + "g"); mwin ("3- Seafroggys - " + priceThree + "g"); mwin ("4- I'm not interested in your srubs!"); input = wait(); mwincls(); if ( input == 1) { mwin("Ah I see you chose the cheapest of warriors.") mwin("That will be " + priceOne + "g"); wait(); mwincls(); neededMoney = priceOne; whichPlayer = "mercenary1.tem"; } elseif (input == 2) { mwin("Hmm, not a bad choice. That will be " + priceTwo + "g"); wait(); mwincls(); neededMoney = priceTwo; whichPlayer = "mercenary2.tem"; } elseif (input == 3) { mwin("He is indeed a fearsome warrior!"); mwin ("That will be " + priceThree + "g"); wait(); mwincls(); neededMoney = priceThree; whichPlayer = "mercenary3.tem"; } elseif (input == 4) { mwin("Humph, what a rude person you are!"); wait(); mwincls(); neededMoney = 0; } else { mwin("I'm sorry, who?"); wait(); mwincls(); } if (playerMoney < neededMoney) { mwin ("You don't have enough money!") wait(); mwincls(); input = 0; } elseif (neededMoney > 0) { fExist = fileExists(whichPlayer); if (fExist == 1) { takeGP(neededMoney); addPlayer(whichPlayer); } else { debugger("Error: Player not found!"); wait(); mwincls(); } } }
```
The default systems provided in the RPG Toolkit are adequate for creating a decent game. Unfortunately, because they are default, they are common in many TK Games and lack originality. Custom systems have nearly become a must if you want your game to succeed, but implementing them is never easy. This section goes over the thought process and design methodology for programming a message window. You may recall from earlier chapters that the default message window is accessed using the function mwin( string text ). We will begin the design by listing the feature we want to include, and then compiling a table of the functions we will need to use in order to implement the custom message window. Finally will go into the actual implementation. You should never approach a custom system blindly. Knowing what you are programming and what you need to program in the future is essential if you plan on programming it right the first time. When starting the design of a custom system, you start by asking yourself the question, "What must it do?" Our custom system must... Next, you should ask yourself what the custom system must not do. Our custom system must not... To clarify, in the RPG Toolkit when you set the colour scheme using a function such as colorRGB, then the rest of the game will be using that colour scheme until the function is called again. Because we may want a specific colour scheme for our custom message window, we must make sure to restore the colour scheme being used before the call to our custom mwin. The same applies to font size. Side note: The above paragraph details a design decision. The inverse of this is to force the person calling the function to save their own colour scheme and restore it after the custom system returns. However, given that we expect multiple calls to our custom message window, the design decision detailed above is probably the better one. Now that we know what the custom system must and must not do, we go through the function reference in the documentation to find the predefined functions that will help us accomplish our task. These functions can be seen in Table 4.3.1, and as you can see they are in no particular order. You may have to go through the command reference more than once (as I did) in order to find all the useful functions for the task. As you program more and more, this will become easier as you will remember functions all on your own. In case it isn't obvious, we'll be designing a method to implement the custom message window. In fact, most custom systems will require the design and implementation of one or several methods. Also, we will be placing the custom message window in its own program file called "myMwin.prg". Whenever we want to access the method, we use the #include"myMwin.prg" command before we make a call to our method (this was covered in Chapter 4 - Application 1). The first step we will undergo is setting up the basic design of the method as well as its "prologue" and "epilogue". The prologue is where we will save the font size/colour and the epilogue is where we will restore it. Meanwhile, the "body" is where the actual meat of the method is. For those migrating from TK2 you may notice that we only require one parameter to be passed. This is because by implementing a word wrap, we will no longer need to keep track of the position of which line the player is on. For those interested, in the past this is how someone may use a custom message window: cMwin(1, "This is line 1"); cMwin(2, "This is line 2"); Notice the extra parameter at the beginning, stating which line the string would be placed on. This is, as you may expect, tedious to implement and use. The next step is to draw a box on the screen to signify where our text will be placed. Now I'm no artist, so the MWin box looks relatively hideous. Feel free to change the colour scheme to your liking by simply changing the RGB values at the function calls. You may also change the position of the MWin box if you please. So far everything should have been straightforward to follow. Before diving into the difficult part, word wrapping, let us first simply add support for one line of text. Through trial and error, we can find that the maximum amount of characters that can fit on one line is 45. Keep in mind that this is dependent on two factors: (1) the font size being 18, (2) the size of the box. If either of these change, the word wrap we are about to implement will fail. Also note that given these specifications we can support 5 lines of text. Using the information listed above, we know that the maximum amount of characters our MWin can support is: 5 * 45 = 225 A smart thing to do would be to check if the string passed is greater than 225 characters. If it is, we will output an error to the debugger and exit the function. Otherwise, we will output everything to the screen. To output everything to the screen, note that we have both the text(...) and print(...) function at our disposal. In order to use print to our advantage, we must use text first. Next, we consider the math and conditions behind string manipulation. The function text will be receiving the first 45 characters of the string. The remaining characters should go through a loop until the entire string is outputted. A variable, strLen is used and is essentially a dynamic "counter" that keeps track of the amount of characters in the string. We can achieve this loop by checking if the variable, strLen, is greater than 0. If it is, we will decrement it by 45. This is all shown in step 3. Note the similarity between the 4 lines of code before the for loop, and the for loop itself. They are almost identical in functionality, except we use the print function instead of the text function. You can test this method with the following cases: a = "Testing this to see if it works hiyo! Blah 1 2 3 "; a = a + a + a + a; myMwin(a); wait(); myMwin("test"); wait(); a = "Testing this to see if it works hiyo! Blah 1 2 3 "; a = a + a + a + a + a; myMwin(a); wait(); Because you followed this tutorial by reading rather than implementing, you may not truly appreciate the power of Table 4.3.1. By setting this table up, it is an easy reference for everything you need to do. I highly encourage you to follow this design methodology when implementing a custom system. While I will end this application here, the custom system is far from being done. The exercises below help further polish this custom message window into something more feasible.
Application 3 - Custom Message Window
Introduction
Design Specifications
- Draw a box on the screen for text to be placed in
- Take in text and place it on the screen
- Check if the text is too long to be placed in one line on the screen, and if it is "wrap" it to the next line
- Alter the present colour scheme used in the game
- Alter the present font size used in the game
Table 4.3.1 - List of useful functions
**Function**
int len (string str)
Returns the length of the string. We will use this to check if the string is too big for the message window.
void fontSize (int size)
Sets the size of the text to be written
void text (double x, double y, string str)
Places text at a certain (x,y) location. Note that x and y are not pixel units, and the location is relative to the fontSize.
void print (string text)
Places text directly after the last location of where text or print was put.
string left (string str, int amount)
Returns a string that is part of the string passed starting from the first character in the string. For example left("Hello", 3) would return Hel
string right (string str, int amount)
Returns a string that is part of the string passed starting from the last character in the string. For example right("Hello", 3) would return llo
void fillRect (int x1, int y1, int x2, int y2)
Draws a filled rectangle given the specified colour from positions (x1, y1) to (x2, y2)
void drawRect (int x1, int y1, int x2, int y2)
Draws the outline of a rectangle given the specified colour from positions (x1, y1) to (x2, y2)
void getColor(&r, &g, &b)
Gets the current RGB colour scheme.
int getFontSize()
Gets the current font size
void colorRGB (int r,int g,int b)
Sets the colour to the specified RGB colour scheme.
Implementation
** Step 1 - Prologue and Epilogue Setup
```
autolocal(1); method myMwin(str) { // Prologue fSize = getFontSize() red = 0; green = 0; blue = 0; getColor (red, green, blue); //red, green, and blue are passed by reference // Body // Epilogue fontSize (fSize); colorRGB (red, green, blue); }
```
**Step 2 - MWin Placement**
```
autolocal(1); method myMwin(str) { // Prologue fSize = getFontSize() red = 0; green = 0; blue = 0; getColor (red, green, blue); //red, green, and blue are passed by reference // Body colorRGB(0,0, 200); fillRect(50,50,350,150); colorRGB(140, 0, 0); drawRect(50, 50, 350, 150); // Epilogue fontSize (fSize); colorRGB (red, green, blue); }
```
**Step 2 - With text**
```
autolocal(1); method myMwin(str) { // Prologue fSize = getFontSize() red = 0; green = 0; blue = 0; getColor (red, green, blue); //red, green, and blue are passed by reference // Body colorRGB(0,0, 200); fillRect(50,50,350,150); colorRGB(140, 0, 0); drawRect(50, 50, 350, 150); colorRGB (255, 255, 255); fontSize(18); text(4, 4, str); // Epilogue fontSize (fSize); colorRGB (red, green, blue); }
```
**Step 3 - Word Wrap**
```
autolocal(1); method myMwin(str) { // Prologue fSize = getFontSize(); red = 0; green = 0; blue = 0; getColor (red, green, blue); //red, green, and blue are passed by reference // Body strLen = len(str); if (strLen > 225) { debugger("Error: String too long."); wait(); } else { colorRGB(0,0, 200); fillRect(50,50,350,150); colorRGB(140, 0, 0); drawRect(50, 50, 350, 150); colorRGB (255, 255, 255); fontSize(18); strTemp = left (str, 45) // Gets first 45 characters of string text(4, 4, strTemp); // prints first 45 characters of string str = right(str, strLen - 45); // Chops off first 45 characters of string strLen -= 45; // Reduces string length by amount chopped off for (strLen; strLen > 0; strLen -= 45) { strTemp = left(str, 45); str = right (str, strLen - 45); print(strTemp); } } // Epilogue fontSize (fSize); colorRGB (red, green, blue); }
```
** Case 1 - Fits 5 lines
** Case 2 - No Word Wrap
**Case 3 - Too many characters**
**Check Point Exercises**
1. Modify the myMwin method to support an image instead of using the fillRect/drawRect functions. The new method should have parameters: myMwin(image, str) 2. Modify the myMwin method to support profile pictures. You may wish to expand the size of the MWin Box. The profile picture can be placed to the left or right of the text. The new method should have parameters: myMwin(profile, str) or myMwin (profile, image, str) if you are expanding from Check Point Exercise 1. 1. Modify the myMwin method to support different locations. That is, the MWin Box appears on different parts of the screen. Ensure that positions do not overlap. The new myMwin method should have parameters myMwin (pos, str). If you implement this correctly, you should be able to have multiple myMwin's displayed on the screen at one time. 2. Through the use of a global variable, use the implementation from Easy-1 to support an image but not have it passed as a parameter. That is, the parameters resort to myMwin(str) but myMwin now relies on a global variable to set the MWin Box with an image. Add error support in case the file does not exist. 1. The current implementation of myMwin does not disappear and does not have an equivalent "mwincls()" function. Add some function calls to the prologue/epilogue to save then restore the screen after wait() returns a character (note: you may wish to place wait() inside the function and have the myMwin method return what the user pressed). Is there an easier way to do this? If so, which way is more beneficial?** Easy
** Intermediate
**Expert**
The review exercises are divided into beginner, intermediate, and expert. Ideally you'll want to be at the intermediate level after going through these 4 chapters. If you are not, do not be discouraged. Programming takes time to understand as it is part art and part science. Keep trying and feel free to ask questions.
Chapter 4 - Review Exercises
Beginner Exercises
- Write a "quiz" program that asks the user 3 or more questions. Tally the results of these questions and at the end of the quiz, tell the user their score as a percentage.
- Design a chest program that, when activated, gives the player 100 GP. Make sure the chest only gives 100 GP once.
- Create a simple Inn program that charges the user 50 GP if they want to restore their health and mana to full. Make sure to check how much GP they have, and if they are already at full health and mana.
Intermediate Exercises
- Draw a button on the screen. Allow the user to click the button, and click elsewhere on the screen in order to move the button there. You need worry about animating the movement, simply make the button disappear then reappear at the desired location.
Expert Exercises
- Design a custom text-based battle system that uses the default character stats (FP, DP, etc). You should use the mwin function and support one enemy. The options for the user in the battle system are: (1) Attack and (2) Run away. Run away has a 20% chance for the user to escape battle. Hint: use a while loop that keeps going until either the player or the enemy is at 0 HP (or the player has run away).
In this chapter we will introduce a common data structure, the array, and understand how it works and how to manipulate it. Unfortunately arrays in the RPG Toolkit are not very robust, and there are several pitfalls that could cause errors in your program. Make sure you pay attention to these as they are pointed out throughout this chapter. An array is a collection of variables with the same name. What differentiates one variable from another is its . For example, let's suppose Vampz (a character in our game) has seven children. One method of naming these seven children is by declaring seven different variables: firstChild = "Asimir"; secChild = "Juice"; ... sevChild = "Picso"; With arrays, we can simplify this process by using one variable name and 7 different : vChild[1] = "Asimir"; vChild[2] = "Juice"; ... vChild[7] = "Picso"; An important thing to note is that the size of an array is dynamic, and does not correspond to the index. For example, the following is perfectly valid: array[1] = 20; array[5] = 14; array[6] = 16; If you're wondering what array[2..4] are, they are . This is very different from programming languages such as C++ where an array's size has to be predetermined and all elements initialized by default. In addition, accessing a non-existent element of an array does not cause an error: show ( array[2] ); // no error wait(); Instead nothing is shown, and the above code simply waits for a key press. This poses a problem: while your program won't crash because it is accessing a non-existent element in an array, if you are accessing a non-existent element you won't know ( ). This means when using arrays you have to be very careful so that you don't attempt to access something that isn't there. Because of this, you may want to use a programming model that does not allow "skipping" indices, so that the code: array[1] = 20; array[5] = 14; array[6] = 16; Is illegal and never used. You must define indices 2-4. You can also have arrays with more than one index. These are called multi-dimensional arrays: array[0][0] = 0; array[0][1] = 1; A 2-dimensional array is the equivalent of a table you may create in Word or Excel. You can consider the first index to be the row number, and the second index to be a column number. Example 1 shows how we can create the multiplication table from 1-9. The table from Example 1 looks like: Indices of arrays are not limited to being numbers, but can also be words or letters: player["name"] = "Marz"; player["sex"] = "male"; These types of arrays are more accurately called maps, but are identical to arrays in terms of functionality. Normally numerical indices are preferred because it makes it easier to "find" a certain element of an array. There are many different ways to search an array with numerical indices. You can search Google for different on searching arrays. An algorithm is a set of instructions that you follow in your code in order to accomplish a common task. Some algorithms are better than others in different situations. We will not interest ourselves in the efficiency of searches, and will introduce a simple linear search algorithm. In a linear search, we traverse an array element-by-element from beginning to end (or end to beginning) in order to find what we are looking for. This search algorithm is limited to knowing the size of the array - if we don't know the boundaries of the array (where it starts and where it ends), then we ultimately cannot search it (due to the pitfall discussed earlier). You may have guessed that to search an array we use a loop. We tell the loop where to begin, and where to end. Example 2 demonstrates how we search an already formed 1 dimensional array for one of its elements. In Example 2 you can see we set up 4 elements and assigned them each some value (at random). We then loop through the array until we find the element we are searching for (which is set with the variable "search"). Once found, we output to the screen how many times we went through the loop, and then set i equal to 5. Technically speaking, we could have set i to any number greater than 4 because that is the condition of the for loop (i <= 4). After reading this chapter you should understand the following: By understanding the limitations and flexibility of arrays, you can begin to use them correctly in programs you implement. One thing to note is that arrays cannot be passed as parameters to methods.
*I am in no way an expert, and the way this tutorial is written in no way implies that this is the correct way to code, nor is it the most optimized method.*
Chapter 5 - Arrays
- Array Declaration
- Searching an Array
- Conclusion
Introduction
Array Declaration
*index*
*indices*
*non-existent*
**pitfall**
**Example 1**
```
for (i = 1; i < 10; i++) { for (j = 1; j < 10; j++) { multi[i][j] = i * j; } } show ( multi[2][7] ); // Will show 2*7 = 14 wait();
```
multi[ i ][ j ]
*algorithms*
**Example 2**
```
autolocal(1); //form a 1-dimensional array array[1] = 34; array[2] = 43; array[3] = 45; array[4] = 12; //Search array for element 45 search = 45; for (i = 1; i <= 4; i++) { mwin("Iteration: " + i); wait(); if (array[i] == search) { mwincls(); mwin("It took " + i + " iterations to find " + search); wait(); i = 5; } }
```
Conclusion
- Why it is important that the indices of an array grow in a linear manner (that is, your array has elements 1,2,3,4 not 1,4,6,3).
- Why it is important for you to always know the size of an array
- How to exit a for-loop by changing its counter variable
- An array can grow dynamically by simply adding elements whenever necessary
- An array cannot shrink
We have seen that a variable we create can be either a string or a number. In this chapter, we will show how a variable can also take the form of a canvas. If you open up MS Paint, the initial white box that you can draw on is called a canvas. This canvas can be resized to be larger and smaller, and can be painted on with the basic tools provided to you by MS Paint. In the RPG Toolkit, a canvas is very similar. The tools used to "paint" on to the canvas are functions (e.g. fillRect, text, etc), and its size is determined when we first declare the variable. One major difference is that canvasses in the RPG Toolkit are initially not on the screen - that is, they are hidden. You can, of course, show the canvas on a part of the screen using a function. Recall that variables of a number or string are easily defined with simple syntax: number = 12; string = "Hiyo!"; In RPG Toolkit, these two types of variables can be considered types. A canvas is a non-primitive type, and doesn't store a number or a string, but rather a collection of images/text "painted" on it. To initialize a canvas, we need to provide the toolkit with a height and width component. Because a canvas is not a primitive data type, we also need to explicitly tell the RPG Toolkit that we want a canvas. The syntax to achieve these two criteria is: canv = createCanvas (300, 200); //Creates a canvass of height 300 and width 200 Notice how similar this syntax is to functions that return a variable. Indeed, it can be thought of as that - recall the wait function: result = wait(); So in the case of the canvas, we have "called a canvas function", passing it parameters of height 300 and width 200, and returned the result to the variable canv. You will notice that a lot of the "graphical" functions have an optional parameter at the very end for a canvas. If this optional parameter is not provided, the graphical function simply draws directly to the screen. If we provide it the optional canvas parameter, then the function draws only onto that canvas: bitmap("background.jpg"); // Stretches the file "background.jpg" on to the entire screen cnv = createCanvas (300,200); bitmap ("background.jpg", cnv); // Stretches the file "background.jpg" on to the canvas, 300x200 pixels only We can perform several of these functions to any particular canvas. To finally display the canvas on the screen at a particular position, we use the function: drawCanvas(canv, x_position, y_position); If you make any changes to the canvas by painting on it, they will not be showed until you use the drawCanvas function again. This is an important fact to remember when you get to the Animation section of the chapter. With the primitive variable types, the RPG Toolkit took care of deleting them from memory at the end of their scope. With canvasses, it's a little bit different. I won't delve into the reasoning behind this (if you're interested, read up on pointers in other programming languages), but as the programmer you must explicitly tell the RPG Toolkit to delete the canvas. This is accomplished with the following syntax: killCanvas (canv); Killing a canvas does not mean what is displayed on the screen is gone. It only means that the canvas you used to be able to draw on is no longer available for use, and you'll have to recreate it. To recap, in order to use canvasses in your program you must The custom MWin we implemented in Chapter 4 can take advantage of canvasses. The final implementation of the message window from Chapter 4 is shown below. We will now use canvasses to simplify some of the expansions listed in the Check Point Exercises. Namely, it will be shown how easy it is to set up different positions for the MWin (Intermediate-1). We will expand the method to support canvasses by creating the canvass in the prologue, and later deleting it in the epilogue. We will also expand the parameters of the method to allow for an x,y position (in pixels) of the MWin. This can become useful if you ever wanted to place message windows above the heads of the characters talking in your game. Step 1 is shown below: You'll notice that we don't draw the canvas until the very end (right before the epilogue, but after the loop). This means that all the drawing will be taking place in an area invisible to the player (this is important for a later topic) and then placed on the screen when the drawing is done. Next we need to change the "painting" functions (fillRect, drawRect, and text) to be drawn onto the canvas. This requires us to add the optional parameter to draw onto the canvas, changing the positions passed into the functions. Remember that the rectangles and text will now be drawn relative to the canvas, not the screen. We are not done yet, there is still a problem. Run this sample code that we tried in Chapter 4 that worked perfectly: a = "Testing this to see if it works hiyo! Blah 1 2 3 "; a = a + a + a + a; myMwin(a, 50, 50); wait(); You will notice that the text doesn't wrap in the correct position. This is because the print function, used in the for loop, does not have an optional parameter to draw onto a canvas. We will need to resort to using the text function now, where the y coordinate increments by 1 for each new line (this is because text doesn't use pixels, so the next y coordinate is directly beneath the last line). To do this we initialize a counter variable outside the for-loop and then increment it within the for loop. Step 3 shows the final variation: The above method now allows us to place the canvas wherever we would like to, adding to the MWin's versatility. "Flickery" animations can be achieved by drawing directly onto the screen, which usually isn't the desired result. Instead of drawing directly onto the screen, we can use canvasses to implement a more fluid animation. Example 1 below shows how to draw a flickery animation of a rectangle going across the screen. While Example 1 can be made to be more efficient by limiting the savescreen/restorescreen functions to only the animated area, the result will still be similar - a flickery animation. The reason for this flicker is because I am painting twice on the screen for every iteration. This means that if the resolution was 640 pixels wide, I am painting 640x2 = 1280 times . The key to fluid animations is to perform the animation frames off the screen, and then display it on the screen when ready. This means that the next frame is ready to go and waiting to be placed onto the screen. Example 2 shows how we can use canvasses to make the animation much more fluid. Note that the positioning of several lines of code is important here. Example 2 creates and kills the canvas every iteration throughout the for loop. While this isn't very efficient, we are still achieving the goal of painting off the screen before displaying it on the screen. Note that when you kill a canvas, what is displayed on the screen does not disappear. Another important factor is the dimensions of the canvas. Its dimensions are the entire area where the box will animate. This is important so that when we draw the next frame, it overlaps the area of the last frame. This may take some time to sink in. Keep looking at where the canvas is drawn and what size it is drawn at. If you're still having trouble, try changing the size of the canvas. Also notice if we remove the createCanvas line outside of the for loop, we end up with a streak instead of a moving box. To fix this, we can cover up the streak by placing a pixel-wide line before continuing. The result is similar to example 2, except we save ourselves the creating and destroying of the canvas twice per iteration, increasing efficiency. While Example 3 is more efficient, it benefits greatly from the straightforward path we've chosen. Had the box moved randomly around, it would be more difficult to cover up its tracks. Example 4 shows how example 3 can be made even more efficient by reducing the size of the canvas to that of the box. For those that are paying attention, Examples 3 and 4 aren't drawing a perfect square as the animation passes through. However, the difference of one pixel is not noticeable to the naked eye, and so we can get away with it. There are other methods of accomplishing these animations, and functions such as canvasDrawPart and cavasGetScreen can be useful to you if you're looking to make some spiffy animations for your game. The use of canvasses greatly simplifies the way we use graphics in the toolkit. A similar non-primitive variable type to canvasses is the cursor map. After reading this chapter, you should be able to use cursor maps as well.
*I am in no way an expert, and the way this tutorial is written in no way implies that this is the correct way to code, nor is it the most optimized method.*
Chapter 6 - Graphics with Canvasses
- Canvass Basics
- Custom MWin Revisited
- Animations
- Conclusion
Introduction
Canvas Basics
*primitive* *just*
- create the canvas with a size in mind
- draw on to it using its identifier as the optional parameter to the drawing-functions
- draw the canvas at a particular position on the screen
- delete the canvas when you're done with it.
Custom MWin Revisited
**Chapter 4's Implementation of a Custom MWin**
```
autolocal(1); method myMwin(str) { // Prologue fSize = getFontSize(); red = 0; green = 0; blue = 0; getColor (red, green, blue); //red, green, and blue are passed by reference // Body strLen = len(str); if (strLen > 225) { debugger("Error: String too long."); wait(); } else { colorRGB(0,0, 200); fillRect(50,50,350,150); colorRGB(140, 0, 0); drawRect(50, 50, 350, 150); colorRGB (255, 255, 255); fontSize(18); strTemp = left (str, 45) // Gets first 45 characters of string text(4, 4, strTemp); // prints first 45 characters of string str = right(str, strLen - 45); // Chops off first 45 characters of string strLen -= 45; // Reduces string length by amount chopped off for (strLen; strLen > 0; strLen -= 45) { strTemp = left(str, 45); str = right (str, strLen - 45); print(strTemp); } } // Epilogue fontSize (fSize); colorRGB (red, green, blue); }
```
**Step 1**
```
autolocal(1); method myMwin(str, xpos, ypos) { // Prologue cnv = createCanvas(300, 100); fSize = getFontSize(); red = 0; green = 0; blue = 0; getColor (red, green, blue); //red, green, and blue are passed by reference // Body strLen = len(str); if (strLen > 225) { debugger("Error: String too long."); wait(); } else { colorRGB(0,0, 200); fillRect(50,50,350,150); colorRGB(140, 0, 0); drawRect(50, 50, 350, 150); colorRGB (255, 255, 255); fontSize(18); strTemp = left (str, 45) // Gets first 45 characters of string text(4, 4, strTemp); // prints first 45 characters of string str = right(str, strLen - 45); // Chops off first 45 characters of string strLen -= 45; // Reduces string length by amount chopped off for (strLen; strLen > 0; strLen -= 45) { strTemp = left(str, 45); str = right (str, strLen - 45); print(strTemp); } } drawCanvas(cnv, xpos, ypos); //Draws the canvas at the position passed // Epilogue killCanvas(cnv); fontSize (fSize); colorRGB (red, green, blue); }
```
**as well as**
**Step 2**
```
autolocal(1); method myMwin(str, xpos, ypos) { // Prologue cnv = createCanvas(300, 100); fSize = getFontSize(); red = 0; green = 0; blue = 0; getColor (red, green, blue); //red, green, and blue are passed by reference // Body strLen = len(str); if (strLen > 225) { debugger("Error: String too long."); wait(); } else { colorRGB(0,0, 200); fillRect(0,0,300,100, cnv); colorRGB(140, 0, 0); drawRect(0, 0, 300, 100, cnv); colorRGB (255, 255, 255); fontSize(18); strTemp = left (str, 45) // Gets first 45 characters of string text(1.5, 1.5, strTemp, cnv); // prints first 45 characters of string str = right(str, strLen - 45); // Chops off first 45 characters of string strLen -= 45; // Reduces string length by amount chopped off for (strLen; strLen > 0; strLen -= 45) { strTemp = left(str, 45); str = right (str, strLen - 45); print(strTemp); } } drawCanvas(cnv, xpos, ypos); //Draws the canvas at the position passed // Epilogue killCanvas(cnv); fontSize (fSize); colorRGB (red, green, blue); }
```
**Step 3 - final**
```
autolocal(1); method myMwin(str, xpos, ypos) { // Prologue cnv = createCanvas(300, 100); fSize = getFontSize(); red = 0; green = 0; blue = 0; getColor (red, green, blue); //red, green, and blue are passed by reference // Body strLen = len(str); if (strLen > 225) { debugger("Error: String too long."); wait(); } else { colorRGB(0,0, 200); fillRect(0,0,300,100, cnv); colorRGB(140, 0, 0); drawRect(0, 0, 300, 100, cnv); colorRGB (255, 255, 255); fontSize(18); line = 1.5; strTemp = left (str, 45) // Gets first 45 characters of string text(1.5, 1.5, strTemp, cnv); // prints first 45 characters of string str = right(str, strLen - 45); // Chops off first 45 characters of string strLen -= 45; // Reduces string length by amount chopped off for (strLen; strLen > 0; strLen -= 45) { line++; strTemp = left(str, 45); str = right (str, strLen - 45); text(1.5, line, strTemp, cnv); } } drawCanvas(cnv, xpos, ypos); //Draws the canvas at the position passed // Epilogue killCanvas(cnv); fontSize (fSize); colorRGB (red, green, blue); }
```
**Check Point Exercise**
1. Revise the final implementation of the custom MWin above to return the canvas when the function is finished. This allows further alterations to be made to the canvas, without losing it completely. Hint: Remove the killCanvas line as otherwise you lose the canvas. Also make sure you return at the very end of the epilogue (after colorRGB). **Easy**
Animations
**Example 1**
```
autolocal(1); getRes(x, y); //gets the resolution (e.g. 640x480) for (i = 0; i < x; i++) { savescreen(); //saves the screen before the rectangle fillRect(i,100,50+i,150); //draws onto the screen restorescreen(); //restores the screen after rectangle } wait();
```
*directly onto the screen*
**Example 2**
```
autolocal(1); size = 50; //dimensions of the square: size x size getRes(x, y); //gets the resolution (e.g. 640x480) for (i = 0; i < x; i++) { cnv = createCanvas(x, size); //Paint on canvas and display it fillRect(i, 0, size+i, size, cnv); drawCanvas(cnv, 0, 200); killCanvas(cnv); } wait();
```
**Example 3**
```
autolocal(1); size = 50; //dimensions of the square: size x size getRes(x, y); //gets the resolution (e.g. 640x480) cnv1 = createCanvas(x, size); for (i = 0; i < x; i++) { //Paint on first canvas and display it colorRGB(255,255,255); //white colour fillRect(i, 0, size+i, size, cnv1); colorRGB(0,0,0); //black colour fillRect(i, 0, i+1, size, cnv1); //thin line to cover up streak drawCanvas(cnv1, 0, 200); } killCanvas(cnv1); wait();
```
**Example 4**
```
autolocal(1); size = 50; //dimensions of the square: size x size getRes(x,y); cnv1 = createCanvas(size, size); for (i = 0; i < x; i++) { //Paint on first canvas and display it colorRGB(255,255,255); fillRect(0, 0, size, size, cnv1); colorRGB(0,0,0); //black colour fillRect(0, 0, 1, size, cnv1); //thin line to cover up streak drawCanvas(cnv1, i, 200); } killCanvas(cnv1); wait();
```
**Check Point Exercise**
1. Modify Example 2 so that it doesn't create/kill the canvas every iteration of the for loop, and instead use the clear function at the end of the for-loop to clear the canvas. Is this better or worse than Examples 3 or 4? **Easy**
Conclusion
Classes are, in my opinion, the greatest feature addition in the 3.x version of the Toolkit. Object Oriented Programming (OOP) simplifies just about every facet of programming a custom system, which is where the majority of coding takes place in a RPG Toolkit game. This chapter introduces you to OOP and the basic syntax of defining a class in the toolkit. Most of this chapter is theory, but is very important in understanding the chapters to come. Object Oriented Programming (OOP) is a method of programming that allows the programmer to define their own variables. Thus far we have seen variables such as numbers, strings, canvasses, and cursor maps. Now imagine you have the ability to create your own variable type. It can be whatever you want it to be. A pen, perhaps. But OOP allows you to create more than just a variable, it allows you to create an . An object is capable of two things: For example, think of a Warrior object. I can have variables tracking his strength, his health, his intelligence, etc. In addition I can define several functions for the Warrior object to perform, such as an attack function that, using his stored variables, returns the amount of damage dealt when he does an attack. When we define our own objects, we decide what it can do and what information it stores. This flexibility allows us to create just about anything we need to program in our games. One thing to understand about objects is that they are made from something called a Class. A Class is a template for that object. As such, I can have several objects deriving from the same class. Using the warrior example from before, suppose I created two warriors. warrior would have their own set of variables. So while they are similar in that they both have variables for strength, health, and intelligence, Warrior A may be stronger than Warrior B, and Warrior B may have more health than Warrior A. Because every object has its own unique attributes, OOP is ideal for programming custom systems such as battle systems, item systems, even custom message windows. To summarize: We know so far that an object is made up of several different parts (objects, variables, functions). These parts can be classified public or private. A private part can only be used within the object. This means that only functions of the object can alter or use the private parts of an object. A public part of an object is accessible by any function, whether it be a function of the object or a function not specific to the object. Example 1 details a pen object. This pen is capable of writing on the screen until it runs out of ink. At which point it needs a refill. A common question asked by programmers introduced to OOP is why it is necessary to have private parts. Why not just make everything public? The answer to this is pretty long-winded, and is explained throughout the rest of this section. Referring to Example 1, notice that one of the private variables (also called a private member) is colour. We don't want the programmer using our pen to be able to change the colour whenever they feel like it. This is a design decision I made to make the pen more realistic. If I'm writing an exam, I can't just look at my pen and yell at it to change colours. The colour of the pen will be defined when we initially create the pen, and cannot be changed thereafter. In our example, the public function write will simply output text on to the screen using the given colour. Depending on how much it is writing, ink will go down by a certain amount. When the ink is done, the programmer using the pen can use the function refill to set ink back to full. Most pens we use in real life allow us to see how much ink is remaining. Unfortunately, our design of a pen object does not provide this functionality. One possible solution is to make variable ink a public part. However this could lead to issues. The programmer using the pen may think he has the write to simply add to the ink. But doing so could result in the pen overflowing with ink because he put too much in. The better solution is to create an "accesor" function. An accessor function simply returns a copy of the value of a variable (in our case, the variable ink). In most class designs, for every private variable declared, there is also an accessor function that allows us to monitor said variable. A less common but equally important type of function is called the "mutator" function of a class. The mutator function allows the programmer using the object to change a private variable by a certain amount. But wait, if we provide both a mutator and an accessor function to a private variable, then what's the point of keeping the variable private? The answer is that inside these functions we can include error checking. If the programmer tries to mutate a private variable too much, too little, or even to a variable not of its data type (changing a numerical variable to a string), then the object will act intelligently and catch that error. Because objects are complex in their composition, the RPG Toolkit needs to be told how to create the object (a constructor) and how to delete the object (in a destructor). A constructor and destructor are implemented as functions of a class, and it is absolutely crucial they are defined. The names of these functions has already been determined when you name the class. For example, if I had named the class Pen, then: Pen( [insert parameters here] ); // is the constructor, and ~Pen( [no parameters] ); // is the destructor (note the ~ at the beginning) There can only be one destructor, however you can have more than one constructor. The difference between one constructor and another is the amount of parameters - so long as each constructor has a unique amount of parameters, it is legal. // Legal set of constructors Pen (ink, colour); Pen (ink); Pen (colour); // Illegal set of constructors Pen (ink, colour); Pen (ink, size); You may be wondering why you may want a number of constructors. This all depends on the design of your object. Using the legal set of constructors listed above: Pen (ink, colour); //Allows the programmer to set how much ink, and what colour the pen starts with. Error checking would be included to ensure not too much ink is used and a valid colour is selected Pen (ink); //Allows the programmer to set how much ink the pen starts with, and the colour is defaulted (for example, defaulted to blue) Pen (colour); //Allows the programmer to set what colour the pen starts with, and the ink may be defaulted to full Luckily, destructors are generally easy to define in the toolkit. As a rule of thumb, for most classes you create, you will only need to include something in the destructor if you used a canvas, cursor map, or another object. Otherwise you'd leave it empty. If you did use a canvas, then the destructor would have a line that called the canvas->release(); function. The above sections should have given the preliminary theory necessary to understand classes. In this section, we will see the actual syntax of a Pen class, despite its uselessness in game applications. Read through Example 2 line by line, an explanation of the code is found below. The class definition syntax is shown as simply stating: class [class name] { [class definition] } Then, everything after private: and before public: is considered private data and can only be accessed by the objects own functions. I chose to handle colour as a RGB value and so I needed 3 variables, and then of course there is the ink variable. I place under scores '_' before private member variable names to distinguish them as this when I start programming. Other programmers may write m_ink, but it's up to you. You could just have ink, but generally it's good to distinguish what are member variables by using the aforementioned two methods. When defining the public portion of the class, you will notice the 2 bold functions are implemented in the definition. This is generally only acceptable if the implementation is one line. The class definition portion of the program is meant to be easily looked at so you know what functions you can use with the object. The implementations for the other functions are below the class definition. The syntax is very important here. You must explicitly state that the function you are defining is for the class CPen. If you do not, then it's as if you are programming a stand alone method. method CPen::[function name] // tells the Toolkit this is a function for CPen method [function name] // simple creates a function not specific to any object (recall chapter 3) The remaining syntax should be self-explanatory if you've read earlier chapters. With regards to the destructor, because the object is only comprised of primitive variables you don't need to kill them off one by one. Thinking in an object-oriented sense is not an easy thing to do. If you didn't catch everything the first time you read through this chapter, do not feel discouraged. Read through it again and try designing some of your own classes. The best way to learn is to try.
*I am in no way an expert, and the way this tutorial is written in no way implies that this is the correct way to code, nor is it the most optimized method.*
Chapter 7 - Introduction to Classes
- Understanding Object Oriented Programming
- Public and Private Members
- Constructors and Destructors
- Defining a Class
Introduction
Understanding Object Oriented Programming
*object*
- Storing information - an object can have several variables (or even objects) inside of it keeping track of different things
- Performing actions - an object can have several defined functions that allow it to accomplish different tasks
**Each**
- An object is defined by a class, which is sort of like a template
- You can have several different objects that are defined by the same class, but these objects are all unique. Changing something in one object does not effect another.
- An object can store lots of different information by using variables and even other objects
- An object can "act" by calling one of its functions
Public and Private Members
**Example 1 - A Pen Object**
Private Parts: variable ink variable colour Public Parts: function write (message) function refill()
Constructors and Destructors
Defining a Class
**Example 2 - The Pen Class Defined**
```
autolocal(1); //Class Definition class CPen { private: var _ink; var _colour_r; var _colour_g; var _colour_b; public: //Constructor method CPen(colour_r, colour_g, colour_b); //Destructor method ~CPen(); method write(message); method getColour (&r, &g, &b); } //Class Implementation method CPen::CPen(colour_r, colour_g, colour_b) { //Error checking! if (colour_r > 255 OR colour_r < 0) { colour_r = 0; } if (colour_g > 255 OR colour_g < 0) { colour_g = 0; } if (colour_b > 255 OR colour_b < 0) { colour_b = 0; } //Set up member variables _colour_r = colour_r; _colour_g = colour_g; _colour_b = colour_b; _ink = 100; } method CPen::~CPen() { //The following is not necessary kill(_ink); kill(_colour_r); kill(_colour_g); kill(_colour_b); } method CPen::write(message) { length = len(message); // how many characters message is inkUsage = length/10; // ink used is 1/10 the amount of characters written if (inkUsage > _ink) { debugger("Not enough ink!"); } else { colorRgb(_colour_r, _colour_g, _colour_b); text(1,1, message); wait(); clear(); _ink -= inkUsage; //Use up the ink } } method CPen::getColour (&r, &g, &b) { r = _colour_r; g = _colour_g; b = _colour_b; }
method refill() { _ink = 100; }
method getInk() { return _ink; }
```
Conclusion
So far we have seen how to define a class and its functions. In order to use a class we have to first initialize it as we would any other variable. Then we need to use it using a special . When we are done with the class, and before its scope ends, we must destroy it. If you'll recall regular variables that were numbers or strings were destroyed at the end of the variables scope by the RPG Toolkit (assuming the use of autolocal). With objects we cannot rely on the RPG Toolkit to get rid of them due to their complexity, and must call the destructor of the object ourselves. If we do not do this, then we will lose access to the object, but it will remain in memory. No imagine thousands of objects sitting around, taking up valuable memory space. To initialize an object we call the constructor of the class. What happens is the constructor acts as a function, creating the object and then returning it to you. Because it is returned, we need to provide the object with an identifier (just like a variable). Using our CPen class from the last chapter, myPen = CPen(0,0,0); // create a CPen object. Now that we have our object, we can call the functions in its public domain by using the -> operator, myPen->write("Test"); ink_remaining = myPen->getInk(); show("There is " + ink_remaining + " ink remaining. Refilling now."); wait(); myPen->refill(); The code for using objects is very similar to calling the functions we used in Chapter 4. The difference now is that we must precede the function call with the object name and the -> operator. This tells the compiler that the function will only apply to the one object. One thing to be very careful about when using objects is when you need to create a copy of another object. Let us create two objects, myPen and otherPen, as follows: myPen = CPen(1,1,1); myPen->write("Test"); ink_remaining = myPen->getInk(); show("There is " + ink_remaining + " ink remaining. Refilling now."); wait(); You'll notice that we didn't call a second constructor for otherPen. Instead, we gave it the myPen object. By using such simple syntax with our definition of CPen, we actually have not created two objects. There is still only ONE object, except it has TWO identifiers. This is very important to understand as it is different from using regular variables. With the above code, I can now access the CPen object I created on line 1 using either otherPen or myPen (in C++ otherPen and myPen are called "pointers", because they point to an object rather than actualy "being" an object). Conversely, with a numerical variable this is the opposite: x = 1; a = x; a += 2; show(x); show(a); wait(); Here x and a are not "pointers". The RPG Toolkit reads the syntax and determines that a will have to be its own entity, and simply assume the value of x for the time being. Again, this is NOT the case with objects. This is quite possibly the most common pitfall in object oriented programming, and it is vital to understand. There are several operators available in RPG Code that we have been using commonly throughout this tutorial. There is the + operator, the - operator, the = operator, etc. When we define a class, we have the option to overload the default operators assigned to a class. One of the most commonly overloaded operators i the = operator. As seen in the previous section, setting one object equal to another causes one object to point to the other. If this is not the desired result, then we can simply overload the operator. Example 1 demonstrates how we can add an overloaded = operator to the CPen class: You will notice 2 new things from above: one obvious, the other not so obvious. The obvious one is the use of the keyword "this". What "this" refers to is the . The second thing to notice is that the operator= function accesses members of another object. This is allowed only in a select few cases, one of which being when you are overloading an operator. It is important to note that you should not be changing the rightSide object whatsoever. None of its functions were called, and as such it should not change. In order to use our newly created function, we must first define two objects: myPen = CPen(1,1,1); myPen->write("Test"); ink_remaining = myPen->getInk(); show("There is " + ink_remaining + " ink remaining. Refilling now."); wait(); otherPen = myPen; myPen->refill(); otherPen->write("Ten charac"); show("Other Pen: " + otherPen->getInk()); show("My Pen: " + myPen->getInk()); wait(); Notice here that otherPen now has a constructor of its own. If this was not the case, then the overloaded = operator function would never be called. Do you understand why? Also note that by defining an overloaded = operator, and by declaring otherPen and myPen a CPen object, we can no longer use them as normal variables. That is, the following is illegal: otherPen = CPen(1,1,1); myPen = CPen(1,1,1); otherPen = 5; myPen = "Hi"; This is because when we call the overloaded = operator function, it looks to find the member variables _ink, _color_r, etc. Unfortunately, the variables 5 and "Hi" have no such member variables, thereby causing an error. It is generally considered mandatory to define an overloaded = operator for your objects. This ensures you don't run into the problem listed above. Most RPG Code programs will not require the use of pointers in any way shape or form, so feel free to forget about them and focus on overloading assignment operators. What we achieved in the last section (with the overloaded = operator) will do essentially the same thing as a copy constructor. The difference is that a copy constructor will not waste as much processing time, and will not require as many lines of code. The syntactical difference between the two is that the copy constructor, by definition, has the same name as the class. The syntax of the copy constructor and overloaded assignment operator are pretty much identical. Note the "dummy" parameter for the copy constructor - this is due to a bug in the 3.1.0 version of the RPG Toolkit. The effect of copying one CPen object to another is the same, though, and this is what the copy constructor is for. myPen->CPen(1,1,1); otherPen->CPen(1, myPen); //creates a copy of myPen
*I am in no way an expert, and the way this tutorial is written in no way implies that this is the correct way to code, nor is it the most optimized method.*
Chapter 8 - More About Classes
- Using Objects
- Overloaded Operators
- The Copy Constructor
Using Objects
*operator*
** otherPen = myPen; // two identifiers to the same object myPen->refill(); otherPen->write("Ten charac"); show("Other Pen: " + otherPen->getInk()); show("My Pen: " + myPen->getInk()); wait(); // End of scope otherPen->release(); //myPen->release(); // This is wrong. Why?
Overloaded Operators
**Overloaded = Operator for CPen Class**
```
method CPen::operator=(rightSide) { this->_ink = rightSide->_ink; this->_colour_r = rightSide->_colour_r; this->_colour_g = rightSide->_colour_g; this->_colour_b = rightSide->_colour_b; }
```
*object being called upon* *private*
**otherPen = CPen(1,1,1);**
Copy Constructors
**Copy Constructor for the CPen Class**
```
method CPen::CPen(dummy, penObject) { this->_ink = penObject->_ink; this->_colour_r = penObject->_colour_r; this->_colour_g = penObject->_colour_g; this->_colour_b = penObject->_colour_b; }
```
{"twitter":[{"text":"Site is up and running, seems any initial problems are solved. See you on the forums :)","date":"Thursday at 2:55pm"},{"text":"New site is online but many of you will see a white screen, it's a problem with the PHPBB software. Trying to fix it, stay patient :)","date":"Thursday at 2:17pm"},{"text":"Site is online, little initial bug so apologies to those in the first 5 minutes who wondered why everything was broke :) Should be okay now.","date":"Thursday at 1:50pm"}]}
