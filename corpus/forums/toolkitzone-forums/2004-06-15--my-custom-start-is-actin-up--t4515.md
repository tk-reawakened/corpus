---
kind: forum-thread
id: "toolkitzone-forums/4515"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Code"
skin: "phpbb2"
thread_id: "4515"
title: "my custom start is actin up"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=4515"
written: "2004-06-15T05:08:00"
last_post: "2005-08-04T02:11:00"
date_confidence: "exact"
captured: ["20051018071907", "20060110142359", "20060110145756", "20060110154442", "20060110154506"]
author: "BlackPanther"
repliers: ["RPGman7", "Asimir", "ddl2829", "Tetsuo", "Noob From The Grave"]
authors: ["BlackPanther", "RPGman7", "Asimir", "ddl2829", "Tetsuo", "Noob From The Grave"]
posts_present: 6
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_240261_amp_3Bsid_7b0f89c3eeb922fa28a65e5f948c276c", captured: "20060110154442", sha256: "2a00598d09978f5e7a23414d122a0573aaee80970026b9a3914a62969be58c26", wayback_url: "https://web.archive.org/web/20060110154442/http://www.toolkitzone.com/forums/viewtopic.php?p=240261&amp%3Bsid=7b0f89c3eeb922fa28a65e5f948c276c"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_241414_amp_3Bsid_7b0f89c3eeb922fa28a65e5f948c276c", captured: "20060110154506", sha256: "2921587930f0d632435608a2a3f10177f797d82b60f38bb4eadc166cb490ff4e", wayback_url: "https://web.archive.org/web/20060110154506/http://www.toolkitzone.com/forums/viewtopic.php?p=241414&amp%3Bsid=7b0f89c3eeb922fa28a65e5f948c276c"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_241441", captured: "20060110145756", sha256: "8fcd3b53f2ff5e61b48711200bba8168b6bc51702f7d4ece640f9e127f055670", wayback_url: "https://web.archive.org/web/20060110145756/http://www.toolkitzone.com/forums/viewtopic.php?p=241441"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_241441_amp_3Bsid_7cde889a94523dc3911efb6795047320", captured: "20051018071907", sha256: "8bbc7d8649efe09d66180c8b9b807c18819f2dd8e9d066a5287a32ef40d688de", wayback_url: "https://web.archive.org/web/20051018071907/http://www.toolkitzone.com/forums/viewtopic.php?p=241441&amp%3Bsid=7cde889a94523dc3911efb6795047320"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_46673_amp_3Bsid_7b0f89c3eeb922fa28a65e5f948c276c", captured: "20060110142359", sha256: "8b7493b6c34bdcabae4d81cea06c733ed57186d4d6a821d557b154534f7976a2", wayback_url: "https://web.archive.org/web/20060110142359/http://www.toolkitzone.com/forums/viewtopic.php?p=46673&amp%3Bsid=7b0f89c3eeb922fa28a65e5f948c276c"}
links: []
---

# my custom start is actin up

### BlackPanther · 2004-06-15 05:08 · #B45688

This is my custom start and a couple of things are wrong with it. music should be playing, i have a cursor map setup so when i press up or down a sound should be playing and somethings wrong with my cursor map. Major help please
#Include("System.prg")
#ItemWalkSpeed("slow")
#WalkSpeed("slow")
#BorderColor(0,0,0)
#FontSize(30)
#Color(32)
#Fade(1)
#Clear()
#MediaPlay("FF3 TITLE.mid")
****************************
#Text(10,5,"BP Software")
#Text(10.5,8,"Presents")
#Pause()
#for (t!=1;t!<=11;t!=t!+1)
{
#Zoom(12.5)
}
#Clear()
#Delay(1)
****************************
#Color(15)
#Bitmap("rostitle.bmp")
#SaveScreen()
#num!=375
#SetImage("arrow.bmp",270,num!,75,45)
#select!=2
:10
#done!=0
#While(done!=0)
{
#Wait(key$)
#If(key$="UP")
{
#num! = num! - 100
#If(num!<=275)
{
#num!=475
}
#Wav("fight.wav")
#RestoreScreen()
#SetImage("arrow.bmp",270,num!,75,45)
#If(num!=275)
{
#select!=1
}
#If(num!=375)
{
#select!=2
}
#If(num!=475)
{
#select!=3
}
#done!=1
}
#If(key$="DOWN")
{
#num! = num! + 100
#If(num!>=475)
{
#num!=275
}
#Wav("fight.wav")
#RestoreScreen()
#SetImage("arrow.bmp",270,num!,75,45)
#If(num!=275)
{
#select!=1
}
#If(num!=375)
{
#select!=2
}
#If(num!=475)
{
#select!=3
}
#done!=1
}
#If(key$="ENTER")
{
#If(select!=1)
{
#End()
}
#If(select!=2)
{
#dirsav(dest$)
#if(dest$~="CANCEL")
{
#load(dest$)
#end
}
}
#If(select!=3)
{
#Mwin("You selected the third option.")
#Pause()
#Mwincls()
#Dos()
}
#done!=1
}
}
#Branch(:10)

