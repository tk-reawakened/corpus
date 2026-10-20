---
kind: forum-thread
id: "toolkitzone-forums/16231"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "16231"
title: "Logical Operators"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=16231"
written: "2005-03-10T22:18:00"
last_post: "2005-03-11T05:52:00"
date_confidence: "exact"
captured: ["20050325131943"]
author: "Tao-Kun"
repliers: ["Colin", "Occasionally_Correct", "Oyerth"]
authors: ["Tao-Kun", "Colin", "Occasionally_Correct", "Oyerth"]
posts_present: 11
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_178913_amp_", captured: "20050325131943", sha256: "66aa9ebe7a750a610cf350d9d5c5c1828de6597167dd8f3a77e66dfef07e7e28", wayback_url: "https://web.archive.org/web/20050325131943/http://toolkitzone.com/forums/viewtopic.php?p=178913&amp="}
links: []
---

# Logical Operators

### Tao-Kun · 2005-03-10 22:18 · #B178707

I was wondering if a few Operators would work with Toolkit
Example
if(pie! == A$ && B$)
if(chance_of_flirt! == 1 OR 2 OR 3 OR 4)
if(pie! ==! B$)
if(pie! == NOT B$)
Something like that.

### Colin · 2005-03-10 22:19 · #B178708

Indeed, we have the logical operator set:
&&, ||, !

### Tao-Kun · 2005-03-10 22:28 · #B178718

Would "OR" Work?

### Occasionally_Correct · 2005-03-10 22:41 · #B178734

AND/OR should work, yeah.

### Tao-Kun · 2005-03-10 22:58 · #B178748

Thanks ^^;;

### Tao-Kun · 2005-03-11 00:07 · #B178771

The "OR" Statement doesnt work for me, unless I am using it wrong >.<

**Code:**

```
if(chance_of_flirt! == 1 OR 2 OR 3 OR 4)

{

name("vKakurine")

text1("Umm..  This isn't the place for this..")

wait

erase

mwin("Flirt Unsuccessful")

wait

mwincls

KakurineFriendship!=KakurineFriendship!-20

kill(chance_of_flirt!)

branch(:menu)

}
```

### Colin · 2005-03-11 00:20 · #B178776

You are.

### Occasionally_Correct · 2005-03-11 00:24 · #B178780

It's condition or condition. Example:

**Code:**

```
a! = 2

if (a! == 2 or a! == 5)

{

    mwin("Either a! is 2, or 5.")

    wait()

}
```

You can also use ||.

### Oyerth · 2005-03-11 05:43 · #B178910

**Colin wrote:**

> You are.
>

Yay for informative posts! Rolling Eyes

### Colin · 2005-03-11 05:46 · #B178912

Considering even the presently (wholly outdated) help files detail the logical operators, and our friend here didn't even ask a question, replying, 'You are,' to the implied question of, 'Am I using the operators wrong?' seems completely sufficient.
Seeing as you are indeed Super Moderator Mike, you might want to reevaluate my decision, and contemplate deletion of the post, however. ;)

### Oyerth · 2005-03-11 05:52 · #B178913

Take it easy. I love it when you post, honest. Rolling Eyes
