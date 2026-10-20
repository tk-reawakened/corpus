---
kind: forum-thread
id: "toolkitzone-forums/6876"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "advanced rpg code"
skin: "phpbb2"
thread_id: "6876"
title: "Seriously need help here!"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=6876"
written: "2004-08-08T04:05:00"
last_post: "2004-08-18T20:04:00"
date_confidence: "exact"
captured: ["20040912085333"]
author: "Sparda"
repliers: ["KSNiloc", "Unyis", "Dont_Think_So", "Marc", "rdemusx", "Mark_of_the_Dragon"]
authors: ["Sparda", "KSNiloc", "Unyis", "Dont_Think_So", "Marc", "rdemusx", "Mark_of_the_Dragon"]
posts_present: 9
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_75470_amp_", captured: "20040912085333", sha256: "b1aefe84a46fee559f081b2258d915bd21e9ef6085445c1068901385f7249055", wayback_url: "https://web.archive.org/web/20040912085333/http://www.toolkitzone.com/forums/viewtopic.php?p=75470&amp="}
links:
  - {url: "http://img.photobucket.com/albums/v293/rdemusx/MOTM/newadbar.gif", status: "external", local: null}
  - {url: "http://img.photobucket.com/albums/v293/rdemusx/newvid.gif", status: "external", local: null}
  - {url: "http://img48.exs.cx/img48/4020/Nomore.gif", status: "external", local: null}
  - {url: "http://img76.exs.cx/img76/421/Muahahahaha.jpg", status: "external", local: null}
  - {url: "http://img85.exs.cx/img85/3596/Niloc.gif", status: "external", local: null}
  - {url: "http://mansionsofthemoon.myfreebb.com/index.php", status: "external", local: null}
  - {url: "http://mansionsofthemoon.tripod.com", status: "external", local: null}
  - {url: "http://vidoentertainment.com", status: "external", local: null}
---

# Seriously need help here!

### Sparda · 2004-08-08 04:05 · #B71559

Ok, so i've posted this thread in the help forum and have gotten no help.
so i decided to post it here, heres the story: so i want a custom title screen, only i dont know much about RPGcode so i would like to ask you guys if there is anyway that you could post up a program about the #fade command. And i dont mean the built in command, i mean a method to make the screen really fade slowly because the normal fade# command
just blacks out the screen, not fade it. Any help would be appreciated. Thank you.

### KSNiloc · 2004-08-08 04:15 · #B71560

You could send to a board that has your title screen as the background image and then adjust the ambientlight variables.
_________________
Fighting for the greater good.

### Unyis · 2004-08-14 05:57 · #B75139

you could try writing a fading method. For example:

**Code:**

```
#method fade2(spd!)

{

#block1!=1

#block2!=352

#while(block1!<176)

{

#fillrect(1,1,608,block1!)

#fillrect(1,352,608,block2!)

#block1!=block1!+spd!

#block2!=block2!-spd!

}

}
```

This method makes two rectangles gradually increase from opposite ends of the screen to the middle. It's a cool effect that creates an illusion of the screen closing.
_________________
~Chris Rose

### Dont_Think_So · 2004-08-14 06:47 · #B75164

...Or use #setimageadditive and use a white square... I'm pretty sure you can set negative values. That would allow you to fade the screen.
_________________
"I have succeded in all but one thing - failure" -Dont_Think_So
"Once upon a midnight dreary, while I websurfed, weak and weary,
...Over many a strange and spurious website of 'hot chicks galore',
...While I clicked my fav'rite bookmark, suddenly there came a warning,
...And my heart was filled with mourning, mourning for my dear amour.
..."'Tis not possible," I muttered, "give me back my cheap hardcore!" -
Quoth the server, "404"."

### Marc · 2004-08-14 14:35 · #B75253

