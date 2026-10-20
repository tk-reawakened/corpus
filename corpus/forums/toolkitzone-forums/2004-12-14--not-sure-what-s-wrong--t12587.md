---
kind: forum-thread
id: "toolkitzone-forums/12587"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12587"
title: "Not sure what's wrong"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12587"
written: "2004-12-14T12:55:00"
last_post: "2004-12-14T12:55:00"
date_confidence: "exact"
captured: ["20041228072820"]
author: "Zio"
repliers: []
authors: ["Zio"]
posts_present: 1
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_139488_amp_", captured: "20041228072820", sha256: "4d98afe5eaf850adba33cb7e84eb15aee629c5dd4e8c826a959b66020a25c852", wayback_url: "https://web.archive.org/web/20041228072820/http://www.toolkitzone.com/forums/viewtopic.php?p=139488&amp="}
links: []
---

# Not sure what's wrong

### Zio · 2004-12-14 12:55 · #B139488

I don't Get why this isn't woring right. It keeps running the Else code as well as the If. It might be just because i've been up for 17 hours so please forgive my stupidity.

**Code:**

```
While(FogInnerY! < 39)

{

#If (X1Y[FogInnerY!]! == 0)

   {

   FogInnerY!++

   #SetImage("cover1.bmp",Fogx!,Fogy!,13,13)

   Fogx! = Fogx! + 12

   Fogloopx!++

   #If(Fogloopx! == 3)

      {

      Fogloopx! = 0

      Fogx! = Fogx! + 3

      }

   }

#Else()

   {

   #If(X0Y[FogInnerY!]! = 0)

      {

      #SetImageTransparent("CoverInner4.bmp",fogx!,fogy!,13,13,255,0,255)

      }

   FogInnerY!--

   #If(X1Y[FogInnerY!]! = 0)

      {

      #SetImageTransparent("CoverInner2.bmp",fogx!,fogy!,13,13,255,0,255)

      }

   FogInnerY! = FogInnerY! + 2

   #If(X1Y[FogInnerY!]! = 0)

      {

      #SetImageTransparent("CoverInner3.bmp",fogx!,fogy!,13,13,255,0,255)

      }

   FogInnerY!--

      #If(X2Y[FogInnerY!]! = 0)

      {

      #SetImageTransparent("CoverInner1.bmp",fogx!,fogy!,13,13,255,0,255)

      }

   Fogx! = Fogx! + 12

   }

}
```

I also don't know why my var!++ don't show up with the rpgcode command when i preview it or if i preview more then once i can't submit or preview again
