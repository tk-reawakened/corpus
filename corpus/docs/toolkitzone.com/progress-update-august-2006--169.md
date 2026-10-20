---
kind: doc
id: "toolkitzone.com/169"
site: "toolkitzone.com"
title: "Progress Update - August 2006"
original_url: "http://toolkitzone.com/library.php?mode=read&doc=169"
written: "2006-08-08T12:44:00"
date_confidence: "exact"
updated: null
captured: ["20061006224623", "20070220005136", "20100101202128"]
author: "Delano"
repliers: []
authors: ["Delano"]
comments_present: 0
f_author: "Delano"
f_date: "August 8, 2006, 12:44 pm"
f_description: "Pick yourself up off the floor, this really is the second progress update to hit the library in just over five weeks! This month the features discussed include waypoints, \"inline\" rpgcode and the new sprite editor."
f_section: "Toolkit 3.x > News"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_169", captured: "20061006224623", sha256: "37e326e12d401e485e61fbcacf0f44f19cf3cd57581eb6df977df301c9f4dd42", wayback_url: "https://web.archive.org/web/20061006224623/http://toolkitzone.com:80/library.php?mode=read&doc=169&PHPSESSID=a820148b616163a5ea1de7ec3d784861"}
  - {path: "wayback/toolkitzone.com/library.php__doc_169_page_1", captured: "20070220005136", sha256: "e89bc762b34be0cdb4cc4a05075262c61bd93c444e2d28f7c353d7169710e776", wayback_url: "https://web.archive.org/web/20070220005136/http://www.toolkitzone.com/library.php?doc=169&page=1"}
  - {path: "wayback/toolkitzone.com/library.php__doc_169", captured: "20100101202128", sha256: "f742e6a437aefde0e059ec0991dc6c465566ea797a1c53c7e1740990a5037d4a", wayback_url: "https://web.archive.org/web/20100101202128/http://toolkitzone.com/library.php?doc=169"}
---

# Progress Update - August 2006

