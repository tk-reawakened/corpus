---
kind: forum-thread
id: "toolkitzone-forums/12318"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "toolkit 2.x support"
skin: "phpbb2"
thread_id: "12318"
title: "Menu System troble"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12318"
written: "2004-12-08T13:28:00"
last_post: "2004-12-09T13:50:00"
date_confidence: "exact"
captured: ["20050116235312"]
author: "Unelemented"
repliers: ["Levi"]
authors: ["Unelemented", "Levi"]
posts_present: 8
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_136963_amp_", captured: "20050116235312", sha256: "4bd6f6caff38782c6b2fe9543174de36d37279a202daaa78433f18d6664d6cc6", wayback_url: "https://web.archive.org/web/20050116235312/http://www.toolkitzone.com/forums/viewtopic.php?p=136963&amp="}
links: []
---

# Menu System troble

### Unelemented · 2004-12-08 13:28 · #B136446

im having some problems with my code

**Code:**

```
:menurestart

#Bitmap("back.bmp")

#SetButton("Stats.bmp", 0, 460, 30, 120, 32)

#SetButton("abilities.bmp", 3, 460, 75, 120, 32)

#SetButton("Equip.bmp", 1, 460, 120, 120, 32)

#SetButton("Items.bmp", 2, 460, 165, 120, 32)

#SetButton("Resume.bmp", 6, 30, 300, 120, 32)

#SetButton("Load.bmp", 5, 290, 300, 120, 32)

#SetButton("x.bmp", 7, 580, 320, 20, 20)

#SetButton("save.bmp", 4, 160, 300, 120, 32)

#if(worldmap!==1)

{

#setbutton("Map.bmp", 8, 460, 0, 120, 32)

}

#GetHP(playerhandle[0]$,oneHP!)

#GetMaxHP(playerhandle[0]$,oneMaxHP!)

#GetFP(playerhandle[0]$,onefp!)

#GetSMP(playerhandle[0]$,onemp!)

#GetMaxSMP(playerhandle[0]$,onemaxmp!)

#GetLevel(playerhandle[0]$,onelevel!)

#GetDP(playerhandle[0]$,onedp!)

#SetImage( "mainchar.jpg", 8, 8, 100, 64, 64)

#Text(8,1,"<playerhandle[0]$>   Level: <onelevel!>")

#Text(8,2,"<onehp!>HP/<onemaxhp!>HP")

#Text(8,3,"<onemp!>MP/<onemaxmp!>MP")

#Text(8,4,"<onefp!>FP and <onedp!>DP")

***********************************************

#If (playerHandle[1]$~= "")

   {

#gethp(playerhandle[1]$,twohp!)

#getmaxhp(playerhandle[1]$,twomaxhp!)

#getfp(playerhandle[1]$,twofp!)

#getsmp(playerhandle[1]$,twomp!)

#getmaxsmp(playerhandle[1]$,twomaxmp!)

#getlevel(playerhandle[1]$,twolevel!)

#getdp(playerhandle[1]$,twodp!)

#text(4,6,"<playerhandle[1]$>   Level: <twolevel!>")

#text(4,7,"<twohp!>HP/<twomaxhp!>HP")

#text(4,8,"<twomp!>MP/<twomaxmp!>MP")

#text(4,9,"<twofp!>FP and <twodp!>DP")

   }

***********************************************

#If (playerHandle[2]$~= "")

   {

#gethp(playerhandle[2]$,threehp!)

#getmaxhp(playerhandle[2]$,threemaxhp!)

#getfp(playerhandle[2]$,threefp!)

#getsmp(playerhandle[2]$,threemp!)

#getmaxsmp(playerhandle[2]$,threemaxmp!)

#getlevel(playerhandle[2]$,threelevel!)

#getdp(playerhandle[2]$,threedp!)

#text(12,6,"<playerhandle[2]$>   Level: <threelevel!>")

#text(12,7,"<threehp!>HP/<threemaxhp!>HP")

#text(12,8,"<threemp!>MP/<threemaxmp!>MP")

#text(12,9,"<threefp!>FP and <threedp!>DP")

   }

***********************************************

***********************************************

#If (playerHandle[3]$~= "")

   {

#gethp(playerhandle[3]$,fourhp!)

#getmaxhp(playerhandle[3]$,fourmaxhp!)

#getfp(playerhandle[3]$,fourfp!)

#getsmp(playerhandle[3]$,fourmp!)

#getmaxsmp(playerhandle[3]$,fourmaxmp!)

#getlevel(playerhandle[3]$,fourlevel!)

#getdp(playerhandle[3]$,fourdp!)

#text(4,11,"<playerhandle[3]$>   Level: <fourlevel!>")

#text(4,12,"<fourhp!>HP/<fourmaxhp!>HP")

#text(4,13,"<fourmp!>MP/<fourmaxmp!>MP")

#text(4,14,"<fourfp!>FP and <fourdp!>DP")

}

#If (playerHandle[4]$~= "")

   {

#gethp(playerhandle[4]$,fivehp!)

#getmaxhp(playerhandle[4]$,fivemaxhp!)

#getfp(playerhandle[4]$,fivefp!)

#getsmp(playerhandle[4]$,fivemp!)

#getmaxsmp(playerhandle[4]$,fivemaxmp!)

#getlevel(playerhandle[4]$,fivelevel!)

#getdp(playerhandle[4]$,fivedp!)

#text(12,11,"<playerhandle[4]$>   Level: <fivelevel!>")

#text(12,12,"<fivehp!>HP/<fivemaxhp!>HP")

#text(12,13,"<fivemp!>MP/<fivemaxmp!>MP")

#text(12,14,"<fivefp!>FP and <fivedp!>DP")

}

:buttonrestart

#done!==0

#while(done!==0)

{

#mouseclick(x!,y!)

#checkbutton(x!,y!,button!)

***********************************************

#if(button!==0)

{

#internalmenu(3)

}

***********************************************

***********************************************

#if(button!==1)

{

#internalmenu(2)

}

***********************************************

***********************************************

#if(button!==2)

{

#internalmenu(1)

}

***********************************************

***********************************************

#if(button!==3)

{

#internalmenu(4)

}

***********************************************

***********************************************

#if(button!==4)

{

        *'load game' clicked

        #dirsav(dest$)

        #if(dest$~="CANCEL")

        {

            #load(dest$)

            #done!=1

            #end

        }

    }

***********************************************

***********************************************

#if(button!==5)

{

        *'load game' clicked

        #dirsav(dest$)

        #if(dest$~="CANCEL")

        {

            #save(dest$)

            #done!=1

            #end

        }

    }

***********************************************

#If(button!==6)

{

#fontsize(size!)

#ClearButtons()

#done!=1

}

***********************************************

***********************************************

#if(button!==7)

{

#dos()

}

***********************************************

***********************************************

#if(button!==8)

{

#bitmap("world-map.jpg")

#SetButton("cancel.bmp", 9, 160, 300, 120, 32)

#branch(:buttonrestart)

}

#if(button!==9)

{

#Branch(:menurestart)

}
```

