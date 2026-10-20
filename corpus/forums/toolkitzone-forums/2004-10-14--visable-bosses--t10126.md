---
kind: forum-thread
id: "toolkitzone-forums/10126"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "advanced"
skin: "phpbb2"
thread_id: "10126"
title: "Visable bosses"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=10126"
written: "2004-10-14T14:22:00"
last_post: "2004-10-15T14:24:00"
date_confidence: "exact"
captured: ["20050109004402"]
author: "prowlor"
repliers: ["Nick"]
authors: ["prowlor", "Nick"]
posts_present: 5
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_110764_amp_", captured: "20050109004402", sha256: "a9982738d6175332e90a4a6daa54569bc37550c12d7944b50c76e3d6b4299bc8", wayback_url: "https://web.archive.org/web/20050109004402/http://www.toolkitzone.com/forums/viewtopic.php?p=110764&amp="}
links: []
---

# Visable bosses

### prowlor · 2004-10-14 14:22 · #B110308

In my game, I plan to make all bosses visable on the map, so that you can plan for the encouter. I planned to set multiple programs that would draw out the creature tile by tile, and it worked, exept, when they die, I dont know how to make the visual and the programs go away, as of now, you can fight the bosses an indefinite ammount of times... does anyone know how i could make the bosses dissapear permenelty off the map?

### Nick · 2004-10-14 14:48 · #B110316

One way you could do it is instead of making the boss tile-by-tile on the map, make a tile bitmap. Then you can use that tile bitmap as a frame for an animation (and it can be just one frame). Use that animation as the rest/south idle graphic for an item. You would set the item on the board and have the player activate the battle through it, then remove the item after the battle.

### prowlor · 2004-10-14 18:29 · #B110368

Although not new to the toolkit community, this is the first game I serioulsy thought about working the entire way through, how would i go about turning the enemy into a bitmap image, or deleateing it... i thought about finding a way to deleate programs off boards, and run a RPGC program at the defeat of the enemy

### Nick · 2004-10-14 20:36 · #B110409

Use the Tile Bitmap editor. It lets you use tiles to assemble pictures, just like making a board. You can then use Tile Bitmaps as frames in an animation, which you use for the graphics for an item.
Then you can use DestroyItem() and EraseItem() to remove them from the board.

### prowlor · 2004-10-15 14:24 · #B110764

Thank you, I shall try that
