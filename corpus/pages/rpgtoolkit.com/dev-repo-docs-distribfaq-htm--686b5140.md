---
kind: page
id: "rpgtoolkit.com/rpgtoolkit.com/dev_repo/docs/distribFAQ.htm"
site: "rpgtoolkit.com"
title: "Updated August 7, 1999"
original_url: "http://rpgtoolkit.com/dev_repo/docs/distribFAQ.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20010410012114"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.com/dev_repo/docs/distribFAQ.htm", captured: "20010410012114", sha256: "a5dbac726ba0a7edf95b7799f2f5345bf68854920402514c99fe1ea864084b03", wayback_url: "https://web.archive.org/web/20010410012114/http://rpgtoolkit.com/dev_repo/docs/distribFAQ.htm"}
---

# Updated August 7, 1999

RPG Toolkit Development System, Version 2.07, (beta 7)**
Preparing A Game For Distribution
*
Covers:
You can use the Setup utility to automatically prepare a game for distribution. In order to use it properly, you must have the program pkzip25.exe, installed into your \Toolkit2\Zip\ directory. You can download pkzip from Awesome Software's website.
Alternatively, you can manually prepare a game for distribution. To do so, follow these steps...
***
Step 1: Copying the Trans2 program and related files
First of all, your game requires the Trans2.exe program in order to run. I suggest you make a separate directory on your computer right now that is the name of your game (something like c:\Jewel\ for ‘The Jewel of Destiny’). Into this directory, copy the following files that are found in your \Toolkit2\ directory:
>
> Trans2.exe *The required translation engine that runs the game.*
>
> Brddraw.exe *High speed graphics engine.*
>
> Base.fnt *The base font required by the game.*
>
> 256RGB.pal *The palette definition file. Required by all version 1 files.*
>
> Eula.txt *Legal info. You distribute this file, unaltered. **must***
>
> System.prg *RPGCode system library.*
>
Apart from these base files, there are some system files that you must copy into this directory as well that should be in your \Windows\System\ directory. They were put there by the Toolkit setup program. So, copy the following files from \Windows\System\ into your game directory:
>
> MSVBvm50.dll
>
> StdOle2.tlb
>
> OleAut32.dll
>
> OlePro32.dll
>
> AsycFilt.dll
>
> Ctl3D32.dll
>
> ComCat.dll
>
> Dialog.ocx
>
> Picclp32.ocx
>
If you don’t include these files, people who try to play your game will get all kinds of errors when they try to run it.
***
Step 2: Copying your game.
OK, so that’s the basic Trans2 program and everything that it requires. Now it’s time to actually copy your game into your new directory...
Copy the \Toolkit2\Main\ directory. This contains your main file. If you look at the \Toolkit2\Game\ directory, you’ll see that it has a number of subdirectories. Inside these subdirectories is where your game is actually stored. Just copy \Toolkit2\Game\gamename\ (where gamename is the name of your game-- it will be a directory). Within that directory, you will find the following...
*
>
\Bitmap\ *Where bitmaps are stored.*
\Bkrounds\ *Where background images are stored.*
\Boards\ *Where boards are stored.*
\Chrs\ *Where characters are stored.*
\Enemy\ *Where enemies are stored.*
\Font\ *Where fonts are stored. You should probably copy Base.fnt into here, too.*
\Item\ *Where items are stored.*
\Media\ *Where multimedia is stored.*
\Prg\ *Where RPGCode programs are stored. You should probably copy System.prg into here, too.*
\SpcMove\ *Where special moves are stored.*
\Tiles\ *Where all tiles are stored.*
You should probably go through these directories and delete any unnecessary files (tiles you don’t use, boards you don’t use, etc).
And that’s that, so far. Your whole game should be copied into the new game directory. I suggest you try running Trans2.exe from this directory to test if your game works before going any further.
***
Step 3: Zip up the files
The next step is to put your game into a zip file. To do this, you need a program like WinZip, but you can also do it with any other file compression program. I’ll explain how to do it with WinZip...
![](Image17.png)
First, go into WinZip, and select ‘New Archive’ from the ‘File’ menu. It will ask you for a filename for the new archive. Give it one, and remember what directory you put it in. This will open up a new window asking you what files you want to put into your zip file. In the file dialogue, locate your directory (c:\Jewel, or whatever), and go into it. Below the list of directories is a ‘File Name’ box. Put *.* into this box.
Make sure the following options is turned on: ‘Include Subdirectories’. Make sure ‘Include extra folder info’ is turned on (actually, that’s more a matter of preference). Then hit the button labeled ‘Add With Wildcards’. This will compress all of your files, and create a new zipped up file, ready to use. **not**
The zipped up file is the file that you will upload onto your website, put on a disk, or whatever. It includes all the files required to play your game.
That’s all. If you have any questions, don’t hesitate to email me (asoft@rocketmail.com). Remember to abide by the rules of distribution as outlined in the file ‘eula.txt’- you may not distribute games . **commercially**
Christopher B. Matthews
April 10, 1999.
*Updated August 7, 1999*