I forgot the command, it might be setimageadditive or setimagetranslucent that has a "opacacy [sp?]" setting and coupled with a while loop you could increese it or decreese it to make it look cool Razz.
_________________
![](http://img85.exs.cx/img85/3596/Niloc.gif)![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)
![](http://img48.exs.cx/img48/4020/Nomore.gif)
When I get a chance after my mounds of homework, I will resize and stuff to the none and one animated banners. Making them as small as I can.

### rdemusx · 2004-08-14 15:21 · #B75280

Cursor Title Screen

**Code:**

```
***************************************

*This is a cursor title screen menu   *

*for newbies. I will also walk you step*

*by step to making it work.************

****************************

*************************************************

*You have to make images and save them as .gif's*

*Then make sure those images are saved into your*

*bitmap folder in the TK directory. Make sure you*

*write all of the images heights & widths*********

*Next type in all the width's and height's of  *

*the images. Also make an image for the title ***

*bkg. Enter all the flienames in the spaces below*

*next you will want to find out where these      *

*images will be placed on the screen. That is the*

*x!,y!,coordinates of each image. You will not  **

*change anything in this program but what I show*

*you.********************************************

******

*************************************************************************

***this is the stuff you will enter here. Anywhere you see " .gif" place*

***an image there. DO NOT CHANGE ANYTHING IN FRONT OF THE EQUAL SIGN!!!**

*************************************************************************

***************************************************************************

*just put #Include("titlecursor.prg") in your start program. You might have*

*to customize your start program for this to work.*************************

***************************************************

*************************************************************************

*just copy and paste this into a new program. Make sure you save the new*

*program as titleclick.prg.**********************************************

*****************************************

*call the method with #cursortitlemenu()*

*****************************************

#method cursortitlemenu()

{

#ya[1]! =

#ya[2]! =

#ya[3]! =

*y! coordinates of the selection icon*

#xa[1]! =

#xa[2]! =

#xa[3]! =

*x! coordinates of selection icon*

#selectionwidth! =

#selectionheght! =

#transred! =

#transgreen! =

#transblue! =

#selectpic$ = " .gif"

#titlepic$ = " .gif"

****DO NOT CHANGE ANYTHING BEYOND THIS POINT!!!!*****************

#setimage(titlepic$,0,0,titlewidth!,titleheight!)

#savescreen()

#select! = 1

#done! = 0

#while(done! == 0)

      {

      #restorescreen()

      #setimagetransparent(selectpic$,xa[select!]!,ya[select!]!,selectionwidth!,selectionheght!,transred!,transgreen!,#transblue!)

      #wait(a$)

      #if(a$ == "UP")

         {

         #if(select! > 1)

            {

            #select! = select! - 1

            }

         }

     #if(a$ == "DOWN")

        {

        #if(select! < 3)

           {

           #select! = select! + 1

           }

        }

    #if(a$ == "ENTER")

       {

       *NEW GAME SELECTED*

       #if(select! == 1)

          {

          #done! = 1

          }

       #if(select! == 2)

          {

          *LOAD GAME SELECTED*

          #dirsav(dest$)

          #if(dest$~="CANCEL")

             {

             #load(dest$)

             #done!=1

             #end

             }

          }

       #if(select! == 3)

          {

          *EXIT SELECTED*

          #dos()

          }

       #if(select! == 4)

          {

          #setimage("orderscreen.gif",0,0,640,480)

          #wait(a$)

          #done! = 0

          }

}

}
```

Mouse Driven Title Screen

**Code:**

```
***************************************

*This is a clickable title screen menu*

*for newbies. I will also alk you step*

*by step to making it work.************

****************************

*************************************************

*You have to make images and save them as .gif's*

*Then make sure those images are saved into your*

*bitmap folder in the TK directory. Make sure you*

*write all three of the images heights & widths***

*Next type in all the width's and height's of  *

*the buttons. Also make an image for the title ***

*bkg. Enter all the flienames in the spaces below*

*next you will want to find out where these      *

*images will be placed on the screen. That is the*

*x!,y!,coordinates of each image. You will not  **

*change anything in this program but what I show*

*you.********************************************

******

*************************************************************************

***this is the stuff you will enter here. Anywhere you see " .gif" place*

***an image there. DO NOT CHANGE ANYTHING IN FRONT OF THE EQUAL SIGN!!!**

*************************************************************************

***************************************************************************

*just put #Include("titleclick.prg") in your start program. You might have*

*to customize your start program for this to work.*************************

***************************************************

*************************************************************************

*just copy and paste this into a new program. Make sure you save the new*

*program as titleclick.prg.**********************************************

****************************

#method titleclick()

{

#titlepic$ = " .gif"

*sets title pic file name*

#titlewidth! = 640

*sets width of title screen*

#titleheight! = 480

*sets height of title screen*

#buttonpic1$ = " .gif"

*sets button 1 pic*

#buttonpic2$ = " .gif"

*sets button 2 pic*

#buttonpic3$ = " .gif"

*sets button 3 pic*

#butx1! =

*sets x!(horizontal coordinate) of button 1*

#buty1! =

*sets y!(vertical coordinate) of button 1*

#butx2! =

*sets x!(horizontal coordinate) of button 2*

#buty2! =

*sets y!(vertical coordinate) of button 1*

#butx3! =

*sets x!(horizontal coordinate) of button 3*

#buty3! =

*sets y!(vertical coordinate) of button 1*

#butwidth1! =

*sets width of button 1 pic*

#butwidth2! =

*sets width of button 2 pic*

#butwidth3! =

*sets width of button 3 pic*

#butheight1! =

*sets height of button 1 pic*

#butheight2! =

*sets height of button 2 pic*

#butheight3! =

*sets height of button 3 pic*

#done! = 1

#while(done! = 1)

      {

      #setimage(titlepic$,0,0,titlewidth!,titleheight!)

      #setbutton(buttonpic1$,0,butx1!,buty1!,butwidth1!,butheight1!)

      #setbutton(buttonpic2$,1,butx2!,buty2!,butwidth2!,butheight2!)

      #setbutton(buttonpic3$,2,butx3!,buty3!,butwidth3!,butheight3!)

      #mouseclick(x!,y!)

      #checkbutton(x!,y!,button!)

      #if(button! ~= 0)

         {

         #if(button! ~= 1)

            {

            #if(button! ~= 2)

               {

               #done! = 1

               }

            }

         }

      #if(button! == 0)

         {

         #done! = 2

         }

      #if(button! == 1)

         {

         #dirsav(dest$)

         #if(dest$~="CANCEL")

            {

            #load(dest$)

            #done!=1

            #end

            }

         }

      #if(button! == 2)

         {

         #dos()

         }

      }

}

**********************************************************

*then also in your start program just type #titleclick() *

*where you want your title menu to be ran. If you need   *

*help with this program just post on my forum and I will *

*be gald to help. I will also be making a cursor menu for*

*newbies in the near future. Then menu system clickable  ****

*and menu system cursor. Then finally a clickable and cursor*

*battle system. I am just trying to help people learn and****

*help themselves.       **********************************

*Thanx RDX aka. R.DemusX**********************************

*VISIT: http://mansionsofthemoon.tripod.com and click the*

*forums link to post any problems or questions************

**********************************************************
```

_________________
![](http://img.photobucket.com/albums/v293/rdemusx/MOTM/newadbar.gif)
![](http://img.photobucket.com/albums/v293/rdemusx/newvid.gif)
VISIT WEBSITE: <http://mansionsofthemoon.tripod.com>
VISIT FORUMS: <http://mansionsofthemoon.myfreebb.com/index.php>
VISIT Vi D.O. ENT: <http://vidoentertainment.com>

### Marc · 2004-08-14 19:20 · #B75358

Mad you forgot your killing spree!
#kill(variablesthatdonotneedtogobeyondtheprogram!)
_________________
![](http://img85.exs.cx/img85/3596/Niloc.gif)![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)
![](http://img48.exs.cx/img48/4020/Nomore.gif)
When I get a chance after my mounds of homework, I will resize and stuff to the none and one animated banners. Making them as small as I can.

### rdemusx · 2004-08-14 21:43 · #B75470

Heh yeah make sure you kill everything. That would've been nice to do ... heh!
RDX
_________________
![](http://img.photobucket.com/albums/v293/rdemusx/MOTM/newadbar.gif)
![](http://img.photobucket.com/albums/v293/rdemusx/newvid.gif)
VISIT WEBSITE: <http://mansionsofthemoon.tripod.com>
VISIT FORUMS: <http://mansionsofthemoon.myfreebb.com/index.php>
VISIT Vi D.O. ENT: <http://vidoentertainment.com>

### Mark_of_the_Dragon · 2004-08-18 20:04 · #B77878

Dude, study the default start program. CBM was nice enough to comment it so that it would be easier to understand. Also, since you're not comfortable with RPGCode, read the help files.
_________________
Never meddle in the affairs of dragons for you are crunchy and taste good with ketchup...
Message to you all: Read the help files before you ask questions; most questions can be answered. Also, make a game using default systems first; that will put you in a better position to make everythign on your own. You think xorlak relied on MrG for everything? No.
