---
kind: forum-thread
id: "toolkitzone-forums/7179"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "toolkit 2.x"
skin: "phpbb2"
thread_id: "7179"
title: "Stupid Question, but..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=7179"
written: "2004-08-14T22:27:00"
last_post: "2004-08-17T14:34:00"
date_confidence: "exact"
captured: ["20040912085348"]
author: "nova11"
repliers: ["Master Tamer", "serpentine lord", "xXPurgatoryXx", "Twin Keyblade", "Colosseus"]
authors: ["nova11", "Master Tamer", "serpentine lord", "xXPurgatoryXx", "Twin Keyblade", "Colosseus"]
posts_present: 15
pages_present: [1]
pages_total: 2
posts_per_page: 15
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 2, start: 16, end: 30, url: "http://toolkitzone.com/forums/viewtopic.php?t=7179&start=15", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_75529_amp_", captured: "20040912085348", sha256: "2670975bfe1d4eceb53a1f62046b132c8655acde636d1ac89030f1cfcfa298fa", wayback_url: "https://web.archive.org/web/20040912085348/http://www.toolkitzone.com/forums/viewtopic.php?p=75529&amp="}
links:
  - {url: "http://img.photobucket.com/albums/v299/Nova11/06d8a966.png", status: "external", local: null}
  - {url: "http://img.photobucket.com/albums/v299/Nova11/eea3e71b.png", status: "external", local: null}
  - {url: "http://img.photobucket.com/albums/v299/Nova11/gmail.png", status: "external", local: null}
  - {url: "http://img85.exs.cx/img85/3596/Niloc.gif", status: "external", local: null}
  - {url: "http://sefa-show.tk", status: "external", local: null}
  - {url: "http://twinkeyblade.suddenlaunch3.com", status: "external", local: null}
  - {url: "http://www.danasoft.com/sig/Nova11.jpg", status: "external", local: null}
  - {url: "http://www.geocities.com/ffskies/advert2.gif", status: "external", local: null}
  - {url: "http://www.geocities.com/tamexplayer/antimastertamer.PNG", status: "external", local: null}
  - {url: "http://www.hilaryduff.com", status: "external", local: null}
  - {url: "http://www.rpgadev.com", status: "external", local: null}
  - {url: "http://www.rpgadev.com/header1.jpg", status: "external", local: null}
  - {url: "http://www.toolkitzone.com/games.php?game=404", status: "captured", local: "wayback/toolkitzone.com/games.php__game_404"}
---

# Stupid Question, but...

### nova11 · 2004-08-14 22:27 · #B75503

Hi, I'm the RPGTK maker for Fusionova productions, and i've played a few TK games that allow you to get people in your party, or already start with them. I can't figure out how. I guess im descirbing party members. Also, how do i get it so charectars/party members can wlk around in coversations? very n00bish. So, i need to know the code, or plugin, or methed. Please, explian it lightly so a n00b like me can understand,

### Master Tamer · 2004-08-14 22:33 · #B75506

