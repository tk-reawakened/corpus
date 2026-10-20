---
kind: forum-thread
id: "toolkitzone-forum/35295"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "35295"
title: "threads and some planning for a cbs *edited* posted AI code"
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=35295"
written: "2007-02-20T01:20:00"
last_post: "2007-02-22T01:31:00"
date_confidence: "exact"
captured: ["20070302171026"]
author: "rpg gamer 17"
repliers: ["yaim0310", "xenxe", "Shadow Eden"]
authors: ["rpg gamer 17", "yaim0310", "xenxe", "Shadow Eden"]
posts_present: 7
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_381835", captured: "20070302171026", sha256: "344b7f41a6100089525ef4c612a2bd035818266840106b9d6321394e719d0420", wayback_url: "https://web.archive.org/web/20070302171026/http://www.toolkitzone.com/forum/viewtopic.php?p=381835"}
links: []
---

# threads and some planning for a cbs *edited* posted AI code

### rpg gamer 17 · 2007-02-20 01:20 · #K381338

i want to make a cbs thats active and on board.
i know threads will run when another prg is moving.
what i dont know is if its possible to thread the same program twice. is it?
how badly will threads slow the game down?
i am making a cbs.
i just need to figure out how many threads im going to have to make and what there for.
heres what i have so far planning wise:
1- place the hp/mhp, mp/mmp and turn charge bar on the screen. check if a arrow key is pressed then check if the skill your using can be used while moving. BUSY! is set to zero if you can use the skill while moving.
2- get the enemy locations and figure out how close they are. when turn bar is charged, list the options of what you can do on the screen. check if the target is close then use the skill. - i need help on this
the enemys are items and are set when you enter a battle board.
heres what i have so far code wise:

**Code:**

```
rendernow("on")

Info! = createcanvas(250, 130)

setimageTranslucent("mwin.jpg", 0, 0, 250, 130, Info!)

getres(SWidth!, SHeight!)

while(0 == 0)

{

   clear(Info!)

   if(ChargeTime! > 100)

   {

      ChargeTime! = 100

   }

   setimageTranslucent("mwin.jpg", 0, 0, 250, 130, Info!)

   font("arial")

   PlayerLvl! = getLevel(playerhandle[0]$)

   PlayerHP! = GetHP(playerhandle[0]$)

   PlayerMHP! = GetMaxHP(playerhandle[0]$)

   PlayerSMP! = GetSMP(playerhandle[0]$)

   PlayerMSMP! = GetMaxSMP(playerhandle[0]$)

   GOLD! = getGP()

   bold("on")

   fontsize(20)

   pixeltext(90, 0, playerhandle[0]$, Info!)

   bold("off")

   fontsize(18)

   Size! = getfontsize()

   pixeltext(10, Size! + 2, "Lvl: " + castlit(PlayerLvl!), Info!)

   pixeltext(10, Size!*2 + 2, "Health: " + castlit(PlayerHP!) + "/" + castlit(PlayerMHP!), Info!)

   pixeltext(10, Size!*3 + 2, "Magic: " + castlit(PlayerSMP!) + "/" + castlit(PlayerMSMP!), Info!)

   pixeltext(10, Size!*4 + 2, "Charge: " + castlit(ChargeTime!), Info!)

   colorrgb(255, 0, 0)

   fillrect(130, Size!*2 + 5, 230, Size!*2 + 15, Info!)

   colorrgb(255,255,255)

   DrawtoHP! = PlayerHP!/PlayerMHP!

   colorrgb(120, 0, 0)

   fillrect(130, Size!*2 + 5, DrawtoHP! * 100 + 130, Size!*2 + 15, Info!)

   colorrgb(255,255,255)

   colorrgb(0, 0, 255)

   fillrect(130, Size!*3 + 5, 230, Size!*3 + 15, Info!)

   colorrgb(255,255,255)

   DrawtoSMP! = PlayerSMP!/PlayerMSMP!

   colorrgb(0, 0, 120)

   fillrect(130, Size!*2 + 5, DrawtoSMP! * 100 + 130, Size!*2 + 15, Info!)

   colorrgb(255,255,255)

   colorrgb(0, 255, 255)

   fillrect(130, Size!*4 + 5, 230, Size!*4 + 15, Info!)

   colorrgb(255,255,255)

   colorrgb(0, 115, 130)

   fillrect(130, Size!*4 + 5, ChargeTime! + 130, Size!*4 + 15, Info!)

   colorrgb(255,255,255)

   pixeltext(10, Size!*5 + 2, "Gold: " + castlit(GOLD!), Info!)

   drawcanvasTransparent(Info!, SWidth! - 250, SHeight! - 130, 255, 255, 255, 250, 130, cnvRenderNow!)

   if(ChargeTime! < 100 && StopCharge! ~= 1)

   {

      ChargeTime! = ChargeTime! + Random(PlayerLvl!) + 1

   }

   KEY$ = get()

   if(KEY$ == "LEFT" | KEY$ == "RIGHT" | KEY$ == "UP" | KEY$ == "DOWN")

   {

      if(BUSY! == 1)

      {

      }

      elseif(BUSY! ~= 1)

      {

         if(KEY$ == "LEFT")

         {

            push("W", playerhandle[0]$)

         }

         if(KEY$ == "RIGHT")

         {

            push("E", playerhandle[0]$)

         }

         if(KEY$ == "UP")

         {

            push("N", playerhandle[0]$)

         }

         if(KEY$ == "DOWN")

         {

            push("S", playerhandle[0]$)

         }

      }

   }

}
```