i cant get the 9th button to work inside the 8ths button command which works.
it works with out the button but not with the button
please help me solve this problem

### Levi · 2004-12-08 13:59 · #B136453

Could you re explain that for me? Do you mean you can't get the if statment for button 9 to work? If so then that's because you are branching out before it reaches the if.
If you mean that the if statement for button 9 doesn't work even though you put it before the branch command Then I'm lost.

### Unelemented · 2004-12-08 20:41 · #B136578

yeah i cnat get the if statement for button 9 to work
with or without the branch
well actually the button does work but it dies the load buttons command not the branch
it worked without a button just using a wait command but that made it feel weird

### Unelemented · 2004-12-08 22:32 · #B136621

ok im trying using the #run command
with the to bits of code
button 8s code

**Code:**

```
#if(button!==8)

{

#run("menumap.prg")

}
```

and the code it runs

**Code:**

```
#bitmap("world-map.jpg")

#SetButton("cancel.bmp", 9, 160, 300, 120, 32)

#done!==0

#while(done!==0)

#mouseclick(x!,y!)

#checkbutton(x!,y!,button!)

#if(button!==9)

{

#run("Menu.prg")

}
```

everything comes up but the button doesnt work
it works if you run it without going through the menu system but it doesnt when you do

### Unelemented · 2004-12-09 11:57 · #B136956

