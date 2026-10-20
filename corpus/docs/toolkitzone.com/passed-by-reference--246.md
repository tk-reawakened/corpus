---
kind: doc
id: "toolkitzone.com/246"
site: "toolkitzone.com"
title: "passed by reference"
original_url: "http://www.toolkitzone.com/library.php?doc=246"
written: "2007-02-27"
date_confidence: "day"
updated: "2007-02-27"
captured: ["20070219210927", "20100101201828"]
author: "Delano"
repliers: []
authors: ["Delano"]
comments_present: 0
f_author: "Delano"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__doc_246_page_1", captured: "20070219210927", sha256: "9290b864809b764ac270988a6d4ea02f7fe1dc2f5c0df6586e9ccdbc4d3e5299", wayback_url: "https://web.archive.org/web/20070219210927/http://www.toolkitzone.com/library.php?doc=246&page=1"}
  - {path: "wayback/toolkitzone.com/library.php__doc_246", captured: "20100101201828", sha256: "dbcd600f56df169e7200c04ee4324d04056c142229fa4e5a529774aff11c9e78", wayback_url: "https://web.archive.org/web/20100101201828/http://www.toolkitzone.com/library.php?doc=246"}
---

# passed by reference

Browse
Progress Update - December
This last month and half we have been working on a few loose ends and small features; development continues slowly but surely.
Passing variables by reference
As of 3.0.6, variables passed to custom methods could be updated using the ReturnMethod() function, which 'returned' a new value to the given variable, e.g.
method myfunc(x!) { x! = 5 ReturnMethod(x!) } y! = 3 myfunc(y!) show(y!) // Shows 5.
ReturnMethod() also allows the method to return a value, e.g.
z! = myfunc(y!) show(z!) // Shows 5.
Owing both to the new implementation of RPGCode and this ambiguity of ReturnMethod(), its dual-functionality cannot be maintained. Instead, a new way of updating variables inside methods is provided: passing 'by reference'; this brings RPGCode more into line with languages such as C++. I don't want to go into the mechanics of 'references' here - they may be expounded at a later date (or try a net search). The new syntax is:
method myfunc(&x) { x = 5; } y = 3; myfunc(y); show(y); // Shows 5.
An ampersand (&) is prefixed to the desired variable in the method declaration, and any assignment to that variable within the method updates the variable in the program that is passed in. This is the only valid use of the & sign; it cannot be used outside a method declaration and cannot be used to obtain references. ReturnMethod() still functions to give the method a return value, as can the 'return' keyword (as in other languages).
Main File Editor
A couple of token images to break up the text: movement style controls have been added to the main file editor to toggle keyboard and mouse movement. The dual cursor keys - numberpad controls have been replaced by a user-assigned array of key assignments that can handle most keys. Dual control is no longer provided, one must use either the cursor keys or the numberpad keys, or a user-defined set (such as W-A-S-D). Diagonal movement caused by pressing two keys together can be disabled. These cannot be altered at runtime.
![](vault/documents/1087.png)
Secondly, options have been added to allow users to display various vectors to aid debugging and navigation. The colour of navigation vectors can be altered; the colour of board-set vectors cannot (these are intended only for debugging). These cannot be altered at runtime.
![](vault/documents/1088.png)
Lighting
An ammendment to the previous update's assertions is required following tester feedback: code has been added to apply the Ambient Level to board images and animation image file frames in both windowed and fullscreen mode. This feature mirrors the current tile functionality of the ambient level, and is applied to the images' data. This makes the process slow, since the images must be reloaded when the level is changed.
To clarify:
- No sub-tile shading or lighting is provided; the graphics engine is not powerful enough at present.
- Tile shading and lights are not applied to non-tile images on boards or sprites.
- A single shading and lighting layer is provided that may be positioned above any layer and casts onto all tiles on layers below.
- The ambient level is applied only to board tiles, board images (including background image), and tiles and image files in sprite frames, in both fullscreen and windowed modes.
[![TBD](thumb.php?src=forum/images/avatars/158435076745ca63cabc1e5.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=580)
*groan* Why can't I have this thing NOW? I'm dying here.
TBD
[![TBD](thumb.php?src=forum/images/avatars/12437706524b0ef223a9ee4.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=5278)
I have to say, this is advancing. I'm gonna break from what everyone else says with the whole 'HURRY IT TEH F UPXORS!' thing, and say take some more time on this, it's gonna easily be as powerful as any industry-grade utility when you get done. Besides, I wanna make Ander's Journey a full 3.0.6 game cuz I'm funny (or suicidal) like that.
[![TBD](thumb.php?src=forum/images/avatars/17208442064953d9e3b8eb9.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=3770)
Oh my god, that's so cool!
[![TBD](thumb.php?src=forum/images/avatars/854920603444e76d660439.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=76)
pretty nifty. Yall are doing a great job there.
[![TBD](thumb.php?src=forum/images/avatars/49198935143f50e086344d.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=5812)
Sounds good and all. Hope it gets released soon.
[![TBD](thumb.php?src=forum/images/avatars/4668018904a48e8254cff8.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=12580)
you can't see it but right now i'm doing my happy dance!
[![TBD](thumb.php?src=forum/images/avatars/18529276848dd1227db10b.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=334)
That all sounds really cool! I'm loving the new parameter convention since I've always been annoyed by the ambiguity of ReturnMethod. How does mouse movement work? Like an RTS - you click somewhere and the player finds a path there and walks? Would it be possible to have Overlay buttons, etc. drawn onto the screen in such a way that clicking them triggers an action (like opening the inventory or quest book) WITHOUT causing the player to move there? That's something I'd love to have answered. Oh, and speaking of LEFT and RIGHT, I hope you are aware that currently, Get() has these reversed for some reason. When you press left, Get() returns "RIGHT" and vice-versa.
[![TBD](thumb.php?src=forum/images/avatars/40740951647012c860fa9d.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=240)
Thanks for the comments guys. @Moo: Yeah, it's point-and-click movement - have a look at http://toolkitzone.com/library.php?doc=41. There's currently no way to define areas of the screen that would not trigger movement. It would probably be pretty easy, but there's hardly any demand for it =P One might be able to achieve it in a convoluted way using MouseClick() in a thread, though I suppose that entails the previous problems you were having with that function. Yeah, we've known about Get() for a while. It was decided to leave it be in the interests of backwards compatibility.
I'm not too sure... Will this be TK V. 3.0.7 or TK 4?
[![TBD](thumb.php?src=forum/images/avatars/8042760334a370662ddd78.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=670)
Looks good. Hope this works on my computer.
[![TBD](thumb.php?src=forum/images/avatars/122035293744654f76c856b.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=9787)
WOW, I like the way the code is evolving into more of a programming language like c++, but is still geared toward games. Simplicity is the best asthetic. I think this should be toolkit 4, because there is a big difference between an upgrade and a whole new program.
[![TBD](thumb.php?src=forum/images/avatars/9042550445ba8b708d05d.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=11720)
If this gets any better i just might kill over and die. i agree with "TheOne102188" it should be toolkit 4. so many changes. anyways keep it up cant wait.
[![TBD](thumb.php?src=forum/images/avatars/83988205947cf8b21becb6.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=27)
Wow, this is looking really good. The changes in rpgcode seem to be making it much more like "real" languages, which is definately good. I was looking at tk2 the other day, and rpgCode2 is really appalling xD. Good work... BTW, Delano, did I understand you correctly that Get() is going to continue returning "RIGHT" for left and "LEFT" for right? Oh, and do you know whether some form of support for saving quotation marks in string variables or writing them to files is going to be included--and whether arcsin and arccos (or at least arctan) are going to be included after all, or if Colin intends us all to be forced to use his plugin? Oh, and at you tk4-clammering people: It can't be tk4 because of legal issues, thus it is tk3. Haven't you heard that said before? Besides, to be tk4 it would really have to be a complete rewrite of trans3 and tk3, which I don't believe it is. However, to the dev people, why isn't this 3.1.0--it seems like a recoding is a pretty major revision? There was a rumor a while back that you might bump up the version number after testing; does that have any truth to it?
[![TBD](thumb.php?src=forum/images/avatars/40740951647012c860fa9d.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=240)
Comfox: yes, Get() will continue to invert 'left' and 'right'. I haven't seen any quotes-in-strings yet, that's Colin's area. We're not going to add the inverse trig functions, so you'll have to use a plugin I'm afraid.
[![TBD](thumb.php?src=forum/images/avatars/80773225245467e9e0c704.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=112)
There is actually sprite vectors. I guess I never noticed before. Sweet.
LMAO...this is very tempting...I'd say i'm better off without reading these,lol cuz all these updates are giving me urges
[![TBD](thumb.php?src=forum/images/avatars/122739259849be649941662.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=12953)
I want this NOW!
[![TBD](thumb.php?src=forum/images/avatars/978009132469388e5cb7cc.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=5071)
maybe give us just a nibble of power? a partial beta, something to abide this thrist for the... [lvl3.0.7] ULTIMA RPGTK - "in Massive strain to brain trying to comprehend the awesomeness of its relese, you asplode, and become UB3R 1337, eliminating all TKZ staff." :b cant wait for final...[though i may be dead by its relese,REMEBER ME!!!]
While I have only fumbled with the Toolkit a little bit (and that maybe a year ago), I still must say that the creators have been doing quite some terrific job. I might use Toolkit someday, too (if I can convince myself to get out of Flash 8 for a while, lol)
[![TBD](thumb.php?src=forum/images/avatars/5795908664ad79558ced7c.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=14791)
this cant become toolkit 4 because we havent got one actuly good tk3 release
[![TBD](thumb.php?src=forum/images/avatars/19128296864181b45a187b1.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=4432)
Umm... [code]method myfunc(x!) { x! = 5 ReturnMethod(x!) } y! = 3 myfunc(y!) show(y!) // Shows 5.[/code] Is the same as... [code]method myfunc(&x) { x = 5; } y = 3; myfunc(y); show(y); // Shows 5.[/code] ??????????????? You have got to be joking me! Even in C++, this should not hold ture. Since when did "functions" with values of a local scope carry out into the main body of the program without using the RETURN command line? (or are all function varialbes for RPGCode now Global scope now?) I don't know, it just seems really odd to me after reading those lines of code. Now, if you are trying to pass a new variable into the same function for a second set of calculations, why not use RECURSION? I know parsing recursion with all the Pointers in "Free Store" memory is a pain and could cause memory leaks. If this is what you're trying to accomplish, I think it's best to learn how to do that, rather than being able to pass a value from a local function scope to global scope without using the RETURN call. The whole point of a function is the RETURN a value to global scope, and keep any values in the Local scope stay in that scope unless returned using the proper command. If you say: [code]method myfunc(&x) { x = 5; }[/code] then nothing after that function call should have the value 5 right after when you display it to screen. (well, in proper high-level code context that is) If I'm inturpreting this new function implementation incorrectly, please tell me what you mean exactly.
[![TBD](thumb.php?src=forum/images/avatars/202350491243172dcbd2811.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=6)
Dredogol, you seemed to have missed what the code was showing you and also not bothered reading the explanation that goes with it. As it clearly details, the ampersand (&) before the parameter x (as in, &x) denotes it as being . As anyone with experience in programming will know, in the example given this means that instead of x being assigned the value of y, it is actually a reference to y. So if you change the value of x within the function, you're actually changing the value of y. Take time to actually read the text that accompanies the code examples in future. **completely**
**passed by reference**
[![TBD](thumb.php?src=forum/images/avatars/40740951647012c860fa9d.png&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=240)
I'm sorry, but I must take exception at this, dredogol; do you even know what you're talking about? Have you ever used references in C++? Does not look familiar? Please, don't try to sound clever when you don't know what you're looking at.
Code:
```
void func(int &x)
```
[![TBD](thumb.php?src=forum/images/avatars/19128296864181b45a187b1.jpg&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=4432)
Sorry, over the past 2-days, I began reading about , and I learned a crap load about them and how they're used in our university uses. Yes, I now know those are references, and whatever values changes inside the fucntion that was passed in will change on the global scope as well. The interesting thing is, I've hated RESOLVE C++ for the past 1.5 years, and I now after 1-day I love it, lol. Basically, every integer/char/etc. is a which allows for easy datastructure implementation (for us students without all the & and * sings). On top of that, we have something called , were anything done in that function will be passed out (as references) rather than a normal function. Quite useful if you ask me. We don't have to put in all those Pointers or References, all done for us. Only down side is... we were never taught this is how the RESOLVE foundation worked, so I never had any idea how function, or Binary_Trees were coded and used the (free-store) efficiently. **references** **RESOLVE C++**
**reference** **Procedure_Bodies**
**procedure** **heap**
Quick Jump
Game Creation | -- Audio | -- Design | -- Graphics | -- | -- 3D | -- | -- Boards | -- | -- Sprites | -- | -- Other | -- RPG Code | -- | -- Canvases | -- | -- Classes | -- | -- Custom Systems | -- | -- Tips & Tricks | -- | -- Functions | -- | -- Other | -- Writing RPG Toolkit | -- News | -- Tutorials Community | -- News | -- Editorials | -- Zone Awards | -- | -- 2008 | -- | -- 2009 | -- Games | -- Contests | -- Interviews | -- Comment | -- Other
Keyword(s)
All Categories Game Creation | -- Audio | -- Design | -- Graphics | -- | -- 3D | -- | -- Boards | -- | -- Sprites | -- | -- Other | -- RPG Code | -- | -- Canvases | -- | -- Classes | -- | -- Custom Systems | -- | -- Tips & Tricks | -- | -- Functions | -- | -- Other | -- Writing RPG Toolkit | -- News | -- Tutorials Community | -- News | -- Editorials | -- Zone Awards | -- | -- 2008 | -- | -- 2009 | -- Games | -- Contests | -- Interviews | -- Comment | -- Other
![Click for more details.](forum/images/avatars/40740951647012c860fa9d.png)
**Published**
November 30th, 2006
**Views**
792
