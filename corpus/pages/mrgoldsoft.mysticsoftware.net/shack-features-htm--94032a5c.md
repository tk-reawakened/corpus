---
kind: page
id: "mrgoldsoft.mysticsoftware.net/mrgoldsoft.mysticsoftware.net/shack/features.htm"
site: "mrgoldsoft.mysticsoftware.net"
title: "Dissy Says :"
original_url: "http://mrgoldsoft.mysticsoftware.net/shack/features.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20021005124112"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/mrgoldsoft.mysticsoftware.net/shack/features.htm", captured: "20021005124112", sha256: "225dcb40611141e473d9b4d1b1549ccaabbbf6343340dbf817b96e5a3cb4a610", wayback_url: "https://web.archive.org/web/20021005124112/http://mrgoldsoft.mysticsoftware.net/shack/features.htm"}
---

# Dissy Says :

- Flippin Fabulous Features -
![](features.gif)
Click on the names of features above to navigate
- Gallery: This is just a small, neat little section that lets you showcase the cool aspects of your game that are done in RPGCode, like systems, mini-games, or cool sequences.
[![](goldenrod.gif)](gallery/4d.png) - [Mystical Quest Rain](gallery/mqrain.jpg) Author: Mike D
[![](goldenrod.gif)](gallery/4d.png) - [Firaxia Menu Sytem](gallery/zephmenu.gif) Author: Zepher
[![](goldenrod.gif)](gallery/4d.png) - [Chrono Crystals](gallery/CC_BS.png) Author: Jer1400
[![](goldenrod.gif)](gallery/4d.png) - [Gaiden Warriors](gallery/GW_BS.png) Author: Jer1400
[![](goldenrod.gif)](gallery/4d.png) - [Tre Menu System](gallery/tremenu.png) Author: Suro
[![](goldenrod.gif)](gallery/4d.png) - [Darq's Paint Program](gallery/Paint.png) Author: Darq
[![](goldenrod.gif)](gallery/4d.png) - [Pests's Shop System](gallery/Ss2.png) Author: Pests
[![](goldenrod.gif)](gallery/4d.png) - [Emerald's Menu System](gallery/emeraldmenu.gif) Author: Emerald
[![](goldenrod.gif)](gallery/4d.png) - [FFTactics Menu System](gallery/bp_screenshot.jpg) Author: BP
[![](goldenrod.gif)](gallery/4d.png) - [New Fourth Dimension Menu](gallery/4d2.png) Author: Rueben
- Tip du Jour: The aptly named Tip of the Day that comes out every week or so. We pester cool RPGCoders and ask them to give us their favorite tip. It's kind of ridiculous. But really fun. Let's say you're making a custom menu or some other custom goodie, and you want to do something for every player, but you wanna make sure that the player is there first. Use a crazy cool #For loop to do it all: #For(player!=0; player! < 5; player!=player!+1) { #if(playerhandle[player!]$~="") { *do crazy things envolving said player } }
***Dissy Says :***
-MrG Says: This tip comes from one of the artful masters of procrastination and general whining as well as the author of one of the cool new upcoming games in the community that may or may not be eventually released.![](silverrod.gif)
Look out behind you! It's an invisible button! Just kidding. Now when you go to make buttons that blend into the background, dont you find it a bit irritating when matching the background to the button pic? It would be so much easier if you could just make the background pic with the buttons on it, and then make an invisible button over it! Is that possible? You bet. Check this out: #setbutton("",1,500,20,600,50) That's it! If you just put ""'s in place of where the filename of a picture is supposed to be it will work just like a button, only it will be invisible so you can see right through it! So go ahead and make those fancy buttons that blur into the abyss! And remember, don't eat rotten meat! :) ***Jer1400 Says :***
Here is a tip that will help with custom menus. Usually, it will look like this when you program the player's stat display: *Player 1 #pic1$=playerhandle[0]$+".bmp" #setimage(pic1$,10,10,100,100) #drawtext(10,115,playerhandle[0]$) #gethp(playerhandle[0]$,hp1!) #getmaxhp(playerhandle[0]$,maxhp1!) #drawtext(10,125,"HP:/") *Player 2 #pic2$=playerhandle[1]$+".bmp" #setimage(pic2$,10,130,100,100) #drawtext(10,245,playerhandle[1]$) #gethp(playerhandle[1]$,hp2!) #getmaxhp(playerhandle[1]$,maxhp2!) #drawtext(10,255,"HP: /) Well, that's not too neat looking, is it? What you can do is (no, this isn't the same as Dissy's, keep reading) make a global y variable and then change it by a certain amount each time you want to put up another player's stats. Then have every other y variable correspond to the global one. Let me show you... #globaly!=-120 #for(num!=0; num! < 5; num!=num!+1) { #if(playerhandle[num!]$~="") { #globaly!=globaly!+130 #pic$=playerhandle[num!]$+".bmp" #setimage(pic1$,10,globaly!,100,100) #namey!=globaly!+105 #drawtext(10,namey!,playerhandle[num!]$) #gethp(playerhandle[num!]$,hp!) #getmaxhp(playerhandle[num!]$,maxhp!) #hpy!=globaly!+115 #drawtext(10,hpy!,"HP: /) } } Look at that! It's like another dimension of coding! One without the countless hours of changing x's and y's! One without frustration, annoyance, and slow menus! I had a dream, and it has finally come true! *ehem* Sorry about that, I got a little carried away. As you probably already figured out, this one needs Good Ol' Triukin's plugin to work. And remember, if it was on the ground for less than 10 seconds, it's still good! ***Jer1400 Says Again :***
-MrG Says: These tips come from one of the up and coming master RPGCoders in our fair community, the winner of the Shack Pong contest, and a kid with really great hair.![](silverrod.gif)
- RPGCode Challenge:
This is a little section that challenges that RPGCode astuteness in you, because, as odd as it may seem, we are an RPGCode site. Every time we feel like updating it, we'll have a small RPGCode challenge. Everything in this challenge must be done in pure RPGCode with no outside graphics or plugins. Once this challenge has run for about a week or so, we'll pick a winner. To apply, simply send an email to MrG@mysticsoftware.net with the subject line "RPGCode Challenge." It really couldn't be simpler. Oh yeah. If you win you get to use that thing above us. And who woudln't want to put that on their site?
*
*Click Above to View Results*
*Click Above to View Results*
