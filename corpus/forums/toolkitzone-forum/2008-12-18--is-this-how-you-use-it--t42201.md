---
kind: forum-thread
id: "toolkitzone-forum/42201"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "42201"
title: "Is this how you use it?"
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=42201"
written: "2008-12-18T02:51:00"
last_post: "2008-12-19T03:30:00"
date_confidence: "exact"
captured: ["20081220004446"]
author: "brenthenry"
repliers: []
authors: ["brenthenry"]
posts_present: 4
pages_present: [3]
pages_total: 3
posts_per_page: 10
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 1, start: 1, end: 10, url: "http://toolkitzone.com/forum/viewtopic.php?t=42201", reason: "never-captured"}
  - {page: 2, start: 11, end: 20, url: "http://toolkitzone.com/forum/viewtopic.php?t=42201&start=10", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_461851", captured: "20081220004446", sha256: "0a110b2369fd4a2a46c1b79ea162203faec48f08274b5142b484c12635dbcd0c", wayback_url: "https://web.archive.org/web/20081220004446/http://www.toolkitzone.com/forum/viewtopic.php?p=461851"}
links: []
---

# Is this how you use it?

> [!missing] gap:1-10 · http://toolkitzone.com/forum/viewtopic.php?t=42201 · never-captured
> Page 1 of 3 was not recovered.

> [!missing] gap:11-20 · http://toolkitzone.com/forum/viewtopic.php?t=42201&start=10 · never-captured
> Page 2 of 3 was not recovered.

### brenthenry · 2008-12-18 02:51 · #K461736

**furyX639 wrote:**

> ...Keep in mind you'd have to modify my line "if (...) { // Proceed to phase 3 is x and y is solid" to use a modified version of your function to check for solid object collisions...
>

Could you eplain which one and how? Im sorta confused

### brenthenry · 2008-12-18 04:17 · #K461745

**jackyboy wrote:**

>
> **Code:**
>
> ```
> elseif (phase == 2) { // Move item until solid object
>
>
>       if (...) { // Proceed to phase 3 is x and y is solid
> ```
>
> If you look close you'll see he has an if(...) that you need to replace with an actual if statement. And you simply need to check to see if the x and y are at a solid object. Isn't that what that tb4intersection() command did anyway, find a solid area and return the number of steps to that area? Same thing except it checks to see if a specific point is solid.
>

I'm still sorta confused, do I use getBoardTileType?
/edit nvm
/edit(2) whenever i press a button, it just says file not found Game/Tribute/SpcMove and /Item/.itm

### brenthenry · 2008-12-18 04:34 · #K461750

**Marz wrote:**

> it can't find a file called ".itm", you did something wrong in your string manipulation.
>

I don't see anything wrong
/edit

**Code:**

```
function preload() {

   for (i = 0; i <= 9; i++) {

      smFile = getSpecialMoveFile(i, 0);

      smpUse[i] = -1 * getSMInfo(smFile, 1);

      item[i] = createItem(left(smFile, len(smFile) - 4) + ".itm");

   }

}

   preload();

   phase = 0;

   while (true) {

      if (phase == 0) { // Get key until 0 - 9 is pressed

         key = get();

         if (key >= 0 && key <= 9) {

            key = (key == 0)? 9: key - 1;

            phase = 1;

         }

         } elseif (phase == 1) { // Put item in front of player

         switch (playerDirection(player)) {

            case (tkDIR_E) {x++;playerDir = "E";}

            case (tkDIR_W) {x--;playerDir = "W";}

            case (tkDIR_S) {y++;playerDir = "S";}

            case (tkDIR_N) {y--;playerDir = "N";}

         }

         x = playerX[0] + (playerDir == "E") - (playerDir == "W");

         y = playerY[0] + (playerDir == "S") - (playerDir == "N");

         putItem(item[key], x, y, playerLayer[0]);

         x += (playerDir == "E") - (playerDir == "W");

         y += (playerDir == "S") - (playerDir == "N");

         phase = 2;

         } elseif (phase == 2) { // Move item until solid object

         if (getBoardTileType(x,y) == "SOLID") { // Proceed to phase 3 is x and y is solid[ill check for items and tings later]

            phase = 3;

            } else {

            itemPath(item[key], tkMV_CLEAR_QUEUE, x, y);

            x += (playerDir == "E") - (playerDir == "W");

            y += (playerDir == "S") - (playerDir == "N");

         }

      }

      elseif (phase == 3) { // Erase item and take SMP

         eraseItem(item[key]);

         giveSmp("Akriso", smUse[key]);

      }

   }
```

### brenthenry · 2008-12-19 03:30 · #K461851

ok part of the problem was preload() conitnuing to loop, so even is there is no spell file, it goes through it, so i added a seterrorhandler(), and does get() return a string or int? or are they the same thing? that might be the problem
