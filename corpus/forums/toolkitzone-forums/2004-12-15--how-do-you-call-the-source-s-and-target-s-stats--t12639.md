---
kind: forum-thread
id: "toolkitzone-forums/12639"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12639"
title: "How do you call the source's and target's stats?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12639"
written: "2004-12-15T01:44:00"
last_post: "2004-12-15T22:48:00"
date_confidence: "exact"
captured: ["20041228072444"]
author: "Megiddo"
repliers: ["Metallic Ego"]
authors: ["Megiddo", "Metallic Ego"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_139815_amp_", captured: "20041228072444", sha256: "5069cf15fd7075668cae41105601a52a559c7857acc4ce52d32dbeb6f4a58e4c", wayback_url: "https://web.archive.org/web/20041228072444/http://www.toolkitzone.com/forums/viewtopic.php?p=139815&amp="}
links: []
---

# How do you call the source's and target's stats?

### Megiddo · 2004-12-15 01:44 · #B139815

Within the RPGcode programs for special moves, I want to call the source's fighting power and the target's defense power so that I can calculate damage. How do you call the source's fighting power and the target's defense power in this context?

### Metallic Ego · 2004-12-15 22:48 · #B140267

To get Defense Power of Target
targetdp! = GetDP("Target")
To get Fight Power of Source
sourcefp! = GetFP("Source")
Then you would just need to calculate the damage using the variables targetdp! and sourcefp!. Someone correct me if I'm wrong...
