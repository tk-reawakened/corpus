---
kind: forum-thread
id: "toolkitzone-forums/12482"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12482"
title: "I've asked this question before but I think TK3 is different"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12482"
written: "2004-12-11T23:02:00"
last_post: "2004-12-11T23:32:00"
date_confidence: "exact"
captured: ["20041227215144"]
author: "Chamgorie Chanbear"
repliers: ["p90m16mp5a4"]
authors: ["Chamgorie Chanbear", "p90m16mp5a4"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_138193_amp_", captured: "20041227215144", sha256: "d4de64132508b264930f49cb79aca9ba0294b4a0b01387179bdbb30acaa47f00", wayback_url: "https://web.archive.org/web/20041227215144/http://www.toolkitzone.com/forums/viewtopic.php?p=138193&amp="}
links: []
---

# I've asked this question before but I think TK3 is different

### Chamgorie Chanbear · 2004-12-11 23:02 · #B138185

Long ago I asked if there was a way to make my character face south. I was told that I could achieve this by using the #Stance() command. This worked for me. However, I am now working with TK3 and I need to do the same thing. The problem here is that the #Stance() command works with the old character graphics editor from TK2. If it does work with TK3, I don't know how to use it. I need to make my character, Jose, turn to the right (east) and for another character, Misaki, turn left (west). Can anybody tell me how to accomplish this using RPG Toolkit v3.0.4?

### p90m16mp5a4 · 2004-12-11 23:32 · #B138193

Hey easiest way is to open up your animation editor, click on your directional facing animations for your character, and just make a new animation with only one frame. ( the direction) Then open your characters, click graphics, then click "ADD" to put a new 'stance' animation. count from top to bottom and whatever number your new animation is, thats the stance you make your character go in.

**Code:**

```
#stance(4, "cham chan")
```

your character will sit like that till ya move.
actually you dont even need to make a single frame... just put in your facing animations and it will not do the whole animation.
