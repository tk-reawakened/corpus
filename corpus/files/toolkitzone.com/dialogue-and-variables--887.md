---
kind: file
id: "toolkitzone.com/887"
site: "toolkitzone.com"
title: "Dialogue and Variables"
original_url: "http://www.toolkitzone.com/fileman.php?id=10&file=887"
written: "2004-11-10"
date_confidence: "day"
updated: "2004-11-10"
captured: ["20060304191339", "20060312124401", "20060312130042", "20060312130331"]
author: "ViperCat"
repliers: []
authors: ["ViperCat"]
comments_present: 0
f_author_source: "ViperCat"
f_name: "Dialogue and Variables"
f_submitted_by: "ViperCat"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_887", captured: "20060304191339", sha256: "cef824b6af874639284b49c8b23549d65b831a2370ec66852558eb3e24a61fd7", wayback_url: "https://web.archive.org/web/20060304191339/http://www.toolkitzone.com:80/fileman.php?id=3&file=887&PHPSESSID=9e94a0bfd739af13980670d1e820a329"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_887", captured: "20060312124401", sha256: "af784c363762270e13f51a0db44c7c26054b8e93ed7d60aac65d689eea68dc78", wayback_url: "https://web.archive.org/web/20060312124401/http://www.toolkitzone.com:80/fileman.php?id=5&file=887&PHPSESSID=9e94a0bfd739af13980670d1e820a329"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_7_file_887", captured: "20060312130042", sha256: "979482b154f6961ea53554a2392debca3b7defb86ca3b51d1ab5190bfe2b1b30", wayback_url: "https://web.archive.org/web/20060312130042/http://www.toolkitzone.com:80/fileman.php?id=7&file=887&PHPSESSID=9e94a0bfd739af13980670d1e820a329"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_887", captured: "20060312130331", sha256: "c3faf752469efb5c7de100c7e78ab3d391841e46228fd7c0d4f703e333218e00", wayback_url: "https://web.archive.org/web/20060312130331/http://www.toolkitzone.com:80/fileman.php?id=10&file=887&PHPSESSID=9e94a0bfd739af13980670d1e820a329"}
---

# Dialogue and Variables

Introductory tutorial for those not only new to RPG Code, but also to the basic concept of using variables. A little short for my liking, but is certainly of use as a quick read to any new user.
Dialogue and Variables
Dialogue
Part 1
Well dialogue is a very simple thing to understand.A very basic skill and is essential for the making of your game.
#MWin("Text....")
#Wait(a$)
#MWincls()
The "Mwin" Command brings up a message window.The "Wait" command simply waits till the player presses a button."MWinCls" closes all Message Windows.Dialogue is more than just the simple 'Three Command Combo' that was shown.It also includes Text, Fonts, and colors.
Part 2
The "Text" Command makes a text appear on the screen.This command is a very flexible command considering that in #MWin, it sets it to a default position, but with the "Text" command you can set the coords of where you want the text to appear.Example:
Text(1,1,"Text....")
See the '1,1' are the X! and Y! Coords of the text.You can also change the color depending on RGB or Red Green and Blue shades.You can change these colors with the "ColorRGB" command.Example:
#ColorRGB(250, 0, 0)
#Text(1,1,"Text...")
Wich appears as - at 1,1. Text...
Now since you see what you can do for color, let's look at the font. The "Font" command changes the font of the text that appears on screen with Text and Mwin.Example:
#Font("Arial")
#MWin("Hi!!")
The text in the Message Window would appear as - if you have Arial as a font. Hi!!
Variables
Variables can be used as alot of things.They are used to identify or declare values like so -
#hi!=1
Variables can be literal($) or numeric(!).Since numeric is numbers, literal is self-explanatory.You can use variables to more expand the RPGCode.
Using Dialogue and Variables Together
You can use dialogue and variables together in a very effective way.Mostly to see stats and such.Example-
#health!=playerHP[0]!
#Text(1,5,"Your health is - health!")
See it is a simple thing to do.Well this is 1 out of many tutorials to come for you beginners out there.
**Browse Sections**
