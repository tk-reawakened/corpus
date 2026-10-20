---
kind: forum-thread
id: "toolkitzone-forums/11317"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "advanced"
skin: "phpbb2"
thread_id: "11317"
title: "Threaded monsters"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11317"
written: "2004-11-13T17:47:00"
last_post: "2004-11-13T18:52:00"
date_confidence: "exact"
captured: ["20050110143101"]
author: "Alex0Xander"
repliers: ["Dont_Think_So"]
authors: ["Alex0Xander", "Dont_Think_So"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_124755_amp_", captured: "20050110143101", sha256: "fbc9990ce5c3ed4ebbeeb1c4bc9ac30746e8a004afa09d1449fa502a7ee18a1a", wayback_url: "https://web.archive.org/web/20050110143101/http://www.toolkitzone.com/forums/viewtopic.php?p=124755&amp="}
links: []
---

# Threaded monsters

### Alex0Xander · 2004-11-13 17:47 · #B124729

I'm doing everything custom, including stats. Threads run with other threads when the player is walking around. When a program starts up, the thread stops. DTS pointed out an example. Say I chose to run Threaded NPC's. If I talked to one of them, the thread would stop running and the program assigned to that NPC would run. Question. Would all the threads stop running ? Next question. Say I ran threaded monsters in my BS, would the threads run even though the program is on progress ? for example:

**Code:**

```
**monsa$ being a variable declared outside battle, which would be some*

*like; monsa$ = "Griever.prg"

**Battle system mock up**

mons1! = Thread(monsa$,0)

mons2! = thread(monsb$,0)

charac1! = thread(player1$,0)

charac2! = thread(player2$,0)

Menu()

method Menu()

{

**blah**

}

*and so on*
```

Question

### Dont_Think_So · 2004-11-13 18:52 · #B124755

Running any program would stop all the threads, although they will resume where they left off when the program ends.
One solution would be to make a thread that controlled your menu, then use the Get() command in a loop (be sure to set the last parameter to 1 or else you will experience huge slowdowns!). I don't know how quickly this will work, however.
Just another reason to add events to RPGCode... (OnButton(Menu_Key$, Method$),...
