---
kind: forum-thread
id: "toolkitzone-forums/23779"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Toolkit Discussion"
skin: "phpbb2"
thread_id: "23779"
title: "How do I make plugins?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=23779"
written: "2005-09-24T14:10:00"
last_post: "2005-10-22T02:51:00"
date_confidence: "exact"
captured: ["20060112040048"]
author: "corim123"
repliers: ["Shapechanger", "Z", "ddl2829", "Hamster", "drcrazy4", "Mr Picso"]
authors: ["corim123", "Shapechanger", "Z", "ddl2829", "Hamster", "drcrazy4", "Mr Picso"]
posts_present: 9
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_264990_amp_3Bsid_676513d1a6980aeb9bf37b2b4364333e", captured: "20060112040048", sha256: "009a0b6907ed174bd35769566592ff31ffbd00ddaa4dd4ec572c29bea1a6260e", wayback_url: "https://web.archive.org/web/20060112040048/http://www.toolkitzone.com/forums/viewtopic.php?p=264990&amp%3Bsid=676513d1a6980aeb9bf37b2b4364333e"}
links: []
---

# How do I make plugins?

### corim123 · 2005-09-24 14:10 · #B259932

As said in the topic COLIN,DELANO please help!
I need to make a plugin that won't allow the game to run after the time expires, so you get to play for an preset amount of time, and then the program will refuse to run after that time period has expired. Colin siad, I would need a plugin, but how do I create a plugin to do this task?

### Shapechanger · 2005-09-24 14:24 · #B259937

A demo timer, eh?

### Z · 2005-09-24 14:29 · #B259940

Create a plugin with C++ or VB

### corim123 · 2005-09-24 19:03 · #B259972

Its just, that I'm not that good at C++ or VB. I'll find a way. And yes, it is a demo timer

### ddl2829 · 2005-10-08 18:52 · #B263347

how about this, there is a plugin creator in the tk downloads section. make one with it. then if it uses rpg code do this:

**Code:**

```
if(gametime!>=2500) *or another number for time limit

{

windows() *or whatever command it is that ends the game

}
```

i have NEVER used the plugin creator tho, so dont yell at me if this dont work.

### Hamster · 2005-10-08 20:54 · #B263364

why the heck would you want to make a demo timer????
your not actually gonna sell your game, are you?

### corim123 · 2005-10-17 12:27 · #B264990

Maybe sell or just to make members join to get acess to the game ect. and it just seems as if it would help other people too.

### drcrazy4 · 2005-10-21 21:12 · #B265911

selling isn't a bad idea. i am considering it but I have played the Dark AgE 2 demo and i am trying to figure out if i can add 10 hours of gameplay for my game. want to sell your game then make it worth playing because people dont like wasting money.

### Mr Picso · 2005-10-22 02:51 · #B265955

**Code:**

```
While (true)

{

if (gametime! > 50)

{

Mwin("This concludes the duration of the demo. Thanks for playing.")

wait()

Windows()

}

}
```

Make this a thread and put it in the first board.
Here's the thread program.

**Code:**

```
timer! = Thread("timer.prg", 1)
```
