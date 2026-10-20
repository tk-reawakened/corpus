---
kind: forum-thread
id: "toolkitzone-forums/12187"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "12187"
title: "Strip-based animations"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12187"
written: "2004-12-05T16:31:00"
last_post: "2004-12-08T23:08:00"
date_confidence: "exact"
captured: ["20050116235212"]
author: "Mystinar"
repliers: ["Nick", "catwhowalksbyhimself", "Dont_Think_So"]
authors: ["Mystinar", "Nick", "catwhowalksbyhimself", "Dont_Think_So"]
posts_present: 6
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_136647_amp_", captured: "20050116235212", sha256: "076347a78ebccd60bf25fcf1245bc30b658ce6005f433dc2d54c217893a075ef", wayback_url: "https://web.archive.org/web/20050116235212/http://www.toolkitzone.com/forums/viewtopic.php?p=136647&amp="}
links: []
---

# Strip-based animations

### Mystinar · 2004-12-05 16:31 · #B135076

I got an interesting idea on a new method for doing animations in the animation editor. You load a strip, and play the entire .anm file from that image. And what is a strip? Well, lan example would be four water tiles to be used in an animation. Each one is 32x32. To make them into a strip, you just take out the good old fashioned MS paint, make an image in that is 128 pixils wide and 32 tall, and then you put number one in, and then place each one, in order, one after the other. So, instead of having four files, you would just have one file. Disk space saved might be minimal, but at least your folders won't get cluttered up with images!
Yes, I realize this could be done in RPGcode, but it is likely to be slow.

### Nick · 2004-12-05 18:03 · #B135095

Yes, this is how every other game maker does it.

### catwhowalksbyhimself · 2004-12-05 19:16 · #B135139

It shouldn't be too hard to do this. Or even to let the editor generate these files itself from individual pictures or use premade strips. It would be much more organized.

### Mystinar · 2004-12-08 20:36 · #B136574

**catwhowalksbyhimself wrote:**

> It would be much more organized.
>

That's why I suggested it.

### Dont_Think_So · 2004-12-08 22:21 · #B136615

Actually, that "grab tiles" feature already lets you convert strips to tilesets.

### catwhowalksbyhimself · 2004-12-08 23:08 · #B136647

Yes, it does, but we are not talking about that.
