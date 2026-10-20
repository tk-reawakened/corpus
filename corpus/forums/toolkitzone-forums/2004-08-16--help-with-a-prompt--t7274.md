---
kind: forum-thread
id: "toolkitzone-forums/7274"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "7274"
title: "help with a prompt"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=7274"
written: "2004-08-16T16:54:00"
last_post: "2004-08-20T04:10:00"
date_confidence: "exact"
captured: ["20040917185210", "20040925162357"]
author: "guest 2"
repliers: ["RPGuru", "Cerebrus", "rdemusx", "KSNiloc", "Asimir"]
authors: ["guest 2", "RPGuru", "Cerebrus", "rdemusx", "KSNiloc", "Asimir"]
posts_present: 15
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_76553_amp_", captured: "20040917185210", sha256: "c9a3a9b4dba332878edbb52361f001dd3a471d36344b43673b58ca6347b57984", wayback_url: "https://web.archive.org/web/20040917185210/http://www.toolkitzone.com/forums/viewtopic.php?p=76553&amp="}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_76965_amp_", captured: "20040925162357", sha256: "98815bf7a340919e05bcc0326abcf68be9e2ac087b7775cd4338a8ab28668232", wayback_url: "https://web.archive.org/web/20040925162357/http://www.toolkitzone.com/forums/viewtopic.php?p=76965&amp="}
links:
  - {url: "http://img.photobucket.com/albums/v293/rdemusx/MOTM/newadbar.gif", status: "external", local: null}
  - {url: "http://img.photobucket.com/albums/v293/rdemusx/newvid.gif", status: "external", local: null}
  - {url: "http://img.photobucket.com/albums/v491/Diddums/banner.png", status: "external", local: null}
  - {url: "http://mansionsofthemoon.myfreebb.com/index.php", status: "external", local: null}
  - {url: "http://mansionsofthemoon.tripod.com", status: "external", local: null}
  - {url: "http://mars.walagata.com/w/asimir/monkeys.gif", status: "external", local: null}
  - {url: "http://mr-diddums.tk", status: "external", local: null}
  - {url: "http://vidoentertainment.com", status: "external", local: null}
  - {url: "http://www.cywh.com/ot/", status: "external", local: null}
  - {url: "http://www.mg.geahost.com/small_theproject.gif", status: "external", local: null}
  - {url: "http://www.mg.geahost.com/tkgforum/index.php?c=5", status: "external", local: null}
  - {url: "http://www.mr-diddums.tk", status: "external", local: null}
  - {url: "http://www.mysticsoftware.net/images/banner_tkarmy.png", status: "captured", local: "wayback/mysticsoftware.net/images/banner_tkarmy.png"}
  - {url: "http://www.toolkitzone.com/forums/viewforum.php?f=165", status: "captured", local: "wayback/toolkitzone.com/forums/viewforum.php__f_165"}
  - {url: "http://www.zakap.com/", status: "external", local: null}
---

# help with a prompt

### guest 2 · 2004-08-16 16:54 · #B76553

i have a program where if you say the right thing in the prompt then you get a charector and i need the prompt thing to still stay there after he puts the word in because the prompt is used for other things to but i need just that program where you get the charector 2 stop after u use it once how would i do this?

### RPGuru · 2004-08-17 04:08 · #B76965

