---
kind: file
id: "toolkitzone.com/336"
site: "toolkitzone.com"
title: "#Bob!=9 #Joe$=\"hi\""
original_url: "http://www.toolkitzone.com/fileman.php?id=10&file=336"
written: null
date_confidence: "unknown"
updated: null
captured: ["20041031020416", "20041105205607", "20041105205655"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_336", captured: "20041031020416", sha256: "36963d18ee24eedc81ee03a740db268d24ba8372bb3d4e03529c9dc8ad40f646", wayback_url: "https://web.archive.org/web/20041031020416/http://www.toolkitzone.com/fileman.php?id=3&file=336"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_336", captured: "20041105205607", sha256: "2f0ef8afdfc5e8c81c3b3060e5e5f97fecc7659478f10887ce3e358d4db16340", wayback_url: "https://web.archive.org/web/20041105205607/http://www.toolkitzone.com/fileman.php?id=5&file=336"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_336", captured: "20041105205655", sha256: "60615001f7104fb817861556d8a2e30a6408e96baf786179d2e0de026b6d8d00", wayback_url: "https://web.archive.org/web/20041105205655/http://www.toolkitzone.com/fileman.php?id=10&file=336"}
---

# #Bob!=9 #Joe$="hi"

#Method Introduction() { Hi everyone. OC here! Today you're gonna learn about little things I like to call arrays. But first, I'll let you get to know me (don't worry, I'll get it over with quickly). First and foremost, I'd like you to get to know my evil side. So join me in laughing in the faces of all those who thought I'd never become anything of a programmer. Ahem...
...BWUAHAHAHAHAHAAHHAHAHAHAHAH! Thank you. Now, over to my nice side. Uh, people say I'm nice. Good! Now you know me. Next, onto the important stuff. }
#Method Variables() { :about_variables This part is aimed toward newbies. So if you know how variables work and don't want to go over the basics again, you can skip this part.
A variable is used in programming as a piece of information that has a name. You can use variables to store names, numbers, locations, and almost anything else you can think of. In RPGCode, a variable is made when you put a $ or ! after a name. This is called declaring a variable. When you declare a variable with the $ symbol, that means that it is a literal variable. A literal variable can store literal values, or characters (or, if you don't know the term characters, then letters such as a, b, and c). When you declare a variable with the ! symbol, that means that it is a numeric variable. A numeric variable can store numeric values, meaning it can store numbers.
The way a variable stores information is by using the '=' (equals) symbol. The variable name is typed on the left side of the = symbol, and the value is typed on the right. If that's confusing for you, here's an example of how to store 9 in the numeric variable Bob! and the word "hi" in the literal variable Joe$:
#Bob!=9 #Joe$="hi"
See? It's that simple. Now you can use the variables whenever and wherever you want inside the program you declared them in. }
#Method Display_Variables() { Now, I'll show you how to display variables using two of the Toolkits built in commands, #Text and #Mwin. The first is the #Mwin command. This command is used for displaying dialogue on the screen during your game, which is encased in a (by default) blue box. Before I show you how to display the variables inside of the #Mwin command, you'll need to get aquainted with the command itself first. So here's an example of how the command is formatted:
#Mwin("Text goes here")
Easy! Just do that and whatever you write inside of the quotation marks (" and ") is displayed on the screen. Now, you'll need to make it stay on the screen until the user presses a button. This is how you do it:
#Mwin("Text goes here") #Wait(a$)
Let's look at that #Wait command. Does something in there look a bit familiar? The a$ is a literal variable! It stores the users key press inside of it, and then the next statement (or line of code) gets run. Now, this is an important part about the #Mwin command: it doesn't disappear by itself. You need another command to do that. And here's how it works:
#Mwin("Text goes here") #Wait(a$) #MwinCls()
Now we have the #Mwincls() command. Does it look confusing? It's simple once you know what it means. Mwin means Message Window, and Cls is clears. Just a bit of information so the command makes a little more sense. #Mwincls() clears the message window and the text inside of it. So now, you've learned three great commands that will definitely help you on your way to making an RPG.
Now, the part you've been waiting for: displaying a variable inside of the #Mwin command. First, what you need to do is declare a variable and give it a value. I'll use Joe$ (the one we used before). And inside of Joe$, I want to store the value "hi".
#Joe$="hi"
Okay! We've got the literal variable Joe, with the value "hi". So what do we do with it? We can't just leave it sitting there. So let's put it onto the screen using the #Mwin command. This is different from displaying regular text, because you need to enclose the variable Joe$ in < and >. Now, put that into the #Mwin command, like so:
#Mwin("") #Wait(a$) #Mwincls()
And there you have it! The value "hi" is printed onto the screen using the #Mwin command. Now that you know how to display text and the values of variables with the #Mwin command, I'll give you something a little different: The #Text command. The #Text command is harder to use than the #Mwin command, but it's more flexible in terms of placement (that means you can display text anywhere on the screen). The way the #Text command works is like this:
#Text(x!,y!,text$)
Confusing? Let's look at it piece by piece. x! is a variable that stores the width (or how far from the left side of the screen the text will be), and y! stores the height (or how far from the top of the screen the text will be). text$ is where your text goes. The text in this command is like the text in the #Mwin command, enclosed in quotation marks. So you can try something like this:
#Text(3,3,"Hello world!")
As simple as that! That will stay on the screen until you clear it with the #Clear command. So I don't recomend using it while you're on a board. Anyway, now we're ready to learn how to display a variable inside of the #Text command. This is where it becomes very separated from the #Mwin command, because you don't show the variable inside of the < and > (left and right angle brackets), you just use it's name. Here's an example of what I mean:
#Text(3,3,Joe$)
And congratulations! You've made it to the next step in this tutorial! You've been reading a lot though, so you might want to grab a cookie for yourself and take a small break (so you don't take in too much at once and forget it all later). }
#Method What_Are_Arrays() { An array is just like a variable with one exception: it can store multiple values with one name. This is a really good way to store information about an enemy, or character, or anything and have it all under the same name. Arrays are simple enough to use once you get the hang of them, although sometimes they may look a little intimidating. The way they store multiple pieces of information under one name is by using [ and ] (or square brackets). A number, letter, or even another variable can go inside the square brackets. But for right now, I'll just use numbers. A little confused at the concept? Well here's a look at what I mean:
#Item[0]$="Bob" #Item[1]$="Joe" #Item[2]$="Bill"
See how that works? I used a number from 0 to 2 to assign each item a different value. As you can see, this is in fact one of the best ways to store groups of information. Without having to give each variable a different name. You could name them different names like Item1$, item2$, and so on, but it looks much more professional (and cooler too) when you use arrays. And if that isn't enough for you, it makes you look like a fancy shmancy programmer :D. }
#Method More_Advanced_Arrays() { Next, we'll take a look at arrays with variables inside of the brackets. This part is very useful if you want to make a list of things, but don't know what order things will go in. The way you do this is declare a variable, give it a value, and then use that inside of an array. Like this:
#Slot!=0 #Item[Slot!]$="" #Slot!=Slot!+1 #Item[Slot!]$=""
Right now, that might seem really confusing. But you'll get the hang of it eventually. Let's take a look at it step by step and see if we can find out what it does. First, it declares a variable called Slot! and assigns it the value 0. Then, you make an array and but Slot! inside of the brackets. So right there, you're actually doing the same thing you did before, because when you put a variable inside of the brackets, what it does is places it's value you. So, you come out with #Item[0]$. The other way might seem easier, and in some cases it's a better way of doing it, but this method of making arrays is great if you want to make a complicated and advanced program.
The next part is a lot more complicated, so bare with me. It involves If statements (also known as conditionals). If you don't know what the #If command does, then I'll give you a quick over view (or, you can fire up the toolkit and look in the RPGCode command reference). The #If command is a command that checks to see if a certain condition is true or false. If it is true, then a block of code gets run. If it is false, then the code does not get run and you can either end the program, go back and check again, or do a number of other things. Here's what the #If command looks like:
#If(condition) { code to run if true... }
That's the basic outline of the #If command. But let's put some more to it so you can understand it a little better...
#Joe$="hi") #If(Joe$=="hi") { #Mwin("JOE: ") #Wait(a$) #Mwincls() #End }
What that does is declares the variable Joe, which you've seen many times over in this tutorial. Then, it asks the computer If Joe$ is equal to "hi". Obviously, Joe$ is equal to "hi", so the next block of code gets run. You see that the #Mwin command is used to display a person named Joe saying "hi". Then, it waits for the user to press a key, clears the message window, and ends the program. If you still don't have a firm grasp on what the If command does, read the help files and play around with the command.
This next part gets really confusing if you're just learning how If statements work. So try and hang in there the best you can. Here, I'm going to be using arrays and if statements together so you can make a more advanced version of the list program. Here it is:
#Slot!=0 #Item[Slot!]$="" #If(Item[Slot!]$="") { #Item[Slot!]$="Bob" #Slot!=Slot!+1 } #Item[Slot!]$=""
At this point, you might be jumping and screaming in fear of this program (if you're new to this kind of thing, anyways). But don't worry, it's really quite simple! Again, I'll explain how this works to you step by step. First, the variable Slot! is assigned the value 0. Slot! is then placed into Item[]$. So now, Item[] is given the value 0 inside of the brackets (item[0]$). I set it so Item[Slot!]$ equals nothing. Then the #If command is brought to the table. It asks the computer If Item[Slot!]$ equals nothing. This, obviously, is true, so the block of code inside the { and } is executed. Inside the If statement, we gave Item[Slot!]$ the value Bob. So now, Item[Slot!]="Bob". In plain English, it would be like saying "Item 0 equals Bob". Sinking in yet? Good, 'cause we're not done! Next, we have #Slot!=Slot!+1. This may look really confusing too, considering I haven't told you about this. What this does is tells the computer that Slot! equals Slot! plus 1. So really, you're assigning a new value to Slot!. Then, it starts all over again, but this time Slot! equals 1.
Phew... That was a lot of explaining. And still kinda confusing. So if that wasn't enough for you, here's the entire program again, except it's translated into English:
Slot! equals 0. Item 0 equals nothing. If item 0 equals nothing, assign it the value "Bob". Then, add 1 to Slot!, making it 1. Now, Slot! equals 1. Item 1 equals nothing. And so on, and so forth.
So now you see how it all comes together. Basically, all it does is check to see if Item 0 is nothing, gives it a value, and moves on to the next Item. So really, once you think about it, it's a simple program. }
Well, that concludes this little tutorial on how to use variables and arrays. You just learned a LOT of information that will lead you down the path of becoming a great programmer. Like you, I still have a lot to learn about programming. All I'm doing is passing what I've learned down to newer generations. So until my next tutorial, bye bye!
#Method Credits() { Written by Sam (Occasionally Correct) February 27th, 6:18AM, 2004.
Special thanks to... Allyson, my girlfriend of one year now. CBM for making the RPG toolkit. Vampz for making this great site that I can submit my knowledge to! And.. Some other people. :D }
