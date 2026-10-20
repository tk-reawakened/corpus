---
kind: forum-thread
id: "acforum/3938"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "3938"
title: "I downloaded this code from TK Zone and..."
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=3938"
written: "2001-12-15T14:23:00"
last_post: "2001-12-15T14:23:00"
date_confidence: "exact"
captured: ["20011230140818"]
author: "Me"
repliers: []
authors: ["Me"]
posts_present: 1
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_3938", captured: "20011230140818", sha256: "ea7e135aa44af9abfad9da9de1f148bd38f5952a0761148b1fd4e8c773aa996d", wayback_url: "https://web.archive.org/web/20011230140818/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=3938"}
links: []
---

# I downloaded this code from TK Zone and...

### Me · 2001-12-15 14:23 · #A1001-3938

...How do I get it to appear on the screen? I know it displays a HP SMP bar but I don't know if it appears on the regular screen or what?
#Method HPbar(HPorSMP!, X!, Y!, endY!, Max!, Value!)
{
#If (HPorSMP!==1)
{
#Barlength!=Max!+X!
#HPLength!=Value!+X!
#BarColor!=BarLength!/4
#If (BarColor!>Value!)
{
#ColorRGB(255,0,0)
#Branch(:draw)
}
#BarColor!=BarColor!+BarLength!/2
#If (BarColor!>Value!)
{
#ColorRGB(255,255,0)
#Branch(:draw)
}
#ColorRGB(0,255,0)
:draw
#FillRect(X!, Y!, HPLength!, endY!)
#ColorRGB(0,0,0)
#DrawRect(X!, Y!, BarLength!, endY!)
#Kill(Value!)
#Kill(X!)
#Kill(Y!)
#Kill(endY!)
#Kill(Max!)
#Kill(BarLength!)
#Kill(BarColor!)
#Kill(HPorSMP!)
}
#If (HPorSMP!==2)
{
#Barlength!=Max!+X!
#SMPLength!=Value!+X!
#ColorRGB(0,0,255)
#FillRect(X!, Y!, SMPLength!, endY!)
#ColorRGB(0,0,0)
#DrawRect(X!, Y!, BarLength!, endY!)
#Kill(Value!)
#Kill(X!)
#Kill(Y!)
#Kill(endY!)
#Kill(Max!)
#Kill(BarLength!)
#Kill(BarColor!)
#Kill(HPorSMP!)
}
}
Thanks for any help in this situation.
