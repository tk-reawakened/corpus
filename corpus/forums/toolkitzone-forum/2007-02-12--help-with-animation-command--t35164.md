---
kind: forum-thread
id: "toolkitzone-forum/35164"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "35164"
title: "Help With animation Command"
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=35164"
written: "2007-02-12T20:20:00"
last_post: "2007-02-14T22:07:00"
date_confidence: "exact"
captured: ["20070302170739"]
author: "Xioyn"
repliers: ["decker666", "yaim0310"]
authors: ["Xioyn", "decker666", "yaim0310"]
posts_present: 6
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_379306", captured: "20070302170739", sha256: "f6eb172ed73119a7481b94735d1ac99943292d6ce5ae2b6edbe9b1ba61b106d0", wayback_url: "https://web.archive.org/web/20070302170739/http://www.toolkitzone.com/forum/viewtopic.php?p=379306"}
links: []
---

# Help With animation Command

### Xioyn · 2007-02-12 20:20 · #K379279

**Code:**

```
hAnm! = animation("firery Explosion.anm",25,150)
```

Thats the code I got
I have 2 problems I get this when I run it Warning: Animation () only returns a value in a thread-- animation("fiery Explosion.anm",25,150) And The animation doesnt show up were its supposed to be I first tried Tiles then I tried Pixels but both are in the wrong spot unless I did my math wrong

### decker666 · 2007-02-12 21:31 · #K379300

what i think the error means is that, your trying to set a variable to something which isnt a variable, and that the only variables that can be pulled from it are file$ , X! and Y!

### Xioyn · 2007-02-12 22:06 · #K379306

So what would you suggest that I change?

### decker666 · 2007-02-12 22:15 · #K379311

what are you trying to do exactly? just put the anm up? i mean is there a reason for the variable?

### yaim0310 · 2007-02-12 22:42 · #K379323

just like the warning says, it only returns a value in a thread... so you can just use

**Code:**

```
animation("firery Explosion.anm",25,150)
```

without returning the value to hAnm! to get rid of those annoying warnings... and unless you give more info on where you want the animation i cant help there, cuz the animation showed up right at 25,150 for me...

### Xioyn · 2007-02-14 22:07 · #K379932

ok thanks I was using the example in the readme
Another Question were does it place the animation from like the top left hand side of it or the center or what?
And I want to place the Top Left corner of the Animation on tiles 11,4
