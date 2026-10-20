---
kind: forum-thread
id: "toolkitzone-forums/22233"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Advanced Coding"
skin: "phpbb2"
thread_id: "22233"
title: "Custom menu problem! need help!"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=22233"
written: "2005-08-08T16:29:00"
last_post: "2005-08-08T20:59:00"
date_confidence: "exact"
captured: ["20051103224607"]
author: "~Shadow~"
repliers: ["Noob From The Grave", "Z"]
authors: ["~Shadow~", "Noob From The Grave", "Z"]
posts_present: 4
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_243014_amp_3Bsid_7cde889a94523dc3911efb6795047320", captured: "20051103224607", sha256: "f760e9435d4f3b826cb1195a225270b95b1285f83d36af0f1269cb13d724c0d2", wayback_url: "https://web.archive.org/web/20051103224607/http://www.toolkitzone.com/forums/viewtopic.php?p=243014&amp%3Bsid=7cde889a94523dc3911efb6795047320"}
links: []
---

# Custom menu problem! need help!

### ~Shadow~ · 2005-08-08 16:29 · #B242932

ok, i made a custom menu for my game but whenever i click on a button the deubgger comes up saying this:

**Code:**

```
Error: Details menu is obsolete!-- internalmenu(3)

Error: Details menu is obsolete!-- internalmenu(3)

Error: Details menu is obsolete!-- internalmenu(3)

Error: Details menu is obsolete!-- internalmenu(3)
```

and so on.
Can anyone tell me wots wrong?
heres my code:

**Code:**

```
*Menu Build Generated Code

#Bitmap("background.jpg")

#SetButton("Status.jpg",0,476,10,125,30)

#SetButton("Equip.jpg",1,476,43,125,30)

#SetButton("items.jpg",2,476,75,125,30)

#setbutton("abilities.jpg",3,476,107,125,30)

#setbutton("Load.jpg", 4, 476, 141, 125, 30)

#setbutton("Save.jpg",5,476,173,125,30)

#setbutton("resume.jpg",6,476,209,125,30)

#setbutton("quit.jpg",7,476,312,125,30)

#getrealtime()

#getGP(Gp!)

#text(49,25,"Game Time:")

#text(49,26,"<hour!>:<min!>")

#text(49,28,"Gold Pieces:")

#text(49,30,"<Gp!>")

#gethp(playerhandle[0]$,onehp!)

#getmaxhp(playerhandle[0]$,onemaxhp!)

#getfp(playerhandle[0]$,onefp!)

#getsmp(playerhandle[0]$,onemp!)

#getmaxsmp(playerhandle[0]$,onemaxmp!)

#getlevel(playerhandle[0]$,onelevel!)

#getdp(playerhandle[0]$,onedp!)

#text(3,3,"<playerhandle[0]$>   Level: <onelevel!>")

#text(3,4,"<onehp!>HP/<onemaxhp!>HP")

#text(3,5,"<onemp!>MP/<onemaxmp!>MP")

#text(3,6,"<onefp!>FP and <onedp!>DP")

#If(playerHandle[1]$~= "")

{

#gethp(playerhandle[1]$,twohp!)

#getmaxhp(playerhandle[1]$,twomaxhp!)

#getfp(playerhandle[1]$,twofp!)

#getsmp(playerhandle[1]$,twomp!)

#getmaxsmp(playerhandle[1]$,twomaxmp!)

#getlevel(playerhandle[1]$,twolevel!)

#getdp(playerhandle[1]$,twodp!)

#text(3,8,"<playerhandle[1]$>   Level: <twolevel!>")

#text(3,9,"<twohp!>HP/<twomaxhp!>HP")

#text(3,10,"<twomp!>MP/<twomaxmp!>MP")

#text(3,11,"<twofp!>FP and <twodp!>DP")

}

#If (playerHandle[2]$~= "")

{

#gethp(playerhandle[2]$,threehp!)

#getmaxhp(playerhandle[2]$,threemaxhp!)

#getfp(playerhandle[2]$,threefp!)

#getsmp(playerhandle[2]$,threemp!)

#getmaxsmp(playerhandle[2]$,threemaxmp!)

#getlevel(playerhandle[2]$,threelevel!)

#getdp(playerhandle[2]$,threedp!)

#text(3,13,"<playerhandle[2]$>   Level: <threelevel!>")

#text(3,14,"<threehp!>HP/<threemaxhp!>HP")

#text(3,15,"<threemp!>MP/<threemaxmp!>MP")

#text(3,16,"<threefp!>FP and <threedp!>DP")

}

#If (playerHandle[3]$~= "")

{

#gethp(playerhandle[3]$,fourhp!)

#getmaxhp(playerhandle[3]$,fourmaxhp!)

#getfp(playerhandle[3]$,fourfp!)

#getsmp(playerhandle[3]$,fourmp!)

#getmaxsmp(playerhandle[3]$,fourmaxmp!)

#getlevel(playerhandle[3]$,fourlevel!)

#getdp(playerhandle[3]$,fourdp!)

#text(3,18,"<playerhandle[3]$>   Level: <fourlevel!>")

#text(3,19,"<fourhp!>HP/<fourmaxhp!>HP")

#text(3,20,"<fourmp!>MP/<fourmaxmp!>MP")

#text(3,21,"<fourfp!>FP and <fourdp!>DP")

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

#text(3,23,"<playerhandle[4]$>   Level: <fivelevel!>")

#text(3,24,"<fivehp!>HP/<fivemaxhp!>HP")

#text(3,25,"<fivemp!>MP/<fivemaxmp!>MP")

#text(3,26,"<fivefp!>FP and <fivedp!>DP")

}

#done!==0

#while(done!==0)

{

#mouseclick(x!,y!)

#checkbutton(x!,y!,button!)

#if(button!==0)

{

#internalmenu(3)

}

#if(button!==1)

{

#internalmenu(2)

}

#if(button!==2)

{

#internalmenu(1)

}

#if(button!==3)

{

#internalmenu(4)

}

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

#if(button!==5)

{

*'save game' clicked

#dirsav(dest$)

#if(dest$~="CANCEL")

{

#save(dest$)

#done!=1

#end

}

}

#If(button!==6)

{

#textspeed(2)

#fontsize(size!)

#ClearButtons()

#clear()

#forceredraw()

#done!=1

#end()

}

#if(button!==7)

{

#dos()

}

#Method getrealtime()

{

#ourmin!=GameTime!

#CastInt(ourmin!,ourmin2!)

#our2!=ourmin2!/3600

#min2!=ourmin2!/60

#CastInt(hour2!,hour!)

#CastInt(min2!,min!)

:mintoour

:time

#If(our!>23)

{

#our!=our!-24

#Fbranch(:time)

}

#If(min!>59)

{

#min!=min!-60

#Fbranch(:mintoour)

}

}

*End of MenuBUILD Generated Code
```

