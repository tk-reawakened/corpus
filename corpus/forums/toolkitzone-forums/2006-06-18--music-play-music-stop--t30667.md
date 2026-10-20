---
kind: forum-thread
id: "toolkitzone-forums/30667"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "RPG Code"
skin: "phpbb2"
thread_id: "30667"
title: "Music Play.. Music stop???"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=30667"
written: "2006-06-18T23:36:00"
last_post: "2006-06-19T23:33:00"
date_confidence: "exact"
captured: ["20060629083026"]
author: "Dragen"
repliers: ["Malegnis", "UltimaWizard"]
authors: ["Dragen", "Malegnis", "UltimaWizard"]
posts_present: 7
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_329004_amp_3Bsid_497143305248e29d431accf0730516d1", captured: "20060629083026", sha256: "3cdda9c96c80a3de28d25d52904ccf40efd0bb7894892cd555deb0f461a88613", wayback_url: "https://web.archive.org/web/20060629083026/http://www.toolkitzone.com/forums/viewtopic.php?p=329004&amp%3Bsid=497143305248e29d431accf0730516d1"}
links: []
---

# Music Play.. Music stop???

### Dragen · 2006-06-18 23:36 · #B328746

Okay. I've got some MP3 files that I want to play. First I want to play a file called Intro_1.mp3 then to seamlessly stop that and then play a file called Intro_2.mp3. I tried the following:

**Code:**

```
#MediaPlay("Intro_1.mp3")

#MediaStop("Intro_1.mp3")

#MediaPlay("Intro_2.mp3")
```

But this made a second gap where there was nothing playing.
Then I tried this:

**Code:**

```
#MediaPlay("Intro_1.mp3")

#MediaPlay("Intro_2.mp3")

#MediaStop("Intro_1.mp3")
```

I thought that this would play the first file, then the second and as the second started, the first would stop. Unfortunatly it stops both the files from playing.
Does anyone know a way in which I can make the first file stop and the second start, withought any noticable gap in the sound??
Please note that I am aware it seems pointless these two files starting and stopping right after the other, but that doesn't matter. There is a method to my madness Razz

### Malegnis · 2006-06-19 01:13 · #B328767

try giving more than a second betoween give it time to start up like ten seconds to be safe. and you can no play two sounds at once, it will automaticly stop the otehr one.

### Dragen · 2006-06-19 20:44 · #B328944

**Malegnis wrote:**

> and you can no play two sounds at once, it will automaticly stop the otehr one.
>

Yeah. I don't want to play them both at once. maybe I didn't explain myself clearly..
To try and solve complications I missed out some uneccassary code. I suppose if I'd left it in it would have made it clearer. In the actual program it's not just playing one then straight to another. There is a bit of time before I want the next music file to play. Hopefully that is clearer.
The problem is, when I set the next one to play and the first one to stop, there is a pause between them, when nothing is playing. What I'd like is if they kinda flowed into one another. Is there a way I can code it so that it wont have the gap between the files?
Note: The two files are actually taken from one larger music file, simply split in two, so they do go together. The Toolkit simply doesn't seem to play them without the pause while stopping one and starting another.
Wow, that was long winded Confused

### UltimaWizard · 2006-06-19 20:52 · #B328954

Or you could download Oyerth's FMod plugin. That gives support for multiple sounds at once as well as streamlined Play and Stop RPGCode commands.

### Dragen · 2006-06-19 20:56 · #B328957

Thanks! This seems to be exactly what I need! I'm gonna go muck about with it now Very Happy
Thankyou.

### UltimaWizard · 2006-06-19 21:01 · #B328961

No problem.
Also, if you're using larger-scale boards and want to use non-broken versions of PlayerLocation() and a couple of other commands, check out Caliber Mengsk's Trans3 update (also in the resources section). Until 3.0.7 comes out, it's the closest you're gonna get to a bugfix for those.

### Dragen · 2006-06-19 23:33 · #B329004

Thanks
