---
kind: forum-thread
id: "toolkitzone-forums/23815"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "P90\\'s Coding forum Tuts&source"
skin: "phpbb2"
thread_id: "23815"
title: "directly to P90 or p09 w/e the fudge his name is.."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=23815"
written: "2005-09-25T23:50:00"
last_post: "2005-10-19T14:35:00"
date_confidence: "exact"
captured: ["20060111130604"]
author: "Z"
repliers: ["p90m16mp5a4", "Phalanxia"]
authors: ["Z", "p90m16mp5a4", "Phalanxia"]
posts_present: 6
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_260714_amp_3Bsid_f2c01a272b36fe85bb1c4aa1247f23ae", captured: "20060111130604", sha256: "db73118cb07fe7b5defe5f270a2b868d39f2662cf47a41dc1c25d6dc6bbfab9a", wayback_url: "https://web.archive.org/web/20060111130604/http://www.toolkitzone.com/forums/viewtopic.php?p=260714&amp%3Bsid=f2c01a272b36fe85bb1c4aa1247f23ae"}
links: []
---

# directly to P90 or p09 w/e the fudge his name is..

### Z · 2005-09-25 23:50 · #B260224

heh its a very long subject name but w/e
This post just died in the coding section so i'll repost because i can here
Ugh, I haven't coded in so long. Anyway i am trying to make a piano program but it doesn't seem to work. I can't see whats wrong but i know I sucked up the coding somewhere along the line.

**rpgcode:**

```
Include("custom mwin.prg")

talk("Khano", "pf.PNG", "Awsome a piano", "*Press 1 to Play*", "*Press 2 to walk away*")

wait(a$)

If(a$ == "1")

{

     talk("Khano", "pf.PNG", "Okay,lets play this thing!")

     delay(3)

     bitmap("piano.bmp")

     talk("Info", "info.PNG", "*Press any key between the letters A and G", "*Press X to Exit")

     wait(nt$)

     If(nt$ == "x")

     {

     }

     nt$ = nt$+".mid"

     Mediaplay(&lt;nt$&gt;)

     delay(1)

     mediarest()

}
```

### p90m16mp5a4 · 2005-09-26 06:20 · #B260272

I actually responded to that one. Basically, nothing inside of the blocks will run. Just in case you missed my previous post. It would help if you posted where lt and gt come in.
Mediaplay(&lt;nt$;&gt)
That doesn't tell me anything, because they are nowhere in your program.
Holding a note will be tricky, you will need to get the #KeyDown method by Colin. (I dont htink it in resources)

### Z · 2005-09-26 23:05 · #B260441

oops, how the hell did that get there, in the coding sec. i didn't get what you were saying, now i see... wait, in my actual code those are < and > maybe it would work if i left those out...... anyway i tryed to fix it but it still doesn't work

**Code:**

```
Include("custom mwin.prg")

talk("Khano", "pf.PNG", "Awsome a piano", "*Press 1 to Play*", "*Press 2 to walk away*")

wait(a$)

If(a$=="1")

{

   talk("Khano", "pf.PNG", "Okay,lets play this thing!")

   delay(3)

   bitmap("piano.bmp")

   talk("Info", "info.PNG","*Press any key between the letters A and G", "*Press X to Exit")

   wait(nt$)

      If(nt$="x")

      {

      }

   nt$=nt$+".mid"

   Mediaplay(nt$)

      delay(1)

      mediarest()

}
```

### p90m16mp5a4 · 2005-09-27 02:20 · #B260503

If it is really bugging you, just debug.. Try running the sound without all the options. You wont be able to hold a note unless you have a *really* long .wav file. Sound *is* the toolkits biggest weakness. However, if a few good mainstream programmers out there made decent plugins, it would be much easier. But, anybody serious enough to take sound seriously, wont usually use the Toolkit over a home made game engine.

### Z · 2005-09-28 01:43 · #B260714

**p90m16mp5a4 wrote:**

> You wont be able to hold a note unless you have a *really* long .wav file.
>

I don't really want to hold it, it just playes for a second...peice of shit *virtually kicks the toolkit*
anyway this is really getting on my nerves, i had a program almost exactly like this and it worked but it got lost, anyway maybe i'll take the long way, just like if(nt$="A") { ......
and so on.....as long as it works in the end

### Phalanxia · 2005-10-19 14:35 · #B265526

Has it worked yet?
