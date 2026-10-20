---
kind: forum-thread
id: "toolkitzone-forums/10520"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "customisation"
skin: "phpbb2"
thread_id: "10520"
title: "Custom Message Window Help (variable trouble)"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=10520"
written: "2004-10-22T20:02:00"
last_post: "2004-10-22T21:56:00"
date_confidence: "exact"
captured: ["20050109004656"]
author: "spitfire"
repliers: ["Occasionally_Correct", "Asimir"]
authors: ["spitfire", "Occasionally_Correct", "Asimir"]
posts_present: 5
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_115384_amp_", captured: "20050109004656", sha256: "22c1165526b9fdc0cefcc43f460a5c9e4a9f382737d10d78aa5aac6504eb7fc1", wayback_url: "https://web.archive.org/web/20050109004656/http://www.toolkitzone.com/forums/viewtopic.php?p=115384&amp="}
links: []
---

# Custom Message Window Help (variable trouble)

### spitfire · 2004-10-22 20:02 · #B115302

**Code:**

```
*Angels Of Darkness is Copyright (c) 2004 Keifer Furzland*

*AoDWin*

Method AoDWin(char$,pos!,Text1$,Text2$,Text3$,Text4$,Text5$)

{

 Font("Verdana")***Some initial settings, that will be used throughout***

 FontSize(14)

 ColorRGB(255,255,255)

 SaveScreen()

If(pos!=1)

 {

x!=150

y!==5

 }

If(pos!=2)

 {

x!==150

y!==495

 }

 Else()

 {

x!==150

y!==5

 }

SetImagetranslucent("mwin.bmp",x!,y!,600,100)

cmd$="char$=mwin_"+char$+".bmp"

 RPGCode(cmd$)

If(pos!=1)

 {

x1!==155

y1!==2

 }

If(pos!==2)

{

x1!==155

y1!==493}

 Else()

 {

x1!==150

y1!==493

 }

If(char$=="mwin_kara.bmp")

{

SetImageTransparent(char$,x1!,y1!,42,96,0,255,0)

}

Else()

{

SetImageTransparent(char$,x1!,y1!49,96,0,255,0)

}

}

AodWin("zhak",1,,,,,,)

Wait()
```

There. I have a problem with it.. It seems to not want to move the MWin around. It stays in the upper corner. And also, how would i make a word inside of other words a different color?
I need that for the key locations. PLEASE HELP!

### Occasionally_Correct · 2004-10-22 20:13 · #B115308

It's caused by the comparison operator (==) being used as the assignment operator (=). This should fix your problem:

**Code:**

```
//Angels Of Darkness is Copyright (c) 2004 Keifer Furzland

//AoDWin

Method AoDWin(char$,pos!,Text1$,Text2$,Text3$,Text4$,Text5$)

{

   Font("Verdana") //Some initial settings, that will be used throughout

   FontSize(14)

   ColorRGB(255,255,255)

   SaveScreen()

   If(pos!==1)

   {

      x!=150

      y!=5

   }

   ElseIf(pos!==2)

   {

      x!=150

      y!=495

   }

   Else()

   {

      x!=150

      y!=5

   }

   SetImagetranslucent("mwin.bmp",x!,y!,600,100)

   RPGCode("char$ = mwin_" + char$ + ".bmp")

   If(pos!==1)

   {

      x1!=155

      y1!=2

   }

   ElseIf(pos!==2)

   {

      x1!=155

      y1!=493

   }

   Else()

   {

      x1!=150

      y1!=493

   }

   If(char$=="mwin_kara.bmp")

   {

      SetImageTransparent(char$,x1!,y1!,42,96,0,255,0)

   }

   Else()

   {

      SetImageTransparent(char$,x1!,y1!49,96,0,255,0)

   }

}

AodWin("zhak",1,"","","","","","")

Wait()
```

### spitfire · 2004-10-22 20:33 · #B115322

hey
Thanks, but it changed now it won't work at all.. It pops up the debugger, and then it just kinda sits there. There isn't anything in the debug window.

### Occasionally_Correct · 2004-10-22 20:40 · #B115326

Oops. I added one-too-many paramters when calling the method. Razz Just take out one set of quotation marks.

### Asimir · 2004-10-22 21:56 · #B115384

Also, notice how OC used ElseIf. Your problem with the mwin always appearing at the bottom was because you didn't use ElseIf
