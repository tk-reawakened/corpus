---
kind: forum-thread
id: "toolkitzone-forums/27014"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Toolkit Discussion"
skin: "phpbb2"
thread_id: "27014"
title: "I need some help on making mazes"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=27014"
written: "2006-01-31T23:18:00"
last_post: "2006-02-05T06:03:00"
date_confidence: "exact"
captured: ["20060213005301", "20060224225919", "20060306024728", "20060306024800", "20060306024927", "20060306025015", "20060306025133"]
author: "Linkmaster2001"
repliers: ["hhh", "vrn790", "zyrshnikashnu", "Occasionally_Correct"]
authors: ["Linkmaster2001", "hhh", "vrn790", "zyrshnikashnu", "Occasionally_Correct"]
posts_present: 6
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_294094_amp_3Bsid_0beff7dfe008648c55ca7ab4d20995ef", captured: "20060306024728", sha256: "245de6222e5011f09317b0fcba388db2eff1635457b794a5fc1119a7a7c20154", wayback_url: "https://web.archive.org/web/20060306024728/http://toolkitzone.com/forums/viewtopic.php?p=294094&amp%3Bsid=0beff7dfe008648c55ca7ab4d20995ef"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_294127_amp_3Bsid_0beff7dfe008648c55ca7ab4d20995ef", captured: "20060306024800", sha256: "9998078bc1a765f2615391431abdc007564af079b47fc9a1e69bcccfe4970d94", wayback_url: "https://web.archive.org/web/20060306024800/http://toolkitzone.com/forums/viewtopic.php?p=294127&amp%3Bsid=0beff7dfe008648c55ca7ab4d20995ef"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_295012_amp_3Bsid_0beff7dfe008648c55ca7ab4d20995ef", captured: "20060306024927", sha256: "789da3d92219ec2c20210d0dc7b3e866e1c192e81c5ca61440ce726aa383be26", wayback_url: "https://web.archive.org/web/20060306024927/http://toolkitzone.com/forums/viewtopic.php?p=295012&amp%3Bsid=0beff7dfe008648c55ca7ab4d20995ef"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_295020_amp_3Bsid_0beff7dfe008648c55ca7ab4d20995ef", captured: "20060306025015", sha256: "ad82e6f340f936be9d3bf87bd89084323cf755da8a44562a0febe3e5c9c1bcf4", wayback_url: "https://web.archive.org/web/20060306025015/http://toolkitzone.com/forums/viewtopic.php?p=295020&amp%3Bsid=0beff7dfe008648c55ca7ab4d20995ef"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_295238_amp_3Bsid_0beff7dfe008648c55ca7ab4d20995ef", captured: "20060306025133", sha256: "cbd4a24d9ffc216e45da83f3808fddb33b37f269e1d0ee63ade21b87edfbd0a0", wayback_url: "https://web.archive.org/web/20060306025133/http://toolkitzone.com/forums/viewtopic.php?p=295238&amp%3Bsid=0beff7dfe008648c55ca7ab4d20995ef"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_295253", captured: "20060224225919", sha256: "ffaa3b88ba9a3723ef6490a4d598118a72e032d050880038ccc089ad7ad26563", wayback_url: "https://web.archive.org/web/20060224225919/http://toolkitzone.com/forums/viewtopic.php?p=295253"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_295253_amp_3Bsid_125a611e962141c45299d3c172df313f", captured: "20060213005301", sha256: "2f6d6c9fa13cc5ab2e1fdb570ca7c085a1ac907564334c99f7091bdc1d506d15", wayback_url: "https://web.archive.org/web/20060213005301/http://toolkitzone.com/forums/viewtopic.php?p=295253&amp%3Bsid=125a611e962141c45299d3c172df313f"}
links:
  - {url: "http://www.toolkitzone.com/stuff/files/226/keyDown.dll", status: "captured", local: "wayback/toolkitzone.com/stuff/files/226/keyDown.dll"}
---

# I need some help on making mazes

### Linkmaster2001 · 2006-01-31 23:18 · #B294094

If i where to make a maze, and i wanted to be able to move boulders in the maze. How would i do that or is that possible?

### hhh · 2006-02-01 01:42 · #B294127

I'll try to make this simple.
Yes and No.
You would have to know the direction the character is facing. If you can
in someway I don't know of because I have stopped using toolkit a while back but still answer forums occasionally.
If you can get the direction when they step on a specific tile, you can have them automatically push the boulder using this.
push("character",(N,E,S,W))
pushitem(boulder.itm, (W,E,S,N))
To push the character and then the boulder. It might look though as if he walked into the boulder then the boulder moving though.
I have no idea of knowing the direction the character is facing.
You could set it up to do that only when stepping on a specific tile like I said.
If you want to do it like pokemon's strength move, you better figure out how to get a player's facing.
I remember seeing somewhere that one of Mr.G's plugins let you do this but I'm not sure.
I hope this answered your question.

### vrn790 · 2006-02-04 17:19 · #B295012

Yeah, there is a plugin for that. But thats not the only way. You could also use the playerx[] and playery[] variables to get the players coordinates (TK3 only!) and then you can use itemlocation to get the items coordinates. From there, you can figure out on which side of the boulder the player is standing Smile

### zyrshnikashnu · 2006-02-04 18:00 · #B295020

Adding to that, you can use a thread to get the player's coordinates. I've got an extremely simple one that seems to work fairly well, which I shall provide here:

**Code:**

```
while (true)

{

   if (keyDown("LEFT"))

   {

      dir$ = "West"

   }

   if (keyDown("RIGHT"))

   {

      dir$ = "East"

   }

   if (keyDown("UP"))

   {

      dir$ = "North"

   }

   if (keyDown("DOWN"))

   {

      dir$ = "South"

   }

}
```

### vrn790 · 2006-02-05 05:03 · #B295238

Eh? am i missing out on something? There's a command called keydown?

### Occasionally_Correct · 2006-02-05 06:03 · #B295253

No, but there is a [plugin](http://www.toolkitzone.com/stuff/files/226/keyDown.dll) that'll allow you to use it. Smile
