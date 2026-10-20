---
kind: forum-thread
id: "toolkitzone-forums/23223"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Advanced Coding"
skin: "phpbb2"
thread_id: "23223"
title: "Battle System Still Under Development"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=23223"
written: "2005-09-05T07:11:00"
last_post: "2005-09-07T13:34:00"
date_confidence: "exact"
captured: ["20051029105816"]
author: "William"
repliers: ["new game maker", "Noob From The Grave", "p90m16mp5a4", "Tao-Kun", "????"]
authors: ["William", "new game maker", "Noob From The Grave", "p90m16mp5a4", "Tao-Kun", "????"]
posts_present: 15
pages_present: [1]
pages_total: 2
posts_per_page: 15
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 2, start: 16, end: 30, url: "http://toolkitzone.com/forums/viewtopic.php?t=23223&start=15", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_254647_amp_3Bsid_7cde889a94523dc3911efb6795047320", captured: "20051029105816", sha256: "930befd25a5c097a2ee3095479050fa9461c83b0d062871ae7f82eaae4f02898", wayback_url: "https://web.archive.org/web/20051029105816/http://www.toolkitzone.com/forums/viewtopic.php?p=254647&amp%3Bsid=7cde889a94523dc3911efb6795047320"}
links: []
---

# Battle System Still Under Development

### William · 2005-09-05 07:11 · #B254178

I kinda took a small break from it, but started working today again, not I have all the AI done, all thats left is the damage part, death method, gain stat method and character walking into enemy method.
Can you see anything that misses, or any bugs you wanna correct?

**Code:**

