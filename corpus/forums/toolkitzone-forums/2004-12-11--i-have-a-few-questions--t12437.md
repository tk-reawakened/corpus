---
kind: forum-thread
id: "toolkitzone-forums/12437"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12437"
title: "i have a few questions"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12437"
written: "2004-12-11T03:34:00"
last_post: "2004-12-11T04:13:00"
date_confidence: "exact"
captured: ["20041227215158"]
author: "guest 2"
repliers: ["p90m16mp5a4"]
authors: ["guest 2", "p90m16mp5a4"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_137868_amp_", captured: "20041227215158", sha256: "29f64fa21e59bf01806f18f60b5c7b4a69ebd537b432d9ae171f1a03d5e8c256", wayback_url: "https://web.archive.org/web/20041227215158/http://www.toolkitzone.com/forums/viewtopic.php?p=137868&amp="}
links: []
---

# i have a few questions

### guest 2 · 2004-12-11 03:34 · #B137851

1. this may seem easy but i just want to make sure im doin this right will this work?

**Code:**

```
#GetHP(ene18!, oldhp!)

#HP(ene18!, oldhp! - Atkpr!)
```

*Atkpr! represents the attack power of the player, ene18! represents the enemy and oldhp! pretty much explains it self im making my own battle system so i wanted to know if the oldhp! - Atkpr! section will work
also
2. how do i delete a single button made using #SetButton? because #ClearButtons clears all the buttons using #SetButton.

### p90m16mp5a4 · 2004-12-11 04:02 · #B137863

Nope.. yer question #1 wont work under any circumstances, your variables are wrong. hang on a sec and I'll give ya some working code for when ya in a battle.

### p90m16mp5a4 · 2004-12-11 04:13 · #B137868

#GetHP(ene18$, oldHP!)
#oldHP!=oldHP!-atkpr!
#HP(ene18$, oldHP!)
I have not tested this in game, if it doesn't help you then I'll test it and re-write it.
Both of your commands require the the argument "handle$" wich is a LITERAL value, meaning $ this sign. Versus the NUMERICAL variable indicator, ! sign. Numerical values can only hold numbers, and literal variables can hold 'strings' of text
