---
kind: doc
id: "toolkitzone.com/123"
site: "toolkitzone.com"
title: "Progress Update - July 2006"
original_url: "http://toolkitzone.com/library.php?mode=read&doc=123"
written: "2006-07-03T17:49:00"
date_confidence: "exact"
updated: null
captured: ["20060709171457"]
author: "Xavier"
repliers: []
authors: ["Xavier"]
comments_present: 0
f_author: "Xavier"
f_date: "July 3, 2006, 5:49 pm"
f_description: "After a six month hiatus we finally have a new update on the progress of the next Toolkit release, focussing on the glistening new board editor, plus details of a couple changes in the development team. Features discussed include zooming, vector drawing and editing of program attributes."
f_section: "Toolkit 3.x > News"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_123", captured: "20060709171457", sha256: "800919651a93f8ba384454109eece93bd5a8d753497ca0d4eca86ef2d58087fd", wayback_url: "https://web.archive.org/web/20060709171457/http://toolkitzone.com:80/library.php?mode=read&doc=123&PHPSESSID=791c6df67d51ddcefe299c1fee2b9cdd"}
---

# Progress Update - July 2006

By Xavier
**Rebirth of the Board Editor**
It's been six months since the last progress report regarding the next Toolkit release, and understandably some of you are getting impatient once more. Development has been somewhat slow in recent times, but there has been some large strides made, especially with the graphic and board editor aspects of the re-write, courtesy of Delano. This update will focus on the development of the new board editor and, hopefully, be the first of more regular updates from the development team. But before we delve into that, there have been a couple of changes to the team itself. Arriving is forum moderator Oyerth, lending the C++ skills that gave rise to the popular audio plugin, and departing is me, Xavier, as I look to an entirely different TK project to keep me entertained during the summer months. So, onto the board editor... [FMod](http://www.toolkitzone.com/fileman.php?id=3&file=1244)
As you may remember from the previous , the new engine supports vectors and true pixel movement and so the board editor must now provide the necessary tools to support those changes. The decision was made for Delano, whose area of the re-write is predominantly graphics, to code the board editor from scratch, with support from Colin. This was due to the outdated board editor code and also allowed for some frequent user suggestions to be implemented, such as zooming. Note everything is subject to change and still undergoing testing and development, so no doubt things will be added/changed/removed come actual release. [update](http://www.toolkitzone.com/library.php?mode=read&doc=41)
Upon creating a new board you can now specify its co-ordinate system (Fig A), with two types of isometric, rotated and stacked, along with the standard view. Stacked is the same as the current isometric system, where X is left to right and Y is top to bottom, while rotated has X from top-left to bottom-right and y from top-right to bottom-left. The rotated system was requested quite often and allows for easier pixel conversion, just imagine it as a standard board but rotated 45 degrees and so the co-ordinates reflect that.
![](library/images/docs/939.png)
*Fig A. Creating a new board*
The layout has changed in as far as the bottom toolbar has been removed in favour of left and right bars which now hold intuitive buttons for all the new tools (Fig B) and information regarding vectors, items and so on. A new set of icons, subject to change, have been created by Khin for the new editor, allowing for a much more user-friendly presentation of the tools available.
![](library/images/docs/940.png)
*Fig B. New left toolbar*
The tools are separated into four clear groupings. Firstly, the general board tools such as toggling the grid or autotiler. The editor now has an undo feature that does exactly what it says on the tin, although there will be a limit on the depth of the undo tool based on memory restrictions, it should be sufficient. The zoom tool is something most users have been asking, nay...screaming, for since the Toolkit began and it's now here, allowing left/right click zooming for in/out respectively, and also supports mouse wheel scrolling. Below is an example of zooming, the first image (Fig C) shows a normal view of the overworld map from where only a portion of the map is in view, the second image (Fig D) shows the zoomed out version where the entire board is now in view. [Heraldy: Freija](http://www.toolkitzone.com/games.php?game=69)
![](library/images/docs/941.png)
*Fig C. Normal, partial view of Heraldy: Freija overworld map*
![](library/images/docs/942.png)
*Fig D. Zoomed out and complete view of Heraldy: Freija overworld map*
The second group of tools can be described as object tools as they relate to the various objects on a board and so whichever is selected dictates what you can manipulate. For the object tool selected, the selected tool in the third group of icons is used. So if you wish to flood the board with the currently selected tile, you'd click the tile tool (#6), select the flood tool (#13) and then click where ever you wish to flood on the board. A tool previous unseen is the draw tool, which is used for placing tiles and also drawing vectors directly on the board. As you may remember from the , the re-written engine will now work using vector collision, so while you can still place tiles as before, the borders of a tile effectively form a vector in the shape of a 32x32 pixel square. To re-cap, vectors are coloured according to type, so solid is white, under is green and programs are yellow. previous [update]()
When drawing a vector (select #7 then #11) it will either snap to the tile grid or on the exact pixel depending on whether your board is set to use pixel co-ordinates or not. Either way, you can override the default by holding CTRL while drawing and when you're finished drawing the vector you can click the right mouse button to automatically close the vector or again hold CTRL to leave an open vector. The image below (Fig E) shows a vector in the process of being drawn around a curved table and that will eventually be set to solid. Each point of the vector is numbered on the screen and you can select any vector to edit or delete by clicking the select tool (#12) and then left-clicking. You can also select specific points of a vector with a click-drag and move them with a further click-drag, also available on a point or the entire vector is delete (press "del"), subdivide ("Z") that inserts new points at the centre of selected lines and extend ("X") which allows you to draw more points for a vector. It's not just vectors that can be selected and manipulated, it also applies to tiles, items and images that have been placed on the board.
![](library/images/docs/943.png)
*Fig E. Drawing a pixel based vector around a curved table*
You can click-drag over numerous objects and copy, cut and paste using the usual key combinations. In the image below (Fig F), you can see a "floating" image that is selected, you can define the transparent colour of an image using the right bar which is deals with the manipulation of the board, the right contains information and everything on it, allowing quick and easy access. There are four tabs, all relate to the object tools that were covered before; vectors, programs, sprites (items) and images.
![](library/images/docs/944.png)
*Fig F. Selecting a floating image*
The image below (Fig G) shows the program tab on the right bar, populated with the attributes of the currently selected program, which will be signified by bold lines on the board. All programs are accessible via the dropdown menu also at the top, the buttons below allow for quick deletion or duplication of the selected program. You can change the associated program file in properties, allowing you to browse the program folder upon pressing the button to the right. The program vector can be set to be always active or conditionally, with the related properties available to edit such as variable usage and activation type, either stepping on the vector or via key press. The numbers at the bottom detail the pixel co-ordinates of the vector point, these can be edited by clicking a value, pressing "del" to delete and then entering a new value followed by enter.
![](library/images/docs/947.png)
*Fig G. Program tab on the right toolbar*
Well, that's the rundown of the new board editor, there is a full shot of it in action at the foot of this article (Fig H). I'm sure you guys will have many questions relating to the editor, so feel free to ask away in the comments and no doubt Delano or another development team member will be around to answer them. Also remember that you run the risk of having your kneecaps sent to Timbuktu if you ask the forbidden question of when the next version will be released. I can assure you, as and when that is known, you'll be told. Until then, keep the suggestions and questions coming in - they're very much welcome.
* Fig H. The new board editor in action with Delano's Quintessence.![](library/images/docs/946.png)
iFrog
July 3, 2006, 5:59 pm
Freakin' awesome! Good work guys!
TheCPPFreak220
July 3, 2006, 6:00 pm
This may convince me to use the Toolkit again. This is very promising. Good job to those involved.
csir
July 3, 2006, 6:14 pm
Looks nice, and good to see some Quintessence in this article.
Seafroggys
July 3, 2006, 6:19 pm
is this.......a progress update?
Scott92002000
July 3, 2006, 6:53 pm
Nice...I like ^_^
comfox
July 3, 2006, 7:24 pm
Wow, that's looking really good. Just a board editor update, but a glorious one. o.o' About the zoom feature--this doesn't portend directly to the board editor, but here goes: is there any chance of enabling users to use zoom features in-game with rpgcode instead of just in the editor--at least for graphics, if not for vectors and all that? Allowing the camera to zoom in or out, even in TK's 2D boards, could allow some really breathtaking effects. Ah--and this doesn't concern me, but it's bound to come up at some point and a) I want credit for being the first to say it and b) it would probably be easiest to do it now instead of six versions down the road: there should be a way to zoom out, just as you've implemented now, but with adjacent boards showing. I realize that the TK lets you connect boards to each other one-way, and so it may not be geometrically possible, but perhaps some sort of editor that could let you choose what zoomed-out boards to display, or perhaps just a program that would check and only allow the display if your boards are connected to each other both ways. People are going to want world maps that are literally zoomed out versions of their boards, and with large games it isn't going to be feasable to go into every board, zoom out, print screen, paste into a graphics editor, cut out the board picture, and align it with other boards. Anyway... That second is just a suggestion, because people are probably evenentually going to want it and it might be easier to do now than later. The first is something I actually would very much enjoy. ^_^ Sorry to bombard you with suggestions for further work. It's looking really great as it is!
Dont_Think_So
July 3, 2006, 8:12 pm
*Has Featuregasm* Any hopes for unidirectional solid vectors? In other words, you can step over in one direction, but not the other? Also, will programs react as soon as the player steps on it (the vectors intersect), or only once the entire character (or the character's mask) is within the area?
Seafroggys
July 3, 2006, 9:27 pm
i like comfox's suggestions, especially the first one.
UltimaWizard
July 3, 2006, 10:21 pm
Simply incredible. I know I've been something of a nag about this, but some updated navigational RPGCode (GetDirection-style functions, GetFrame-style functions, especially) would be most welcome and useful. Also, adding in camera panning would also be most helpful. Besides that...TK3.0.7's Octember release is gonna simply be great. ^_^
Sir Pimpalot
July 3, 2006, 11:20 pm
This is awesome..amazing..great.....super..........can't think of any other words! Kinda reminds me of a really advanced version of a rpg maker board editor. Edit: Oh, by the way, I know this is a board editor update but will the code explanations in the quick reference be updated?
slipknot42388
July 3, 2006, 11:43 pm
I got question will this version fix the graphics problem people have with the toolkit when they have windows ME such as with the random images showing up on the character?
bound4ct
July 3, 2006, 11:43 pm
This is going to be such an amazing update, I'm curious as to why this is only 3.0.7 when the update is major enough to warrent a 4.0.0 because of the significance... Also, where's Timbuktu and is the climate nice there?
Jarty
July 4, 2006, 12:37 am
Question: with the addition of vectors, would it now be possible to allow for varying encounters on the same board through another feature add-on or through a user-made program? For instance, on one part of the board (within a vector) a certain set of enemies levels 4-6 are set up to appear, whereas on another part enemies levels 7-9 are set up to appear. I'm just hoping for the ability to do this so that localized enemy set-ups could be created for, say, a world map with different areas (desert, forest, etc.) on the same board.
Greg
July 4, 2006, 1:01 am
AMAZING!!! Suggestion: The return of 16x16 tiles (and not crappy stretched out ones, but true 16x16)
Ivan
July 4, 2006, 1:03 am
Wow this is awesume! You guys are doing great!
Bad Kids
July 4, 2006, 3:10 am
I'm lov'n this! But I'm a afraid this will cause more bugs to emerge and this has to be too good to be true! :O
spelmo
July 4, 2006, 4:35 am
its looking wicked but one thing though is that the toolkit is proggressively getting hard to use. ppl new to the toolkit may no understand well
Talyn
July 4, 2006, 5:27 am
Looks promising. Welcome to Oyerth to, congratulations mate =)
Delano
July 4, 2006, 8:36 am
Thanks for your comments guys. I'm going to have to delay answering your questions for a couple of days since I'm away today and tomorrow, but keep them coming. Congratulations to Oyerth on his joining - we're looking forward to seeing what you come up with!
SuperIsoRPG
July 4, 2006, 12:00 pm
pixel-based vector... right... (takes Xavier and Colin hostage) Release TK 3.0.7 right now or you'll be sorry!
drcrazy4
July 4, 2006, 12:58 pm
This looks GREAT. I really do hope it comes out in October though as I want a demo for the winter expo.
csir
July 4, 2006, 1:01 pm
@ SuperIso- if it were released right now we would all be terribly dissapointed. @ bound4ct- There will never be a 4.0.0, first off I dont believe this would merit the amount of change that is happening and second there will never be a 4.0.0 due to some legalities, I believe.
TK Game Boy
July 4, 2006, 2:27 pm
Über awesome. I LOVE IT! OI! Feels just like yesterday I'm saying TK2 will live forever and now I'm awaiting the next TK3 release. You guys kick ass. Though I wonder, with all these new features if the TK is straying from it's philosophy.
Cuzit
July 4, 2006, 3:04 pm
0_0 Wow, this is freakin' awesome! I was looking forward to it before, but now, I'd kill for this! It's just amazing! If not with this release, then a few more releases down the road this will be the best game maker on the internet! And it's free! Please have this out by next year, I can't wait to use this!
Mick
July 4, 2006, 6:44 pm
Amazing! Good job TK Devs!
????
July 4, 2006, 7:38 pm
Wow this is really good stuff, I might come back when 3.0.7 is released, keep up the good work
Oyerth
July 4, 2006, 8:08 pm
" " Thanks! " " Hehe. Thanks. :) Also, the article somewhat mentions that my FMod plugin was a C++ plugin...which it's not (it's a VB plugin). :) *Looks promising. Welcome to Oyerth to, congratulations mate =)*
*Congratulations to Oyerth on his joining - we're looking forward to seeing what you come up with!*
William
July 5, 2006, 6:31 am
Wow, it actually looks very good. Great Job.
Blob Dude
July 5, 2006, 2:35 pm
Wow this is looking great! It's making me think I'll make a game again... when it's all done and ready of course! :D
Omnioni
July 5, 2006, 6:40 pm
Sex! This is pure, and simple sex!
Telemachus Rhade
July 5, 2006, 7:25 pm
I am SO looking forward to using this! This is going to be a revolution in game makers! Thanks, Oyerth! I'll keep my eyes wide open for this!
Dan
July 5, 2006, 10:13 pm
Soooo.... When's it out? ;)
Hamster
July 5, 2006, 11:05 pm
ZOMFG! this is truly amazing. The tk is gojng to be by far the number one tool for regular people who make 2d rpg games to do so. like many i can only think how this is going to make the TK really hard to use. But its all for the best. we really should figure out a way to better help out the newbs who wander in here confused....
Montai
July 6, 2006, 12:30 am
Dan, I guess when Jesus comes back...(never) I'm so proud of you guys... The toolkit is looking more and more professional every time we see an update. I'm really supprised you all did this much.(Seeing as you all arn't being paid anything. And it's summer break!) Good job you all, and thank you. btw: I just might wait until this is out before I continue working on my game...
peace
July 6, 2006, 5:28 am
Nice though i would personally ike to here more about the changesand additions to rpg code.
Delano
July 6, 2006, 8:33 am
Okay, to address some of your questions: @comfox 1) There are no plans to implement zooming in-game; any such feature would come at a cost to performance. Maybe it's something to consider to subsequent releases. 2) Whilst displaying multiple boards in the editor might be nice, it sounds a bit superfluous. Don't most people use specific tilesets for their world maps? In any case, an Export Image feature is intended for the board editor, which would facilitate doing this in an external editor. @Dont_Think_So 1) Unidirectional vectors are partially implemented but there are a couple of technical issues preventing them working in particular situations, so they're indefinitely on hold. 2) Programs trigger when their vector first intercepts the program's vector - this emulates the behaviour of previous program triggering. @UltimaWizard Your suggestions don't sound too taxing; they could probably be achieved through a plugin. I think adding functions to the engine itself is only justified if they are difficult to write in a plugin, or if there is a high demand for them. @Sir Pimpalot Yes, we will try to [remember to] update the code reference. @slipknot42388 It's unlikely that the rewrite will fix the Win9x bug because the problem is in the Win9x software rather than the Toolkit code. @bound4ct Timbuktu is in Mali, Africa. It's hot and sandy :P @Jarty Yes, you could write a program to launch the battle system via the Fight() function, which takes the enemy level as a parameter. You could set programs on the board that set a global variable that holds the enemy level, and pass that into Fight(). @Greg I'm afraid there's no framework in the graphics engine for drawing 16x16 tiles; it would be a large amount of work to implement it. It's possible, but I'm not doing it ;P @spelmo More advanced features require more complex interfaces to create them. I'm sure new users will be smart enough to get the hang of the editor; it's the current users who'll complain now that everything's been rearranged ;)
July 6, 2006, 7:19 pm
I may have missed it in the last few progress updates (They have been quite lengthy), but has multiple tile drawing been added? Fury2 used to allow you to drag and select a segment of a tileset comprised of multiple tiles (Like a tree, for example) and draw them to the board at once. It really sped up board design, would be nice to see this added to TK. Everything so far is looking tasty, though.
Trent
July 6, 2006, 10:26 pm
All of this is awesome. I'll hold off moving to Game Maker for a while, if not only because I don't know how GM will handle it and I don't wanna get pissed off when it doesn't work. Hmm... I think my kneecaps need a vacation. When's the next version coming out?
daman
July 6, 2006, 11:48 pm
OMFG!!! I love the toolkit and cannot wait till the release of 3.0.7!!!!!!!!!!!!!!!!!!!!!!!! A release date would be highly anticipated but it would be better just to have it be one suprise!!!!! **BIG**
comfox
July 7, 2006, 6:34 am
Has rpgcode already been changed for the upcoming (and upcoming... and upcoming...) release? Colin noted that the distinction between numeric and literal variables is going to be removed... And with major changes like that (ESPECIALLY that one in particular), I wonder how backwards compatable it's going to be. What if we have var! and var$? Will there be a program that goes through and changes ! to "n" and $ to "l" in all cases, even in parameters and If statements? This news was about the board editor, which looks great ^^, but I have been wondering about the rpgcode thing. Will it be functionally backwards compatable, or is there something potential 3.0.7 code needs to have specially done to ti? o.o' Thanks ^^.
Xavier
July 7, 2006, 7:55 am
@comfox The last progress report covered backwards compatibility, albeit very briefly, and confirmed that redundant type characters can be automatically removed. Maybe next update there will be a more indepth review of RPG Code changes.
comfox
July 7, 2006, 8:23 am
Yes... I'd forgotten about that, thanks. But I'm still concerned about variables with the same name; if it just removes the characters, var! and var$ will end up being considered the same variable, and that will mess a lot of stuff up. I haven't heard anyone mention this or explain precisely how the whole thing will work, so I was concerned that it might have been overlooked and curious as to what the changes are.
Fuzzman
July 7, 2006, 4:54 pm
Wow.
Colin
July 7, 2006, 6:34 pm
Comfox, I'm skeptical whether anyone would actually be silly enough to use both var! and var$ (this is not allowed, for example, in BASIC, where it is obviously derived from). We cannot change them to say, numVar and strVar, although that would be desirable, because it would confuse users who are just looking to make their code work. Perhaps an option to do that would satisfy everyone? And I agree that an article on RPGCode in 3.0.7 would be useful. There are a variety of things that need to be articulated and not too much to worry about.
comfox
July 8, 2006, 5:21 am
Okay, thank you ^^.
legomaster88
July 9, 2006, 12:10 pm
This seems like it's gonna take a little time to readjust to. How long would you guys say it'll take to redajust? a week or two? (i'm talking about the whole system. I know it's not done yet, but an estimation if at all possible? thx) I second an article on 3.0.7's RPGcode! Anyway, 3.0.7 seems like all that, a bag of chips and a soda!! =) Pretty sweet!
After a six month hiatus we finally have a new update on the progress of the next Toolkit release, focussing on the glistening new board editor, plus details of a couple changes in the development team. Features discussed include zooming, vector drawing and editing of program attributes.
**Recent News**
Jan 5, '06
Jun 6, '05
Apr 5, '05
Mar 24, '05
Jan 22, '05
