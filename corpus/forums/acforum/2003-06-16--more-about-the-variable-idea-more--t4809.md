---
kind: forum-thread
id: "acforum/4809"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "4809"
title: "more about the variable idea (more)"
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=4809"
written: "2003-06-16T27:15:00"
last_post: "2003-06-16T27:15:00"
date_confidence: "exact"
captured: ["20030725040454"]
author: "game_king"
repliers: []
authors: ["game_king"]
posts_present: 1
pages_present: []
pages_total: null
posts_per_page: null
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: null, start: null, end: null, url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=4798", reason: "never-captured", note: "earlier post in this thread (msg 4798)"}
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_4809", captured: "20030725040454", sha256: "a52db57959d10a36e086f5cc91c94a76ed6d6def7582c13ad55473cca74bf5d2", wayback_url: "https://web.archive.org/web/20030725040454/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=4809"}
links: []
---

# more about the variable idea (more)

> [!missing] gap:earlier · http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=4798 · never-captured
> earlier post in this thread (msg 4798) was not recovered.

### game_king · 2003-06-16 27:15 · #A1001-4809

set the variables to whatever you want, but here is what you do. the variable for the level of your character will be charlvl$. Put what the effect is where it says *effect.
#if(charlvl$=="4")
{
*effect
}
#if(charlvl$~="4")
{
#end()
}
*that simple, took me a minute to think of it...
The Game King
