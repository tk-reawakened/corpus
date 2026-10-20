---
kind: forum-thread
id: "toolkitzone-forums/7303"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "7303"
title: "Toolkit Source code question"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=7303"
written: "2004-08-17T00:36:00"
last_post: "2004-08-28T15:39:00"
date_confidence: "exact"
captured: ["20040925162156"]
author: "vbgamer2"
repliers: ["Euix", "Deathy", "KSNiloc", "zzz", "Cyranoid", "Levi", "Marc"]
authors: ["vbgamer2", "Euix", "Deathy", "KSNiloc", "zzz", "Cyranoid", "Levi", "Marc"]
posts_present: 8
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_76792_amp_", captured: "20040925162156", sha256: "36ac30816e92a33a5b20b838e25323b75a0895cf95502596f1210e22b7d3bc3a", wayback_url: "https://web.archive.org/web/20040925162156/http://www.toolkitzone.com/forums/viewtopic.php?p=76792&amp="}
links:
  - {url: "http://img.photobucket.com/albums/v491/Diddums/banner.png", status: "external", local: null}
  - {url: "http://img55.exs.cx/img55/5484/Swordoffate.gif", status: "external", local: null}
  - {url: "http://img72.exs.cx/img72/6003/Link-AnimatedB.gif", status: "external", local: null}
  - {url: "http://img72.exs.cx/img72/610/Link-AnimatedLR.gif", status: "external", local: null}
  - {url: "http://img76.exs.cx/img76/421/Muahahahaha.jpg", status: "external", local: null}
  - {url: "http://img86.exs.cx/img86/3049/Link-Animated.gif", status: "external", local: null}
  - {url: "http://swordoffate.tk", status: "external", local: null}
  - {url: "http://www.jamesmurphy.tk", status: "external", local: null}
  - {url: "http://www.mr-diddums.tk", status: "external", local: null}
  - {url: "http://www.msanthrope.com/jamesmurphy/jmsite-bnr2.gif", status: "external", local: null}
  - {url: "http://www.rpgadev.com", status: "external", local: null}
  - {url: "http://www.rpgadev.com/sig.gif", status: "external", local: null}
  - {url: "http://www.toolkitzone.com/blog.php?user=Euix", status: "captured", local: "wayback/toolkitzone.com/blog.php__user_Euix"}
  - {url: "http://www.toolkitzone.com/games.php?game=9", status: "captured", local: "wayback/toolkitzone.com/games.php__game_9"}
  - {url: "http://www.your-poetry.com/modules.php?name=News&file=article&sid=39971", status: "external", local: null}
---

# Toolkit Source code question

### vbgamer2 · 2004-08-17 00:36 · #B76792

Hi,
I was looking at the rpgtoolkit v2.something source code and i saw in the global section under trans2. What does the dollar sign ($) mean?

**Code:**

```
 Global tempath$

Thanks.
```

### Euix · 2004-08-26 19:28 · #B82222

Just like in RPGCode, the dollar sign means it's a string. But that's a bad way to declare variable types in Visual Basic.
it SHOULD be..

**Code:**

```
Global tempath as String
```

Welcome. Razz
_________________
[My Blog!](http://www.toolkitzone.com/blog.php?user=Euix) | [My Game!](http://www.toolkitzone.com/games.php?game=9)

### Deathy · 2004-08-27 12:52 · #B82755

Well, How did a Guest post in here.....Its supossed to be for registered users....oh well...
_________________
Artist of The Month....
--------------------------------
[![](http://www.msanthrope.com/jamesmurphy/jmsite-bnr2.gif)](http://www.jamesmurphy.tk)
[![](http://img.photobucket.com/albums/v491/Diddums/banner.png)](http://www.mr-diddums.tk)
DeathSquad

### KSNiloc · 2004-08-27 17:06 · #B82841

Should be Public not global too,
_________________
Pawn.

### zzz · 2004-08-27 17:39 · #B82862

heheeh, i can post when i am a guest, i just am never a guest Razz
_________________
I'm still the sexiest!!!!!
"You're wrong. I know now, without a doubt, Kingdom Hearts...is
light!"- Sora
[![](http://img55.exs.cx/img55/5484/Swordoffate.gif)](http://swordoffate.tk)
The Link Sprite for My Game (LOZ:R)
![](http://img86.exs.cx/img86/3049/Link-Animated.gif)![](http://img72.exs.cx/img72/6003/Link-AnimatedB.gif)![](http://img72.exs.cx/img72/610/Link-AnimatedLR.gif)
Thanks to Khin for the avatar Wink

### Cyranoid · 2004-08-28 01:23 · #B83133

Visual Basic is evil. I learned that when going back to it attempting a graphic buffer.... It totaly sucks Razz. Now with c# its as simple as:
Image[] myBuffer = new Image[10]
Then when your ready for your buffer, or part of it, you can set the dimentions of it. From file or new image buffer Razz. Quite nice. VB is evil with image buffers...
_________________
- Cy -
[![](http://www.rpgadev.com/sig.gif)](http://www.rpgadev.com)

### Levi · 2004-08-28 12:37 · #B83438

Now come on, that's sort of harsh wouldn't you say? VB wasn't originally intended for extreme graphics use, or much graphics use at that. It was meant for ease of use in creating applications for the windows system. It later evolved to include such abilities and more but through addins and dlls and components. All the while keeping its main purpose. So yes extremely difficult for such things but not a bad thing to use. Especially if youknow what you are doing. Besides it makes some things easier.
Although I do wish C# was free. That language sounds like it would be so cool to have.
_________________
Levi
"Darkness hides the light
Darkness keeps me from it
Darkness is my life
Darkness I am in it"
"Light and Darkness my life is filled with thee
Light and Darkness my life my destiny
Light and Darkness both my life they share
Light and Darkness does no one care"
Quotes from "Who I am" by Levi
<http://www.your-poetry.com/modules.php?name=News&file=article&sid=39971>

### Marc · 2004-08-28 15:39 · #B83483

I know of a free C# editor and compiler. I don't remember the link, MT gave it to me.
_________________
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)
