---
kind: forum-thread
id: "toolkitzone-forums/11929"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "11929"
title: "Many would say &quot;You idiot&quot;"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11929"
written: "2004-11-29T21:31:00"
last_post: "2004-11-29T22:18:00"
date_confidence: "exact"
captured: ["20041226222854"]
author: "Levi"
repliers: ["Colin"]
authors: ["Levi", "Colin"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_131742_amp_", captured: "20041226222854", sha256: "fb2c5ec98795f64aa9bd143a57b44b115948e969c4ab7fdfc9b4f3ec31d19639", wayback_url: "https://web.archive.org/web/20041226222854/http://www.toolkitzone.com/forums/viewtopic.php?p=131742&amp="}
links: []
---

# Many would say &quot;You idiot&quot;

### Levi · 2004-11-29 21:31 · #B131704

But I think I have finally found a fix for the problem of coloring comments. Its like, duh dummy. How could I have missed it?
A comment is most always placed on a line by itself in RPGCode. That's how it was designed. If you place it on the same line as setting a variable equal to something it'll mess up and assume you are mulitplying. And oddly enough after a text vairable it just adds the comment to the regular text.
After a command like #show() its no problem. You just need to add some extra conditional statements to look for such things. Easy.
Yeah, you just have to know how TK looks at it to know how to color it. Now If only I could properly get coloring down.

### Colin · 2004-11-29 22:16 · #B131740

// can be placed not on its own line. I plan to add /* and */ too. Have fun! Smile

### Levi · 2004-11-29 22:18 · #B131742

Oh yeah I know some big edits to the language are being made and planned for the newer ones. But I have an odd thing where until TK moves to 4.x then I'm sticking with 2.2. Though anything I make will be obsolete by the time I do get arond to it. Smile
