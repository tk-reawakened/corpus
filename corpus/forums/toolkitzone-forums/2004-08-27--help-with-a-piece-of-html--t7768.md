---
kind: forum-thread
id: "toolkitzone-forums/7768"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "web design"
skin: "phpbb2"
thread_id: "7768"
title: "Help with a piece of HTML"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=7768"
written: "2004-08-27T03:52:00"
last_post: "2004-08-28T06:05:00"
date_confidence: "exact"
captured: ["20050120115849"]
author: "Gnarf"
repliers: ["Colin", "Deathy", "Dark Paladin", "reignofmagic"]
authors: ["Gnarf", "Colin", "Deathy", "Dark Paladin", "reignofmagic"]
posts_present: 8
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_83366_amp_", captured: "20050120115849", sha256: "d2c4bf6aab78bf08fac95ad4f3a867e28deb4850196f7040ffad062eaa69b961", wayback_url: "https://web.archive.org/web/20050120115849/http://www.toolkitzone.com/forums/viewtopic.php?p=83366&amp="}
links:
  - {url: "http://www.w3schools.com", status: "external", local: null}
---

# Help with a piece of HTML

### Gnarf · 2004-08-27 03:52 · #B82580

How do I make it so that there is a text box that has whatever I put into scrolling across the box...
______________________________________
l......................................................................l
l..............Words scroll through here...............l
l____________________________________l
I just need to know that in HTML...thanks Wink

### Colin · 2004-08-27 03:58 · #B82583

Use the MARQUEE tag.

### Gnarf · 2004-08-27 04:12 · #B82596

THe Marquee tag?
I am not good with HTML, I just began learning it...sivart did most of the coding for TK_cafe, as seen in the sig...I just fixed up some pages and added some text in the first paragraph and some links and some pages but thats it...check out the site...be sure to read the news...its short...

### Deathy · 2004-08-27 07:47 · #B82670

Well:

**Code:**

```
<marquee>Im Scrollin...</marquee>
```

**Code:**

```
<marquee direction="right">No!, Im scrollin backwarrds!</marquee>
```

Basicly you have:
Direction
Delay
ScrollAmount
Behevior(scroll, Alternate, slide)
Loop
Well basicly:

**Code:**

```
<marquee behavior="alternate" direction="right" loop="3" scrollamount="2" scrolldelay="86">Im a Word</marquee>
```

### Gnarf · 2004-08-27 22:54 · #B83056

**deathsquad wrote:**

> Well:
>
> **Code:**
>
> ```
> <marquee>Im Scrollin...</marquee>
> ```
>
> **Code:**
>
> ```
> <marquee direction="right">No!, Im scrollin backwarrds!</marquee>
> ```
>
> Basicly you have:
> Direction
> Delay
> ScrollAmount
> Behevior(scroll, Alternate, slide)
> Loop
> Well basicly:
>
> **Code:**
>
> ```
> <marquee behavior="alternate" direction="right" loop="3" scrollamount="2" scrolldelay="86">Im a Word</marquee>
> ```
>

Sweet thanks deathsquad Wink

### Dark Paladin · 2004-08-27 23:00 · #B83060

I had fun with that tag. I'd do pictures of volcanoes with the background a volcano. My computer teacher didn't like that but I didn't care. I was learning wasn't I?

### Deathy · 2004-08-27 23:22 · #B83066

**Gnarf wrote:**

> Sweet thanks deathsquad Wink
>

No Problem....
And yeah man, I have yet to have a web page without at least 2 or 3 of them things.......It looks so tacky Razz

### reignofmagic · 2004-08-28 06:05 · #B83366

You should check some tutorials from <http://www.w3schools.com>. They have some basic and advanced HTML tutorial there.
