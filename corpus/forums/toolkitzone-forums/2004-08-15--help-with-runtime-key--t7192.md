---
kind: forum-thread
id: "toolkitzone-forums/7192"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "7192"
title: "Help With Runtime Key"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=7192"
written: "2004-08-15T03:38:00"
last_post: "2004-08-15T19:42:00"
date_confidence: "exact"
captured: ["20040925162228"]
author: "Gnarf"
repliers: ["rdemusx", "Ross L.", "KSNiloc", "gcn_zelda"]
authors: ["Gnarf", "rdemusx", "Ross L.", "KSNiloc", "gcn_zelda"]
posts_present: 13
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_76022_amp_", captured: "20040925162228", sha256: "0164c2c9f6157f743508797c975a3d8e3e0bce9614d5ca43bedbca9203de4ca1", wayback_url: "https://web.archive.org/web/20040925162228/http://www.toolkitzone.com/forums/viewtopic.php?p=76022&amp="}
links:
  - {url: "http://cywh.com/ot/", status: "external", local: null}
  - {url: "http://free.hostdepartment.com/t/tk_cafe/", status: "external", local: null}
  - {url: "http://img.photobucket.com/albums/v293/rdemusx/MOTM/newadbar.gif", status: "external", local: null}
  - {url: "http://img.photobucket.com/albums/v293/rdemusx/newvid.gif", status: "external", local: null}
  - {url: "http://img48.exs.cx/img48/8619/kokocompanybanner.png", status: "external", local: null}
  - {url: "http://img53.exs.cx/img53/5207/crazymovie.gif", status: "external", local: null}
  - {url: "http://mansionsofthemoon.myfreebb.com/index.php", status: "external", local: null}
  - {url: "http://mansionsofthemoon.tripod.com", status: "external", local: null}
  - {url: "http://rossleland.deviantart.com", status: "external", local: null}
  - {url: "http://rpgtoolkithole.000k2.com/images/antianti.png", status: "external", local: null}
  - {url: "http://vidoentertainment.com", status: "external", local: null}
  - {url: "http://www.cywh.com/ot/", status: "external", local: null}
  - {url: "http://www.freewebs.com/kokocompany/", status: "external", local: null}
  - {url: "http://www.geocities.com/midget4d2/TK_Cafemove.gif", status: "external", local: null}
  - {url: "http://www.gnarfinion.tk", status: "external", local: null}
  - {url: "http://www.mg.geahost.com/small_theproject.gif", status: "external", local: null}
  - {url: "http://www.mg.geahost.com/tkgforum/index.php?c=5", status: "external", local: null}
  - {url: "http://www.mozilla.org/products/firefox/", status: "external", local: null}
  - {url: "http://www.mysticsoftware.net/images/tk_army.png", status: "captured", local: "wayback/mysticsoftware.net/images/tk_army.png"}
  - {url: "http://www.toolkitzone.com/games.php?game=394", status: "captured", local: "wayback/toolkitzone.com/games.php__game_394"}
---

# Help With Runtime Key

### Gnarf · 2004-08-15 03:38 · #B75696

Ok, I have a runtime key set for "S" so that when the player presses it, it uses a town scroll...
everything is working but i need a program that uses the item when the player presses it...
there was no #useitem...or anything like that....
anyone know a prg that uses the item?
Thanks.
EDIT*
Oh and I thought it would help if i showed it...

**Code:**

```
#include("custom.prg")

#while(usescroll!="S")

{

#itemcount("Town Scroll",tscroll!)

#if(tscroll!<1)

{

#say("You don't have any town scrolls.","","")

}

#if(tscroll!>0)

{

#ques("Are you sure you want to use a town scroll","Yes","No",usetscroll!)

#if(usetscroll!=1)

{

#say("You use a town scroll...","","")

#

}

#if(usetscroll=2)

{

#say("You decide not to use one...","","")

}

}
```

