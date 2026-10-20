---
kind: forum-thread
id: "toolkitzone-forums/11272"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "advanced"
skin: "phpbb2"
thread_id: "11272"
title: "Get .sav file info??"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11272"
written: "2004-11-12T03:15:00"
last_post: "2004-11-13T23:40:00"
date_confidence: "exact"
captured: ["20050110143109"]
author: "reignofmagic"
repliers: ["Dont_Think_So", "Asimir", "catwhowalksbyhimself"]
authors: ["reignofmagic", "Dont_Think_So", "Asimir", "catwhowalksbyhimself"]
posts_present: 5
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_124907_amp_", captured: "20050110143109", sha256: "1263af7049112bef424be0f1841f5812002d5f7a247a1f04d4d7406be63c11c4", wayback_url: "https://web.archive.org/web/20050110143109/http://www.toolkitzone.com/forums/viewtopic.php?p=124907&amp="}
links: []
---

# Get .sav file info??

### reignofmagic · 2004-11-12 03:15 · #B124162

How do you get some information from a save file??
Examples:
#GetSavPlayers(savfilename$, returnvar!)
#GetSavPlayerName(savfilename$, playerhandle!, returnvar$)
#GetSavPlayerHP(savfilename$, playerhandle!, returnvar!)
#GetSavNum(savfilename$, varname!, returnvar!)
#GetSavStr(savfilename$, varname$, returnvar$)
Thanks!

### Dont_Think_So · 2004-11-12 06:04 · #B124200

Two ways:
Load(filename.gam)
...which could pose a problem...
and Use your own variation of the File I/O Commands. See Niloc's example.

### Asimir · 2004-11-13 00:11 · #B124488

Load(filename.gam) wipes all your variables and loads every variable from the save file. That's why it can cause problems, as DTS said.
It's great for making a regular 'load' option, but if you're trying something more specific (which it looks like you are) it'll be no use.

### reignofmagic · 2004-11-13 00:37 · #B124498

Can you try to add that code in the next release of TK3? It'll be grateful.
Smile
Thanks!

### catwhowalksbyhimself · 2004-11-13 23:40 · #B124907

Just use the IO commands to save the stats you need to a different file and load them again afterwards. Study the included IO methods to get an idea of how this would work.
