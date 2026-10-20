---
kind: forum-thread
id: "toolkitzone-forums/12023"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "toolkit 2.x support"
skin: "phpbb2"
thread_id: "12023"
title: "ReturnMethod trouble"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12023"
written: "2004-12-01T22:00:00"
last_post: "2004-12-04T04:40:00"
date_confidence: "exact"
captured: ["20050114191945"]
author: "zyrshnikashnu"
repliers: ["zeno"]
authors: ["zyrshnikashnu", "zeno"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_134419_amp_", captured: "20050114191945", sha256: "a1c9567a795dfcbc9fec82c3af8b9291bfce17ca01e8d85016537d7823757cef", wayback_url: "https://web.archive.org/web/20050114191945/http://www.toolkitzone.com/forums/viewtopic.php?p=134419&amp="}
links: []
---

# ReturnMethod trouble

### zyrshnikashnu · 2004-12-01 22:00 · #B133053

Are there any known problems with ReturnMethod in TK2? I ask this because it doesn't seem to function properly in some programs, yet both the working and non-working utilize the same method! I suppose the code might help you a bit...

**rpgcode:**

```
Method QBox(QBox_name$, QBox_quest$, QBox_Text1$, QBox_Text2$, QBox_Text3$, QBox_profile$, ResVar!)

{

     Include("system.prg")

     ResVar! = 1

     cursormax! = 3

     setimage("mwin2.png", 29, 340, 550, 110)

     setimage(QBox_profile$, 52, 363, 64, 64)

     If(QBox_profile$ == "")

     {

          SetImage("dprofile.png", 52, 363, 64, 64)

     }

     FontSize(15)

     Bold("on")

     colorrgb(0, 255, 0)

     Text(9.8, 24.7, QBox_name$)

     bold("off")

     colorrgb(255, 255, 255)

     Text(9.8, 25.7, QBox_quest$)

     Text(10, 26.7, QBox_Text1$)

     Text(10, 27.7, QBox_Text2$)

     Text(10, 28.7, QBox_Text3$)

     cachescreen(1)

     qbdone! = 0

     cursor! = 1

     if(QBox_Text3$ == "")

     {

          cursormax! = 2

     }

     while(qbdone! == 0)

     {

          flipscreen(1)

          if(cursor! == 1)

          {

               colorrgb(255, 0, 0)

               Text(10, 26.7, QBox_Text1$)

          }

          if(cursor! == 2)

          {

               colorrgb(255, 0, 0)

               Text(10, 27.7, QBox_Text2$)

          }

          if(cursor! == 3)

          {

               colorrgb(255, 0, 0)

               Text(10, 28.7, QBox_Text3$)

          }

          wait(move$)

          if(move$ == "UP")

          {

               if(cursor! == 1)

               {

                    cursor! = cursor!-1

               }

          }

          if(move$ == "DOWN")

          {

               if(cursor! == cursormax!)

               {

                    cursor! = cursor!+1

               }

          }

          if(move$ == "ENTER")

          {

               qbdone! = 1

               ResVar! = cursor!

               returnmethod(ResVar!)

               kill(cursor!)

               kill(move$)

          }

     }

}
```

### zeno · 2004-12-03 01:47 · #B133938

don't use the return method..I just don't need to!! try making up your own methods...

### zyrshnikashnu · 2004-12-04 04:40 · #B134419

Ah, but ReturnMethod is needed if you're using a library for your methods, which I am doing. Also, I am using my own method, as is seen above. I don't know why you assume I didn't write it...
I've fixed most of my problems by putting the QBox method directly in any programs that use it and then excluding ReturnMethod altogether, but that's a bit of a hassle. What I really want to know is whether anyone else has experienced this problem, and, if so, if it can be worked around in any other way than described above.
