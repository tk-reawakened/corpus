---
kind: doc
id: "toolkitzone.com/41"
site: "toolkitzone.com"
title: "Intro"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=41"
written: "2006-01-05T08:06:00"
date_confidence: "exact"
updated: null
captured: ["20060211044249", "20060222124122", "20100101201516"]
author: "Xavier"
repliers: []
authors: ["Xavier"]
comments_present: 0
f_author: "Xavier"
f_date: "January 5, 2006, 8:06 am"
f_description: "It has been a long while since news was last posted regarding the next release, 3.0.7, which will see the Toolkit have a re-written engine. Considering development still has a long way to go, we thought it best to provide you patient folks with a quick look at what's going on behind the scenes and create some screenshots to demonstrate new features in action."
f_section: "Toolkit 3.x > News"
f_title: "Progress Update"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_41", captured: "20060211044249", sha256: "0211fd151d52a26fafdbe719418f6cd74d70699758da8925d864645e3fbc9931", wayback_url: "https://web.archive.org/web/20060211044249/http://www.toolkitzone.com:80/library.php?mode=read&doc=41&PHPSESSID=ef05e627eb8c2677174592c2e7f83195"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_view_cadd_doc_41", captured: "20060222124122", sha256: "cc362ad8c2ef2bacdd9df2718a7d1d0bb5f5b5124564f5ee2ff577b57c84a0b8", wayback_url: "https://web.archive.org/web/20060222124122/http://www.toolkitzone.com:80/library.php?mode=read&view=cadd&doc=41&PHPSESSID=ef05e627eb8c2677174592c2e7f83195"}
  - {path: "wayback/toolkitzone.com/library.php__doc_41", captured: "20100101201516", sha256: "75bc96a58a0463085da5b2286f441d49bfa618895cb5f6cc94de00f2783c2329", wayback_url: "https://web.archive.org/web/20100101201516/http://toolkitzone.com/library.php?doc=41"}
---

# Intro

