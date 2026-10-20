---
kind: forum-thread
id: "toolkitzone-forums/24023"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "P90\\'s Coding forum Tuts&source"
skin: "phpbb2"
thread_id: "24023"
title: "I need help with these (weird) coding stuff"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=24023"
written: "2005-10-03T12:00:00"
last_post: "2005-10-04T11:45:00"
date_confidence: "exact"
captured: ["20060111131357"]
author: "X"
repliers: ["Phalanxia", "lavarock09", "Tao-Kun", "p90m16mp5a4"]
authors: ["X", "Phalanxia", "lavarock09", "Tao-Kun", "p90m16mp5a4"]
posts_present: 7
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_262259_amp_3Bsid_f2c01a272b36fe85bb1c4aa1247f23ae", captured: "20060111131357", sha256: "d83da01ee7791fb03965c1cd657ce8f70dd03851bab2f04989ce56afdec3485d", wayback_url: "https://web.archive.org/web/20060111131357/http://www.toolkitzone.com/forums/viewtopic.php?p=262259&amp%3Bsid=f2c01a272b36fe85bb1c4aa1247f23ae"}
links: []
---

# I need help with these (weird) coding stuff

### X · 2005-10-03 12:00 · #B262022

Well, I was going to post this in the advanced code section, but you are always the first to reply to the topics, so I will just put it in your forum to make things faster. I need help with these:
1) As far as I know, there are a few variables named playerHandle[X]$, which hold the name of the five characters in the team. I want to know if there is any way to get the names of more than five characters, in order to make CBSs and CMSs which work with larger numbers of players.
2) The CallPlayerSwap() command was not working, so I made my own program to arrange my party. The problem is, it is extremely big (somewhere about 14 Kb, and 7 pages in Word), and only swaps 8 characters. In the game I am making, you will be able to control more than 5 times that number, so I wanted to know if there is any possible way to get the names of the players that have been removed with the RemovePlayer() command, or at least if there is any way to use something like stacks or queues (well, Pascal is the only thing we have seen so far in the University), to get the names of the players in the order they are removed.
3) Okay, I have no idea of how to explain this in English, but I will try my best. I need to know if it is possible to call the value inside a variable without writing the variable name as you would do normally. This is, if the variable is called "Dude_dex!", I want to know if you can pass it´s
value to another variable without typing "box! = Dude_dex!", but using instead something like this:
Part_A$ = playerHandle[0]$
Part_B$ = "_dex!"
box! = (Part_A$ + Part_B$)
Or:
box! = playerHandle[0]$ + "_dex!"
As you may have guessed, I am using this to write methods that get the custom stats I am using for my game (Like GetFP("Source")). I have tried with using Classes and Structures, but if I put the variables under private scope, I cannot access them; in the other hand, if I put them under public scope, I can access them, but the Debugger says something like:
"You seem to be exposing variables from your class--this defeats abstraction by circumventing
encapsulation--you may want to reconsider this choice of action; dex!"
everytime I run the program. Also, if I try to assignate the Object to the Class like I tried to do with the variables, the computer locks up and a message says that there is some error with the Kernel. E.g:
If the object is called "Dudeobj" and the class is "dudeclass", I try with:
playerHandle[0]$ + "obj" = playerHandle[0]$ + "class()"
Or:
Part_A$ = playerHandle[0]$ + "obj"
Part_B$ = playerHandle[0]$ + "class()"
Part_A$ = Part_B$
If this worked, it would be great, but it doesn´t work, instead it screws up my Kernel.
Any ideas of how to fix (any of) those?

### Phalanxia · 2005-10-03 14:50 · #B262048

Well i can't help you!!! Everyone thank me for being useless.

### lavarock09 · 2005-10-03 15:31 · #B262061

**Phalanxia wrote:**

> Well i can't help you!!! Everyone thank me for being useless.
>

Shut the hell up!
If you can't help, don't post, you're making your self look like a complete idiot, or are you already? *shakes head out of thought* who cares, just shut up!

### Tao-Kun · 2005-10-03 19:20 · #B262097

I apologizes, but I had to edit your topic. All the words bunched up together like that was hard to read.
1. ACutally, there is a way. I never done it myself, but there is a tutorial either on this site or on the mystic site telling you how. I thought you could have more then 5 characters though, just not all playable at the same time O.o..
2. Sorry, can;t help
3. I would think yes. I mean, in my game, I consitly put the name of Player 1 into a varible. Like:
profile$ = playerhandle[0]$
mwin("His name is <Profile$>")

### Phalanxia · 2005-10-04 07:37 · #B262241

**lavarock09 wrote:**

>
> **Phalanxia wrote:**
>
> > Well i can't help you!!! Everyone thank me for being useless.
> >
>
> Shut the hell up!
> If you can't help, don't post, you're making your self look like a complete idiot, or are you already? *shakes head out of thought* who cares, just shut up!
>

Meh.
Someone woke up grumpy today.

### p90m16mp5a4 · 2005-10-04 08:34 · #B262250

1. The variable is only for current party members.
2. Instead of trying to track RemovePlayer(), make your own tracking system.
3. I don't see the point in number three. You are talking about what I call 'automatic' functions, wich do something without you having to modify the source code. You may want to try #RPGcode, It has a good versatility, but lacks debugging power, and you can do the same things without it.
a$ = "hi"
b$ = "a$"
RpgCode(b$ + "= Hello") //This runs ' a$ = "Hello" '
Show(a$)
wait
I can't imagine a 18kb callswap method, Word makes the programs very large though, to truly see how large it is, save it as .txt, or tell us how many lines the program is.
[un-needed yabber]
(yabber isn't a real word)
An 18kb callswap for me would have 20 objects, each wich use four methods, 20 methods for graphics, and 20 methods for text. THats a big program, lol.
[/ un-needed yabber]

### X · 2005-10-04 11:45 · #B262259

Well, actually, I wrote the callswap thingie a long time ago and it was crappy, because I didn`t much RPGCode, so I just assigned some fixed places on the screen for the players profiles and stats to appear, which made the program (does this word exist? =>) uselessly big. I guess I could write a new one in much less space, and keep the (not really) nice looking (does this word exist? =>) clickable button thingies I coded back then. And the 14Kb were not in ".doc", but in ".prg".
Also, I think I have found a way to fix the problem with classes (number 3), but I have just figured it out on my way to the cyber, so I will try it later.
I think I also found a crappy way to make a tracking system (figured it out while writing these lines), so I will try it later too.
I will look now for the tutorial Tao-Kun mentioned, but I think I already read that one before.
EDITED: Okay, I have solved all the stuff, but I don´t know how to put that *Solved* thingy next to the topic name, so if anyone knows how to do it please tell me.
