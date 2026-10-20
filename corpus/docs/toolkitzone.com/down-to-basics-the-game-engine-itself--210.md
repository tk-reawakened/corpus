---
kind: doc
id: "toolkitzone.com/210"
site: "toolkitzone.com"
title: "Down to basics, the game engine itself"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=210"
written: "2005-04-08T15:54:00"
date_confidence: "exact"
updated: null
captured: ["20060207033238"]
author: "Talyn"
repliers: []
authors: ["Talyn"]
comments_present: 0
f_author: "Talyn"
f_date: "April 8, 2005, 3:54 pm"
f_description: "A lot of us harbour dreams of getting into the gaming industry, and many see the Toolkit itself as a stepping stone towards this. Talyn discusses just how relevant the Toolkit is to real game creation."
f_section: "Games > Design"
f_title: "Game Dev. in the real world"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_210", captured: "20060207033238", sha256: "f257ef853ef9c0481b5b48675de934a89edc8fea8226578287e71dfad4a5f3a4", wayback_url: "https://web.archive.org/web/20060207033238/http://www.toolkitzone.com:80/library.php?mode=read&doc=210&PHPSESSID=c55bda703eab3f300fd5ff76f9754f25"}
---

# Down to basics, the game engine itself

When us game developers foolishly start creating our masterpieces, we tend to take for granted all the hard work and effort which goes into the Toolkit itself, to make our development process as easy and quick as possible. However, a question we rarely ask ourselves is How accurate is this development process? Is this the kind of thing the boffins at Square-Enix do? This article will attempt to answer those. Anyone who's experienced with game dev please bear with me while I explain to those without game dev experience what a game engine is. The game engine is the program which runs the game itself. We're not talking your little RPGCode scripts now, we're talking about the program which controls everything. From the cycles per second, to painting the screen, to handling user input, to cleaning up on closure, this program does it all. We call this beast the Game Engine, as it effectively does for our game what a combustion engine does for a car, it keeps it going. In the Toolkits case, the game engine is the trans3.exe program (ah so that's what that program does! :) ) The Toolkit's game engine does basically everything an industry engine would do. It draws all the pretty graphics on the screen, it organises keypresses and it presents you with that horrible boss that you can't defeat. However, what's unusual about the Trans engine, is that it has it's own internal scripting language (namely RPGCode). Many industry engines are built using C++, and the game code is also written in the same delightful language. This is one of the first differences we see between real game development, and our own beloved Toolkit. Is this difference a bad thing though? Well, probably not. RPGCode is seen by many to be simpler than C++ (C++ also has a reputation which scares many people off) and simplicity is the key to creating a good piece of software, regardless of whther it's a game or investment calculator. A purist striving for performance might say that using an internal scripting language is an unneccesary middle-man, however if it gets more people involved with the software, does this marginal effect on performance really matter? So that's the engine done, now for the bit which most people are interested in, the development environment. The Toolkit boasts an impressive development environment which caters for near enough everything the developer could wish for. Graphics, animations, code, characters, it's all done in the environment. Here's big difference number two: Most game developers don't work with an integrated development environment, they hard code straight on top of the engine in C++ (apart from graphics which are done in imaging suites mostly). This big difference is essential to understand before launching yourself into the games industry. You probably won't be working with something as pretty and easy to use as the Toolkit. Why? Because game engines are different for every game. It doesn't make sense to use the same game engine for Kingdom Hearts 3 as you do for Medal of Honour. The games demand different things, different styles of graphics, different systems, different game objectives. You would either end up with one huge engine which could do it all but take two DVD's in it's own right, or lots of little engines which do exactly what they need to do and nothing more. Developers of course choose the second option (n.b It's not true to say that they write each engine from scratch. There is usual a Bog-Standard engine which does the things which every game requires and they just modify this template to fit the game). This changing of engines shows us why they don't use development environments. You'd have to write a brand new environment for each game! That takes time, equipment, programmers and money, all things which game companies do not want to waste. At this point, you might be tempted to think that, but in fact, the trans engine does a lot of things a GBA engine would do (alright, the engines are very different as they are for different types of system, but bear with me). Trans2 and 3 both use sprite animation. This was industry standard for many years (play back Pokemon and you'll quickly see the similarity). The way the sprites are made differs slightly, no tilesets as such, but the principle is the same. The Toolkit also uses a process known as Parallaxing. This is where the background moves slower than the foreground. This is a process still used in modern game development. After all, it would look stupid if you ran past a window and the Mountain 5 miles away was moving just as quickly as you were. Therefore, the Toolkit can still measure up to the big boys. Unfortunately though, there is still one thing which pushes the Toolkit way back down, and that's 2D animation. You would be outraged if you bought a PS3 with Devil May Cry 4 and found out that Dante was a 32 pixel high sprite who looked decidedly deflated. Nearly all console and PC games now are 3D, using technologies such as DirectX to ensure the big Wow factor when you turn on your games machine. In this respect, Trans3 will never match up to the modern consoles. However, with full Isometric support, we are starting to get there. Look back at that superb PS game Harvest Moon and you'll see it's entirely iso. Now we could have done that on the TK! Back to the question I started with, how relevant is it? Well, very. By using the Toolkit, you'll gain a very shrewd idea of what actually goes into a game. Many a time I've heard a person at my college say "Making a game is easy! All you do is draw a couple of things in a program, tell it what to do and then sell it!" As anyone who has created a game knows, this is far from the truth. The Toolkit will teach you that Game Dev. is hard, and you usually hate your creation by the time you publish it! In the comnputing field, this is not the easy option. Many things have to be created, modified, bodged and bargained with to create a successful game, and this is true whther you're working on the next Final Fantasy in Japan or if you're in sunny Brighton working on your TK game. For many, the Toolkit also indirectly helps them in other area's of their computing. For example, many will set up websites about their creation, and this is another important aspect of Game Dev. There's a hell of a lot more to it than just making the game. A lot of beginners will complain when their creation gets very little attention, the lesson to learn from this is to make a big deal about it! Create a good looking graphic and stik it in your sig or something like that. This teaches the important aspect of marketing. Your game needs help to get off the shelf. It's fine to create the greatest thing the TK has ever seen, but it needs to make people say wow from the start. Games companies do this through posters, TV adverts, game magazines and the internet as well as word of mouth. We can't do that here with the Toolkit, but you can do things like enter the Summer and Winter Expo's, maintain a vibrant and active profile, try and badger someone to write a review of your game on tkgaming. All these things are done in industry, we just do them on a smaller scale. And this seems to be the general theme throughout the Toolkit. We do everything the big boys do, just smaller. So in fact, the Toolkit is a fair indication of the mass produced games which go on sale. I myself am hoping to enter the games industry and I've included everything I've done with the Toolkit in my portfolio. It will help as it shows prior experience with the whole process of making a game. You should do the same if you consider going into a game oriented career. Universities and employers love to see enthusiasm, and by making games in your spare time, it shows a willingness to do it, something which both will value highly. It may also drum up more support for our little game engine! To sum up, the Toolkit is undoubtedly a brilliant piece of software for the beginner game developer. However for those who want to take game development further, it is also a good indication of how things are done (or at least used to be done three or four years ago). Any experience you gain with the TK will help you gain an understanding of how games really work "under the hood". If you enjoy working with the Toolkit, then it might be a good idea to buy yourself some books on game development in something like C++, and you'll quickly realise that we aren't so behind the times really.
Game Development in the real world
How relevant is the Toolkit to real game creation?
**Down to basics, the game engine itself**
**The Toolkit itself**
**Sounds like the Toolkit's nothing like the real world then.**
**The biggest difference of all**
**So how relevant is the Toolkit?**
**A more academic approach**
**In Conclusion then**
*Talyn*
Maelstrom
April 9, 2005, 12:49 am
One of the best articles I've read lately! This could be the last bit of motivation that pushed me back into game development with TK3, especially with that great new bug-fix version :D
Aquila Hawk
April 9, 2005, 1:29 am
Very inspiring, Talyn. I have heard from more then a few people in college game develoment programs that tell others who use the Toolkit or RPGMaker to just abandon it because it is futile to use. From the sounds of them, they really needed this article before they gave up on their own projects. I applaude you for this article.
Slasher
April 9, 2005, 7:28 am
Very nice, Talyn. The article is well-written, and should be that little push people need in order dust off that old dream of making it into the real world of game development. Excellent work.
William
April 9, 2005, 9:08 am
This one was great!! ;)
TK Game Boy
April 9, 2005, 10:57 am
*Applauses* Yah! Great article. I loved it. Now I am more enthustiastic about working in the VG industry. WOO!
AlienDude
April 12, 2005, 9:26 am
Thank you for this article, it shows all those nonbelievers (like some parents) that what we are doing hard. Look at my game i have been slowly getting it together for the past 2.5 years and just getting somewhere now. on a lighter note: Talin are goblin-like creatures in my game, infact one of the players is one. Just a coincedence i assure u. lol *is*
ever_dying
April 12, 2005, 10:02 am
well i think u are right, when i started to make game i also thought "ow thats easy" but the real thing is different. u guys should also see my first demo game: ist called Macbeth. i cant link u so plz search i yourselfs :P
cola56
April 13, 2005, 5:45 pm
Thanx, this article really hits the spot with me
AlienDude
April 15, 2005, 3:40 pm
You guys should expand this to include marketing, or make a separate artile on it. maketing is very important, amost as much as dev!!! Also a few possible sites that do just that of good places to advertise. Thanks again for this!!!!!!!!
UltimaWizard
May 6, 2005, 12:25 pm
Aah...this brought a tear to my eye. I'm relatively new to TK3, but you're right about the dev process. I love TK3 more than ever, now. Thanks for a real gift. *sniff*
daman
July 21, 2005, 6:40 pm
Dude i actually have tears in my eyes but thats true C++ does have a bad reputation although i do have a older verison of a C++ development tool
A lot of us harbour dreams of getting into the gaming industry, and many see the Toolkit itself as a stepping stone towards this. Talyn discusses just how relevant the Toolkit is to real game creation.
Feb 6, '06
Jan 21, '06
Dec 7, '05
Dec 1, '05
Jul 26, '05
Oct 25, '05
Sep 19, '05
Jun 2, '05
May 2, '05
Mar 16, '05
