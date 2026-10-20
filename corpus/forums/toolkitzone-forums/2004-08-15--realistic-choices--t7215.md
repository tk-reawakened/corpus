---
kind: forum-thread
id: "toolkitzone-forums/7215"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "7215"
title: "Realistic choices"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=7215"
written: "2004-08-15T18:15:00"
last_post: "2004-08-15T18:34:00"
date_confidence: "exact"
captured: ["20040925162216"]
author: "bradseguin"
repliers: ["Occasionally_Correct", "Night_Elf"]
authors: ["bradseguin", "Occasionally_Correct", "Night_Elf"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_75981_amp_", captured: "20040925162216", sha256: "2db44e3379332f659c57d766efc49abae1f191bdaec3f2d1e6c1dd05289e7fd4", wayback_url: "https://web.archive.org/web/20040925162216/http://www.toolkitzone.com/forums/viewtopic.php?p=75981&amp="}
links:
  - {url: "http://dontemailmeanycrap.com/avatar.gif", status: "external", local: null}
  - {url: "http://img.photobucket.com/albums/v207/funeral6/fsban2.gif", status: "external", local: null}
  - {url: "http://img.photobucket.com/albums/v214/night-elf/Animation1.gif", status: "external", local: null}
  - {url: "http://img.photobucket.com/albums/v325/brent329/sw018.gif", status: "external", local: null}
  - {url: "http://overkill2013.geahost.com/Anti-Everything.png", status: "external", local: null}
  - {url: "http://www.jellyphant.myfreebb.com", status: "external", local: null}
  - {url: "http://www.startrekers.myfreebb.com", status: "external", local: null}
  - {url: "http://www.winefromwater.myfreebb.com", status: "external", local: null}
---

# Realistic choices

### bradseguin · 2004-08-15 18:15 · #B75976

I need help!
I just started a new game and I want mostly all conversations to have realistic responses from the play, example:
Man: Can you help me please?
Answer: 1- help him
2- help him but demand reward
3- kill him
4- dont help him
I want to be able to make conversations like this without having the "Prompt" window pop up. Does anybody know how to do this?
_________________
![](http://overkill2013.geahost.com/Anti-Everything.png)![](http://dontemailmeanycrap.com/avatar.gif)
![](http://img.photobucket.com/albums/v325/brent329/sw018.gif)
Wherever you see the evil monkey on the stairs pointing at you, you know I was there.

### Occasionally_Correct · 2004-08-15 18:32 · #B75980

Just use If statements to check what the user pressed, and act upon their decision:

**Code:**

```
#done! = 0

#While(done! == 0)

{

   #Mwin("Hey, be a pal and help me out.")

   #Mwin("[1] Alright. I'll help.")

   #Mwin("[2] I'll help, but you have to give me a reward.")

   #Mwin("[3] Die. Die. Die.")

   #Wait(answer!)

   #Mwincls()

   #If(answer! == 1)

   {

      *Help the guy.

      #done! = 1

   }

   #If(answer! == 2)

   {

      *Ask for a reward.

      #done! = 1

   }

   #If(answer! == 3)

   {

      *Kill the bugger.

      #done! = 1

   }

}

#Kill(answer!)
```

Use that as a basis for your program and just replace the commented lines with events relevant to what the user pressed.
_________________
:: it's better in the matinee, the dark of the matinee ::

### Night_Elf · 2004-08-15 18:34 · #B75981

yeah. Heres an example of an mwin based one.

**Code:**

```
#Mwin("Man: Can you help me please?")

#wait(a$)

#mwincls()

#Mwin("1- help him  2- help him but demand reward")

#Mwin("3- kill him  4- dont help him")

#wait(help!)

#If(help!=1)

{

#Mwin("You: Yeah I'll help")

#wait(a$)

#Mwincls()

*etc.

}

#If(help!=2)

{

#Mwin("You: Ok, but I demand payment!")

#wait(a$)

#Mwincls()

*etc

}

#If(help!=3)

{

#Fight("man.ene","bkg1.bkg")

}

#If(help!=4)

{

#Mwin("You: No, sorry.")

#wait(a$)

#Mwincls()

*etc

}
```

Thats just a example obviously/
_________________
[Wine From Water](http://www.winefromwater.myfreebb.com) | [Star Trek: Online Frontier](http://www.startrekers.myfreebb.com)
[![](http://img.photobucket.com/albums/v214/night-elf/Animation1.gif)](http://www.jellyphant.myfreebb.com)
![](http://img.photobucket.com/albums/v207/funeral6/fsban2.gif)
