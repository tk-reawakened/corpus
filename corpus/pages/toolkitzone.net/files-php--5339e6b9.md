---
kind: page
id: "toolkitzone.net/toolkitzone.net/files.php?file=1763"
site: "toolkitzone.net"
title: "Date Added"
original_url: "http://toolkitzone.net/files.php?file=1763"
written: null
date_confidence: "unknown"
updated: null
captured: ["20101011080028"]
author: null
repliers: []
authors: []
comments_present: 0
f_category: "All Categories Audio | -- Background | -- Effects | -- Other Graphics | -- Animations | -- Battle Backgrounds | -- Other | -- Tilesets | -- | -- Buildings (Exterior) | -- | -- Buildings (Interior) | -- | -- Characters | -- | -- Collections | -- | -- Items | -- | -- Monsters | -- | -- Other | -- | -- Terrain RPG Code | -- Custom Systems | -- Methods | -- Other | -- Plugins"
f_downloads: "Juryiel Alpha 0.02 Thursday 9.47am, September 30th 2010 Thursday 9.57am, September 30th, 2010 13"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.net/files.php__file_1763", captured: "20101011080028", sha256: "8120b42967853fa9781fe7e6dc9a51f5931962933ee48e3c0999161ef91d2be2", wayback_url: "https://web.archive.org/web/20101011080028/http://toolkitzone.net/files.php?file=1763"}
---

# Date Added

Juryiel's Action RPG System
Juryiel Alpha 0.02 Thursday 9.47am, September 30th 2010 Thursday 9.57am, September 30th, 2010 13
A realtime action-adventure battle system similar to Zelda. It still runs at a fairly impressive rate (by RPG Toolkit standards). The speed gain, however, may be attributed to the fact that it's lacking in some much needed features. This bare-bones demo offers a player/enemy walking system and a basic attack system. It's far from being a drop-in solution as it's missing collision detecting and it's not easily customizable. Hopefully these issues will be addressed in future updates.
No votes cast.
I added collision detection (except enemy/player but that's trivial) and updated the file several days ago Not sure which one is uploaded thoughTBD
[![TBD](thumb.php?src=forum/images/avatars/9872561424b5ab1f09a7f9.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=14726)
I'm talking about being able to walk through enemies.
Oh sorry that was more of a changelog post And I intend to keep the enemy thing that way, but add damage and a small knockback in a random direction (not enough to counter the full movement) to it.TBD
[![TBD](thumb.php?src=forum/images/avatars/12284569474c555ef3c884d.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=7660)
Pretty Cool but I dont like the way enemies overlap the player, like when they stand on your headTBD
I am currently working on a Z order function that will work by getting the bottom y of each sprite, and using that to determine the drawing order. That way, sprites with higher bottomY will be drawn on top of ones with lower bottomY. This should effectively flip which sprite is over the otehr based on where the sprite's feet are, and should eliminate this problem.
[![TBD](thumb.php?src=forum/images/avatars/12284569474c555ef3c884d.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=7660)
That would be awesome because then I could steal your Z buffer
Juryiel wrote:
> I am currently working on a Z order function that will work by getting the bottom y of each sprite, and using that to determine the drawing order. That way, sprites with higher bottomY will be drawn on top of ones with lower bottomY. This should effectively flip which sprite is over the otehr based on where the sprite's feet are, and should eliminate this problem.
>
TBD
