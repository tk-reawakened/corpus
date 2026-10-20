---
kind: forum-thread
id: "toolkitzone-forum/43996"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "43996"
title: "Proof of concept BS... proto"
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=43996"
written: "2009-10-12T20:02:00"
last_post: "2009-10-14T20:10:00"
date_confidence: "exact"
captured: ["20100102024252"]
author: "draconous1846"
repliers: ["playsoon"]
authors: ["draconous1846", "playsoon"]
posts_present: 6
pages_present: [1]
pages_total: 2
posts_per_page: 10
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 2, start: 11, end: 20, url: "http://toolkitzone.com/forum/viewtopic.php?t=43996&start=10", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_483453", captured: "20100102024252", sha256: "ded81dec8b0fe2bcbb8a41ff153c6408327744d4dfdc99c925a7554ecdc04228", wayback_url: "https://web.archive.org/web/20100102024252/http://toolkitzone.com/forum/viewtopic.php?p=483453"}
links: []
---

# Proof of concept BS... proto

### draconous1846 · 2009-10-12 20:02 · #K483436

This is a battle Engine that is without canvases, battlebackground (*.bkg), or boards (*.bds). As will be asked about the costant redrawing of main cha. is to deal with the draw over / flicker problem. I have only two probs. one : if I start off with two "J" attacks, it freezes. and two:
I cant win by "C" I have to use "C" X2+, then "J"X2.

**Code:**

```
// //////  RealityWarp Engine mark 0.0.1 ( Thoaz)

E1=loadEnemy("Barbricandbrood.ene",0) // / plug in monster, gamr does rest.

E1[0]=getEnemyHp(E1) // /// all the stats needed in the battle.  FF style.

E1[1]=getEnemyFp(E1)

E1[2]=getEnemyDp(E1)

pl1=activePlayer()

pl1[0]=getHp(pl1)

pl1[1]=getFp(pl1)

pl2[2]=getDp(pl1)

ne1=pl1[1]-E1[2]

d1=E1[1]-pl1[2]

movepl1=(pl1[1]*.03)+1

movee1=(E1[1]*.03)+1

method enemy()  /// draws enemy on screen.

{

ro=setEnemyStance("Rest",0)

DrawAnimation(ro,290,300)

}

method destroyE1() /// to destroy.

{

destroyStance(ro)

}

method pl1r() /// rest.

{

po=Animation("start/start_rest.anm",400,300)

}

method pl1f() /// the attack sequence.  Its awesome sauce

{

animation("start/start_fight.anm",286,300)

}

method destroypl1()  /// to die.

{

endanimation(po)

}

method pde()  /// player damage enemy

{

mo=getEnemyHp(0)

ne11=mo-ne1

setEnemyHp(0, - ne11)

}

method pdec()  /// pde combo

{

mo=getEnemyHp(0)

ne11=mo-ne1

setEnemyHp(0, ne11 - movepl1) /// placing in ()-() causes immortality.

}

method edp() /// enemy damage player

{

givehp(pl1, -d1)

}

while (getHp (pl1) > 0 && getEnemyHp (E1) > 0)

{

turn()               /// the battle start. goes by highest HP.

method turn()

{

bitmap("bkg.jpg")

enemy()

pl1r()   /// sets them on board.

}

if ( getHp(pl1) >= getEnemyHp(E1))

{

goddess()

}

else

{

semi()

}

method goddess()

{

setimagetranslucent("ldbkg.jpg",10,10,80,200)

pixeltext(10,10,"Attack")

pixeltext(10,31,"Item")

pixeltext(10,52,"Ability")

pixeltext(10,73,"Craft") /// the menu.

pixeltext(10,84,"run")

pl1r() /// places on  board without blips.

while (movepl1 >=1) /// to erase flicker.

{

if (KeyDown("J"))

{

attack() ///this on down to semi() is were I run into probs.

}             /// abit.

elseif (KeyDown("C"))

{

combo()

}

}

method semi()

{

edp()     /// works flawlessly.

pl1r()

if (movepl1 >= 1) /// at test mode. enemy only has 1 move/turn.

{

movepl1=(pl1[1]*.03)+1 /// gives full moves to cha.

goddess()

}

else

{

turn() restarr turn.

}

}

method attack() /// kepress, J.

{

pl1f() /// moves to attack. before going back to rest.(looks like an atk.)

delay(.15) /// so the attack looks like it hits.

if (movepl1 >= 1 )

{

pde() /// damages  enemy

movepl1-- /// then takes off a move.

goddess()

}

elseif (movepl1 < 1)

{

moveel=(E1[1]*.03)+1 /// supposed to go to next turn after movepl1

semi() /// goes to 0 or less. doesn't work that way.

}

}

method combo()

{

pl1f()  /// weakens opt. with a powerful combo attack.

delay(.15)  /// deals movepl1 * damg to opt. (finally).

getenemyHP(0)

pdec()

movepl1=(pl1[1]*.03)+1 /// regives full movement.

semi()  /// goes to enemies turn.

}

}

}

mwin(getHP(pl1))

mwin(getEnemyHP(E1))   /// shows what everyone had. move and hpwise.

mwin(movepl1)

mwin(movee1)

wait()
```

