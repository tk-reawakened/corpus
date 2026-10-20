---
kind: forum-thread
id: "toolkitzone-forums/6965"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "general chat"
skin: "phpbb2"
thread_id: "6965"
title: "Battle System Tutorial"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=6965"
written: "2004-08-10T08:51:00"
last_post: "2004-08-14T17:08:00"
date_confidence: "exact"
captured: ["20040824064646", "20040915043355"]
author: "matt72186"
repliers: ["Marc", "Browser", "seveneternal", "TK Game Boy", "xXPurgatoryXx", "Xavier"]
authors: ["matt72186", "Marc", "Browser", "seveneternal", "TK Game Boy", "xXPurgatoryXx", "Xavier"]
posts_present: 9
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_73035_amp_", captured: "20040824064646", sha256: "1c6e65e6eb2e2ab5d844a5c5e176258864e98a572d79d6dff46bb7a18ef10cc1", wayback_url: "https://web.archive.org/web/20040824064646/http://www.toolkitzone.com/forums/viewtopic.php?p=73035&amp="}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_75320_amp_", captured: "20040915043355", sha256: "fdc405a8112d34feb69dde08de0c78a872dc7ca6c2dc198ca7026be60f0c575c", wayback_url: "https://web.archive.org/web/20040915043355/http://www.toolkitzone.com/forums/viewtopic.php?p=75320&amp="}
links:
  - {url: "http://img17.exs.cx/img17/3476/Drink7E.jpg", status: "external", local: null}
  - {url: "http://jupiter.walagata.com/w/tkgameboy/tkrant_soon.gif", status: "external", local: null}
  - {url: "http://tkrants.toolkitzone.com/TKR_home.htm", status: "captured", local: "wayback/toolkitzone.com/tkrants.toolkitzone.com/TKR_home.htm"}
  - {url: "http://www.danasoft.com/sig/LH21222.jpg", status: "external", local: null}
  - {url: "http://www.mysticsoftware.net", status: "captured", local: "wayback/mysticsoftware.net/index-572c95"}
  - {url: "http://www.mysticsoftware.net/images/mscomm_02.png", status: "captured", local: "wayback/mysticsoftware.net/images/mscomm_02.png"}
  - {url: "http://www.toolkitzone.com/blog.php?id=380", status: "captured", local: "wayback/toolkitzone.com/blog.php__id_380"}
---

# Battle System Tutorial

### matt72186 · 2004-08-10 08:51 · #B72613

(a repost of this from Advanced RPG Code board, this didn't very much fit that forum, makes more sense as a general topic Smile)
I know this may seem obvious to most people, but it seems like a lot of people have no idea where to start when it comes to a battle system, so I decided to write up a quick guide to battle systems (not rpg code, just simple explanatory text) I will eventually convert this guideline to a tutorial with examples if anyone is interested.
In most RPG battle systems there is a simple list of tasks to do, the battle system in it's whole may look complex but in reality it is very simple if you break it down into pieces.
Here is a list I have conducted of the basic steps in the battle.
(throughout the list I will refer to any enemy/player/monster on the screen as a sprite)
----------------------------------------------------
Turn-based battle system
- Draw battle screen
- Load player stats
- Load enemy stats
- Determine which sprite has priority to take a turn
- Allow sprite to take an action
- Repeat 4-5 until all enemies HP=0 or all players HP=0
- Determine experience increase
----------------------------------------------------
Now we must go through each step and think about how it can be accomplished
----------------------------------------------------
The Steps
Step 1
- Set a background image to the screen
- Draw all enemies to the screen
- Draw all players to the screen
Step 2
- Loop through all players and load their stats into arrays
Step 3
- Loop through all enemies and load their stats into arrays
Step 4
- Add each sprites speed to their wait_time variable
- Repeat step 1 until one (or more) of the sprites wait_time exceeds some MAX_SPEED constant
- If multiple sprites wait_time exceed the MAX_SPEED choose the sprite with the greatest speed
- If sprites tie in greatest speed then randomly choose among the sprites for one to take a turn
Step 5
- If selected sprite is an enemy conduct an A.I. algorithm to determine the action
- If selected sprite is a player allow player to choose the action
Step 6
- Loop through players, if any player HP>0 skip step 2
- Game over
- Loop through enemies, if any enemy HP>0 skip step 4
- End battle
Step 7
(this part is up to you, although for simplicities sake I will list options for this step)
How to distribute EXP
Each enemy has a number of experience points to give out
- Distribute the total enemy experience to all players
- Divide the total enemy experience among all players
- Only distribute the enemy experience to the player who killed the enemy
- Compare the average enemy level to the average player level as ENEMY/PLAYER and multiply the ratio to the enemy EXP then follow step 1-3 using this as the EXP
the first option is the simplest way and allows equal points to all players
the second option is like the first only distributes less experience to each player
the third option allows exp to be determined by player activity
the fourth option allows less experience to be delivered by lower level enemies and more by higher level enemies
----------------------------------------------------
Following this step would be to determine any stat increases/level increases for each player, the easiest way to do this is to set curves for each stat into algorithms, for example
----------------------------------------------------
Stat determination
LEVEL = the square root of experience
so when experience is 1 you're level 1
when experience is 4 you're at level 2
9 -> 3
16 -> 4
Then you have stats based on level
HP = level*2+98
Level 1 would yield HP 100
level 2 -> HP 102
3 -> 104
and same for each stat
(note I do not recommend those algorithms they were just examples)
One easy way to make the algorithm is to use a calculator (or other graphing utility) to determine the exponential equation that connect 3 points, to determine the three points you need to consider how you want the player to grow, usually you use 0, 50, 100 for the X-coordinates (assuming 100 is the max level and 0 is the initial level) and the Y coordintes are the stats, so for the points you have
(0, initial stat value)
(50, variable stat value)
(100, final stat value)
the variable stat value is what determines the player growth
take the initial stat value, add it to the max stat value, then divide by 2, this gets the average
(initial stat<variable stat<final stat)
If the variable stat value is greater then this average then the player will grow fast then slow down, if it is lower then the player will start by growing slowly then will increase faster later in the game
(variable stat<initial stat<final stat)
If the variable stat is lower than the initial stat, the player will get worse for the first half of progression, then suddenly jump up later on
(initial stat<max stat<variable stat)
If the variable stat is greater than the max stat, the player will grow for the first half, then decrease for the second half of progression
(max stat<variable stat<initial stat)
The player will only get worse
----------------------------------------------------
That's all for now, depending on the Poll results I may or may not continue this tutorial. If this was helpful I will go more into detail about how this is specifically accomplished in RPG Code and include examples as well as a full fledged simple battle system once every example is put together. I will include a section covering the UI of the battle system and explore other battle systems as well (Tactics, Realtime), and lastly will cover an in depth section about Artificial Intelligence and more statistical information

### Marc · 2004-08-10 15:13 · #B72677

I think this should be stickied in the Help board as many people there say: "How do you make a Battle System". It's quite annoying.
_________________
[my blog](http://www.toolkitzone.com/blog.php?id=380)
![](http://www.danasoft.com/sig/LH21222.jpg)
The mouse that knows every thing about your comp! Razz
DeathFlame
Favorite mods (in order)
1)Xavier, 2) Dan, 3)Spyder, 4) Asimir, 5)Doc_wellsy, 6) Woozy, 6) Indy, 7)Seafroggies, 8)R048482, 9)Nick.
Watch the moon every night you can... for Xedret... For him the night will just not arrive.