You cant, or atleast I cant. Every thing freeze if you use the defualt menu. Try a Custom, then See what happens
_________________
MMORPG creation
[![](http://www.rpgadev.com/header1.jpg)](http://www.rpgadev.com)
[![](http://www.geocities.com/tamexplayer/antimastertamer.PNG)](http://www.hilaryduff.com)
![](http://img85.exs.cx/img85/3596/Niloc.gif)

### nova11 · 2004-08-14 22:53 · #B75520

But....Andromeda Sky has tons of stuff like that, and, i'm probably mistaken but the 2.2 Demo had it too...

### serpentine lord · 2004-08-14 23:01 · #B75524

well, for the starting with certain party members, include this code in your start program at the end:
[code]
#AddPlayer("Whoever.tem")
[code][/code]
_________________
Also known as that_kid_sam.
Favorite Quote:
"Oh, Serra... you're the last person I wanted to see." ~Erk from Fire Emblem
"You wanted to see me again! That's so sweet!" ~Serra from Fire Emblem

### xXPurgatoryXx · 2004-08-14 23:18 · #B75529

You have to use the
#Putplayer("whoever", x!, y!, l!)
#push(d!, "Whoever")
#eraseplayer("Whoever")
_________________
It's a chance to strike back at the critical brotherhood and give each his comeuppance for evaluative sins of the past - Judith

### nova11 · 2004-08-15 14:55 · #B75850

could you give an example....like for moving left then up?

### nova11 · 2004-08-16 01:33 · #B76248

bump..... O_O

### nova11 · 2004-08-16 02:07 · #B76276

Okay...i'm getting the idea....create NPCs of the charectars...and make a wander program.....but wander does what is says. Wanders. I need to control where they go, to simulate people actually doing something. Like in Dark Age and Andromeda Sky.

### serpentine lord · 2004-08-16 21:16 · #B76667

uh, so don't use wander. Let's take a look at what purgy said:
#PutPlayer("Whoever.tem", 10, 10,
Ah Im too lazy sorry mon
_________________
Also known as that_kid_sam.
Favorite Quote:
"Oh, Serra... you're the last person I wanted to see." ~Erk from Fire Emblem
"You wanted to see me again! That's so sweet!" ~Serra from Fire Emblem

### nova11 · 2004-08-17 00:43 · #B76797

ARGH!!!!!! That dosent work either!!! I've tried every possible RPGC command for trying to move a guy, in V.2 and V.3 AND IT WON"T Work!!!!
I guess i'm saying i need a working example of sorts.
_________________
badgerbadgerbadger.com
![](http://img.photobucket.com/albums/v299/Nova11/eea3e71b.png)
![](http://img.photobucket.com/albums/v299/Nova11/06d8a966.png)
![](http://img.photobucket.com/albums/v299/Nova11/gmail.png)
[![](http://www.geocities.com/ffskies/advert2.gif)](http://sefa-show.tk)
^Vote for Dragonsgate
![](http://www.danasoft.com/sig/Nova11.jpg)
Guess what i did? I created a 126 file media server.

### Twin Keyblade · 2004-08-17 10:45 · #B77036

Step aside, Andromeda Sky's programmer coming through!
For a conversation I used this sort of thing:

**Code:**

```
#send("example.brd",15,10,1)

#putplayer("Tao",15,10,1)

#push(w,Tao)

#push(w,Tao)

#mwin(" Hey there Raie! Why do we always get stuck in example code?")

#wait()

#mwincls()

#posture(2,Raie)

#mwin(" I dunno. It sucks though.")

#wait()

#mwincls()

#push(e,Tao)

#push(e,Tao)

#eraseplayer(Tao)

#putplayer(Raie,15,10,1)
```

Right, let's walk you through it:
Firstly, the send isn't necessary. I just used it to show where your player is standing.
You then put the player you want using the #putplayer command. Put them directly on top, then walk them away by a couple of steps using #push. It's important that the player you want to appear MUST be in your party at the time!
Then they talk a bit, and then push them back on top of each other. Then use #eraseplayer to get rid of the other character. It's important to then put the original player back onto the square as when you erase the second player, the original usually disappears. That's what the final #putplayer command is for.
If you Unzip the file within the Andromeda Sky program files then you can see all the code/boards/tiles etc that were used in the project. Most of the programs names are self explanitary.
As for your original question about starting with characters already in your party, this is what I did:

**Code:**

```
#addplayer("Kiran")

#addplayer("Geo")

#addplayer("Kristin")
```

Put that in the start.prg and you will start the game with (in this example) Raie [main character], Kiran, Geo and Kristin [support characters].
Hope that helps!
_________________
[Andromeda Sky](http://www.toolkitzone.com/games.php?game=404)
[Andromeda Sky Forums](http://twinkeyblade.suddenlaunch3.com)
I'm stuck in a basement,
Sittin on a tricycle,
Girl gettin on my nerves,
Goin outta my mind,
I thought she was fine,
Can't tell if her body is hers.

### Colosseus · 2004-08-17 10:52 · #B77037

AFAIK, if the character handles are literal, you have to put them inside quotation marks, like this:
#push(w,"Tao")
I've never tried to remove them, though, so I don't know if it works without.

### Twin Keyblade · 2004-08-17 11:02 · #B77039

It does work if you remove them. Half the ones in my game are removed and they still work.
_________________
[Andromeda Sky](http://www.toolkitzone.com/games.php?game=404)
[Andromeda Sky Forums](http://twinkeyblade.suddenlaunch3.com)
I'm stuck in a basement,
Sittin on a tricycle,
Girl gettin on my nerves,
Goin outta my mind,
I thought she was fine,
Can't tell if her body is hers.

### nova11 · 2004-08-17 12:59 · #B77071

Thank you!!!! I will try that. Also, just a note but, I LOVE YOUR GAME. It's really good. Really. Just fix up that first snow environment. you should use a program where you set the letter r to the redraw board commmand or something.
_________________
badgerbadgerbadger.com
![](http://img.photobucket.com/albums/v299/Nova11/eea3e71b.png)
![](http://img.photobucket.com/albums/v299/Nova11/06d8a966.png)
![](http://img.photobucket.com/albums/v299/Nova11/gmail.png)
[![](http://www.geocities.com/ffskies/advert2.gif)](http://sefa-show.tk)
^Vote for Dragonsgate
![](http://www.danasoft.com/sig/Nova11.jpg)
Guess what i did? I created a 126 file media server.

### Twin Keyblade · 2004-08-17 14:34 · #B77084

Lol, thanks! The snow environment was one of the first I set up, so the code there is still pretty basic. I'm in the middle of creating the BS for it at the moment, so Demo 2 is gonna be delayed for a while. Thanks for playing it.
Going back to this thing about " marks, it's neater and better code so get into the habit of using it! I've just got into the bad habit of not putting them there.
_________________
[Andromeda Sky](http://www.toolkitzone.com/games.php?game=404)
[Andromeda Sky Forums](http://twinkeyblade.suddenlaunch3.com)
I'm stuck in a basement,
Sittin on a tricycle,
Girl gettin on my nerves,
Goin outta my mind,
I thought she was fine,
Can't tell if her body is hers.

> [!missing] gap:16-30 · http://toolkitzone.com/forums/viewtopic.php?t=7179&start=15 · never-captured
> Page 2 of 2 was not recovered.
