---
kind: forum-thread
id: "acforum/1492"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "1492"
title: "For the #Random..(more)"
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=1492"
written: "2001-12-14T25:03:00"
last_post: "2001-12-15T19:55:00"
date_confidence: "exact"
captured: ["20011231041243", "20011231042144", "20020101204226", "20020101204502"]
author: "MrG"
repliers: ["marco_lucifer"]
authors: ["MrG", "marco_lucifer"]
posts_present: 4
pages_present: []
pages_total: null
posts_per_page: null
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: null, start: null, end: null, url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=1490", reason: "never-captured", note: "earlier post in this thread (msg 1490)"}
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1002_mode_1_msg_1492", captured: "20011231041243", sha256: "262eae023e8f84dcee6e34212fb81c44cef61366f5caf03400b035851a74ae3c", wayback_url: "https://web.archive.org/web/20011231041243/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=1492"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1002_mode_1_msg_1495", captured: "20011231042144", sha256: "e328b32b55f556bf84ebab8f16f14c3f0e41ecbf56dd77edc71c6ef14ac572a6", wayback_url: "https://web.archive.org/web/20011231042144/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=1495"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1002_mode_1_msg_1503", captured: "20020101204226", sha256: "5bc72711258601c30f6e90c29b488fbca61f7defe9efa62ac95e956eb04e0329", wayback_url: "https://web.archive.org/web/20020101204226/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=1503"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1002_mode_1_msg_1504", captured: "20020101204502", sha256: "34c8f4894127f340d2738412cd90bb68bd2e5d0a6ac15b840263a7c61a94196a", wayback_url: "https://web.archive.org/web/20020101204502/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=1504"}
links:
  - {url: "http://www.rpgtoolkit.com/cgi-bin/<small", status: "never-captured", local: null}
---

# For the #Random..(more)

> [!missing] gap:earlier · http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=1490 · never-captured
> earlier post in this thread (msg 1490) was not recovered.

### MrG · 2001-12-14 25:03 · #A1002-1492

Fairly easy to do.. Say you want a range of 3 to 10, just do this:
#Random(10,dest!)
#dest!=dest!+2 *change the least possible from 1 to 3; i.e if it gave you a 1 it would be a 3
#If(dest!>10) *make sure you don't go over 10
{
#change!=dest!-10
#dest!=dest!-change!
}
A little bit of a pain, but it works.. :)
Mike

### marco_lucifer · 2001-12-15 14:41 · #A1002-1495

**Its easier like this (more)**

#Random(8,dest!)
#dest!=dest!+2 *change the least possible from 1 to 3; i.e if it gave you a 1 it would be a 3 and change the highest possible from 8 to 10
check out [<small](http://www.rpgtoolkit.com/cgi-bin/<small)

### MrG · 2001-12-15 16:27 · #A1002-1503

**Yes, good point..(more)**

I'm not great with the easiest way to do things. :P
Mike

### marco_lucifer · 2001-12-15 19:55 · #A1002-1504

**And with that way the numbers 8,9,10 all result in 10 so it favors a certain number, removing randomness </a> -nt-**

check out [<small](http://www.rpgtoolkit.com/cgi-bin/<small)
