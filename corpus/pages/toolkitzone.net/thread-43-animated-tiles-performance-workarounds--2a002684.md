---
kind: page
id: "toolkitzone.net/toolkitzone.net/thread/43/animated-tiles-performance-workarounds"
site: "toolkitzone.net"
title: "Welcome Guest. Please or . Login Register"
original_url: "http://toolkitzone.net/thread/43/animated-tiles-performance-workarounds"
written: null
date_confidence: "unknown"
updated: null
captured: ["20170303134515"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.net/thread/43/animated-tiles-performance-workarounds", captured: "20170303134515", sha256: "b1e01197da859ee847385aec33f297c8b5f03a6c53a0da8e002f3ae4c88c1ba7", wayback_url: "https://web.archive.org/web/20170303134515/http://toolkitzone.net/thread/43/animated-tiles-performance-workarounds"}
---

# Welcome Guest. Please or . Login Register

[![Toolkitzone](//storage.proboards.com/6485149/images/7gAH7AdAG8qWcbWHeVa5.png)](/)
-
-
-
- [ Toolkitzone
- [ News
- [ Welcome
- [ Site Suggestions
- [ RPG Toolkit 4.x
- [ News
- [ Discussion
- [ Complete Games
- [ Incomplete Games
- [ Support
- [ Tutorials
- [ RPG Toolkit 3.x
- [ Complete Games
- [ Incomplete Games
- [ Support
- [ Tutorials
- [ Resources
- [ Graphics
- [ Music & Sound Effects
- [ Plugins
- [ Other Game Development Systems
- [ Complete Games
- [ Incomplete Games
- [ General
- [ General Discussion
- [ Gaming
- [ My Things
![*](//storage.proboards.com/6485149/images/y7IhFg8NjD3OKcbIt3rP.png)
![deiss Avatar](//storage.proboards.com/6485149/avatar/MFliEJHSKj3dU0MY7_6t.gif)
Posts: 8
[Animated tiles performance and workarounds?](/thread/43/animated-tiles-performance-workarounds) Aug 6, 2016 14:37:28 GMT -5
Post by deiss on Aug 6, 2016 14:37:28 GMT -5
Hi folks. Been messing about with 3.2.1, got a couple of ideas rattling around upstairs. Anyway, while poking around the editor I've run into a wee issue. I can set up animated tiles just fine, but if there's more than say 6 on a board, performance starts tanking horribly. I ran into this trying to animate water on a test board. I've tried using a large tile bitmap item on a low layer to work around it, thinking that maybe it was an issue with timekeeping with a lot of separate animated tiles, but that didn't help at all. My next cunning plan was to set up a set of canvases, and just blit them in sequence in a board thread. The good news is, the basic idea seems to be sound - this eliminates the performance issue, but raises two more. 1) Is there a timekeeping function I can use to limit the threads' frame rate? 2) Is it possible to blit a canvas on to a low layer, instead of the cnvRenderNow layer on top of everything? I think I can work around (2) with some crazy shenanigans. If I set the background colour to hot pink and use transparent tiles instead of water, in theory I can copy the frame into canvas TEMP, draw the water onto a canvas WORK, blit TEMP over WORK with drawCanvasTransparent, then blit all that onto rendernow. Any better ideas?
![Cuthalion Avatar](//storage.proboards.com/6485149/avatar/8_9wfZRfi__oYb4moQo3.jpg)
Posts: 52
[Animated tiles performance and workarounds?](/thread/43/animated-tiles-performance-workarounds) Aug 6, 2016 15:18:14 GMT -5
Post by Cuthalion on Aug 6, 2016 15:18:14 GMT -5
1) I believe there is a function to get the current time in milliseconds (I think it's precise to 8ms last I measured, and that may vary by system). I don't recall its name, sadly. I believe there's also a plugin Xavier released that lets you set up timers to fire off stuff on a regular basis. Shao might know where you could find that, as (s)he's our unofficial eldritch archivist. 2) I'm not sure, but I believe canvases can go on top of each other based on the order they are drawn. This may not help if your goal is to draw below tiles. Also, you aren't limited to just the cnvRenderNow canvas. Also also, there is a function to copy the screen to a canvas (cnvGetScreen?), which you may find useful.
by Last Edit: Aug 6, 2016 15:19:18 GMT -5 [Cuthalion](/user/7)
![*](//storage.proboards.com/6485149/images/y7IhFg8NjD3OKcbIt3rP.png)
![deiss Avatar](//storage.proboards.com/6485149/avatar/MFliEJHSKj3dU0MY7_6t.gif)
Posts: 8
[Animated tiles performance and workarounds?](/thread/43/animated-tiles-performance-workarounds) Aug 6, 2016 17:31:18 GMT -5
Post by deiss on Aug 6, 2016 17:31:18 GMT -5
Yeah, I've found the screengrab function. Unfortunately, that plan didn't pan out - introduced a tonne of flickering that couldn't be resolved. The solution I'm working with at the moment has eliminated the flickering issue completely, and I'm up from ~1fps to ~42fps, so huge improvement there. Basically, I'm using a modified copy of the board as a mask (1 layer, 2 colours), and using viewBRD to load that into a canvas. That's acting as a mask for the animated water, which can then be dropped into cnvRenderNow without the flickering issues. The limitation doing it this way is that I'm currently limited to single screen maps when using it, and can't use this to animate anything sprites can cross. If I could blit a canvas onto a lower layer, that would eliminate the second limitation and allow me to use the same technique for grass, etc. That said, I'm not sure the engine would allow it. Going to have another player with items/sprites in a bit and see if I can figure something out there - maybe loading from a single big bitmap instead of a tile bitmap? If not, I'll stick with what I've got.
Guest Shao
![Guest Avatar](http://s5149.storage.proboards.com/6485149/a/n3wRLBmaUFtlA5lEEUBU.png)
[Animated tiles performance and workarounds?](/thread/43/animated-tiles-performance-workarounds) Aug 6, 2016 18:05:18 GMT -5
Post by on Aug 6, 2016 18:05:18 GMT -5
May not be relevant now, but to tag in for Cuthalion, GetTickCount() is the function and xLib.Timers the plugin. ThreadSleep() would have done the trick though. But to revisit your idea of using an item with an idle animation, a call to SpriteTranslucency(0) may resolve performance issues there.
![Cuthalion Avatar](//storage.proboards.com/6485149/avatar/8_9wfZRfi__oYb4moQo3.jpg)
Posts: 52
[Animated tiles performance and workarounds?](/thread/43/animated-tiles-performance-workarounds) Aug 6, 2016 18:07:16 GMT -5
Post by Cuthalion on Aug 6, 2016 18:07:16 GMT -5
Yeah, I wish I could remember exactly how I did it. I think I saved the screen to a canvas first thing, as soon as a fight started. Then every frame, I'd draw that first, than the other stuff on top of it, then flip/display the results at the very end to avoid flicker. But I wasn't walking around on normal boards for that. On the plus side, the early versions of the engine rewrites people have been demoing (browse around on these forums) have apparently had better performance. A big issue with TK3 is that performance varies dramatically from computer to computer, with no rhyme or reason. And of course, TK4 will be out in Octember. Edit: Oh hey, it's Shao!
by Last Edit: Aug 6, 2016 18:08:03 GMT -5 [Cuthalion](/user/7)
![*](//storage.proboards.com/6485149/images/y7IhFg8NjD3OKcbIt3rP.png)
![deiss Avatar](//storage.proboards.com/6485149/avatar/MFliEJHSKj3dU0MY7_6t.gif)
Posts: 8
[Animated tiles performance and workarounds?](/thread/43/animated-tiles-performance-workarounds) Aug 6, 2016 19:21:45 GMT -5
Post by deiss on Aug 6, 2016 19:21:45 GMT -5
That SpiteTranslucency trick worked perfectly - muchos gracias. Looks like performance still tanks if an edge of the item drops off the edge of the map, but that's easy enough to avoid. No problems with walking over them either with that approach - looks like I'll be able to go mad with animated backgrounds after all. Thanks again.
>
> May not be relevant now, but to tag in for Cuthalion, GetTickCount() is the function and xLib.Timers the plugin. ThreadSleep() would have done the trick though. But to revisit your idea of using an item with an idle animation, a call to SpriteTranslucency(0) may resolve performance issues there.
>
>
![:)](//storage.proboards.com/6485149/images/bed0tKwtj8NvFSLwGpkw.png)
Guest Shao
![Guest Avatar](http://s5149.storage.proboards.com/6485149/a/n3wRLBmaUFtlA5lEEUBU.png)
[Animated tiles performance and workarounds?](/thread/43/animated-tiles-performance-workarounds) Aug 7, 2016 13:52:02 GMT -5 via mobile
Post by on Aug 7, 2016 13:52:02 GMT -5
Happy I could help!![:)](//storage.proboards.com/6485149/images/bed0tKwtj8NvFSLwGpkw.png)
This Forum Is Hosted For FREE By Get Your Own !
