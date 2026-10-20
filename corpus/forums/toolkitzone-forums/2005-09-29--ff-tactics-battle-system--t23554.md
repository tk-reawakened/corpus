---
kind: forum-thread
id: "toolkitzone-forums/23554"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "P90\\'s Coding forum Tuts&source"
skin: "phpbb2"
thread_id: "23554"
title: "FF tactics battle system"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=23554"
written: "2005-09-29T18:33:00"
last_post: "2005-10-21T20:43:00"
date_confidence: "exact"
captured: ["20060111131131"]
author: "X"
repliers: ["eclipze", "Dredogol", "CG-I", "I_Cant_Believe_Its_Me"]
authors: ["X", "eclipze", "Dredogol", "CG-I", "I_Cant_Believe_Its_Me"]
posts_present: 7
pages_present: [2]
pages_total: 2
posts_per_page: 15
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 1, start: 1, end: 15, url: "http://toolkitzone.com/forums/viewtopic.php?t=23554", reason: "capture-failed"}
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_262020_amp_3Bsid_f2c01a272b36fe85bb1c4aa1247f23ae", captured: "20060111131131", sha256: "e6e3e44dc30d9f4b65d7e0d78e8d3ce130c934a053456e09593cee3fcfcbbc30", wayback_url: "https://web.archive.org/web/20060111131131/http://www.toolkitzone.com/forums/viewtopic.php?p=262020&amp%3Bsid=f2c01a272b36fe85bb1c4aa1247f23ae"}
links: []
---

# FF tactics battle system

> [!missing] gap:1-15 · http://toolkitzone.com/forums/viewtopic.php?t=23554 · capture-failed
> Page 1 of 2 was not recovered.

### X · 2005-09-29 18:33 · #B261167

Err, actually "where to start" was covered in the first reply to this topic...

### eclipze · 2005-10-02 10:41 · #B261764

yeah i no that, but i dont understand it properly-

### X · 2005-10-03 11:45 · #B262020

I suggest (again) that you read the tutorials in the resource section, they will help you making first a normal CBS. Once you learn that (how the turn system works, how to add enemies, etc.), the only thing missing is add the stuff relationed to the board (like movement grids, aiming, etc.). For movement system, check the Zelda CBS programs in the resources section, you will only need to use a few lines from the first paragraphs. As for aiming (the range of spells, weapons, etc.), I still haven`t coded it in my CBS, so I can`t really help you much there. If you want, I can give you what I have coded so far, it is not finished yet but it may help you. You (or anyone else) will have to tell me how to send you the program, because I have no idea of how to do it.
Actually, I was planing on uploading my CBS somewhere in this site once it was finished (if it is possible) so that anyone can use it, but again, I have no idea of how to do that either.

### Dredogol · 2005-10-20 03:38 · #B265670

I'm guessing he's lost in which part of the battle system to start off with.
Since you're doing a FFTA battle system...you have something to go by, so the idea are in front of you. Go and play the game again, and look for the following:
MENU:
1) What options are they, and what are the sub-menu options
2) If I select those options, what kind of graphics show up
3) How does it let me interact with the screen.
FIGHT:
1) What kind of movements does it let me make
2) What kind of weapons/spells are there
3) How does it let me aim
4) What battle grahpics are there
5) How does My and Enemy stats change
GRAPHICS:
1) Is the background solid tiles...or animated tiles
2) Are my characters animated or non-moving sprites
3) Are there any "layered" grahpics (i.e. characters behind trees)
There are more major categories, but those are the basics.
If I were you, I'd DRAW what the screen looks like on paper. Once you've done that, you have to have your Background and Characters in the back, and let the menu graphics appear on those of those graphics.
This part will be complicated to do, but you must keep this in the back of your mind.
I personally think the MENU part is the easiest. Maybe import a BMP file as a background to work with (any pic) and draw rectangles or smaller Pic files that look like menu boxes in the way you want them to look.
For the battle menu, you need a hud that'll display something...A hud that is always the same and shows stats. That's the first Menu graphic you have to make. If there's HP and stuff, you'll have to change those values at that part of the screen whenever it needs changing.
If it's time for your turn, you'll need to show a pop-up window that'll give you options. Be able to move a cursor graphic when you move your arrow keys. If you press enter, another sub-menu pops up again. Once you've selected the final option, those menus will close and disapear from the screen returning to the screen before those menus began to pop up.
Basically, you have to think of those individual actions. If my time comes, what graphics show when I DO something. Once i'm done, what graphics go AWAY, and what screen do I return to. Keeping these grahipcs in mind, you must preserve that Graphic so you may return to it. Because drawing on top of those graphics will make them disapear, so you'll need an old copy of the graphic somewhere in my program.
Learn how to use CANVAS. Once you've drawn something on it and wana show the final result...do it. Otherwise, you'll see every little step the computer makes before you get to the final graphic result, which would look silly or odd.
Well, that's a lot, but you MUST read the HELP files and try to understand WHAT each RPG code does. Once you've learned how they work, you can begin to program. We can't help you to program and expect you to understand what's going on until you understand What the code lines mean, and being able to think in Logical ORDER. Everything the computer does is one step at a time.
Exercise, think of how you would program a robot to walk from your front door to your room. (How many steps forwar, left, right...if it sees stairs, should it slow down...keep walking, or go Up/down the stairs...etc) Same idea in how a computer works. You need to provide every stop of the way. Seems annoying...but the final result = your own work. Something to be proud of...and you can always make it better in the future.

