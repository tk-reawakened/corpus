---
kind: forum-thread
id: "toolkitzone-forums/7184"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "7184"
title: "Menu screws everthing up"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=7184"
written: "2004-08-14T23:47:00"
last_post: "2004-08-16T12:59:00"
date_confidence: "exact"
captured: ["20040925161828"]
author: "Z"
repliers: ["DEXTER", "oblivious_casualty", "stanleywuu"]
authors: ["Z", "DEXTER", "oblivious_casualty", "stanleywuu"]
posts_present: 8
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_76483_amp_", captured: "20040925161828", sha256: "6cc40b0789c340c671d7c189af33e68046394d8e5bceead4bb133dbf7c761e40", wayback_url: "https://web.archive.org/web/20040925161828/http://www.toolkitzone.com/forums/viewtopic.php?p=76483&amp="}
links:
  - {url: "http://img12.imageshack.us/img12/6572/banner1-1.gif", status: "external", local: null}
  - {url: "http://img54.exs.cx/img54/4108/IDSbanner.jpg", status: "external", local: null}
  - {url: "http://thanian-nation.com/expo/images/expo_story.gif", status: "external", local: null}
  - {url: "http://www.galacforums.com/Z_Forum/", status: "external", local: null}
  - {url: "http://www.grind.bravehost.com", status: "external", local: null}
  - {url: "http://www.toolkitzone.com/stuff/files/3094/Animation1.gif", status: "never-captured", local: null}
  - {url: "http://www.toolkitzone.com/stuff/files/3094/Lod.jpg", status: "never-captured", local: null}
  - {url: "http://www.toolkitzone.com/stuff/files/3094/Zstudioswmoto.JPG", status: "never-captured", local: null}
---

# Menu screws everthing up

### Z · 2004-08-14 23:47 · #B75537

