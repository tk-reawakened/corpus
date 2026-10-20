---
kind: forum-thread
id: "acforum/3947"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "3947"
title: "PLEASE HELP ME!!!!!!!!!!..."
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=3947"
written: "2001-12-15T17:41:00"
last_post: "2002-08-13T29:02:00"
date_confidence: "exact"
captured: ["20011230105420", "20011230112821", "20011230121657", "20020105144453", "20020105150214", "20020829233536"]
author: "GAME GUY"
repliers: ["Lon PoPo", "mestwin", "Gamemaster", "natsy", "bobharkin"]
authors: ["GAME GUY", "Lon PoPo", "mestwin", "Gamemaster", "natsy", "bobharkin"]
posts_present: 6
pages_present: []
pages_total: null
posts_per_page: null
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: null, start: null, end: null, url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=3931", reason: "never-captured", note: "earlier post in this thread (msg 3931)"}
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_3947", captured: "20011230112821", sha256: "204d38bdc44ca0a5fa491f64815b2fee8cd6c2361a8bdf35a8d7c9ab78380fd3", wayback_url: "https://web.archive.org/web/20011230112821/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=3947"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_3957", captured: "20011230121657", sha256: "a93b102529dd8759e5098858faaeba83563116a583b4ee1347b2ee2ac33bd2e9", wayback_url: "https://web.archive.org/web/20011230121657/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=3957"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_3979", captured: "20011230105420", sha256: "d60bcd8c2a0920e999816fa5dbcfeb7f42814dfc861fea9ca647dcf78a62f616", wayback_url: "https://web.archive.org/web/20011230105420/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=3979"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_3983", captured: "20020105144453", sha256: "cceb5b67dd6d63bcd6b704202793095eadb77d7214193fc257e18aade75089c0", wayback_url: "https://web.archive.org/web/20020105144453/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=3983"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_3988", captured: "20020105150214", sha256: "cbee34425ede7af610a37eb3c544e9210c7b28f17d64f9078d861e60d5ba5acb", wayback_url: "https://web.archive.org/web/20020105150214/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=3988"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1002_mode_1_msg_3951", captured: "20020829233536", sha256: "95e327c77ecb8d17baf18e30986fd94cbd8c21442d77e6ee7b7c8cd095b9bc62", wayback_url: "https://web.archive.org/web/20020829233536/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=3951"}
links: []
---

# PLEASE HELP ME!!!!!!!!!!...

> [!missing] gap:earlier · http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=3931 · never-captured
> earlier post in this thread (msg 3931) was not recovered.

### GAME GUY · 2001-12-15 17:41 · #A1001-3947

I've been trying to lay off the capps guys, and I know you're anoyed with my questions... Sorry about that. Anyway here's my question:
I've been working on this code for a while now.....
I seriously need help, and I need an answer to what's wrong with this code..... Whenever I play my game the rpg debugger pops up,AND DOESN'T SAY ANYTHING!?...(whatz up with that?)It also freezes up my character. I've set it as an item, and used the multitask board... I don't need help with any of those, just the coding. People have told me to take Out The #Delay NOTHING WORKS(for me anyway)!...please help me with the coding I'M DESPERATE!(I apoligize if I sound crazy, and too demanding) Could someone please try this code for themselves,and see what happens? I've debugged it so many times, I need someone elses help...
here's the code:
#If (timestart!==0)
{
#MWIN("TIME HAS STARTED!!!!")
#timestart!==240
}
#Time!= timestart!
:Top
#Delay(1)
#Time!=Time!-1
#if (Time!=<1)
{
#Mwin("GAME OVER!")
#END()
}
#Branch (:Top)

### Lon PoPo · 2001-12-15 20:43 · #A1001-3957

**Dyn i need your help**

You seem intelligent, and informational. What do i need to download that will make it easy for me to make a 3d character like FF7. Also do you know the battle systal Fantasy 7, you know were they actually run up and hit the enemy? Help me.

### mestwin · 2001-12-15 24:24 · #A1001-3979

**take one of the equal signs out of #timestart!==240 (I think) (nt)**

*(no text captured)*

### Gamemaster · 2001-12-15 25:08 · #A1001-3983

**Here...**

To make a bitmap appear, use this command...
#Bitmap("yourpicture.bmp")
The #Bitmap command can also be used to display gifs and jpgs, and a whole bunch of other image files (only in 2.19, though).
When you say "make a noise", I assume you mean to play a wav file. To do that, use this...
#Wav("Yoursound.wav")
Gamemaster

### natsy · 2001-12-15 25:56 · #A1001-3988

**Also...**

#setimage can be used to place an image on the screen.
This message courtesy of Flustered Owl Productions

### bobharkin · 2002-08-13 29:02 · #A1002-3951

**no -nt**

you don't
later...
bob
