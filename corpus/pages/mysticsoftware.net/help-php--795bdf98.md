---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/help.php?article=6&mode=1"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/help.php?mode=1&article=6"
written: null
date_confidence: "unknown"
updated: null
captured: ["20041106232832"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/help.php__mode_1_article_6", captured: "20041106232832", sha256: "98af5967ad4a9c670e6bfcca3ca066ca736fac3156fe5995f2e0babc47fbdcf3", wayback_url: "https://web.archive.org/web/20041106232832/http://www.mysticsoftware.net/help.php?mode=1&article=6"}
---

# Mystic Software

The first release of what I hope to be a looooooong series is complete. I'll fill you in on what is here. --New Documented Variables-- _-Gametime-_ _-Playerx[x!]!-_ _-Playery[x!]!-_ _-PlayerLayer[x!]!-_ _-Constant[x!]!-_ _-BoardSkill!-_ _-AmbientRed!-_ _-AmbientGreen!-_ _-AmbientBlue!-_ _-Music$_- _-Playerhandle[x!]$_- _-BoardTitle[x!]$_- _-BoardBackground$_- *--->Returned Variables < ---* ._-=/' Numrical '\=-_. 1. Gametime! *Time in seconds. Must use #castint because it returns decimals. 2. Playerx[0]! *X coord of player #0. 3. Playery[0]! *Y coord of player #0. 4. PlayerLayer[0] * Current layer player #0 is on. **Returned variables 2-4 can be used to find the same information for the rest **of the player in your party. Use them in the same fashion as above, except **replace 0 with the player's # you want the information for. Using a method **would help make this task easier. Try this: #method getplayerspots() { #for(num!=0; num! < 5; num!=num!+1) { #X[num!]!=playerx[num!]! #Y[num!]!=playery[num!]! #layer[num!]!=playerlayer[num!]! } } **Use that just to shorten it up a bit. 5. Constant[1]! *Value of constant #1 set by you in board editor. **In all there are 10 constant variables that are always the same and can be **edited by you in the board editor. All of them are set up in the same **fashion as the one shown above. Just put 1-10 in place of the #01. Like **this: #for(c!=1; c! < 11; c!=c!+1) { #show(constant[c!]!) #wait() #mwincls() } **That would show you all of the constants in the message window. 6. Boardskill! *The variable for the enemy skill on the current board. 7. AmbientRed! 8. AmbientGreen! 9. AmbientBlue! **#'s 7-9 specify what color of light shading should be used when boards are **drawn. They can contain #'s between -255 & 255. The normal shade of **light is used when all of these reserved variables are equal to 0. By using **these you can make day / night programs with very little hassle. **Day** #for(l!=-80; l! < 1; l!=l!+10) { #AmbientRed!=l! #AmbientGreen!=l! #AmbientBlue!=l! #forceredraw() } **Night** #for(l!=0; l!>90; l!=l!-10) { #AmbientRed!=l! #AmbientGreen!=l! #AmbientBlue!=l! #forceredraw() } ._-=/' Literal '\=-_. 1. Music$ *The currently playing music. 2. Playerhandle[0]$ *The name of player #0. **#2 is used as the variable for the names of the rest of the players also. **Just replace the #0 with the number of the player that you want the name **of. Here is a method that would help make the variable shorter: #for(n!=0; n! < 5; n!=n!+1) { #name[n!]$=playerhandle[n!]$ } **The names are returned in the name[x!]$ variable. This just makes it **easier to remember and use. 3. Boardtitle[x!]$ *The name of the board that the player is currently on. **This is specified by you in the board editor. 4. Boardbackground$ *the file name of the fight background of the board the **player is currently on. --->End < --- If you want to contact me, you can email me at Jer1400@mysticsoftware.net
- Constant Variables - Written By Jer1400 **___Jer1400's___** **____Guide to___** **_Returned Var's_** _-=|[ Version 1.0 ]|=-_ --->History < --- |[ 6-13-02 ]| --Version 1.0--