### RPGman7 · 2004-06-17 13:37 · #B46673

I'm sorry but movable cursors are beyond me. For the MIDI try using #midiplay("music.mid") I have had problems with #mediaplay before. In fact, I can't even find it in the command reference. Confused

### Asimir · 2004-06-17 14:36 · #B46691

with this:

**Code:**

```
 #If(num!<=275)

{

#num!=475

}
```

try < instead of <=
and > instead of >= for this:

**Code:**

```
 #If(num!>=475)

{

#num!=275

}
```

Also, unless you're running this full screen, 375 and 475 are off the screen.
These are the only things that jumped out at me as being wrong. If there's still problems I'll take a closer look at the code.

### ddl2829 · 2005-07-31 18:17 · #B240261

also it might be eisier to use a cursormap. to chnge the cursor use the cursormaphand("cursor.png") command.

### Tetsuo · 2005-08-04 01:24 · #B241414

**ddl2829 wrote:**

> also it might be eisier to use a cursormap. to chnge the cursor use the cursormaphand("cursor.png") command.
>

Try using Dragcash's Pillar.....

### Noob From The Grave · 2005-08-04 02:11 · #B241441

**Code:**

```
#Include("System.prg")

#ItemWalkSpeed("slow")

#WalkSpeed("slow")

#BorderColor(0,0,0)

#FontSize(30)

#Color(32)

#Fade(1)

#Clear()

#MediaPlay("FF3 TITLE.mid")

****************************

#Text(10,5,"BP Software")

#Text(10.5,8,"Presents")

#Pause()

#for (t!=1;t!<=11;t!=t!+1)

{

   #Zoom(12.5)

}

#Clear()

#Delay(1)

****************************

#Color(15)

#Bitmap("rostitle.bmp")

#SaveScreen()

#num!=375

#SetImage("arrow.bmp",270,num!,75,45)

#select!=2

:10

#done!=0

#While(done!=0)

{

   #Wait(key$)

   #If(key$="UP")

   {

      #num! = num! - 100

      #If(num!<=275)

      {

         #num!=475

      }

      #Wav("fight.wav")

      #RestoreScreen()

      #SetImage("arrow.bmp",270,num!,75,45)

      #If(num!=275)

      {

         #select!=1

      }

      #If(num!=375)

      {

         #select!=2

      }

      #If(num!=475)

      {

         #select!=3

      }

      #done!=1

   }

   #If(key$="DOWN")

   {

      #num! = num! + 100

      #If(num!>=475)

      {

         #num!=275

      }

      #Wav("fight.wav")

      #RestoreScreen()

      #SetImage("arrow.bmp",270,num!,75,45)

      #If(num!=275)

      {

         #select!=1

      }

      #If(num!=375)

      {

         #select!=2

      }

      #If(num!=475)

      {

         #select!=3

      }

      #done!=1

   }

   #If(key$="ENTER")

   {

      #If(select!=1)

      {

         #End()

      }

      #If(select!=2)

      {

         #dirsav(dest$)

         #if(dest$~="CANCEL")

         {

            #load(dest$)

            #end

         }

      }

      #If(select!=3)

      {

         #Mwin("You selected the third option.")

         #Pause()

         #Mwincls()

         #Dos()

      }

      #done!=1

   }

}

#Branch(:10)
```

The sound works alright when i test this so the cmap is fine try that out.
