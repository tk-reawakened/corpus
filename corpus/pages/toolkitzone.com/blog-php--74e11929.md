---
kind: page
id: "toolkitzone.com/toolkitzone.com/blog.php?mode=view&user=203&view=user"
site: "toolkitzone.com"
title: "User Entries (3)"
original_url: "http://www.toolkitzone.com/blog.php?mode=view&view=user&user=203"
written: "2004-01-28"
date_confidence: "day"
updated: null
captured: ["20051105123608"]
author: "ViperCat"
repliers: []
authors: ["ViperCat"]
comments_present: 0
f_interests: "Making games"
f_joined: "January 28, 2004"
f_username: "ViperCat"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/blog.php__mode_view_view_user_user_203", captured: "20051105123608", sha256: "31380f5f879ca41d800b82205e0910898f4ecbf3e446621a6c7515b0a715acd7", wayback_url: "https://web.archive.org/web/20051105123608/http://www.toolkitzone.com/blog.php?mode=view&view=user&user=203"}
---

# User Entries (3)

02 June, 2004
Well for my first blog in a LONG time I would like to post a scene for my up and coming game,Mythological Chronicles(AKA Myth Chron) Nitrious:What are they Triven? Triven:They are Goldargs. Nitrious:Goldargs?! Triven:Yes.One of the strongest Mythos in the land.Whatever you do,do not touch the horn on their heads.It contains a poison,so deadly,after contact you have five seconds to say your last words. Nitrious:Horn,got it!! *Enters battle* Well, not much but still,something to look at!!
08 May, 2004
*Method Library* **************** *#1-Heal* ********* #Method Heal(handle$,handle2$,handle3$,HP!) } #GiveHP("",HP!) #GiveHP("",HP!) #GiveHP("",HP!) { #Kill(handle$) #Kill(handle2$) #Kill(handle3$) #Kill(HP!) } *************** *#2-Give Items* *************** #Method GiveItems(itm$,itm2$,itm4$,itm5$) } #GiveItem("") #GiveItem("") #GiveItem("") #GiveItem("") #GiveItem("") { #Kill(itm$) #Kill(itm2$) #Kill(itm3$) #Kill(itm4$) #Kill(itm5$) } ****************** *#3-Multiple Wave* ****************** #Method MultiWav(wav1$,wav2$,wav3$) } #Wav("") #Wav("") #Wav("") { #Kill(wav1$) #Kill(wav2$) #Kill(wav3$) } ************* *#4-Pic-Talk* ************* #Method ProTalk(img1$,img2$,img3$,speed!,x!,y!) } #SetImage("",x!,y!) #Delay(speed!) #SetImage("",x!,y!) #Delay(speed!) #SetImage("",x!,y!) { #Kill(img1$) #Kill(img2$) #Kill(img3$) #Kill(speed!) #Kill(x!) #Kill(y!) *************** *#5-Flash Send* *************** #Method FSend(brd$,brd2$,brd3$,x!,y!) } #Send("",x!,y!,1) #Send("",x!,y!,1) #Send("",x!,y!,1) { #Kill(brd$) #Kill(brd2$) #Kill(brd3$) #Kill(x!) #Kill(y!) ******************** *#6-Attack Everyone* ******************** #Method AtkEvryOne(ENEATK!,PlyrATK!) } #AttackAll(ENEATK!) #GiveHP("",-PlyrATK!) **Keep going depending on the number of players in the party** { #Kill(ENEATK!) #Kill(PlyrATK!) } Here is the command reference now!! #Heal Description-#Heal("First Handle","Second Handle","Third Handle",HP!) This program allows you to give the players a certain amount of HP.Leave the second,or third one,or just the third,depending on how many players you want to heal. #GiveItems Description-#GiveItems("itm1$","itm2$","itm3$") Allows you to give multiple items. #MultiWav Description-#MultiWav("wav1","wav2","wav3") This little program makes wavs play back-to-back.This I think would be a good thing for a computer. #ProTalk Description-#ProTalk("img1$","img2$","img3",speed!,x!,y!) This program is useful for many things,mostly talking though.It makes an image appear as if its moving and talking while the #MWin is up.Speed!,is the number of seconds between each picture. #FSend Description-#FSend("brd1$","brd2$",brd3$",x!,y!) If you've ever played 'The Legend of Zelda:Oracle of Seasons',you would see why this would be useful.If the world is changing around you,this program will let you make it seem it's changing. #AtkEvryOne Description-#AtkEvryOne(eneatk!,plyratk!) This command let's you attack every one battling.Eneatk!,is the amount of damage done to the enemy.Plyratk!,is the amount of damage done to the players. Alright that's the finish.But before you close,save the 'MethodLibrary.txt',as a .prg,then every time you're going to use any command from this,at the top of the method you're using put the following(Having MethodLibrary before the extension): Heal - .Heal GiveItems - .GiveItems MultiWav - .MultiWav ProTalk - .ProTalk FSend - .FSend AtkEvryOne - .AtkEvryOne
05 May, 2004
Well,can't wait for my card game to be done lets see,the coding is a secret
![](forums/images/avatars/143517295442aeed0e4289c.jpg)
ViperCat
January 28, 2004
Making games
