---
kind: forum-thread
id: "toolkitzone-forums/27432"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Code"
skin: "phpbb2"
thread_id: "27432"
title: "Linking Boards and making an NPC Speak"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=27432"
written: "2006-02-15T03:27:00"
last_post: "2006-02-20T05:02:00"
date_confidence: "exact"
captured: ["20060304215848", "20060324113905"]
author: "Vancex"
repliers: ["Dont_Think_So", "leonheart"]
authors: ["Vancex", "Dont_Think_So", "leonheart"]
posts_present: 4
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_298337_amp_3Bsid_ba706b3b349665fd8b869bd57bdc2f0c", captured: "20060304215848", sha256: "ea02679a42e7c87dcb11aa14e25350443784406cfce460f9b94841bc66870f2a", wayback_url: "https://web.archive.org/web/20060304215848/http://www.toolkitzone.com/forums/viewtopic.php?p=298337&amp%3Bsid=ba706b3b349665fd8b869bd57bdc2f0c"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_300034_amp_3Bsid_d68bd6ae0d6c02b950ae92fbfd57a280", captured: "20060324113905", sha256: "e63d3167151e6a4f5dd72979a7f7cb8c5f1a189f29e2736edd339d8ea37a86a0", wayback_url: "https://web.archive.org/web/20060324113905/http://www.toolkitzone.com/forums/viewtopic.php?p=300034&amp%3Bsid=d68bd6ae0d6c02b950ae92fbfd57a280"}
links: []
---

# Linking Boards and making an NPC Speak

### Vancex · 2006-02-15 03:27 · #B298333

Linking Boards
How do I do so...?
Making an NPC Speak
Okay I know the code,

**Code:**

```
Mwin("Hey xxx want to do to xxx?")

Wait()

Mwincls()
```

However it freezes when I set the program on "When the Item is picked up" which I thought make him speak...

### Dont_Think_So · 2006-02-15 03:38 · #B298337

Linking Boards
There are two ways to do this; first, you can open up the board editor, go into its properties, and set a directional link, which sends the character to another board if they walk off the edge.. See the TK's manual for more information.
The other way is with warp tiles, which allow you to send the player to another board when they step on a tile. Again, see the manual for more information.
Making NPCs Speak
Don't set that code for when the item is picked up; instead, set the item on the board and choose the program for when it is activated (with a button or when it is walked in to).

### leonheart · 2006-02-18 02:08 · #B299331

every time i do this all way put to mch text and it disapears at the bottom of the window ... how can i make the window slighly bigger

### Dont_Think_So · 2006-02-20 05:02 · #B300034

Use wait() to wait for a keypress, then mwincls() to clear the mwin.
