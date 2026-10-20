---
kind: forum-thread
id: "toolkitzone-forums/16185"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "16185"
title: "If/ElseIf/Else Still broke in new build"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=16185"
written: "2005-03-09T15:13:00"
last_post: "2005-03-09T22:36:00"
date_confidence: "exact"
captured: ["20050325132009"]
author: "Dragonmaster"
repliers: ["Colin"]
authors: ["Dragonmaster", "Colin"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_178277_amp_", captured: "20050325132009", sha256: "af949b5e8a7b2d2dbcc6360175d889405fd183ac35ff94705962b54e70da663e", wayback_url: "https://web.archive.org/web/20050325132009/http://toolkitzone.com/forums/viewtopic.php?p=178277&amp="}
links: []
---

# If/ElseIf/Else Still broke in new build

### Dragonmaster · 2005-03-09 15:13 · #B178178

simple program

**Code:**

```
thenumber! = 4

if(thenumber! < 4)

{

  Mwin("< 4")

}

elseif(thenumber! == 3)

{

  Mwin("3")

}

else

{

  Mwin("neither")

  if(thenumber! == 4)

  {

  Mwin("4")

  }

  elseif(thenumber! >4)

  {

   Mwin("> 4")

  }

  else

  {

   Mwin("neither 2")

  }

}
```

I get the result:
neither
4
neither 2
neither 2 should have never displayed, which possibly means that it evaluates the elseif even after the adjoining if has passed true. Just letting you know.

### Colin · 2005-03-09 22:36 · #B178277

At least it's less broken. ;)
Fixed now.
