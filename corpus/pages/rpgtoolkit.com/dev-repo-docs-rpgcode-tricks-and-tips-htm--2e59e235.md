---
kind: page
id: "rpgtoolkit.com/rpgtoolkit.com/dev_repo/docs/rpgcode_tricks_and_tips.htm"
site: "rpgtoolkit.com"
title: "RPGCode Tricks and Tips"
original_url: "http://rpgtoolkit.com/dev_repo/docs/rpgcode_tricks_and_tips.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20010411054330"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.com/dev_repo/docs/rpgcode_tricks_and_tips.htm", captured: "20010411054330", sha256: "a2c288575800a83fb943e3bae8cd99f107d93fddf94f65f71d04e52296ac3ad0", wayback_url: "https://web.archive.org/web/20010411054330/http://rpgtoolkit.com/dev_repo/docs/rpgcode_tricks_and_tips.htm"}
---

# RPGCode Tricks and Tips

**
RPGCode Tricks and Tips
(and some other cool stuff)
Christopher B. Matthews 11/30/99
RPGCode is powerful. And with any powerful tool, there are features that go unnoticed due to the large number of things you can do with it. This article will show you a few tricks you can do with RPGCode that you may not have known.
**
The #Start command
The #Start command is an all-purpose media command. It allows you to launch programs to view media types not supported by the Toolkit, but it also allows you to visit websites.
If you have a website for your game, you may want to use the #Start command to pop up the default browser and take you there. Here’s how that works…
#Mwin("Press 1 to go to my website")
#Wait(a$)
#if(a$=="1")
#Start("http://rpgtoolkit.pyar.com")
Your game will continue to run, but a new window will pop up to take you to the website. #Start can also be used to access ftp sites.
Let’s say you want to pop up a user’s guide for your game. You would probably save it as pure text (.txt) or some format like MSWord (.doc). You can access your file using this:
#Start("Media\guide.txt") *Will probably pop up notepad
#Start("Media\guide.doc") *Will pop up MS Word
If you use this, make sure you put these files into the \Toolkit2\Media\ directory.
**
#Method can be used for re-usable code
When you use the Toolkit, you will often find yourself typing the same commands over and over again. For example, if you wanted to put some text in the Message Window, you might use this:
#MwinCls()
#Mwin("text....")
#Mwin("")
#Mwin("Press any key")
#Wait(a$)
You probably know that this can get very repetitive. An alternative is to create a new command using the #Method command. For example, I could make a command called #MyWin that does all of the above for me. It might look like this:
#Method MyWin(text$)
#MwinCls()
#Mwin(text$)
#Mwin("")
#Mwin("Press any key")
#Wait(a$)
If I want to use my new command, I just have to type:
#MyWin("text right here")
The #Method command works by setting the variable in brackets (in his case, text$) to whatever value is passed to it (in this case, "text right here"). You can see that the body of the MyWin method acts the very same as the first code I showed you, except that it prints out the contents of text$.
If you want to use #MyWin a lot, you can put the #Method in its own file, called something like myCommands.prg. Now, whenever you want to use #MyWin, you just have to put #include ("myCommands.prg") at the top of each program.
**
Smaller graphics
Most people use the #Bitmap command to display graphics on the screen. But #Bitmap will automatically fill the screen with the graphic. What if you want to show a smaller graphic and you don’t want it to fill the screen?
An interesting trick is to use the #SetButton command to create a dummy button that uses a graphic. All buttons in the Toolkit are created from regular graphics, scaled to the size of the button. So, you could place a ‘button’ anywhere you want on the screen and just have it do nothing—it would essentially be a graphic.
Here’s an example:
#SetButton("graphic.jpg",0,x!,y!,width!,height!)
Of course, you would set the x! and y! coordinates to locate the graphic on the screen and also specify the width! and height!
**
General Toolkit Tricks
Apart from RPGCode, there are a few little tricks you can do with the Toolkit in general. One thing you can do is customize the Editor’s background graphic.
**
Changing the nebula graphic
When you start the Toolkit, you will see a nebula graphic in the background. You can change that graphic if you want to. It is saved as a file called bkg.jpg in the \Toolkit2\ directory. You can put any graphic called bkg.jpg in your toolkit directory and the Toolkit will use it as a background image (it would be smart to backup the original graphic, first).
This has no real use, but it would be sort of cool if you had the Title screen of the game you are working on right in the Toolkit editor.
Here’s an interesting experiment—what happens if you remove bkg.jpg from the directory altogether? (remember to back it up first!)
