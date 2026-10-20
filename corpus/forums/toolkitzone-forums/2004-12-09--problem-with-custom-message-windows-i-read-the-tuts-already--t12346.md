---
kind: forum-thread
id: "toolkitzone-forums/12346"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12346"
title: "Problem with custom message windows(I read the tuts already)"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12346"
written: "2004-12-09T00:37:00"
last_post: "2004-12-09T21:35:00"
date_confidence: "exact"
captured: ["20041227215230"]
author: "stanleywuu"
repliers: ["RDemusX", "Occasionally_Correct"]
authors: ["stanleywuu", "RDemusX", "Occasionally_Correct"]
posts_present: 8
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_137091_amp_", captured: "20041227215230", sha256: "abb3a0d3e720b681f6e02a1db3a7a452c4f30962efc2135d32261e16f532fa66", wayback_url: "https://web.archive.org/web/20041227215230/http://www.toolkitzone.com/forums/viewtopic.php?p=137091&amp="}
links:
  - {url: "http://img.photobucket.com/albums/v196/Stanleywuu/error.jpg", status: "external", local: null}
---

# Problem with custom message windows(I read the tuts already)

### stanleywuu · 2004-12-09 00:37 · #B136700

![](http://img.photobucket.com/albums/v196/Stanleywuu/error.jpg)
This is what I get when I use my custom message system, I used the one on the last column, but i'm pretty sure it's not the code, though because I got these kinda problem before with setimage, but I don't know how I solved it.....
Here's my code

**rpgcode:**

```
Include("msgm.prg")

//Followed by the default codes in start.prg except I changed history() method so it's like

Method hitory()

{

*Main story

     mbox("Your", " story", " goes here..", "Is it", " a dream?abc", 1)

     Wait()

}
```

mbox method is in my msgm.prg

**rpgcode:**

```
Method mbox(line1$, line2$, line3$, line4$, line5$, layout!)

{

//Save the screen for later reference

     SaveScreen()

//Setting up coordinates

     If(layout! == 1)

     {

//x pos of the img

          mx! = 0

// y pos of the img

          my! = 0

          tx! = 10

          ty! = 20

          If(layout! == 2)

          {

               mx! = 0

               my! = 450

               tx! = 10

               ty! = 470

          }

//Crate a new canvas for the message window

          cnvMWin! = CreateCanvas(640, 150)

//Set the background image and text into the canvas

          SetImage("mwin.jpg", mx!, my!, 640, 150, cnvMWin!)

          PixelText(1, 2, line1$)

          PixelText(tx!, ty!+25, line2$)

          PixelText(tx!, ty!+50, line3$)

          PixelText(tx!, ty!+75, line4$)

          PixelText(tx!, ty!+100, line5$)

//Draw the canvas to the screen

          DrawCanvas(cnvMWin!, mx!, my!)

//Return the keypress

          ReturnMethod(Wait())

//Kill the canvas and canvas ID

          KillCanvas(cnvMWin!)

          Kill(cnvMWin!)

//Return the screen to its original state

          RestoreScreen()

     }

     Method Msgprofile(line1$, line2$, line3$, line4$, line5$, layout!, profile$)

     {

//Save the screen for later reference

          SaveScreen()

          profile$ = profile$+".jpg"

          If(layout! == 1)

          {

//x pos of the img

               mx! = 0

// y pos of the img

               my! = 0

//y pos of the profile pi

               px! = 30

//y pos of the profile pi

               py! = 30

               tx! = 160

               ty! = 20

//Create a new canvas for the message window

               cnvMWin! = CreateCanvas(640, 150)

//Set the background image and text into the canvas

               SetImage("mwin.jpg", mx!, my! 640, 150, cnvMWin!)

               SetImage(profile$, px!, my!, 120, 120, cnvMWin!)

//tx!=x pos of the text, ty!=y pos of the text

               PixelText(tx!, ty!, line1$)

               PixelText(tx!, ty!+25, line2$)

               PixelText(tx!, ty!+50, line3$)

               PixelText(tx!, ty+75, line4$)

               PixelText(tx!, ty+100, line5$)

//Draw the canvas to the screen

               DrawCanvas(cnvMWin!, mx!, my!)

//Return the keypress

               ReturnMethod(Wait())

//Kill the canvas and canvas ID

               KillCanvas(cnvMWin!)

               Kill(cnvMWin!)

//Return the screen to its original state

               RestoreScreen()

          }
```

I just don't know why it shows the code, but not even the "#" sign if I add it before those mbox commands
HELP~~What should I do?? Is there something wrong with the code??

### stanleywuu · 2004-12-09 02:11 · #B136777

um.......after some testing, I think that tk doesn't recognize that mbox method I just made.....I even used the event editor to use the include command, but it just doesn't run the method....why??
What??I think it's saying that my setimage method is not found
I also tried setimagetranslucant...it didn't work either........... Evil or Very Mad
oh...never mind those, I realized I forgot to make changes when I made backup,after I changed everything, it just doesn't run that method AGAIN, i know because I put a msgbox as the first line to excecute in that method
Hm.........I think this is a bug now, when I rename the method to line1 which works in another program I downloaded, it reads the method and excecutes the command!! But I think TK is having trouble with either pixetext or restore now

### stanleywuu · 2004-12-09 03:00 · #B136809

Yes!! i figured it out!! I think tk3 is reading my variables as methods, did I do anything wrong in the if statement?? I deleted a lot stuff to get to the result,lol
Actually, it's not just the variable....doesn't matter what I put inside one of those if statements, I get an error
So I guess I know what to do now, I'm using switch instead

### RDemusX · 2004-12-09 03:52 · #B136846

This is what you could do:

**Code:**

```
*********************

*Custom Talk Program*

*********************

*Call Custom Talk Program: #talk(color!,pos!,text1$,text2$,text3$)*

#method talk(color!,pos!,text1$,text2$,text3$,text4$,text5$)

{

*Call all Varables*

#mwin$ = "mwin.gif"

#mx! =

#my! =

#prox! =

#proy! =

#anmx! =

#anmy! =

#tx1! =

#ty1! =

#tx2! =

#ty2! =

#tx3! =

#ty3! =

#tx4! =

#ty4! =

#tx5! =

#ty5! =

#mw! =

#mh! =

#prow! =

#proh! =

*Call Main Funtiion Block Program*

#color(color!)

#bold("on")

#fontsize(18)

#if(pos! = 2)

   {

   #mx! = mx! +

   #my! = my! +

   #prox! = prox! +

   #proy! = proy! +

   #anmx! = anmx! +

   #anmy! = anmy! +

   #tx1! = tx1! +

   #ty1! = ty1! +

   #tx2! = tx2! +

   #ty2! = ty2! +

   #tx3! = tx3! +

   #ty3! = ty3! +

   #tx4! = tx4! +

   #ty4! = ty4! +

   #tx5! = tx5! +

   #ty5! = ty5! +

   }

#if(pos! = 3)

   {

   #mx! = mx! +

   #my! = my! +

   #prox! = prox! +

   #proy! = proy! +

   #anmx! = anmx! +

   #anmy! = anmy! +

   #tx1! = tx1! +

   #ty1! = ty1! +

   #tx2! = tx2! +

   #ty2! = ty2! +

   #tx3! = tx3! +

   #ty3! = ty3! +

   #tx4! = tx4! +

   #ty4! = ty4! +

   #tx5! = tx5! +

   #ty5! = ty5! +

   }

#if(pos! = 4)

   {

   #mx! = mx! +

   #my! = my! +

   #prox! = prox! +

   #proy! = proy! +

   #anmx! = anmx! +

   #anmy! = anmy! +

   #tx1! = tx1! +

   #ty1! = ty1! +

   #tx2! = tx2! +

   #ty2! = ty2! +

   #tx3! = tx3! +

   #ty3! = ty3! +

   #tx4! = tx4! +

   #ty4! = ty4! +

   #tx5! = tx5! +

   #ty5! = ty5! +

   }

#savescreen(1)

#setimage(mwin$,mx!,my!,mw!,mh!)

#text(tx1!,ty1!,text1$)

#text(tx2!,ty2!,text2$)

#text(tx3!,ty3!,text3$)

#text(tx4!,ty4!,text4$)

#text(tx5!,ty5!,text5$)

#wait(a$)

#restorescreenarray(1)

#kill(mx!)

#kill(my!)

#kill(prox!)

#kill(proy!)

#kill(anmx!)

#kill(anmy!)

#kill(tx1!)

#kill(tx2!)

#kill(tx3!)

#kill(tx4!)

#kill(tx5!)

#kill(ty1!)

#kill(ty2!)

#kill(ty3!)

#kill(ty4!)

#kill(ty5!)

#kill(text1$)

#kill(text2$)

#kill(text3$)

#kill(text4$)

#kill(text5$)

#kill(color!)

#kill(pos!)

}

```

This could be used with your own values. You could also make it to where we through an animated picture profile in there. That is what I did. All profiles are animated.
This MWIN supports 4 different screen positions, 5 lines of text, and color.
You could get really detailed with it though.
RDX

### stanleywuu · 2004-12-09 04:08 · #B136855

um........so "if" statement works???
But when I used my own code, "if" statement didn't work at all
I tried deleting everything and found the problem was within that statement, so I switched the variables with things like savescreen, setimage
I still get the error mesage saying method not found......but when I use switch, everything's fine...

### RDemusX · 2004-12-09 15:55 · #B136997

**Code:**

```
Method mbox(line1$, line2$, line3$, line4$, line5$, layout!)

{

//Save the screen for later reference

     SaveScreen(1)

//Setting up coordinates

     If(layout! == 1)

     {

//x pos of the img

          mx! = 0

// y pos of the img

          my! = 0

          tx! = 10

          ty! = 20

         }

          If(layout! == 2)

          {

               mx! = 0

               my! = 450

               tx! = 10

               ty! = 470

          }

//Crate a new canvas for the message window

          cnvMWin! = CreateCanvas(640, 150)

//Set the background image and text into the canvas

          SetImage("mwin.jpg", mx!, my!, 640, 150, cnvMWin!)

          PixelText(1, 2, line1$)

          PixelText(tx!, ty!+25, line2$)

          PixelText(tx!, ty!+50, line3$)

          PixelText(tx!, ty!+75, line4$)

          PixelText(tx!, ty!+100, line5$)

//Draw the canvas to the screen

          DrawCanvas(cnvMWin!, mx!, my!)

//Return the keypress

          ReturnMethod(Wait())

//Kill the canvas and canvas ID

          KillCanvas(cnvMWin!)

          Kill(cnvMWin!)

//Return the screen to its original state

          RestoreScreenArray(1)

}

     Method Msgprofile(line1$, line2$, line3$, line4$, line5$, layout!, profile$)

     {

//Save the screen for later reference

          SaveScreen(1)

          profile$ = profile$+".jpg"

          If(layout! == 1)

          {

//x pos of the img

               mx! = 0

// y pos of the img

               my! = 0

//x pos of the profile pi

               px! = 30

//y pos of the profile pi

               py! = 30

               tx! = 160

               ty! = 20

              }

//Create a new canvas for the message window

               cnvMWin! = CreateCanvas(640, 150)

//Set the background image and text into the canvas

               SetImage("mwin.jpg", mx!, my! 640, 150, cnvMWin!)

               SetImage(profile$, px!, my!, 120, 120, cnvMWin!)

//tx!=x pos of the text, ty!=y pos of the text

               PixelText(tx!, ty!, line1$)

               PixelText(tx!, ty!+25, line2$)

               PixelText(tx!, ty!+50, line3$)

               PixelText(tx!, ty+75, line4$)

               PixelText(tx!, ty+100, line5$)

//Draw the canvas to the screen

               DrawCanvas(cnvMWin!, mx!, my!)

//Return the keypress

               ReturnMethod(Wait())

//Kill the canvas and canvas ID

               KillCanvas(cnvMWin!)

               Kill(cnvMWin!)

//Return the screen to its original state

               RestoreScreenArray(1)

          }
```

Copy and Paste the above code. I fixed the #if's and #Method's Brackets ... { } ... Everytime you start an #if statement you need to close it and everytime you start a #method ... you need to close it.
That is all I really seen wrong with it at a glance.
Try it and tell me what happens.
RDX

### Occasionally_Correct · 2004-12-09 16:10 · #B136999

You're drawing the canvas over your text. Razz
Change this:

**Code:**

```
//Crate a new canvas for the message window

cnvMWin! = CreateCanvas(640, 150)

//Set the background image and text into the canvas

SetImage("mwin.jpg", mx!, my!, 640, 150, cnvMWin!)

PixelText(1, 2, line1$)

PixelText(tx!, ty!+25, line2$)

PixelText(tx!, ty!+50, line3$)

PixelText(tx!, ty!+75, line4$)

PixelText(tx!, ty!+100, line5$)

//Draw the canvas to the screen

DrawCanvas(cnvMWin!, mx!, my!)
```

to this:

**Code:**

```
//Crate a new canvas for the message window

cnvMWin! = CreateCanvas(640, 150)

//Set the background image and text into the canvas

SetImage("mwin.jpg", mx!, my!, 640, 150, cnvMWin!)

PixelText(1, 2, line1$, cnvMWin!)

PixelText(tx!, ty!+25, line2$, cnvMWin!)

PixelText(tx!, ty!+50, line3$, cnvMWin!)

PixelText(tx!, ty!+75, line4$, cnvMWin!)

PixelText(tx!, ty!+100, line5$, cnvMWin!)

//Draw the canvas to the screen

DrawCanvas(cnvMWin!, mx!, my!)
```

### stanleywuu · 2004-12-09 21:35 · #B137091

Oh, thank you so much, now I"m done my message sys. can work on my homeworks now,lol