```
//Made by William from Toolkitzone 2005

//Character Varibles

CharStartX!=5

CharStartY!=5

CharSizeX!=32 //Not implemented

CharSizeY!=32 //Not implemented

CharNorth$ = "CharNorth.bmp"

CharSouth$ = "CharSouth.bmp"

CharWest$  = "CharWest.bmp"

CharEast$  = "CharEast.bmp"

CharR!=255

CharG!=255

CharB!=255

//Board Varibles

BattleBoardMapName$ = "BattleMap.brd"

XStart!=0

YStart!=0

XEnd!=13

YEnd!=9

GrassTile$ = "Grass.bmp"

//EnemyOptions Varibles

EnemySpeedTime!=10 //Not recommended to have it above 50

EnemyAmount!=2 //Max 4 Enemies for normal users.

EnemyR!=255

EnemyG!=255

EnemyB!=255

//Enemy 1 Stat Varibles

EnemyName[1]$="Goblin" //Not implemented

EnemyGraphic[1]$= "CharSouth.bmp"

EnemyStrength[1]!=5

EnemyMinimumDmg[1]!=1

EnemyDefence[1]!=3

EnemyStartX[1]!=4

EnemyStartY[1]!=2

EnemySizeX[1]!=32

EnemySizeY[1]!=32

//Enemy 2 Stat Varibles

EnemyName[2]$="Skeleton" //Not implemented

EnemyGraphic[2]$= "Enemy2.bmp"

EnemyStrength[2]!=5

EnemyMinimumDmg[2]!=1

EnemyDefence[2]!=3

EnemyStartX[2]!=2

EnemyStartY[2]!=2

EnemySizeX[2]!=32

EnemySizeY[2]!=32

//Enemy 3 Stat Varibles

EnemyName[3]$="Maze" //Not implemented

EnemyGraphic[3]$= "Enemy3.bmp"

EnemyStrength[3]!=5

EnemyMinimumDmg[3]!=1

EnemyDefence[3]!=3

EnemyStartX[3]!=5

EnemyStartY[3]!=7

EnemySizeX[3]!=32

EnemySizeY[3]!=32

//Enemy 4 Stat Varibles

EnemyName[4]$="Ghost" //Not implemented

EnemyGraphic[4]$= "Enemy4.bmp"

EnemyStrength[4]!=5

EnemyMinimumDmg[4]!=1

EnemyDefence[4]!=3

EnemyStartX[4]!=8

EnemyStartY[4]!=4

EnemySizeX[4]!=32

EnemySizeY[4]!=32

//Start Mehotds and Commands

ViewBRD(BattleBoardMapName$) //Command

ShowEnemies() //Method

SetImageTransparent(CharSouth$, CharPositionX!, CharPositionY!, CharSizeX!, CharSizeY!, 255, 255, 255) //Command

Equations() //Command

Done!=0

While(Done!==0)

{

If(CharDirection$="SOUTH")

{

SetImageTransparent(CharSouth$, CharPositionX!, CharPositionY!, CharSizeX!, CharSizeY!, CharR!, CharG!, CharB!)

}

If(CharDirection$="NORTH")

{

SetImageTransparent(CharNorth$, CharPositionX!, CharPositionY!, CharSizeX!, CharSizeY!, CharR!, CharG!, CharB!)

}

If(CharDirection$="WEST")

{

SetImageTransparent(CharWest$, CharPositionX!, CharPositionY!, CharSizeX!, CharSizeY!, CharR!, CharG!, CharB!)

}

If(CharDirection$="EAST")

{

SetImageTransparent(CharEast$, CharPositionX!, CharPositionY!, CharSizeX!, CharSizeY!, CharR!, CharG!, CharB!)

}

For (slots! = 1; Slots! <= EnemyAmount!; Slots!++)

{

SetImageTransparent(EnemyGraphic[slots!]$, EnemyPositionX[slots!]!, EnemyPositionY[slots!]!, EnemySizeX[slots!]!, EnemySizeY[slots!]!, EnemyR!, EnemyG!, EnemyB!)

}//For Loop End

Get(ButtonPress$)

If (ButtonPress$ == "UP"){Walk(1)}

If (ButtonPress$ == "DOWN"){Walk(2)}

If (ButtonPress$ == "RIGHT"){Walk(3)}

If (ButtonPress$ == "LEFT"){Walk(4)}

If (ButtonPress$ == "Z"){Attack()}

EnemySpeed! = EnemySpeed! + 1

If (EnemySpeedTime! == EnemySpeed!)

{

EnemySpeed! = 0

CheckAttackOrMovement()

}

}//While Loop End

Method Walk(num!)

{

//Clear old character from screen

//Check new direction and move the char

if (num! == 1){ShowCharGraphic(1)}//Num == 1 End

if (num! == 2){ShowCharGraphic(2)}//Num == 1 End

if (num! == 3){ShowCharGraphic(3)}//Num == 1 End

if (num! == 4){ShowCharGraphic(4)}//Num == 1 End

}//Method Walk End

Method CheckAttackOrMovement()

{

slot! = slot! + 1

If(slot! > EnemyAmount!){slot! = 1}

CharSouth!=CharPositionY[slot!]! + 32

CharNorth!=CharPositionY[slot!]! - 32

CharEast! =CharPositionX[slot!]! + 32

CharWest! =CharPositionX[slot!]! - 32

Movement!=0

If (EnemyPositionY[slot!]! == CharSouth!){EnemyDamage(slot!) Movement=1}

If (EnemyPositionY[slot!]! == CharNorth!){EnemyDamage(slot!) Movement=1}

If (EnemyPositionX[slot!]! ==  CharEast!){EnemyDamage(slot!) Movement=1}

If (EnemyPositionX[slot!]! ==  CharWest!){EnemyDamage(slot!) Movement=1}

If (Movement! == 0)

{

If (EnemyPositionY[slot!]! > CharPositionY!){Move!=1} //North

If (EnemyPositionY[slot!]! < CharPositionY!){Move!=2} //South

If (EnemyPositionX[slot!]! > CharPositionX!){Move!=3} //West

If (EnemyPositionX[slot!]! < CharPositionX!){Move!=4} //East

//Clear old enemy tile

SetImage(GrassTile$, EnemyPositionX[slot!]!, EnemyPositionY[slot!]!, 32, 32)

If (Move!==1){EnemyPositionY[slot!]!=EnemyPositionY[slot!]!-32} //North

If (Move!==2){EnemyPositionY[slot!]!=EnemyPositionY[slot!]!+32} //South

If (Move!==3){EnemyPositionX[slot!]!=EnemyPositionX[slot!]!-32} //West

If (Move!==4){EnemyPositionX[slot!]!=EnemyPositionX[slot!]!+32} //East

CheckSameCoordAsChar()

CheckSameCoordAsOtherEnemy()

SetImage("mole.PNG", EnemyPositionX[slot!]!, EnemyPositionY[slot!]!, 32, 32)

}//If Movement == 0 End

}//Method CheckAttackOrMovement End

Method ShowCharGraphic(number!)

{

SetImage(GrassTile$, CharPositionX!, CharPositionY!, 32, 32)

if (number! == 1)//North

{

CharPositionY!=CharPositionY! - 32

CheckCharOutOfRange(1)

CheckCharOnSameCoordAsEnemy()

SetImageTransparent(CharNorth$, CharPositionX!, CharPositionY!, CharSizeX!, CharSizeY!, CharR!, CharG!, CharB!)

CharDirection$="NORTH"

}

if (number! == 2)//South

{

CharPositionY!=CharPositionY! + 32

CheckCharOutOfRange(2)

CheckCharOnSameCoordAsEnemy()

SetImageTransparent(CharSouth$, CharPositionX!, CharPositionY!, CharSizeX!, CharSizeY!, CharR!, CharG!, CharB!)

CharDirection$="SOUTH"

}

if (number! == 3)//West

{

CharPositionX!=CharPositionX! - 32

CheckCharOutOfRange(3)

CheckCharOnSameCoordAsEnemy()

SetImageTransparent(CharWest$, CharPositionX!, CharPositionY!, CharSizeX!, CharSizeY!, CharR!, CharG!, CharB!)

CharDirection$="WEST"

}

if (number! == 4)//East

{

CharPositionX!=CharPositionX! + 32

CheckCharOutOfRange(4)

CheckCharOnSameCoordAsEnemy()

SetImageTransparent(CharEast$, CharPositionX!, CharPositionY!, CharSizeX!, CharSizeY!, CharR!, CharG!, CharB!)

CharDirection$="EAST"

}

}//Method ShowCharGraphic End

Method CheckCharOutOfRange(num!)

{

if (num! == 1)//North

{

if (CharPositionY! < YStart!)

{

CharPositionY!=CharPositionY!+32

SetImageTransparent(CharNorth$, CharPositionX!, CharPositionY!, CharSizeX!, CharSizeY!, CharR!, CharG!, CharB!)

}

}

if (num! == 2)//South

{

if (CharPositionY! > YEnd!)

{

CharPositionY!=CharPositionY!-32

SetImageTransparent(CharSouth$, CharPositionX!, CharPositionY!, CharSizeX!, CharSizeY!, CharR!, CharG!, CharB!)

}

}

if (num! == 3)//West

{

if (CharPositionX! < XStart!)

{

CharPositionX!=CharPositionX!+32

SetImageTransparent(CharWest$, CharPositionX!, CharPositionY!, CharSizeX!, CharSizeY!, CharR!, CharG!, CharB!)

}

}

if (num! == 4)//East

{

if (CharPositionX! > XEnd!)

{

CharPositionX!=CharPositionX!-32

SetImageTransparent(CharEast$, CharPositionX!, CharPositionY!, CharSizeX!, CharSizeY!, CharR!, CharG!, CharB!)

}

}

}//Method CheckCharOutOfRange End

Method ShowEnemies()

{

For (slots!=0; Slots! <= EnemyAmount!; Slots!++)

{

SetImageTransparent(EnemyGraphic[slots!]$, EnemyPositionX[slots!]!, EnemyPositionY[slots!]!, EnemySizeX[slots!]!, EnemySizeY[slots!]!, EnemyR!, EnemyG!, EnemyB!)

}//For Loop End

}

Method CheckSameCoordAsChar()

{

If (EnemyPositionX[slot!]!==CharPositionX!)//Checks if enemy is on same X coord as character

{

If (EnemyPositionY[slot!]!==CharPositionY!)//Checks if enemy is on same Y coord as character

{

//Checks what direction the enemy moved in so we can move the same way back

if (move!==1){EnemyPositionY[slot!]!=EnemyPositionY[slot!]!+32}

if (move!==2){EnemyPositionY[slot!]!=EnemyPositionY[slot!]!-32}

if (move!==3){EnemyPositionX[slot!]!=EnemyPositionX[slot!]!+32}

if (move!==4){EnemyPositionX[slot!]!=EnemyPositionX[slot!]!-32}

}//If Y End

}//If X End

}//Method CheckSameCoordAsChar End

Method CheckSameCoordAsOtherEnemy()

{

For (slots!=0; Slots! <= EnemyAmount!; Slots!++)

{

if(slot!=slots!)

{

}

Else

{

if (EnemyPositionX[slots!]! == EnemyPositionX[slot!]!)

{

if (EnemyPositionY[slots!]! == EnemyPositionY[slot!]!)

{

if (move!==1)

{

EnemyPositionY[slot!]!=EnemyPositionY[slot!]! + 32

}

if (move!==2)

{

EnemyPositionY[slot!]!=EnemyPositionY[slot!]! - 32

}

if (move!==3)

{

EnemyPositionX[slot!]!=EnemyPositionX[slot!]! + 32

}

if (move!==4)

{

EnemyPositionX[slot!]!=EnemyPositionX[slot!]! - 32

}

SetImage("mole.PNG", EnemyPositionX[slot!]!, EnemyPositionY[slot!]!, 32, 32)

}//If Y End

}//If X End

}//Else End

}//For Loop End

}//Method CheckSameCoordAsOtherEnemy End

Method CheckCharOnSameCoordAsEnemy()

{

For (slots!=0; slots! <= EnemyAmount!; slots!++)

{

if (EnemyPositionX[slots!]! == CharPositionX!)

{

if (EnemyPositionY[slots!]! == CharPositionY!)

{

if (number!==1)

{

CharPositionY!=CharPositionY!+32

SetImageTransparent(CharSouth$, CharPositionX!, CharPositionY!, CharSizeX!, CharSizeY!, CharR!, CharG!, CharB!)

}//Old North, walking to South

if (number!==2)

{

CharPositionY!=CharPositionY!-32

SetImageTransparent(CharNorth$, CharPositionX!, CharPositionY!, CharSizeX!, CharSizeY!, CharR!, CharG!, CharB!)

}//Old South, walking to North

if (number!==3)

{

CharPositionX!=CharPositionX!+32

SetImageTransparent(CharEast$, CharPositionX!, CharPositionY!, CharSizeX!, CharSizeY!, CharR!, CharG!, CharB!)

}//Old West, walking to East

if (number!==4)

{

CharPositionX!=CharPositionX!-32

SetImageTransparent(CharWest$, CharPositionX!, CharPositionY!, CharSizeX!, CharSizeY!, CharR!, CharG!, CharB!)

}//Old East, walking to West

}//If Y End

}//If X End

}//For Loop End

}//Method CheckCharOnSameCoordAsEnemy End

Method EnemyDamage(slot!)

{

}//Method EnemyDamage End

Method Equations()

{

//All Equations (should be left untouched)

   CharPositionX!=CharStartX! * 32

   CharPositionY!=CharStartY! * 32

   XStart!=XStart! * 32

   YStart!=YStart! * 32

   XEnd!=XEnd! * 32

   YEnd!=YEnd! * 32

   EnemyPositionX[1]!=EnemyStartX[1]! * 32

   EnemyPositionY[1]!=EnemyStartY[1]! * 32

   EnemyPositionX[2]!=EnemyStartX[2]! * 32

   EnemyPositionY[2]!=EnemyStartY[2]! * 32

   EnemyPositionX[3]!=EnemyStartX[3]! * 32

   EnemyPositionY[3]!=EnemyStartY[3]! * 32

   EnemyPositionX[4]!=EnemyStartX[4]! * 32

   EnemyPositionY[4]!=EnemyStartY[4]! * 32

      EmemyTurn!=0

}
```

