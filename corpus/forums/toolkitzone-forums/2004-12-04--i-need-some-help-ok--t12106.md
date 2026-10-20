---
kind: forum-thread
id: "toolkitzone-forums/12106"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "toolkit 2.x support"
skin: "phpbb2"
thread_id: "12106"
title: "i need some help ok?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12106"
written: "2004-12-04T05:02:00"
last_post: "2004-12-04T06:19:00"
date_confidence: "exact"
captured: ["20050114191957"]
author: "CRAZY MAN"
repliers: ["Brad", "zyrshnikashnu"]
authors: ["CRAZY MAN", "Brad", "zyrshnikashnu"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_134469_amp_", captured: "20050114191957", sha256: "682805c8668aefdaf4bd36df07fb9cbb38f11231f2ec515c98d1f0fedb0ec717", wayback_url: "https://web.archive.org/web/20050114191957/http://www.toolkitzone.com/forums/viewtopic.php?p=134469&amp="}
links: []
---

# i need some help ok?

### CRAZY MAN · 2004-12-04 05:02 · #B134429

how would you make iot so if you would runa program , and at the end of a program you would leanr a new magic? Like if at the end iof a prgrsm liek this:
#mwin(" You have learn water magic!")
#wait(@$)
----------------(then righ there a method to leanr water magci?)

### Brad · 2004-12-04 05:05 · #B134433

Use variables.

### zyrshnikashnu · 2004-12-04 06:19 · #B134469

You're a big help...
In the character editor, go to special moves. Add the water magic move to the list, then edit it (there's a button for doing so). Set the requirements iinsanely high, then under the variable section, write in a nmerical variable, like watermagic!. Then have the condition require it to be set equal to 1. Now go to your program and add watermagic!=1 to it.
