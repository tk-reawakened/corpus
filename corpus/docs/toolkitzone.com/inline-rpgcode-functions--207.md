---
kind: doc
id: "toolkitzone.com/207"
site: "toolkitzone.com"
title: "Inline Rpgcode functions"
original_url: "http://toolkitzone.com/library.php?doc=207"
written: null
date_confidence: "unknown"
updated: null
captured: ["20070219211058", "20100101201938"]
author: "Delano"
repliers: []
authors: ["Delano"]
comments_present: 0
f_author: "Delano"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__doc_207_page_1", captured: "20070219211058", sha256: "d67906fa7df1726a65f0e5264a1986aace8df91f3ae820410de532eca30b46c6", wayback_url: "https://web.archive.org/web/20070219211058/http://www.toolkitzone.com/library.php?doc=207&page=1"}
  - {path: "wayback/toolkitzone.com/library.php__doc_207", captured: "20100101201938", sha256: "c35d475dd82cdc1192c7a988bfecb1a406b844d3bd59d50fef401b6bc9219a32", wayback_url: "https://web.archive.org/web/20100101201938/http://toolkitzone.com/library.php?doc=207"}
---

# Inline Rpgcode functions

Browse
As mentioned in the last update, development has slowed this month due to our other commitments, but progress is still steady.
**Inline Rpgcode functions**
Improvements continue to be made to the RPGCode engine's performance, and a new feature has been introduced: inline functions. The idea of inline functions should be familiar to users of languages such as C++; the concept being that the contents of an inline function are substituted (not textually) into the program code wherever the function is called. For instance, consider the following code: The above code will be transformed at run-time (no design-time substitution takes place) into: Use inline functions when the amount of code in the function is small and simple; they may improve the performance of your code! *semantically*
```
inline method add(a, b)
{
return a + b;
}
x = add(y, z);
```
```
x = y + z;
```
**Lighting and shading**
The implementation of the lighting system has changed slightly for the next release, both to make it more user-friendly and to improve its performance. In 3.0.6 there are two styles of lighting available: tile-level lighting applied through the board editor and the screen-level 'ambient level' handled through the board editor and the 'ambient variables' (e.g. AmbientRed!). The method of applying tile-level lighting is tedious at best, since it is set only when laying tiles. A limited capability of creating spotlights and gradients is also available. The ambient level is limited in its scope and is only applied to board and sprite tiles.
Lighting in the next release aims to address these issues; firstly 'lighting' has been split into three groups: tile shading, dynamic lighting and an ambient level. Tile shading describes the tile-level lighting above, but has now been decoupled from the tiles: tile shades can be drawn and manipulated on the board in exactly the same way as tiles can. Previously, a lighting layer existed for each tile layer, each of which was only applied to its associated layer - leading to a lot of redundancy. Tile shades are now applied to a single 'shading layer' that may be located above any tile layer and whose contents is onto tiles on all layers below it. The convention with which lighting is currently applied enables a standard upgrade process, which should suffice for the large majority of lighting users. *cast*
![TBD](vault/documents/1009.png)
*Left - current lighting (3.0.6); right - new lighting*
Dynamic lighting is the name given to lighting objects such as the spotlight and gradient; they are now 'dynamic' in the sense that they are decoupled from tile shading and can be manipulated in the board editor in a more comprehensive manner than at present. Each 'light' is represented on the board through a vector defining its range and axes, whose points can be manipulated like a collision vector. Lights are applied to the tile shading layer in tile units, but are only merged with the shades at run-time. Lights are treated in the same way as tile shades, and are applied to all tiles on all layers below.
![TBD](vault/documents/1010.png)
*A gradient light and a spotlight with the lighting toolbar visible*
Ambient level: presently the ambient level is applied only to tiles on the board and in sprite animations, it is not applied to non-tile images. Applying real-time changes are extremely slow. An attempt to address these issues has been made and a partial solution reached: by utilising the hardware's the colour scheme can be adjusted without altering the game's colour data. Using it, the ambient level is applied to the entire screen: boards, images and sprites as well as menus and battle systems. However it can only be used in fullscreen mode, and so the old implementation remains in windowed mode and for those graphics cards that do not support the gamma ramp. *gamma ramp*
A new function has been introduced to simplify the ambient level: setAmbientLevel(r, g, b); -- this sets the level and redraws the screen. Currently, changes to the reserved variables (e.g. AmbientRed!) must be followed by a ForceRedraw(); to apply them. Note that the reserved variables are still valid.
And finally, to resolve any ambiguities:
- No sub-tile shading or lighting is provided; the graphics engine is not powerful enough at present.
- Tile shading and lights are not applied to non-tile images on boards or sprites.
- A single shading and lighting layer is provided that may be positioned above any layer and casts onto all tiles on layers below.
- Dynamic lights cannot be edited at run-time.
- In windowed mode, the ambient level is applied only to board tiles and tiles in sprites.
- In fullscreen mode, the ambient level is applied to the entire screen.
We would again like to thank you for your support and patience as we work towards the next release.
[![TBD](thumb.php?src=forum/images/avatars/140194639449fe0613c85cf.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=349)
Yay lighting! Although I mostly am looking forward to the speed issues being fixed, it's a pretty good idea to finally get the tile lighting easier to manage. ::Looks at bottom:: Wait... ForceRedraw() currently works in 3.0.6? o_o Or does that mean in 3.0.7? ... ::Leaves to try it again::
[![TBD](thumb.php?src=forum/images/avatars/177829761144e3bf034c1be.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=13238)
This will make lighting that much easier
[![TBD](thumb.php?src=forum/images/avatars/11474909574ae06dca14b48.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=11101)
i wont have to make so many of the same bitmaps with different gradient colors!
[![TBD](thumb.php?src=forum/images/avatars/8292699574a81116350efb.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=141)
I'm in love with the lighting. This is what we've been needing since version 2.07!
[![TBD](thumb.php?src=forum/images/avatars/11817394394a87614066d85.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=6218)
does this mean that Tk 3.0.7 will not be released october? ah man and i really wanted to see FT get started
[![TBD](thumb.php?src=forum/images/avatars/197574015647bb62fd9d5a9.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=4798)
@roy0007: Tk 3.0.7 was never supposed to be released in October. There was, and still is, a rumor that it will be released in Octember. However, no official release date has been issued.
[![TBD](thumb.php?src=forum/images/avatars/2000348661473d1bf40d8e1.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=9970)
@Bagel: There will always be a rumor that it will be released in Octember, because Octember is not a set time. It sounds like October - November, but in reality, it is just like saying it will be released the fourth Thursday of next week. It is nonsensical and represents no certain point on a timeline. And I'm quite excited, both for the inline methods and lighting. I never imagined you would be able to declare a method as a certain type. Kudos!
[![TBD](thumb.php?src=forum/images/avatars/36047520452fd6ed4455a.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=13986)
Yay, that lighting system is looking delightful. And of course, absolutely everyone appreaciates updates that make the software run smoother with no tradeoff. Keep it up, friends.
[![TBD](thumb.php?src=forum/images/avatars/9920395614670bb4110e64.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=6955)
The toolkit is going to be so different. It will be like starting all over again in the learning of the tool. I am just excited as everyone else! I cant wait!!!
[![TBD](thumb.php?src=forum/images/avatars/2000348661473d1bf40d8e1.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=9970)
Speaking of which, will there be other method types other than inline? And seeing as variables do not need (! / $) to denote them as numerical or literal variables, will there be different variables types? That would be beastie. =)
[![TBD](thumb.php?src=forum/images/avatars/11474909574ae06dca14b48.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=11101)
@Enzix Octember stands for November i tought it stood for Deceember?? @Desh im cool
[![TBD](thumb.php?src=forum/images/avatars/206798559647f42249a0065.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=12373)
I cant wait for 3.0.7!I love the features not to mention the shorter methodsTBD
[![TBD](thumb.php?src=forum/images/avatars/951540698452ad61dbb557.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=4944)
@Enzix There will still be different variable types such as: Cat = "1" Cat = 1 (The quotes make a difference) Anyway, nice to see how things are going The lighting is awesome.
TBD
[![TBD](thumb.php?src=forum/images/avatars/49198935143f50e086344d.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=5812)
Its good to see lightinng will be made easier, well I hope 3.0.7 gets released soon
[![TBD](thumb.php?src=forum/images/avatars/2000348661473d1bf40d8e1.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=9970)
@vrn790: I knew that there would be both literal and numerical variables, I just wondered if the variable declaration syntax would be changed to resemble other common programming languages, such as C++. For instance, in many programming languages, variables are declared with the following syntax: identifier; I was just wondering if, since the method type(s) were introduced (inline methods), if there would be other method types besides that. I was also curious as to the syntax for declaring variables. If there is just a "universal" variable type ( variable = "Hi" variable2 = 10 ), so no variable type is needed, or if there is some kind of declaration required ( string variable = "Hi" num variable2 = 10 ). I figure they won't go into all kind of primitive data types, but I just wanted to know about that. ~
*varType*
TBD
[![TBD](thumb.php?src=forum/images/avatars/190135673648b2208aeada6.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=1377)
Sweeeeeeeeeeeeeeeeet. Can't wait!
[![TBD](thumb.php?src=forum/images/avatars/18750184534a18aebc64aee.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=226)
"For instance, in many programming languages, variables are declared with the following syntax: varType identifier; I was just wondering if, since the method type(s) were introduced (inline methods), if there would be other method types besides that" is a calling convention (or lack thereof!). It has nothing in particular to do with the return type of the function. Variables have "hidden" types used for addition but these are deduced from how they are set; there is no need or desire to specify types in declarations.
*inline*
holy crap dudes..... dynamic lighting! what a cool idea
[![TBD](thumb.php?src=forum/images/avatars/158838120745a6a00ea9569.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=148)
It's great to see you guys working on features like this, and I was wondering if in the future (ie releases after 3.0.7) we might someday be able to create animated real-time spotlights on the screen, and things like that?
[![TBD](thumb.php?src=forum/images/avatars/40740951647012c860fa9d.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=240)
Perhaps the term 'dynamic' is a little liberal! Real-time lights and lights cast on sprites is the realm of Direct3D, which would require the ubiquitous graphics engine rewrite. It's certainly viable but it's not something I (or Colin, I expect) are willing to undertake.
[![TBD](thumb.php?src=forum/images/avatars/38676064b23fc5fb1f6c.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=12682)
Yesss...this'll help alot...!!!!!
[![TBD](thumb.php?src=forum/images/avatars/158841209945cb1cb35fd60.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=7783)
I've only worked with the TK and some VB, so what are inline commands? The example just shows a method adding, and thus I don't see the point (esp. of the method, lol) And relating to the board above, would that mean that the character could walk into dark/black areas? I can see that it might give a nice effect of clouds with shadows on the ground, but for other places. I barely understand anything.....Such a loser I am.
AWSOME!!!
[![TBD](thumb.php?src=forum/images/avatars/1217834594459fc4a9a52f8.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=13076)
one minute....so this update....it comes with 3.07 yeah? just the sound of upfdate makes it sound like you can download this rigyt now
[![TBD](thumb.php?src=forum/images/avatars/202350491243172dcbd2811.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=6)
Things like "Progress Update", "development has slowed this month", "lighting system has changed slightly for the next release", "Lighting in the next release", "as we work towards the next release", quite easily suggest it's not ready to download right now. Heh.
[![TBD](thumb.php?src=forum/images/avatars/1509720427477071839fe3f.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=7471)
Administrator Xavier, can you download it right now?
I dont know why this verison is still 3.0.7. This shoud be like 3.1 or something...
[![TBD](thumb.php?src=forum/images/avatars/1509720427477071839fe3f.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=7471)
It's still be 3.0x until version 3.09, probably.
[![TBD](thumb.php?src=forum/images/avatars/13788297874540aeee9f909.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=13491)
I know you have been asked this a thousand times, but when will the 3.0.7 finally get here?! It looks sweet!
October is one day from over, where is 3.0.7? I've heard that it's coming out in "octember" [October] Let's see, it can't be October of 2007 because it's almost done, so it must come out between now, and 11:59:59 Halloween night. Unless the "octember" person was mistaken. I won't re-instal (had it, stopped using it, wanted back, noticed new one) l 3.0.6 because I don't want to re-uninstall it so I can use 3.0.7. I'm wanting it soon, patience is running out!!! Other than time, I think it's doing a good job. When it does come out, hopefully within now and Thanksgiving, I'm going to restart the game that I had in 3.0.6 : When does 3.0.7 come out???
**BTW**
[![TBD](thumb.php?src=forum/images/avatars/1509720427477071839fe3f.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=7471)
If you'd use modern logic, Octember means "Sometime from October to December". It still has 2 months left.
[![TBD](thumb.php?src=forum/images/avatars/202350491243172dcbd2811.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=6)
"Octember" is not an actual month or group of months, it was a passing joke by Colin a long time ago that was adopted by some people in the community. The next release is ready when it's ready.
[![TBD](thumb.php?src=forum/images/avatars/1509720427477071839fe3f.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=7471)
Administrator, you just practically copied what I said in an earlier post. I deserve some sort of Mod-ship for such actions.
[![TBD](thumb.php?src=forum/images/avatars/61553022146dc9b7c29c4e.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=5265)
My, we may have to post disclaimers everywhere. "Octember is NOT a real month. It does not exist. 3.0.7 will be released when it is finished, not in 'Octember.'" "This 'Progress Update' means that the program is NOT ready to be downloaded. It is not available. This simply shows what work we have done (progress) for the current month."
Please read "Percent of Progress" under the Site Discussion Forums. This is a suggestion for the site and one for the toolkit.
[![TBD](thumb.php?src=forum/images/avatars/2013059001465f0dea58e73.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=2789)
Dude ... that had to have been one of the funniest posts I've read in awhile ... and I look forward to reading more of your posts. RDX
[![TBD](thumb.php?src=forum/images/avatars/11523533824419467c49c0c.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=8994)
wow this has changed since i was last on here
[![TBD](thumb.php?src=forum/images/avatars/19128296864181b45a187b1.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=4432)
Ahh, very nice to know we can apply the same lighting to all layers of the map through one command rather than each layer.
Quick Jump
Game Creation | -- Audio | -- Design | -- Graphics | -- | -- 3D | -- | -- Boards | -- | -- Sprites | -- | -- Other | -- RPG Code | -- | -- Canvases | -- | -- Classes | -- | -- Custom Systems | -- | -- Tips & Tricks | -- | -- Functions | -- | -- Other | -- Writing RPG Toolkit | -- News | -- Tutorials Community | -- News | -- Editorials | -- Zone Awards | -- | -- 2008 | -- | -- 2009 | -- Games | -- Contests | -- Interviews | -- Comment | -- Other
Keyword(s)
All Categories Game Creation | -- Audio | -- Design | -- Graphics | -- | -- 3D | -- | -- Boards | -- | -- Sprites | -- | -- Other | -- RPG Code | -- | -- Canvases | -- | -- Classes | -- | -- Custom Systems | -- | -- Tips & Tricks | -- | -- Functions | -- | -- Other | -- Writing RPG Toolkit | -- News | -- Tutorials Community | -- News | -- Editorials | -- Zone Awards | -- | -- 2008 | -- | -- 2009 | -- Games | -- Contests | -- Interviews | -- Comment | -- Other
**Published**
October 15th, 2006
**Views**
221