### CG-I · 2005-10-20 10:09 · #B265701

That's like the most helpful post I've seen...ever. Very Happy
Hats off to you.

### Dredogol · 2005-10-21 20:20 · #B265899

thanks =)
Just keep things in basic prespective and explain as if you had no clue what you were working on...or something like that.

### I_Cant_Believe_Its_Me · 2005-10-21 20:43 · #B265904

**Dredogol wrote:**

> I'm guessing he's lost in which part of the battle system to start off with.
> Since you're doing a FFTA battle system...you have something to go by, so the idea are in front of you. Go and play the game again, and look for the following:
> MENU:
> 1) What options are they, and what are the sub-menu options
> 2) If I select those options, what kind of graphics show up
> 3) How does it let me interact with the screen.
> FIGHT:
> 1) What kind of movements does it let me make
> 2) What kind of weapons/spells are there
> 3) How does it let me aim
> 4) What battle grahpics are there
> 5) How does My and Enemy stats change
> GRAPHICS:
> 1) Is the background solid tiles...or animated tiles
> 2) Are my characters animated or non-moving sprites
> 3) Are there any "layered" grahpics (i.e. characters behind trees)
> There are more major categories, but those are the basics.
> If I were you, I'd DRAW what the screen looks like on paper. Once you've done that, you have to have your Background and Characters in the back, and let the menu graphics appear on those of those graphics.
> This part will be complicated to do, but you must keep this in the back of your mind.
> I personally think the MENU part is the easiest. Maybe import a BMP file as a background to work with (any pic) and draw rectangles or smaller Pic files that look like menu boxes in the way you want them to look.
> For the battle menu, you need a hud that'll display something...A hud that is always the same and shows stats. That's the first Menu graphic you have to make. If there's HP and stuff, you'll have to change those values at that part of the screen whenever it needs changing.
> If it's time for your turn, you'll need to show a pop-up window that'll give you options. Be able to move a cursor graphic when you move your arrow keys. If you press enter, another sub-menu pops up again. Once you've selected the final option, those menus will close and disapear from the screen returning to the screen before those menus began to pop up.
> Basically, you have to think of those individual actions. If my time comes, what graphics show when I DO something. Once i'm done, what graphics go AWAY, and what screen do I return to. Keeping these grahipcs in mind, you must preserve that Graphic so you may return to it. Because drawing on top of those graphics will make them disapear, so you'll need an old copy of the graphic somewhere in my program.
> Learn how to use CANVAS. Once you've drawn something on it and wana show the final result...do it. Otherwise, you'll see every little step the computer makes before you get to the final graphic result, which would look silly or odd.
> Well, that's a lot, but you MUST read the HELP files and try to understand WHAT each RPG code does. Once you've learned how they work, you can begin to program. We can't help you to program and expect you to understand what's going on until you understand What the code lines mean, and being able to think in Logical ORDER. Everything the computer does is one step at a time.
> Exercise, think of how you would program a robot to walk from your front door to your room. (How many steps forwar, left, right...if it sees stairs, should it slow down...keep walking, or go Up/down the stairs...etc) Same idea in how a computer works. You need to provide every stop of the way. Seems annoying...but the final result = your own work. Something to be proud of...and you can always make it better in the future.
>

Ah man, your awsome. I always get confused where to start when i'm making a bs.
