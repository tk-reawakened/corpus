---
kind: forum-thread
id: "toolkitzone-forums/27012"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Newbie Haven"
skin: "phpbb2"
thread_id: "27012"
title: "Help me please,I would appreciate it."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=27012"
written: "2006-01-31T20:22:00"
last_post: "2006-02-04T16:01:00"
date_confidence: "exact"
captured: ["20060218141726"]
author: "gamekillereater"
repliers: ["Walker-san", "Valgarde", "DrJ", "Whist", "Z"]
authors: ["gamekillereater", "Walker-san", "Valgarde", "DrJ", "Whist", "Z"]
posts_present: 13
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_294067_amp_3Bsid_261ccecbd8cf338342ad29f7ad0a4213", captured: "20060218141726", sha256: "955dd5221e5ba17db74228713c2d6e950b4406ed83294c86afc4c2ca18803e29", wayback_url: "https://web.archive.org/web/20060218141726/http://www.toolkitzone.com/forums/viewtopic.php?p=294067&amp%3Bsid=261ccecbd8cf338342ad29f7ad0a4213"}
links:
  - {url: "http://toolkitzone.com/fileman.php?id=3&file=1207", status: "captured", local: "wayback/toolkitzone.com/fileman.php__id_3_file_1207"}
---

# Help me please,I would appreciate it.

### gamekillereater · 2006-01-31 20:22 · #B294048

I want that the player could press on the board and that on that tile there would be set an item.
But I don't know the command for checking on which tile the player presses with the mouse
I think it would be like this:

**Code:**

```
.......<--(don't know command for checking tile where the player presses on)

putitem(item.itm)

mwin(You set the item!!!)

wait()

mwincls()
```

### Walker-san · 2006-01-31 21:37 · #B294067

mouseClick(x!, y![, wait!])
that's the function you're looking for

### gamekillereater · 2006-02-01 14:20 · #B294222

Thanks but does that check on which tile you click or only the x and y?
I mean does it goes with pixels or with tiles?

### Valgarde · 2006-02-01 14:40 · #B294228

I do beleive thats by pixels Smile

### DrJ · 2006-02-01 21:12 · #B294317

Pixels. Divide by 32 to get the tile coords.

### gamekillereater · 2006-02-02 17:07 · #B294520

**Code:**

```
createItem(:"myitem.itm", 1) )

mouseClick(ix!, iy!,[wait!])

putitem(1,ix!,iy!,1)

mwin(You set the item!!!)

wait()

mwincls()
```

should it be like this but how should i use the command(mouseclick()) that checks on which tile the player presses.
Because i want to set something that is as big as one tile.
And it needs to be set over a tile.
please help

### DrJ · 2006-02-03 01:31 · #B294614

Just use it how it says in the command reference then divide the pixels by 32. BTW you can't use a board that your player can scroll on. Then it won't work.

### Whist · 2006-02-03 03:54 · #B294662

Seems like you lucked out today because:
<http://toolkitzone.com/fileman.php?id=3&file=1207>
CHA CHING!
You don't have to learn anything today!
w00000000000t

### DrJ · 2006-02-03 04:03 · #B294664

Better yet I'll be a pal and post them for you!
GettplayerCoords method

**Code:**

```
G! = 0

e! = 0

method GetPlayerCoords(PlayNum!, PnX!, PnY!)

{

//PlayerX[playerhandle!]! is a global constant, that you cant modify.

//Playery[playerhandle!]! is a global constant, that you cant modify.

PnX! = PlayerX[playNum!]!

PnY! = PlayerY[playNum!]!

ReturnMethod(PnX!)

ReturnMethod(PnY!)

kill(PnY!, PnX!, PlayNum!)

}

GetPlayerCoords(0, G!, e!)

Show(G!)

show(e!)

wait
```

Player move method

**Code:**

```
// BY:AC Your local programmer... GREETINGS!~

// this programs a little buggy but it works decent

// now i will tell you what you need to change NOT MUCH...

// where it says send("YOURBOARD.brd"etc put the board name of your starting place

// and finally where it says YOURCHAR put the handle of your character or

// lets say your characters name is joey its saved as joey.tem

// to load it all you need is to put it in the quotes i have there

// and just the NAME not the extension Ex. .tem get it?

// oh when its set up and working if your wondering why it runs slow its because

// of the comments delete this when you've set it up so its faster

// oh you can also change the gamespeed i just like fast little guys lol

include("getplayercoordmeth.prg")

send("YOURBOARD.brd",5,3,1)

:move

playerspeed(0,0.1)

getplayercoords(0,p_x!,p_y!)

mouseclick(mc_x!,mc_y!)

mc_x! /= 32

mc_y! /= 32

mc_x! = CastInt(MC_x!)

mc_y! = CastInt(MC_y!)

mc_x! = mc_x + 1

mc_y! = mc_y! + 1

pathfind(p_x!,p_y!,mc_x!,mc_y!,moveto$)

push(moveto$,"YOURCHAR") //without.tem for ex. "frap"

branch(:move)
```

