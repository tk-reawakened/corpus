---
kind: forum-thread
id: "toolkitzone-forums/24370"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Toolkit Discussion"
skin: "phpbb2"
thread_id: "24370"
title: "Uh...Will TK3.0.7 have a good debugger?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=24370"
written: "2005-10-17T21:11:00"
last_post: "2005-10-17T23:22:00"
date_confidence: "exact"
captured: ["20060112040204"]
author: "TKFanBoy"
repliers: ["Colin", "p90m16mp5a4"]
authors: ["TKFanBoy", "Colin", "p90m16mp5a4"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_265126_amp_3Bsid_676513d1a6980aeb9bf37b2b4364333e", captured: "20060112040204", sha256: "49ad900593254d33bbc8b60ab06a0a63d8aa64b707b61e67574ae17a03c47bac", wayback_url: "https://web.archive.org/web/20060112040204/http://www.toolkitzone.com/forums/viewtopic.php?p=265126&amp%3Bsid=676513d1a6980aeb9bf37b2b4364333e"}
links: []
---

# Uh...Will TK3.0.7 have a good debugger?

### TKFanBoy · 2005-10-17 21:11 · #B265071

One that shows which line has a bracket mismatch or something
Right now, I have a program with a couple methods like this

**Code:**

```
Method a()

{

For (Whatever)

{

}

Method b()

{

}
```

Just because I was missing a bracket, the program mysteriously ends
of course, my program was much longer than this, and without something telling me that there's a bracket missing, it took me almost an hour to find the problem, all that work just for a simple "}", come on, we gotta have a good debugger

### Colin · 2005-10-17 21:22 · #B265083

Of course, the best way to avoid the above problem is to intent your code. I have little pity for people who refuse to intent then demand a fix to their code. Additionally, the RPGCode editor has contained a tool that will intent your sloppy code for quite some time now.
I consider myself a reasonable person, however, and the 3.0.7 debugger issues the following message for the above code, which makes it quite easy to correct:
Near line 3: Unmatched curly brace.

### p90m16mp5a4 · 2005-10-17 23:22 · #B265126

Lol fanboy, an hour? At least you tried Smile
