---
kind: forum-thread
id: "acforum/14235"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "14235"
title: "Try something like this:"
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=14235"
written: "2002-06-05T25:46:00"
last_post: "2002-06-05T26:00:00"
date_confidence: "exact"
captured: ["20020620170436", "20020620170507"]
author: "pherexio"
repliers: []
authors: ["pherexio"]
posts_present: 2
pages_present: []
pages_total: null
posts_per_page: null
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: null, start: null, end: null, url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=14230", reason: "never-captured", note: "earlier post in this thread (msg 14230)"}
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_14235", captured: "20020620170436", sha256: "40eeadf5a08ccd74c68fceb39ef4dab91227e24a5c0a5695cf10e546781793e2", wayback_url: "https://web.archive.org/web/20020620170436/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=14235"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_14237", captured: "20020620170507", sha256: "e5bc2e9b95efdd4cb0b38c5f8d1b58d5dc5da70f13058755988746f34251c8af", wayback_url: "https://web.archive.org/web/20020620170507/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=14237"}
links: []
---

# Try something like this:

> [!missing] gap:earlier · http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=14230 · never-captured
> earlier post in this thread (msg 14230) was not recovered.

### pherexio · 2002-06-05 25:46 · #A1001-14235

#if fightB! = 0
{
#MWin("I tell ya wut, fight me and I'll come along.")
#wait(a$)
#MWinCls
#delay(1)
#fightenemy(B.ene, Ring.bkg)
#fightB! = 1
#end
}
*Yes, the player must talk to "B" again
#MWin("Okay I'm a coming.")
#wait(a$)
#addplayer("B.tem")
#MWin("B joined!")
#wait(a$)
#MWinCls
*next part for if u used item for guy on the board
#EraseItem(0)
#DestroyItem(0)
*0=the item slot any # from 0-9
*makes the item go away (never come back 2 run prg
Ph£r¢Xi0

### pherexio · 2002-06-05 26:00 · #A1001-14237

**btw**

I haven't used fightenemy in a while so if it screws up, I don't know whats wrong. (All the games i used it in were deleted somehow... GRR.)
Ph£r¢Xi0
