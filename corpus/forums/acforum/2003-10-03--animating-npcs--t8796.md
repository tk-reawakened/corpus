---
kind: forum-thread
id: "acforum/8796"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "8796"
title: "animating npcs"
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=8796"
written: "2003-10-03T23:18:00"
last_post: "2003-10-03T23:42:00"
date_confidence: "exact"
captured: ["20031027010925", "20031027011418", "20031027011534"]
author: "frogzilla"
repliers: ["chuckrpg"]
authors: ["frogzilla", "chuckrpg"]
posts_present: 3
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_8796", captured: "20031027011534", sha256: "8b2e15cd793d45976b9cf792672c7e2cc6ec097a8e51454576ca1af7b22a0d71", wayback_url: "https://web.archive.org/web/20031027011534/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=8796"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_8797", captured: "20031027010925", sha256: "2a247d730cc75f238f17d3394513febc2f2d3248cea9615e10fd83800e081a67", wayback_url: "https://web.archive.org/web/20031027010925/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=8797"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_8799", captured: "20031027011418", sha256: "11d8bd8d5ce5537b7fba62e82a971143eabf4511a7124c8b304c82fb31a368ed", wayback_url: "https://web.archive.org/web/20031027011418/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=8799"}
links: []
---

# animating npcs

### frogzilla · 2003-10-03 23:18 · #A1001-8796

Does anyone know how to get npcs to move around? Ive tried everything the help files say but am having no luck.

### chuckrpg · 2003-10-03 23:32 · #A1001-8797

**try this (more)**

go to edit item thentype in the name of the npc then check off th board driven box and the used by all charecters cricle make sure the sell and buy price is 0 because its not an item its an npc . then go to graphics and put in the tiles you want for your npc graphics
then save
then exit the edit items window and go open up main file editer then make the mulititasking speed at like 450ms then save that and exit
then aply that item onthe map.................
Whats this for???

### chuckrpg · 2003-10-03 23:42 · #A1001-8799

**and (more)**

If you want to make it move
Lol
Open the npc you made then edit board driven
Then under program to run when item is on board
Type wander.prg
And under program to run when item is picked up type in the name of a text program you made
Warning dont put wander.prg on program to run when item is picked up because
Itwill have the npc flying around you forever!!!!!!!!!!!!!!! It sux so dont even try it
Whats this for???
