---
kind: forum-thread
id: "acforum/4765"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "4765"
title: "Trouble with the Eternal Blade Start Menu"
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=4765"
written: "2003-06-16T11:29:00"
last_post: "2003-06-16T11:29:00"
date_confidence: "exact"
captured: ["20030721011437"]
author: "yourlittlebuttercup"
repliers: []
authors: ["yourlittlebuttercup"]
posts_present: 1
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_4765", captured: "20030721011437", sha256: "fabf03cf5c0dd4b8d7d824363d96677a94635315cd896ae1a9cf56b2e6bcdbf5", wayback_url: "https://web.archive.org/web/20030721011437/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=4765"}
links: []
---

# Trouble with the Eternal Blade Start Menu

### yourlittlebuttercup · 2003-06-16 11:29 · #A1001-4765

Can someone take a looks at this? After the title screen shows, i load this. The thing is, if you press up on 'new game', down on 'quit' or move the curser onto something it was already one, then the program exits. What should I change?
#drawtitle()
#Method drawtitle()
{
#Include(startload.prg)
#Bitmap("title.bmp")
#Done!==0
#ColorRGB(000,000,000)
#CursorPlace!==0
#StartMenu()
#Method StartMenu()
{#While Done!==0
{
#Bitmap("title.bmp")
#Fontsize(26)
#Text(9,6,"New Game")
#Text(9,7,"Continue")
#Text(9,8,"Quit")
#If(CursorPlace!==0)
{
#Put(6,5,"LSOT menu.tst1")
#Wait(a$)
#If(a$=="DOWN")
{
#Wav("menumove.mid")
#Put(6,5,"LSOT menu.tst2")
#CursorPlace!==1
}
#If(a$=="UP")
{
#Wav("menumove.mid")
#Put(6,5,"LSOT menu.tst2")
#CursorPlace!==2
}
#If(a$=="ENTER")
{
#Wav("menuselect.mid")
#Fontsize(18)
#History
}
}
#If(Cursorplace!==1)
{
#Put(6,5.75, "LSOT menu.tst1")
#Wait(a$)
#If(a$=="DOWN")
{
#Wav("menumove.mid")
#Put(6,5.75,"LSOT menu.tst2")
#Cursorplace!==2
}
#If(a$=="UP")
{
#Wav("menumove.mid")
#Put(6,5.75,"LSOT menu.tst2")
#CursorPlace!==0
}
#If(a$=="ENTER")
{
#Wav("menuselect.mid")
#loadgame
#Fontsize(18)
}
}
#If(Cursorplace!==2)
{
#Put(6,6.5,"LSOT menu.tst1")
#Wait(a$)
#If(a$=="UP")
{
#Wav("menumove.mid")
#Put(6,6.5,"LSOT menu.tst2")
#Cursorplace!==1
}
#If(a$=="DOWN")
{
#Wav("menumove.mid")
#Put(6,6.5,"LSOT menu.tst2")
#Cursorplace!==0
}
#If(a$=="ENTER")
{
#Wav("menuselect.mid")
#Dos
}
}
}
}
"When you got it, flaunt it"
