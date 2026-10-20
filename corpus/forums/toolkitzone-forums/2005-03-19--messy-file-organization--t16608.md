---
kind: forum-thread
id: "toolkitzone-forums/16608"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "16608"
title: "Messy File Organization ..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=16608"
written: "2005-03-19T18:36:00"
last_post: "2005-03-19T18:39:00"
date_confidence: "exact"
captured: ["20050326002707"]
author: "RDemusX"
repliers: ["Colin"]
authors: ["RDemusX", "Colin"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_182732_amp_", captured: "20050326002707", sha256: "441242c6f3fb413cadc1c1375acf153cf786195e6b9da454c8fd89bab0314b4e", wayback_url: "https://web.archive.org/web/20050326002707/http://toolkitzone.com/forums/viewtopic.php?p=182732&amp="}
links: []
---

# Messy File Organization ...

### RDemusX · 2005-03-19 18:36 · #B182729

I wanted to know if there is a way ... (in a future release maybe) to make the organization of files better.
In my program folder , there are so many programs that it's really hard to keep up with all of them. What would be cool is if in RPG Code somehow we could access folders within our program and bitmap folders that hold the info and just point to the info ... maybe something like:
setimagetransparent(townpics/"town01.gif",x!,y!,w!,h!,r!,g!,b!)
^ ^ ^ ^
call command folder file rest of command
then instead of having all my image files in the bitmap folder and unorganized ... I could make a new folder within the bitmap folder named town pics and put all my town pics in there. Then just point to that folder and specific image with RPG Code.
That would really make everyting very organized.
RDX

### Colin · 2005-03-19 18:39 · #B182732

You can already.

**Code:**

```
bitmap("cool\reallyAwesome.png")
```

(location is bitmap\cool\)
It won't be packaged into any internal distribution methods, but it works.
