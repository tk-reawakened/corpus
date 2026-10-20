---
kind: page
id: "toolkitzone.net/toolkitzone.net/thread/35"
site: "toolkitzone.net"
title: "Welcome Guest. Please or . Login Register"
original_url: "http://toolkitzone.net/thread/35"
written: null
date_confidence: "unknown"
updated: null
captured: ["20170303134050"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.net/thread/35", captured: "20170303134050", sha256: "f21db98ee7b277cf43e7b0fd3ca496b4cce7e587668c3aee800d389a8942f472", wayback_url: "https://web.archive.org/web/20170303134050/http://toolkitzone.net/thread/35"}
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
I forgot who created it... Running from Flash Drive Troubles
rpg17
![rpg17 Avatar](http://s5149.storage.proboards.com/6485149/a/n3wRLBmaUFtlA5lEEUBU.png)
Posts: 0
[I forgot who created it... Running from Flash Drive Troubles](/thread/35/forgot-created-running-flash-troubles) Jun 11, 2016 15:56:22 GMT -5
Post by rpg17 on Jun 11, 2016 15:56:22 GMT -5
Well, here is the problem: I'm trying to run the rpg toolkit 3.2.1 from a flash drive on a no admin access computer (public library). Someone on rpg toolkit.net posted a fix for the trans3 and editor that would allow it to work but... I don't have a clue who it was and can't search the forum obviously. :/ If anyone could help me in some way I'd greatly appreciate it.
Guest Shao
![Guest Avatar](http://s5149.storage.proboards.com/6485149/a/n3wRLBmaUFtlA5lEEUBU.png)
[I forgot who created it... Running from Flash Drive Troubles](/thread/35/forgot-created-running-flash-troubles) Jul 15, 2016 5:18:38 GMT -5
Post by on Jul 15, 2016 5:18:38 GMT -5
That would be me! :p No-admin Toolkit3: If you don't use any plugins, Trans3 shouldn't require admin access. As a fallback, you can try my build here: If you do need plugin support, I know of a possible fix.
[www.mediafire.com/download/t0ared7frbp6caw/toolkit3.321.editedmanifest.packed.exe.zip](http://www.mediafire.com/download/t0ared7frbp6caw/toolkit3.321.editedmanifest.packed.exe.zip)
[shaodrop.nfshost.com/misc/rpgtoolkit/trans3.mumu.zip](http://shaodrop.nfshost.com/misc/rpgtoolkit/trans3.mumu.zip)
rpg17
![rpg17 Avatar](http://s5149.storage.proboards.com/6485149/a/n3wRLBmaUFtlA5lEEUBU.png)
Posts: 0
[I forgot who created it... Running from Flash Drive Troubles](/thread/35/forgot-created-running-flash-troubles) Jul 24, 2016 19:07:53 GMT -5 via mobile
Post by rpg17 on Jul 24, 2016 19:07:53 GMT -5
Thanks shao Why not try to fix the plugin problem and release your flash drive patch? That way we at least have a release. >.<![:D](//storage.proboards.com/6485149/images/NVnxz5kJDjGvY6S0Az1D.png)
Guest Shao
![Guest Avatar](http://s5149.storage.proboards.com/6485149/a/n3wRLBmaUFtlA5lEEUBU.png)
[I forgot who created it... Running from Flash Drive Troubles](/thread/35/forgot-created-running-flash-troubles) Jul 26, 2016 16:42:32 GMT -5
Post by on Jul 26, 2016 16:42:32 GMT -5
Not sure if the plugin fix even works, but I'll look into it!
rpg17
![rpg17 Avatar](http://s5149.storage.proboards.com/6485149/a/n3wRLBmaUFtlA5lEEUBU.png)
Posts: 0
[I forgot who created it... Running from Flash Drive Troubles](/thread/35/forgot-created-running-flash-troubles) Aug 21, 2016 14:27:59 GMT -5 via mobile
Post by rpg17 on Aug 21, 2016 14:27:59 GMT -5
Thanks I'll be needing the hotspot plugin to work. Trying to make tiles for city of yodel ATM. So far... They suck.
Guest Shao
![Guest Avatar](http://s5149.storage.proboards.com/6485149/a/n3wRLBmaUFtlA5lEEUBU.png)
[I forgot who created it... Running from Flash Drive Troubles](/thread/35/forgot-created-running-flash-troubles) Aug 22, 2016 20:20:40 GMT -5
Post by on Aug 22, 2016 20:20:40 GMT -5
Nice to hear you're still working on City Of Yo'Dell. I put together a test for the plugin fix. Grab it here, and verify whether clicking the red rectangles triggers the hotspot: Fingers crossed!![:)](//storage.proboards.com/6485149/images/bed0tKwtj8NvFSLwGpkw.png)
[www.mediafire.com/download/9ekih2ncuut6a92/ManifestTest.zip](http://www.mediafire.com/download/9ekih2ncuut6a92/ManifestTest.zip)
rpg17
![rpg17 Avatar](http://s5149.storage.proboards.com/6485149/a/n3wRLBmaUFtlA5lEEUBU.png)
Posts: 0
[I forgot who created it... Running from Flash Drive Troubles](/thread/35/forgot-created-running-flash-troubles) Aug 23, 2016 11:10:58 GMT -5
Post by rpg17 on Aug 23, 2016 11:10:58 GMT -5
I gave it a shot. No debugger pop up. However, if you add a drawrect to the onclick function that will show when you click a box Basically: Yes it works, but debugger doesn't want to show up. I ran it from .gam I haven't tested it from the toolkit test program thingy. So far it seems to work fine. Thank's Shao!
![:)](//storage.proboards.com/6485149/images/bed0tKwtj8NvFSLwGpkw.png)
Guest Shao
![Guest Avatar](http://s5149.storage.proboards.com/6485149/a/n3wRLBmaUFtlA5lEEUBU.png)
[I forgot who created it... Running from Flash Drive Troubles](/thread/35/forgot-created-running-flash-troubles) Aug 24, 2016 0:15:33 GMT -5
Post by on Aug 24, 2016 0:15:33 GMT -5
Thanks for giving it a go. That's weird. Does Debugger() work outside onclick? BTW, I uploaded the Hotspots readme: And just to cover all the bases, don't forget to change the project dir in "xLibHotspots.dll.x.manifest", and make sure to keep trans3.tlb in the same directory as the exe.
[shaodrop.nfshost.com/misc/rpgtoolkit/xLib.Hotspots.Readme.pdf](http://shaodrop.nfshost.com/misc/rpgtoolkit/xLib.Hotspots.Readme.pdf)
rpg17
![rpg17 Avatar](http://s5149.storage.proboards.com/6485149/a/n3wRLBmaUFtlA5lEEUBU.png)
Posts: 0
[I forgot who created it... Running from Flash Drive Troubles](/thread/35/forgot-created-running-flash-troubles) Aug 29, 2016 8:14:28 GMT -5 via mobile
Post by rpg17 on Aug 29, 2016 8:14:28 GMT -5
I'll be able to test it soon. Sick atm. -.- If it don't get better by Wednesday, I'll see what it is. Probably bronchitic again.![:(](//storage.proboards.com/6485149/images/FZUhtQ02ryuYo_Vwww6L.png)
Guest Shao
![Guest Avatar](http://s5149.storage.proboards.com/6485149/a/n3wRLBmaUFtlA5lEEUBU.png)
[I forgot who created it... Running from Flash Drive Troubles](/thread/35/forgot-created-running-flash-troubles) Aug 30, 2016 6:36:47 GMT -5
Post by on Aug 30, 2016 6:36:47 GMT -5
Don't worry about it, was just idle curiosity. Hope you feel better.
This Forum Is Hosted For FREE By Get Your Own !
