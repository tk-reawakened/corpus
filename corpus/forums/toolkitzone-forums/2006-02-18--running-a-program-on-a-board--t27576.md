---
kind: forum-thread
id: "toolkitzone-forums/27576"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Toolkit Discussion"
skin: "phpbb2"
thread_id: "27576"
title: "running a program on a board"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=27576"
written: "2006-02-18T18:15:00"
last_post: "2006-02-18T20:11:00"
date_confidence: "exact"
captured: ["20060305160109"]
author: "Lisha"
repliers: ["Delano"]
authors: ["Lisha", "Delano"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_299580_amp_3Bsid_41a8f0424612fd95602078968b75364d", captured: "20060305160109", sha256: "2bc1baf104129433bf5bf27e813d1fa381a6f2705a2e50f903e65fea2fc778e1", wayback_url: "https://web.archive.org/web/20060305160109/http://toolkitzone.com/forums/viewtopic.php?p=299580&amp%3Bsid=41a8f0424612fd95602078968b75364d"}
links: []
---

# running a program on a board

### Lisha · 2006-02-18 18:15 · #B299520

I want to run a program right when a player enters the start board... but when I put my program in the "Run program on entering" box in the board editor, it plays to program BEFORE the player enters the board. When I set the program on the space the player starts out on, the player has to get off the space and get on it again before it will work. How on earth do you do this? It's getting frustrating.

### Delano · 2006-02-18 20:11 · #B299580

Try putting a ForceRedraw() at the top of the program...
