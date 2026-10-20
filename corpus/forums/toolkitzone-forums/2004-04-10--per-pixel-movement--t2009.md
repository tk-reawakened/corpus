---
kind: forum-thread
id: "toolkitzone-forums/2009"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions &amp; bugs"
skin: "phpbb2"
thread_id: "2009"
title: "Per pixel movement"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=2009"
written: "2004-04-10T21:57:00"
last_post: "2004-08-15T07:18:00"
date_confidence: "exact"
captured: ["20040925162046"]
author: "Dash"
repliers: ["gcn_zelda", "Occasionally_Correct", "vUnit321", "Nick"]
authors: ["Dash", "gcn_zelda", "Occasionally_Correct", "vUnit321", "Nick"]
posts_present: 6
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_75755_amp_", captured: "20040925162046", sha256: "235159c527dc6861ad2ce3b1a0333fceefb31d527fa2d178a84fefda9a482a51", wayback_url: "https://web.archive.org/web/20040925162046/http://www.toolkitzone.com/forums/viewtopic.php?p=75755&amp="}
links:
  - {url: "http://cywh.com/ot/", status: "external", local: null}
  - {url: "http://rpgtoolkithole.000k2.com/images/antianti.png", status: "external", local: null}
  - {url: "http://saoghal.cywh.com/Stadsport/banner.gif", status: "external", local: null}
  - {url: "http://www.mg.geahost.com/small_theproject.gif", status: "external", local: null}
  - {url: "http://www.mozilla.org/products/firefox/", status: "external", local: null}
  - {url: "http://www.toolkitzone.com/games.php?game=482", status: "never-captured", local: null}
---

# Per pixel movement

### Dash · 2004-04-10 21:57 · #B20533

We really need this feature.
If anyone's played any of the newer snes square rpg's theyl notice the character's move pixel per pixel on the board.

### gcn_zelda · 2004-04-10 22:05 · #B20538

**Zerzic wrote:**

> We really need this feature.
> If anyone's played any of the newer snes square rpg's theyl notice the character's move pixel per pixel on the board.
>

Actually, usually it's around 4 pixels per step.
Pixel by pixel would be very slow. But it would still be better than 32 pixels per step.
It's a good suggestion.
_________________
.:: [Get Firefox!](http://www.mozilla.org/products/firefox/)::.
.:: [Off-Topicness!](http://cywh.com/ot/)::.
.::(redacted: email)::.
[
![](http://www.mg.geahost.com/small_theproject.gif)
![](http://rpgtoolkithole.000k2.com/images/antianti.png)

### Dash · 2004-04-10 22:38 · #B20553

**gcn_zelda wrote:**

>
> **Zerzic wrote:**
>
> > We really need this feature.
> > If anyone's played any of the newer snes square rpg's theyl notice the character's move pixel per pixel on the board.
> >
>
> Actually, usually it's around 4 pixels per step.
> Pixel by pixel would be very slow. But it would still be better than 32 pixels per step.
> It's a good suggestion.
>

Ok fine we need per 4 pixel movement then.

### Occasionally_Correct · 2004-04-11 12:26 · #B20695

**Zerzic wrote:**

>
> **gcn_zelda wrote:**
>
> >
> > **Zerzic wrote:**
> >
> > > We really need this feature.
> > > If anyone's played any of the newer snes square rpg's theyl notice the character's move pixel per pixel on the board.
> > >
> >
> > Actually, usually it's around 4 pixels per step.
> > Pixel by pixel would be very slow. But it would still be better than 32 pixels per step.
> > It's a good suggestion.
> >
>
> Ok fine we need per 4 pixel movement then.
>

Then people would stop complaining about the characters moving too fast. Because you'd have to go forward eight times to get across one tile. Razz
4 * 8 = 32. Perhaps it should be around 8 pixels per step, so it'd be 4 steps per pixel. That way, it wouldn't be too slow, but still look better than the 32 pixel-step.
Dunno. I'm just spitting random things out. Usually, my random things to say are useless. Razz
_________________
:: it's better in the matinee, the dark of the matinee ::

### vUnit321 · 2004-08-15 04:59 · #B75713

here's one way to look at it in an optimistic view.
you CAN have a 4 pixel step. here's how.
let's say your base character sprite is 32x32 and you want to walk 4 pixels instead of 32 pixel, which is your character sprite size.
32 / 4 = 8
so multiply 32 and 8 together = 256
so now, make your sprite size 256x256. now he is moving 32 pixels still but with the size ratio, it's the same with being 32x32 walking 4 pixels steps. Smile
_________________
[Initial D Midnight Showdown](http://www.toolkitzone.com/games.php?game=482)
- Overall 4%
- RPGCode 6%
- Storyline 1%
- Sprites/Gfx 7%
- Sounds/Music 5%
- Map/Board 2%

### Nick · 2004-08-15 07:18 · #B75755

It's already in the next release of TK anyway.
_________________
![](http://saoghal.cywh.com/Stadsport/banner.gif)