thanx if anyone can help!

### Noob From The Grave · 2005-08-08 19:00 · #B242977

**Code:**

```
Menu Build Generated Code

#Bitmap("background.jpg")

#SetButton("Status.jpg",0,476,10,125,30)

#SetButton("Equip.jpg",1,476,43,125,30)

#SetButton("items.jpg",2,476,75,125,30)

#setbutton("abilities.jpg",3,476,107,125,30)

#setbutton("Load.jpg", 4, 476, 141, 125, 30)

#setbutton("Save.jpg",5,476,173,125,30)

#setbutton("resume.jpg",6,476,209,125,30)

#setbutton("quit.jpg",7,476,312,125,30)

#getrealtime()

#getGP(Gp!)

#text(49,25,"Game Time:")

#text(49,26,"<hour!>:<min!>")

#text(49,28,"Gold Pieces:")

#text(49,30,"<Gp!>")

#gethp(playerhandle[0]$,onehp!)

#getmaxhp(playerhandle[0]$,onemaxhp!)

#getfp(playerhandle[0]$,onefp!)

#getsmp(playerhandle[0]$,onemp!)

#getmaxsmp(playerhandle[0]$,onemaxmp!)

#getlevel(playerhandle[0]$,onelevel!)

#getdp(playerhandle[0]$,onedp!)

#text(3,3,"<playerhandle[0]$>   Level: <onelevel!>")

#text(3,4,"<onehp!>HP/<onemaxhp!>HP")

#text(3,5,"<onemp!>MP/<onemaxmp!>MP")

#text(3,6,"<onefp!>FP and <onedp!>DP")

#If(playerHandle[1]$~= "")

{

   #gethp(playerhandle[1]$,twohp!)

   #getmaxhp(playerhandle[1]$,twomaxhp!)

   #getfp(playerhandle[1]$,twofp!)

   #getsmp(playerhandle[1]$,twomp!)

   #getmaxsmp(playerhandle[1]$,twomaxmp!)

   #getlevel(playerhandle[1]$,twolevel!)

   #getdp(playerhandle[1]$,twodp!)

   #text(3,8,"<playerhandle[1]$>   Level: <twolevel!>")

   #text(3,9,"<twohp!>HP/<twomaxhp!>HP")

   #text(3,10,"<twomp!>MP/<twomaxmp!>MP")

   #text(3,11,"<twofp!>FP and <twodp!>DP")

}

#If (playerHandle[2]$~= "")

{

   #gethp(playerhandle[2]$,threehp!)

   #getmaxhp(playerhandle[2]$,threemaxhp!)

   #getfp(playerhandle[2]$,threefp!)

   #getsmp(playerhandle[2]$,threemp!)

   #getmaxsmp(playerhandle[2]$,threemaxmp!)

   #getlevel(playerhandle[2]$,threelevel!)

   #getdp(playerhandle[2]$,threedp!)

   #text(3,13,"<playerhandle[2]$>   Level: <threelevel!>")

   #text(3,14,"<threehp!>HP/<threemaxhp!>HP")

   #text(3,15,"<threemp!>MP/<threemaxmp!>MP")

   #text(3,16,"<threefp!>FP and <threedp!>DP")

}

#If (playerHandle[3]$~= "")

{

   #gethp(playerhandle[3]$,fourhp!)

   #getmaxhp(playerhandle[3]$,fourmaxhp!)

   #getfp(playerhandle[3]$,fourfp!)

   #getsmp(playerhandle[3]$,fourmp!)

   #getmaxsmp(playerhandle[3]$,fourmaxmp!)

   #getlevel(playerhandle[3]$,fourlevel!)

   #getdp(playerhandle[3]$,fourdp!)

   #text(3,18,"<playerhandle[3]$>   Level: <fourlevel!>")

   #text(3,19,"<fourhp!>HP/<fourmaxhp!>HP")

   #text(3,20,"<fourmp!>MP/<fourmaxmp!>MP")

   #text(3,21,"<fourfp!>FP and <fourdp!>DP")

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

   #text(3,23,"<playerhandle[4]$>   Level: <fivelevel!>")

   #text(3,24,"<fivehp!>HP/<fivemaxhp!>HP")

   #text(3,25,"<fivemp!>MP/<fivemaxmp!>MP")

   #text(3,26,"<fivefp!>FP and <fivedp!>DP")

}

#done!==0

#while(done!==0)

{

   #mouseclick(x!,y!)

   #checkbutton(x!,y!,button!)

   #if(button!==0)

   {

      #internalmenu(3)

   }

   #if(button!==1)

   {

      #internalmenu(2)

   }

   #if(button!==2)

   {

      #internalmenu(1)

   }

   #if(button!==3)

   {

      #internalmenu(4)

   }

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

   #if(button!==5)

   {

      *'save game' clicked

      #dirsav(dest$)

      #if(dest$~="CANCEL")

      {

         #save(dest$)

         #done!=1

         #end

      }

   }

   #If(button!==6)

   {

      #textspeed(2)

      #fontsize(size!)

      #ClearButtons()

      #clear()

      #forceredraw()

      #done!=1

      #end()

   }

   #if(button!==7)

   {

      #dos()

   }

   #Method getrealtime()

   {

      #ourmin!=GameTime!

      #CastInt(ourmin!,ourmin2!)

      #our2!=ourmin2!/3600

      #min2!=ourmin2!/60

      #CastInt(hour2!,hour!)

      #CastInt(min2!,min!)

      :mintoour

      :time

      #If(our!>23)

      {

         #our!=our!-24

         #Fbranch(:time)

      }

      #If(min!>59)

      {

         #min!=min!-60

         #Fbranch(:mintoour)

      }

   }

   *End of MenuBUILD Generated Code
```

