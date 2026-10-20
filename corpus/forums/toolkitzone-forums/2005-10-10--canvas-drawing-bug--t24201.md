---
kind: forum-thread
id: "toolkitzone-forums/24201"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Toolkit Discussion"
skin: "phpbb2"
thread_id: "24201"
title: "Canvas drawing bug"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=24201"
written: "2005-10-10T03:00:00"
last_post: "2005-10-10T04:09:00"
date_confidence: "exact"
captured: ["20060112035727"]
author: "OBCT"
repliers: ["Colin"]
authors: ["OBCT", "Colin"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_263684_amp_3Bsid_676513d1a6980aeb9bf37b2b4364333e", captured: "20060112035727", sha256: "38df8d2d0c933bdaf0d15ec1df6774bed4efe60aaf6c642250ad930d21da248f", wayback_url: "https://web.archive.org/web/20060112035727/http://www.toolkitzone.com/forums/viewtopic.php?p=263684&amp%3Bsid=676513d1a6980aeb9bf37b2b4364333e"}
links: []
---

# Canvas drawing bug

### OBCT · 2005-10-10 03:00 · #B263672

Greg and I found this bug. I know it's stupid and only morons do this, but it's still a bug. Razz

**Code:**

```
cnvMain! = createCanvas(640, 480)

drawCanvas(cnvMain!, 0, 0, 0, 0, cnvInvis!)
```

**Code:**

```
cnvMain! = createCanvas(640, 480)

drawCanvasTransparent(cnvMain!, 0, 0, 255, 0, 255, 0, 0, cnvInvis!)
```

In each case, trans3 causes a fatal error and is forced to close, because the program tried to draw a canvas of zero height and/or width. It'd be nice if the debugger popped up and told the user what was the problem. Greg was flipping out. Razz

### Colin · 2005-10-10 04:09 · #B263684

It's not a bug and it won't be 'fixed'. The more checks we add, the slower everyone's code runs. If your code sucks, you should be the one who pays the price, not all users.
Incidentally, 3.0.7 has a catch (...) clause which should catch all errors not covered normally, so this will not crash the program in 3.0.7, and it will even report the approximate line.
