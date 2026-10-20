---
kind: forum-thread
id: "toolkitzone-forums/7279"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "7279"
title: "how do i get x,y coord of player/item?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=7279"
written: "2004-08-16T18:48:00"
last_post: "2004-08-16T23:33:00"
date_confidence: "exact"
captured: ["20040925162324"]
author: "vUnit321"
repliers: ["xXPurgatoryXx", "Occasionally_Correct", "Hellfire_Dragoon"]
authors: ["vUnit321", "xXPurgatoryXx", "Occasionally_Correct", "Hellfire_Dragoon"]
posts_present: 6
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_76765_amp_", captured: "20040925162324", sha256: "4b311640945eab794f4314f33a7716d9a531da2ec95f674e9da17b1b060247bc", wayback_url: "https://web.archive.org/web/20040925162324/http://www.toolkitzone.com/forums/viewtopic.php?p=76765&amp="}
links:
  - {url: "http://www.toolkitzone.com/games.php?game=482", status: "never-captured", local: null}
---

# how do i get x,y coord of player/item?

### vUnit321 · 2004-08-16 18:48 · #B76588

i want to know how to get a player's x, y position and an item's (or npc) position on a board. is there a way to get it cause i don't see any #GetX or #GetLocation or something like that in the RPGCode Reference.
_________________
[Initial D Midnight Showdown](http://www.toolkitzone.com/games.php?game=482)
- Overall 4%
- RPGCode 6%
- Storyline 1%
- Sprites/Gfx 7%
- Sounds/Music 5%
- Map/Board 2%

### xXPurgatoryXx · 2004-08-16 18:51 · #B76590

You can use #targetlocation, but just make sure if you use an item that it is the target instead of the main character.
_________________
It's a chance to strike back at the critical brotherhood and give each his comeuppance for evaluative sins of the past - Judith

### Occasionally_Correct · 2004-08-16 19:03 · #B76595

You can also use the playerx[index!]!/playery[index!]! reserved variables. Just replace index! with the slot number of the player (counting from 0 to 4).
_________________
:: it's better in the matinee, the dark of the matinee ::

### xXPurgatoryXx · 2004-08-16 19:05 · #B76596

Yeah, forget what I said.
_________________
It's a chance to strike back at the critical brotherhood and give each his comeuppance for evaluative sins of the past - Judith

### vUnit321 · 2004-08-16 19:45 · #B76610

here's what i have so far in my code.
this code should make the npc, walk towards the player.

**Code:**

```
   #ItemLocation(2, ix!, iy!, il!)

   #PathFind(ix!, ix!, playerX[0]!, playerY[0]!, d$)

   #PushItem(2, d$)
```

item 2 is the npc.
so far, its not walking. i'm using TK 3.0.2. It said that PushItem has been update and to use the form "N,N,W,W,........"
_________________
[Initial D Midnight Showdown](http://www.toolkitzone.com/games.php?game=482)
- Overall 4%
- RPGCode 6%
- Storyline 1%
- Sprites/Gfx 7%
- Sounds/Music 5%
- Map/Board 2%

### Hellfire_Dragoon · 2004-08-16 23:33 · #B76765

it means if say u want the player to Move Use N,S,E,W=North south east west.
_________________
It took god 7 days to make the world cause he was rendering with caustics and parralex mapping.