WOW... Can you say.. Run on Sentance... or maybe thats just the biggest sentance in the world.. lol.. actually If you explained your question just a bit more clearly we could help you.. lol.. good luck!
_________________
~`~'Guru'~`~
[Visit My Site! Zakap Enteprises](http://www.zakap.com/)

### guest 2 · 2004-08-18 17:49 · #B77781

how do i get a part of a prompt to stop forever while other things in the prompt will still work

### RPGuru · 2004-08-19 02:42 · #B78128

hehe... your question is still WAY to vague.. I'd writh the script for you if I knew WHAT you meant by "parts of a prompt" and the other things... can you give me an example.. like a specific example..?
_________________
~`~'Guru'~`~
[Visit My Site! Zakap Enteprises](http://www.zakap.com/)

### guest 2 · 2004-08-19 14:52 · #B78317

{
#Prompt ("What is the word?",name$)
#Mwincls()
#If(name$ == moneydoesntgrowontrees)
{
#Mwin("Cheat activated")
#Wait(a!)
#givegp(100)
#done! = 1
}
#If(name$ ==no)
{
#Mwin("no")
#Wait(a!)
#done! = 1
}
#If(name$ == yes)
{
#Mwin("yes")
#Wait(a!)
#done! = 1
}
ok so i want he part that says "#If(name$ == no)" to stop working after you use it once but i still want the part that says "#If(name#$ == yes)"
to still be able to work how would i get this 2 happen?

### Cerebrus · 2004-08-20 02:33 · #B78734

You need quotation marks around yes and no in the if commands.
_________________
Cerebrus
"A journey of a thousand miles is started by taking the first step." -Chinese Proverb
Anyone who has played Resident Evil and bothered to *READ* should know the following quote...
"4. Itchy. Tasty."
MUAHAHAHAHA!
[![](http://img.photobucket.com/albums/v491/Diddums/banner.png)](http://www.toolkitzone.com/forums/viewforum.php?f=165)

### RPGuru · 2004-08-20 03:32 · #B78751

Ahh... so you are basically saying.. if they choose yes it loops to the top? and if they choose no then the program ends? cause that I do know how to do! if this is in fact what you are trying to do! Wink
_________________
~`~'Guru'~`~
[Visit My Site! Zakap Enteprises](http://www.zakap.com/)

### rdemusx · 2004-08-20 03:33 · #B78752

This might work but I haven't tested it. You will make two different programs and use the #change(programfilename$) command to make it stop using everything but the #if(name$ = "no") stuff. Try it.
RDX

**Code:**

```
***********************

*Here ya go (hopefully ... )*

***********************

#done! = 1

#while(done! = 1)

          {

          #prompt("What is the word?",name$)

          #wait(a$)

          #mwincls()

          #if(name$ = "moneydon'tgrowontrees")

              {

              #mwin("Cheat Activated!")

              #wait(a$)

              #mwincls()

              #givegp(100)

              #done! = 2

              }

          #if(name$ = "no ")

              {

              *put what ever commands you want to run*

              #change("prompt2.prg")

              #done! = 2

              }

          #if(name$ = "yes")

              {

              *put what ever commands you want to run*

              #change("prompt2.prg")

              #done! = 2

              }

          #kill(name$)

          }

*************************************************************

*You would make the above program and save as whatever you want     *

*Then make a program like this and save as "prompt2.prg"...                 *

*************************************************************

#done! = 1

#while(done! = 1)

          {

          #prompt("What is the word?",name$)

          #wait(a$)

          #mwincls()

          #if(name$ = "yes")

              {

              *put whatever commands you want to run

              #done! = 2

              }

          #kill(name$)

          }
```

_________________
![](http://img.photobucket.com/albums/v293/rdemusx/MOTM/newadbar.gif)
![](http://img.photobucket.com/albums/v293/rdemusx/newvid.gif)
VISIT WEBSITE: <http://mansionsofthemoon.tripod.com>
VISIT FORUMS: <http://mansionsofthemoon.myfreebb.com/index.php>
VISIT Vi D.O. ENT: <http://vidoentertainment.com>

### KSNiloc · 2004-08-20 03:35 · #B78753

Change() only works until you leave the board.
Don't use it.
_________________
[![](http://img.photobucket.com/albums/v491/Diddums/banner.png)](http://mr-diddums.tk)

### rdemusx · 2004-08-20 03:54 · #B78764

well ... I thought I was helping. It was a shot. Smile
RDX
_________________
![](http://img.photobucket.com/albums/v293/rdemusx/MOTM/newadbar.gif)
![](http://img.photobucket.com/albums/v293/rdemusx/newvid.gif)
VISIT WEBSITE: <http://mansionsofthemoon.tripod.com>
VISIT FORUMS: <http://mansionsofthemoon.myfreebb.com/index.php>
VISIT Vi D.O. ENT: <http://vidoentertainment.com>

### Asimir · 2004-08-20 03:57 · #B78766

**Quote:**

> Change() only works until you leave the board.
> Don't use it.
>

It would be nice of you to provide an alternative then

**Code:**

```
#done! = 0

#while(done! = 0)

{

 #Prompt ("What is the word?",name$)

 #Mwincls()

 #If(name$ == "moneydoesntgrowontrees")

 {

  #Mwin("Cheat activated")

  #Wait(a!)

  #givegp(100)

  #done! = 1

 }

 #If(name$ =="no")

 {

  #if(noDone! == 0)

  {

   #Mwin("no")

   #Wait(a!)

   #done! = 1

   #noDone! = 1

  }

 }

 #If(name$ == "yes")

 {

  #Mwin("yes")

  #Wait(a!)

  #done! = 1

 }

}
```

_________________
![](http://mars.walagata.com/w/asimir/monkeys.gif)
[![](http://www.mysticsoftware.net/images/banner_tkarmy.png)](http://www.cywh.com/ot/) [![](http://www.mg.geahost.com/small_theproject.gif)](http://www.mg.geahost.com/tkgforum/index.php?c=5)
[![](http://img.photobucket.com/albums/v491/Diddums/banner.png)](http://www.mr-diddums.tk)

### rdemusx · 2004-08-20 03:59 · #B78767

could you have make two methods and #redirect? Just wanting to know now! heh ...
RDX
_________________
![](http://img.photobucket.com/albums/v293/rdemusx/MOTM/newadbar.gif)
![](http://img.photobucket.com/albums/v293/rdemusx/newvid.gif)
VISIT WEBSITE: <http://mansionsofthemoon.tripod.com>
VISIT FORUMS: <http://mansionsofthemoon.myfreebb.com/index.php>
VISIT Vi D.O. ENT: <http://vidoentertainment.com>

### KSNiloc · 2004-08-20 04:06 · #B78770

**Asimir wrote:**

>
> **Quote:**
>
> > Change() only works until you leave the board.
> > Don't use it.
> >
>
> It would be nice of you to provide an alternative then
>

I didn't understand the question, all I saw was Change(). Razz
_________________
[![](http://img.photobucket.com/albums/v491/Diddums/banner.png)](http://mr-diddums.tk)

### RPGuru · 2004-08-20 04:08 · #B78772

You all bicker like your married or something! Wink
_________________
~`~'Guru'~`~
[Visit My Site! Zakap Enteprises](http://www.zakap.com/)

### rdemusx · 2004-08-20 04:10 · #B78775

Thank You Aismir for clearing that up for everyone! Smile
RDX
_________________
![](http://img.photobucket.com/albums/v293/rdemusx/MOTM/newadbar.gif)
![](http://img.photobucket.com/albums/v293/rdemusx/newvid.gif)
VISIT WEBSITE: <http://mansionsofthemoon.tripod.com>
VISIT FORUMS: <http://mansionsofthemoon.myfreebb.com/index.php>
VISIT Vi D.O. ENT: <http://vidoentertainment.com>
