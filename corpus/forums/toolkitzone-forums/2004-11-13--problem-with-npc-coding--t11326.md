---
kind: forum-thread
id: "toolkitzone-forums/11326"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "advanced"
skin: "phpbb2"
thread_id: "11326"
title: "Problem With NPC Coding"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11326"
written: "2004-11-13T21:03:00"
last_post: "2004-11-15T02:15:00"
date_confidence: "exact"
captured: ["20050110143125"]
author: "jatenate"
repliers: ["Alex0Xander", "Asimir", "spitfire"]
authors: ["jatenate", "Alex0Xander", "Asimir", "spitfire"]
posts_present: 7
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_125422_amp_", captured: "20050110143125", sha256: "551398b04c25a7e91bcda2d747591d7b4bf3c062e8267b4cb2c98778876a06b6", wayback_url: "https://web.archive.org/web/20050110143125/http://www.toolkitzone.com/forums/viewtopic.php?p=125422&amp="}
links: []
---

# Problem With NPC Coding

### jatenate · 2004-11-13 21:03 · #B124835

I have been working on some code recently for my latest game (Shadow). I got it finished up with some help from Alex0Xander, but now there are some problems. I would appreciate it if noone else would copy this code to use in their game, but if you chose to, so be it.
The Idea
Okay, in a nut shell, the code is intended to make an NPC on a board "chase" the player if he/she comes within 3 both ways. The NPC represents the enemy, and when it comes in contact with the player, it engages in battle. The difficult part is, I have assigned a certain number to every enemy. This way, by having an NPC named 640321, It will split the name into 64, 03, and 21. Then battle will start using enemies 64.ene, 03.ene, and 21.ene.
The problem
Whenever I run the program, (the NPC running it as its Multi-task program) with all enemies needed existing and such, the game locks-up and doesnt display the NPC or anything but the player and board. I can't find any problems in it and the debugger doesnt do anything either.
The Code

**Code:**

```
AutoLocal()

handle$ = TargetHandle()  *This puts the NPC as handle$

Done!=1

While(Done! == 1) *This while loop has to be here, or it does this

*once the skips to starting battle

{

   GetPlayerCoords(0,px!,py!)

   GetItemLocation(handle$,ex!,ey!)

   If(px!-ex! <=3 && px!-ex! >=-3)

   {

      If(py!-ey! <=3 && py!-ey!>=-3)

      {

         Done! = 0 *Ends this loop and starts the next

      }

   }

}

While(Done! == 0)

{

   GetPlayerCoords(0,px!,py!)

   GetItemLocation(handle$,ex!,ey!)

   dest! = PathFind(ex!,ey!,px!,py!)

   PushItem(num!,dest!) *NPC moves towards, "chases", the player

   If(px!-ex!<=1 && px!-ex!>=-1) *Compares the coords

   {

      If(py!-ey!<=1 && py!-ey!>=-1) *Compares the coords

      {

         Done! = 1 *The NPC keeps doing this until battle

      }

   }

}

Initiate battle()

Method Initiate battle()

{

   targName$ = GetItemName(handle$)

   targName! = CastNum(targName$)

   *Gets the item (NPC's) name and makes it to a number so that

   *it can be used to determine the needed enemies

   enemy1! = CastInt(targName!/10000)

   enemy2! = CastInt((targName! - (enemy1!*10000))/100)

   enemy3! = targName!- (enemy1!*10000) - (enemy2!*100)

   *Determines the names of the enemies to be fought with

   enemy1$ = CastLit(enemy1!)

   enemy2$ = CastLit(enemy2!)

   enemy3$ = CastLit(enemy3!)

   *Turns all of the numerical enemy values into literal values

   *so that they can be used for determing enemie names

   {

      MWin("You prepare to engage in battle!")

      system.Pause()

      EraseItem(handle$)

      DestroyItem(handle$)

      Done! = 1

      FadeNum!=Random(5) *Randomly picks a fade to occur

      ColorRGB(255,255,255)

      Fade((FadeNum!-1)) *Executes the fade

      ColorRGB(255,255,255)

      FightEnemy(enemy1$+".ene", enemy2$+".ene", enemy3$+".ene", background$+".bkg")

      *Background is determined by a set variable that a previous warp tile sets

   }

}
```

Thanks for the help, and PLEASE dont copy it (not that anyone would want to..... Smile ) I'm really sorry about posting so much code, but I couldn't isolate it to a smaller area containing the problem.
-jatenate-

### Alex0Xander · 2004-11-13 21:32 · #B124855

**Code:**

