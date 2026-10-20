---
kind: forum-thread
id: "toolkitzone-forums/11480"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "advanced"
skin: "phpbb2"
thread_id: "11480"
title: "I need Help With Code..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11480"
written: "2004-11-18T03:08:00"
last_post: "2004-11-30T04:45:00"
date_confidence: "exact"
captured: ["20050113181416"]
author: "forsaken"
repliers: ["casper323", "matt72186", "reignofmagic", "catwhowalksbyhimself", "Alex0Xander", "p90m16mp5a4"]
authors: ["forsaken", "casper323", "matt72186", "reignofmagic", "catwhowalksbyhimself", "Alex0Xander", "p90m16mp5a4"]
posts_present: 12
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_131962_amp_", captured: "20050113181416", sha256: "544122cb8938ad855a378b1c9b90dc82be6b6c8a3e725654e3c3f177e29236ed", wayback_url: "https://web.archive.org/web/20050113181416/http://www.toolkitzone.com/forums/viewtopic.php?p=131962&amp="}
links:
  - {url: "http://www.mysticsoftware.net/wiki/", status: "never-captured", local: null}
---

# I need Help With Code...

### forsaken · 2004-11-18 03:08 · #B126612

well i have my menu stuff and i know how to display text but how would i make it to display something only if you have that something.
for instance the main player always has his statistics showing but i dont want player 2 stats showing if hes not in party... how would i do that

### casper323 · 2004-11-18 03:35 · #B126630

that's what i need help with too Cool hehe

### forsaken · 2004-11-18 03:40 · #B126635

well hope we get a solution if anyone cares to give one

### matt72186 · 2004-11-18 03:42 · #B126636

So have you read the TK Reference?
Try checking out <http://www.mysticsoftware.net/wiki/>

### forsaken · 2004-11-18 04:05 · #B126648

ok i can add the player with the normal menu everything displays fine but with myne it dosent but if i try using the main character to show it does just fine.

### forsaken · 2004-11-18 04:10 · #B126650

this is what i have im only putting sections that matter not entire file.
start.prg

**rpgcode:**

```
*Damien Stats*

Include("stats.prg")

SetStatLit("Damien", "DamienSex", "Male")

SetStatLit("Damien", "DamienClass", "Mage")

SetStatElement("Damien", "Fire", "Fire")

DamienHP! = GetHP("Damien")

DamienM! = GetSMP("Damien")

DamienA! = GetDP("Damien")

DamienF! = GetFP("Damien")

DamienL! = GetLevel("Damien")

*Drako Stats*

SetStatLit("Drako", "DrakoSex", "Male")

SetStatLit("Drako", "DamienClass", "Theif")

SetStatElement("Damien", "Wind", "Wind")

DrakoHP! = GetHP("Drako")

DrakoM! = GetSMP("Drako")

DrakoA! = GetDP("Drako")

DrakoF! = GetFP("Drako")

DrakoL! = GetLevel("Drako")
```

menu.prg

**rpgcode:**

