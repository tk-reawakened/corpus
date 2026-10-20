---
kind: file
id: "toolkitzone.com/166"
site: "toolkitzone.com"
title: "password"
original_url: "http://www.toolkitzone.com/fileman.php?id=10&file=166"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040720042442", "20041105003827", "20060612031253"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_166", captured: "20040720042442", sha256: "aafc8377c923b57554d2bf36bc55becf8bb82bdb7801dc28236bb55ef0f567e3", wayback_url: "https://web.archive.org/web/20040720042442/http://www.toolkitzone.com/fileman.php?id=10&file=166"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_166", captured: "20041105003827", sha256: "89b7bc4984bdbe76a6ce2805e344c595753fb2d78f135462512285628dfe76de", wayback_url: "https://web.archive.org/web/20041105003827/http://www.toolkitzone.com/fileman.php?id=5&file=166"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_166", captured: "20060612031253", sha256: "0cad4982b719ae989c13e1e2a0d5f05f62717310dc67a86b7c5c11dfbd7f90a0", wayback_url: "https://web.archive.org/web/20060612031253/http://www.toolkitzone.com/fileman.php?id=3&file=166"}
---

# password

beta version - report any problems to filemanager@toolkitzone.com
**Rpg-code tutorial**
In this tutorial I will show you how to make a Inn program. It's a tutorial for beginners so if you are not a beginner don't waste your time on this.
Here are the commands I will use in this tutorial:
** #mwin() #mwincls() @ #if() #delay() #wait() #inn() #end() #getgp() #takegp()
You should check the help-files for command that you don't know. (Help-->RpgCode Command Reference)
We start with a little conversation where you are asked what you want:
** #getgp(gp!) #mwin("Do you want to sleep here tonight?") #delay(0.5) #mwin("Price:10 GP: ") @ #mwin("1 - Yes") #mwin("2 - No") #wait(choice$) #mwincls()
The command is so that the program knows how much gp you have. You can choose between "Yes" and "No", so we gotta make those programs with the command: **#getgp()** **#if()**
** #if(choice$="1") {
** #if(gp!=<10) { #mwin("I'm sorry, you dont have that much money") #wait() #mwincls() #end() }
** #if(gp!=>10) { #mwin("Sleep well!") #wait() #mwincls() #takegp(10) #inn() } }
If you want to sleep there, you have to press 1. But the program does also have to know if you have enough gp. It checks this with the two commands in the original command. If you don't have enough it goes to the command , and if you do have enough money it goes to the command . That is what those > and < are for, you will probably use them a lot in other programs, so remember them. **#if()** **#if()** **#if(gp!=<10)** **#if(gp!=>10)**
You have also gotta have a program for if you don't want to sleep there of course:
** #if(choice$="2") { #mwincls() #mwin("Come back anytime!") #wait() }
I don't think there's something not to understand about this… Anyways, here's the full program:
** #GetGP(gp!) #mwin("Do you want to sleep here tonight?") #delay(0.5) #mwin("Price:10 GP: ") @ #mwin("1 - Yes") #mwin("2 - No") #wait(choice$) #mwincls() #if(choice$="1") {
** #if(gp!=<10) { #mwin("I'm sorry, you dont have that much money") #wait() #mwincls() #end() }
** #if(gp!=>10) { #mwin("Sleep well!") #wait() #mwincls() #takegp(10) #inn() } }
** #if(choice$="2") { #mwincls() #mwin("Come back anytime!") #wait() }
One last thing. In the first command you see two other commands. They are a bit further in the line. This is so that I wont get confused if there's something I want to add, look at this: **#if()** **#if()**
** #if() { #if { #something } #if { #something } }
Confusing? Yes, now take a look at this:
** #if() { #if { #something } #if { #something } }
Much less confusing. Don't forget to do this in other programs. You can also have a program where you have 2 commands in a command, and 2 other in that first command, and also some in that command, and if you do it in a straight line then, you get even more confused then here :S. **#if()** **#if()** **#if()** **#if()**
