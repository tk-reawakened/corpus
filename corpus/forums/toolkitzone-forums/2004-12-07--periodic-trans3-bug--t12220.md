---
kind: forum-thread
id: "toolkitzone-forums/12220"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "12220"
title: "(Periodic) Trans3 Bug..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12220"
written: "2004-12-07T00:56:00"
last_post: "2004-12-09T14:25:00"
date_confidence: "exact"
captured: ["20050116235317"]
author: "Akura_TheDragonBlader"
repliers: ["Delano", "Levi", "Koh Wei Zane", "Colin", "oblivious_casualty", "Dont_Think_So"]
authors: ["Akura_TheDragonBlader", "Delano", "Levi", "Koh Wei Zane", "Colin", "oblivious_casualty", "Dont_Think_So"]
posts_present: 15
pages_present: [2]
pages_total: 2
posts_per_page: 15
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 1, start: 1, end: 15, url: "http://toolkitzone.com/forums/viewtopic.php?t=12220", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_136975_amp_", captured: "20050116235317", sha256: "d866f03e47d4520263f16572d54f1507640caa7217a049b458fcdef9a8c1d561", wayback_url: "https://web.archive.org/web/20050116235317/http://www.toolkitzone.com/forums/viewtopic.php?p=136975&amp="}
links:
  - {url: "http://darkforce.shyper.com/stuff/2cursor.png", status: "external", local: null}
  - {url: "http://darkforce.shyper.com/stuff/blurred.png", status: "external", local: null}
---

# (Periodic) Trans3 Bug...

> [!missing] gap:1-15 · http://toolkitzone.com/forums/viewtopic.php?t=12220 · never-captured
> Page 1 of 2 was not recovered.

### Akura_TheDragonBlader · 2004-12-07 00:56 · #B135765

TK3 runs moderately well on mine. Actually, the only slowdown I noticed was possibly during battle, but I think that was supposed to be butt-slow to begin with. A crappy 950MHz, too.

### Delano · 2004-12-07 18:33 · #B136065

Are you guys using the latest dev builds? One of the reasons for the fps in the window title is to quantify the tk's speed and gauge it's performance across the community's computers.
Currently the fps is tied in with the walking system, but it's a good estimate of the general performance of the tk engine. However, because of the way the movement system has been set up (to use absolute walking speeds), the walking speed should be consistent across all pc's, independent of fps.

### Levi · 2004-12-07 19:08 · #B136076

I don't know what it is but it is very slow on mine. Sometimes it takes up to five seconds before the character moves. Actually, hmmm, I wonder if I've been observing things wrong. I've never tried the demo. Just my own program. I'll check it out and see what happens.

### Koh Wei Zane · 2004-12-07 23:07 · #B136186

By the way, the latest build of Trans3.exe (Dec 5) is running wickedly fast for me. The start up at 120+ fps. The Test Game where the NPC is outside the house is moving ridicuously fast that it is IMPOSSIBLE to talk to it. (95 FPS)

### Colin · 2004-12-07 23:21 · #B136188

FPS does not affect walking speed. I'll have a new build in a moment that has a non-flickering cursor too.
The reason walking is "messed up" is because game speed setting in the main file editor work differently now. A call to GameSpeed() in start.prg can fix it until the release when y'all get the editor.

### Levi · 2004-12-08 01:01 · #B136244

Ah yes. Tried it out. It works fine until I bring in other walking characters and such. And my first scene was full of that. I'll look for the next update. Can't wait.

### Delano · 2004-12-08 13:30 · #B136447

The problems with the character/item speeds is that each item/player can (and should be) assigned it's own walk speed - this is given in fractions of a second (say 0.1) so as to be the same across all pcs.
The individual speeds can be set either through rpgcode (#ItemSpeed(num!, speed!) etc.) or in the editor... er, which I guess you haven't had access to yet... hmm!

### oblivious_casualty · 2004-12-08 14:25 · #B136461

TK3 runs at an acceptable speed for me on my 333Mhz 96MB RAM computer, although some RPGCode runs a bit slow.

### Koh Wei Zane · 2004-12-09 00:20 · #B136693

Thanks Colin for the build. Very Happy
Heh.
![](http://darkforce.shyper.com/stuff/2cursor.png)
Nice frame speed and I've got a cursor moving at the bottom right and the other is left on the top left.
![](http://darkforce.shyper.com/stuff/blurred.png)
Very smooth looking text. Nice cursors. And my character can travel a hundred miles per second.
But still promising... Great improvements..

### Dont_Think_So · 2004-12-09 03:04 · #B136812

yay, SetConstants works now...
And so does my spotlight.

### Colin · 2004-12-09 04:07 · #B136854

**silent'-darkforce wrote:**

> But still promising... Great improvements..
>

That build is in the middle of major gfx changes, it was just for testing and can easily be changed back. You're lucky I'm so patient. I did as for bug reports to me pmmed Razz
It's all good.

### Koh Wei Zane · 2004-12-09 05:55 · #B136914

Ah, ok. Next you might want to try making the logo of a sword (in the titlebar) beside "test game [xxx.x fps]".

### Colin · 2004-12-09 06:00 · #B136917

The sword brands a game much more than just the windows thingy.

### Koh Wei Zane · 2004-12-09 06:05 · #B136921

Everytime one of my program crashes it will look exactly as that logo. It's making me go mad. Evil or Very Mad

### oblivious_casualty · 2004-12-09 14:25 · #B136975

hey colin, could you add an option to select the icon for the window during runtime?
