---
kind: file
id: "toolkitzone.com/162"
site: "toolkitzone.com"
title: "password"
original_url: "http://toolkitzone.com/fileman.php?id=10&file=162"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040621094721", "20040621094721", "20040621094721", "20040706140055", "20040706140055", "20040706140055", "20041104193548", "20060312125415"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_162", captured: "20040621094721", sha256: "04a0f85359c5da0edae4b7a60c783f3013be976307be917ab3cac24f7f5a6c6b", wayback_url: "https://web.archive.org/web/20040621094721/http://toolkitzone.com/fileman.php?id=3&file=162"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_162-198758", captured: "20040621094721", sha256: "04a0f85359c5da0edae4b7a60c783f3013be976307be917ab3cac24f7f5a6c6b", wayback_url: "https://web.archive.org/web/20040621094721/http://www.toolkitzone.com/fileman.php?id=3&file=162"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_162-6e54d0", captured: "20040621094721", sha256: "04a0f85359c5da0edae4b7a60c783f3013be976307be917ab3cac24f7f5a6c6b", wayback_url: "https://web.archive.org/web/20040621094721/http://toolkitzone.com/fileman.php?id=3&file=162"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_162", captured: "20040706140055", sha256: "fcfe560794b1f2198648d26dcaa6ade82c873c0a87cb40a7c85a993144f1fb51", wayback_url: "https://web.archive.org/web/20040706140055/http://toolkitzone.com/fileman.php?id=10&file=162"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_162-4a9177", captured: "20040706140055", sha256: "fcfe560794b1f2198648d26dcaa6ade82c873c0a87cb40a7c85a993144f1fb51", wayback_url: "https://web.archive.org/web/20040706140055/http://www.toolkitzone.com/fileman.php?id=10&file=162"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_162-c745a9", captured: "20040706140055", sha256: "fcfe560794b1f2198648d26dcaa6ade82c873c0a87cb40a7c85a993144f1fb51", wayback_url: "https://web.archive.org/web/20040706140055/http://toolkitzone.com/fileman.php?id=10&file=162"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_162", captured: "20041104193548", sha256: "896f575531a6e906f19168760235d5300b12a5f88e2c597014c202eb63286a5e", wayback_url: "https://web.archive.org/web/20041104193548/http://www.toolkitzone.com/fileman.php?id=5&file=162"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_7_file_162", captured: "20060312125415", sha256: "147c08fe46a01fdbb9f491484c4c994bbd90883c9478b16308f6e54024b00308", wayback_url: "https://web.archive.org/web/20060312125415/http://www.toolkitzone.com:80/fileman.php?id=7&file=162&PHPSESSID=9e94a0bfd739af13980670d1e820a329"}
---

# password