```
******************

*Custom Main Menu*

*Fosaken Realms***

****************

Main()

method main()

{

******Call All Included Programs******

     Include("savegame.prg")

******Call Image Filenames To Varaible******

     mbkg$ = "main.gif"

     mcur$ = "mcur.gif"

******Call Image x!,y!, Coordinates To Variable******

     mbkgx! = 0

     mbkgy! = 0

     mcurx[1]! = 443

     mcurx[2]! = 411

     mcurx[3]! = 390

     mcurx[4]! = 390

     mcurx[5]! = 398

     mcurx[6]! = 412

     mcurx[7]! = 426

     mcurx[8]! = 476

     mcury[1]! = 28

     mcury[2]! = 56

     mcury[3]! = 94

     mcury[4]! = 134

     mcury[5]! = 169

     mcury[6]! = 202

     mcury[7]! = 234

     mcury[8]! = 267

******Call Image Widths &amp; Heights To Variable******

     mbkgw! = 640

     mbkgh! = 480

     mcurw! = 25

     mcurh! = 21

******Call Image Effects To Variable******

     mr! = 255

     mg! = 255

     mb! = 255

******Call Main Function Of Program******

     mselx! = 1

     msely! = 1

     Done! = 1

     SetImage(mbkg$, mbkgx!, mbkgy!, mbkgw!, mbkgh!)

**********Call Stats Damien********

     Include("stats.Prg")

     DamienSex$ = GetStatLit("Damien", "DamienSex")

     DamienClass$ = GetStatLit("Damien", "DamienClass")

     Fire$ = GetStatElement("Damien", "Fire")

*********Call Stats Drako***********

     DrakoSex$ = GetStatLit("Drako", "DrakoSex")

     DrakoClass$ = GetStatLit("Drako, "DrakoClass")

     Wind$ = GetStatElement("Drako", "Wind")

***********************************

*********Display Damien Stats*************

     Text(10, 3.2, DamienSex$)

     Text(9.7, 4.3, DamienL!)

     Text(9, 5.5, DamienHP!)

     Text(9, 6.5, DamienM!)

     Text(18, 3.1, DamienA!)

*********Display Player 2 Stats***********

     If(Drako! == 1)

     {

          Text(10, 10, DrakoSex$)

          Text(9.7, 11.1, DrakoL!)

          Text(9, 12.3, DrakoHP!)

          Text(9, 13.3, DrakoM!)

          Text(18, 9.9, DrakoA!)

     }

************************************

     SaveScreen()

     While(Done! == 1)

     {

          RestoreScreen()

          setimagetransparent(mcur$, mcurx[mselx!]!, mcury[msely!]!, mcurw!, mcurh!, mr!, mg!, mb!)

          wait(a$)

          if(a$ == "UP")

          {

               if(msely! &gt; 1)

               {

                    if(mselx! &gt; 1)

                    {

                         msely! = msely! - 1

                         mselx! = mselx! - 1

                    }

               }

          }

          if(a$ == "DOWN")

          {

               if(msely! &lt; Cool

               {

                    if(mselx! &lt; Cool

                    {

                         msely! = msely! + 1

                         mselx! = mselx! + 1

                    }

               }

          }

          if(a$ == "ENTER")

          {

               if(msely! == 1)

               {

                    if(mselx! == 1)

                    {

*item method*

                    }

               }

               if(msely! == 2)

               {

                    if(mselx! == 2)

                    {

*equip method*

                    }

               }

               if(msely! == 3)

               {

                    if(mselx! == 3)

                    {

*special method*

                    }

               }

               if(msely! == 4)

               {

                    if(mselx! == 4)

                    {

*status method*

                    }

               }

               if(msely! == 5)

               {

                    if(mselx! == 5)

                    {

*load method*

                         dirsav(dest$)

                         if(dest$ == "CANCEL")

                         {

                              load(dest$)

                              done! = 4

                         }

                    }

               }

               if(msely! == 6)

               {

                    if(mselx! == 6)

                    {

*save method*

                         savegame()

                    }

               }

               if(msely! == 7)

               {

                    if(mselx! == 7)

                    {

*return method*

                         Done! = 2

                         Done()

                    }

               }

               if(msely! == 8)

               {

                    if(mselx! == 8)

                    {

*exit method*

                         Dos()

                    }

               }

          }

     }

}
```

Drako.prg

**rpgcode:**

```
AddPlayer("drako.tem")

If(Drako! == 0)

{

     Include("system.prg")

     mtop("Drako:", "Drako.gif")

     m1("Watch who goes there...")

     m2("Oh its only you Damien whats wrong?")

     mtop("Damien:", "Damien.gif")

     m1("Oh nothing my mom just got kidnapped by 3 monsters")

     m2("I could use your help..")

     mtop("Drako:", "Drako.gif")

     m1("You got it i still owe you for saving my life..")

     Drako! = 1

}
```

