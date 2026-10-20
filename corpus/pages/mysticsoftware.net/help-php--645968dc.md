---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/help.php?article=11&mode=1"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://mysticsoftware.net/help.php?mode=1&article=11"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040504142342"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/help.php__mode_1_article_11", captured: "20040504142342", sha256: "51bf553add1dbe1d41415aae868e1d021be404f1b0891425bd695a037c52a05c", wayback_url: "https://web.archive.org/web/20040504142342/http://mysticsoftware.net/help.php?mode=1&article=11"}
---

# Mystic Software

*********Graphical Rpg Code Tutorial****** **********Created by Stalfospk********** I. Introduction II. Changing Colors A. Variables B. Effects III. Changing text colors A. commands B. Guide IV. drawrect,fillrect,drawcircle,fillcircle,drawline V. Closing words I. Introduction Welcome friend. The reason you're reading this is either to learn about graphical rpg code, or because you have no life. Either way, I hope you enjoy it. In this tutorial, you'll learn about rpg code and the graphical capabilities of it (that was hard to figure out). II. Changing Colors Let's start with some basics, changing colors and shades in rpg code. Here are the variables for the shades of color: ambientred! ambientblue! ambientgreen! They control the amount of the certain color on the screen. Now, we can go onto changing these for your benefit... Say you want to have a town on fire or something, so you want to give the screen a tint of red. All you'd have to do is: #ambientred!=ambientred!+100 Of course, change the 100 to however red you want it, the larger, the redder it gets. Now, to make a better effect, add this to it: #ambientblue!=ambientblue!-100 #ambientgreen!=ambientgreen!-100 Also, when you want to change them back, just do this: #AmbientRed!=AmbientRed!-100 #AmbientGreen!=AmbientGreen!+100 #ambientblue!=ambientblue!+100 I hope that helped you with shading colors. III. Changing Text colors To change the color of text made form the #text command, just type #color(color!) before the #text command. Replace color! with a number from 1-15. Any number after 15 will show up black. Now, here's a list of the colors for you: 1=blue 2=green 3=teel 4=red 5=purple 6=brown 7=grey 8=dark grey 9=light blue 10=light green 11=very light blue 12=light red 13=pink 14=yellow 15=white 16+=black There, now you won't have to experiment to find the color you're looking for. That should do it for changing text colors... IV. The Draw commands So far, you've learned the basics of colors,etc., but here's where the real graphical programming is. I'll introduce 5 commands to you and teach you how to use them: #drawrect(x1!,y1!,x2!,y2!) This command draws a rectangle from the the variables you give it. It uses the current color that is being used. To change this, just use the #color command you learned earlier. #fillrect(x1!,y1!,x2!,y2!) This command does the same as #drawrect, but it fills in the rectangle with the current color. #drawline(x1!,y1!,x2!,y2!) I think you can figure out what this does #DrawCircle(x!,y!,radius![, startangle!, endangle!]) This draws a circle like #drawrect draws a rectangle. The last two variables in it are optional. #FillCircle( x!, y!, radius!) Does what #fillrect does,but with a circle. Those commands are very helpful if you're "artistically challenged" like I am... That does it for those commands... V. Closing statements Well, I hope this short tutorial helps you understand the basics of graphical rpg code. If you have any questions or comments, just mail me at: (redacted: email). Good luck!
