---
kind: forum-thread
id: "acforum/4768"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "4768"
title: "another question"
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=4768"
written: "2003-06-16T15:36:00"
last_post: "2003-06-16T18:04:00"
date_confidence: "exact"
captured: ["20030721011911", "20030721012715"]
author: "squirelman1"
repliers: ["gildedlink"]
authors: ["squirelman1", "gildedlink"]
posts_present: 2
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_4768", captured: "20030721011911", sha256: "4303c86aa2cf51d0a0f483379e0a71f7cfac81d5dd2d303ce93f4b7236c14899", wayback_url: "https://web.archive.org/web/20030721011911/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=4768"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_4781", captured: "20030721012715", sha256: "2cfe6162079b3e9c0efd40c25f35a5b75fb12e6b833ca88a5fdaba4e1565dbda", wayback_url: "https://web.archive.org/web/20030721012715/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=4781"}
links: []
---

# another question

### squirelman1 · 2003-06-16 15:36 · #A1001-4768

Where would i put the #attackall command to make a special move attack all enemies. I can't figure it out.
-Weasle-

### gildedlink · 2003-06-16 18:04 · #A1001-4781

**No subject**

Maybe something like this?
#Mouseclick (x!,y!)
#Checkbutton (x!,y!)
#if(opt=1){#AttackAll}