i know there is some places that could be shortened but it works thats all i care about.
how would i get the enemys location and figure out how close they are?
what i dont know is if its possible to thread the same program twice. is it?
how badly will threads slow the game down?

### yaim0310 · 2007-02-20 06:42 · #K381390

the function reference in the user's guide i think is the best page in the guide! it lists every function in alphabetical and again by category. there is even a category called items which as all the functions for items, maybe you'll find the function to get an items location, since your enemies are items.
as for figuring out how close they are, do it with some geometry.
here is a method to find the distance between two points:

**Code:**

```
dist! = distance(playerX!,playerY!,enemyX!,enemyY!)

method distance(x1!, y1!, x2!, y2!)

{

   squaredx! = (x1!-x2!)^2

   squaredy! = (y1!-y2!)^2

   returnmethod( sqrt(squaredx! + squaredy!) )

}
```

yes you can thread the same program twice, you would just use a different handle for them:

**Code:**

```
hThread1! = thread("thread.prg", 0)

hThread2! = thread("thread.prg", 0)
```

but i have absolutely no clue as to why you would want to thread the same program twice.
the speed impact from a thread depends on what the thread does... if you know that using setimage() slows your game, then using it in a thread will slow your game.

### xenxe · 2007-02-20 10:43 · #K381422

wow big math words everywhere i need to pay attention in class more

### Shadow Eden · 2007-02-20 14:31 · #K381446

hmm... i dont know why you'd want to thread something twice... it would just do the same thing...? but the main code u had looks good, i ran it and played around with a few things... i think future editions of TK should have default BS like this as well as the standard one...

### rpg gamer 17 · 2007-02-20 22:01 · #K381554

yeah... i have just been wondering if it was possible to thread a program twice... no reason... well i might of had something in mind when i asked it but idk now...
okay my plans for the battle system are to make 3 threads:
1 to find the player and enemys location and the players target...
2 to set the players stats (health, magic, charge time, gold, ect)
3 to set the players options (attack, defend, black magic, white magic, swordsmanship, ect...)
the AI of the monsters is going to be the hard part... im going to have to make a thread that controls the item(s)... maybe that was the double thread... Confused well i must code...
thxs
*EDIT*
I might have made the basic AI code... might... please check it...
its probally wrong... help Crying or Very sad Very Happy

**Code:**

