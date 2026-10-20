---
kind: doc
id: "toolkitzone.com/106"
site: "toolkitzone.com"
title: "By Slipknot42388 AKA Sean"
original_url: "http://toolkitzone.com/library.php?mode=read&doc=106"
written: "2006-02-04T12:56:00"
date_confidence: "exact"
updated: null
captured: ["20060213005514", "20060222122941"]
author: "slipknot42388"
repliers: []
authors: ["slipknot42388"]
comments_present: 0
f_author: "slipknot42388"
f_date: "February 4, 2006, 12:56 pm"
f_description: "Slipknot42388's own custom code solution to adding jump functionality to your TK3 side scoller, including full explanation from the man himself."
f_section: "RPG Code"
f_title: "Easy Side Scroller"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_106", captured: "20060213005514", sha256: "6d53c2e06eadd3177cc649d57c570bb50a806f487ca00d2076595f5df48268ad", wayback_url: "https://web.archive.org/web/20060213005514/http://toolkitzone.com:80/library.php?mode=read&doc=106&PHPSESSID=374ad37a3635070021cff42be32021a5"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_view_cadd_doc_106", captured: "20060222122941", sha256: "5209d930d9359858f6e2b23581e7027ffb8624c42c4e4453b2944305ca4f9eb8", wayback_url: "https://web.archive.org/web/20060222122941/http://toolkitzone.com:80/library.php?mode=read&view=cadd&doc=106&PHPSESSID=374ad37a3635070021cff42be32021a5"}
---

# By Slipknot42388 AKA Sean

