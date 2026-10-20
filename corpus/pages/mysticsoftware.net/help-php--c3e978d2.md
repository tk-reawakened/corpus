---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/help.php?article=9&mode=1"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://mysticsoftware.net/help.php?mode=1&article=9"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040504142651"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/help.php__mode_1_article_9", captured: "20040504142651", sha256: "1d8a7c5472f338b13c15ec36e656770689f3da37db31d2b7e84f536f2886466f", wayback_url: "https://web.archive.org/web/20040504142651/http://mysticsoftware.net/help.php?mode=1&article=9"}
---

# Mystic Software

Well, I have seen many people request extra players for Battle Systems and the like. Well, I decided to show you just how easy this really is. Well, we could make all of your players a set of variables (which your normal players are anyway). This, however, means we have to define their stats in a text file. Lets make our own file, called... how about players.prg: #method defplayers() { ********* Flamp *********** #setstat("Flamp","HP",12) #setstat("Flamp","DP",12) #setstat("Flamp","FP",12) #setstat("Flamp","SMP",12) #setstat("Flamp","Speed",12) ********* Dandrif ********** #setstat("Dandrif","HP",22) #setstat("Dandrif","DP",22) #setstat("Dandrif","FP",22) #setstat("Dandrif","SMP",22) #setstat("Dandrif","Speed",22) } This methods create 2 players, Flamp and Dandrif. It uses my custom stat proggie, available at the shack. Call this in your start program, and these players are created. Remember, only call this method ONCE, or it will reset all of your characters. Now, to access these commands, use #getstat, #givestat, and #setstat wherever you want, just as you would a normal character. Remember, you dont have to use these stats - you could use any you like, such as "Instinct" or "Knowledge". Now, lets make some new methods for switching these players in. #method switchplayer(num!,player$) { #playername[num!]$=player$ } #method getplayer(num!,playerreturn$) { #playerreturn$=playername[num!]$ #returnmethod(playerreturn$) } #method removeplayer(num!) { #kill(playername[num!]$) } These are quite simple methods. num! is the number to set the player. For example, lets say you wanted to change player 1 to Flamp, then player 2 to Dandrif: #switchplayer(1,"Flamp") #switchplayer(2,"Dandfrif") Now, lets say, in another program, you want to change player 1 to Dandrif, and get rid of player 2: #switchplayer(1,"Dandrif") #removeplayer(2) Also, you need some way to set the graphics of a character. Maybe, you want, in your battle system, to just have 3 fighting graphics (1 of them standing still, 2 of them actually fighting). Well, we could put all of the graphics into one file, plyrsattack.tst. Then, add your graphics, in the order that you want them. So, maybe we want Flamp first, then Dandrif. We add these stats: #setstat("Flamp","Fightorder",1) #setstat("Dandrif","Fightorder",4) Well, that shows what tile the characters start on. Flamp is the first tile in the tileset, and Dandrif is the 4th. Now, if we want the first frame of the character: #getstat("Flamp","Fightorder",fighttile!) #castlit(fighttile!,fighttile$) #tile$="plyrsattack.tst"+fighttile$ #put(10,10,tile$) That puts down the first tile you put in the tileset for that character. Lets say you want the second: #getstat("Flamp","Fightorder",fighttile!) #fighttile!=fighttile!+1 #castlit(fighttile!,fighttile$) #tile$="plyrsattack.tst"+fighttile$ #put(10,10,tile$) Well, thats it. Add this into your battle system, and you are all set! Happy mass-player usage! -Dont_Think_So
- Extra Battle System Characters - Written By Dont_Think_So
