---
kind: page
id: "toolkitzone.com/toolkitzone.com/library.php?mode=read=doc=239.html"
site: "toolkitzone.com"
title: "Team Reorganisation"
original_url: "http://toolkitzone.com/library.php?mode=read=doc=239.html"
written: "2005-06-06T08:14:00"
date_confidence: "exact"
updated: null
captured: ["20061006224635"]
author: "Delano"
repliers: []
authors: ["Delano"]
comments_present: 0
f_author: "Delano"
f_date: "June 6, 2005, 8:14 am"
f_description: "Details of a reorganisation of the team into an official body with defined structure and principles, and information on the next stage of the Toolkits development."
f_section: "Toolkit 3.x > News"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_239.html", captured: "20061006224635", sha256: "1718ce528a2ab61ebf348f4365ff05747ac008a8b1ea5a5491dcc11a11bad788", wayback_url: "see README"}
---

# Team Reorganisation

By Delano
Since the 3.0.6 release at the start of April the development team has been pretty tight-lipped about the next move for the Toolkit. Although there have been no updates, a lot has been going on behind the scenes to set up the next stage of development.
Since the Toolkit went open source after version 3.0.1, various users have contributed to its releases and it has become a stable platform for game creation to rival and even supersede TK2. However, this has happened in a somewhat chaotic way, with developers coming and going and adding features individually without a solid framework for continued development and progress.
As a result the core developers, with the full support and endorsement of Chris Matthews, have reorganised the previously un-official, loose team into an official body with a set of principles and a development structure that aims to preserve the integrity of the Toolkit and ensure that all developments are carefully considered and implemented. An integral part is the creation of dedicated testers; community members with a solid understanding of the editor and RPG Code who are able to donate their time to testing development builds.
With this framework in place we have begun discussing the next development for the Toolkit, which is the logical progression of previous work. This is the translation of the engine from VB to C++, a step that will allow huge advances in capabilities. The primary benefit will be the massive increase in speed that C++ allows, which will have an effect across all features for all users; for instance, finally enabling movement to be truly pixel-based. Coupled with this will be the rewriting of the RPGCode parser, allowing for further expansion of RPGCode and providing another speed boost.
The rewrite also allows us the opportunity to implement new features without the side-effects that have plagued previous releases, and the first planned feature is the replacement of tile collision with vector collision, a tool that will vastly improve the detail and user-friendliness of games.
These are the principal developments for the next release of the Toolkit, which we must stress will require longer to achieve than previous releases. As we work through the rewrite we will review other possible feature implementations, so watch out for more indepth articles and news updates on our progress.
Allan@Aljo
June 6, 2005, 9:26 am
I had a post I wrote about this because it is near impossible for one person to do it on thier own... I've got a question though... will TK eventually go cross platform? That is one of the capabilities in c++. Alot of work though. something to think about. On the Organization thing Kudos. Good luck, and thank you for all yalls work.
Mystinar
June 6, 2005, 9:37 am
Somewhere I heard that compiled C++ is smaller than compiled VB. Will this mean that the TK3 download will be smaller?
Marz
June 6, 2005, 10:13 am
May I please recommend that we use OpenGL instead of DirectX. While DirectX is technically ahead of OpenGL in terms of graphics for this generation, the toolkit doesn't need the features of DirectX that make it better than openGL. Going openGL means that we have increased portability, which means we can finally use the toolkit on other platforms.
Colin
June 6, 2005, 10:28 am
The underlying graphics engine is already deeply rooted in DirectX, Marz. It's perfectly functional and fast; rewriting it to change engines would take quite a while. Thus, if we were going to do that at all, we'd do it so it used lots of fancy things like abstract base classes making it possible, theoretically, to switch in any engine with little effort. Porting is different from moving to C++ too; it still won't be close to portable. The good news is that the engine will in a position to be ported at a latter date; that would take a substantial amount of time, however, and is not part of this release.
Marz
June 6, 2005, 4:02 pm
My apologies. I was under the impression that the engine was about to undergo a complete rewrite, which is why I recommended using the OpenGL libraries.
Trent
June 6, 2005, 10:22 pm
Wow, sounds great. I'm rooting for you guys.
Mystinar
June 7, 2005, 12:12 pm
With the collision system rewrite, will users have the ability to define which areas of character sprites are used for collision detection?
ViperCat
June 7, 2005, 12:20 pm
I'm not a major voice, but if you keep using directX, maybe you can take advantage of it's lighting effect capabillites. I know you may think it only works on 3d games, but it doesn't it even applies to 2D graphics, ( Diablo II) Or just add a shadowing effect your self, just at the main menu, add a lighting effects checkbox, then ask for the direction. Then the shadow could be applied to all boards in the game, just copy the pixel structure of an object, put it as a dark shade, and starting at a starting refernce point strecth at the angle of the direction the light was coming from... Hey, If it's to complicated, I dont blame ya, it's just a suggestion.
Craig Reeves00
June 7, 2005, 12:21 pm
Porting it to a new language? There's certainly going to be bugs. I think the smart thing to do is get the bugs out of the realease we've got first and then port, IMHO. Big changes bring in big bugs.
Xavier
June 7, 2005, 1:45 pm
The majority of bugs that remain, especially the crippling ones, can only be fixed by moving the engine to a new language. If anything we'll be able to capture more bugs, solve more issues and put it through periodic build testing more easily.
Hamster
June 7, 2005, 3:23 pm
Just wondering, since the engine is being changed to C++, will anything having to do with plugins change? and is the new version going to be 3.07 or 4.0 ?
Xavier
June 7, 2005, 3:45 pm
There will never be a 4.0, people need to stop talking about it. It'll be 3.0.7 or maybe 3.1.0, but likely 3.0.7.
Hamster
June 7, 2005, 5:50 pm
good to know you guys want to perfect version 3 before going to another. seemed like for a while no one cared about bugs. & be more optimistic, Xavier. the TK has lasted this long, maybe it will get that far.
ViperCat
June 7, 2005, 6:40 pm
There has to be more versions!! I know there has to be!!! If not... Maybe I''l learn C++ and keep working on it myself!!!
Dont_Think_So
June 7, 2005, 6:51 pm
I don't think you guys understand. Just because TK3 is the last revision doesn't mean it won't keep going for a long time. A TK4 would have to be something written entirely (or almost entirely) from scratch, and likely from a different development team, which means it shouldn't be called TK4 anyway.
Xavier
June 8, 2005, 8:01 am
Some of you guys don't understand, there can be no TK4. The TK could last for 100 years but TK4 can only be initiated by CBM and that is very, very, very unlikely. Anything else is just TK3 open source spin-offs and legally cannot be called Toolkit 4 nor will truly be the TK. Some of you new users really need to understand this and just lose this obsession with verson "4". Toolkit 3 will easily surpass any wet dreams over 4 eventually, just forget the idea of a new number. Anyways, back to the topic...
ViperCat
June 8, 2005, 10:47 pm
Well, I didnt think of all that legal stuff, sry bout hat i understand :P
Alex0Xander
June 10, 2005, 7:08 pm
Xavier likes saying 'Wet Dreams' =P I sayyy, a new TK4 in 2008! But seriously, the best of luck to you guys.
SoSexyBoy
June 18, 2005, 7:11 pm
heh, scince u dont wanna make a 4th toolkit, how about keep adding new cool features like that shadow thing that guy said. You can also make dynamic lightin' and an enached battle system, etc. I know it's hard, but i know that over time the TK3 will be one of the most powerfull editors in the web. And can compete with the GM(Game Maker) or even the 3D Game Studio(ROFL) and be superior than most of game editors arround =D just work hard.ooo
sk8er32234
July 2, 2005, 12:14 am
THIS IS A SPECIAL THANKS (AND I SPEAK OF ALL OF US WHEN I SAY THIS) ...THANKS THANKS THANKS THANKS THANKS......
Ivan
July 21, 2005, 1:34 pm
TK is a big rival of GM already. And it would never compete with 3D GameStudio becasue thats a game maker solely for creating 3D content while TK is for RPG's
zeno
July 25, 2005, 10:36 am
"Somewhere I heard that compiled C++ is smaller than compiled VB. Will this mean that the TK3 download will be smaller?" I heard that somewhere too...but I dont think that It will matter to anyone unless they have dial up :D
Treefrog_programmer
August 17, 2005, 5:18 am
C++ is faster, more powerfull and smaller than any other computer language (exept assembaly language and machine language - but those are imposibly hard to use) , this is because C++ is closer to machine language (the only language a computer understands) than say vb (visual basic). so the toolkit will be able to have more functions, make smaller and faster games and be smaller and faster itself. on the TK4 debate: i think there will be a TK4 at some point, but we need to stop looking for it, it will be made if a compleate rewrite is neccesary, TK3 has just come out and it is amazing. stop thinking about the next one when youv already got an amazing rpg toolkit. TZ RULES!
Oyerth
October 3, 2005, 7:07 pm
Treefrog, you have no idea what you are talking about when it comes to 'TK4'. I highly suggest you read over Xavier's comments.
Delano
June 6, 2005, 8:14 am
Toolkit 3.x > News
Details of a reorganisation of the team into an official body with defined structure and principles, and information on the next stage of the Toolkits development.
**Recent News**
Sep 5, '06
Aug 8, '06
Jul 3, '06
Jan 5, '06
Apr 5, '05
