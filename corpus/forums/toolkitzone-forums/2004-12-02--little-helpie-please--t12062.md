---
kind: forum-thread
id: "toolkitzone-forums/12062"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "toolkit 2.x support"
skin: "phpbb2"
thread_id: "12062"
title: "Little Helpie Please?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12062"
written: "2004-12-02T22:58:00"
last_post: "2004-12-02T23:49:00"
date_confidence: "exact"
captured: ["20050114191634"]
author: "Brad"
repliers: ["Dont_Think_So"]
authors: ["Brad", "Dont_Think_So"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_133859_amp_", captured: "20050114191634", sha256: "6439c3e10dbda1d7da50fbccfb5707e0ddd9bc90101b05a6daa01e5c1452d610", wayback_url: "https://web.archive.org/web/20050114191634/http://www.toolkitzone.com/forums/viewtopic.php?p=133859&amp="}
links: []
---

# Little Helpie Please?

### Brad · 2004-12-02 22:58 · #B133823

Why won't this code work?

**rpgcode:**

```
{

     done! = 1

     while(done! == 1)

     {

          itemcount("key", key!)

          if(key! &lt;= 0)

          {

               mwin("The door is locked.")

               wait(a$)

               mwincls()

               done! = 2

          }

          if(key! &gt;= 1)

          {

               mwin("You use the key to open the door.")

               wait(a$)

               mwincls()

               kill(key!)

               Send("ship4.brd", 4, 9, 1)
```

Anybody tell me why? It keeps looping.

### Dont_Think_So · 2004-12-02 23:37 · #B133850

You're missing quite a few closing brackets there...
Also, be sure to put done!=2 within the last If.

### Brad · 2004-12-02 23:49 · #B133859

Okey Dokey fixed it.