### new game maker · 2005-09-05 12:49 · #B254220

looks good to me so far..

### Noob From The Grave · 2005-09-05 13:56 · #B254233

I didn't have an in-depth look however the enemydamage method at the end contains nothing? the method requires slot! but that isn't assigned within the method?

### William · 2005-09-05 14:35 · #B254241

**William wrote:**

> I kinda took a small break from it, but started working today again, not I have all the AI done, all thats left is the damage part, death method, gain stat method and character walking into enemy method.
>

I said I wasn't finished with the damage methods, you should read the posts Razz

### p90m16mp5a4 · 2005-09-05 18:08 · #B254318

Why don't you comment your code? You will forget what you were trying to do later on, get in a habbit of explaining why you are doing something.
Proper commenting is an incredible way to remember wtf you were doing later on, remember, say *why* you are doing something, not *what* you are doing.
Mwin("Hi, this is a message of your death") //Display message
Wait //Pauses game
EHHHH WRONGOOOO!!
mwin("hi, this is a message of your death") //Tell player he is going to die.
wait //Keep message window on screen
There is absolutely no reason to comment a Mwin, hardly ever, but it shows good form if you ask me.

### William · 2005-09-05 19:27 · #B254349

Yes i know, and I will do that when the battle is finished

### new game maker · 2005-09-05 19:33 · #B254357