EASY SIDE SCROLLER
Chapter 1 : The Jump Program
**By Slipknot42388 AKA Sean**
Hello everyone, welcome to my first tutorial. Today we will talk about making a jump command for a side scroller. I have seen many people asking how to create such a feature on the forums, so here is my version of how to do one in RPG Toolkit 3.0.6.
1. Understanding of a Little Bit of Programming **What You'll Need**
push() get() Time() moveME() **Commands We'll Be Using**
Time() moveME() **Methods We'll Be Making**
Okay, so now that you have seen what commands we will be using and what methods we will be making let's start with the jump program itself, here is how the main program will look.
*jump command programed by slipknot42388* include("time.prg") push("N,N","sam") moveME() time(1) push("S,S,S,S,S,S,S","sam")
That's the main program for the jump command, so let's look at what we did:
1st : We had to include a program that holds the two methods we'll be making later. 2nd : We used the command push() to move the player upward two spaces. 3rd : We used a command we'll be making later moveME(), what this does is check to see if a button was pressed such as "left" and moves them in that direction while the player is in the air. 4th : We used another command we'll be making later, time(), what this does is makes a set time the player will be in the air. I explain this better later on. 5th : We then use the push() command again, but this time sending the player back down. This is to make it look like gravity is polling the player back down.
Okay, there you have it - as you can see, nothing hard! Now let's move on to making our methods.
**Method 1: time()**
*method coded by slipknot42388* method time(num!) { time!=0 run!=random(num!) If(run!==1) { total!=time!+1 time!=total! } }
Okay, so there you have the time method, let's take a closer look:
1st : We have to declare it as a method with the method name "time" and then we have a variable num! inside the ( and ), this is for the random number slot. 2nd : We declared a variable called "time!" and we made it equal 0. 3rd : We used the random command using the variable we declared at the top, "num!", to selcect a random number from 1 to "num!". 4th : We used a "IF" statement to execute if the random number, "run!", is equal to "1". 5th : Inside this block we declare a new variable called "total!" and this equals the variable we declared earlier, "time!", and then adds "1" to it. 6th : We then have the variable "time!" equal the variable total, you should know by now why that is like that.
And that is it for this method. The reason we need it is because when you jump you normaly have some hang time and then come back down, well this method gives the player just that. Of course you can add on to the code to make it have more hang time. Lets move on to the next method.
This method will let the player move in a direction while in the air. **Method 2: moveME()**
*method coded by slipknot42388* method moveME() { get(move$) If(move$=="LEFT") { push("NE","sam") push("E","sam") push("SE","sam") } ElseIf(move$=="RIGHT") { push("NW","sam") push("W","sam") push("SW","sam") } ElseIf(move$=="B") { get(move2$) push("N,N","sam") If(move2$=="LEFT") { push("NE","sam") push("E","sam") push("SE,"sam") push("S,S","sam") } ElseIf(move2$=="RIGHT") { push("NW","sam") push("W","sam") push("SW","sam") push("S,S","sam") } } Else { get(move$) If(move$=="LEFT") { push("E,E,E","sam") } ElseIF(move$=="RIGHT") { push("W,W,W","sam") } } }
Okay, there is the method "moveME", lets take a look at what it does:
1st : We used the command get() with the variable "move$" to get a key press. 2nd : We nowI have to check if a button is pressed. In the first IF statement it checks if the "LEFT" key was pressed but what it really does is check if the "Right" key was pressed (don't ask me why this is, but it is). For some reason you'll have to put in "LEFT" to get it to check if the right key is pressed. Then we used the push() command to push the player in a arc like motion. 3rd : We have it set to IF "move$" equals "B" to allow for a double jump like move. So in other words it sends the player up higher than they would normally jump. 4th : We then have another get() command with another variable "move2$" inside of it. So as with before it'll be used to check if a button is pressed. "move2$" is being used for the right and left movement in the double jump. 5th : We use the "else" command to check if the left or right button is pressed down to move the player a few extra spaces while still in the air.
There you have it that's the jump command. If your good at programing your probably shiting your self how easy it is to make a jump program.
So that is everything you'll need in the programing department. But what about the graphics? This is easy since all you have to do is set the player's north and and south graphics to the east graphics and there you have a person who looks like they're jumping. Then you'll need to make some graphics for the background (ground & sky). Plus add things for the player to jump onto.
Now you're probably asking yourself where do I set this program to run it? Well open your mainfile box in the toolkit editor and go to the RPGCODE button and select the "Run time program" button, then select the jump program. Then go down to the "run time program activation key" and click in the box and set it to what button you want to use. Now save the mainfile and go play around with our new jumping player.
I'll be messing around with this some more to make some cool things for this type of game. I'll put it in the update for this tutorial. If you tweak any of the codes to make them run better let me know and I'll be sure to put yours in the update.
Well this is all for now, I hope this helps people understand things alot better about making a jump program.
later on Sean
slipknot42388
February 4, 2006, 2:12 pm
So what does everyone think?
Insanity
February 4, 2006, 6:42 pm
... Uh, I didn't actually read the article (as I'm not interested in the subject), I read the code examples, but there're FAR better ways to do a side scroller in TK. Using Push() and such methods is just annoying and won't work very well =/
slipknot42388
February 4, 2006, 7:24 pm
um the codes I put above do work they work real good. I made sure everything worked just right befor writing this tutorial. If you would of read the tutorial you would of been explained better for what each code does. And I'm sure there is other way's of doing it, this is just my way.
blanel
February 6, 2006, 8:31 am
Fairly good actually. Only trouble is that gravity aint really working... you can walk off ledges and shit and levitate... Otherwise very cool program :) and i guess its quite basic so even noobs like me could understand it ;)
slipknot42388
February 6, 2006, 8:26 pm
ya I fixed most of the programs in this so when you walk off stuff you fall. So it'll be in the next update
TOPLIZARDS8
February 7, 2006, 3:58 pm
Just gettiletype below the player and if it is normal pusht the player South. Problem fixed.
slipknot42388
February 7, 2006, 4:37 pm
humm I didn't think of doing it that way thanks
Slipknot42388's own custom code solution to adding jump functionality to your TK3 side scoller, including full explanation from the man himself.
May 7, '05
Apr 7, '05
Jan 1, '05
Nov 30, '04
