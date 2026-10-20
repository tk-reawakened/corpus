---
kind: forum-thread
id: "toolkitzone-forum/35396"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "35396"
title: "concept of time"
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=35396"
written: "2007-02-28T04:27:00"
last_post: "2007-02-28T23:38:00"
date_confidence: "exact"
captured: ["20070305054350"]
author: "gta_fido"
repliers: ["xenxe"]
authors: ["gta_fido", "xenxe"]
posts_present: 2
pages_present: [2]
pages_total: 2
posts_per_page: 10
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 1, start: 1, end: 10, url: "http://toolkitzone.com/forum/viewtopic.php?t=35396", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_383297", captured: "20070305054350", sha256: "9b45c1fe78c06df06b9eca6e07b8961dc9f8fbea258c614c7d3bf38e4c5e828f", wayback_url: "https://web.archive.org/web/20070305054350/http://toolkitzone.com/forum/viewtopic.php?p=383297"}
links: []
---

# concept of time

> [!missing] gap:1-10 · http://toolkitzone.com/forum/viewtopic.php?t=35396 · never-captured
> Page 1 of 2 was not recovered.

### gta_fido · 2007-02-28 04:27 · #K383170

**Code:**

```
time()

method Time()

{

time! = gametime!

overalltime$ = "A.M."

hourtime! = CastInt(time!/3600)

mintime! = castint(time!/60) - 60*hourtime!

sectime! = time! - 60*mintime! - 3600*hourtime!

until (hourtime! <= 12)

{

hourtime! = hourtime! - 12

if (overalltime$ = "A.M.")

{

overalltime$ = "P.M."

}

elseif (overalltime$ = "P.M.")

overalltime$ = "A.M."

}

}

text(1,1,"<hourtime!>:<mintime!>:<sectime!> <overalltime$>")

delay(1)

clear()

time()

}
```

this code (the same one from earlier will tell you what time it is with the A.M. and P.M. included. try it out if you want. an example time would be 10:53:05 A.M.

**Code:**

```
time()

method Time()

{

time! = gametime!

hourtime! = CastInt(time!/3600)

mintime! = castint(time!/60) - 60*hourtime!

sectime! = time! - 60*mintime! - 3600*hourtime!

until (hourtime! <= 23)

{

hourtime! = hourtime! - 24

}

text(1,1,"<hourtime!>:<mintime!>:<sectime!> <overalltime$>")

delay(1)

clear()

time()

}
```

This code will use millitary time meaning it wont use the A.M. and P.M. and instead go up to 23:59:59 then reset back at 0:0:0 (midnight). This method of time keeping is similar to that of the Grand Theft Auto games. Using this method would also be alot easier to use for coding purposes.

### xenxe · 2007-02-28 23:38 · #K383297

thank you ill go play whith your new time code to see what i can do whith it