### forsaken · 2004-11-18 04:16 · #B126654

it works if i add the player in the start prg but not if its in any other program

### forsaken · 2004-11-18 04:31 · #B126657

i found 2 solutions....
this is the original code for the menu.

**rpgcode:**

```
******************

*Custom Main Menu*

*Fosaken Realms***

****************

Main()

method main()

{

******Call All Included Programs******

     Include("savegame.prg")

     Include("stats.Prg")

******Call Image Filenames To Varaible******

     mbkg$ = "main.gif"

     mcur$ = "mcur.gif"

******Call Image x!,y!, Coordinates To Variable******

     mbkgx! = 0

     mbkgy! = 0

     mcurx[1]! = 443

     mcurx[2]! = 411

     mcurx[3]! = 390

     mcurx[4]! = 390

     mcurx[5]! = 398

     mcurx[6]! = 412

     mcurx[7]! = 426

     mcurx[8]! = 476

     mcury[1]! = 28

     mcury[2]! = 56

     mcury[3]! = 94

     mcury[4]! = 134

     mcury[5]! = 169

     mcury[6]! = 202

     mcury[7]! = 234

     mcury[8]! = 267

******Call Image Widths &amp; Heights To Variable******

     mbkgw! = 640

     mbkgh! = 480

     mcurw! = 25

     mcurh! = 21

******Call Image Effects To Variable******

     mr! = 255

     mg! = 255

     mb! = 255

******Call Main Function Of Program******

     mselx! = 1

     msely! = 1

     Done! = 1

     SetImage(mbkg$, mbkgx!, mbkgy!, mbkgw!, mbkgh!)

**********Call Stats Damien********

     DamienSex$ = GetStatLit("Damien", "DamienSex")

     DamienClass$ = GetStatLit("Damien", "DamienClass")

     Fire$ = GetStatElement("Damien", "Fire")

*********Call Stats Drako***********

     DrakoSex$ = GetStatLit("Drako", "DrakoSex")

     DrakoClass$ = GetStatLit("Drako, "DrakoClass")

     Wind$ = GetStatElement("Drako", "Wind")

***********************************

*********Display Damien Stats*************

     Text(10, 3.2, DamienSex$)

     Text(9.7, 4.3, DamienL!)

     Text(9, 5.5, DamienHP!)

     Text(9, 6.5, DamienM!)

     Text(18, 3.1, DamienA!)

*********Display Drako Stats***********

     If(Drako! == 1)

     {

          Text(10, 10, DrakoSex$)

          Text(9.7, 11.1, DrakoL!)

          Text(9, 12.3, DrakoHP!)

          Text(9, 13.3, DrakoM!)

          Text(18, 9.9, DrakoA!)

     }

************************************

     SaveScreen()

     While(Done! == 1)

     {

          RestoreScreen()

          setimagetransparent(mcur$, mcurx[mselx!]!, mcury[msely!]!, mcurw!, mcurh!, mr!, mg!, mb!)

          wait(a$)

          if(a$ == "UP")

          {

               if(msely! &gt; 1)

               {

                    if(mselx! &gt; 1)

                    {

                         msely! = msely! - 1

                         mselx! = mselx! - 1

                    }

               }

          }

          if(a$ == "DOWN")

          {

               if(msely! &lt; Cool

               {

                    if(mselx! &lt; Cool

                    {

                         msely! = msely! + 1

                         mselx! = mselx! + 1

                    }

               }

          }

          if(a$ == "ENTER")

          {

               if(msely! == 1)

               {

                    if(mselx! == 1)

                    {

*item method*

                    }

               }

               if(msely! == 2)

               {

                    if(mselx! == 2)

                    {

*equip method*

                    }

               }

               if(msely! == 3)

               {

                    if(mselx! == 3)

                    {

*special method*

                    }

               }

               if(msely! == 4)

               {

                    if(mselx! == 4)

                    {

*status method*

                    }

               }

               if(msely! == 5)

               {

                    if(mselx! == 5)

                    {

*load method*

                         dirsav(dest$)

                         if(dest$ == "CANCEL")

                         {

                              load(dest$)

                              done! = 4

                         }

                    }

               }

               if(msely! == 6)

               {

                    if(mselx! == 6)

                    {

*save method*

                         Savegame()

                    }

               }

               if(msely! == 7)

               {

                    if(mselx! == 7)

                    {

*return method*

                         Done! = 2

                         Done()

                    }

               }

               if(msely! == 8)

               {

                    if(mselx! == 8)

                    {

*exit method*

                         Dos()

                    }

               }

          }

     }

}
```