U see the empty spot with the # only...thats where i dont know what to do...and should I use #if or #while for the runtime key? I figured #while would keep it going but then again it wouldnt stop so i will probably change it to #if...
_________________
Gnarf
ED o4
[Gnarfinion.tk](http://www.gnarfinion.tk)
[ToaC](http://www.toolkitzone.com/games.php?game=394)
[![](http://www.geocities.com/midget4d2/TK_Cafemove.gif)](http://free.hostdepartment.com/t/tk_cafe/)
[![](http://www.mysticsoftware.net/images/tk_army.png)](http://www.cywh.com/ot/)
![](http://img53.exs.cx/img53/5207/crazymovie.gif)

### rdemusx · 2004-08-15 05:34 · #B75721

What exactly does the town scroll do? Or supposed to do? Like the actual effect of that item.
RDX
_________________
![](http://img.photobucket.com/albums/v293/rdemusx/MOTM/newadbar.gif)
![](http://img.photobucket.com/albums/v293/rdemusx/newvid.gif)
VISIT WEBSITE: <http://mansionsofthemoon.tripod.com>
VISIT FORUMS: <http://mansionsofthemoon.myfreebb.com/index.php>
VISIT Vi D.O. ENT: <http://vidoentertainment.com>

### Gnarf · 2004-08-15 06:02 · #B75731

Does it matter what it does?
well anyway, its a method that returns the player to the last point where his coordinates were saved, basically every last town he visits...
its perfectly fine and i have tested it 1 million times...just need a runtime key to work...
_________________
Gnarf
ED o4
[Gnarfinion.tk](http://www.gnarfinion.tk)
[ToaC](http://www.toolkitzone.com/games.php?game=394)
[![](http://www.geocities.com/midget4d2/TK_Cafemove.gif)](http://free.hostdepartment.com/t/tk_cafe/)
[![](http://www.mysticsoftware.net/images/tk_army.png)](http://www.cywh.com/ot/)
![](http://img53.exs.cx/img53/5207/crazymovie.gif)

### Ross L. · 2004-08-15 06:12 · #B75734

Not sure if this will answer your question but here goes:
Go into your Main File of your game.
Click the RPGCode tab.
Click More bbutton next to the Run Time General Activation key.
Select a key number.
Input activation key and program to run.
Test and celebrate. I hope this helps.
_________________
ロス レランド Ross Leland
-------------------------------------------------
Current projects:
[![](http://www.mg.geahost.com/small_theproject.gif)](http://www.mg.geahost.com/tkgforum/index.php?c=5)
Mortalis
[My Deviant Art](http://rossleland.deviantart.com)
For my other work, see my website below:
[![](http://img48.exs.cx/img48/8619/kokocompanybanner.png)](http://www.freewebs.com/kokocompany/)

### rdemusx · 2004-08-15 06:15 · #B75736

**Gnarf wrote:**

> Does it matter what it does?
> well anyway, its a method that returns the player to the last point where his coordinates were saved, basically every last town he visits...
> its perfectly fine and i have tested it 1 million times...just need a runtime key to work...
>

Well then. It was a harmless question. Smile
Should just be able to put the program in the main file editor and when the key is pressed it should run. Have you tried setting it to another key?
*just a question don't bite my head off* Wink
RDX
_________________
![](http://img.photobucket.com/albums/v293/rdemusx/MOTM/newadbar.gif)
![](http://img.photobucket.com/albums/v293/rdemusx/newvid.gif)
VISIT WEBSITE: <http://mansionsofthemoon.tripod.com>
VISIT FORUMS: <http://mansionsofthemoon.myfreebb.com/index.php>
VISIT Vi D.O. ENT: <http://vidoentertainment.com>

### Gnarf · 2004-08-15 06:15 · #B75737

Hmmm, well I tried that before but I thought that is for custom menus...
But it works already, i jsut need a program that uses an item..
_________________
Gnarf
ED o4
[Gnarfinion.tk](http://www.gnarfinion.tk)
[ToaC](http://www.toolkitzone.com/games.php?game=394)
[![](http://www.geocities.com/midget4d2/TK_Cafemove.gif)](http://free.hostdepartment.com/t/tk_cafe/)
[![](http://www.mysticsoftware.net/images/tk_army.png)](http://www.cywh.com/ot/)
![](http://img53.exs.cx/img53/5207/crazymovie.gif)

### Gnarf · 2004-08-15 06:16 · #B75739

Im so stupid...screw the method...i will just make it run the program and then take away teh item...
Thanks RDX and i was really mad when i posted the other thing...sorry... Embarassed
_________________
Gnarf
ED o4
[Gnarfinion.tk](http://www.gnarfinion.tk)
[ToaC](http://www.toolkitzone.com/games.php?game=394)
[![](http://www.geocities.com/midget4d2/TK_Cafemove.gif)](http://free.hostdepartment.com/t/tk_cafe/)
[![](http://www.mysticsoftware.net/images/tk_army.png)](http://www.cywh.com/ot/)
![](http://img53.exs.cx/img53/5207/crazymovie.gif)

### rdemusx · 2004-08-15 06:20 · #B75741

No prob man. We all get frustrated. Trust me I know! Smile
RDX
_________________
![](http://img.photobucket.com/albums/v293/rdemusx/MOTM/newadbar.gif)
![](http://img.photobucket.com/albums/v293/rdemusx/newvid.gif)
VISIT WEBSITE: <http://mansionsofthemoon.tripod.com>
VISIT FORUMS: <http://mansionsofthemoon.myfreebb.com/index.php>
VISIT Vi D.O. ENT: <http://vidoentertainment.com>

### Ross L. · 2004-08-15 06:20 · #B75742

Did my post help any at all? Rolling Eyes Oh well. At least I tried. Razz
_________________
ロス レランド Ross Leland
-------------------------------------------------
Current projects:
[![](http://www.mg.geahost.com/small_theproject.gif)](http://www.mg.geahost.com/tkgforum/index.php?c=5)
Mortalis
[My Deviant Art](http://rossleland.deviantart.com)
For my other work, see my website below:
[![](http://img48.exs.cx/img48/8619/kokocompanybanner.png)](http://www.freewebs.com/kokocompany/)

### Gnarf · 2004-08-15 06:23 · #B75744

**Ross L. wrote:**

> Did my post help any at all? Rolling Eyes Oh well. At least I tried. Razz
>

Hey thanks for trying Ross...
and thanks RDX...I hate when I forget the obvious...
*slaps head*
_________________
Gnarf
ED o4
[Gnarfinion.tk](http://www.gnarfinion.tk)
[ToaC](http://www.toolkitzone.com/games.php?game=394)
[![](http://www.geocities.com/midget4d2/TK_Cafemove.gif)](http://free.hostdepartment.com/t/tk_cafe/)
[![](http://www.mysticsoftware.net/images/tk_army.png)](http://www.cywh.com/ot/)
![](http://img53.exs.cx/img53/5207/crazymovie.gif)

### KSNiloc · 2004-08-15 16:11 · #B75882

TakeItem()
_________________
Pawn.

### gcn_zelda · 2004-08-15 16:17 · #B75883

To elaborate on Niloc's answer, use TakeItem() to remove the item and then merely have the program do whatever the item is supposed to do.
_________________
.:: [Get Firefox!](http://www.mozilla.org/products/firefox/)::.
.:: [Off-Topicness!](http://cywh.com/ot/)::.
.::smc42190@gmail.com::.
[
![](http://www.mg.geahost.com/small_theproject.gif)
![](http://rpgtoolkithole.000k2.com/images/antianti.png)

### Gnarf · 2004-08-15 19:42 · #B76022

Yeah I used takeitem and then it runs the program that returns the player...
but the runtme key is not working....i press S and nothing happens and i also set it as a runtime under the main file editor and it still didnt work...any ideas?
_________________
Gnarf
ED o4
[Gnarfinion.tk](http://www.gnarfinion.tk)
[ToaC](http://www.toolkitzone.com/games.php?game=394)
[![](http://www.geocities.com/midget4d2/TK_Cafemove.gif)](http://free.hostdepartment.com/t/tk_cafe/)
[![](http://www.mysticsoftware.net/images/tk_army.png)](http://www.cywh.com/ot/)
![](http://img53.exs.cx/img53/5207/crazymovie.gif)
