---
kind: forum-thread
id: "toolkitzone-forums/30462"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "RPG Code"
skin: "phpbb2"
thread_id: "30462"
title: "Cursor maps &gt;.&lt;;"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=30462"
written: "2006-06-11T20:07:00"
last_post: "2006-06-11T20:07:00"
date_confidence: "exact"
captured: ["20060612045751"]
author: "factualpuddle"
repliers: []
authors: ["factualpuddle"]
posts_present: 1
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_326631", captured: "20060612045751", sha256: "72e1d1241624caba594fd899d8e59336d60ccac1b26d41aca7cf8ca0aa62657a", wayback_url: "https://web.archive.org/web/20060612045751/http://www.toolkitzone.com/forums/viewtopic.php?p=326631"}
links: []
---

# Cursor maps &gt;.&lt;;

### factualpuddle · 2006-06-11 20:07 · #B326631

ok, i need help >.<; i made it to where, if a player exists put the cursormap there...but now, if a player doesnt exist in the party...it messes up the res! number of my back button, can someone tell me what to do? lol, here is the code:

**Code:**

```
//============

// Clearing

//============

Clear()

//============

// Includes

//===============

include("menu.prg")

include("abilities.prg")

//=================

// Abilities Image

//=================

setimagetransparent("abilities2.bmp", 20, 380, 153, 77, 0, 0, 0)

//================

// Buttons

//================

Setimagetransparent("back2.bmp", 530, 398, 153, 56, 0, 0, 0)

Setimagetransparent("abilities_khaun.bmp", 50, 5, 99, 63, 0, 0, 0)

if(playerHandle$[1] !>"")

{

Setimagetransparent("abilities_john.bmp", 150, 5, 99, 63, 0, 0, 0)

}

if(playerHandle$[2] !>"")

{

Setimagetransparent("abilities_antione.bmp", 250, 5, 99, 63, 0, 0, 0)

}

//=========================

// Cursor Map

//=========================

cursorMapHand("cursor.bmp",0)

cMap! = createCursorMap()

   cursorMapAdd(70, 40, cMap!)

   if(playerhandle$[1] !>"")

   {

   cursorMapAdd(180, 40, cMap!)

   }

   if(playerHandle$[2] !>"")

   {

   cursorMapAdd(270, 40, cMap!)

   }

   cursorMapAdd(535, 427, cMap!)

   res! = cursorMapRun(cMap!)

   killCursorMap(cMap!)

//=============

// Results

//=============

switch(res!)

{

case (0)

{

setimagetransparent("profilemain.bmp", 50, 100, 100, 100, 0, 255, 0)

   if (Khaun[level]! <= 4)

   {

   pixeltext(150, 135, "No Abilities")

   wait()

   }

}

if(playerhandle$[1] !>"")

{

   case (1)

   {

   setimagetransparent("profilejohn.bmp", 50, 100, 100, 100, 0, 255, 0)

      if (John[level]! <= 4)

      {

      pixeltext(150, 135, "No Abilities")

      wait()

      }

   }

}

if(playerHandle$[2] !>"")

{

   case (2)

   {

   setimagetransparent("profileantione.bmp", 50, 100, 100, 100, 0, 255, 0)

   pixeltext(150, 132, "Job: Mage")

   pixeltext(150, 150,"HP:<MaxHP!>/<Hp!>")

   pixeltext(150, 168, "MP:<MaxSMP!>/<SMP!>")

   wait()

   }

}

case (3)

{

clear()

run("menu.prg")

}

}
```

**I edited the code a little...
