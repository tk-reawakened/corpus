---
kind: doc
id: "toolkitzone.com/104"
site: "toolkitzone.com"
title: "TK3 Amelioration VI ? Aftermath"
original_url: "http://toolkitzone.com/library.php?mode=read&doc=104"
written: "2007-01-25"
date_confidence: "day"
updated: "2007-01-25"
captured: ["20051228115808", "20070309061735", "20070318002913", "20070318002913"]
author: "Colin"
repliers: []
authors: ["Colin"]
comments_present: 0
f_author: "Colin"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_amp_3Bdoc_104", captured: "20051228115808", sha256: "54190cd201bf54ab1553d4a4ab2282da3dcf8eeaacd66eaa528260d955e60f8b", wayback_url: "https://web.archive.org/web/20051228115808/http://toolkitzone.com/library.php?mode=read&amp%3Bdoc=104"}
  - {path: "wayback/toolkitzone.com/library.php__doc_104_highlight_", captured: "20070309061735", sha256: "38c938e5fe40d15cdb4578c58cd19f2039d7cffbfad6948c4200ab2a49f2c1c3", wayback_url: "https://web.archive.org/web/20070309061735/http://www.toolkitzone.com:80/library.php?doc=104&highlight"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_104", captured: "20070318002913", sha256: "5866a342db7edf51e7ecc0652f60903a9c51382f0b9ea129e69847527c4c0697", wayback_url: "https://web.archive.org/web/20070318002913/http://www.toolkitzone.com/library.php?mode=read&doc=104"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_104-4849dd", captured: "20070318002913", sha256: "5866a342db7edf51e7ecc0652f60903a9c51382f0b9ea129e69847527c4c0697", wayback_url: "https://web.archive.org/web/20070318002913/http://toolkitzone.com/library.php?mode=read&doc=104"}
---

# TK3 Amelioration VI ? Aftermath

Browse
**TK3 Amelioration VI ? Aftermath**
Prelude
After months of anticipation, the RPGToolkit, Version 3.05 has been released. While initial impressions vary, most people seem to agree it is better than its predecessor. Others, however, are experiencing difficult starting the editor ? much less enjoying all it has to offer. Others find messy graphical glitches; certainly not something to be expected after so long a wait. These claims aside, I believe 3.05 to be thoroughly more stable than 3.04.
All of these issues?besides the editor not functioning?are not bugs at all. ?How can that be?? you ask. Well, that?s will this article will cover ? exactly how you can have the most successful and overall enjoyable experience with the newly released version. I?ll also suggest some possibilities for said editor bug and hopefully we can fix it. Bugs and non-bugs aside, please accept my apology ? things should function exactly as they did in previous versions. Hopefully, you can forgive us (the developers), and are able to get 3.05 functioning.
?The Installer Doesn?t Work!?
You?ve just downloaded 3.05 and opened its new installer. After you click through the first pages, you get to the actual installation. To your horror, the progress bar stops! A generic error message pops up and the installer closes! This must be a one time thing, right? So you run the installer again and it stops in . The installer just doesn?t work. *exactly the same position*
There a number of possible reasons why this problem is occurring ? all are curable. First and foremost, I highly recommend that you ? even consider restarting and then . This by itself may fix your installation problems. If not, take note of where the installer is stopping. Is it a *.ocx or *.dll file? If so, could any background processes (possibly the programs stacked in the system tray left of your clock) be using this file? To be sure, you might close running processes [via the (press ctrl + alt + del)] with the exception of , and, if on , other programs marked as belonging to the system (except ? definitely close that). **close all running programs** **closing all running programs** *all* *Task Manager* *explorer.exe* *systray.exe* *Windows XP* *dllhost.exe*
If it doesn?t work, you might try closing (your task bar and associated things will disappear, but they?ll come back after restarting) as it sometimes references things it shouldn?t. Also makes sure that you?re not attempting to install into the directory where the installer itself lies. If, after all this, you find it impossible to install?but this shouldn?t happen?, please download , or a program with similar functionality, and use it to extract the files from the setup program. If you use the latter method, run the file located where you extracted the files. Good luck! *still* *explorer.exe* [WinACE](http://www.winace.com/) *regocx.bat*
?My Sprites Move Too Quickly (But Smoothly)!?
So you?ve shown the installer who?s boss and have decided it might be a good idea to give your 3.04 developed game a test play ? just to make sure no new bugs have been introduced. But what?s this ? everything is moving considerably faster than you remembered it. It?s not clucky, laggy, or otherwise bad, just? fast. You conclude this must be a bug.
As you may have read, the movement system was rewritten for 3.05. Every item and character now be given their own fine-tuned speed via the item and character editors or the RPGCode functions and , respectively. However, is not obsolete, its use has simply changed. The game speed now serves as an ?offset? for sprite speeds ? possibly for use on a menu. Negative values the speed, making sprites move slower, while positive values have the opposite effect. *must* itemSpeed() playerSpeed() gameSpeed() *decrease*
As a result, you?ll need to set the game speed to its midpoint (0) in order to observe and experiment with the ?true? speeds of sprites. In many cases, just returning the game speed to the midpoint will cause the sprites to move at their original speed.
?I?ve Seen Less Lag Playing a MMORPG on Modem!?
Finally your sprites are moving at their original speeds ? or they should be. Even after reading the above, your sprites still ?lag?. They?re not responsive, they zoom around, and they?re just moving pretty poorly. Attempts to change speeds, resolution, color depth ? it?s all in vein ? they just move so . *awfully*
There is both good and bad news. The bad news being that this actually a bug. The good news, however, is that there is a workaround so you can forget that this bug exists and get on with your game making. The speed at which everything happens is based around how many frames can be rendered in one second ? frames per second (FPS). If the FPS were to be incorrectly calculated, everything would happen at the wrong speed. *is*
The formulas used to calculate the FPS were fine tuned while we had the FPS in the title bar ? constantly changing the title bar using an unimaginably small amount of time. Milliseconds add up, however, and as a result these formulas don?t work when the FPS is not being shown in the title bar. To resolve this problem, simply turn on the FPS in the title bar in the under the tab. My apologizes for any inconvenience this causes you. *Main File Editor* *Graphics*
?Some (or All) of My Sprites Aren?t Transparent!?
Now all your sprites are moving at a reasonable, responsive speed. There?s only one problem ? they have big white boxes behind them! They aren?t transparent! There can only be one logical explanation ? it must be a bug! *finally*
The previous release, version 3.04, had a bug where it made the both the transparent color white transparent. Many people were already using white as their transparent color neglected to set the actual color ? and it worked . Fortunately for some, and unfortunately for others, this bug was fixed. As a result, people who did not set their transparent colors will need to now. *and* *because of the bug*
?The Editor Doesn?t Even Open!?
Well, you?ve successfully installed version 3.05, you go to open up the editor and are surprised to find you see . If you?re lucky, maybe you see a tip or two, but then it?s all gone. You just can?t get to the editor ? it consists of . *nothing* *nothing*
At present, a solution to this bug is not known ? I am terribly sorry to those who cannot use the editor because of this. In order to enable us to post this bug, please tell us information about your system. Which version of are you running? If you?re XP, are your styles enabled? Which resolution do you use? Color depth? With your help, we may well be able to fix this bug. *Windows*
Wake
The situations detailed herein not withstanding, 3.05 seems to have been an incredibly successful release. The stability of many things have increased tenfold ? if not more! RPGCode, now object oriented, has become more than trustworthy but radiantly stable. The RPGToolkit has, once again, become fit for making games.
[![TBD](thumb.php?src=forum/images/avatars/180374083845e39c0971ae0.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=3969)
...Well written and informative. I had encountered the installation program once --- but with the use of this guide, I had easily remedied the problem. Nice article, Colin.
[![TBD](thumb.php?src=forum/images/avatars/199900821459c2e273a880.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=254)
To the 'Editor doesn't Open" bug: Sometimes just reinstalling helps. This happened to me in the previous version. It may not solve all problems, but it might help a few people.
[![TBD](thumb.php?src=forum/images/avatars/95475461445c5e2ebb49ea.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=392)
Also remember not to install from a read-only drive, because it won't work.
Oh, I forgot about that one - thanks for pointing it out.
[![TBD](thumb.php?src=forum/images/avatars/54730488645e8af527dbaf.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=1395)
Damn Spammers! Ruin everything! I've had no problems at all with the TK3 so far, so you've done it right for my machine(s). 3.05 is the first respectable release for TK3 to date, and this release has seriously made me consider porting my TK2 games onto TK3, since the OOP support is so appealing. Good job Dev.Team. You've earn't your fifteen mince pies this year!
[![TBD](thumb.php?src=forum/images/avatars/199057001842e42f75cf179.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=310)
Good article. Should hopefully help quite a few people. It'd be better if it wasn't needed but hopefully we're getting there.
TBD
Hmmm.... looks like this release will help me out a lot, but... I'm gonna have to learn RPG Code almost all over again... Could someone write a tutorial or explaing to me classes, and OOP in like.. lamen's terms, something simple??? |spitfire|
Quick Jump
Game Creation | -- Audio | -- Design | -- Graphics | -- | -- 3D | -- | -- Boards | -- | -- Sprites | -- | -- Other | -- RPG Code | -- | -- Canvases | -- | -- Classes | -- | -- Custom Systems | -- | -- Tips & Tricks | -- | -- Functions | -- | -- Other | -- Writing RPG Toolkit | -- News | -- Tutorials Community | -- News | -- Games | -- Contests | -- Interviews | -- Comment | -- Other
Keyword(s)
All Categories Game Creation | -- Audio | -- Design | -- Graphics | -- | -- 3D | -- | -- Boards | -- | -- Sprites | -- | -- Other | -- RPG Code | -- | -- Canvases | -- | -- Classes | -- | -- Custom Systems | -- | -- Tips & Tricks | -- | -- Functions | -- | -- Other | -- Writing RPG Toolkit | -- News | -- Tutorials Community | -- News | -- Games | -- Contests | -- Interviews | -- Comment | -- Other
**Published**
December 27th, 2004
**User Rating**
No votes cast.
**Views**
Who's Online: , , , , , , , , , , , [Acra](community.php?user=5400) [Avalon](community.php?user=349) [Desh](community.php?user=11101) [Lord Partikle](community.php?user=5533) [Lukkas](community.php?user=12945) [Montai](community.php?user=39) [Mr Picso](community.php?user=3699) [Occasionally_Correct](community.php?user=94) [Oyerth](community.php?user=37) [roy0007](community.php?user=6218) [theIronBulldog](community.php?user=14621) [valermos5](community.php?user=10533)
