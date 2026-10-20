---
kind: forum-thread
id: "toolkitzone-forums/16218"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "16218"
title: "A problem with AVI's"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=16218"
written: "2005-03-10T07:13:00"
last_post: "2005-03-13T19:22:00"
date_confidence: "exact"
captured: ["20050325132000"]
author: "tsmpaul"
repliers: ["Delano", "khaldore"]
authors: ["tsmpaul", "Delano", "khaldore"]
posts_present: 4
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_179973_amp_", captured: "20050325132000", sha256: "19f95e9dfd5b0fe63751087137e13eb85bf1468d863fc281fb528dcabe32c5b0", wayback_url: "https://web.archive.org/web/20050325132000/http://toolkitzone.com/forums/viewtopic.php?p=179973&amp="}
links: []
---

# A problem with AVI's

### tsmpaul · 2005-03-10 07:13 · #B178498

Hi guys, I don't know if you're looking into this at the moment, or if developmental builds have addressed these issues, but I'm having AVI problems.
I ran a search about PlayAvi in the forum, but none of the answers people suggested did anything... I'm trying to play a movie in my game, in particular, during the Start.Prg as an introduction sequence when beginning a new game. There are a few bugs:
Firstly, if the game is running in fullscreen mode, it doesn't enlarge the movie to fill the screen, but plays it in its actual size in the top left corner of the screen. However, if I play the movie while running the game in windowed mode, the movie fills the whole screen.
Secondly: When a PlayAvi movie finishes playing, it freezes on the last frame of the movie, and you have to Alt-Tab or Ctrl-Alt-Del to get out of it, and manually close down the program. However, if you use PlayAviSmall, it plays the movie and continues with the game just like it should - but the movie flashes on and off while playing...

### Delano · 2005-03-13 15:58 · #B179890

Sorry for the delay there... hopefully all the movie issues should be resolved now - PlayAvi() will stretch the video to the size of the trans3 window (rather than full-screening in both windowed and fullscreen mode), and PlayAviSmall() will centre the video on the screen, playing it at it's own resolution. Trans3 shouldn't lock up now after the movie has finished, either.

### khaldore · 2005-03-13 16:08 · #B179895

Shocked This is great news...
I had originally planned a small .avi as the post-menu intro, but cut it out due to the problems listed in the initial post. Maybe now I can put it back in there and see how it looks, perhaps add a voiceover instead of displaing text on-screen. Mr. Green
EDIT: Mind you, this will require finding a different codec for it... 9mb for a 30-second clip (at 640x480) is a bit much. Razz

### tsmpaul · 2005-03-13 19:22 · #B179973

Awesome news! And the TK 3.06 is 93% finished - I can't wait to download it Smile
