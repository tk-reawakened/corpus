---
kind: forum-thread
id: "acforum/1443"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "1443"
title: "Audio problems"
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=1443"
written: "2001-12-10T30:53:00"
last_post: "2001-12-11T19:32:00"
date_confidence: "exact"
captured: ["20011230231648", "20011230232328"]
author: "(redacted: email)"
repliers: ["Darq"]
authors: ["(redacted: email)", "Darq"]
posts_present: 2
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1002_mode_1_msg_1443", captured: "20011230231648", sha256: "4f3bd0e0a1adf08bc501dbd30217735c2794cda9046da747fb61e3a9206177b2", wayback_url: "https://web.archive.org/web/20011230231648/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=1443"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1002_mode_1_msg_1448", captured: "20011230232328", sha256: "8635ce41234a82b9b221d3ba31b186179f2053346c03cb2479c854e297fca15f", wayback_url: "https://web.archive.org/web/20011230232328/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=1448"}
links:
  - {url: "http://wind.prohosting.com/~darq/index.html", status: "external", local: null}
---

# Audio problems

### (redacted: email) · 2001-12-10 30:53 · #A1002-1443

I have a problem with the audio during part of my game. The audio just stops when the titles start. Try this code out if you can see what I mean. If you take out the empty TExt("")in the beginning the audio stops.
*******************************************************
**
** Basic Startup Program.
** ----------------------
**
** Look for all lines commented as TBD (to be done)
** to see what you should change.
**
*******************************************************
*******************************************************
* Some initial settings. Maybe you want to change these...
#Fontsize(12)
#itemwalkspeed("slow")
#walkspeed("slow")
*******************************************************
#BorderColor(0,0,0)
#Fade(1)
*******************************************************
* TBD: Play a title screen file here...
#Mp3("song1.mp3")
#Clear
*******************************************************
*******************************************************
* TBD: Put your own company name here...
#Text(9,20,"")
#Clear
#delay(1)
*******************************************************
*******************************************************
* Draws the title screen...
#drawtitle()
*******************************************************
*******************************************************
* Waits for the user to choose something...
#done!=0
#While(done!=0)
{
#MouseClick(x!,y!) *waits for a mouse click and returns x y coords
#CheckButton(x!,y!,opt!) *checks if we clicked a button
#if (opt!=0)
{
*'new game' clicked
#history()
#Color(15)
* TBD: You might want to change the message window graphic...
#WinGraphic("mwin.jpg") *Message window graphic
#Fontsize(12)
#done!=1
#end
}
#if (opt!=1)
{
*'load game' clicked
#dirsav(dest$)
#if(dest$~="CANCEL")
{
#load(dest$)
#done!=1
#end
}
}
#if (opt!=2) {#dos}
}
#end
*******************************************************
* This method draws the title screen...
*******************************************************
#method drawtitle()
{
#Fade(1)
#Clear
#Text(1,1,"Your Game Title...")
* TBD: Set some graphic for your title screen graphic.
* #Bitmap("title.jpg")
#WinGraphic("mwin.jpg")
* TBD: Maybe you want to change these buttons...
#setbutton("new.jpg", 0,123,45,125,30)
#setbutton("load.jpg",1,248,45,125,30)
#setbutton("quit.jpg",2,373,45,125,30)
}
* TBD: Put a stroy here...
#method history()
{
*Main story
#MWin(" Your story goes here...")
#Wait(a$)
}

### Darq · 2001-12-11 19:32 · #A1002-1448

**For one thing, this goes under help, and do you have the registered version of TK? -nt-**

**[Atomic Computers Homepage](http://wind.prohosting.com/~darq/index.html)**
