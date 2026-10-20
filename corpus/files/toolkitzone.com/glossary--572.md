---
kind: file
id: "toolkitzone.com/572"
site: "toolkitzone.com"
title: "Glossary"
original_url: "http://www.toolkitzone.com/fileman.php?id=10&file=572"
written: null
date_confidence: "unknown"
updated: null
captured: ["20041106041222", "20041106082024", "20060304162046"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_572", captured: "20041106041222", sha256: "a59a15b438e92b58e1ee67d91a5848b4cf279f7f80aeb7fefeb030d32038c204", wayback_url: "https://web.archive.org/web/20041106041222/http://www.toolkitzone.com/fileman.php?id=10&file=572"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_572", captured: "20041106082024", sha256: "c9b93537f5a4c8d0eeeed693319387b00a31f168b6df560e580856d8c3a600a0", wayback_url: "https://web.archive.org/web/20041106082024/http://www.toolkitzone.com/fileman.php?id=5&file=572"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_572", captured: "20060304162046", sha256: "413cd4ac1ee6bd033279e25c4b100af779f20700682d908ff4d6624bbaa0eb3b", wayback_url: "https://web.archive.org/web/20060304162046/http://www.toolkitzone.com/fileman.php?id=3&file=572"}
---

# Glossary

Special moves:
While I was on TKZ forums today and I noticed that there was a post on how to do special attack variables. I too had this problem when I was a n00b, so, It is very frustration to look at it all the time, so I am making a tutorial on how to do it instead of wasting vampz's Precious space and bandwidth.
**Glossary**
-
Variables
-
how to learn special moves
-
#fight()
Variables are the little gears of your game, you can go a short time without them, or a long time depending on what you are doing, I expact you not to know what or how to use a RPGcode variable.
The variables are like so: ! - means it's a number. $ - means it's going to be or is text . It's always good to initialize a variable, like so #myname$=Wordtwo , Or #myage!=14. Variables are everywhere, and without them you couldn't make a RPGgame (or at least a good one). Even the "#wait(A$)" uses a variable, it takes the key pressed and put it into "A$". This is also good for things like #if statements. #if(A$==1). The #for loop and the #while loops also need variables to operate. Everything you do will almost all ways need a variable, even if it's talking to a girl on your game ;). Some things require a load of variables like BSes, or MSes. And a variable cannot be a keyword/ command. It cannot be #for!=50, but it can be #four!=50. Or #Mwin$=Word, but it can be #mwind$=Word. You need variables for everything, no matter what it is, sooner or later a variable is going to rear it's ugly head in on you, but you have got to be ready to push it away. After all, everything advanced needs a variable :).
Ok to start you have to make a special move. Then you go to the character editor --> hit special moves ---> Click on "1 - None" ----> Change special move ---> select the file ---> then hit special move info -----> put 9999999 for EXP 9999999 for level and finaly for special move being the first one put in: specialmove1! , then in the secon box put 1.
In a Program please type the following:
#fontsize(16)
#mwin("how are you?")
#delay(1)
#mwin("Im going to teach you your first special move!")
#wait(A$)
#mwin("doeesn't that sound good?")
**#specialmove! = 1**
#mwin(" you now know the new special move :)" )
#wait(A$)
#end()
in the bold font is how to initialize the special move, if you want it to be more complex like in a if statement please view the following code snippet:
#fontsize(16)
#mwin("how are you?")
#delay(1)
#mwin("Im going to teach you your first special move!")
#wait(A$)
#mwin("doeesn't that sound good?")
#mwin("please press 1- for no and 2- for yes)
#wait(b$)
#if(b$==1) { #mwin(ok fine have it your way)
#wait(A$)
**#specialmove! =2**
#if(b$==2)
#mwin(here you are)
**#specialmove! = 1**
#wait(A$)
#mwin(" you now know the new special move :)" )
#wait(A$)
#end()
You can only learn the special move if it equals 1, therefor you can do specialmove!= 2 or you don't even have to use it at all if you want.
The #fight command makes you fight a enemy on a backround. The correct way to have this done is like this: #Fight(5, Fire.bkg). #fight starts a fight with a level 5 monster or somthing on the backround Fire.
Variables should be used to intiate a fight, like with the #if statement. Like so:
#fontsize(16)
#mwin("do you want to fight?")
#wait(A$)
#mwin( "1 for yes and 2 for no")
#mwin(B$)
#if(B$==1) { #fight(5, FIRE.BKG)
#end() } #if(B$==2)
#mwin("you chicken")
#wait(A$) #end() }
You could do loops, but It wouldn't be necessary at this point. All you would have to do is put a #while() and a #Fbranch.
