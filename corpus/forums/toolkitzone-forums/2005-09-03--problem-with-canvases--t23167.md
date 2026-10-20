---
kind: forum-thread
id: "toolkitzone-forums/23167"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Code"
skin: "phpbb2"
thread_id: "23167"
title: "Problem with canvases"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=23167"
written: "2005-09-03T18:15:00"
last_post: "2005-09-03T19:33:00"
date_confidence: "exact"
captured: ["20051212121252", "20051212121320", "20060108042322"]
author: "Dragen"
repliers: ["Dont_Think_So"]
authors: ["Dragen", "Dont_Think_So"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_253467_amp_3Bsid_f159bf35788486cdb97f50bd9c7569a4", captured: "20051212121252", sha256: "6c5ca78d22111b233f1ad6a4d5952d235254d35bbe49b79e6b86f3b72236eff4", wayback_url: "https://web.archive.org/web/20051212121252/http://www.toolkitzone.com/forums/viewtopic.php?p=253467&amp%3Bsid=f159bf35788486cdb97f50bd9c7569a4"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_253479_amp_3Bsid_f159bf35788486cdb97f50bd9c7569a4", captured: "20060108042322", sha256: "14c0590620a3dbf1de0c93dcb4764043791294af408cc0819465163a6aee19ef", wayback_url: "https://web.archive.org/web/20060108042322/http://www.toolkitzone.com/forums/viewtopic.php?p=253479&amp%3Bsid=f159bf35788486cdb97f50bd9c7569a4"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_253486_amp_3Bsid_f159bf35788486cdb97f50bd9c7569a4", captured: "20051212121320", sha256: "d5bc1795d5f909b626874bcfbb696778d5288243d250e8d73d61426036f3a5ab", wayback_url: "https://web.archive.org/web/20051212121320/http://www.toolkitzone.com/forums/viewtopic.php?p=253486&amp%3Bsid=f159bf35788486cdb97f50bd9c7569a4"}
links: []
---

# Problem with canvases

### Dragen · 2005-09-03 18:15 · #B253467

Ok. What am I doing wrong.. I know all the variables etc are right and work fine, I've tested them, so don't say anything about them...
The problem is if I run the prg it brings up the text and and the seconds tick away, but it doesn't delete the previous seconds, so they overlapp and you can't read it. How do I get it so it deletes the previous Clockseconds$ (And all the other variable) and the re-writes the new ones in?
This is the code:

**Code:**

```
font("Evanescence")

font-colorrgb(255,255,255)

fontsize(23)

#Text(37.5,3.5,"<Clockhours$>:<Clockminutes$>   <Clockseconds$>", cnvTimer!)

#Text(41.3,3.5,"am", cnvTimer!)

#Text(39.3,5.8,"<Day[Clockday!]$>", cnvTimer!)

#Text(39.3,7,"<Month[Clockmonth!]$>", cnvTimer!)

#Text(39.3,9,"week: <Clockweek$>", cnvTimer!)

drawCanvas(cnvTimer!, 0, 0)
```

### Dont_Think_So · 2005-09-03 18:49 · #B253479

**Code:**

```
font("Evanescence")

colorrgb(0, 0, 0)

fillrect(0, 0, 640, 480, cnvTimer!)

font-colorrgb(255,255,255)

fontsize(23)

#Text(37.5,3.5,"<Clockhours$>:<Clockminutes$>   <Clockseconds$>", cnvTimer!)

#Text(41.3,3.5,"am", cnvTimer!)

#Text(39.3,5.8,"<Day[Clockday!]$>", cnvTimer!)

#Text(39.3,7,"<Month[Clockmonth!]$>", cnvTimer!)

#Text(39.3,9,"week: <Clockweek$>", cnvTimer!)

drawCanvas(cnvTimer!, 0, 0)
```

You'll notice I just filled the background with black. If you want a different color or an image instead, you will need to change the code accordingly.
If you decide to use an image, a faster way than calling bitmap every time is to a canvas once:
cnvMenuBackground! = createCanvas(640, 480)
bitmap("bkg.jpg", cnvMenuBackground!)
Then you can draw the canvas over to the cnvTimer! one. This way, the image is already loaded into memory and it draws much, much faster.

### Dragen · 2005-09-03 19:33 · #B253486

Thanks Very Happy I tried it, but it didn't seemto do anything (even when I changed the colour to white).. heh.. So I tried it with a pic instead and that worked. It stopped the numbers layering each other. Thankyou!!! Very Happy
I'm not quite sure why it worked though... Is it because layers automatically re-render themselves or something, so it places the pic over the previous clock time, then puts the new one over the top????
