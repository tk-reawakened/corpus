---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/help.php?article=4&mode=1"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://mysticsoftware.net/help.php?mode=1&article=4"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040504142350"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/help.php__mode_1_article_4", captured: "20040504142350", sha256: "f8eeb3616f4bdf88f03d44d963fb98e92428c3e70093cb4bdbd86715d227ec71", wayback_url: "https://web.archive.org/web/20040504142350/http://mysticsoftware.net/help.php?mode=1&article=4"}
---

# Mystic Software

Have you ever wanted to have the Toolkit respond to every step made by the character? Perhaps you want to be able to have a counter that logs steps, or want to make an online game that updates according to every step. Well, finally, it is possible! And, believe it or not, it is surprisingly easy, and you have been able to do it since version 1! So, let's get going. We will make a program that adds to a counter with every step. Here is our code: #counter! = counter! + 1 We will name this program Everystep.prg. We will make the Toolkit display the results of the counter with this program: #mwin("
- Clever Steps -
Written By Dont_Think_So
") #Wait() #mwincls() Okay, so we have made our programs. Now is the time where we will trick the TK into calling our first program with every step. Here is the method, step-by-step (no pun intended): 1. Open up the Main file editor 2. Go into the Fighting Tab (yes, the FIGHTING tab!) 3. Make sure that fighting is enabled in your game. 4. Click the Edit button. 5. Where it says "Use Built-In Fighting System?" Select No, Run Program. 6. Enter your your program's name (In our example, Everystep.prg) into the box. 7. Almost finished! Under "Fighting Type", select Planned. 8. In the box that appears type "1". This will force the toolkit to run our program every step of the way (again, no pun intended)! But wait! We're not finished! Okay, so now the toolkit logs every step that we make. But, now we don't have a battle system! Don't worry. Modify your Everystep.prg program to look like this: #counter! = counter! + 1 #random(10,fightornot!) #if(fightornot!==5){#fight(boardskill!,boardbackground$)} This program makes it a 1-in-10 chance to fight an enemy. If you want a different chance, then change 10 in the #random command to whatever you want. Have fun! :)
