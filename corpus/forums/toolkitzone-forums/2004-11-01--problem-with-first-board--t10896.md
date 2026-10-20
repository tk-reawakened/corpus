---
kind: forum-thread
id: "toolkitzone-forums/10896"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "editor help"
skin: "phpbb2"
thread_id: "10896"
title: "Problem with first board"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=10896"
written: "2004-11-01T23:30:00"
last_post: "2004-11-02T23:35:00"
date_confidence: "exact"
captured: ["20050109194316"]
author: "bamMargera"
repliers: ["Dont_Think_So", "Delano"]
authors: ["bamMargera", "Dont_Think_So", "Delano"]
posts_present: 4
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_120558_amp_", captured: "20050109194316", sha256: "0b351ff12987d4fd006ecd0a9c24841a58f7a70f6583bf844ebe64810c521139", wayback_url: "https://web.archive.org/web/20050109194316/http://www.toolkitzone.com/forums/viewtopic.php?p=120558&amp="}
links: []
---

# Problem with first board

### bamMargera · 2004-11-01 23:30 · #B120112

On the first board i want to move my character up three spaces and then say something but my code is not working
#fontsize( Cool
#BREAK()
#PushItem(start.tem,"N,N,N")
MWin("Were am I?")
Delay(5)
Wait(a$)
Please Help me

### Dont_Think_So · 2004-11-02 00:21 · #B120130

Take out #BREAK.

### Delano · 2004-11-02 11:48 · #B120371

Also, you're using #PushItem when you're pushing a player (start.tem). Instead, use #Push to move a player.

**Code:**

```
Fontsize( 8 )

Push("N,N,N")

MWin("Were am I?")

Delay(5)

Wait()
```

Note that when using #PushItem, you need to use the item slot rather than its' name, i.e. #PushItem(0, "N,N,N") rather than #PushItem("man.itm", "N,N,N").

### Dont_Think_So · 2004-11-02 23:35 · #B120558

Also note that pushing a player causes the board to scroll.