thats my baby at the moment. What do you think? Oh and Thaoz is one of the characters in our game.
-Draco

### draconous1846 · 2009-10-13 00:20 · #K483444

Thanks for the snippet / clarfication, added it.
-Draco

### playsoon · 2009-10-13 08:32 · #K483453

Eh... might take time to read the code if it had some proper indenting. It hurts my head as is :\

### draconous1846 · 2009-10-13 20:13 · #K483458

**Code:**

```
// //////  RealityWarp Engine mark 0.0.1 ( Thoaz)

E1=loadEnemy("Barbricandbrood.ene",0) // / plug in monstername, and game does th rest.

E1[0]=getEnemyHp(E1) // /// all the stats needed in the battle.  FF style.

E1[1]=getEnemyFp(E1)

E1[2]=getEnemyDp(E1)

pl1=activePlayer()

pl1[0]=getHp(pl1)

pl1[1]=getFp(pl1)  /// these are for all needed calculations.

pl2[2]=getDp(pl1)  /// will be making an armor class / damage

ne1=pl1[1]-E1[2]  /// mods later.

d1=E1[1]-pl1[2]

movepl1=(pl1[1]*.03)+1  /// move modifier. for player pl, and E.

movee1=(E1[1]*.03)+1

method enemy() /// draws enemy on screen.

{

   if(ro == 0){ //If no stance loaded

      ro=setEnemyStance("Rest",0) //Load stance

   }

   DrawAnimation(ro,290,300) //Draw next frame of loaded stance

}

method destroyE1()  ///destroy enemy when dead.

{

   destroyStance(ro)

}

method pl1r() /// pl1 rest.

{

   po=Animation("start/start_rest.anm",400,300)

}

method pl1f() /// pl1 fight, static fights are the only thing

{            /// I dislike about the default. That and placement.

   animation("start/start_fight.anm",286,300)

}

method destroypl1() ///pl1 dead animation.

{

   endanimation(po)

}

method pde() /// player damages enemy.

{

   mo=getEnemyHp(0)

   ne11=mo-ne1

   setEnemyHp(0, - ne11)

}

method pdec() /// pde combo

{

   mo=getEnemyHp(0)

   ne11=mo-ne1

   setEnemyHp(0, ne11 - movepl1)

}

method edp() /// enemy damgaes player

{

   givehp(pl1, -d1)

}

while (getHp (pl1) > 0 && getEnemyHp (E1) > 0) /// BS start.

{

   turn()    /// HP based turn system. You know the more hp

   method turn() /// you have the more energy. less = fatigue.

   {

      bitmap("bkg.jpg")  places on the map.

      enemy()

      pl1r()

   }

   if ( getHp(pl1) >= getEnemyHp(E1))

   {

      goddess() /// pl1 starts.

   }

   else

   {

      semi() /// enemy starts.

   }

   method goddess() /// the player turn. Cx2+,Jx2 to kill barbricand,

   {                /// Jx2 before kill freezes bs.

      setimagetranslucent("ldbkg.jpg",10,10,80,200)

      pixeltext(10,10,"Attack")

      pixeltext(10,31,"Item")

      pixeltext(10,52,"Ability")

      pixeltext(10,73,"Craft")

      pixeltext(10,84,"run")

      pl1r()

      while (movepl1 >=1) /// removes flicker.

      {

         if (KeyDown("J")) // /attack sequence only

         {                 ///so far.

            attack()

         }

         elseif (KeyDown("C"))

         {

            combo()

         }

      }

      method semi()

      {

         edp()     /// damage player. this method is

         pl1r()  /// flawless. no quirks.

         if (movepl1 >= 1)

         {

            movepl1=(pl1[1]*.03)+1

            goddess()

         }

         elseif(movepl1 <1)

         {

            turn()

         }

         method attack()

         {

            pl1f()

            delay(.15)

            if (movepl1 >= 1 )

            {

               getEnemyHp(E1)

               pde() // / damage enemy.

               movepl1--  /// -1 move.

               goddess()

            }

            elseif (movepl1 < 1)

            {

               moveel=(E1[1]*.03)+1

               semi()

            }

         }

         method combo()

         {

            pl1f()

            delay(.15)

            getenemyHP(0)

            pdec() ///combo damage.

            movepl1=(pl1[1]*.03)+1

            semi()

         }

      }

   }

}

mwin(getHP(pl1))  /// these are controls ot watch for the

mwin(getEnemyHP(E1)) /// move modifier.

mwin(movepl1) /// and life points. to make sure damage is

mwin(movee1) /// being done.

wait()
```

