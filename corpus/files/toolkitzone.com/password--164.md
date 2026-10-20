---
kind: file
id: "toolkitzone.com/164"
site: "toolkitzone.com"
title: "password"
original_url: "http://www.toolkitzone.com/fileman.php?id=10&file=164"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040622151243", "20040706142014", "20040706142014", "20040706142014", "20040706142545", "20040706142545", "20040706142545", "20060612031224", "20060612031224"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_164", captured: "20040622151243", sha256: "2a870d37287bb9ae06d602e8db1cf333b2d681cd9e43901b15ccf3b1a34fd7b9", wayback_url: "https://web.archive.org/web/20040622151243/http://toolkitzone.com/fileman.php?id=3&file=164"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_164", captured: "20040706142014", sha256: "3300a02298a2b2f967f279a9abe4c2174e7c9881de33ce2dfef93740c33e5120", wayback_url: "https://web.archive.org/web/20040706142014/http://toolkitzone.com/fileman.php?id=10&file=164"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_164-2f80a4", captured: "20040706142014", sha256: "3300a02298a2b2f967f279a9abe4c2174e7c9881de33ce2dfef93740c33e5120", wayback_url: "https://web.archive.org/web/20040706142014/http://toolkitzone.com/fileman.php?id=10&file=164"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_164-5d1058", captured: "20040706142014", sha256: "3300a02298a2b2f967f279a9abe4c2174e7c9881de33ce2dfef93740c33e5120", wayback_url: "https://web.archive.org/web/20040706142014/http://www.toolkitzone.com/fileman.php?id=10&file=164"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_164", captured: "20040706142545", sha256: "fc1c1f7baa76a199f9416771b875994179e0a407b62e5570ff2c64731cf6aafb", wayback_url: "https://web.archive.org/web/20040706142545/http://toolkitzone.com/fileman.php?id=5&file=164"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_164-c523cb", captured: "20040706142545", sha256: "fc1c1f7baa76a199f9416771b875994179e0a407b62e5570ff2c64731cf6aafb", wayback_url: "https://web.archive.org/web/20040706142545/http://www.toolkitzone.com/fileman.php?id=5&file=164"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_164-c7f383", captured: "20040706142545", sha256: "fc1c1f7baa76a199f9416771b875994179e0a407b62e5570ff2c64731cf6aafb", wayback_url: "https://web.archive.org/web/20040706142545/http://toolkitzone.com/fileman.php?id=5&file=164"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_164-056e7c", captured: "20060612031224", sha256: "80881d495f21ab260c23c94523734539f999c3330efeee54292f551f01140d6f", wayback_url: "https://web.archive.org/web/20060612031224/http://www.toolkitzone.com/fileman.php?id=3&file=164"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_164-6859e6", captured: "20060612031224", sha256: "80881d495f21ab260c23c94523734539f999c3330efeee54292f551f01140d6f", wayback_url: "https://web.archive.org/web/20060612031224/http://toolkitzone.com/fileman.php?id=3&file=164"}
---

# password