In June we announced that there was a changing in the structure and organisation of the now official development team, and the first team decision was to focus on migrating and re-writing the TK engine from a VB/C++ hybrid to a purely C++ system. The core aim was to vastly improve speed and reliability, with the added benefit of re-coding allowing for new and exciting functionality. So six months on and little news later, where exactly is the Toolkit? We had become used to reasonably regular releases and patches, so unsurprisingly many of you have become a little impatient and nonplussed as to the next release. Well, as a special (and deserved) New Year treat here is a short sneak peak at the progress of 3.0.7. Before we go into the details I'd like to stress that this is purely a progress update, the fact is a release is still a long way off. At the moment we have two developers in Colin and Delano who have devoted a lot of their free time to the project and we owe them a huge thanks, but as with us all they have other things to do in life and so development take time. Nonetheless, what they have done thus far is truly fantastic and a great sign of things to come. So lets take a look... One of the most noticeable changes will be the abandonment of variable types, such as literals and numerals, for a single dynamic type, similar to that in PHP. This means you no longer have to worry about casting and type consistency, and the greatest advantage being increased execution speed of code due to less variable related checking. I know it's easy to say, but the engine really will be faster. Migration alone to C++ would support some improvement but Colin, who is primarily involved with the language aspects, has re-written the parser and confirms performance is definitely heightened with many inefficiencies curbed. I suppose for now you'll have to take our word for it :). Due to the vast changes behind the scenes, a lot of concerns have been raised regarding compatibility with prior TK3 versions, specifically with RPG Code. The answer is simple; the developers assure that all commands will be fully compatible between versions. An updater will be included that will make any syntax changes to programs such as removing the now redundant type characters among other things. Nothing can be guaranteed, but Colin has taken great care in keeping as much as he possible can backwards compatible. We all appreciate speed and performance, it's the cornerstone of any system, but lets face it nothing beats eye candy. The work behind the graphics aspects of the engine, primarily by Delano, is impressive to say the least, bringing many features to the Toolkit that have been sighted as serious omissions by fans of other RPG makers. Now we have vector collision, where an object can be given a set of points to form vectors, therefore establishing contact areas. A sprite polygon, upon making contact with other vectors, can trigger a specific event or, for example, the vector acts as a "solid" area it cannot enter. Lets take a look at vectors, all visible for testing purposes, in use with a board from The Lost Epic. As you can see, polygons have been used to define various areas on the board. The white lines are solid vectors, such as rocks in this case. You'll notice the base of the sprite is a white polygon, so in this case their feet cannot cross other solid vectors but of course their head and body will, giving the result of walking in front (but not over) objects. The green lines are "under" vectors, anything below the vectors will appear in front of it and anything higher, in the sense of the Y axis, are behind it. Speaking of boards, the limit on the number of layers you can have has been removed. So that's an example of vector types, but what about event triggering? Here is board from Heraldy: Freija in action; the statue is a separate image placed on a higher layer (rather than being an under tile): An event is triggered when the sprite contacts a vector or alternatively when an activation key is pressed within a contact area. As you can see in the image, the yellow vectors represent event triggers. To prevent multiple triggers when moving within a contact area, a programs can be deactivated for a certain number of steps or until the player leaves the box. You may have noticed red vectors in the two images - these demonstrate mouse-driven (point & click), vector-based, path finding movement. Sprites can move in any direction, with the sprite adopting the nearest corresponding direction animation while moving. NPCs can be given vector paths to follow or told to wander via vector. For those of you wondering how vectors can be compatible with the current use of tiles and tile types, here is the system in action with the demo start board. Those of you with keen eyes will notice in the above shots that we also now have partial translucency, whereby only parts of a sprite turns translucent when covered. Currently the enter sprite becomes translucent, or remains solid, when partially under a tile. Partial translucency applies not just to "under" vectors, but also objects on a higher layer and other sprites. Of course, with some of the changes to the engine such as vectors, changes will also be required with the editor. Right now development is focussed on the engine, however we are confident that the next board editor will have all the required drawing and shape tools for handing vectors and other new functionality. There's still a lot of work to be done, but as you can see Colin and Delano have done a fantastic job thus far and I'm sure we can all offer them the patience and support they deserve as they continue development. And thank you guys for using the Toolkit and continuing to promote its use, I promise to try and keep you guys more up to date over the months to come. Oh, and before I forgot anyone who asks for a release date or estimation in the comments will be publicly flogged :). We have no date or estimations, when we do we'll announce it
Progress Update
**Intro**
**RPG Code**
**Graphics**
![](library/images/docs/805.png)
![](library/images/docs/804.png)
![](library/images/docs/802.png)
**Future**
Caliber Mengsk
January 5, 2006, 9:02 am
*is first to comment... YAY!* Looks good, and I would like to say I am thankful to Colin and Delano for doing a supreme job so far.
Ekamp
January 5, 2006, 9:39 am
Frickin' awsomest thing I've ever seen. I love all of you. I really do. I can't wait to be able to use this.
Whist
January 5, 2006, 10:06 am
This looks great guys.
thing
January 5, 2006, 10:20 am
When this come's out, it might even make me start using the toolkit again. Nice work.
Doc_Wellsy
January 5, 2006, 12:31 pm
Excellent - I've been waiting for collision detection like this for ages - keep up the good work everyone.
drcrazy4
January 5, 2006, 1:13 pm
finally i can use bitmaps on boards without location problems! yay! well done dev tema
AlienDude
January 5, 2006, 1:25 pm
That is cool and i cant wait till i have access regularly again to help out i have been practicing in C++ and such a lot in the past couple weeks and i hope to do some good for the TK.
Fuzzman
January 5, 2006, 1:58 pm
No more tile based collisons! SWEET!!!
TK Game Boy
January 5, 2006, 3:38 pm
Wow. THis is all great stuff. I can't wait. OI! I hope this stuff doenst interfere with the tutorial I'm writting.
January 5, 2006, 4:02 pm
Wow, I really can't wait until the next version, the TK seems to be getting alot more powerful, but yet it may be getting harder to use, driving away newer members to the community
Slasher
January 5, 2006, 4:08 pm
And I thought nothing was happening backstage... Looks great. Keep up the fantastic work, Devteam.
hehheh, allllrite
January 5, 2006, 5:03 pm
I haven't been eager for the next version until now. Dammit! Now I'm in suspense. But seriously, nice work. Hopefully you'll have it ready soon.
Scott92002000
January 5, 2006, 6:18 pm
muy bein! This news couldnt have come at a better time! I learned that i may be getting a new computer sometime in the next 6 months. now i can restart my project with newer toolkit! ^_^ (the reason i quit toolkit was my computer running to slow to test battles :'( )
MrB
January 5, 2006, 6:29 pm
Great job guys. Colin and Delano, it's hard to express thanks through internet text, but I really appreciate all the time and energy you've given up to consistently improve TK.
Bad Kids
January 5, 2006, 7:39 pm
This is great! Thanks you dev team for showing us these shots. Good work!
Trent
January 5, 2006, 7:51 pm
Wow. Looking at this, it's very obvious that we have really badass stuff coming. The long wait is now very justified. Keep it up, guys.
EzekielRemirez
January 5, 2006, 8:00 pm
Wow, I have to say the Idea of vector based movement and typed variables looks promising. This definitly anwers all my questions about vector collision. WOOHOO!!!
sami
January 5, 2006, 8:43 pm
wow this gonna help so many people with their games! gotta love those 2 guys ;)
????
January 5, 2006, 9:34 pm
Wow guys this is good stuff, good luck with your future development
reignofmagic
January 5, 2006, 9:53 pm
Ok...I'm resuming my work on Chrono Eye as soon as it come out.
catwhowalksbyhimself
January 5, 2006, 10:57 pm
Very impressive. While the time lost is regretable, if the result is as impressive as it looks, it will be worth a delay to make toolkit a truely impressive RPG creator.
Neol
January 6, 2006, 12:54 am
Wow, just wow.
Devastation
January 6, 2006, 5:02 am
You should name it RPGToolkit version 4, not 3.0.7, because I think after seeing those cool stuffs, it deserves the next number =P It's converted to C++ from VB, after all.
Hamster
January 6, 2006, 9:36 am
can partial translucency be turned off and have the character partially opaque instead? also, what are those 3 digit numbers for on the vectors?
Talyn
January 6, 2006, 10:50 am
Thank Christ that the variable types have finally been scrapped! Aye, what are the numbers on the vectors? My most elated praise and thanks to the Dev Team, you're doing us all proud. We'll be patient, honest :P
Ekamp
January 6, 2006, 1:29 pm
I THINK the numbers are point coordinates, but I know nothing of this.
Delano
January 6, 2006, 2:00 pm
Thanks for your comments guys :) Yeah, the numbers are pixel co-ordinates, some people might find them useful references. There will be an option to vary the intensity of the partial translucency, so that could be set to zero to make the characters "partially opaque" instead.
????
January 6, 2006, 8:43 pm
I have a question, I was wondering you could see and use those red, green and white lines on the board editor, like move them around and other stuff
Spyder
January 6, 2006, 8:55 pm
Vector collisions, if they're as easy to create as i think they will be, will make board creation a lot simpler than the old days of setting the tile type of every tile you put down, and the kind of effect it will bring to games will make them much, much funner to play, and create as well. Just look at what tile based collision games look like (the screenshot of JoD) compared to games designed for vector based collision (Heraldry). Those of us not so skilled in pixelating and drawing, can now effectively use 3D rendered backgrounds as boards as well. These changes will only bring more people to use the TK, whereas before, the features that they replaced, likely drove people away. *"the TK seems to be getting alot more powerful, but yet it may be getting harder to use, driving away newer members to the community"*
inumattsha
January 6, 2006, 9:59 pm
Wow, just, wow. This looks like the biggest release of the tk in recent times. It looks amazing. This is going to make me have wet dreams about what the future of the TK will be like, especially by the time tk 3.1 or so is out. It looks amazing. The best just got better. BTW, Spyder, is funner a word?
John@aljo
January 7, 2006, 2:20 pm
"more fun" would be the correct partial phrase. Delano, Colin, wonderful work. Though Delano's pieces have more representation as far as visual goes, I am sure what Colin is doing is just as impressive. Colin is a creature of perfection and because of such I believe what to come for RPGCode itself will be utterly amazing.
(\/)artin
January 7, 2006, 4:43 pm
i'm really impressed...the toolkit 3 is really taking an excellent path ! good luck for the future.
RPGOtaku
January 7, 2006, 10:33 pm
Awesome! Can't wait!
Fuzzman
January 8, 2006, 5:06 pm
Hey, can you guys include an example battle and menu system as a .PRG instead of just .DLL? That would make it a lot easier to learn how to code CBSs and MSs... I think. Thanks.
ViperCat
January 8, 2006, 8:21 pm
...... I am In Awe..... I've been waiting for these features in Version 2...... This is going to be unbelievable... Wow... Wow.. This is going to be..... WOW...
vrn790
January 8, 2006, 8:41 pm
Awsome! i wonder how commands such as tiletype..etc would work...
BlackPanther
January 8, 2006, 11:44 pm
Man. Keep up the good work Colin and Delano. Toolkit Maker is becoming more powerful and powerful everytime. This is probably the best editor I've used so far.
khaldore
January 11, 2006, 2:52 am
*blinks* This... is unbelieveable. Never in my wildest dreams would I have imagined such amazing improvements like these. Colin, Delano (and anyone else that might be behind the scenes, but not mentioned in this article)... supremely well done. Something this good is well worth any length of wait, as far as I'm concerned. - Mike
January 11, 2006, 7:40 am
It's nice to see necessary features finally being added. It's just unfortunate this is going to require me to practically restart my whole game due to the changes. Regarding the addition of partial transparency, I hope that the level of transparency can be adjusted, for example, I would prefer to have it where part of a sprite is under a higher layer, it is not visible at all rather than transparent.
blanel
January 11, 2006, 8:33 am
Hey! Thought you guys were dead but hell, it seems like you've been busy! :P This is all great stuff. TK.s gonna be great when it comes out again. This is actually all the stuff I need in my new game so this is great! I'm using great alot right now but its a good word to describe this. One funny feature would be to implement some of the plugins into the engine such as the Flash plugin. That would kick ass
Xavier
January 11, 2006, 10:24 am
@EB: Yes, partial translucency is adjustable, including to 0.
daman
January 11, 2006, 4:37 pm
As a user of the toolkit I highly anticipate this next update. with that being said, w00t!!111elevenone1!11
comfox
January 12, 2006, 10:58 am
Mm... Looking good. Quite an improvement from old 2.07... ^^ Hopefully my girlfriend and I can have our webcomic up and running smoothly enough to give me time for other projects by the time this comes out... O.O I want to make games! Oh, and the thing that's supposed to update syntax... As the different variable types have been merged, I expect that it will get rid of the !s and $s... But I'd just like to point out that you should build some support, if you haven't already thought of it, into it for literal and numeric variables of the same name; if I have a program with both answer! and answer$ variables, the syntax updater needs to automatically change the name of one; perhaps replacing all occurrences of "!" with "n" and "$" with "l"--or whatever. You see my point, and you'd probably already thought of it anyway. Yeah. Shit... I used the little face with the two html tag markers in it and it deleted the rest of my post. Bad move for me *insert that face here*. Oh well. The rest said something like: hey, while your at it, it would be really nice to have a command that could fill a given region of the screen with a user-defined texture, since using setpixel within programmed bounds and with random color selection from a limited range is way, way, way too slow XD. Anyway, it's looking good. The next release looks something like the best ever :P. Kinda tk4-ish... Actually, if you're recoding it all, it technically should be tk4, shouldn't it? XD stfu n00b, there will never be a tk4. Good job! ^^ -comfox
jake54
January 12, 2006, 8:44 pm
*whistles* vector collision would be a nice upgrade for the toolkit. i can't wait
Dont_Think_So
January 12, 2006, 11:05 pm
Comfox, couldn't you just use a canvas?
comfox
January 13, 2006, 12:29 pm
How would that help? I still wouldn't be able to use whatever I put on there to fill things; and if you mean for preloading, it wouldn't help because the programs this would be used in would include movement; it wouldn't matter if I put the picture on the canvas or on the normal screen, it still wouldn't be able to move or change shape smoothly. Unless there's something else you meant...
whats a computer
January 16, 2006, 12:58 pm
thats gonna be awesome. will definitly make board editing seem more professional and easier to do
Michael J. Hill
January 19, 2006, 11:04 pm
Are you moving the editor to C++ as well, or just the engine itself? I have a project planned once 3.0.7 is released (you'll all find out what it is if I get anywhere with it) and knowing if the editor is remaining VB will help my prioritize the project. Now, the standalone engine will be entirely C++, absolutely no VB code? (I know what other updates say, but I'm one to be careful when it comes to clarification.)
Delano
January 20, 2006, 12:30 pm
The engine is pure C++ now, the editor is remaining as it is (albeit with a new board editor).
Michael J. Hill
January 20, 2006, 5:51 pm
You make my life easier and more difficult at the same time. Oh well, I need some time to relearn some old stuff and learn some new stuff.
vrn790
January 20, 2006, 9:20 pm
I like where all this is going. I wonder what the new commands might include... also, if its not too late to make a suggestion, with all the changes to the board editor...it would be great if you had the option of the screen fading from one board into another when you step on warp tiles (kindof like the transition effects in powerpoint). And also a command to do the same thing, but with images. Anyway, keep up the good work! :)
HughBatey4
January 22, 2006, 6:31 pm
I'm very anxious for these features but will gladly wait as lnog as it takes to get close-to-perfect.
Gerudu Bombshell
January 23, 2006, 4:07 am
amazing! I cant even beleive how siked i was when i looked at this. Im not as siked now, because i just read every single comment. Anywho, i couldnt thank you guys enough for (echo?) keeping this going around the world of your lives. I think this should be tk4. its practically revoloutinary. Man, this will rule. I cant even wait until it comes out! Will the item editor be rewritten aswell? *definetly*
William
January 23, 2006, 8:28 am
What kind of programmersareyoulooking for? I might know some who can help out on the new toolkit. Contact me on MSN.
vrn790
January 23, 2006, 7:40 pm
Just to clarify, it doesn't mater how good the next version of toolkit will be. There wont be a toolkit 4!! The reason for that is because cbm has to declare it toolkit 4 and uhh...well you get the point.
leviathan278
January 24, 2006, 9:58 pm
r u going to allow fmv's or extend the frames of the animations to more than 51 frames
Ifrit Zero
January 26, 2006, 7:39 pm
Holy crap. I came today just to see what was up here, and then this. I'm seriously drooling at the sight of the vector system. It has to be one of the most beautiful things I've ever seen. I
It has been a long while since news was last posted regarding the next release, 3.0.7, which will see the Toolkit have a re-written engine. Considering development still has a long way to go, we thought it best to provide you patient folks with a quick look at what's going on behind the scenes and create some screenshots to demonstrate new features in action.
Jun 6, '05
Apr 5, '05
Mar 24, '05
Jan 22, '05
Dec 27, '04
Dec 15, '05
Sep 15, '05
Aug 24, '05
Aug 20, '05
Aug 17, '05