beta version - report any problems to filemanager@toolkitzone.com
**Rpg Code tutorial**
This tutorial will learn you how to make a custom shop program using commands. It's best to first try the normal shop tutorial. At first, the commands we will use: **#while()**
** #getgp() #colorrgb() #fillrect() #drawline() #fontsize() #text() #while() #wait() #if() #branch() #giveitem() #takegp() #delay() #clearbuffer()
For commands you don't know, check the helpfile in Toolkit. (Help-->RpgCode Command Reference)
Actually, in this tutorial you will not only learn how to make a custom shop program, but also how to use a very useful command, the command. You will use this command a lot in other programs, so make sure you know how to use it. **#while()**
It's best to now open the program editor in Toolkit (if you haven't done so already).
Let's start with putting the lines in the right locations:
** #colorrgb(50,50,250) #fillrect(1,1,606,350)
** #colorrgb(0,0,0) #drawline(0,0,607,0) #drawline(0,0,0,351) #drawline(607,0,607,351) #drawline(0,351,608,351)
** #drawline(1,52,180,52) #drawline(180,1,180,351) #drawline(1,200,180,200)
Copy and past this into the program editor. Put a command behind it so you have the time to see how it looks. Test it. You will see a blue background with lines in it. The first command made the background blue, after that I made the colorrgb black so the lines would be black. Now let's put the text in it: **#wait()** **#colorrgb()**
** #getgp(gold!) #fontsize(25) #text(2,2,"Woozy's Shop!") #text(2,5,"What do you") #text(2,6,"want to buy?") #text(2,14,"GP: ")
Nothing not to understand here I think. First it checked how many GP you got and saved it in the gold! variable. In the text it displayed this with the command. Copy and past this into your program editor behind the first part. Don't forget to put the command behind it and delete the other one. Test to see what we got now. **#wait()**
Now we will going to put in the commands. First make a variable: **#while()**
**#shop!=0**
Now start with putting the all the commands in the program: **#while()**
** #while (shop!=0) { }
** #while (shop!=1) { }
** #while (shop!=2) { }
** #while (shop!=3) { }
Because we first made the variable, it will go to the first because that equals the variable. Since I have 3 items and 1 "leave" command, I need 4 commands. If you have more items, you will need more of them. Now let's start with putting the other commands IN those commands: **#while()** **#while()** **#while()**
** :shop0 #While (shop!==0) {
** #colorRGB(200,0,0) #Text(11,3.5,"Sword 50 GP") #colorRGB(255,255,255) #Text(11,5.5,"Shield 50 GP") #Text(11,7.5,"Gem 500 GP") #Text(11,12.5,"Leave") #Wait(a$) }
** :shop1 #while (shop!=1) { #Text(11,3.5,"Sword 50 GP") #colorRGB(255,255,255) #colorRGB(200,0,0) #Text(11,5.5,"Shield 50 GP") #colorRGB(255,255,255) #Text(11,7.5,"Gem 500 GP") #Text(11,12.5,"Leave") #Wait(a$) }
** :shop2 #while (shop!=2) { #colorRGB(255,255,255) #Text(11,3.5,"Sword 50 GP") #Text(11,5.5,"Shield 50 GP") #colorRGB(255,255,255) #colorRGB(200,0,0) #Text(11,7.5,"Gem 500 GP") #colorRGB(255,255,255) #Text(11,12.5,"Leave") #Wait(a$) }
** :shop3 #while (shop!=3) { #Text(11,3.5,"Sword 50 GP") #Text(11,5.5,"Shield 50 GP") #Text(11,7.5,"Gem 500 GP") #colorRGB(200,0,0) #Text(11,12.5,"Leave") #Wait(a$) }
If you would check the #colorrgb command in each command you would see that they are different each time. There is 1 red colorrgb in every command to make one line of text red, which is the text you are on at that point. The goal is that if you press UP or DOWN on your keyboard, you would go to the command above or beneath the line you are on at that point. This is what the labels are for (the thingys). If you would press then then would be different and you would have to branch up again. Let's put this in one command: **#while()** **#while()** **:shop0** **#shop!** **#while()**
** :shop0 #While (shop!==0) {
** #If (a$=="UP") { #shop!==3 #Branch(:shop3) }
** #If (a$=="DOWN") { #shop!==1 #Branch(:shop1) }
I left the commands out of it to save some space, they would be directly under the bracket under the command like they were in the example above. Now you see that when you would press UP or DOWN, the variable would change and that you would branch to the command that equals the #shop! variable. You can of course also just make 1 branch command above all the code but I did it this way. Now here's the command for if you press ENTER (so if you want to buy something): **#text()** **#while()** **#shop!** **#while()**
** #If (a$=="ENTER") { #If (gold!>50) { #Giveitem("sword.itm") #TakeGP(50) } #If (gold!<50) { #Delay(1) } } }
It checks if you have enough gold first and then go to the correct command. So if you wouldn't have enough money, it would wait for one second (the command) and if you would have enough money it would give you the item and take your GP (if it wouldn't do this the items would be free). This is the same for all commands (except a different item) except for if you want to leave. I'll put the whole code here first: **#if()** **#delay()** **#while()**
** #colorrgb(50,50,250) #fillrect(1,1,606,350)
** #colorrgb(0,0,0) #drawline(0,0,607,0) #drawline(0,0,0,351) #drawline(607,0,607,351) #drawline(0,351,608,351)
** #drawline(1,52,180,52) #drawline(180,1,180,351) #drawline(1,200,180,200)
** #getgp(gold!) #fontsize(25) #text(2,2,"Woozy's Shop!") #text(2,5,"What do you") #text(2,6,"want to buy?") #text(2,14,"GP: ")
**#shop!=0**
** ******************************** :shop0 #While (shop!==0) {
** #colorRGB(200,0,0) #Text(11,3.5,"Sword 50 GP") #colorRGB(255,255,255) #Text(11,5.5,"Shield 50 GP") #Text(11,7.5,"Gem 500 GP") #Text(11,12.5,"Leave") #Wait(a$)
** #If (a$=="UP") { #shop!==3 #Branch(:shop3) }
** #If (a$=="DOWN") { #shop!==1 #Branch(:shop1) }
** #If (a$=="ENTER") { #If (gold!>50) { #Giveitem("sword.itm") #TakeGP(50) } #If (gold!<50) { #Delay(1) } } } ***************************** :shop1 #While (shop!==1) {
** #Text(11,3.5,"Sword 50 GP") #colorRGB(255,255,255) #colorRGB(200,0,0) #Text(11,5.5,"Shield 50 GP") #colorRGB(255,255,255) #Text(11,7.5,"Gem 500 GP") #Text(11,12.5,"Leave") #Wait(a$)
** #If (a$=="UP") { #shop!==0 #Branch(:shop0) }
** #If (a$=="DOWN") { #shop!==2 #Branch(:shop2) }
** #If (a$=="ENTER") { #If (gold!>50) { #TakeGP(50) #Giveitem("Shield.itm") #TakeGP(50) } #If (gold!<50) { #Delay(1) } } } *********************************** :shop2 #While (shop!==2) {
** #colorRGB(255,255,255) #Text(11,3.5,"Sword 50 GP") #Text(11,5.5,"Shield 50 GP") #colorRGB(255,255,255) #colorRGB(200,0,0) #Text(11,7.5,"Gem 500 GP") #colorRGB(255,255,255) #Text(11,12.5,"Leave") #Wait(a$)
** #If (a$=="UP") { #shop!==1 #Branch(:shop1) }
** #If (a$=="DOWN") { #shop!==3 #Branch(:shop3) }
** #If (a$=="ENTER") { #If (gold!<1000) { #Delay(1) } #If (gold!>1000) { #Giveitem("gem.itm") #TakeGP(1000) } } } ******************************** :shop3 #While (shop!==3) {
** #Text(11,3.5,"Sword 50 GP") #Text(11,5.5,"Shield 50 GP") #Text(11,7.5,"Gem 500 GP") #colorRGB(200,0,0) #Text(11,12.5,"Leave") #Wait(a$)
** #If (a$=="UP") { #shop!==2 #Branch(:shop2) }
** #If (a$=="DOWN") { #shop!==0 #Branch(:shop0) }
** #If (a$=="ENTER") { #colorrgb(255,255,255) #Text(13.5,13.5, "Come back anytime!") #delay(1) #Clearbuffer() #shop!==4 } }
First copy and paste everything (first clear the program editor) and test it to see what it does. It doesn't gives you any items since it's only a test and you probably don't have those items in the item folder. About the last command; if you press enter there it would bring up the text "Come back anytime!". This is easy to understand. Then it would delay for 1 second, also easy. The #clearbuffer() clears the keyboard buffer. Sometimes the internal keyboard buffer gets full and continues to 'type' even after the player has finished pressing any buttons. This command wipes the buffer clean to prevent this (BTW copied and pasted this from help-file). Anyways, this is what might confuse you, the variable. If you have a program with commands and you want to program to end, you could send it to a command with an in it, or just give it a variable that no command has. Then it would automatically just quit, because it doesn't knows what to do. It don't think that one of these ways is "better" to do but the one I choose is easier. And last, you see that I've putted those * in it, this is just to make it more readable. You can put those anywhere you want because the program doesn't reads those things. It's just to make the program look easier for your eyes. Delete those things and then read the code again, you'll see what I mean. I also added quite a lot empty sentences in it, also to make it easier readable. **#while()** **#shop!==4** **#while()** **#while()** **#end()** **#while()**