```
Method distance(x1!, y1!, x2!, y2!)

{

   squaredx! = (x1!-x2!)^2

   squaredy! = (y1!-y2!)^2

   returnmethod( sqrt(squaredx! + squaredy!) )

}

Method Monsterstats(Num!, LowRanNuM!, HEAlTH!, Smp!, Item!, Magic!)

{

   PLvL! = getlvl(playerhandle[0]$)

   Monstername[Num!]$ = getitemname("Monster" + Num! + ".itm")

   MonsterLvL[Num!]! = random(LowRanNuM!) + PLvL! - random(LowRanNuM!)

   MonsterMaxHP[Num!]! = castint(random(HEAlTH!/random(LvL[Num!]!)) + HEAlTH!)

   MonsterHP[Num!]! = MonsterMaxHP[Num!]!

   MonsterMaxSMP[Num!]! = random(Smp*random(LvL[Num!]!)) + Smp!

   MonsterSMP[Num!]! = MonsterMaxSMP[Num!]!

   MonsterAttack[Num!]! = castint(random(LowRanNuM!) + PLvL!/LowRanNuM! - random(LowRanNuM!))

   MonsterDefence[Num!]! = LowRanNuM! + random(LvL[Num!]!)

   MonsterEvasion[Num!]! = random(LowRanNuM!) + random(LvL[Num!]!) - random(LowRanNuM!)

   MonsterCanUseItem[Num!]! = Item!

   MonsterCanUseMagic[Num!]! = Magic!

}

Method MonsterAI(Num!)

{

   if(MonsterAttacked[Num!]! == 1)

   {

      while(MonsterHP[Num!]! > 0 || Dist! < PlayerRange!)

      {

         Clear(DidItHit!)

         SetConstants()

         getitemlocation(Num!, itmx!, itmy!, itmlayer!)

         Dist! = distance(playerx[0]!, playery[0]!, itmx!, itmy!)

         SetConstants()

         if(itmx! < playerx[0]! - 2 || itmx! < playerx[0]! + 2 && itmy! < playery[0]! - 2 || itmy! < playery[0]! + 2)

         {

            DidItHit! = createcanvas(60, 70)

            itemstance(Num!, "Attack")

            nuM! = random(3)

            if(nuM! <= 1)

            {

               SetConstants()

               giveHP(playerhandle[0]!, -MonsterAttack[Num!]!)

               getitemlocation(Num!, itmx!, itmy!, itmlayer!)

               Dist! = distance(playerx[0]!, playery[0]!, itmx!, itmy!)

               SetConstants()

               colorrgb(120, 0, 0)

               pixeltext(playerx[0]!*32, playery[0]!*32+32, MonsterAttack[Num!]!, DidItHit!)

               colorrgb(255, 255, 255)

            }

            elseif(nuM! == 2)

            {

               SetConstants()

               colorrgb(0, 0, 120)

               getitemlocation(Num!, itmx!, itmy!, itmlayer!)

               Dist! = distance(playerx[0]!, playery[0]!, itmx!, itmy!)

               SetConstants()

               pixeltext(playerx[0]!*32, playery[0]!*32+32, "MISS", DidItHit!)

               colorrgb(255, 255, 255)

            }

            elseif(nuM! >= 3)

            {

               SetConstants()

               colorrgb(0, 0, 120)

               getitemlocation(Num!, itmx!, itmy!, itmlayer!)

               Dist! = distance(playerx[0]!, playery[0]!, itmx!, itmy!)

               SetConstants()

               pixeltext(playerx[0]!*32, playery[0]!*32+32, "GUARDED", DidItHit!)

               colorrgb(255, 255, 255)

            }

            drawcanvastransparent(DidItHit!, playerx[0]!*32, playery[0]!*32+32, 0, 0, 0)

         }

         SetConstants()

         getitemlocation(Num!, itmx!, itmy!, itmlayer!)

         Dist! = distance(playerx[0]!, playery[0]!, itmx!, itmy!)

         itemstep(Num!, playerx[0]!, playery[0]!)

         delay(.0003)

         use! = random(3)

         if(use! <= 1)

         {

            if(MonsterHP[Num!]! < castint(MonsterHP[Num!]!/30) && MonsterCanUseItem[Num!]! == 1)

            {

               SetConstants()

               getitemlocation(Num!, itmx!, itmy!, itmlayer!)

               Dist! = distance(playerx[0]!, playery[0]!, itmx!, itmy!)

               animation("Potion.anm", itmx!*32, itmy!*32)

               MonsterHP[Num!]! = MonsterHP[Num!]! + castint(random(MonsterMaxHP[Num!]!/3))

               SetConstants()

            }

         }

         elseif(use! == 2 && MonsterCanUseMagic[Num!]! == 1)

         {

            PlayerHP! = GetHP(playerhandle[0]$)

            if(PlayerHP! > MonsterHP[Num!]!)

            {

               SetConstants()

               getitemlocation(Num!, itmx!, itmy!, itmlayer!)

               Dist! = distance(playerx[0]!, playery[0]!, itmx!, itmy!)

               animation("fire.anm", itmx!*32, itmy!*32)

               giveHP(playerhandle[0]!, castint(MonsterMaxSMP[Num!]!/MonsterAttack[Num!]!))

               SetConstants()

            }

         }

         elseif(use! == 3 && MonsterCanUseMagic[Num!]! == 1)

         {

            PlayerHP! = GetHP(playerhandle[0]$)

            if(PlayerHP! > MonsterHP[Num!]!)

            {

               SetConstants()

               getitemlocation(Num!, itmx!, itmy!, itmlayer!)

               Dist! = distance(playerx[0]!, playery[0]!, itmx!, itmy!)

               animation("shock.anm", itmx!*32, itmy!*32)

               giveHP(playerhandle[0]!, castint(MonsterMaxSMP[Num!]!/MonsterAttack[Num!]!))

               SetConstants()

            }

         }

      }

   }

}
```