whats the game gonna be called, that your making?

### Tao-Kun · 2005-09-05 19:58 · #B254374

**new game maker wrote:**

> whats the game gonna be called, that your making?
>

He is creating a ATB system for the community.

### new game maker · 2005-09-05 20:12 · #B254387

oh.. damet sorry

### ???? · 2005-09-05 20:41 · #B254414

Looks good to me

### p90m16mp5a4 · 2005-09-05 21:14 · #B254434

Ah, I can actually start to see some form of a battle system now that you have some comments Smile

### William · 2005-09-06 15:05 · #B254628

Thanks, I will add more comments after the battle is finished. =)

### p90m16mp5a4 · 2005-09-06 16:56 · #B254647

I can give youa tip on rt bs's, use the hotkeys. Dont use #While for action keys, it's very slow.
Your graphics system, while unique, seems to be inneficient, from what I saw, the Toolkit processing all of those custom walking positions, most likely wont hold up Smile But you deserve dibs for trying, but it is most likely ganna run slow when you finish Sad
To help it run a bit faster:
1. Use shorter method names
2. Reduce the amount of method calls
3. Reduce amount of variable calls.
So, instead of doing :
CharEnemy[x]! = charenemy[x]! * 32, do
CharEnemy[x]! *= 32, wich does the same thing.
Good job so far, I actually see a BS in there now, since I know its RT.
I see you have alot of logic you used to create this, so I can't really pick up on it to help out. But you seem to have a good grasp on it Smile

### new game maker · 2005-09-06 19:40 · #B254701

how do i make a bs or menu.. can you give me the programs please?

### William · 2005-09-07 13:34 · #B254927

This battle system will not run slow since I tested it, and I will add something like 32/5 pixel movement, so the character doesn't move 32 pixels on each step.. well you will see later. And long method names doesn't really slow it down. You cant even notice the time you are saying slowing my system down.

> [!missing] gap:16-30 · http://toolkitzone.com/forums/viewtopic.php?t=23223&start=15 · never-captured
> Page 2 of 2 was not recovered.