all good now i fixed it
i needed to use the #ClearButtons() command

### Unelemented · 2004-12-09 13:20 · #B136960

K i have a new problem now

**Code:**

```
{

#fontsize(25)

#ClearButtons()

#bitmap("statsbkg.bmp")

#text(5,2,"Which Characters stats do you want to view?")

#text(5,3,"1 - <playerhandle[0]$>")

#text(5,4,"2 - <playerhandle[1]$>")

#text(5,5,"3 - <playerhandle[2]$>")

#text(5,6,"4 - <playerhandle[3]$>")

#text(5,7,"5 - <playerhandle[4]$>")

#wait(a!)

#clear()

#done!==0

#while(done!==0)

{

   #if("a!==1")

   {

   #GetHP(playerhandle[0]$,HP!)

   #GetMaxHP(playerhandle[0]$,MaxHP!)

   #GetFP(playerhandle[0]$,fp!)

   #GetSMP(playerhandle[0]$,mp!)

   #GetMaxSMP(playerhandle[0]$,maxmp!)

   #GetLevel(playerhandle[0]$,level!)

   #GetDP(playerhandle[0]$,dp!)

   #SetImage( "mainchar.jpg", 8, 8, 100, 64, 64)

   #text(5,5,"<HP!> HP / <MaxHP!> HP")

   #text(5,6,"<mp!> SMP / <maxmp!> MP")

   #text(5,3,"<playerhandle[0]$>, Is level <level!>")

   #text(5,7,"Has <fp!> Fighting Ability")

   #text(5,8,"Has <dp!> Defencive Ability")

   #text(5,9,"Has <playerhandle[0]$[experience]!> Experience")

   #wait()

   #kill(a!)

   #kill(HP!)

   #kill(MaxHP!)

   #kill(mp!)

   #kill(maxmp!)

   #kill(level!)

   #kill(fp!)

   #kill(dp!)

   #done!==1

   #run("Menu.prg")

   }

{

   #if("a!==2")

   {

   #GetHP(playerhandle[1]$,HP!)

   #GetMaxHP(playerhandle[1]$,MaxHP!)

   #GetFP(playerhandle[1]$,fp!)

   #GetSMP(playerhandle[1]$,mp!)

   #GetMaxSMP(playerhandle[1]$,maxmp!)

   #GetLevel(playerhandle[1]$,level!)

   #GetDP(playerhandle[1]$,dp!)

   #SetImage( "mainchar.jpg", 8, 8, 100, 64, 64)

   #text(5,5,"<HP!> HP / <MaxHP!> HP")

   #text(5,6,"<mp!> SMP / <maxmp!> MP")

   #text(5,3,"<playerhandle[1]$>, Is level <level!>")

   #text(5,7,"Has <fp!> Fighting Ability")

   #text(5,8,"Has <dp!> Defencive Ability")

   #text(5,9,"Has <playerhandle[1]$[experience]!> Experience")

   #wait()

   #kill(a!)

   #kill(HP!)

   #kill(MaxHP!)

   #kill(mp!)

   #kill(maxmp!)

   #kill(level!)

   #kill(fp!)

   #kill(dp!)

   #done!==1

   #run("Menu.prg")

   }

{

   #if("a!==3")

   {

   #GetHP(playerhandle[2]$,HP!)

   #GetMaxHP(playerhandle[2]$,MaxHP!)

   #GetFP(playerhandle[2]$,fp!)

   #GetSMP(playerhandle[2]$,mp!)

   #GetMaxSMP(playerhandle[2]$,maxmp!)

   #GetLevel(playerhandle[2]$,level!)

   #GetDP(playerhandle[2]$,dp!)

   #SetImage( "mainchar.jpg", 8, 8, 100, 64, 64)

   #text(5,5,"<HP!> HP / <MaxHP!> HP")

   #text(5,6,"<mp!> SMP / <maxmp!> MP")

   #text(5,3,"<playerhandle[2]$>, Is level <level!>")

   #text(5,7,"Has <fp!> Fighting Ability")

   #text(5,8,"Has <dp!> Defencive Ability")

   #text(5,9,"Has <playerhandle[2]$[experience]!> Experience")

   #wait()

   #kill(a!)

   #kill(HP!)

   #kill(MaxHP!)

   #kill(mp!)

   #kill(maxmp!)

   #kill(level!)

   #kill(fp!)

   #kill(dp!)

   #done!==1

   #run("Menu.prg")

   }

{

   #if("a!==4")

   {

   #GetHP(playerhandle[3]$,HP!)

   #GetMaxHP(playerhandle[3]$,MaxHP!)

   #GetFP(playerhandle[3]$,fp!)

   #GetSMP(playerhandle[3]$,mp!)

   #GetMaxSMP(playerhandle[3]$,maxmp!)

   #GetLevel(playerhandle[3]$,level!)

   #GetDP(playerhandle[3]$,dp!)

   #SetImage( "mainchar.jpg", 8, 8, 100, 64, 64)

   #text(5,5,"<HP!> HP / <MaxHP!> HP")

   #text(5,6,"<mp!> SMP / <maxmp!> MP")

   #text(5,3,"<playerhandle[3]$>, Is level <level!>")

   #text(5,7,"Has <fp!> Fighting Ability")

   #text(5,8,"Has <dp!> Defencive Ability")

   #text(5,9,"Has <playerhandle[3]$[experience]!> Experience")

   #wait()

   #kill(a!)

   #kill(HP!)

   #kill(MaxHP!)

   #kill(mp!)

   #kill(maxmp!)

   #kill(level!)

   #kill(fp!)

   #kill(dp!)

   #done!==1

   #run("Menu.prg")

   }

{

   #if("a!==5")

   {

   #GetHP(playerhandle[4]$,HP!)

   #GetMaxHP(playerhandle[4]$,MaxHP!)

   #GetFP(playerhandle[4]$,fp!)

   #GetSMP(playerhandle[4]$,mp!)

   #GetMaxSMP(playerhandle[4]$,maxmp!)

   #GetLevel(playerhandle[4]$,level!)

   #GetDP(playerhandle[4]$,dp!)

   #SetImage( "mainchar.jpg", 8, 8, 100, 64, 64)

   #text(5,5,"<HP!> HP / <MaxHP!> HP")

   #text(5,6,"<mp!> SMP / <maxmp!> MP")

   #text(5,3,"<playerhandle[4]$>, Is level <level!>")

   #text(5,7,"Has <fp!> Fighting Ability")

   #text(5,8,"Has <dp!> Defencive Ability")

   #text(5,9,"Has <playerhandle[4]$[experience]!> Experience")

   #wait()

   #kill(a!)

   #kill(HP!)

   #kill(MaxHP!)

   #kill(mp!)

   #kill(maxmp!)

   #kill(level!)

   #kill(fp!)

   #kill(dp!)

   #done!==1

   #run("Menu.prg")

   }
```