By Delano
Apologies to those who were settling down for hybernation, because Xavier's finally convinced us to try and put out some more regular dev team updates, and since he's retired from developing it's left to Colin and I to conjure something up. Firstly we welcome Xorlak to the testing team, who brings with him his considerable experience and knowledge via his Dark Age series. Secondly, the board editor is progressing steadily. A number of useful tools and options have been added and the tabbed interface style continued by arranging the board properties on a tab within the editor itself. One new feature is the ability to move sprites along "waypoint" vectors, which provides a convenient method of creating complex paths. The introduction of vector collision to 3.0.7 has required a shift from the relative directon-based movement (e.g., Push("W")) to an absolute position-based movement (e.g., Push(96, 64)) and to a pixel co-ordinate system, in order to make full use of vectors. Hence a sprite can be supplied with a series of co-ordinates to walk between, or more easily, can be assigned a vector along which to walk, as seen below. Another new feature demonstrated in the image is that of so-called "inline" rpgcode, where instead of specifying the filename of a program, a line of code may be written instead. This handy addition should spell the end of warp programs and other single-line programs that clutter up the \Prg folder (though the contents of old warp programs will be substituted during format upgrades). A number of rpgcode functions have been introduced to handle vectors and vector movement, and in order to minimise this number, the functions' behaviours are determined by rather than numerous optional parameters (flags are a common programming convention that is easy to pick up and useful to understand). For instance, player movement can now be controlled solely through the new PlayerPath() function, which handles groups of co-ordinates, pathfinding and vector assignment. Due to the nature of arrays in rpgcode it is unfeasible to pass an array of co-ordinates to playerPath() (or any other function). Hence the vector access functions operate on a single-point basis: Matching "set" functions and similar functions for programs are also provided. Other bits of work include a makeover to the sprite editors that allow custom interaction vectors to be drawn (rather than the default shapes seen in previous screenshots). A simple wizard tool is provided for quickly completing the basic stances by supplying a common substring. As suggested in the next image, files can be saved and selected from within subfolders of the default game folders (in this instance, \Misc), which should help users to better organise their files. The translation of existing engine elements into C++ continues with the implementation of the reserved "virtual" variables (e.g. playerX[]), pak files, function redirects and animated tiles. The number of dll dependencies of the engine has also been reduced with the aim of improving the Make Exe feature. Various issues with rpgcode and vector collision identified by our testers have been investigated; the majority have been addressed, but as always a few will remain - which will hopefully be minor enough to be go unnoticed by the majority of users. It is worth remarking again that this is not a professional project and we have limited time and resources with which to work. Your support and patience is greatly appreciated as we progress towards this release.
**not**
![](library/images/docs/949.png)
*A waypoint vector on a Heraldry:Freija board*
*flags*
```
playerPath(handle, flags, x1, y1, ... , xn, yn); // Set a user-defined path.
playerPath(handle, flags | tkMV_PATH_FIND, x, y); // Pathfind to x, y.
playerPath(handle, flags | tkMV_WAYPOINT_PATH, index); // Assign a waypoint vector.
```
```
boardGetVector(); // Get a vector's attributes.
boardGetVectorPoint(); // Get a point on the vector.
```
![](library/images/docs/950.png)
*Character editor graphics window with a Heraldry:Freija sprite*
Flamencos
August 8, 2006, 12:56 pm
I am first to comment! Yay awesomeness!
Enzix
August 8, 2006, 1:15 pm
Delano you bastard! You made me pee my pants twice in a matter of two months... *fuming* Really, though! Great work. This will definitely be a monumental (if not THE monumental) release in TK history. w00t! w00t!
Sir Pimpalot
August 8, 2006, 1:18 pm
This's awesome!!! And hurray for better organization!!!
polraudio
August 8, 2006, 1:54 pm
WOW so many changes! might take a wile to get use to it.
Moo Of Doom
August 8, 2006, 3:07 pm
I'm so happy we'll be able to make custom collision/activation areas for our sprites. Great work, guys! *Golf clap*
Bad Kids
August 8, 2006, 3:35 pm
I love you tkdev! :P
????
August 8, 2006, 4:13 pm
Great stuff, vector collison and path-finding will greatley help with the making of Forbidden Truths
Cuzit
August 8, 2006, 4:52 pm
O_O Holy! Octember can't come any longer.... Or whenever it's coming out... >_>
Fuzzman
August 8, 2006, 5:12 pm
I'm loving 3.07 more and more. Keep it up, guys!
l3lue
August 8, 2006, 5:14 pm
Nice progress~ I'll have to get my stuff together for a demo when this is ready. ~__~
Bagel
August 8, 2006, 5:24 pm
Wow, this made my day.
TK Game Boy
August 8, 2006, 6:35 pm
Tis great. This will be on happy Octember. OI! Do not forget the philosophy of the TK. That the TK is to make game making easy. I dont think the word "proffesional" would be appropriate.
**It is worth remarking again that this is not a professional project and we have limited time and resources with which to work**
Zuntyh
August 8, 2006, 6:42 pm
where can we download this???
Sir Pimpalot
August 8, 2006, 8:13 pm
@zyunthos: HA HA HA! Sadly, not yet. Will animated backgrounds be possible?
Seafroggys
August 8, 2006, 10:19 pm
waypoints would be awesome.....definitally would be helpful with enemy AI functions
daman
August 8, 2006, 11:43 pm
I agree the collision detection will be awesome! Now it will be possible to create a great city game!
iFrog
August 9, 2006, 7:42 pm
I'm more jumpy then when I've had 5 cups of coffee... w00t!
Talyn
August 10, 2006, 4:14 pm
Very promising indeed =) Might have to visit the front page of the site more often. Thank God the Sprite editor has been cleaned up and improved. After having to work with it for a while just recently I began to loose the will to develop lol. Can only see good things coming from this. And keep us up to date!
narnianwolf
August 11, 2006, 8:21 am
I don't understand this much...which means it's good. I'll eventually get it, though. It looks amazing. Can't wait for whenever this thing is coming out!
Spyder
August 12, 2006, 9:47 am
It's really amazing to have watched the TK come this far. Keep up the good work =)
Trent
August 12, 2006, 4:52 pm
Ah... I can't wait to use all this cool new crap. XD
Gooseboy
August 13, 2006, 12:58 pm
I think im going to leave school just to use this.
UltimaWizard
August 16, 2006, 5:38 pm
Awesome. I know I sound like a broken record, but
**we need navigational RPGCode that returns values about which direction and what speed a player/item is moving at.**
Colin
August 16, 2006, 8:20 pm
(Look, I can embolden huge passages of text too.) **That's what plugins are for.**
Dude Man
August 18, 2006, 1:52 am
Waypoint vectors ftw!!! =)
Darwen
August 26, 2006, 9:18 am
This is really wicked! Toolkit is getting better-and-better with this wonderful dev-team. One thing guys: solve the instalation problem, you could spread it by installshield or something. ;)
zyrshnikashnu
August 26, 2006, 5:24 pm
Great job, dev team! The banishment of warp tiles was a great idea.
Colin
August 26, 2006, 5:34 pm
Which installation problem are you referring to, Darwen? (Edited to address the right person...)
zyrshnikashnu
August 26, 2006, 11:42 pm
Darwen != Darwin
hades01
August 27, 2006, 3:00 pm
sounds great XD can't wait to use it! keep up the good work :D
Falcon
August 30, 2006, 8:44 am
I like it so far. But using the playerpath function can we also make the player walk by itself automatically like in FF8 etc.?
Joe the Outlaw
September 1, 2006, 6:35 pm
I can't wait to get this so I can finaly use that damn playavi command (along with everything else.)
Darwen
September 2, 2006, 9:06 am
Colin! Darwin and Darwen aren't the same users and person. ;) The problem with the installer is that no matter what I do, gives error when I try to install. I managed to unarchive the installer, but no success. So, I would really recommend an archived version for download for all TK releases. :D Thanks you!
Colin
September 3, 2006, 1:38 pm
If you would actually be so kind as to say what errors they are, I could probably help you. If it's errors with the VB runtimes (likely), having a *.zip isn't going to help you. And it isn't going to help anyone else, because the installer does more things than just copy files. Instead, you need to download the VB6 runtimes - there is a link in the technical issues section of the help (which is available online). We don't know what it is, though, until you describe the errors.
Martine
October 4, 2006, 1:51 am
The Board Editor Is cool and easy to use, And the character editor too is cool, ToolKit 3.0.7 ROCKS! I can't wait to use this toolkit 3.0.7.
Pick yourself up off the floor, this really is the second progress update to hit the library in just over five weeks! This month the features discussed include waypoints, "inline" rpgcode and the new sprite editor.
**Recent News**
Sep 5, '06
Jul 3, '06
Jan 5, '06
Jun 6, '05
Apr 5, '05