### Shadow Eden · 2007-02-21 15:40 · #K381718

i haven't tested it but it looks alright... maybe someone who knows a thing or two will do so...
the custom AI of most of the CBS have basically been #random()

### rpg gamer 17 · 2007-02-22 01:31 · #K381835

okay what im going to have to do (mostlikly) is create a monstermove method.
you know set a variable that tells its graphic direction. then make a method that checks if its graphical direction is facing the player.
then in the MonstersAIThread.prg check if the monster is facing the player then switch aninmation and attack.
in this prg im going to place its health bar, use skills, items, and attack, ect... and its going to be a method and the acual AI (the prg that holds the method) is going to be threaded. when i make a Monster the Num! will be replaced with the handle of the item
...
AH! HA! i finally figured out the thread he same prg reason
...
do i get a cookie? Crying or Very sad please!!
*cough* well i must code Very Happy
P.S. has anyone noticed that i basiclly use this post to do my planning?
*edit*
i think this is done... please check...

**Code:**

```
Method distance(x1!, y1!, x2!, y2!)

{

   squaredx! = (x1!-x2!)^2

   squaredy! = (y1!-y2!)^2

   returnmethod( sqrt(squaredx! + squaredy!) )

}

Method Monsterstats(Num!, MonAttackRange[Num!]!, LowRanNuM!, HEAlTH!, Smp!, Potion!, Magic!, ElementMagic$, AutoAttack[Num!]!)

{

   Global(MonsterHP[Num!]!)

   Global(MonsterMaxHP[Num!]!)

   Global(MonsterLvL[Num!]!)

   PLvL! = getlvl(playerhandle[0]$)

   Monstername[Num!]$ = getitemname("Monster" + Num! + ".itm")

   MonsterLvL[Num!]! = random(LowRanNuM!) + PLvL! - random(LowRanNuM!)

   MonsterMaxHP[Num!]! = castint(random(HEAlTH!/random(LvL[Num!]!)) + HEAlTH!)

   MonsterHP[Num!]! = MonsterMaxHP[Num!]!

   MonsterMaxSMP[Num!]! = random(Smp*random(LvL[Num!]!)) + Smp!

   MonsterSMP[Num!]! = MonsterMaxSMP[Num!]!

   MonsterAttack[Num!]! = castint(random(LowRanNuM!) + PLvL!/LowRanNuM! - random(LowRanNuM!))

   MonsterDefence[Num!]! = LowRanNuM! + random(LvL[Num!]!)

   MonsterEvasion[Num!]! = random(LowRanNuM!) + random(LvL[Num!]!) - random(LowRanNuM!)

   MonsterCanUsePotion[Num!]! = Potion!

   MonsterAttackRange[Num!]! = MonAttackRange!

   MonsterCanUseThisElement[Num!]$ = ElementMagic$

   MonsterCanUseMagic[Num!]! = Magic!

   ///////////////////

   while(MonsterHP[Num!]! > 0 && onboard(0) == 1)

   {

      if(AutoAttack[Num!]! == 1)

      {

         MonsterAttacked[Num!]! = 1

      }

      getitemlocation(Num!, itmx[Num!]!, itmy[Num!]!, itmlayer!)

      SetConstants()

      Dist! = distance(playerx[0]!, playery[0]!, itmx[Num!]!, itmy[Num!]!)

      if(MonsterAttacked[Num!]! == 1 || Dist! < PlayerRange!)

      {

         getitemlocation(Num!, itmx[Num!]!, itmy[Num!]!, itmlayer!)

         SetConstants()

         Dist! = distance(playerx[0]!, playery[0]!, itmx[Num!]!, itmy[Num!]!)

         while(MonsterHP[Num!]! > 0 || Dist! < PlayerRange!)

         {

            Clear(DidItHit!)

            SetConstants()

            getitemlocation(Num!, itmx[Num!]!, itmy[Num!]!, itmlayer!)

            Dist! = distance(playerx[0]!, playery[0]!, itmx[Num!]!, itmy[Num!]!)

            SetConstants()

            if(itmx[Num!]! < playerx[0]! - MonAttackRange[Num!]! || itmx[Num!]! < playerx[0]! + MonAttackRange[Num!]! && itmy[Num!]! < playery[0]! - MonAttackRange[Num!]! || itmy[Num!]! < playery[0]! + MonAttackRange[Num!]!)

            {

               itemstance(Num!, "Attack")

               nuM! = random(3)

               if(nuM! <= 1)

               {

                  Mutirun()

                  {

                     SetConstants()

                     giveHP(playerhandle[0]!, -MonsterAttack[Num!]!)

                     getitemlocation(Num!, itmx[Num!]!, itmy[Num!]!, itmlayer!)

                     Dist! = distance(playerx[0]!, playery[0]!, itmx[Num!]!, itmy[Num!]!)

                     SetConstants()

                     colorrgb(120, 0, 0)

                     pixeltext(playerx[0]!*32, playery[0]!*32+32, MonsterAttack[Num!]!, DidItHit[Num!]!)

                     colorrgb(255, 255, 255)

                     MonsterCharge[Num!]! = 0

                  }

               }

               elseif(nuM! == 2)

               {

                  Mutirun()

                  {

                     SetConstants()

                     colorrgb(0, 0, 120)

                     getitemlocation(Num!, itmx[Num!]!, itmy[Num!]!, itmlayer!)

                     Dist! = distance(playerx[0]!, playery[0]!, itmx[Num!]!, itmy[Num!]!)

                     SetConstants()

                     pixeltext(playerx[0]!*32, playery[0]!*32+32, "MISS", DidItHit[Num!]!)

                     colorrgb(255, 255, 255)

                     MonsterCharge[Num!]! = 0

                  }

               }

               elseif(nuM! >= 3)

               {

                  Mutirun()

                  {

                     SetConstants()

                     colorrgb(0, 0, 120)

                     getitemlocation(Num!, itmx[Num!]!, itmy[Num!]!, itmlayer!)

                     Dist! = distance(playerx[0]!, playery[0]!, itmx[Num!]!, itmy[Num!]!)

                     SetConstants()

                     pixeltext(playerx[0]!*32, playery[0]!*32+32, "GUARDED", DidItHit[Num!]!)

                     colorrgb(255, 255, 255)

                     MonsterCharge[Num!]! = 0

                  }

               }

            }

            SetConstants()

            getitemlocation(Num!, itmx[Num!]!, itmy[Num!]!, itmlayer!)

            Dist! = distance(playerx[0]!, playery[0]!, itmx[Num!]!, itmy[Num!]!)

            itemstep(Num!, playerx[0]!, playery[0]!)

            use! = random(4) //i ment to put 4

            if(use! <= 1)

            {

               if(MonsterHP[Num!]! < castint(MonsterHP[Num!]!/30) && MonsterCanUsePotion[Num!]! == 1)

               {

                  SetConstants()

                  getitemlocation(Num!, itmx[Num!]!, itmy[Num!]!, itmlayer!)

                  Dist! = distance(playerx[0]!, playery[0]!, itmx[Num!]!, itmy[Num!]!)

                  animation("Potion.anm", itmx!*32, itmy!*32)

                  MonsterHP[Num!]! = MonsterHP[Num!]! + castint(random(MonsterMaxHP[Num!]!/3))

                  SetConstants()

                  MonsterCharge[Num!]! = 0

               }

            }

            elseif(use! == 2 && MonsterCanUseMagic[Num!]! == 1)

            {

               PlayerHP! = GetHP(playerhandle[0]$)

               if(PlayerHP! > MonsterHP[Num!]!)

               {

                  SetConstants()

                  getitemlocation(Num!, itmx[Num!]!, itmy[Num!]!, itmlayer!)

                  Dist! = distance(playerx[0]!, playery[0]!, itmx[Num!]!, itmy[Num!]!)

                  animation(MonsterCanUseThisElement[Num!]$ ".anm", Playerx[0]!*32, playery*32)

                  giveHP(playerhandle[0]!, castint(MonsterMaxSMP[Num!]!/MonsterAttack[Num!]!))

                  SetConstants()

                  MonsterCharge[Num!]! = 0

               }

            }

         }

      }

      else

      {

         move! = random!

         push

      }

   }

}

Method MonsterCanvasMethod(NuM!)

{

   MonsterCharge[NuM!]! = 0

   Global(MonsterCharge[NuM!]!)

   Monster[NuM!]! = createcanvas(100, 10)

   while(playeronboard[NuM!]! = 1)

   {

      Clear(Monster[NuM!]!)

      If(onboard(0) == 1)

      {

         playeronboard[NuM!]! = 1

      }

      else

      {

         playeronboard[NuM!]! = 0

      }

      While(MonsterHP[NuM!]! > 0)

      {

         If(onboard(0) == 1)

         {

            playeronboard[NuM!]! = 1

         }

         else

         {

            playeronboard[NuM!]! = 0

         }

         DrawMonHP[NuM!]! = castint(MonsterHP[NuM!]!/MonsterMaxHP[NuM!]!)

         colorrgb(0, 0, 120)

         fillrect(0, 10, 100, 10, Monster[NuM!]!)

         colorrgb(255,255,255)

         colorrgb(0, 0, 120)

         fillrect(0, 10, DrawMonHP[NuM!]!*100, 10, Monster[NuM!]!)

         colorrgb(255,255,255)

         getitemlocation(Num!, itmx[NuM!]!, itmy[NuM!]!, itmlayer!)

         if(MonsterCharge[NuM!]! < 100)

         {

            MonsterCharge[NuM!]! = MonsterCharge[NuM!]! + random(MonsterLvL[Num!]!)

         }

         if(MonsterCharge[NuM!]! >= 100)

         {

            MonsterCharge[NuM!]! == 100

         }

         drawcanvastransparent(Monster[NuM!]!, itmx[NuM!]!*32, itmy[NuM!]!*32+32, 0, 0, 0)

      }

   }

}
```