### Whist · 2006-02-03 16:06 · #B294736

**TOPLIZARDS8 wrote:**

> Better yet I'll be a pal and post them for you!
> GettplayerCoords method
>
> **Code:**
>
> ```
> G! = 0
>
>
> e! = 0
>
>
>
>
>
> method GetPlayerCoords(PlayNum!, PnX!, PnY!)
>
>
> {
>
>
> //PlayerX[playerhandle!]! is a global constant, that you cant modify.
>
>
> //Playery[playerhandle!]! is a global constant, that you cant modify.
>
>
> PnX! = PlayerX[playNum!]!
>
>
> PnY! = PlayerY[playNum!]!
>
>
> ReturnMethod(PnX!)
>
>
> ReturnMethod(PnY!)
>
>
> kill(PnY!, PnX!, PlayNum!)
>
>
> }
>
>
>
>
>
> GetPlayerCoords(0, G!, e!)
>
>
> Show(G!)
>
>
> show(e!)
>
>
> wait
> ```
>
> Player move method
>
> **Code:**
>
> ```
> // BY:AC Your local programmer... GREETINGS!~
>
>
> // this programs a little buggy but it works decent
>
>
> // now i will tell you what you need to change NOT MUCH...
>
>
> // where it says send("YOURBOARD.brd"etc put the board name of your starting place
>
>
> // and finally where it says YOURCHAR put the handle of your character or
>
>
> // lets say your characters name is joey its saved as joey.tem
>
>
> // to load it all you need is to put it in the quotes i have there
>
>
> // and just the NAME not the extension Ex. .tem get it?
>
>
> // oh when its set up and working if your wondering why it runs slow its because
>
>
> // of the comments delete this when you've set it up so its faster
>
>
> // oh you can also change the gamespeed i just like fast little guys lol
>
>
> include("getplayercoordmeth.prg")
>
>
> send("YOURBOARD.brd",5,3,1)
>
>
> :move
>
>
> playerspeed(0,0.1)
>
>
> getplayercoords(0,p_x!,p_y!)
>
>
> mouseclick(mc_x!,mc_y!)
>
>
> mc_x! /= 32
>
>
> mc_y! /= 32
>
>
> mc_x! = CastInt(MC_x!)
>
>
> mc_y! = CastInt(MC_y!)
>
>
> mc_x! = mc_x + 1
>
>
> mc_y! = mc_y! + 1
>
>
> pathfind(p_x!,p_y!,mc_x!,mc_y!,moveto$)
>
>
> push(moveto$,"YOURCHAR") //without.tem for ex. "frap"
>
>
> branch(:move)
> ```
>

If he's just going to copy and paste it from the forum, then you forgot to tell him the names of the prgs he should save them as...Or to edit the include lines.
GAWD!

### gamekillereater · 2006-02-03 21:15 · #B294782

Sorry but i don't think you know what i mean.
I would like to make a program that sets an item on a tile.
And that the player itself could say where it has to go.
Example:
The player buys a table, he could put it wherever he likes.

### Z · 2006-02-03 21:47 · #B294796

Something more or less on the sides of this

**Code:**

```
*create item

*get the item name

x!=prompt("What tile would you like to put the <itm$> on?(x value)")

y!=prompt("What tile would you like to put the <itm$> on?(x value)")

putItem(item_num!, x!, y!, layer!)
```

### Whist · 2006-02-04 16:01 · #B294991

**Z wrote:**

> Something more or less on the sides of this
>
> **Code:**
>
> ```
> *create item
>
>
> *get the item name
>
>
> x!=prompt("What tile would you like to put the <itm$> on?(x value)")
>
>
> y!=prompt("What tile would you like to put the <itm$> on?(x value)")
>
>
> putItem(item_num!, x!, y!, layer!)
> ```
>

Why not use the mouseclick function in that case?
here:

**Code:**

```
mouseClick(x!, y![, wait!])  *Not sure how this one works, just copy & pasted it from above, never use TK3

putItem(slot!,x!,y!,layer!)
```

Of course, you are going to have to use the CreateItem function once he buys it and specify it has the slot! and also specify layer!.
