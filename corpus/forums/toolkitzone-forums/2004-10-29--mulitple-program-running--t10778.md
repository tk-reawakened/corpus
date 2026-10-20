---
kind: forum-thread
id: "toolkitzone-forums/10778"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "editor help"
skin: "phpbb2"
thread_id: "10778"
title: "Mulitple Program Running...."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=10778"
written: "2004-10-29T06:20:00"
last_post: "2004-11-13T17:36:00"
date_confidence: "exact"
captured: ["20050110143053"]
author: "Caliber Mengsk"
repliers: ["Dont_Think_So", "Alex0Xander"]
authors: ["Caliber Mengsk", "Dont_Think_So", "Alex0Xander"]
posts_present: 7
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_124727_amp_", captured: "20050110143053", sha256: "d450b3fe361a193afa5e538d3c76d0e74dce5089c5e0e6786a10b0e367b292e2", wayback_url: "https://web.archive.org/web/20050110143053/http://www.toolkitzone.com/forums/viewtopic.php?p=124727&amp="}
links: []
---

# Mulitple Program Running....

### Caliber Mengsk · 2004-10-29 06:20 · #B118670

Is there a way to do it? I would suppose it would be under multitasking in truth, but I want to know if I can run two seaperate programs, or methods at the same time, with out reacting with eachother in the sense of controls, but are reacting with eachother in variables?
I am trying to do this for my custom BS, and if I can't, then the programing I did for the past hour is pretty much useless unless I want it to be only the charactor time based... which is pretty lame... Any help?

### Dont_Think_So · 2004-10-29 14:24 · #B118716

Well, you could fake multitasking (with while, etc), or you could use threads, though the player will be able to walk at the same time. A solution is to make all of the tiles around the player solid, then make them un-solid when the time allows.
Although, threads that run at the same time as other programs should be possible... perhaps a little hard to implement, though.

### Caliber Mengsk · 2004-10-30 02:21 · #B119001

Thanks. I haven't really tried threads... didn't know what they did, so I ignored them... still am not useing them. I just had to redo a bit of the math orders and math stuff in total.
^_^ So threads are something that runs constantly? Such as a health bar always on top?

### Dont_Think_So · 2004-10-31 05:27 · #B119465

Yup. Unless, that is, a program draws over it (threads don't run at the same time as programs, only other threads).

### Alex0Xander · 2004-11-12 20:09 · #B124366

**Dont_Think_So wrote:**

> Yup. Unless, that is, a program draws over it (threads don't run at the same time as programs, only other threads).
>

soo...if I were to run my BS, and use threaded monsters in it, the threads would not run ?

### Dont_Think_So · 2004-11-13 06:32 · #B124632

They would run, but only when no other programs (except other threads) are running.
For example, an NPC is walking around (and you decided to do this with threads). If you talk to him, the thread stops running and the program starts.

### Alex0Xander · 2004-11-13 17:36 · #B124727

**Dont_Think_So wrote:**

> They would run, but only when no other programs (except other threads) are running.
> For example, an NPC is walking around (and you decided to do this with threads). If you talk to him, the thread stops running and the program starts.
>

How about if the program to start when the item is activated is to tell the thread something? Like a method within the thread, would the thread execute it ?