Didnt get any problems about the internal menu, try that.

### ~Shadow~ · 2005-08-08 20:19 · #B242999

ack!
now this comes up when i use your one!

**Code:**

```
Error: Method not found!-- Menu Build Generated Code

Error: Invalid conjunction-- == -- done! = 0 +0+0
```

### Z · 2005-08-08 20:59 · #B243014

I can fix that first error

**Code:**

```
//Menu Build Generated Code

#Bitmap("background.jpg")

#SetButton("Status.jpg",0,476,10,125,30)

#SetButton("Equip.jpg",1,476,43,125,30)

#SetButton("items.jpg",2,476,75,125,30)

#setbutton("abilities.jpg",3,476,107,125,30)

#setbutton("Load.jpg", 4, 476, 141, 125, 30)

#setbutton("Save.jpg",5,476,173,125,30)

#setbutton("resume.jpg",6,476,209,125,30)

#setbutton("quit.jpg",7,476,312,125,30)

#getrealtime()

#getGP(Gp!)

#text(49,25,"Game Time:")

#text(49,26,"<hour!>:<min!>")

#text(49,28,"Gold Pieces:")

#text(49,30,"<Gp!>")

#gethp(playerhandle[0]$,onehp!)

#getmaxhp(playerhandle[0]$,onemaxhp!)

#getfp(playerhandle[0]$,onefp!)

#getsmp(playerhandle[0]$,onemp!)

#getmaxsmp(playerhandle[0]$,onemaxmp!)

#getlevel(playerhandle[0]$,onelevel!)

#getdp(playerhandle[0]$,onedp!)

#text(3,3,"<playerhandle[0]$>   Level: <onelevel!>")

#text(3,4,"<onehp!>HP/<onemaxhp!>HP")

#text(3,5,"<onemp!>MP/<onemaxmp!>MP")

#text(3,6,"<onefp!>FP and <onedp!>DP")

#If(playerHandle[1]$~= "")

{

   #gethp(playerhandle[1]$,twohp!)

   #getmaxhp(playerhandle[1]$,twomaxhp!)

   #getfp(playerhandle[1]$,twofp!)

   #getsmp(playerhandle[1]$,twomp!)

   #getmaxsmp(playerhandle[1]$,twomaxmp!)

   #getlevel(playerhandle[1]$,twolevel!)

   #getdp(playerhandle[1]$,twodp!)

   #text(3,8,"<playerhandle[1]$>   Level: <twolevel!>")

   #text(3,9,"<twohp!>HP/<twomaxhp!>HP")

   #text(3,10,"<twomp!>MP/<twomaxmp!>MP")

   #text(3,11,"<twofp!>FP and <twodp!>DP")

}

#If (playerHandle[2]$~= "")

{

   #gethp(playerhandle[2]$,threehp!)

   #getmaxhp(playerhandle[2]$,threemaxhp!)

   #getfp(playerhandle[2]$,threefp!)

   #getsmp(playerhandle[2]$,threemp!)

   #getmaxsmp(playerhandle[2]$,threemaxmp!)

   #getlevel(playerhandle[2]$,threelevel!)

   #getdp(playerhandle[2]$,threedp!)

   #text(3,13,"<playerhandle[2]$>   Level: <threelevel!>")

   #text(3,14,"<threehp!>HP/<threemaxhp!>HP")

   #text(3,15,"<threemp!>MP/<threemaxmp!>MP")

   #text(3,16,"<threefp!>FP and <threedp!>DP")

}

#If (playerHandle[3]$~= "")

{

   #gethp(playerhandle[3]$,fourhp!)

   #getmaxhp(playerhandle[3]$,fourmaxhp!)

   #getfp(playerhandle[3]$,fourfp!)

   #getsmp(playerhandle[3]$,fourmp!)

   #getmaxsmp(playerhandle[3]$,fourmaxmp!)

   #getlevel(playerhandle[3]$,fourlevel!)

   #getdp(playerhandle[3]$,fourdp!)

   #text(3,18,"<playerhandle[3]$>   Level: <fourlevel!>")

   #text(3,19,"<fourhp!>HP/<fourmaxhp!>HP")

   #text(3,20,"<fourmp!>MP/<fourmaxmp!>MP")

   #text(3,21,"<fourfp!>FP and <fourdp!>DP")

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

   #text(3,23,"<playerhandle[4]$>   Level: <fivelevel!>")

   #text(3,24,"<fivehp!>HP/<fivemaxhp!>HP")

   #text(3,25,"<fivemp!>MP/<fivemaxmp!>MP")

   #text(3,26,"<fivefp!>FP and <fivedp!>DP")

}

#done!==0

#while(done!==0)

{

   #mouseclick(x!,y!)

   #checkbutton(x!,y!,button!)

   #if(button!==0)

   {

      #internalmenu(3)

   }

   #if(button!==1)

   {

      #internalmenu(2)

   }

   #if(button!==2)

   {

      #internalmenu(1)

   }

   #if(button!==3)

   {

      #internalmenu(4)

   }

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

   #if(button!==5)

   {

      *'save game' clicked

      #dirsav(dest$)

      #if(dest$~="CANCEL")

      {

         #save(dest$)

         #done!=1

         #end

      }

   }

   #If(button!==6)

   {

      #textspeed(2)

      #fontsize(size!)

      #ClearButtons()

      #clear()

      #forceredraw()

      #done!=1

      #end()

   }

   #if(button!==7)

   {

      #dos()

   }

   #Method getrealtime()

   {

      #ourmin!=GameTime!

      #CastInt(ourmin!,ourmin2!)

      #our2!=ourmin2!/3600

      #min2!=ourmin2!/60

      #CastInt(hour2!,hour!)

      #CastInt(min2!,min!)

      :mintoour

      :time

      #If(our!>23)

      {

         #our!=our!-24

         #Fbranch(:time)

      }

      #If(min!>59)

      {

         #min!=min!-60

         #Fbranch(:mintoour)

      }

   }

   *End of MenuBUILD Generated Code
```

but the second one puzzles me
