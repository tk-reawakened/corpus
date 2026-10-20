---
kind: forum-thread
id: "toolkitzone-forums/30499"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "RPG Code"
skin: "phpbb2"
thread_id: "30499"
title: "Using the cbs documents"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=30499"
written: "2006-06-13T00:05:00"
last_post: "2006-06-19T04:26:00"
date_confidence: "exact"
captured: ["20060619050714"]
author: "Icbim"
repliers: ["Malegnis", "Darrien", "Euix"]
authors: ["Icbim", "Malegnis", "Darrien", "Euix"]
posts_present: 14
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_327388_amp_3Bsid_cd9f43d9186c9e39d55b863ced3a4ece", captured: "20060619050714", sha256: "36f5c5b0842fb94e3537906f412bfecfed5938441a3ad76201c54aea56557c94", wayback_url: "https://web.archive.org/web/20060619050714/http://toolkitzone.com/forums/viewtopic.php?p=327388&amp%3Bsid=cd9f43d9186c9e39d55b863ced3a4ece"}
links: []
---

# Using the cbs documents

### Icbim · 2006-06-13 00:05 · #B326981

Meant for 2.20...but it cant be too far off from 3.06. Nothing that can't be fixed.
I need your help though... I ran it and it came up with a few errors.
The 1st one: Send back to the right X and Y coordinates.
Mine pops up with the little box in the corner saying : Send()x- location less than one as well as with Y.
Here's the chunk of the program where it's gathering the X and Y and stuff:

**Code:**

```
Method Battle(enemy1$, enemy2$, enemy3$, enemy4$, enemy5$, battle_theme$, run!)

{

fade(4)

oldmusic$=music$

oldboard$=Boardtitle[1]$

oldlayer!=playerlayer[0]!

oldx!=playerX[0]!

oldy!=playerY[0]!

midirest

Send(BoardBackground$,1,1,8)

ErasePlayer(playerHandle[0]$)

Midiplay(battle_theme$)
```

and this is the command it's reffering to:

**Code:**

```
Wait(a$)

Send(oldboard$, oldx!, oldy!, oldLayer!) //the command I was reffering to since bold doesn't work in these things :P

Kill(oldx!)

Kill(oldy!)

kill(oldLayer!)

Kill(oldBoard$)

Midirest()

KillUsedVariables()

Midiplay(Music$)
```

Also, the battle background doesn't show up. Here's the command I used when it's gathering info and what not:

**Code:**

```
Method Battle(enemy1$, enemy2$, enemy3$, enemy4$, enemy5$, battle_theme$, run!)

{

fade(4)

oldmusic$=music$

oldboard$=Boardtitle[1]$

oldlayer!=playerlayer[0]!

oldx!=playerX[0]!

oldy!=playerY[0]!

midirest

Send(BoardBackground$,1,1,8) //the command to setup the battle background

ErasePlayer(playerHandle[0]$)

Midiplay(battle_theme$)
```

PS. I know it looks exactly like the one from the document, that's causing i'm typing it straight from the document and am gonna mess around with it when i'm done. This is just practice, since this is my first battle system. I will not be using this in my games. But I will use what I learnt to create one of my own in the future when the practice comes out successfull.
Thank's for help ahead of time.

### Malegnis · 2006-06-13 00:31 · #B326998

i read all that stuff the entire CBS series, and you cant use it at all dont even copy the code period it will mess you up. wigure out what the code is suppost to do then write it yourself from your brain. trust i went through this.

### Icbim · 2006-06-13 00:32 · #B326999

**Malegnis wrote:**

> i read all that stuff the entire CBS series, and you cant use it at all dont even copy the code period it will mess you up. wigure out what the code is suppost to do then write it yourself from your brain. trust i went through this.
>

But I need help. It's working great except for those.
Plus I have no code up on the top of my brain....so someone needs to guide me Smile .

### Malegnis · 2006-06-13 00:43 · #B327007

like this is how the music part are the end (before the methods start)

**Code:**

```
   Send(oldBoard$,oldx!,oldy!,oldLayer!)

   Mediarest(battle_theme$)

   KillUsedVariables()

   Mediaplay(oldmusic$)

   Kill(oldMusic$)
```

because you want to play the old music then kill it, make sure to take old music out of the kil all varibles method.

### Icbim · 2006-06-13 22:04 · #B327312

**Malegnis wrote:**