beta version - report any problems to (redacted: email)
Rpg Code tutorial
In this tutorial I will show you how to make a custom menu system. There are many ways to make a menu system, and there are many different menu systems, but in this tutorial I will show you how to make one of the easiest menu systems. Here are the things available in the menu:
Characters Status Abilities Equipment Items Load Save Continue Quit
At first, here are the commands that we are gonna use:
** #bitmap() #setbutton() #if() #internalmenu() #while() #mouseclick() #checkbutton() #dirsav() #load() #end() #save() #clearbuttons() #mwin() #delay() #mwin() #wait() #windows() #mwincls() #branch() #gethp() #getmaxhp() #getsmp() #getmaxsmp() #getfp() #getdp() #text() #setimage() @
Quite some commands, but don't worry, most of them we will only use once or twice. Also, we will use quite some variables here to show how much HP, SMP etc a player has. If you are not so sure about how to work with variables, check the toolkit helpfile. (Help-->RpgCode Introduction) For the commands you don't know, check the other helpfile in toolkit. (Help-->RpgCode Command Reference)
At first, let us start with setting up the background for the menu:
**#bitmap("back.gif")**
Nothing not to understand about this I think. Now we put some variables in it to make the a bit easier: **#setbutton()**
** #xtop!=450 #width!=150 #height!=50
The xtop!, width and height will always be the same (if you put the buttons under each other that is). So that way we can just use text in the commands, I will show them first and then explain further: **#setbutton()**
** #setbutton("status.gif", 0, xtop!, 10, width!, height!) #setbutton("abilities.gif", 1, xtop!, 65, width!, height!) #setbutton("equipment.gif", 2, xtop!, 120, width!, height!) #setbutton("items.gif", 3, xtop!, 175, width!, height!) #setbutton("load.gif", 4, xtop!, 230, width!, height!) #setbutton("save.gif", 5, xtop!, 285, width!, height!) #setbutton("continue.gif", 6, xtop!, 340, width!, height!) #setbutton("quit.gif", 7, xtop!, 395, width!, height!)
As you can see, I use xtop!, width! and height! in them. If you are putting your buttons in the menu, and you put them in the wrong place, you would have to change all the 8 buttons after each other, which takes a long time. Now, we can just change only the variable that you've set before, which is much easier. The reason that I haven't made a variable for #y!, is because that one is different each time. Good, now we put in the player statuses. You can make those in another program, but I'll just do them in the same program:
** #GetHP(playerHandle[0]$,Hp!) #GetMaxHp(playerHandle[0]$,MaxHp!) #GetSMP(playerHandle[0]$,SMP!) #GetMaxSMP(playerHandle[0]$,MaxSMP!) #Text(11,1.5,"Name: ") #Text(11,2.5,"HP:/") #Text(11,3.5,"SMP:/")
** #GetHP(playerHandle[1]$,Hp1!) #GetMaxHp(playerHandle[1]$,MaxHp1!) #GetSMP(playerHandle[1]$,SMP1!) #GetMaxSMP(playerHandle[1]$,MaxSMP1!) #Text(11,7.5,"Name: ") #Text(11,8.5,"HP:/") #Text(11,9.5,"SP:/")
** #GetHP(playerHandle[2]$,Hp2!) #GetMaxHp(playerHandle[2]$,MaxHp2!) #GetSMP(playerHandle[2]$,SMP2!) #GetMaxSMP(playerHandle[2]$,MaxSMP2!) #Text(11,12.5,"Name: ") #Text(11,13.5,"HP:/") #Text(11,14.5,"SP:/")
** #GetHP(playerHandle[3]$,Hp3!) #GetMaxHp(playerHandle[3]$,MaxHp3!) #GetSMP(playerHandle[3]$,SMP3!) #GetMaxSMP(playerHandle[3]$,MaxSMP3!) #Text(11,17.5,"Name: ") #Text(11,18.5,"HP: /") #Text(11,19.5,"SP:/")
** #GetHP(playerHandle[4]$,Hp4!) #GetMaxHp(playerHandle[4]$,MaxHp4!) #GetSMP(playerHandle[4]$,SMP4!) #GetMaxSMP(playerHandle[4]$,MaxSMP4!) #Text(11,22.5,"Name: ") #Text(11,23.5,"HP:/") #Text(11,24.5,"SP:/")
Quite some text as you can see. They are all the same actually, except for one difference that they are all for another player. The first 4 commands are for the variables. In the last commands are to show that variables. You may have seen that there are 4 commands, but that the commands shows 5 different variables. The "name" variable doesn't needs to be "gotten" by some command. This is called a Reserved Variable. You can see them in the bottom of the Rpg-Code Introduction helpfile. **#get()** **#text()** **#get()** **#text()** **#get()**
Now we are gonna show the profile pictures, you do this with the command: **#setimage()**
** #setimage("profile1.gif",10,10,100,100) #setimage("profile2.gif",10,110,100,100) #setimage("profile3.gif",10,220,100,100) #setimage("profile4.gif",10,330,100,100) #setimage("profile5.gif",10,440,100,100)
You could have used variables here again like in the commands, but I didn't have much trouble with putting the pictures in the right place. Now you should put in this command: **#setbutton()**
**:top**
I'll tell you later what this is for. You probably know that it has something to do with the command. Now we are going to let the program know what it should do when you press a button, we start with this: **#branch()**
** #done!=0 #while(done!==0) { #MouseClick(x!,y!) #CheckButton(x!,y!,button!)
**This checks where you click the mouse. Now, here is the first button:**
** #if (button!==0) { #internalmenu(3) }
Very easy. Just a simple command and after that a simple command. If you don't know what the command does, check the help files in toolkit. This number 3 is for the player statuses. The abilities, equipment and items can also be done with the command: **#if()** **#internalmenu()** **#internalmenu()** **#internalmenu()**
** #if (button!==1) { #internalmenu(4) }
** #if (button!==2) { #internalmenu(2) }
** #if (button!==3) { #internalmenu(1)
Nothing not to understand I think. Now comes a harder part, the load button. Here is the command:
** #if (button!==4) { #dirsav(dest$) #if(dest$~="CANCEL") { #load(dest$) #done!=1 #end } }
The command is so that it goes to the load menu (which is just a boring windows screen). In the command you see a ~= thingy. This means "is not equal to". So if you choose something different then "cancel", it loads ( ) the file you have chosen. Simple, not? Now the save command, which looks just like the load command: **#dirsav()** **#if()** **#load()**
** #if (button!==5) { #dirsav(dest$) #if(dest$~="CANCEL") { #save(dest$) #done!=1 #end } }
It's the same as the load command, only now it saves ( ) instead of loads ( ) something. Now for the "continue" button: **#save()** **#load()**
** #if (button!==6) { #clearbuttons() #done!=1 }
Because and not 0 anymore, it goes out of the while command that it's in, so the program stops and you go back to your game. Now for the "quit" button: **#done!=1**
** #if (button!==7) { #mwin("Do you really want to quit? Don't forget to save!") #delay(0.5) @ #mwin("1 - Yes") #mwin("2 - No") #wait(answer!) #if (answer!==1) { #windows() }
** #if (answer!==2) { #mwincls() #branch(:top) } } }
As you can see there are some commands in this. The program first asks if you really want to quit. If you do want to quit, it goes to the command, which let's you go back to windows, and if you do not want to quit, it goes to the branch command. This is the command we saw earlier. It brings you back up again so you can press everything again. There are other ways for it, but I do it like this. **#if()** **#windows()**
This is how you put a self-made menu in your game. First you go to "edit main file". Then to "Rpg-Code". Under "programs" you can see the "run time program". Place you menu program here. Under that you see "action keys". The second one (built in menu activation key) is for the built in menu. You see that you have to press enter for it. Click in the place where it says "enter" and press DELETE. Now click in the one above it and press enter. Now save your main file and test your game. It should show you your self-made menu. Here is the full menu:
**#bitmap("Back.gif")**
** #xtop!=450 #width!=150 #height!=50
** #setbutton("status.gif", 0, xtop!, 10, width!, height!) #setbutton("abilities.gif", 1, xtop!, 65, width!, height!) #setbutton("equipment.gif", 2, xtop!, 120, width!, height!) #setbutton("items.gif", 3, xtop!, 175, width!, height!) #setbutton("load.gif", 4, xtop!, 230, width!, height!) #setbutton("save.gif", 5, xtop!, 285, width!, height!) #setbutton("continue.gif", 6, xtop!, 340, width!, height!) #setbutton("quit.gif", 7, xtop!, 395, width!, height!)
** #GetHP(playerHandle[0]$,Hp!) #GetMaxHp(playerHandle[0]$,MaxHp!) #GetSMP(playerHandle[0]$,SMP!) #GetMaxSMP(playerHandle[0]$,MaxSMP!) #Text(11,1.5,"Name: ") #Text(11,2.5,"HP:/") #Text(11,3.5,"SMP:/")
** #GetHP(playerHandle[1]$,Hp1!) #GetMaxHp(playerHandle[1]$,MaxHp1!) #GetSMP(playerHandle[1]$,SMP1!) #GetMaxSMP(playerHandle[1]$,MaxSMP1!) #Text(11,7.5,"Name: ") #Text(11,8.5,"HP:/") #Text(11,9.5,"SP:/")
** #GetHP(playerHandle[2]$,Hp2!) #GetMaxHp(playerHandle[2]$,MaxHp2!) #GetSMP(playerHandle[2]$,SMP2!) #GetMaxSMP(playerHandle[2]$,MaxSMP2!) #Text(11,12.5,"Name: ") #Text(11,13.5,"HP:/") #Text(11,14.5,"SP:/")
** #GetHP(playerHandle[3]$,Hp3!) #GetMaxHp(playerHandle[3]$,MaxHp3!) #GetSMP(playerHandle[3]$,SMP3!) #GetMaxSMP(playerHandle[3]$,MaxSMP3!) #Text(11,17.5,"Name: ") #Text(11,18.5,"HP: /") #Text(11,19.5,"SP:/")
** #GetHP(playerHandle[4]$,Hp4!) #GetMaxHp(playerHandle[4]$,MaxHp4!) #GetSMP(playerHandle[4]$,SMP4!) #GetMaxSMP(playerHandle[4]$,MaxSMP4!) #Text(11,22.5,"Name: ") #Text(11,23.5,"HP:/") #Text(11,24.5,"SP:/")
** #setimage("profile1.gif",10,10,100,100) #setimage("profile2.gif",10,110,100,100) #setimage("profile3.gif",10,220,100,100) #setimage("profile4.gif",10,330,100,100) #setimage("profile5.gif",10,440,100,100)
**:top**
** #done!=0 #while(done!==0) { #MouseClick(x!,y!) #CheckButton(x!,y!,button!)
** #if (button!==0) { #internalmenu(3) }
** #if (button!==1) { #internalmenu(4) }
** #if (button!==2) { #internalmenu(2) }
** #if (button!==3) { #internalmenu(1) }
** #if (button!==4) { #dirsav(dest$) #if(dest$~="CANCEL") { #load(dest$) #done!=1 #end } }
** #if (button!==5) { #dirsav(dest$) #if(dest$~="CANCEL") { #save(dest$) #done!=1 #end } }
** #if (button!==6) { #clearbuttons() #done!=1 }
** #if (button!==7) { #mwin("Do you really want to quit? Don't forget to save!") #delay(0.5) @ #mwin("1 - Yes") #mwin("2 - No") #wait(answer!) #if (answer!==1) { #windows() }
** #if (answer!==2) { #mwincls() #branch(:top) } } }
It's best to look at the menu again and see if there's anything you don't understand. If there's something you don't understand, scroll up again to check what it means, or if I didn't tell what it means (or not good enough) just ask it.
As last, there are many different menu styles. This is the easiest way to make a menu (IMO anyway). If you want to make you game look more custom, you can use this tutorial as a guide, but it's best to make your own menu. This tutorial is just to show you the basics of making a menu. You can add more things to your own, like a cheat menu, or you can make a different style, like cursor based, it's your call. Happy coding!
