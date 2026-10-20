---
kind: forum-thread
id: "toolkitzone-forums/7332"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "7332"
title: "help w/ making credits scroll"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=7332"
written: "2004-08-17T15:53:00"
last_post: "2004-08-29T18:18:00"
date_confidence: "exact"
captured: ["20040928044443"]
author: "guest 2"
repliers: ["Occasionally_Correct", "bradseguin", "guest guy", "Mark_of_the_Dragon", "trunksbrief39", "Dont_Think_So", "Guest guy", "Kyra", "ForeverNoobish"]
authors: ["guest 2", "Occasionally_Correct", "bradseguin", "guest guy", "Mark_of_the_Dragon", "trunksbrief39", "Dont_Think_So", "Guest guy", "Kyra", "ForeverNoobish"]
posts_present: 14
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_77263_amp_", captured: "20040928044443", sha256: "2d97be2a8aa0d5aa9a412ece6ab91020ca27ad782b2035c806c2f37465f11edb", wayback_url: "https://web.archive.org/web/20040928044443/http://www.toolkitzone.com/forums/viewtopic.php?p=77263&amp="}
links:
  - {url: "http://dontemailmeanycrap.com/avatar.gif", status: "external", local: null}
  - {url: "http://img.photobucket.com/albums/v325/brent329/sw018.gif", status: "external", local: null}
  - {url: "http://kysoft.toolkitzone.com", status: "captured", local: "wayback/toolkitzone.com/kysoft.toolkitzone.com/index"}
  - {url: "http://overkill2013.geahost.com/Anti-Everything.png", status: "external", local: null}
  - {url: "http://server.net.nz/host/ks.gif", status: "external", local: null}
  - {url: "http://server.net.nz/host/kysoft_small.gif", status: "external", local: null}
  - {url: "http://server.net.nz/host/tko.gif", status: "external", local: null}
  - {url: "http://www.toolkitzone.com/stuff/files/101/handyvac-ASSHOLE.jpg", status: "captured", local: "wayback/toolkitzone.com/stuff/files/101/handyvac-ASSHOLE.jpg"}
---

# help w/ making credits scroll

### guest 2 · 2004-08-17 15:53 · #B77107

how do i make the credits scroll if its possible?

### Occasionally_Correct · 2004-08-17 17:23 · #B77139

Since, I'm lazy, I'll just copy and paste my reply from another topic. Razz

**I wrote:**

> Scrolling text method. Yay.
>
> **Code:**
>
> ```
> #Method ScrollText(initx!, inity!, endy!, text$, speed!)
>
>
> {
>
>
>    #speed! = speed! / 10
>
>
>    #For(y! = inity!; y! > endy!; y! = y! - 1)
>
>
>    {
>
>
>       #Text(initx!, y!, text$)
>
>
>       #Delay(speed!)
>
>
>       #Clear()
>
>
>    }
>
>
>    #Kill(initx!)
>
>
>    #Kill(inity!)
>
>
>    #Kill(endy!)
>
>
>    #Kill(text$)
>
>
>    #Kill(speed!)
>
>
>    #Kill(y!)
>
>
> }
> ```
>
> - initx! and inity! are the initial x and y coordinates to place the text.
> - endy! is the ending y coordinate of the text. If you want it to scroll down, change the For loop (y! < endy! instead of y! > endy!).
> - text$ is obvious.
> - speed! is pretty obvious too.
> Hope that helps.
>

_________________
:: it's better in the matinee, the dark of the matinee ::

### bradseguin · 2004-08-17 22:40 · #B77263

