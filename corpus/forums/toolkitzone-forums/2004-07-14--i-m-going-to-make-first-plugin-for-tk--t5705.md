---
kind: forum-thread
id: "toolkitzone-forums/5705"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "5705"
title: "I'm going To make First Plugin for TK"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=5705"
written: "2004-07-14T02:17:00"
last_post: "2004-07-16T17:24:00"
date_confidence: "exact"
captured: ["20040920063119"]
author: "Master Tamer"
repliers: ["seveneternal", "Marc", "Woozy", "KSNiloc", "Asimir", "gcn_zelda"]
authors: ["Master Tamer", "seveneternal", "Marc", "Woozy", "KSNiloc", "Asimir", "gcn_zelda"]
posts_present: 14
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_60061_amp_", captured: "20040920063119", sha256: "cf22044bbb669666ab113a8a92d2258fa1a299fc4ebf5eae822ce0f129433917", wayback_url: "https://web.archive.org/web/20040920063119/http://www.toolkitzone.com/forums/viewtopic.php?p=60061&amp="}
links:
  - {url: "http://cywh.com/ot/", status: "external", local: null}
  - {url: "http://img.photobucket.com/albums/v491/Diddums/banner.png", status: "external", local: null}
  - {url: "http://img76.exs.cx/img76/421/Muahahahaha.jpg", status: "external", local: null}
  - {url: "http://img85.exs.cx/img85/3596/Niloc.gif", status: "external", local: null}
  - {url: "http://mars.walagata.com/w/asimir/monkeys.gif", status: "external", local: null}
  - {url: "http://mr-diddums.tk", status: "external", local: null}
  - {url: "http://rpgtoolkithole.000k2.com/images/antianti.png", status: "external", local: null}
  - {url: "http://thanian-nation.com/", status: "external", local: null}
  - {url: "http://thanian-nation.com/dwd/", status: "external", local: null}
  - {url: "http://thanian-nation.com/tkland/", status: "external", local: null}
  - {url: "http://www.cywh.com/ot/", status: "external", local: null}
  - {url: "http://www.geocities.com/tamexplayer/antimastertamer.PNG", status: "external", local: null}
  - {url: "http://www.hilaryduff.com", status: "external", local: null}
  - {url: "http://www.mg.geahost.com/small_theproject.gif", status: "external", local: null}
  - {url: "http://www.mg.geahost.com/tkgforum/index.php?c=5", status: "external", local: null}
  - {url: "http://www.mozilla.org/products/firefox/", status: "external", local: null}
  - {url: "http://www.mr-diddums.tk", status: "external", local: null}
  - {url: "http://www.mysticsoftware.net/images/banner_tkarmy.png", status: "captured", local: "wayback/mysticsoftware.net/images/banner_tkarmy.png"}
  - {url: "http://www.qtk.ip3.com", status: "external", local: null}
  - {url: "http://www.rpgadev.com", status: "external", local: null}
  - {url: "http://www.rpgadev.com/header1.jpg", status: "external", local: null}
  - {url: "http://www.thanian-nation.com/temp/tklandbannerad.jpg", status: "external", local: null}
---

# I'm going To make First Plugin for TK

### Master Tamer · 2004-07-14 02:17 · #B58624

