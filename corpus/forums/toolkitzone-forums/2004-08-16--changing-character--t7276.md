---
kind: forum-thread
id: "toolkitzone-forums/7276"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "7276"
title: "changing character"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=7276"
written: "2004-08-16T18:19:00"
last_post: "2004-08-17T16:33:00"
date_confidence: "exact"
captured: ["20040928044211"]
author: "sosmartthat...uh, well"
repliers: ["RPGuru", "xXPurgatoryXx"]
authors: ["sosmartthat...uh, well", "RPGuru", "xXPurgatoryXx"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_77127_amp_", captured: "20040928044211", sha256: "f5711f6db49a76a986efa9db6cacb95d81fe6d1be8c06f68b47569ac548a7b81", wayback_url: "https://web.archive.org/web/20040928044211/http://www.toolkitzone.com/forums/viewtopic.php?p=77127&amp="}
links:
  - {url: "http://www.zakap.com/", status: "external", local: null}
---

# changing character

### sosmartthat...uh, well · 2004-08-16 18:19 · #B76578

ok, i'm making a game. i need a program to change characters. something like this:
character a
do you wish to be a samurai (character b) or ninja (character c)
whatever the player chooses they become
i have the characters ready. just need to know how to switch them

### RPGuru · 2004-08-17 03:43 · #B76956

ok.. I think I know what you wont.. and how to do it.. just clarify me here.. are you talking about choosing at the begining of the game.. or being able to choose throughout the game to choose?
_________________
~`~'Guru'~`~
[Visit My Site! Zakap Enteprises](http://www.zakap.com/)

### xXPurgatoryXx · 2004-08-17 16:33 · #B77127

Set it up like this:

**Code:**

```
#MWin("Choose your character.")

#mwin(" 1- Become a Samurai.")

#mwin(" 2- Become a Ninja.")

#while(done!=0)

#done! = 0

#wait(a!)

#if(a! = 1)

{

     #MWincls()

     #newplyr("Samurai.tem")

     #Mwin("You are a Samurai!")

     #giveitm("SamuraiSword.itm")

     #system.pause()

     #done! = 1

}

#if(a! = 2)

{

     #MWincls()

     #newplyr("Ninja.tem")

     #Mwin("You are a Ninja!")

     #giveitm("NinjaSword.itm")

     #system.pause()

     #done! = 1

}
```

You might want to revise it a little, and maybe give them some stats based on what they chose.
_________________
It's a chance to strike back at the critical brotherhood and give each his comeuppance for evaluative sins of the past - Judith