i added the following code to where drakos stats are

**rpgcode:**

```
SetStatLit("Drako", "DrakoSex", "Male")

SetStatLit("Drako", "DamienClass", "Theif")

SetStatElement("Damien", "Wind", "Wind")

DrakoHP! = GetHP("Drako")

DrakoM! = GetSMP("Drako")

DrakoA! = GetDP("Drako")

DrakoF! = GetFP("Drako")

DrakoL! = GetLevel("Drako")
```

so this is what it looks with it added

**rpgcode:**

```
******************

*Custom Main Menu*

*Fosaken Realms***

****************

Main()

method main()

{

******Call All Included Programs******

     Include("savegame.prg")

     Include("stats.Prg")

******Call Image Filenames To Varaible******

     mbkg$ = "main.gif"

     mcur$ = "mcur.gif"

******Call Image x!,y!, Coordinates To Variable******

     mbkgx! = 0

     mbkgy! = 0

     mcurx[1]! = 443

     mcurx[2]! = 411

     mcurx[3]! = 390

     mcurx[4]! = 390

     mcurx[5]! = 398

     mcurx[6]! = 412

     mcurx[7]! = 426

     mcurx[8]! = 476

     mcury[1]! = 28

     mcury[2]! = 56

     mcury[3]! = 94

     mcury[4]! = 134

     mcury[5]! = 169

     mcury[6]! = 202

     mcury[7]! = 234

     mcury[8]! = 267

******Call Image Widths &amp; Heights To Variable******

     mbkgw! = 640

     mbkgh! = 480

     mcurw! = 25

     mcurh! = 21

******Call Image Effects To Variable******

     mr! = 255

     mg! = 255

     mb! = 255

******Call Main Function Of Program******

     mselx! = 1

     msely! = 1

     Done! = 1

     SetImage(mbkg$, mbkgx!, mbkgy!, mbkgw!, mbkgh!)

**********Call Stats Damien********

     DamienSex$ = GetStatLit("Damien", "DamienSex")

     DamienClass$ = GetStatLit("Damien", "DamienClass")

     Fire$ = GetStatElement("Damien", "Fire")

*********Call Stats Drako***********

     DrakoSex$ = GetStatLit("Drako", "DrakoSex")

     DrakoClass$ = GetStatLit("Drako, "DrakoClass")

     Wind$ = GetStatElement("Drako", "Wind")

***********************************

*********Display Damien Stats*************

     Text(10, 3.2, DamienSex$)

     Text(9.7, 4.3, DamienL!)

     Text(9, 5.5, DamienHP!)

     Text(9, 6.5, DamienM!)

     Text(18, 3.1, DamienA!)

*********Display Drako Stats***********

     If(Drako! == 1)

     {

          SetStatLit("Drako", "DrakoSex", "Male")

          SetStatLit("Drako", "DamienClass", "Theif")

          SetStatElement("Damien", "Wind", "Wind")

          DrakoHP! = GetHP("Drako")

          DrakoM! = GetSMP("Drako")

          DrakoA! = GetDP("Drako")

          DrakoF! = GetFP("Drako")

          DrakoL! = GetLevel("Drako")

          Text(10, 10, DrakoSex$)

          Text(9.7, 11.1, DrakoL!)

          Text(9, 12.3, DrakoHP!)

          Text(9, 13.3, DrakoM!)

          Text(18, 9.9, DrakoA!)

     }

************************************

     SaveScreen()

     While(Done! == 1)

     {

          RestoreScreen()

          setimagetransparent(mcur$, mcurx[mselx!]!, mcury[msely!]!, mcurw!, mcurh!, mr!, mg!, mb!)

          wait(a$)

          if(a$ == "UP")

          {

               if(msely! &gt; 1)

               {

                    if(mselx! &gt; 1)

                    {

                         msely! = msely! - 1

                         mselx! = mselx! - 1

                    }

               }

          }

          if(a$ == "DOWN")

          {

               if(msely! &lt; Cool

               {

                    if(mselx! &lt; Cool

                    {

                         msely! = msely! + 1

                         mselx! = mselx! + 1

                    }

               }

          }

          if(a$ == "ENTER")

          {

               if(msely! == 1)

               {

                    if(mselx! == 1)

                    {

*item method*

                    }

               }

               if(msely! == 2)

               {

                    if(mselx! == 2)

                    {

*equip method*

                    }

               }

               if(msely! == 3)

               {

                    if(mselx! == 3)

                    {

*special method*

                    }

               }

               if(msely! == 4)

               {

                    if(mselx! == 4)

                    {

*status method*

                    }

               }

               if(msely! == 5)

               {

                    if(mselx! == 5)

                    {

*load method*

                         dirsav(dest$)

                         if(dest$ == "CANCEL")

                         {

                              load(dest$)

                              done! = 4

                         }

                    }

               }

               if(msely! == 6)

               {

                    if(mselx! == 6)

                    {

*save method*

                         Savegame()

                    }

               }

               if(msely! == 7)

               {

                    if(mselx! == 7)

                    {

*return method*

                         Done! = 2

                         Done()

                    }

               }

               if(msely! == 8)

               {

                    if(mselx! == 8)

                    {

*exit method*

                         Dos()

                    }

               }

          }

     }

}
```

