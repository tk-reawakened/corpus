---
kind: file
id: "toolkitzone.com/358"
site: "toolkitzone.com"
title: "Phoenix"
original_url: "http://www.toolkitzone.com/fileman.php?id=3&file=358"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040617052315", "20041031040106", "20070323044039"]
author: "computerdude800"
repliers: []
authors: ["computerdude800"]
comments_present: 0
f_author_source: "Daniel Gillespie"
f_description: "Fierce battles, or collaberation, seems to work wonders. This time the release of Phoenix is great! Plugin system, recoding of the editor itself, much smaller size, and project files are just some of the new features. Try it out. This release has a few bug fixes."
f_downloads: "782"
f_name: "Phoenix"
f_size: "225.6 kb"
f_submitted_by: "computerdude800"
f_version: "v2.1"
f_website: "www.chronogames.com"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_358", captured: "20040617052315", sha256: "1989b66c23b2241a0d4c11ea64c27e69c83834f5721ab17f8ae652f0187cdc5f", wayback_url: "https://web.archive.org/web/20040617052315/http://www.toolkitzone.com/fileman.php?id=5&file=358"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_358", captured: "20041031040106", sha256: "af3ced250e13a7dba862144135a0eda4de56408d6a9ff27d7fcbe1cadd66cb9b", wayback_url: "https://web.archive.org/web/20041031040106/http://www.toolkitzone.com/fileman.php?id=3&file=358"}
  - {path: "wayback/toolkitzone.com/files.php__file_358", captured: "20070323044039", sha256: "df9ca7205242392511e3fb95092b74c8b25678bfec5245d51a75d27e071ea18d", wayback_url: "https://web.archive.org/web/20070323044039/http://toolkitzone.com/files.php?file=358"}
---

# Phoenix

