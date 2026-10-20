---
kind: forum-thread
id: "toolkitzone-forums/12470"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12470"
title: "Help with &quot;Triggers&quot;"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12470"
written: "2004-12-11T20:35:00"
last_post: "2004-12-11T22:27:00"
date_confidence: "exact"
captured: ["20041227215326"]
author: "st_jimmy"
repliers: ["Bad Kids", "p90m16mp5a4"]
authors: ["st_jimmy", "Bad Kids", "p90m16mp5a4"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_138170_amp_", captured: "20041227215326", sha256: "a2987633ad818572af496eb9abcc69c7c10fc37cfc71920fe82d486c4843457d", wayback_url: "https://web.archive.org/web/20041227215326/http://www.toolkitzone.com/forums/viewtopic.php?p=138170&amp="}
links: []
---

# Help with &quot;Triggers&quot;

### st_jimmy · 2004-12-11 20:35 · #B138098

I'm new to the toolkit and I know the basics of RPG code such as message windows, adding players, warp points and such...but I got no idea how to put these things in order. (Kind of like triggers)
I want to have someone say something, but then after talking to someone else, the first persons speech changes. Or I want to do something like a warp point can't be opened until my character talks to someone...stuff like that. (Could help with putting locks on doors, or fighting a certain boss at a certain time)
I got no idea how to do this and I would greatly appreciate it if someone explained how.

### Bad Kids · 2004-12-11 21:11 · #B138112

theses are varaiables. In the first person prg put a var. like this;

**Code:**

```
Man! = 0
```

at the top
after the chat put something like:

**Code:**

```
Man! = 1
```

for the other guy put

**Code:**

```
If(man! = 1)

{

//whatever here

Man! = 2

}
```

### p90m16mp5a4 · 2004-12-11 22:27 · #B138170

Sure I'll help ya, no prob!

**Code:**

```
*St jimmy talks to a NPC in his board

#MWin("ST_jimmy: Hi, what is your name?")

#Wait()

#MWin("person on board: My name is bad kid, nice to meet you!")

#Wait()

*Now, you want for a door to open after you talk to bad kid, and for him to *say something different for as many different times as you want

*so in this code add at the top:

#if(talked!~=0) *if you talked to him any number of times other than 0 run this block of code:

{

#KeyNPC!==1

*add as many talking lines as you want using a new IF statement for each one!

}

#else() *other wise if you talked to him 0 times run this block!

{

 #MWin("ST_jimmy: Hi, what is your name?")

#Wait()

#MWin("person on board: My name is bad kid, nice to meet you!")

#Wait()

#Talked!=1

#keyNPC!==1

}
```

This is the most unconfusing way of writing it, if you want me to write a program with alot phrases let me know ^^
