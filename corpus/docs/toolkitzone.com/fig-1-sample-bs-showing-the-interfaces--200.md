---
kind: doc
id: "toolkitzone.com/200"
site: "toolkitzone.com"
title: "(Fig. 1 : sample BS showing the interfaces)"
original_url: "http://toolkitzone.com/library.php?mode=read&doc=200"
written: "2005-03-09T16:53:00"
date_confidence: "exact"
updated: null
captured: ["20051218072622", "20060312120250"]
author: "Cedrick Bryan Sagum"
repliers: []
authors: ["Cedrick Bryan Sagum"]
comments_present: 0
f_author: "Cedrick Bryan Sagum"
f_date: "March 9, 2005, 4:53 pm"
f_description: "New series of articles by Cedrick Bryan Sagum, concentrating on creating a custom battle system in TK2."
f_section: "RPG Code > Custom Battle System"
f_title: "Custom Battle System #1"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_200", captured: "20051218072622", sha256: "016d3e68fee750544f648d67a13ada1156fd7dc70b63680a7df1f6a436d3a432", wayback_url: "https://web.archive.org/web/20051218072622/http://toolkitzone.com:80/library.php?mode=read&doc=200&PHPSESSID=22af9c29bceeb94dce4bcfc8b732692e"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_view_cadd_doc_200", captured: "20060312120250", sha256: "497fd7983eba55b0d1c37a5122421bc148b7e4d1acd972abbcb32bb3db5e3d62", wayback_url: "https://web.archive.org/web/20060312120250/http://toolkitzone.com:80/library.php?mode=read&view=cadd&doc=200&PHPSESSID=bdcceeefceef8ff863ad82d0d089ece4"}
---

# (Fig. 1 : sample BS showing the interfaces)