Fierce battles, or collaberation, seems to work wonders. This time the release of Phoenix is great! Plugin system, recoding of the editor itself, much smaller size, and project files are just some of the new features. Try it out. This release has a few bug fixes.
**screenshots**
posted by on 2004-03-03 02:59:42 [Nih](forums/profile.php?mode=viewprofile&u=24)
Not too bad. Looks promising if more features are added in future releases. However, I only use the TK's prg editor. It's easier than external editors. Maybe if one was good enough...
posted by on 2004-03-06 18:45:10 [Colosseus](forums/profile.php?mode=viewprofile&u=718)
It's a great editor, but it's got poor error handling... Dunno if it's only me, but when I try to open paint or calculator I get runtime errors and the program shuts down. Same if I try to add a command from the list to the right... Other than that, it's just as good as it should be to kick some Vortex arse.
posted by on 2004-03-08 21:27:53 [computerdude800](forums/profile.php?mode=viewprofile&u=73)
hey If you guys find errors and crap like some of you posted above than email me the error number and the promblem ocuring. my email adress is or if that dosent work than (redacted: email). Thanks
posted by on 2004-03-09 10:33:51 [Colosseus](forums/profile.php?mode=viewprofile&u=718)
Uhm, another thing, the line numbers seem to be overlapping the code... Dunno if it's just Windows 98 again (damn piece of crap), but it's annoying. Btw the errors I've experienced are: When I double-click on a command on the right this is what I get up: Run-time error '91': Object variable or With block variable not set And when I try to run paint or calculator from it, I get this: Run-time error '53': File not found ... But those are the only flaws I can see (except from the line numbers of course). Good job with the rest.
posted by on 2004-03-11 20:21:54 [computerdude800](forums/profile.php?mode=viewprofile&u=73)
Im going to try to fix that but the main problem with that is that your OS is Windows 98. The file not found is because Phoenix is going to open a directory that is only in Windows XP. And the Double click on the command list is what I cant explain, it seems to me that this error is regulated to the fact that your OS is Win 98. So since I dont have 98 would tell me the directory in which MSPaint is in and the Calculator program. I will do my best to fix this problem. Thanks
posted by on 2004-03-13 13:23:49 [Colosseus](forums/profile.php?mode=viewprofile&u=718)
Windows 98 keeps those programs (paint and calculator) in C:/Windows/ Paints name is pbrush.exe Calculators name is calc.exe Hope that helps! Btw, could you tell me what the file names and paths of Paint and Calculator are under Windows XP?
posted by on 2004-03-15 01:56:18 [computerdude800](forums/profile.php?mode=viewprofile&u=73)
oh ok, Your probally looking for the pasth cuz ur making a program to right? i think its RedRose or something-pad, dunno, well I would fix the problem, but I just realesed v1.2 so ill fix it in v1.3 , anyway the paths for Paint and Calculator in XP are, C:WINDOWSSystem32calc.exe C:WINDOWSSystem32mspaint.exe Just curious, what language are you writing your program in?
posted by on 2004-03-15 21:11:02 [Colosseus](forums/profile.php?mode=viewprofile&u=718)
I do Redrose in Delphi 7 - it's a great language and easy to learn.
posted by on 2004-03-18 02:09:27 [Euix](forums/profile.php?mode=viewprofile&u=9)
ComputerDude, since you are using VB use the Shell command, but don't include the entire filename of Paint or Calculator. Since they are in the System folder they can be called like this: Shell "mspaint" - or - Shell "calc" Although, you can also you a little error checking "Check the number of the error, if it's 53.. then...". 53 would be file not found, so if the error number is 53, simply have it direct the user to "pbrush" instead of "mspaint". This would fix some problems for Win9x users.
posted by on 2004-03-18 06:13:11 [computerdude800](forums/profile.php?mode=viewprofile&u=73)
Thanks Euix, duelly noted
posted by on 2004-03-18 13:30:13 [Colosseus](forums/profile.php?mode=viewprofile&u=718)
Stop fighting, dudes! I must admit, you still haven't fixed the Win9x problems as you said you would, computerdude. And you, Euix, really do have a lot to do to catch up with computerdude. You're both right, okay? Happy?
posted by on 2004-03-18 16:41:02 [computerdude800](forums/profile.php?mode=viewprofile&u=73)
I wasnt fighting, i was merely stating the truth. Yea I forgot to add the Win9x stuff, ill put it in for v1.4
posted by on 2004-03-18 18:59:47 [Colosseus](forums/profile.php?mode=viewprofile&u=718)
Yeah, k... Lol, this is just like WW2, everybody defending THEIR case (which now is their RPGCode editor) and being picky on others. Hehe. Hmm, I'm kinda curious, how did you make your media player run externally although it has no .exe in the directory?
posted by on 2004-03-18 20:11:01 [computerdude800](forums/profile.php?mode=viewprofile&u=73)
Its not being run externally, its just looks like it.
posted by on 2004-03-19 13:13:22 [Colosseus](forums/profile.php?mode=viewprofile&u=718)
Cool! But hey, listen, how about making an external version of it too? I mean, I've made a media player in the newest version of Redrose (which is awaiting acceptance), and I've asked Vampz if he could add an "utilities" sub-zone under the sounds section too! Would be cool, don't ya think? Sound editing utilities could be the next big thing here at Toolkitzone :D
posted by on 2004-03-19 16:31:50 [computerdude800](forums/profile.php?mode=viewprofile&u=73)
yea sounds pretty cool, but if I make an eternal version ill have to beef it up with features.
posted by on 2004-03-19 19:13:00 [Colosseus](forums/profile.php?mode=viewprofile&u=718)
You do that. It oughta be a success! My media player named Bluerose was actually an internal player, but I decided to extract it and run it externally so that you can listen to music even when Redrose is not running.
posted by on 2004-03-19 20:39:47 [computerdude800](forums/profile.php?mode=viewprofile&u=73)
I might do it. Hey do you have AIM? If you do can I have your sn, I would like to talke to you some time.
posted by on 2004-03-19 20:47:53 [Colosseus](forums/profile.php?mode=viewprofile&u=718)
Don't have AIM, but I got MSN Messenger... (redacted: email) I'm downloading AIM now - should be up in a minute!
posted by on 2004-03-19 20:51:52 [computerdude800](forums/profile.php?mode=viewprofile&u=73)
alright cool, when you get AIM just tell me your SN
posted by on 2004-03-19 22:50:51 [Colosseus](forums/profile.php?mode=viewprofile&u=718)
My SN is "colosseusdude"
posted by on 2004-03-23 01:29:06 [computerdude800](forums/profile.php?mode=viewprofile&u=73)
Im going to fix the Copy/Paste thing in v1.4, so wha do you guys think?
posted by on 2004-03-23 17:38:06 [Colosseus](forums/profile.php?mode=viewprofile&u=718)
Phoenix 1.4 rox - only a few steps and Vortex 4 is dead meat!
posted by on 2004-03-23 23:53:08 [computerdude800](forums/profile.php?mode=viewprofile&u=73)
thanks man, but VorteX 4 still has a couple of more features that Phoenix dosnet have yet.
posted by on 2004-03-24 20:12:40 [Colosseus](forums/profile.php?mode=viewprofile&u=718)
Wait 4 it... We have Xperience now =)) We can do it!
posted by on 2004-03-26 22:58:16 [computerdude800](forums/profile.php?mode=viewprofile&u=73)
Yea I suppose your right. I can't wait for your or me to beat VorteX, I like VorteX though but its needlessly complicated.
