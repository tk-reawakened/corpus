---
kind: forum-thread
id: "toolkitzone-forums/24597"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Legacy Support"
skin: "phpbb2"
thread_id: "24597"
title: "urgh, how do I make this?..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=24597"
written: "2005-10-28T03:38:00"
last_post: "2005-12-05T04:45:00"
date_confidence: "exact"
captured: ["20060319120322", "20060321154147", "20060321155936"]
author: "eternal gladiator"
repliers: ["jkfd"]
authors: ["eternal gladiator", "jkfd"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_267008_amp_3Bsid_7244b862ae3fd639d6518f5107d4d792", captured: "20060319120322", sha256: "f44786907a0e8e52c893f765705e65723841f65b88fc7d9fde4ddad77afdc6a0", wayback_url: "https://web.archive.org/web/20060319120322/http://toolkitzone.com/forums/viewtopic.php?p=267008&amp%3Bsid=7244b862ae3fd639d6518f5107d4d792"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_276824", captured: "20060321154147", sha256: "e4af52cab65e09a2d64f87dcf0aa1810191e29cbc306547ebe36b82510190307", wayback_url: "https://web.archive.org/web/20060321154147/http://toolkitzone.com/forums/viewtopic.php?p=276824"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_276824_amp_3Bsid_06e0f790333e23d2463ff11405c7f78a", captured: "20060321155936", sha256: "eda3e193919d23c96656e495003ee61f56c7f32f5b4ef770e6846cd2214fe80b", wayback_url: "https://web.archive.org/web/20060321155936/http://toolkitzone.com/forums/viewtopic.php?p=276824&amp%3Bsid=06e0f790333e23d2463ff11405c7f78a"}
links: []
---

# urgh, how do I make this?...

### eternal gladiator · 2005-10-28 03:38 · #B267008

a program that runs dependant on if you have a certain item so if you say have the item inspiration you can move forward but if you don't you have to go find it

### jkfd · 2005-12-05 04:45 · #B276824

When you get the item, make it so that havetheitem$=yes, and when you lose the item, havetheitem$=no.
Then:

**Code:**

```
If(havetheitem$=yes)

{

  Run(Continue.prg)

}

If(havetheitem($=no)

{

  Run(Goaway.prg)

}
```