By Cedrick Bryan Sagum Oct. 1999 was the date I discovered RPGToolkit. I was looking for an RPG game to play. I searched in downloads.com with keyword RPG. The RPGToolkit was showed after around 5 or more pages. I became interested in it so I download it. I was amazed at the sight of its interface (well, its the first RPG-making engine that I saw and decided to read the help files. A couple of days later, I learned almost the RPGCode commands. I have even tried downloading other demo games for research. One thing was certain. Everything has the default BS system. I tried to work on my game, but to my dismay, several disasters happen. Characters sprites move so fast, animations play at wrong coordinates, the menu is difficult to control and many other things about the Default BS that we love to hate. I tried Mr.Gs Shack for some help there. I found the answer. In Custom BSs, I found DragCash. I decided to reverse engineer it (meaning, open up the product, study how it was made, and create a much better product out of the product, not something similar to it). To my dismay, I was lost. I didnt understand the #RPGCode command (that was before) and most of his commands there uses it. Four months after the discovery, I quit. Another two months later, RPGToolkit 2 was updated. I decided to try again. I played Final Fantasy IV on an emulator for research about the pattern of battles. It was somehow confusing at first to organize the data, but its fine now. From that day on, I have decided to start creating my own custom BS. Six months after that, I finally achieved in creating one fully functional CBS (Custom Battle System) I would like to share my experiences and knowledge for those who want to have a CBS as a part of their game design. I created a CBS because of the necessity, and because of the challenge. And I dare those who have finished reading the entire tutorial to come up with their own. This tutorial is more focused on creating the most simple of the simplest CBS possible. This program will possibly serve as the backbone of the CBS that will emerge in the future. However, this tutorial is only limited to the Battle Systems used mostly by Squaresofts Final Fantasy series. It is also limited to the RPGToolkit2 engine (because I cannot confirm it yet if it is backwards compatible with TK3.0.5, the most updated RPGToolkit engine as this was written). The first step is to have a complete knowledge of the RPGCode. You can't create a CBS without appropriate knowledge. What I mean of "complete" is not just the list of commands found in the help3 file, but also understanding the help2 file. You can't just read this and expect to have created a BS already.Mbr> Next step is to have a design. A sketch is enough for the interface. This is a tricky part of the CBS. There are more aspects in developing Custom BSs that has to be planned in detail. These are some of the points that need consideration. 1. Set a design and sticks with it, unless you are confident in your programming skills. I once changed the system from mouse-based to cursor based due to popularity demand. The change was hell; I have to start the fighting menu system all-over again. Remember, this design will serve as the direction you have to take to reach your destination. You may take short cuts or take an alternate route. How can you go to your destination without a direction? 2. Create backup(s). In reinforcement with #1, creating a back up wouldn't hurt. It is better to load your back up than to start all over again. 3. Indent properly. If you don't indent properly, chances are the program may run wrong. Keep track of the {'s and the }'s. They should be equal in number. One misplaced { is enough to prevent your program from working effectively. Keep in mind that a CBS is a combination of lots of lots of lots of nested #Ifs, and #While statements. 4. Progress step by step. You can't just stop programming the Skills menu, just because you have suddenly a good idea for you Item menu. Just put your new ideas in a to-do list. 5. When I say planning, it means in detail. The screen has very limited space to project information to your game-tester. 6. Big Battle Systems makes big programming. Start out small first, and then improve later. You can't create a complete BS in just one run. Ideas soon come to mind so BS's always gets updated. 7. Do not ask someone to make you a CBS. If you have difficulty in grasping the concepts of a program that you make, how much more if you are to comprehend the concepts of a program others make. I find it easy to understand my own CBS as opposed to the CBS others made. You can however ask others for help on how to improve your BS. Remember, we were noobs before. Dont stay there. Also, remember that creating a CBS is a challenge. CUSTOM BATTLE SYSTEM: INTRODUCTION
PROLOGUE AND FOREWORD
SCOPES AND LIMITATIONS
INTRODUCTION
> a. # of players and enemies, their position in the screen, their attributes to use(name, hp, skills, exp). You should also have a database for you character skills and enemy skills (skill name, skill abilities) b. the interface. What I mean the interface is how will the information be given to the user such as the design of the hp/mp window, a possible ATB bar, design of the command window, displaying the options of the command window (attack, magic, item, etc.), help window, how the options will be selected (key-based, cursor-based, or mouse-based), capacity of every window (number of items/skills displayed per window, if the character is a magic user who has many skills) c. The fighting system. Much more difficult than the first two, the fighting system includes mostly formulas for use to calculate some things related to fighting such as basic attack damage, magical damage, elemental modifiers (like ice weak to fire and vice versa), etc. This may also calls for a decision whether there is a need for custom stats (instead of FP,DP, you will STR,AGI,CON,VIT,DEX and other stat) or use the default ones. However, be wary of the repercussion of custom stats. Customized stats absolutely need custom menu systems. The idea here is to make a game that isn't too easy or too difficult. d. Additional features. Every BS has a distinct special feature. Examples are Swapping Players in battle (FFX), Changing Job in Battle (FFXI), Combination attacks (Chrono Trigger, Suikoden II), Limit Breaks (FFVII), Trance Mode (FFIX), Character Changes In Battle (FFVII-Vincent, Legend of Dragoon), etc. e. The database. The database is the list of things that needed a constant loading and reloading. Examples are the list of enemy and their stats, names, HP, skills, exp, list of skills and effects for both players and enemies, list of battle items and effects, loading weapons attack strength and armors defense strength. Etc. Everything, including the simple Potion that restores 50HP, counts.
>
![](http://www.toolkitzone.com/library/images/docs/563.PNG)
*(Fig. 1 : sample BS showing the interfaces)*
DOS and DON'TS
Khin
March 10, 2005, 12:03 am
Wow, you're a writer now! Congratulations Bryan. ;)
Cedrick Bryan Sagum
March 10, 2005, 3:21 am
I guess I am. I'm working on my thesis for now before I edit the #2, #3 and create the rest.
John@aljo
March 12, 2005, 4:54 pm
good work but you might work on some sentence organization. oh yeah and its forward compatible.. not backwards :P
Cedrick Bryan Sagum
March 13, 2005, 3:32 pm
Yeah, I know... I wastyping this like it was an adlib
Marc
March 21, 2005, 4:35 pm
One problem I've allways ran into was speed, RAM and mess. Though, this isn't my article to give hints in :P.
roy0007
February 19, 2006, 9:17 am
why did you have to steal a lunatic from ragnarok
New series of articles by Cedrick Bryan Sagum, concentrating on creating a custom battle system in TK2.