but i dont want to have that extra part there i just want it to be in start menu but it dosent work in start menu unless i have added the character there.

### reignofmagic · 2004-11-18 04:49 · #B126659

**matt72186 wrote:**

> So have you read the TK Reference?
> Try checking out <http://www.mysticsoftware.net/wiki/>
>

Wow! Never been to that site before matt72186.
[quote="forsaken]blah blah blah[quote]
Your code is too long. It make my eye sore.

### catwhowalksbyhimself · 2004-11-18 21:28 · #B126855

A more efficient way of accomplishing this is to set the characters' names in arrays.
Instead of DrakoHP! use HP[Drako]!
Then set the characters' names as variables. Character[1]$ = "Drako" and so forth. Then in the menu where you select the character, use a number value for the selected character that matches the array where the character name is stored. Lets say you sue menu! as the selected variable. As you move the cursor, add or sutract from the number and use it to display the cursor. Then when you want to, for instance, shows HP, all you have to do is.

**Code:**

```
Name$ = character[menu!]$

pixeltext(1,1,castlit(HP[name$]!)
```

That way, you can even switch around the characters and their positions on the team and on the screen and it still works.

### Alex0Xander · 2004-11-19 19:45 · #B127240

[quote="reignofmagic"]

**matt72186 wrote:**

> So have you read the TK Reference?
> Try checking out <http://www.mysticsoftware.net/wiki/>
>

Wow! Never been to that site before matt72186.
[quote="forsaken]blah blah blah

**Quote:**

> Your code is too long. It make my eye sore.
>

Try making your own battle/menu system, then comment.

### p90m16mp5a4 · 2004-11-30 04:45 · #B131962

that is one kick a$$ menu system, its really nice. especially the character selection part. thumbs up man.
Couldn't you just check at the start of the method to see whos playing in the game before drawing the stats on screen? Thats seems like the logical thing to do =\P
