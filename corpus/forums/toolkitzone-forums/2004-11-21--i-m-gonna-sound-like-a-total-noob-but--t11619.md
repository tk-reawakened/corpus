---
kind: forum-thread
id: "toolkitzone-forums/11619"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "toolkit 2.x support"
skin: "phpbb2"
thread_id: "11619"
title: "I'm gonna sound like a total noob but"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11619"
written: "2004-11-21T21:37:00"
last_post: "2004-11-21T22:18:00"
date_confidence: "exact"
captured: ["20050111163119"]
author: "Da Almighty Wombat"
repliers: ["marcos"]
authors: ["Da Almighty Wombat", "marcos"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_128094_amp_", captured: "20050111163119", sha256: "a21fcd6ec6ff7adaf813cbac4992eb5f32398d2ad5473c003501e45ae5a58214", wayback_url: "https://web.archive.org/web/20050111163119/http://www.toolkitzone.com/forums/viewtopic.php?p=128094&amp="}
links: []
---

# I'm gonna sound like a total noob but

### Da Almighty Wombat · 2004-11-21 21:37 · #B128084

How do you make it so a special move doesn't inflict damage on the target? I set the Fight Power to 0 and it still just did 1 damage. x.x

### marcos · 2004-11-21 22:18 · #B128094

You could have this line in your RPGCode program used by the SM:

**Code:**

```
#giveHP("target",1)
```

Too bad it doesn't help much, the red "1" will still appear...
