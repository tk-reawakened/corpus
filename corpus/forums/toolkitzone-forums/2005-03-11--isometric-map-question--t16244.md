---
kind: forum-thread
id: "toolkitzone-forums/16244"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "16244"
title: "Isometric Map question"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=16244"
written: "2005-03-11T09:01:00"
last_post: "2005-03-13T11:28:00"
date_confidence: "exact"
captured: ["20050325131930"]
author: "tsmpaul"
repliers: ["Delano", "RDemusX"]
authors: ["tsmpaul", "Delano", "RDemusX"]
posts_present: 8
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_179842_amp_", captured: "20050325131930", sha256: "a4506800aae7194d684f70f8d9aaa50e75e04a10d16af75df0e39b3730ef3f24", wayback_url: "https://web.archive.org/web/20050325131930/http://toolkitzone.com/forums/viewtopic.php?p=179842&amp="}
links: []
---

# Isometric Map question

### tsmpaul · 2005-03-11 09:01 · #B178933

Hi, I don't know if this is a bug or I'm just doing something wrong... I thought I'd try making an isometric map, but no matter what size I set in the Board Information, it won't put a vertical scrollbar on the screen for me to scroll down and see more of the map, it only seems to resize it along the X coordinate... I also tried converting a large square tile map to isometric, and it basically displayed the top part of it, and I should have been able to scroll down the screen to see the rest but it wasn't there... Weird. I tried searching the forums and reading the bug report, but I didn't find any mention of this sort of thing?

### Delano · 2005-03-11 13:44 · #B178950

For isometrics y-tiles scale half that of normal tiles (16px), and x-tiles double (64px) on the board, so you need twice as many rows in order for the board to occupy the same amount of space. If you keep on resizing you should eventually fill the screen. Or do you mean the scroll bar is off the screen to the right? What resolution do you run?
As for converting 2D boards to isometrics, it just doesn't really work. Conversion doesn't rotate the board, it rotates the tiles and staggers the columns - it's best to set the mode to isometric before starting to make a board.

### tsmpaul · 2005-03-11 22:52 · #B179125

Yeah, the scroll bar was off the screen to the right so I had no way of scrolling down the screen. Weird though, I booted up my computer today, and the scroll bar is there now! Yesterday nothing I did would make it appear, but now I can scroll around and access the whole board. I guess I can't complain about that Smile

### tsmpaul · 2005-03-11 23:59 · #B179172

I found out what is happening, cause the vertical scroll bar seemed to vanish again! It's acrually still there, but only two pixels wide as the rest of it goes off the screen to the right. It seems that if I open the project list or any of the buttons on the top-right that pop up a listbox, the slider bar will appear beside the box, but if no extra window is open, the scroll bar goes off the screen if width is above 15 tiles. I guess the way to get around that is just to keep the project list open so the scroll bar is always visible.

### Delano · 2005-03-12 13:55 · #B179436

Ah, ok - that's a mis-calculation of the width on my part - it'll be easy to sort. What resolution do you use?

### RDemusX · 2005-03-12 14:26 · #B179443

He uses 640 x 480 ...
RDX

### tsmpaul · 2005-03-12 22:02 · #B179654

The game plays in 640x480, but my windows desktop resolution is 1024x768 at the moment.

### Delano · 2005-03-13 11:28 · #B179842

Ah yeah, I meant the desktop res Wink