### Browser · 2004-08-10 15:37 · #B72683

Yes this tutorial would be ver useful to all people who plan to use battle systems.
I agree with Word2 this should be made stickied in the help forum to avoid the same thread poping up every couple of days.
_________________
![](http://www.danasoft.com/sig/LH21222.jpg)

### seveneternal · 2004-08-10 16:25 · #B72701

**Word2 wrote:**

> I think this should be stickied in the Help board as many people there say: "How do you make a Battle System". It's quite annoying.
>

No, these are guidelines for people who actually know what they are doing, but don't know where to start.
People who ask you how to make a bs, well... the only thing you can tell them is to go learn the RPG code.
_________________
http://www.toolkitzone.com/mygames/images/121/893.jpg <http://img17.exs.cx/img17/3476/Drink7E.jpg>
:.::.:...:.:.:..:.:.:..:::..:.:.:....:..:..::::..::.:.::..:.seveneternal@gmail.com.:.:.:.:.:::.:.::.:.::.:.:.:.::.:.:::.:.:..:..:..:.:::::.:.::

### TK Game Boy · 2004-08-10 16:50 · #B72712

Oi. I was going to do this for the TK2 board. Ack. Well it don't matter. Seems you are better at it.
_________________
---
[![](http://jupiter.walagata.com/w/tkgameboy/tkrant_soon.gif)](http://tkrants.toolkitzone.com/TKR_home.htm)

### xXPurgatoryXx · 2004-08-11 02:31 · #B73035

**seveneternal wrote:**

>
> **Word2 wrote:**
>
> > I think this should be stickied in the Help board as many people there say: "How do you make a Battle System". It's quite annoying.
> >
>
> No, these are guidelines for people who actually know what they are doing, but don't know where to start.
> People who ask you how to make a bs, well... the only thing you can tell them is to go learn the RPG code.
>

I agree. If you can understand what you wrote, then you don't need to read it. They have to know 2 + 2, before you teach them what 4 is.
_________________
It's a chance to strike back at the critical brotherhood and give each his comeuppance for evaluative sins of the past - Judith

### Xavier · 2004-08-12 12:35 · #B73892

It's always good to break down such tasks into it's components, like you have, to aid new users to prepare. When it's just "Make a BS" they panic, but in this form it may be less of a stumper.
_________________
Out of sight, out of mind.

### matt72186 · 2004-08-14 09:50 · #B75207

Alright, checking on the positive replies to this topic I have decided to continue this series, I'm beginning work right now on a series of articles and a site specificially for RPG Toolkit battle systems (in RPG Code) and may include the addition of other random RPG Code components (menu system, mini games) thanks for the feedback guys
_________________
[![](http://www.mysticsoftware.net/images/mscomm_02.png)](http://www.mysticsoftware.net)

### xXPurgatoryXx · 2004-08-14 17:08 · #B75320

Hey, cool, I want to see it when it's done.
_________________
It's a chance to strike back at the critical brotherhood and give each his comeuppance for evaluative sins of the past - Judith
