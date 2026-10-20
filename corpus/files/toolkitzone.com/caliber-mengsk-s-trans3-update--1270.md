---
kind: file
id: "toolkitzone.com/1270"
site: "toolkitzone.com"
title: "Caliber Mengsk's Trans3 Update"
original_url: "http://www.toolkitzone.com/fileman.php?id=3&file=1270"
written: "2006-04-07"
date_confidence: "day"
updated: "2006-04-07"
captured: ["20060519091712"]
author: "Caliber Mengsk"
repliers: []
authors: ["Caliber Mengsk"]
comments_present: 0
f_author_source: "Ray Phillips"
f_name: "Caliber Mengsk's Trans3 Update"
f_submitted_by: "Caliber Mengsk"
f_version: "1.2"
f_website: "calibermengsk.com"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_1270", captured: "20060519091712", sha256: "d2042ac0637f6fa027b7a17dae99ea43b27798b9552158c28bff4ba9491d5334", wayback_url: "https://web.archive.org/web/20060519091712/http://www.toolkitzone.com:80/fileman.php?id=3&file=1270&PHPSESSID=6defe02bb6a1008021d574cf4a52c396"}
---

# Caliber Mengsk's Trans3 Update

User patch that contains fixes to CreateItem, ItemLocation and TargetLocation, plus a new command in PlayerLocation for retrieving the players X and Y co-ordinates. Includes source and readme.
**This is not an official release, therefore not endorsed by the official development team. New commands are not guarenteed to be supported in future Toolkit releases, so use at your own risk. Always back-up original files before using.**
22 March, 2006
Cool! Someone finally issued a patch! The broken item commands caused work on my game to stop. Now it can continue. Many thanks!
22 March, 2006
Just to state, the sourcecode will be uploaded within a week or so... We are commenting the changes at the moment. They will be uploaded for all to see.
22 March, 2006
Thanks, is this what you're using for your real-time BS?
22 March, 2006
Yes, this is what I am using for my real time battle system. The trans3 file will be included when I release the CM Zelda BS.
22 March, 2006
Good job.... This should help with my battle system.....I shall test it immediately
22 March, 2006
prgDelay() doesn't even make any sense, causing you to wonder if the author knows anything about the infrastructure of the Toolkit.
22 March, 2006
But at least he actually fixed the game-killing bugs, which no body else bothered doing. While I don't mind waiting a while for the next version, not having a quick bug-fix of some kind in the meantime is in very poor sport.
22 March, 2006
Or did he? We can't know because he withholds the source. He's so ashamed of his own code that he stalls to "comment" it.
22 March, 2006
Colin... Quit being an ass. I also said I don't have the source files, my brother does. He works a full time job and I am a full time college student and work a part time job, so I rarely see him to get the files from him as well. I am really getting annoyed that pretty much anything I say or do you bash down, not in a constructive way.
23 March, 2006
I don't care how busy you are. If you have enough time to build the executable, you have enough time to document what you've changed (even just explain it in words) before you submit the finished product.
23 March, 2006
Colin: Allow me to introduce myself. My name is Ray Phillips. I am the brother of Randy Phillips (better known on the TKZ as "Caliber Mengsk"). I'm sorry if uploading the executable before the source code made you or anyone else upset. You can rest assured that the only reason the exe was uploaded before the source was simply because I hadn't had time to comment my code. When I write code, I do not comment it. So after making the changes, I needed to go back to comment them. Rany (Caliber) asked if it was ready to upload (he gets a bit exited sometimes) so I gave him the exe. In hind sight, I'm glad that I did do it that way. As you can tell, I was corrected on a few points. e.g. prgDelay was in fact un-nessesary and will be ommited from the source when I upload it (unless you want me to leave it in, tho I can't see why). Also it gave me a chance to finish PlayerLocation so that it returns the Layer and allows the user to specify the player's handle to get any player's location. Don't worry, In an hour or so I should be uploading the commented source for you to rip to shreds :) Also, I agree that it would be a good Idea to do PlayerLocation as a plugin. But, as I looked through the plugin SDK, I couldn't see any way to get the "theProgram" or "pPos" variables from the Trans3. So I left it in the Trans3 for now. -Cheers- (and please calm down a bit!)
*completely*
23 March, 2006
It's reactions like Colins that make me stay away from this community when I don't have to be here. I am part of another Open Source community, the Battle for Wesnoth, and they are very nice friendly and civil. They have very strict standards about how they do things, but no one every gets insulted or put down. I am also a member of the Freedom Force community. Same there, very kind and friendly. The longest-running members will always take time to answer a stupid little question they've already answered fifty times before. The newer members, in turn, quickly start helping out the next time the question is asked. Yes here people are always getting yelled at or told, in response to feature suggestions, to just "do it yourself" without any help which would allow them to do so or without any cosideration for the possibility that it would be simpler to have one person code it once than for fifty different people to all do it on their own. Caliber was kind enough to release this. He is under no obligation to release the source code if he doesn't want to, although he by all means should. Instead of yelling at him, try politely asking. As for whether it works or not, I'll verify that the next time I get around to working on my BS.
23 March, 2006
I hear you catwhowalks~! Don't worry too much about the source, Ray. If the bug fixes work then great - kudos to you; if they don't, then it's your loss. The whole "guilty until proven innocent" thing is ridiculous. Well done for putting in the effort.
23 March, 2006
Source is uploaded, just waiting for approval... BTW: I'm NEVER ashamed of my code :) The source doesn't have prgDelay in it anymore and I made the changes to PlayerLocation that was mentioned earlier.
24 March, 2006
Now doesnt it seem kind of "childish" Colin ... to get mad at someone and put them down for doing what you were doing in the first place ... except they did it right? I find it ammusing that you would actually get jealous over someone trying to do the TK one better. These bugs should have been fixed a long time ago. I'm not saying that your lazy ... but it's good to have someone here that can actually clean the versions up while your hard at work on the next release. You should be thankful not jealous. BTW ... Thank you Ray and Caliber ... us users really do appreciate your update. RDX
24 March, 2006
Why does it not suprise me it's Colin who drags file comments down the gutter, sigh.
24 March, 2006
Why do you want to personalise this, Xavier? I was talking about source and submissions, not Caliber. This isn't some show of "jealousy" or a "putting down". I'm starting to think I can't even be reasonable without being accused of doing something wrong.
24 March, 2006
Indeed, you mean personalise like; "He's so ashamed of his own code that he stalls to comment it."? Anyway, update will be up soon (just need Calib to correct something first).
24 March, 2006
Yes I do. It's only fair that I personalise after the walking cat steps in and attacks everybody around ("which no body else bothered doing").
25 March, 2006
Ok, the source is included now. The new exe excludes pgrDelay and changes PlayerLocation to the following syntax: PlayerLocation(PlayerHandle$, X!, Y!, Layer!) Click "Download" to get the latest (2.8MB)
26 March, 2006
It wasn't meant as an attack and certainly wasn't aimed at anyone in particular. It's just a fact that no one corrected the two major bugs left after an otherwise excellent bugfix release in spite of the fact that those bugs made some custom systems uncodable. And even if I was aiming at you(Colin) personally, that's no reason to personally insult someone else who had nothing whatsoever to do with anything I was saying. Now my comments about how rude and uncaring people are around here, those were aimed at you.
27 March, 2006
Hey Sweet! Gonna test this as soon as possible :D
**Browse Sections**
