---
kind: file
id: "toolkitzone.com/1503"
site: "toolkitzone.com"
title: "Click to enlarge"
original_url: "http://toolkitzone.com/files.php?file=1503"
written: null
date_confidence: "unknown"
updated: null
captured: ["20100210140245"]
author: "Shao"
repliers: []
authors: ["Shao"]
comments_present: 0
uploader: "Shao"
f_category: "All Categories Audio | -- Background | -- Effects | -- Other Graphics | -- Animations | -- Battle Backgrounds | -- Other | -- Tilesets | -- | -- Buildings (Exterior) | -- | -- Buildings (Interior) | -- | -- Characters | -- | -- Collections | -- | -- Items | -- | -- Monsters | -- | -- Other | -- | -- Terrain RPG Code | -- Custom Systems | -- Methods | -- Other | -- Plugins"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/files.php__file_1503", captured: "20100210140245", sha256: "e36ada9bcae69e19c19ff6afeedd9c6a17c75e1494d6506906532ba29e9234ca", wayback_url: "https://web.archive.org/web/20100210140245/http://toolkitzone.com/files.php?file=1503"}
---

# Click to enlarge

32-bit Image Support
This plugin greatly improves the toolkit's abilities in setting images to the screen. It includes support for over a hundred different formats, supports alpha channels, and comes with the ability to accomplish many different effects in only fractions of a second! This is definitely a must-have plugin for anyone who wants to accomplish rich graphical effects in their toolkit game. Please note this plugin uses DLLs that disallow any game that uses it to be distributed commercially! NON-COMMERCIAL USE ONLY!
*5 votes cast.*
[![TBD](thumb.php?src=forum/images/avatars/12415846514b67f226152d5.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=141)
Hmmm whenever I work on Colony next I better tinker with this, see what I can do
[![TBD](thumb.php?src=forum/images/avatars/2139021133495ac85b3eeee.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=15959)
This here thingy may even Help my games look good.
[![TBD](thumb.php?src=forum/images/avatars/18352407164a8c65dda89e9.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=13905)
Thanks dude! You just saved my game!TBD
[![TBD](thumb.php?src=forum/images/avatars/141533142444a77edcc4491.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=9987)
This seems to bugger up with pixel text horribly.. Is there a work around that any is aware of? The plugin is very good though. I've spent the morning adding alpha mapped drop shadows to everything..
[![TBD](thumb.php?src=forum/images/avatars/107978653144bda65667c1e.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=84)
Uh, so what does this actually do apart from not work? I was quite excited to finally see alpha channel support but I simply cannot get it working. _____ id0! = spGrLoadFromFile("\bmp001\bmp001a.PNG") spGrDraw(id0!, 0, 0) spGrKill(id0!) _____ this snippet simply loads the image but doesn't load the alpha channel and the bits that are supposed to be transparent just show up as black.
It works for me, EB. I think there is a specifif function in the plugin for doing an alpha blend as opposed to just drawing, but I don't remember. "Please note this plugin uses DLLs that disallow any game that uses it to be distributed commercially! NON-COMMERCIAL USE ONLY!" The non-free component in the plugin actually disallows ALL use since it says it may not be used to make components for other developers to use, which is what Shao has done. I wasn't going to bring this up, but you felt the need to offer incorrect advice, so I've corrected it.
[![TBD](thumb.php?src=forum/images/avatars/14362985504898e6fa74d0d.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=17132)
Thx, ShaoTBD
[![TBD](thumb.php?src=forum/images/avatars/20515787084a57f7c9b6f3c.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=1384)
Wow. Is this a miracle? I never thought I'd see the day where there were alpha channels in TK. I haven't used the plugin though yet, but the readme sure looks promising. I can't wait to use it in future projects though - right now I'm just finishing up 3GNB - man, pretty exciting. Thanks. Update: So far, this plugin works wonders. Images are drawn considerably faster from my tests so far, and of course, alpha capabilities are a huge leap forward. Awesome plugin.
I´m New here with a great project in mind, working on my game since a year, (i have ALL the media stuff ready)but when made tests on TK my graphics shown errors like transparent areas....now it works perfect with your plugin....THANK YOU my friend!!!!!!!!!!! You save my project Long Live TK zone!!!!!haha
[![TBD](thumb.php?src=forum/images/avatars/13993740424a7dd268b68fa.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=4177)
**Update: I have to advise against using this plugin. Over the year, issues have surfaced regarding its compatibility with Vista and possibly some XP systems.** I always knew it was a bad idea to release an unfinished product, but at the time I was high on the thought of contributing to such high caliber projects as Vii and Of Rage and War... little did I know, I was actually hurting these games with my little "contribution". I considered it to be a temporary solution during the wait for 3.1.0, which I (mistakenly) assumed would contain similar functionality. I'll see about removing it from the site, to spare prospective developers any future heartache. I should mention, I think I actually know how to fix the bug. But due to limitations with the plugin callbacks, it would entail copying the entire screen regardless of how much actually needs to be drawn, effectively crippling the plugin's performance.
[![TBD](thumb.php?src=forum/images/avatars/15766365204a3fd5d4bbda7.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=14417)
for the last time people i tried this with vista it worksTBD
[![TBD](thumb.php?src=forum/images/avatars/13993740424a7dd268b68fa.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=4177)
xenxe, I don't want to be mean, really, but why should I value your report more than that of EB and several others? Have you tried to break it, tried to expose it to different test cases, different video drivers, different hardware? How can you be so sure it works 100% just because it works for you? I know you're just trying to be helpful, and I thank you for your report. But this is a plugin meant for distribution with users' games to their audience. If it doesn't work fully for even 10% of these people, then I'd argue it is insufficient for its intended purpose, and should not be used unless you're making games just for yourself. By the way, the bug in question occurs when you try to draw an alpha-enabled image to the screen (not a canvas). The transparent areas sometimes show as black. Running this code should show no black at all: ColorRGB(255, 0, 0); FillRect(0, 0, 640, 480); id = spGrLoadFromFile("orb.png"); spGrSetAlpha(id, 0.5); spGrDraw(id, 10, 10); Wait(); spGrKill(id);
