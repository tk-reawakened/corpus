---
kind: forum-thread
id: "toolkitzone-forums/23015"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Advanced Coding"
skin: "phpbb2"
thread_id: "23015"
title: "Check last post for new BS Code"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=23015"
written: "2005-08-29T19:37:00"
last_post: "2005-09-08T03:01:00"
date_confidence: "exact"
captured: ["20051031004624"]
author: "William"
repliers: ["sephy", "????", "TKFanBoy", "p90m16mp5a4", "new game maker", "Caliber Mengsk", "Zio"]
authors: ["William", "sephy", "????", "TKFanBoy", "p90m16mp5a4", "new game maker", "Caliber Mengsk", "Zio"]
posts_present: 15
pages_present: [1]
pages_total: 2
posts_per_page: 15
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 2, start: 16, end: 30, url: "http://toolkitzone.com/forums/viewtopic.php?t=23015&start=15", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_252187_amp_3Bsid_7cde889a94523dc3911efb6795047320", captured: "20051031004624", sha256: "76d6de987cc3c324914f354b70f624d1a6b14d36544534c757573c0d575ae7fa", wayback_url: "https://web.archive.org/web/20051031004624/http://www.toolkitzone.com/forums/viewtopic.php?p=252187&amp%3Bsid=7cde889a94523dc3911efb6795047320"}
links: []
---

# Check last post for new BS Code

### William · 2005-08-29 19:37 · #B251835

Just give me some opinions on it, suggestions on faster coding etc:

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

EnemySpeedTime!=50

AmountOfEnemies!=3 //Max 4 Enemies!

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

//All Equations (should be left untouched)

   EnemyAmount! = AmountofEnemies! + 1

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

//Start Varibles and Commands

ViewBRD(BattleBoardMapName$)

ShowEnemies()

SetImageTransparent(CharSouth$, CharPositionX!, CharPositionY!, CharSizeX!, CharSizeY!, 255, 255, 255)

SetImageTransparent(EnemyGraphic[1]$, EnemyPositionX[1]!, EnemyPositionY[1]!, EnemySizeX[1]!, EnemySizeY[1]!, EnemyR!, EnemyG!, EnemyB!)

Done!=0

While(Done!==0)

{

ShowEnemies()

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

For slot!=1; Slot! < EnemyAmount!; Slot!++)

{

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

SetImage("mole.PNG", EnemyPositionX[slot!]!, EnemyPositionY[slot!]!, 32, 32)

}//If Movement == 0 End

}//For Loop End

}//Method CheckAttackOrMovement End

Method ShowCharGraphic(number!)

{

SetImage(GrassTile$, CharPositionX!, CharPositionY!, 32, 32)

if (number! == 1)//North

{

CharPositionY!=CharPositionY!-32

SetImageTransparent(CharNorth$, CharPositionX!, CharPositionY!, CharSizeX!, CharSizeY!, CharR!, CharG!, CharB!)

CheckCharOutOfRange(1)

}

if (number! == 2)//South

{

CharPositionY!=CharPositionY!+32

SetImageTransparent(CharSouth$, CharPositionX!, CharPositionY!, CharSizeX!, CharSizeY!, CharR!, CharG!, CharB!)

CheckCharOutOfRange(2)

}

if (number! == 3)//West

{

CharPositionX!=CharPositionX!-32

SetImageTransparent(CharWest$, CharPositionX!, CharPositionY!, CharSizeX!, CharSizeY!, CharR!, CharG!, CharB!)

CheckCharOutOfRange(3)

}

if (number! == 4)//East

{

CharPositionX!=CharPositionX!+32

SetImageTransparent(CharEast$, CharPositionX!, CharPositionY!, CharSizeX!, CharSizeY!, CharR!, CharG!, CharB!)

CheckCharOutOfRange(4)

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

For slots!=1; Slots! < slots!; Slots!=slots!+1)

{

SetImageTransparent(EnemyGraphic[slots!]$, EnemyPositionX[slots!]!, EnemyPositionY[slots!]!, EnemySizeX[slots!]!, EnemySizeY[slots!]!, EnemyR!, EnemyG!, EnemyB!)

}//For Loop End

}

Method EnemyDamage(slot!)

{

}//Method EnemyDamage End
```

Right now you can move around, and you cant walk outside the map. Made some equations for you guys so its easier to decide the map size. Any more varibles you want added?

### sephy · 2005-08-29 21:30 · #B251894

is this gonna be a plugin?

### ???? · 2005-08-29 21:46 · #B251916

How are going to use the program, do we just modify the program to own needs or is it gonna be a plug-in like sephy asked

### TKFanBoy · 2005-08-29 22:49 · #B251951

I suppose you are gonna have to do the first part every time a battle occurs?
Maybe you should put the equations in a method

### p90m16mp5a4 · 2005-08-30 05:18 · #B252081

Would't it be easier to wrap these up into classes and simple methods like #Swing? It seems very slow if you ask me.

### William · 2005-08-30 13:38 · #B252187

This is not a plugin, and I will show you how to use different enemies on different boards, since there is this varible on each board:
BattleBoard! or something, dont remember the varible?
This is coded in RPG Code. You cant code with cls in it.

### new game maker · 2005-09-06 19:44 · #B254705

is it done..?

### William · 2005-09-07 18:01 · #B254979

80%

### new game maker · 2005-09-07 18:59 · #B254998

oh ok, wasnt sure, not trying to rush you

### William · 2005-09-07 19:37 · #B255012

90% Done now =)

### new game maker · 2005-09-07 19:39 · #B255014

w00t Smile

### p90m16mp5a4 · 2005-09-07 23:34 · #B255137

Make a demo out of it, IE, a .exe. Unless you can run it straight from the editor. (Lol, im sure you have bitmaps and items)

### Caliber Mengsk · 2005-09-08 00:10 · #B255171

**p90m16mp5a4 wrote:**

> Make a demo out of it, IE, a .exe. Unless you can run it straight from the editor. (Lol, im sure you have bitmaps and items)
>

.exe's from the TK rarely work... like 99% of the files don't run... I belive it doesn't run threads or metheds.

### Zio · 2005-09-08 01:30 · #B255209

I released both my menu demo and smithy demo as exe only and methods and threads both work. Come to think of it I don't think I rereleased the menu demo with threaded programs but I have tested it as an exe.

### p90m16mp5a4 · 2005-09-08 03:01 · #B255232

I have never made a .exe whos threads dont work.

> [!missing] gap:16-30 · http://toolkitzone.com/forums/viewtopic.php?t=23015&start=15 · never-captured
> Page 2 of 2 was not recovered.
