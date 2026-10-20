---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/tip.php"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://mysticsoftware.net/tip.php"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040506134636"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/tip.php", captured: "20040506134636", sha256: "c398a79c858f530f934770f237755dde43974ee58a3086f56e1b746a9b9cc1dd", wayback_url: "https://web.archive.org/web/20040506134636/http://mysticsoftware.net/tip.php"}
---

# Mystic Software

Tip du Jour
Have a RPG Code tip? . **- Tip du Jour:**Email Xorlak
Multi-dimensional arrays are a very "mysterious" concept for those of you have have solely programmed with RPGCode. Whether you've used them or not, however, you can quickly see how they might be useful. Take a look at this (surreal) battle system's variables: **KSNiloc Says:**
#Enemy[health]! #Enemy[fight]! ...
What if we want more than one enemy? Many people were either so stumped that they just left their battlesystem having one enemy or adapted like this:
#Enemy1[health]! #Enemy2[health]! ...
The only problem with that is the ease at which it can be used with for loops. Not very eaisly. I counteract this by using the all-mighty #RPGCode command.
---RPGCode(commmand$)
This command simply runs the command passed to it. CBM was originally planning on using this solely for debugginf purposes but soon enough he soon its potential usefulness and left it in.
Here is how we can use it to simulate multi-d arrays:
#Method SetMultiDLit(name$,para1!,para2!,data$) { #CastLit(para1!,a$) #CastLit(para2!,b$) #temp$="#" + name$ + "_MD_" + a$ + "_MD_" + b$ + " = data$" #RPGCode(temp$) }
#Method GetMultiDLit(name$,para!,para2!,dest$) { #CastLit(para1!,a$) #CastLit(para2!,b$) #temp$="#dest$ = " + name$ + "_MD_" + a$ + "_MD_" + b$ #RPGCode(temp$) }
That is how you would do a multi-d array. These work rather nicely. Look at this example:
*Assuming the methods are avaliable for use...
*Pretend declarations... *MDArray SomethingArray(2)(2)
*Populate the array... #for(a2!=0;a2!<=2;a2!=a2!+1) { #for(b2!=0;b2!<=2;b2!=b2!+1) { #Prompt("Enter something:",temp$) #SetMultiDLit(SomethingArray,a2!,b2!,temp$) } }
*Spit out the stuff... #for(a2!=0;a2!<=2;a2!=a2!+1) { #for(b2!=0;b2!<=2;b2!=b2!+1) { #GetMultiDLit(SomethingArray,a2!,b2!,dest$) #MWin("Para , = ") #system.pause() #MWinCls() } }
Thank you for reading KSNiloc's "Tip du Jour". Stay tuned for the next episode, "Stacks".
I really couldn't think of anything groundbreaking, so I thought I'd share one of my old graphical tricks that just makes your game's overall sexy level a little higher. This quick how-to will show you how to give your buttons sound and have a "click" appearance when you press them. It's pretty easy to do. In this example, I'll have a single button (load.jpg). Since I'm too lazy to make another varation that makes it look like it were clicked, I'll simply set another translucent instance of it over the original.: **Nick Says:**
#setbutton("load.jpg",1,10,10,100,25) #while(done!==0) { #mouseclick(x!,y!) #checkbutton(x!,y!,num!) #if(num!==1) { #done!==1 #setimageadditive("load.jpg",10,10,100,25,50) #delay(0.1) #setimage("load.jpg",10,10,100,25) #Mwin("You pressed the 'Load' button. You're special!") #wait } } Basically, that waits for the player to click the button (if they don't, it just waits again), and when they do, says "You pressed the 'Load' button. You're special!" in the Message Window. But when you click it, it flashes a lighter color, making it look spiffeh. However, you'll probably want to make the button look like it's pressed in. This is similar to how the bevel on Windows' buttons invert when you click them. So if you want to do this, use basically the same code. Only this time, you set a different image for the "clicked" appearance. #setbutton("load.jpg",1,10,10,100,25) #while(done!==0) { #mouseclick(x!,y!) #checkbutton(x!,y!,num!) #if(num!==1) { #done!==1 #setimage("load_clicked.jpg",10,10,100,25,50) #delay(0.1) #setimage("load.jpg",10,10,100,25) #Mwin("You pressed the 'Load' button. You're special!") #wait } }
-Stalfy Says: This lovely little code comes from entrepeneur and hardware master Nick, who also happens to be a forum mod, so be nice to him =P.
Let's say you're making a custom menu or some other custom goodie, and you want to do something for every player, but you wanna make sure that the player is there first. Use a crazy cool #For loop to do it all: **Dissy Says:**
#For(player!=0; player!<5; player!=player!+1) { #if(playerhandle[player!]$~="") { *do crazy things envolving said player } }
-MrG Says: This tip comes from one of the artful masters of procrastination and general whining as well as the author of one of the cool new upcoming games in the community that may or may not be eventually released.
Look out behind you! It's an invisible button! Just kidding. Now when you go to make buttons that blend into the background, dont you find it a bit irritating when matching the background to the button pic? It would be so much easier if you could just make the background pic with the buttons on it, and then make an invisible button over it! Is that possible? You bet. Check this out: **Jer1400 Says:**
#setbutton("",1,500,20,600,50)
That's it! If you just put ""'s in place of where the filename of a picture is supposed to be it will work just like a button, only it will be invisible so you can see right through it! So go ahead and make those fancy buttons that blur into the abyss! And remember, don't eat rotten meat! :)
Here is a tip that will help with custom menus. Usually, it will look like this when you program the player's stat display: **Jer1400 Says Again:**
*Player 1 #pic1$=playerhandle[0]$+".bmp" #setimage(pic1$,10,10,100,100) #drawtext(10,115,playerhandle[0]$) #gethp(playerhandle[0]$,hp1!) #getmaxhp(playerhandle[0]$,maxhp1!) #drawtext(10,125,"HP:/") *Player 2 #pic2$=playerhandle[1]$+".bmp" #setimage(pic2$,10,130,100,100) #drawtext(10,245,playerhandle[1]$) #gethp(playerhandle[1]$,hp2!) #getmaxhp(playerhandle[1]$,maxhp2!) #drawtext(10,255,"HP: /)
Well, that's not too neat looking, is it? What you can do is (no, this isn't the same as Dissy's, keep reading) make a global y variable and then change it by a certain amount each time you want to put up another player's stats. Then have every other y variable correspond to the global one. Let me show you...
#globaly!=-120 #for(num!=0; num!<5; num!=num!+1) { #if(playerhandle[num!]$~="") { #globaly!=globaly!+130 #pic$=playerhandle[num!]$+".bmp" #setimage(pic1$,10,globaly!,100,100) #namey!=globaly!+105 #drawtext(10,namey!,playerhandle[num!]$) #gethp(playerhandle[num!]$,hp!) #getmaxhp(playerhandle[num!]$,maxhp!) #hpy!=globaly!+115 #drawtext(10,hpy!,"HP: /) } }
Look at that! It's like another dimension of coding! One without the countless hours of changing x's and y's! One without frustration, annoyance, and slow menus! I had a dream, and it has finally come true! *ehem* Sorry about that, I got a little carried away. As you probably already figured out, this one needs Good Ol' Triuken's plugin to work. And remember, if it was on the ground for less than 10 seconds, it's still good!
-MrG Says: These tips come from one of the up and coming master RPGCoders in our fair community, the winner of the Shack Pong contest, and a kid with really great hair.
Here's a little trick to allow players to skip animation efficiently...I don't know if any of you has ever thought about it, but I though it'd be quite helpful. The trick is to create an animation and to save all the frames with numbers after each of them, like : **Martin Says:**
-Fire1.jpg -Fire2.jpg -Fire3.jpg -Fire4.jpg etc...
It's very easy to do with Animation Shop, just "Save Frames As..." and select the filename type you want. Then all you have to do is to create a little program like this :
[#Method RunAnimation(name$,frames!){}] <- this is not needed, but it works as a method.
#For (x!=1; x!<=frames!; x!=x!+1) { *will run a loop playing the frames 1 after another #key$="" #CastLit(frames!, framenumber$ ) *to be able to use with the filename which is a literal var. #playname$=name$+framenumber$ *just switching from one frame to the next one... #Bitmap(playname$) *shows the frame #Get(key$) *if player hit a key... #If(key$~="") { #x!=frames! *skipping the whole stuff } }
[using the method, a single line does it : #RunAnimation(Fire,4)]
Have fun !
-MrG Says: This tip comes from one of the ancient oldbies in the community, the guy that runs TKGR and its Awards, the best maker of games involving people turning into wolves, and the undispusted heavyweight champion of waffles. He also gave this section its name (tip du jour).
