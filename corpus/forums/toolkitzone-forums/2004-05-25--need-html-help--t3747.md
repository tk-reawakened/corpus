---
kind: forum-thread
id: "toolkitzone-forums/3747"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "web design"
skin: "phpbb2"
thread_id: "3747"
title: "need html help!!"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=3747"
written: "2004-05-25T14:22:00"
last_post: "2004-08-22T10:44:00"
date_confidence: "exact"
captured: ["20050120115757"]
author: "Gangsta"
repliers: ["Occasionally_Correct", "nova11", "Colin", "Ersuis", "Gnarf", "Sander"]
authors: ["Gangsta", "Occasionally_Correct", "nova11", "Colin", "Ersuis", "Gnarf", "Sander"]
posts_present: 8
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_79577_amp_", captured: "20050120115757", sha256: "5af56dbd5c3218314eb56bb0c5a486b99fef8290946a91e6214fc1e931855742", wayback_url: "https://web.archive.org/web/20050120115757/http://www.toolkitzone.com/forums/viewtopic.php?p=79577&amp="}
links: []
---

# need html help!!

### Gangsta · 2004-05-25 14:22 · #B37834

I want one of them things down the left hand side of the page so you can get to other places in the site (a navigation?). And right now I can only think to use frames, so each page is actually two- the navigation takes up about 10% of the screen, while the rest is something else. personally, I think this is a waste of memory... theres got to be an easier way... help me! [color=red][/color]

### Gangsta · 2004-05-25 14:23 · #B37836

that color red thing was a mistake... ignore it...

### Occasionally_Correct · 2004-05-25 18:07 · #B37935

Simple... All you need to do is use tables.

**Code:**

```
<table cellspacing=0 cellpadding=0 border=0 width=100%>

<tr>

<td width=10%>

Put whatever you want in the navigation here...

</td>

<td width=80%>

Put the other contents of the site here.. It will appear to the right side of the navigation.

</td></tr></table>
```

Hope that helps.

### nova11 · 2004-08-19 00:54 · #B78054

Div Layers work extremly well, if you know how to use them. But, yea, tables will work fine.

### Colin · 2004-08-20 03:38 · #B78756

And so does CVS, DHTML, weird combinations of js and html, and about 59 million other things.
But simply put, tables are the best for that situation.

### Ersuis · 2004-08-22 03:35 · #B79336

Hardly the best... just a solution for that situation. In all fairness, though, absolute positioning a div somewhere on the page is just as crappy.
If it was a page I was working on, I'd set widths to the navigation and body layers and float them left using CSS. But, if I was doing it, the whole thing would be XHTML and CSS anyway.

### Gnarf · 2004-08-22 03:48 · #B79354

I thought there were somehtings called frames...those are helpful...but that means it would....nevermind, i dont know much about HTML

### Sander · 2004-08-22 10:44 · #B79577

Nah, don't use frames. They're evil.