OK. Everything indented and the /// to clarify why everythings in there place. Oh, I have the attack and combo outside of " goddess()" because it was fubaring up my code otherwise. Sorr about not indenting and thanks for your alls time.
-Draco

### draconous1846 · 2009-10-14 06:19 · #K483483

Ok, the turn() thing works somewhat. It still wont end the program with out hitting C twice or more ( to lower hp), and J twice. but J will now make the prog to skip all line of code after a while to end it.
as for the stats. Do you mean my character stats ? I'm using the stats of the defalt character without armor.
IF you mean how am I using them? I made a detailed chart on everything but the system logged me off. So I'll just quickly jot this down.
E1=loadEnemy("monstername",0) : is Enemy one, and allows for plug and play graphics.
and
pl1=activePlayer(): is player one. I don't get the whole playerhandle(x) thing, expecially when there aren't really going to be any " Set" party members. rather than a free roaming you don't know who you may gain type of thing.
[0]= HP, is not in se yet, but will be soon to set up DR.
DR=(E1[0]+E1[2]*.05)
this way your battles last somewhat long.
[1]= Fp you've already seen it as move modifier ( Oh, I'm going to have such epic combo animations.).
as well as once the whole making my monsters dead ( they take damage, but I can get me down to 0 and my enemies down to -554 and still no end to the battle loop.)I'm putting in a
r= E1[2]*.05
comsave=random(r)
then place it as setEnemyHP(E1, ne11+comsave) thus making battles longer, nad giving a chance to make saving rolls.
and a
r1=E1[1]*.05
comroll=random(r1)
then set it in a giveHp(pl1, -(d1+comroll)) thus making a combat roll.
these will also be used as my dice rolls. Thus giving some randomness to fights.
[2] = Dp ... pretty much the above code is what I'm going to be using this for that and damage. [1]-[2] = damage.
then all I needed to do was set it in there.
///////////////////
Ok a few things real quick.
///////////////// Removeing goddess() from J makes it go fuzzy and restart, but it also removes the fight graphic partially ( he'll go to the E1, but not back to origional position.
replaceing goddess() with turn() after attack() causes the same prob. so goddess() isn't to blame. by removing the movepl1=(pl1[1]*.03)+1 in combo() also doesn't impact it. So I'm keeping that out, but even when the monster is past - hp, battle loop still goes on.
/////////////// the problem lays not necessarily with combo() or semi() since neither will end once the" while ( getHp(pl1) > 0 && getEnemyHp(E1) >0) {}" is resolved. so yeah goddess() perplexes me. but is proving to be beautifull when not being evil.
-Draco.

### draconous1846 · 2009-10-14 20:10 · #K483513

actually your debugger version would prob. be best ... tried going over it, and sprucing it up. get the same probs.
As for recursive functions ... isn't that what you ment by a central function that calls all the other functions for the BS? Or was that a gross misunderstanding in my part?
-Draco

> [!missing] gap:11-20 · http://toolkitzone.com/forum/viewtopic.php?t=43996&start=10 · never-captured
> Page 2 of 2 was not recovered.
