---
kind: forum-thread
id: "toolkitzone-forums/23047"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Code"
skin: "phpbb2"
thread_id: "23047"
title: "Code on same row"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=23047"
written: "2005-08-30T14:06:00"
last_post: "2005-08-31T06:14:00"
date_confidence: "exact"
captured: ["20051228050454", "20051228050525"]
author: "William"
repliers: ["tc"]
authors: ["William", "tc"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_252200_amp_3Bsid_3b697b9010639cacab5742d20899e491", captured: "20051228050454", sha256: "bb098ae44c76db81bfafe03d269416b4bdd51226a8530eb6b02c53981a550091", wayback_url: "https://web.archive.org/web/20051228050454/http://www.toolkitzone.com/forums/viewtopic.php?p=252200&amp%3Bsid=3b697b9010639cacab5742d20899e491"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_252489_amp_3Bsid_3b697b9010639cacab5742d20899e491", captured: "20051228050525", sha256: "3a25de667e8a8a413a64ac062c7568ba5a7b872b12f1cd06b3f93adf34f2422f", wayback_url: "https://web.archive.org/web/20051228050525/http://www.toolkitzone.com/forums/viewtopic.php?p=252489&amp%3Bsid=3b697b9010639cacab5742d20899e491"}
links: []
---

# Code on same row

### William · 2005-08-30 14:06 · #B252200

Does this work:

**Code:**

```
if (EnemyPositionX[slots!]! = EnemyPositionX[slot!]!){if (move!=3){EnemyPositionX[slot!]!=EnemyPositionX[slot!]!+32}}
```

Before it was:

**Code:**

```
if (EnemyPositionX[slots!]! = EnemyPositionX[slot!]!)

{

if (move!=3){EnemyPositionX[slot!]!=EnemyPositionX[slot!]!+32}

}
```

________________________________________________________
Does this work:

**Code:**

```
if (slot! <> slots!) //run code if slot doesn't equal to slots

{

}
```

### tc · 2005-08-31 06:14 · #B252489

try it out i will say, that is the only way to be sure
