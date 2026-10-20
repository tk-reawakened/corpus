---
kind: forum-thread
id: "toolkitzone-forums/25807"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Code"
skin: "phpbb2"
thread_id: "25807"
title: "[fixed]treasure chest code"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=25807"
written: "2005-12-16T14:04:00"
last_post: "2005-12-20T17:55:00"
date_confidence: "exact"
captured: ["20051230033845"]
author: "kahless"
repliers: ["legomaster88", "TOPLIZARDS8", "Colin", "p90m16mp5a4"]
authors: ["kahless", "legomaster88", "TOPLIZARDS8", "Colin", "p90m16mp5a4"]
posts_present: 7
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_279989_amp_3Bsid_60cfce32d76fe84825cecbbcfebb5aa5", captured: "20051230033845", sha256: "988654a614eb0192af3ef5cd2319826120b488ffe9ac28c340a717049896e128", wayback_url: "https://web.archive.org/web/20051230033845/http://toolkitzone.com/forums/viewtopic.php?p=279989&amp%3Bsid=60cfce32d76fe84825cecbbcfebb5aa5"}
links: []
---

# [fixed]treasure chest code

### kahless · 2005-12-16 14:04 · #B279916

I'm not sure if these codes would work for treasure chests. What I want to do is use one program to set the chest on the board.

**Code:**

```
if(pChestAC1!==0)

{

    createitem("ACchest1", x,y,l)

}

else()

{

    createitem("ACchestOpen", x,y,l)

}
```

and on the item:

**Code:**

```
giveitem("[random item]")

mwin("You got [random item]")

wait()

global pACchest1! = 1

mwincls()

destroyitem("ACchest1")

createitem("ACchestOpen", x,y,l)
```

I think it would work if variables default to zero, if not I could check pACchest1! = 1.

### legomaster88 · 2005-12-16 15:50 · #B279930

So this is supposed to place an chest on a board, 1 variable determines if it has been opened, if it is one value, it places the graphic not yet opened, and if it is another value, it shows that it has been?
Theoretically this code should work. Make sure that the closed value is 0.
That is because when just making a variable in an if statement, the default value is zero until otherwise assigned. Then when the character presses a key next to it, run the program and in it, after character has received item, equal the variable to the open value.
Maybe something like this
If(open! == 0)
{
bitmap("Closed Chest.bmp", 4, 4, 32, 32)
giveItem("Chest Item")
mwin("Got the Item!")
wait()
mwincls
open! = 1
}
ElseIf(open! == 1)
{
mwin("Empty....")
wait()
mwincls
}
Reread to try and make sense.
Some of this might accidentally be in VB code. Sorry, but it should be extremely close to something that works. Enjoy.

### TOPLIZARDS8 · 2005-12-16 21:13 · #B279989

elseif isn't in RPG code, unless it is something on Tk3 only...

### Colin · 2005-12-16 23:40 · #B280022

Indeed, if you use the latest version of the software, you are privy to many features not found in outdated versions, among which is the if...else control structure.

### kahless · 2005-12-19 14:13 · #B280623

Actually, looking at that code, I think you'd run into a problem if you leave the screen and come back. The variables often reset to zero allowing the player to get 375 "Doomsday swords". I still think I need a global var.

### p90m16mp5a4 · 2005-12-19 18:30 · #B280661

If a global variable is what you need, then by dove use it! You can always #kill it later.

### kahless · 2005-12-20 17:55 · #B280968

**Code:**

```
If(open! == 0)

{

*Bitmap("Treasure.bmp", 4, 4, 32, 32)

GiveItem("leather-hat.itm")

MWin("Got the Item!")

Wait()

MWinCls()

Global open! = 1

Wait()

}

ElseIf(open! == 1)

{

MWin("Empty....")

Wait()

MWinCls()

}

Else()

{

MWin("This should never happen")

Wait()

MWinCls()

}
```

I'm not sure what's wrong here, but I keep getting the Debug menu. I think I might need to set up Global Vars somewhere so as it isn't looking for a var that isn't there yet. I could probably set this in Start.prg, but if I have a lot of treasures, it might get messy.
edit: Fixed. declare global first and then change it. me are newb.