> like this is how the music part are the end (before the methods start)
>
> **Code:**
>
> ```
>    Send(oldBoard$,oldx!,oldy!,oldLayer!)
>
>
>    Mediarest(battle_theme$)
>
>
>    KillUsedVariables()
>
>
>    Mediaplay(oldmusic$)
>
>
>    Kill(oldMusic$)
> ```
>
> because you want to play the old music then kill it, make sure to take old music out of the kil all varibles method.
>

I never had a problem with the music....It plays just fine....
Everything works except what I listed above.

### Malegnis · 2006-06-14 02:46 · #B327388

**Quote:**

> oldx!=playerX[0]!
> oldy!=playerY[0]!
>

in sdread of that use get player loacation or whatever and store it to oldx and oldy

**Quote:**

> Send(oldboard$, oldx!, oldy!, oldLayer!)
>

this should be fixed

**Quote:**

> Send(BoardBackground$,1,1,Cool
>

make sure its in brd format not in bkg (changed in boardeditor->board information)

### Darrien · 2006-06-15 18:50 · #B327898

Also having the same problem with the playerX[0]! and playerY[0]! variables... for some reason, the first time the Toolkit runs these on any of my programs, it gives me an error stating that the "X value is less than one/Y value is less than one" errors. However, if I run the same program again without quitting the game, it runs perfectly fine. Any reason for this?
Also, neither Vortex nor the Toolkit is registering any GetPlayerLocation function, so if you could elaborate on that a little?
EDIT: forgot to mention, using 3.0.6 if it's important...not sure on Vortex's version, but it should be the same one as the resources page.

### Malegnis · 2006-06-15 21:55 · #B327940

**toolkit Help Files wrote:**

> NAME: Get Target Location
> FORMAT: targetLocation(x!, y!)
> This command gets the x and y coordinates of the 'taret' character or enemy in battle. This is useful for programs that run with special moves because you can put an explosion graphic or something on the enemy or player.
> - x!,y! are the returned x and y coordinates of the player or enemy in battle.
>
> **Code:**
>
> ```
> targetLocation(x!, y!)
>
>
> layerPut(x!, y!, 1, "boom.gph")
>
>
> mediaPlay("boom.wav")
> ```

### Darrien · 2006-06-17 23:08 · #B328514

Heh, must of missed that I s'pose.
So then, would that function work on a normal board as well, since its description states battle? And how would I go about making the character moving on screen the "target" character?

### Malegnis · 2006-06-18 00:49 · #B328530

you only need to find where the "target" player is right before the battle, so that you can send him back to that spot after the battles over... like so....
1. locate player, store to oldx and oldy old board and old layer
2. erase the player from the board.
3. put the player back on the board as well as the rest of your party.(probley towards the right side)
4. swing swords
5. if the player lives send him to the old board old x oldy and old layer.
6. kill all the varibles.

### Darrien · 2006-06-18 05:57 · #B328608

One last thing, and then it'll be working nicely.
For some reason, when I use the command:
#board$=boardtitle[1]$
It won't load the board's name in memory, so when I use the send command to return my characters, it sends them to a white screen. However, during a second battle, it registers the board$ variable (through an mwin command) as "start", the name of the board I'm using as a test, even though the white board is not "start". Any ideas, or is there another way to keep the name of a board in memory?

### Malegnis · 2006-06-18 07:11 · #B328618

**Darrien wrote:**

> One last thing, and then it'll be working nicely.
> For some reason, when I use the command:
> #board$=boardtitle[1]$
> It won't load the board's name in memory, so when I use the send command to return my characters, it sends them to a white screen. However, during a second battle, it registers the board$ variable (through an mwin command) as "start", the name of the board I'm using as a test, even though the white board is not "start". Any ideas, or is there another way to keep the name of a board in memory?
>

thats cause its ment for TK2

**Help Files wrote:**

> NAME: Get Board Name
> FORMAT: dest$ = getBoardName()
> This command gets the board name and stores it in dest$ for later use.
>
> **Code:**
>
> ```
> boardName$ = getBoardName()
> ```

### Euix · 2006-06-18 21:27 · #B328719

Darrien, VorteX is one of the older code editors now. You should use something more updated such as EuixCode², RedRose/Code Impression, or Phoenix. =O

### Darrien · 2006-06-19 04:26 · #B328818

Wow, I'm thinking I need to spend the next few days reading through the entire Manual again, since I seem to of missed so many things. Thanks for the help though.
And I'm trying out both EuixCode2 and Phoenix right now, and so far, they both are running better than Vortex, so thanks for the advise there too, Euix.
