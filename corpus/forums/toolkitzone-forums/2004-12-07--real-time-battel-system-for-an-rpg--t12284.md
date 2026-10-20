---
kind: forum-thread
id: "toolkitzone-forums/12284"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "12284"
title: "real time battel system for an rpg"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12284"
written: "2004-12-07T18:46:00"
last_post: "2004-12-07T19:11:00"
date_confidence: "exact"
captured: ["20041227095843"]
author: "tsunai"
repliers: ["Levi"]
authors: ["tsunai", "Levi"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_136078_amp_", captured: "20041227095843", sha256: "22ada361d72af5ffc24689530bed849caf333b7d1cad203db27a5005817c408f", wayback_url: "https://web.archive.org/web/20041227095843/http://www.toolkitzone.com/forums/viewtopic.php?p=136078&amp="}
links: []
---

# real time battel system for an rpg

### tsunai · 2004-12-07 18:46 · #B136068

i need help with a real time battle system i confused on how to calculate collsion and such. And how do convert C++ to rpg code?????

### Levi · 2004-12-07 19:11 · #B136078

Ummm...what?
You can do a general conversion but not C++ itself to RPGCode. You can make a plugin that makes RPGCode commands. For that you'd use the C++ SDK available here. They are different depening on the version you're using.
For collision you could check the positions of the result of movement before movement happens. If enemy and player x and y are the same then collision happens. Send warning to user, or enter battle, or cause damage. Depending on what you want to do.
