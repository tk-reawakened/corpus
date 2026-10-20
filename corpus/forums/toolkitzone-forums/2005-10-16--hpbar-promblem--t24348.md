---
kind: forum-thread
id: "toolkitzone-forums/24348"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Code"
skin: "phpbb2"
thread_id: "24348"
title: "HPBar Promblem"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=24348"
written: "2005-10-16T17:37:00"
last_post: "2005-10-18T02:16:00"
date_confidence: "exact"
captured: ["20051219230028"]
author: "????"
repliers: ["X", "Tao-Kun", "p90m16mp5a4", "Dont_Think_So"]
authors: ["????", "X", "Tao-Kun", "p90m16mp5a4", "Dont_Think_So"]
posts_present: 6
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_265168_amp_3Bsid_b4534c849086ea60f22aa5790d1e69a7", captured: "20051219230028", sha256: "05c62ddbd4a8134081ceafe850def40592cf3057d2230f769977c4e07865c2e0", wayback_url: "https://web.archive.org/web/20051219230028/http://toolkitzone.com/forums/viewtopic.php?p=265168&amp%3Bsid=b4534c849086ea60f22aa5790d1e69a7"}
links: []
---

# HPBar Promblem

### ???? · 2005-10-16 17:37 · #B264860

OK
Here is my code and here is the promblem

**Code:**

```
Autolocal

RenderNow("ON")

Bold("ON")

setImageTransParent("HPBar.bmp",1,1,100,100,255,255,255)

Text(1,1,"HP:9999/9999")
```

Ok thats part of the code, anyways here's the promblem how do you change text without clearing the hpbar like how would you make go from 9999/9999 to 120/9999 or 24/24 stuff like that, I am confused on how to do it

### X · 2005-10-17 12:48 · #B264992

If you are not using custom stats, try something like:
TextText(1,1,"HP:<Hero[health]!>/<Hero[maxhealth]!>")
I know there is a way using the RPGCode command to combine PlayerHandle[x!]$ with [health]!, but I cant remember it right now. Also, my custom health/energy/whatever bars are still somewhat crappy, so I wont be able to help you much there.

### Tao-Kun · 2005-10-17 17:47 · #B265033

**X wrote:**

> I know there is a way using the RPGCode command to combine PlayerHandle[x!]$ with [health]!, but I cant remember it right now.
>

You could get the player's health and save it into a varible, then do it the way you stated above.

### ???? · 2005-10-17 22:16 · #B265110

I still need help

### p90m16mp5a4 · 2005-10-17 23:16 · #B265122

While you have turned 'rendernow' on, you have nothing drawn to it. Check the #Setimage definition, the last paramet says : [hCnvDest!], wich means 'handle to the canvas to be draw to'. So, if you wanted to use #Setimage to draw to a canvas, you supply the canvas id as the last parameter. Now, you want to *permanently* show the hp so you put the "constant canvas" id as the last parameter, wich is CnvRenderNow!. yep, CnvRenderNow! is a constant, premade canvas.
SetImageTransparent("Mypic.pic", 1,1, 200,200, 12,12,120, CnvRenderNow!)
You can use CnvRenderNow! for any command that can draw to a canvas, like #text and #setimage.

### Dont_Think_So · 2005-10-18 02:16 · #B265168

**Code:**

```
while(true)

{

     multirun()

     {

          RenderNow("ON")

          Bold("ON")

          setImageTransParent("HPBar.bmp",1,1,100,100,255,255,255, cnvRenderNow!)

          Text(1,1,"HP:<PLAYER[health]!>/<PLAYER[maxhealth]!>", cnvRenderNow!)

      }

}
```

Untested, but that should do it.
