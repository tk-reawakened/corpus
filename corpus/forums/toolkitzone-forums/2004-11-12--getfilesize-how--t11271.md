---
kind: forum-thread
id: "toolkitzone-forums/11271"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "advanced"
skin: "phpbb2"
thread_id: "11271"
title: "#GetFilesize(how???)"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11271"
written: "2004-11-12T02:46:00"
last_post: "2004-11-14T01:56:00"
date_confidence: "exact"
captured: ["20050110143113"]
author: "reignofmagic"
repliers: ["TheCPPFreak220"]
authors: ["reignofmagic", "TheCPPFreak220"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_124934_amp_", captured: "20050110143113", sha256: "4f01bceecaf12ba62eff6fb56bf3b16b4e3f0c87a5fe28da730a2b99e98a1231", wayback_url: "https://web.archive.org/web/20050110143113/http://www.toolkitzone.com/forums/viewtopic.php?p=124934&amp="}
links: []
---

# #GetFilesize(how???)

### reignofmagic · 2004-11-12 02:46 · #B124157

I hope there's a way to do this:
#GetFilesize(filename$)
I really need that!

### TheCPPFreak220 · 2004-11-14 01:56 · #B124934

I do not think this is implimented in the tk, but you could have a while loop read the entire file using #FileGet (assuming it only reads one character) and adding the number of times the loop ran together. This would get the number of characters in the file but would be very slow.