I'm a C++ Newbie, So I'll start with some thing Very easy. It's just an "About" Box. ^_^ but I'll Make it!!!!! It'll be easy to make. I'm also learning about making my own battle System in C++. Then, When I have lots of experince, I'll make a MMORPG plugin. [joke] That is if tk doesn't blow up! [/joke] just kidding, but it'll be very slow If I do. DakrBASIC Can only Support 256 players at once, with overloading. So TK should be able support 20 to 40 players(But DB was wrote in C++ so it is more powerful than VB), and that's on a good day. When (and if) I get around to making this a MMORPG plugin, You'll have to use RPG code limit the areas, cuase if 100s of player load up into one area, all i can say is your TK engine will go *kaboom*. It'll be so slow, it'll take an hour to move arcoss.; you can berly move. For now I'm making an "about" command!
_________________
MMORPG creation
[![](http://www.rpgadev.com/header1.jpg)](http://www.rpgadev.com)
[![](http://www.geocities.com/tamexplayer/antimastertamer.PNG)](http://www.hilaryduff.com)
![](http://img85.exs.cx/img85/3596/Niloc.gif)

### seveneternal · 2004-07-14 02:56 · #B58642

congratulations
_________________
Fake smiles.

### Marc · 2004-07-14 15:46 · #B58802

Well, I took myself about 5 minutes to make (and 10 to figure out what was wrong) to make this program from scratch for you:

**Code:**

```
#include <iostream>

#include <windows.h>

#include <stdlib.h>

using namespace std;

int main()

{

int x;

cout << " I personaly think you are going to screw the TK up. But it's your call\n";

cout <<"Press 1 if you want to continue or 2 to quit\t";

cin >> x;

switch(x)

{

      case 1:

              MessageBox(NULL," press OK to continue", "choice", MB_OK | MB_ICONWARNING);

                  cout << " your going to destroy the fracken TK!";

                  cout <<"\n the warning level for this will be in beep form, so count them!";

                  cout << "\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a";

                  break;

      case 2:

               exit(4);

               return 0;

      default:

      cout <<" shows how smart you are, I as for a 1 or 2 and you give me\n";

      cout <<" a fucking\t" <<x;

      break;

      }

 }
```

Go one, compile and run it!
_________________
![](http://img85.exs.cx/img85/3596/Niloc.gif)
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### Master Tamer · 2004-07-14 16:35 · #B58824

Read that code Word2, and I know what it means >_> Why do think that scewing TK up???
_________________
MMORPG creation
[![](http://www.rpgadev.com/header1.jpg)](http://www.rpgadev.com)
[![](http://www.geocities.com/tamexplayer/antimastertamer.PNG)](http://www.hilaryduff.com)
![](http://img85.exs.cx/img85/3596/Niloc.gif)

### Marc · 2004-07-14 16:37 · #B58826

I think you will Master Tamer. People advanced or intermediate with C++ can't make plugins with that much ease. I can, I just don't have the MFC librarys. Yes Master Tamer you need those.
_________________
![](http://img85.exs.cx/img85/3596/Niloc.gif)
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### Woozy · 2004-07-14 17:39 · #B58887

**Word2 wrote:**

> People advanced or intermediate with C++ can't make plugins with that much ease. I can
>

That makes it sound like only newbs can make plugins (Not only because of the "I can", but also because of what you said before it).
_________________
[Thanian Nation](http://thanian-nation.com/)
[DarkwinterDreams](http://thanian-nation.com/dwd/)
[Quintessential](http://www.qtk.ip3.com)
[![](http://www.thanian-nation.com/temp/tklandbannerad.jpg)](http://thanian-nation.com/tkland/)

### Master Tamer · 2004-07-14 18:06 · #B58899

**Word2 wrote:**

> I think you will Master Tamer. People advanced or intermediate with C++ can't make plugins with that much ease. I can, I just don't have the MFC librarys. Yes Master Tamer you need those.
>

You didn't read EVEN my post. That will be longs ways down the road beofre I do that becuase I'm still learning! >_>
_________________
MMORPG creation
[![](http://www.rpgadev.com/header1.jpg)](http://www.rpgadev.com)
[![](http://www.geocities.com/tamexplayer/antimastertamer.PNG)](http://www.hilaryduff.com)
![](http://img85.exs.cx/img85/3596/Niloc.gif)

### Marc · 2004-07-14 20:05 · #B59007

**Woozy wrote:**

>
> **Word2 wrote:**
>
> > People advanced or intermediate with C++ can't make plugins with that much ease. I can
> >
>
> That makes it sound like only newbs can make plugins (Not only because of the "I can", but also because of what you said before it).
>

Newbies to C++ CAN'T make them, If they can, then I am amazed.
doing a MessageBox isn't that hard. When he can do the more advanced things then he is. Like writing to a file would be abit hard for a newbie. Even with the MFC librarys I would struggle to make one.
_________________
![](http://img85.exs.cx/img85/3596/Niloc.gif)
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### KSNiloc · 2004-07-14 20:07 · #B59011

Maybe that's because you are a newbie. Wink
_________________
[![](http://img.photobucket.com/albums/v491/Diddums/banner.png)](http://mr-diddums.tk)

### Master Tamer · 2004-07-14 20:18 · #B59013

.hack//legend of twlight bracelet. *bites sandwhich*
_________________
MMORPG creation
[![](http://www.rpgadev.com/header1.jpg)](http://www.rpgadev.com)
[![](http://www.geocities.com/tamexplayer/antimastertamer.PNG)](http://www.hilaryduff.com)
![](http://img85.exs.cx/img85/3596/Niloc.gif)

### Marc · 2004-07-14 22:11 · #B59050

**KSNiloc wrote:**

> Maybe that's because you are a newbie. Wink
>

Well, then I am the only newbie that can make a plugin for the toolkit (If I had the MFC librarys).
_________________
![](http://img85.exs.cx/img85/3596/Niloc.gif)
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### Asimir · 2004-07-16 03:05 · #B59781

Rolling Eyes plugins are easy to make. I made one to get info about items and perform some calculations to do with tiles when I'd only started learning C++. I'm pretty sure it the code was right, but my compiler wouldn't work. It was telling me I had 2 errors, no matter how many errors I had. It would say that whether I had 2, 0, 5 or 46234 errors. I tried to compile an essay about osmosis with it and it said I only had two errors. That compiler was a complete pile of shite.
_________________
![](http://mars.walagata.com/w/asimir/monkeys.gif)
[![](http://www.mysticsoftware.net/images/banner_tkarmy.png)](http://www.cywh.com/ot/) [![](http://www.mg.geahost.com/small_theproject.gif)](http://www.mg.geahost.com/tkgforum/index.php?c=5)
[![](http://img.photobucket.com/albums/v491/Diddums/banner.png)](http://www.mr-diddums.tk)

### gcn_zelda · 2004-07-16 17:12 · #B60057

Which is why you download a good compiler(MinGW is a common one)
_________________
.:: [Get Firefox!](http://www.mozilla.org/products/firefox/)::.
.:: [Off-Topicness!](http://cywh.com/ot/)::.
.::(redacted: email)::.
[
![](http://www.mg.geahost.com/small_theproject.gif)
![](http://rpgtoolkithole.000k2.com/images/antianti.png)

### Marc · 2004-07-16 17:24 · #B60061

What is the dev-C++ one? And Asimir, the Tk can't use the plugins without the MFC librarys.
_________________
![](http://img85.exs.cx/img85/3596/Niloc.gif)
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)
