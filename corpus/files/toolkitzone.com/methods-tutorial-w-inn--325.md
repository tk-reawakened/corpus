---
kind: file
id: "toolkitzone.com/325"
site: "toolkitzone.com"
title: "Methods Tutorial (w/ Inn)"
original_url: "http://www.toolkitzone.com/fileman.php?id=10&file=325"
written: "2004-02-25"
date_confidence: "day"
updated: "2004-02-25"
captured: ["20051112074829", "20051216022120", "20051218231501", "20051219002627"]
author: "Marz"
repliers: []
authors: ["Marz"]
comments_present: 0
f_author_source: "DeadMech"
f_name: "Methods Tutorial (w/ Inn)"
f_submitted_by: "Marz"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_325", captured: "20051112074829", sha256: "ed6c8018fb850f578d89e927ece7d8136bd30cdf6844886a3294479231689a8e", wayback_url: "https://web.archive.org/web/20051112074829/http://www.toolkitzone.com/fileman.php?id=3&file=325"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_7_file_325", captured: "20051216022120", sha256: "88361870c1be1a6705d91000fc12dfdb4acb4f98662c91ea941d1da2cced4496", wayback_url: "https://web.archive.org/web/20051216022120/http://www.toolkitzone.com/fileman.php?id=7&file=325"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_325", captured: "20051218231501", sha256: "cdb4d75d93760c14849b572e4c224e35cf8610ed7814fe80e27026eaca392a1d", wayback_url: "https://web.archive.org/web/20051218231501/http://www.toolkitzone.com/fileman.php?id=5&file=325"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_325", captured: "20051219002627", sha256: "c56a14700099f4d92da18ce344a0946e3cea808e0ea832663e09b1df844f2f74", wayback_url: "https://web.archive.org/web/20051219002627/http://www.toolkitzone.com/fileman.php?id=10&file=325"}
---

# Methods Tutorial (w/ Inn)

Not a bad tutorial on methods. gives you a custom inn to work with. Personally I would of used something a little easier for a beginner to understand but it still gets the job done. Nice job here.
Creating methods
A method is a very time saving piece of rpgcode. It allows you to call upon frequently used programs or program parts that get used over and over again. Of course it does take a little time to actually make a method.
An important part is to have what is called a method library. In your program menu you should see a program called system. Here there are about 4 fairly large programs. You may or may not want to put your own future methods in this program. Personally I would prefer to make my own library with a more easily found name. Something like AMethods so that it would be at the front of the list of programs. Either way.
Open your method library or at least what you plan on turning into a method library. We are going to make a program that gets run for an inn type situation. But let's say that I wanted an inn system that is different from the average inn rest you see in toolkit games. Let's say that the more health and special move power the charactesr were missing the more the rest at the inn would cost. A similar system was used in final fantasy 2 jap (for the nes) This system was alittle annoying for the fact that that game was unnessicarilly hard. An odd "leveling" system ruined it in my mind. But anyway...
In your method library type this.
************ * #InnMethod ************ #Method InnMethod() { *Make sure that you put the character name where it says character in this program. #GetMaxHP(“character”,characterHPMax!) #GetHP(“character”,characterHP!) #GetMaxSMP(“Character”,characterSMPMax!) #GetSMP(“Charater”,characterSMP!) *you should repeat the last 4 lines of code per character in your game. #inncostcharater! = characterHPMax! - characterHP! + characterSMPMax! - characterSMP! *the last line applies to one character. Repeat the last line once per character in the game #inncost! = inncostcharacter! *you must put one inncostcharacter per character in the game. make sure you add them. #mwincls() #Mwin(" Innkeeper: Would you like to stay and recover.") #Mwin(" It only costs . “) #wait(a$) #inn! = 0 #while(inn! == 0) #mwincls() #Mwin("1-stay the night.") #Mwin("2-no thanks.") #wait(s$) #if (s$=="1") { #getgp(gp!) #if (gp! > inncost!) { #TakeGP(inncost!) #Inn() *perhaps you would like to add a short bit of music and some lighting effects about here. #Fade(2) #Delay(3) *could be any number but keep it low. #Return() #inn! = 1 } #if (s$=="2") { #mwincls() #Mwin("Innkeeper: You don't have enough.") #wait(a$) #inn! = 1 } #if (q$=="2") { #mwincls() #Mwin("Innkeeper: Come by later then.") #wait(a$) #inn! = 1 } *I should add that a few kill commands to get rid of all those variables would be a nice addition to the end of the program. Free up memory.
Wow thats a big complicated program that took me almost 40 minutes to make. I haven't tested it either but in theory it should work. Keep in mind that it would be easy to simply delete some of the parts and modify the program to use a fixed inn cost. It certainly would make the program smaller. But this isn't a tutorial on making an inn program. This is to teach you how to make and use methods.
Save the program into your method library. Now when you want to use this method you must do this.
Open the board that is the inn interior. Open the program editor. Type something like this.
#mwincls() #Mwin("Innkeeper: Welcome to the Conarian Inn") #wait(a$) #Include(“library.prg”) *replace library with the name of your method library program #InnMethod()
Save this program as something like Conarian Inn.
Place this program as an npc, the innkeeper. Now when the player talks to the inn keeper that very large and complicated code gets run. But you might be wondering how all that work was worth it.
Lets say that you had 7 cities. Each city has an inn. It would stand to reason that every inn needs a original program. That would mean typing that big program 7 times. You could copy and paste but using methods makes your game look much more professional. Besides you are likely to make some sort of mistake doing everything. This way you only have one program to fix.
Well that seems to conclude this tutorial. Remember though. Making your own methods and programs is the only way to make your game the best it can be.
DeadMech
**Browse Sections**