```
AutoLocal()

handle$ = TargetHandle()  *This puts the NPC as handle$

Done!=1

While(Done! == 1) *This while loop has to be here, or it does this

*once the skips to starting battle

{

   GetPlayerCoords(0,px!,py!)

   GetItemLocation(handle$,ex!,ey!)

   If(px!-ex! <=3 && px!-ex! >=-3)

   {

      If(py!-ey! <=3 && py!-ey!>=-3)

      {

         Done! = 0 *Ends this loop and starts the next

      }

   }

}

While(Done! == 0)

{

   GetPlayerCoords(0,px!,py!)

   GetItemLocation(handle$,ex!,ey!)

   dest! = PathFind(ex!,ey!,px!,py!)

   PushItem(num!,dest!) *NPC moves towards, "chases", the player

   If(px!-ex!<=1 && px!-ex!>=-1) *Compares the coords

   {

      If(py!-ey!<=1 && py!-ey!>=-1) *Compares the coords

      {

         Done! = 1 *The NPC keeps doing this until battle

      }

   }

}

Initiate battle()

Method Initiate battle()

{

   targName$ = GetItemName(handle$)

   targName! = CastNum(targName$)

   *Gets the item (NPC's) name and makes it to a number so that

   *it can be used to determine the needed enemies

   enemy1! = CastInt(targName!/10000)

   enemy2! = CastInt((targName! - (enemy1!*10000))/100)

   enemy3! = targName!- (enemy1!*10000) - (enemy2!*100)

   *Determines the names of the enemies to be fought with

   enemy1$ = CastLit(enemy1!)

   enemy2$ = CastLit(enemy2!)

   enemy3$ = CastLit(enemy3!)

   *Turns all of the numerical enemy values into literal values

   *so that they can be used for determing enemie names

   {

      MWin("You prepare to engage in battle!")

      system.Pause()

      EraseItem(handle$)

      DestroyItem(handle$)

      Done! = 1

      FadeNum!=Random(5) *Randomly picks a fade to occur

      ColorRGB(255,255,255)

      Fade((FadeNum!-1)) *Executes the fade

      ColorRGB(255,255,255)

      FightEnemy(enemy1$+".ene", enemy2$+".ene", enemy3$+".ene", background$+".bkg")

      *Background is determined by a set variable that a previous warp tile sets

   }

}
```

Thanks for the help, and PLEASE dont copy it (not that anyone would want to..... Smile ) I'm really sorry about posting so much code, but I couldn't isolate it to a smaller area containing the problem.
-jatenate-[/quote]
I still cant see why the NPC does not show up just yet. But some things I found:

**Code:**

```
While(Done! == 1) *This while loop has to be here, or it does this
```

did that in all your while loops.
the double equal sign should only be used when making a variable equal something. I think this is insignificant, but just try one "=".

**Code:**

```
   dest! = PathFind(ex!,ey!,px!,py!)

   PushItem(num!,dest!) *NPC moves towards, "chases", the player*
```

num! has to be an acutal number or you can make num! equal the number of the item that represents the NPC on the board, for this you have to click RPGcode in the board edito (for that board) and your items list.
One thing I was thinking. How would you do to get the actual names of the mosnters? It seems they will be names 62, 11, 20, and so on..
Right now it seems like your problem is not in your code, I dont see anything that would make your NPC dissapear. I'll look into it some more.

### Asimir · 2004-11-13 21:40 · #B124856

**Quote:**

> the double equal sign should only be used when making a variable equal something. I think this is insignificant, but just try one "=".
>

No no no no no.
Double = is for comparison. Single = is for assignment. He used them correctly.
Try replacing all the *s for comments with //. Rpgcode has a bit of trouble with * comments on the same line as code.

### Alex0Xander · 2004-11-13 21:53 · #B124863

**Asimir wrote:**

>
> **Quote:**
>
> > the double equal sign should only be used when making a variable equal something. I think this is insignificant, but just try one "=".
> >
>
> No no no no no.
> Double = is for comparison. Single = is for assignment. He used them correctly.
> Try replacing all the *s for comments with //. Rpgcode has a bit of trouble with * comments on the same line as code.
>

really? Evil or Very Mad someone misguided me.

### jatenate · 2004-11-13 23:29 · #B124899

I used double ='s cause I am too used to C++ Smile. I noticed that the *'s werent coming out right because it would turn the stuff after the 2nd one to green, a comment. I assumed it was just a mistake. Thanks for the help! I'll retry it and see if it works, but I don't think that will be enough to make it work. I gotta go to church tho, so it'll have to wait till tommorrow! Thanks again!
-jatenate-
PS: Oh yeah, alex0Xander, I added you to my sig now Smile! I owe you!

### spitfire · 2004-11-14 19:15 · #B125202

**Asimir wrote:**

> Try replacing all the *s for comments with //. Rpgcode has a bit of trouble with * comments on the same line as code.
>

Hmm... I missed that.. cool! I didn't know I could do that...heh

### Alex0Xander · 2004-11-15 02:15 · #B125422

**jatenate wrote:**

> I used double ='s cause I am too used to C++ Smile. I noticed that the *'s werent coming out right because it would turn the stuff after the 2nd one to green, a comment. I assumed it was just a mistake. Thanks for the help! I'll retry it and see if it works, but I don't think that will be enough to make it work. I gotta go to church tho, so it'll have to wait till tommorrow! Thanks again!
> -jatenate-
> PS: Oh yeah, alex0Xander, I added you to my sig now Smile! I owe you!
>

I just like helping ^.^
and besides you got me into the mood to start work on my game again. YOu don't owe me anything.
