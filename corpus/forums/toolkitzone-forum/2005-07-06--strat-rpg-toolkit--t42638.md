---
kind: forum-thread
id: "toolkitzone-forum/42638"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "42638"
title: "Strat-RPG Toolkit?"
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=42638"
written: "2005-07-06T19:27:00"
last_post: "2009-02-07T16:13:00"
date_confidence: "exact"
captured: ["20100102031140", "20100102031534"]
author: "Tomb Lifter"
repliers: ["Flamencos", "Jason Zombolt", "Geep4W", "SuperIsoRPG", "Grindalf"]
authors: ["Tomb Lifter", "Flamencos", "Jason Zombolt", "Geep4W", "SuperIsoRPG", "Grindalf"]
posts_present: 12
pages_present: [1]
pages_total: 2
posts_per_page: 10
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 2, start: 11, end: 20, url: "http://toolkitzone.com/forum/viewtopic.php?t=42638&start=10", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_228643", captured: "20100102031534", sha256: "35edd30301ddb0c13e584edbeb55b88e4e3e9e96f6ffdc297100ced19bc52361", wayback_url: "https://web.archive.org/web/20100102031534/http://toolkitzone.com/forum/viewtopic.php?p=228643"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_466977", captured: "20100102031140", sha256: "a0b631111e8a03ce470658b073b08043774055ac4702d1817a8cd37bce891e51", wayback_url: "https://web.archive.org/web/20100102031140/http://toolkitzone.com/forum/viewtopic.php?p=466977"}
links:
  - {url: "http://toolkitzone.com/games.php?game=2566", status: "never-captured", local: null}
  - {url: "http://www.toolkitzone.com/games.php?image=11410", status: "never-captured", local: null}
---

# Strat-RPG Toolkit?

### Tomb Lifter · 2005-07-06 19:27 · #K228604

**NPC's**

Ok, im new to this RPG making thingy, and i have 4 questions:
-How do i make an NPC
-How do i make the NPC sell me stuff
-How do i make an NPC walk around a board
-How do i make the NPC talk to me
Its all, could you please answer my questions?

### Flamencos · 2005-07-06 19:34 · #K228609

**NPC's**

one word: F1

### Tomb Lifter · 2005-07-06 20:14 · #K228643

**NPC's**

Ok, thanks, i made an NPC, the only problem is that the white color apeears on the animation, i mean, the sprite is there, but the white color around him is also there! How do i get rid of it?

### Flamencos · 2005-07-06 20:25 · #K228648

**NPC's**

when in the animation editor, you see a black block and under that there is a button that says select, press the button and clik the white color in your animation, save the animation and u are done.

### Jason Zombolt · 2009-02-06 00:29 · #K466977

Can RPG toolkit be used for a Strategy rpg like Fire Emblem or Super Robot Taisen?
if so what do I have to do?

### Geep4W · 2009-02-06 02:39 · #K466987

**Jason Zombolt wrote:**

> Can RPG toolkit be used for a Strategy rpg like Fire Emblem or Super Robot Taisen?
> if so what do I have to do?
>

Wrong way of looking at the task.
When building a house, workers don't aim to build a whole house. They take it step by step. They lay the flooring. They make a wall. They make three more walls. They build a roof. Add them all together and they have a house. It is step-wise refinement. You take the large task at hand and break it down into smaller tasks to make it an easier to work with.
Here is an example of how your programing could work:
function StrategyRPG() // Break down the final goal into sections
{
spacewhile(true)
space{
spacespaceplayerTurn()
spacespaceenemyTurn()
space}
}
function playerTurn()
{
spacebuildUnits()
spacemoveUnits()
spaceattackUnits()
spacecheckWin()
}
function enemyTurn()
{
spaceenemyBuild()
spaceenemyMove()
spaceenemyAttack()
spaceenemyWin()
}
//Then break down those functions into more and more basic tasks to
//the point where you can easily code one of them.
//The large task of making a strategy game then becomes several small
//varrious tasks and it is easier to comprehend.
Work with your strategy idea and complete your idea before trying to code it. Know exactly how you want it to work before coding. Going back and changing things around and editing can cause problems and be very time consuming.

### SuperIsoRPG · 2009-02-06 08:16 · #K467019

AI is a bitch.
And then you die.
I'm working on it.

### Grindalf · 2009-02-06 12:52 · #K467027

It could definatly be used to make turn based strategy like you want.
check out of Rage and War an amazing game
<http://toolkitzone.com/games.php?game=2566>
I know this is not tile based(I asume you want tile based) but this will give you some ideas of what is posible with the Toolkit.
also check out tkz hero quest
<http://www.toolkitzone.com/games.php?image=11410>
no demo availible yet though Sad
as long as you are willing to put the time and effort in, the toolkit can do pretty much anything you want.

### Jason Zombolt · 2009-02-06 17:11 · #K467038

Well I just wanted to know if it was possible.
I know I'm not skilled at this right now, yet I just wished to know for a latter game.
Sorry
and I am currently trying the games there, and so far better than what I have now...
Yet I'm not giving up!

### SuperIsoRPG · 2009-02-06 22:55 · #K467066

I wouldn't say "easily" possible. I've had to rewrite pathfinding within RPGCode.
I'm so close to getting to the point where it would be easier to rewrite the whole shabang in C++. Sadly, I have no time to do either at the moment.

### Grindalf · 2009-02-07 15:50 · #K467125

@superiso
I was useing the built in Ai to control items on board, but had problems when they hit a vector(I couldent move them after that) it was working good enough for the enemy ai. It didnt always work nicely for the player though, so i just did it with keyboard controls for the player.

### SuperIsoRPG · 2009-02-07 16:13 · #K467126

I mean, the approach I took was that all the pathfinding is done in the bit where you flood fill the possible positions that a unit can take (Fire Emblem styley), the flood "remembers" the shortest path to each point, then all you need to do is reconstruct the path backwards, rather similar to how you'd do it in graph theory (it's what gave me the idea) It's pretty snappy, normally the draw / process takes less than a second, even for huge fills, which is nice.

> [!missing] gap:11-20 · http://toolkitzone.com/forum/viewtopic.php?t=42638&start=10 · never-captured
> Page 2 of 2 was not recovered.