You could code it yes, but you could also make a animation to make it creative.
_________________
![](http://overkill2013.geahost.com/Anti-Everything.png)![](http://dontemailmeanycrap.com/avatar.gif)
![](http://img.photobucket.com/albums/v325/brent329/sw018.gif)
Wherever you see the evil monkey on the stairs pointing at you, you know I was there.

### guest guy · 2004-08-26 19:19 · #B82217

i tryed that code and it dint work, where do i write what i want to write and stuff, its just dosnt go on and i need it cause im finishing my game now

### Mark_of_the_Dragon · 2004-08-26 19:32 · #B82223

**Code:**

```
#Method ScrollText(initx!, inity!, endy!, text$, speed!)

{

   #speed! = speed! / 10

   #For(y! = inity!; y! > endy!; y! = y! - 1)

   {

      #Text(initx!, y!, text$)

      #Delay(speed!)

      #Clear()

   }

   #Kill(initx!)

   #Kill(inity!)

   #Kill(endy!)

   #Kill(text$)

   #Kill(speed!)

   #Kill(y!)

}
```

See where it says #Method ScrollText(initx!, inity!, endy!, text$, speed!)? It goes in the text$ parameter.
_________________
Never meddle in the affairs of dragons for you are crunchy and taste good with ketchup...
Message to you all: Read the help files before you ask questions; most questions can be answered. Also, make a game using default systems first; that will put you in a better position to make everythign on your own. You think xorlak relied on MrG for everything? No.

### trunksbrief39 · 2004-08-26 20:51 · #B82260

I think its alot easier to just make an animation, looks better too.
_________________
"Fear of living on, natives getting restless now! Mutiny in the air! Got some death to do! Mirror stares back hard, kill is such a friendly word! It seems the only way, for reaching out again!" - Metallica "Welcome Home (Sanitarium)"

### Dont_Think_So · 2004-08-26 23:56 · #B82379

Use #savescreen and #restorescreen to make a scrolling effect, then add text to the bottom of the screen with #text.
For the scrolling effect, use #savescreen then #restorescreen with slightly different offsets in the second set of coordinates; in other words, restore one part of the screen on top of the other, except a little up, and repeat.
Hope that helps; too lazy to code right now.
_________________
"Once upon a midnight dreary, while I websurfed, weak and weary,
...Over many a strange and spurious website of 'hot chicks galore',
...While I clicked my fav'rite bookmark, suddenly there came a warning,
...And my heart was filled with mourning, mourning for my dear amour.
..."'Tis not possible," I muttered, "give me back my cheap hardcore!" -
Quoth the server, "404"."
![](http://www.toolkitzone.com/stuff/files/101/handyvac-ASSHOLE.jpg)

### guest guy · 2004-08-27 18:00 · #B82874

can you please write this in code for me, the scrolling page thing where i can just write what i want

### Dont_Think_So · 2004-08-28 00:25 · #B83091

**Code:**

```
*Dont_Think_So's Super Credits System!

*Simply Add to the list below for your credits...

#CreditText[0]$="Designer"

#CreditEffect1[0]$="#bold(on)"

#CreditEffect2[0]$="#Colorrgb(255,128,0)"

#CreditEffect3[0]$="#fontsize(12)"

#CreditText[1]$="Guest Guy"

#CreditEffect1[1]$=""

#CreditText[2]$=""

#CreditEffect1[2]$="#fontsize(30)"

#CreditText[3]$="Producer"

#CreditEffect1[3]$="#bold(on)"

#CreditEffect2[3]$="#Colorrgb(255,128,0)"

#CreditEffect3[3]$="#fontsize(12)"

#CreditText[4]$="Guest Guy"

#CreditEffect1[4]$=""

#CreditText[5]$=""

#CreditEffect1[5]$="#fontsize(30)"

#CreditText[6]$="Character Designer"

#CreditEffect1[6]$="#bold(on)"

#CreditEffect2[6]$="#Colorrgb(255,128,0)"

#CreditEffect3[6]$="#fontsize(12)"

#CreditText[7]$="Guest Guy"

#CreditEffect1[7]$=""

#CreditText[8]$=""

#CreditEffect1[8]$="#fontsize(30)"

#CreditText[9]$="Special Thanks"

#CreditEffect1[9]$="#bold(on)"

#CreditEffect2[9]$="#Colorrgb(255,128,0)"

#CreditEffect3[9]$="#fontsize(12)"

#CreditText[10]$="Dont_Think_So"

#CreditEffect1[10]$=""

*Change this to the number of lines you have in your credits, including blank spots...

#numoflines!=30

*Replace the values with the color of the background you want, in RGB.

#BKG$="255,0,0"

*Replace this with the text color...

#Textcolor$="255,255,255"

********************************************

*You shouldn't have to change anything below here...

#Temp$="#ColorRGB("+BKG$+")"

#RPGCode(temp$)

#Clear

#Temp$="#ColorRGB("+Textcolor$+")"

#RPGCode(Temp$)

#getfontsize(fsize!)

*Start Credits Loop...

#for(c!=0; c!<=numoflines!; c!=c!+1)

{

#rpgcode(Temp$)

#fontsize(fsize!)

#RPGCode(CreditEffect1[c!]$)

#RPGCode(CreditEffect2[c!]$)

#RPGCode(CreditEffect3[c!]$)

#RPGCode(CreditEffect4[c!]$)

#getfontsize(tempfsize!)

#SpawnY!=352/tempfsize!

#text(1,SpawnY!,CreditText[c!]$)

#bold(off)

#italics(off)

#underline(off)

*Scroll for the length of one line...

#colorrgb(0,0,0)

#for(n!=0; n!<=tempfsize!; n!=n!+1)

{

#savescreen

#fillrect(0,351,540,352)

#restorescreen(0,1,540,384,0,0)

}

}
```

Read the comments, and replace the variables as they say, and it will work...
_________________
"Once upon a midnight dreary, while I websurfed, weak and weary,
...Over many a strange and spurious website of 'hot chicks galore',
...While I clicked my fav'rite bookmark, suddenly there came a warning,
...And my heart was filled with mourning, mourning for my dear amour.
..."'Tis not possible," I muttered, "give me back my cheap hardcore!" -
Quoth the server, "404"."
![](http://www.toolkitzone.com/stuff/files/101/handyvac-ASSHOLE.jpg)

### Guest guy · 2004-08-29 08:21 · #B84197

Thanks for that Cool , but is there anyway of making it so that i dont have to keep enter pressed the whole time

### Kyra · 2004-08-29 09:20 · #B84214

how about you do what everyone else has been saying and just make an animation?
_________________
[![](http://server.net.nz/host/kysoft_small.gif)](http://kysoft.toolkitzone.com)
![](http://server.net.nz/host/tko.gif)
![](http://server.net.nz/host/ks.gif)

### guest guy · 2004-08-29 09:52 · #B84233

thats to dificult

### ForeverNoobish · 2004-08-29 14:36 · #B84309

**Guest guy wrote:**

> Thanks for that Cool , but is there anyway of making it so that i dont have to keep enter pressed the whole time
>

Just looking at his code, you shouldn't have to press any buttons while the credits are rolling. Confused

### Dont_Think_So · 2004-08-29 18:18 · #B84392

Hmm... I didn't have to hold a key for it to work... I don't see why you should...
_________________
"Once upon a midnight dreary, while I websurfed, weak and weary,
...Over many a strange and spurious website of 'hot chicks galore',
...While I clicked my fav'rite bookmark, suddenly there came a warning,
...And my heart was filled with mourning, mourning for my dear amour.
..."'Tis not possible," I muttered, "give me back my cheap hardcore!" -
Quoth the server, "404"."
![](http://www.toolkitzone.com/stuff/files/101/handyvac-ASSHOLE.jpg)
