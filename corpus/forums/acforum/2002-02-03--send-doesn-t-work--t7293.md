---
kind: forum-thread
id: "acforum/7293"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "7293"
title: "#Send doesn't work?!"
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=7293"
written: "2002-02-03T30:44:00"
last_post: "2002-02-04T13:37:00"
date_confidence: "exact"
captured: ["20020214083453", "20020214085356"]
author: "maxiking"
repliers: ["Xorlak"]
authors: ["maxiking", "Xorlak"]
posts_present: 2
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_7293", captured: "20020214085356", sha256: "b8fd30a46c972f3806754d99506c7162aacca2977daa8e6021c6f999dc04b7a0", wayback_url: "https://web.archive.org/web/20020214085356/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=7293"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_7297", captured: "20020214083453", sha256: "990529f4b79a636b1d3f1c97605b8089372b4bc94a0fada226794891a9508dfc", wayback_url: "https://web.archive.org/web/20020214083453/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=7297"}
links:
  - {url: "http://darkage.tkzone.net", status: "external", local: null}
---

# #Send doesn't work?!

### maxiking · 2002-02-03 30:44 · #A1001-7293

I have used the #Send command lots of times in my game and it has always worked except for this one time. I used the command but it was sending the character to the on the right board but to the wrong tile. Any ideas why?
Thanks
P.S.
The RPG code looks like this
#If(foughtboss!=2)
{
#send("bosskey1.brd" 4,8,1)
#end
}
#Mwin(I need to slash the tile with the picture of swords.")

### Xorlak · 2002-02-04 13:37 · #A1001-7297

**Here (more)**

#send("bosskey1.brd",4,8,1)
It looks like you forgot that first comma.
-Xorlak
[Dark Age :: Dark Age 2](http://darkage.tkzone.net)