I have a custoom menu system, I put it in the runtime Program Slot (Main file>RPGCode) and now when i start the game it comes to the title screen then when you pick an option, then press enter, the game doesn't start and the screen turns white. How do i fix this, I am using TK 3.0.2
_________________
![](http://www.toolkitzone.com/stuff/files/3094/Lod.jpg)
![](http://www.toolkitzone.com/stuff/files/3094/Zstudioswmoto.JPG)
My Forums are getting dull so click [Here](http://www.galacforums.com/Z_Forum/)
Ok check out this dude's game idea by going to [www.grind.bravehost.com](http://www.grind.bravehost.com)
![](http://www.toolkitzone.com/stuff/files/3094/Animation1.gif)

### DEXTER · 2004-08-15 00:27 · #B75558

Maybe your code is all wrong or maybe is because you use #RPGcode()
_________________
What if i am 11 years old?
Watch the moon every night you can... for me...the night will just not arrive.
-DEXTER

### oblivious_casualty · 2004-08-15 00:36 · #B75567

he didnt use #rpgcode(), and besides, that command works fine. he put the program in the rpgcode tab in the main file editor. he said nothing about any commands.
_________________
...............![](http://thanian-nation.com/expo/images/expo_story.gif)...............
![](http://img12.imageshack.us/img12/6572/banner1-1.gif)
![](http://img54.exs.cx/img54/4108/IDSbanner.jpg)

### DEXTER · 2004-08-15 00:39 · #B75570

that command doesn't works fine at all man well at least in the binary version
_________________
What if i am 11 years old?
Watch the moon every night you can... for me...the night will just not arrive.
-DEXTER

### Z · 2004-08-15 00:45 · #B75579

heres the code just in case its that.

**Code:**

```
#Bitmap("Background.bmp")

#xtop!=450

#width!=150

#height!=50

#setbutton("Stats.JPG", 0, xtop!, 10, width!, height!")

#setbutton("Abilities.JPG", 1, xtop!, 65, width!, height!)

#setbutton("equipment.JPG", 2, xtop!, 120, width!, Height!)

#setbutton("items.JPG", 3, xtop!, 175, width!, height!)

#setbutton("cheats.JPG", 4, Xtop!, 230, width!, height!)

#setbutton("load.BMP",4, xtop!, 285, width!, height!)

#setbutton("save.BMP", 5, xtop!, 340, width!, height!)

#setbutton("continue.JPG", 6, xtop!, 340, width!, height!)

#setbutton("quit.BMP", 7, xtop!, 395, width!, height!)

#GetHP(playerHandle[0]$,Hp!)

#GetMaxHp(playerHandle[0]$,MaxHp!)

#GetSMP(playerHandle[0]$,SMP!)

#GetMaxSMP(playerHandle[0]$,MaxSMP!)

#Text(11,1.5,"Name: <playerHandle[0]$>")

#Text(11,2.5,"HP:<MaxHP!>/<Hp!>")

#Text(11,3.5,"SMP:<MaxSMP!>/<SMP!>")

#GetHP(playerHandle[1]$,Hp1!)

#GetMaxHp(playerHandle[1]$,MaxHp1!)

#GetSMP(playerHandle[1]$,SMP1!)

#GetMaxSMP(playerHandle[1]$,MaxSMP1!)

#Text(11,7.5,"Name: <playerHandle[1]$>")

#Text(11,8.5,"HP:<MaxHP1!>/<HP1!>")

#Text(11,9.5,"SP:<MaxSMP1!>/<SMP1!>")

#setimage("profile1.gif",10,10,100,100)

#setimage("profile2.gif",10,110,100,100)

#setimage("profile3.gif",10,220,100,100)

#setimage("profile4.gif",10,330,100,100)

#GetHP(playerHandle[2]$,Hp2!)

#GetMaxHp(playerHandle[2]$,MaxHp2!)

#GetSMP(playerHandle[2]$,SMP2!)

#GetMaxSMP(playerHandle[2]$,MaxSMP2!)

#Text(11,12.5,"Name: <playerHandle[2]$>")

#Text(11,13.5,"HP:<MaxHP2!>/<HP2!>")

#Text(11,14.5,"SP:<MaxSMP2!>/<SMP2!>")

:top

#done!=0

#while(done!==0)

{

#MouseClick(x!,y!)

#CheckButton(x!,y!,button!)

#if (button!==0)

{

#internalmenu(3)

}

#if (button!==4)

{

#dirsav(dest$)

#if(dest$~="CANCEL")

        {

     #load(dest$)

        #done!=1

        #end

        }

}

#if (button!==5)

{

#dirsav(dest$)

#if(dest$~="CANCEL")

        {

     #save(dest$)

        #done!=1

        #end

        }

}

#if (button!==6)

{

#clearbuttons()

#done!=1

}

#if (button!==7)

{

#mwin("Do you really want to quit? Don't forget to save!")

#delay(0.5)

@

#mwin("1 - Yes")

#mwin("2 - No")

#wait(answer!)

#if (answer!==1)

   {

   #windows()

   }

#if (answer!==2)

   {

#mwincls()

#branch(:top)

   }

}

}
```

_________________
![](http://www.toolkitzone.com/stuff/files/3094/Lod.jpg)
![](http://www.toolkitzone.com/stuff/files/3094/Zstudioswmoto.JPG)
My Forums are getting dull so click [Here](http://www.galacforums.com/Z_Forum/)
Ok check out this dude's game idea by going to [www.grind.bravehost.com](http://www.grind.bravehost.com)
![](http://www.toolkitzone.com/stuff/files/3094/Animation1.gif)

### Z · 2004-08-15 19:28 · #B76018

Plese some one help
_________________
![](http://www.toolkitzone.com/stuff/files/3094/Lod.jpg)
![](http://www.toolkitzone.com/stuff/files/3094/Zstudioswmoto.JPG)
My Forums are getting dull so click [Here](http://www.galacforums.com/Z_Forum/)
Ok check out this dude's game idea by going to [www.grind.bravehost.com](http://www.grind.bravehost.com)
![](http://www.toolkitzone.com/stuff/files/3094/Animation1.gif)

### stanleywuu · 2004-08-15 20:09 · #B76043

change your run time key to space or something
_________________
There is no death, there is force

### Z · 2004-08-16 12:59 · #B76483

I tried that it still doesn't work
_________________
![](http://www.toolkitzone.com/stuff/files/3094/Lod.jpg)
![](http://www.toolkitzone.com/stuff/files/3094/Zstudioswmoto.JPG)
My Forums are getting dull so click [Here](http://www.galacforums.com/Z_Forum/)
Ok check out this dude's game idea by going to [www.grind.bravehost.com](http://www.grind.bravehost.com)
![](http://www.toolkitzone.com/stuff/files/3094/Animation1.gif)
