---
kind: forum-thread
id: "toolkitzone-forums/12337"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "job center"
skin: "phpbb2"
thread_id: "12337"
title: "I know that every one asks for this but..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12337"
written: "2004-12-08T22:55:00"
last_post: "2005-01-06T23:44:00"
date_confidence: "exact"
captured: ["20050116235208"]
author: "Tetsuo"
repliers: ["Shinyumo", "Dont_Think_So", "Marz"]
authors: ["Tetsuo", "Shinyumo", "Dont_Think_So", "Marz"]
posts_present: 5
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_136639_amp_", captured: "20050116235208", sha256: "51409cb84eed232db22bfbc5433f4f8585a6a0fa8eb8951e71cd37861f0e65c9", wayback_url: "https://web.archive.org/web/20050116235208/http://www.toolkitzone.com/forums/viewtopic.php?p=136639&amp="}
links: []
---

# I know that every one asks for this but...

### Tetsuo · 2004-12-08 22:55 · #B136639

Can anyone make me a cursor based start program where the buttons are like this:
|
New Game |
Load game |
Quit |
on the lower right corner of the screen but still not be touching the side of
the screen.
I will add the story and such myself.

### Shinyumo · 2004-12-15 22:26 · #B140246

bitmap("background.jpg") *replace this with your own image
SetImage("button1.jpg",500,300,100,50) *also replace these buttons
SetImage("button2.jpg",500,350,100,50)
SetImage("button3.jpg",500,400,100,50)
menu! = CreateCursorMap()
CursorMapAdd(495,325,menu!)
CursorMapAdd(495,375,menu!)
CursorMapAdd(495,425,menu!)
choice! = CursorMapRun(menu!)
KillCursorMap(menu!)
Switch(choice!)
{
case(0) { new game commands}
case(1) { load game commands}
case(2) { quit commands}
}
That would work for 640 by 480 resolution with 100 by 50 pixel buttons
So...what resolution did you want, and what's the size of the buttons? ^^

### Tetsuo · 2005-01-06 18:16 · #B152151

Oh man!
I almost gave up on this!
Any way the Resolution is 640 X 480
And the the buttons are....How do you count button size?

### Dont_Think_So · 2005-01-06 23:21 · #B152345

Or instead of using the cursorMap command, you can use setButton. That way you click them instead of using the keyboard.

### Marz · 2005-01-06 23:44 · #B152350

**Dont_Think_So wrote:**

> Or instead of using the cursorMap command, you can use setButton. That way you click them instead of using the keyboard.
>

Mouse? Seriously, who uses a mouse anymore? You must be a witch. A female witch that thinks its a male. Burn him!