When you press 1 to 5 it only comes up with the first players stats not any of the others
and it cant read the experience code
it comes up with 0 at the start and its sposed to have 100
damn custom stats menu

### Levi · 2004-12-09 13:41 · #B136962

Ummm...why are your if statements surrounded with " " I ask because conditions placed like that are not read like conditions but like literal values. Try removing those and see how far it gets you.
Also I see that each time you end one of your if statements you put a { after it.
These serve no purpose and probably confuse the toolkit. Because you aren't starting anything else that requires these brackets.
Also you never ended you while loop. I'll post the edited code. Or at least some edited code. No guarantee it'll work either.

### Levi · 2004-12-09 13:50 · #B136963

**Code:**

```
{ * I don't see a use for this bracket but I also don't see all of the code before this post

#fontsize(25)

#ClearButtons()

#bitmap("statsbkg.bmp")

#text(5,2,"Which Characters stats do you want to view?")

#text(5,3,"1 - <playerhandle[0]$>")

#text(5,4,"2 - <playerhandle[1]$>")

#text(5,5,"3 - <playerhandle[2]$>")

#text(5,6,"4 - <playerhandle[3]$>")

#text(5,7,"5 - <playerhandle[4]$>")

#wait(a!)

#clear()

#done!==0

#while(done!==0)

{  *start while brackets here

   #if(a!==1)

   {   * start if brackets

   #GetHP(playerhandle[0]$,HP!)

   #GetMaxHP(playerhandle[0]$,MaxHP!)

   #GetFP(playerhandle[0]$,fp!)

   #GetSMP(playerhandle[0]$,mp!)

   #GetMaxSMP(playerhandle[0]$,maxmp!)

   #GetLevel(playerhandle[0]$,level!)

   #GetDP(playerhandle[0]$,dp!)

   #SetImage( "mainchar.jpg", 8, 8, 100, 64, 64)

   #text(5,5,"<HP!> HP / <MaxHP!> HP")

   #text(5,6,"<mp!> SMP / <maxmp!> MP")

   #text(5,3,"<playerhandle[0]$>, Is level <level!>")

   #text(5,7,"Has <fp!> Fighting Ability")

   #text(5,8,"Has <dp!> Defencive Ability")

   #text(5,9,"Has <playerhandle[0]$[experience]!> Experience")

   #wait()

   #kill(a!)

   #kill(HP!)

   #kill(MaxHP!)

   #kill(mp!)

   #kill(maxmp!)

   #kill(level!)

   #kill(fp!)

   #kill(dp!)

   #done!==1

   #run("Menu.prg")

   }  * end if brackets

  * you had a { here.  No purpose, useless.

   #if(a!==2)

   {  *start if brackets

   #GetHP(playerhandle[1]$,HP!)

   #GetMaxHP(playerhandle[1]$,MaxHP!)

   #GetFP(playerhandle[1]$,fp!)

   #GetSMP(playerhandle[1]$,mp!)

   #GetMaxSMP(playerhandle[1]$,maxmp!)

   #GetLevel(playerhandle[1]$,level!)

   #GetDP(playerhandle[1]$,dp!)

   #SetImage( "mainchar.jpg", 8, 8, 100, 64, 64)

   #text(5,5,"<HP!> HP / <MaxHP!> HP")

   #text(5,6,"<mp!> SMP / <maxmp!> MP")

   #text(5,3,"<playerhandle[1]$>, Is level <level!>")

   #text(5,7,"Has <fp!> Fighting Ability")

   #text(5,8,"Has <dp!> Defencive Ability")

   #text(5,9,"Has <playerhandle[1]$[experience]!> Experience")

   #wait()

   #kill(a!)

   #kill(HP!)

   #kill(MaxHP!)

   #kill(mp!)

   #kill(maxmp!)

   #kill(level!)

   #kill(fp!)

   #kill(dp!)

   #done!==1

   #run("Menu.prg")

   }  * end if brackets.

  *Again with this bracket...{

#if(a!==3)

   {  * If brackets

   #GetHP(playerhandle[2]$,HP!)

   #GetMaxHP(playerhandle[2]$,MaxHP!)

   #GetFP(playerhandle[2]$,fp!)

   #GetSMP(playerhandle[2]$,mp!)

   #GetMaxSMP(playerhandle[2]$,maxmp!)

   #GetLevel(playerhandle[2]$,level!)

   #GetDP(playerhandle[2]$,dp!)

   #SetImage( "mainchar.jpg", 8, 8, 100, 64, 64)

   #text(5,5,"<HP!> HP / <MaxHP!> HP")

   #text(5,6,"<mp!> SMP / <maxmp!> MP")

   #text(5,3,"<playerhandle[2]$>, Is level <level!>")

   #text(5,7,"Has <fp!> Fighting Ability")

   #text(5,8,"Has <dp!> Defencive Ability")

   #text(5,9,"Has <playerhandle[2]$[experience]!> Experience")

   #wait()

   #kill(a!)

   #kill(HP!)

   #kill(MaxHP!)

   #kill(mp!)

   #kill(maxmp!)

   #kill(level!)

   #kill(fp!)

   #kill(dp!)

   #done!==1

   #run("Menu.prg")

   }  *end if brackets

  *This is still pointless {

   #if(a!==4)

   { *start if brackets

   #GetHP(playerhandle[3]$,HP!)

   #GetMaxHP(playerhandle[3]$,MaxHP!)

   #GetFP(playerhandle[3]$,fp!)

   #GetSMP(playerhandle[3]$,mp!)

   #GetMaxSMP(playerhandle[3]$,maxmp!)

   #GetLevel(playerhandle[3]$,level!)

   #GetDP(playerhandle[3]$,dp!)

   #SetImage( "mainchar.jpg", 8, 8, 100, 64, 64)

   #text(5,5,"<HP!> HP / <MaxHP!> HP")

   #text(5,6,"<mp!> SMP / <maxmp!> MP")

   #text(5,3,"<playerhandle[3]$>, Is level <level!>")

   #text(5,7,"Has <fp!> Fighting Ability")

   #text(5,8,"Has <dp!> Defencive Ability")

   #text(5,9,"Has <playerhandle[3]$[experience]!> Experience")

   #wait()

   #kill(a!)

   #kill(HP!)

   #kill(MaxHP!)

   #kill(mp!)

   #kill(maxmp!)

   #kill(level!)

   #kill(fp!)

   #kill(dp!)

   #done!==1

   #run("Menu.prg")

   } * end if brackets

 * here we go again {

   #if(a!==5)

   {  * start if brackets

   #GetHP(playerhandle[4]$,HP!)

   #GetMaxHP(playerhandle[4]$,MaxHP!)

   #GetFP(playerhandle[4]$,fp!)

   #GetSMP(playerhandle[4]$,mp!)

   #GetMaxSMP(playerhandle[4]$,maxmp!)

   #GetLevel(playerhandle[4]$,level!)

   #GetDP(playerhandle[4]$,dp!)

   #SetImage( "mainchar.jpg", 8, 8, 100, 64, 64)

   #text(5,5,"<HP!> HP / <MaxHP!> HP")

   #text(5,6,"<mp!> SMP / <maxmp!> MP")

   #text(5,3,"<playerhandle[4]$>, Is level <level!>")

   #text(5,7,"Has <fp!> Fighting Ability")

   #text(5,8,"Has <dp!> Defencive Ability")

   #text(5,9,"Has <playerhandle[4]$[experience]!> Experience")

   #wait()

   #kill(a!)

   #kill(HP!)

   #kill(MaxHP!)

   #kill(mp!)

   #kill(maxmp!)

   #kill(level!)

   #kill(fp!)

   #kill(dp!)

   #done!==1

   #run("Menu.prg")

   } *end if brackets

}  *end while loop.  You didn't have this originally.
```
