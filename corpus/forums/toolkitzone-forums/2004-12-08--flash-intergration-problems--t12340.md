---
kind: forum-thread
id: "toolkitzone-forums/12340"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12340"
title: "Flash intergration problems"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12340"
written: "2004-12-08T23:26:00"
last_post: "2004-12-08T23:26:00"
date_confidence: "exact"
captured: ["20041227215422"]
author: "solaceinsilence"
repliers: []
authors: ["solaceinsilence"]
posts_present: 1
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_136654_amp_", captured: "20041227215422", sha256: "4f866326e6600128979d7200b682a6926c5a3d5807ced5b7639b5724d6be9e5d", wayback_url: "https://web.archive.org/web/20041227215422/http://www.toolkitzone.com/forums/viewtopic.php?p=136654&amp="}
links: []
---

# Flash intergration problems

### solaceinsilence · 2004-12-08 23:26 · #B136654

Hello, I am currently working on a game for the RPGToolkit using the 3.0.4 release. I created a flash intro for my game and added it with the following code

**rpgcode:**

```
SetFlashMovie(0, "intro.swf", 0, 0, 640, 480)

SWF_Play(0)

swfFSCommand[0]$ = "auto"

Method StartGame()

{

     SWF_Remove(0)

}
```

In the flash movie itself, i also put this FSCommand

**Code:**

```
onFrame (725) {

    fscommand("#StartGame()","");

}
```

Now I am using SwishMax, which is why the fscommand syntax looks as it does. the syntax is fscommand(command, argument). Ok well i have two problems. One when the movie starts playing it glichs and doesnt take up the width! and height! that i specified. Instead, it gradually fills up the space as my animations in the flash movie play. Secondly, after the movie is finished it loops. When it should remove itself from the screen and allow the user to begin playing that game. I would like it if anyone could help me out with this, or if anyone has had similar problems with this before Rolling Eyes
