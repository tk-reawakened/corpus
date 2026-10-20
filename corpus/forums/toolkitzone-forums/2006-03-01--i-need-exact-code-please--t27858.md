---
kind: forum-thread
id: "toolkitzone-forums/27858"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Code"
skin: "phpbb2"
thread_id: "27858"
title: "I need exact code please!"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=27858"
written: "2006-03-01T01:19:00"
last_post: "2006-03-03T04:03:00"
date_confidence: "exact"
captured: ["20060325140756"]
author: "DrJ"
repliers: ["p90m16mp5a4"]
authors: ["DrJ", "p90m16mp5a4"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_302974_amp_3Bsid_a3b82b25f3eceada8736100cf95dc6b0", captured: "20060325140756", sha256: "34bdaedd335101e102e00f9856908bb99aa78b33519215263c838be50acc4070", wayback_url: "https://web.archive.org/web/20060325140756/http://toolkitzone.com/forums/viewtopic.php?p=302974&amp%3Bsid=a3b82b25f3eceada8736100cf95dc6b0"}
links: []
---

# I need exact code please!

### DrJ · 2006-03-01 01:19 · #B302425

**Code:**

```
if(showsecond!<10)

{

text(30,1, "<showminute!> : 0<showsecond!>", cnvCanvas)

}

if(showsecond!>10)

{

text(30,1, "<showminute!> : <showsecond!>", cnvCanvas)

}
```

This is in a while loop and I want the text to update with out the screen flashing. How would I do that?

### p90m16mp5a4 · 2006-03-03 04:03 · #B302974

Sad Had a really good example of this on a CD somewhere..
Check out the command #RenderNow, it allows you to use a constant canvas who's id is CnvRenderNow! . Also, use a time checking method to only update every second, that way it will minimize flashing.

**Quote:**

> RenderNow("ON")
> while(0==0)
> {
> t! = gameTime! +1
> Text(1,1, "HIHIHIH <GAMETIME!>", CnvRenderNow!)
> while(gameTime! ~= t!)
> { //idle }
> Clear(CnvRenderNow!)
> }
>

I think that was the general idea of what I had written a while back.. Using CnvRenderNow! won't die when you use #Clear or exit the board, or go to a menu, or anything!! That's why CnvRenderNow! pwns regular canvases.
