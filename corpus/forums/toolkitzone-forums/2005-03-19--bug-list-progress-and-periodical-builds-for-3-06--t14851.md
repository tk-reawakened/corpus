---
kind: forum-thread
id: "toolkitzone-forums/14851"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "14851"
title: "Bug List/Progress, and Periodical Builds For 3.06"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=14851"
written: "2005-03-19T02:17:00"
last_post: "2005-03-21T21:53:00"
date_confidence: "exact"
captured: ["20050326002817"]
author: "AlienDude"
repliers: ["Eternal EoN", "Delano"]
authors: ["AlienDude", "Eternal EoN", "Delano"]
posts_present: 3
pages_present: [6]
pages_total: 6
posts_per_page: 15
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 1, start: 1, end: 15, url: "http://toolkitzone.com/forums/viewtopic.php?t=14851", reason: "never-captured"}
  - {page: 2, start: 16, end: 30, url: "http://toolkitzone.com/forums/viewtopic.php?t=14851&start=15", reason: "never-captured"}
  - {page: 3, start: 31, end: 45, url: "http://toolkitzone.com/forums/viewtopic.php?t=14851&start=30", reason: "never-captured"}
  - {page: 4, start: 46, end: 60, url: "http://toolkitzone.com/forums/viewtopic.php?t=14851&start=45", reason: "never-captured"}
  - {page: 5, start: 61, end: 75, url: "http://toolkitzone.com/forums/viewtopic.php?t=14851&start=60", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_182543_amp_", captured: "20050326002817", sha256: "d17b02683b10e9091242e0670dd1cc909df5a95c8bff6ce8f6c40a9b68d04268", wayback_url: "https://web.archive.org/web/20050326002817/http://toolkitzone.com/forums/viewtopic.php?p=182543&amp="}
links: []
---

# Bug List/Progress, and Periodical Builds For 3.06

> [!missing] gap:1-15 · http://toolkitzone.com/forums/viewtopic.php?t=14851 · never-captured
> Page 1 of 6 was not recovered.

> [!missing] gap:16-30 · http://toolkitzone.com/forums/viewtopic.php?t=14851&start=15 · never-captured
> Page 2 of 6 was not recovered.

> [!missing] gap:31-45 · http://toolkitzone.com/forums/viewtopic.php?t=14851&start=30 · never-captured
> Page 3 of 6 was not recovered.

> [!missing] gap:46-60 · http://toolkitzone.com/forums/viewtopic.php?t=14851&start=45 · never-captured
> Page 4 of 6 was not recovered.

> [!missing] gap:61-75 · http://toolkitzone.com/forums/viewtopic.php?t=14851&start=60 · never-captured
> Page 5 of 6 was not recovered.

### AlienDude · 2005-03-19 02:17 · #B182540

EDIT: I set the color depth to 16-bit, and the boards showed fine, but not the characters, also the double cursor move thingy is cool now too.

### Eternal EoN · 2005-03-19 02:26 · #B182543

Edit your posts, please...

### Delano · 2005-03-21 21:53 · #B183639

Sorry you've not received a reply in a while AlienDude, this topic gets overlooked.
Okay... so, the Windows 9x bug - in terms of drivers and controls, there are no other requirements other than DirectX 8+ and the controls supplied with the Toolkit; the problem is purely due to the GDI. We've tried a number of solutions without any success; it won't be fixed in 3.0.6.
One thing you could do is try turning down hardware acceleration in Display > Settings > Advanced properties. Might make it worse though!
