---
kind: doc
id: "toolkitzone.com/126"
site: "toolkitzone.com"
title: "Introduction"
original_url: "http://toolkitzone.com/library.php?mode=read&doc=126"
written: "2004-12-31T14:09:00"
date_confidence: "exact"
updated: null
captured: ["20060312124254"]
author: "Occasionally_Correct"
repliers: []
authors: ["Occasionally_Correct"]
comments_present: 0
f_author: "Occasionally_Correct"
f_date: "December 31, 2004, 2:09 pm"
f_description: "OC provides a quick and easy to follow tutorial on oa fundamental trick to help you create your game, having certain events only happen once."
f_title: "Making things work... once!"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_126", captured: "20060312124254", sha256: "6788fe323e11b7f9eea78674b4ba39dba8c18354b428a5e3a03f59b8b6948b10", wayback_url: "https://web.archive.org/web/20060312124254/http://toolkitzone.com:80/library.php?mode=read&doc=126&PHPSESSID=bdcceeefceef8ff863ad82d0d089ece4"}
---

# Introduction

Hi there! OC here, and today I'll be taking a break from more or less intermediate things. This article will be answering that age old question that almost everyone in the community has seen pop up on the forums more than a few times; how do you make things happen only one time? You know when you walk up to your NPC's and try to talk to them? They always seem to have the same thing to say. So, how are we going to remedy this? The simlpest way is to use an if statement to check if a variable is equal to 1 or 0. Based on the comparison, the NPC will say something different when you talk to them. And there you have it. If you run that in your game, you'll see that your NPC first says, "Good morning," then, upon talking to them again, they will say, "Hey, I've already talked to you." If you are unfamilliar with if statements, all this does is check to see if talkedToNPC! is equal to 1. The if statement will only run if that condition is correct, or 'true' (executing the commands inside it's opening and closing braces). The else statement will run if talkedToNPC! is not 1. Since numeric variables are automatically set to 0, the else statement will automatically run. You won't have to create the variable beforehand. So, you need to get an item for an NPC so they'll devulge some secret to you. However, you aren't sure how to make the NPC tell you something (or give you something) after you get the item. There are a few steps you'll need to take: The first is writing the program for the NPC, whic we'll do now; Now, the second step you need to take is to get the item. So, put that somewhere in your game. In the item editor, attach this program to the 'Program to run when picked up' slot: Easy, right? Now, if you go back to the NPC, he'll tell you the secret and take the ice cream. How does that happen, though? Well, when you create a variable, it stays in your computers memory until you either quit the game, declare it locally, or use the kill() command to destroy it. By default, though, they stay in memory. So the gotItem! variable, which was created in the NPC's program, will be accessible in the program to run with the item. Well, that does it for today. I hope this answers that age-old question for those of you know need to know. Remeber that this same technique can be applied to many things, not just making NPC's say different things. These are just some of the most asked about cenarios. If you have any suggestions or articles you'd like to see, you can PM me or e-mail me at . **Making things happen... Once!**
**Introduction**
**Say something else!**
```
//Check the talkedToNPC! variable
if(talkedToNPC! == 1)
{
//The talkedToNPC! variable is equal to 1
//So we've talked already...
//Display a message to the user
mwin("Hey, I already talked to you!")
wait()
mwincls()
}
else
{
//The talkedToNPC! variable isn't equal to 1
//so we haven't talked yet.
//Display a message to the user
mwin("Good morning!")
wait()
mwincls()
//Set the variable to 1
talkedToNPC! = 1
}
```
**Go get an item for me**
```
//Check the gotItem! variable
if(gotItem! == 1)
{
//gotItem! is equal to 1
//We've gotten the item!
mwin("Ah, you've got my ice cream.")
mwin("There's cool stuff around here. Some secret, eh?")
wait()
mwincls()
//Take the ice cream item away
takeItem("icecream")
}
else
{
//gotItem! isn't equal to 1
//We haven't gotten the item
mwin("Get me some ice cream and I'll tell you a secret.")
wait()
mwincls()
}
```
```
//Set gotItem! to 1
gotItem! = 1
```
**Conclusion**
words.so.leisured@gmail.com
John@aljo
December 31, 2004, 7:55 pm
hehe I remeber finding that out on my own when I was a noob bout 4 years ago. Interesting stuff you got there. Wish the tutorials would of been this good :P.
Stanley
January 1, 2005, 4:00 pm
Pretty good tutorial.
stanleywuu
January 11, 2005, 4:27 pm
Lol, I almost thought that I posted the above message
Renegade
March 24, 2005, 1:27 pm
Really helpful! Loved it! Thanks a lot!
**Column**
RPG Code > Tips & Tricks
OC provides a quick and easy to follow tutorial on oa fundamental trick to help you create your game, having certain events only happen once.
**Past Columns**
Feb 18, '05
Feb 11, '05
Jan 29, '05
Jan 15, '05
Jan 8, '05
Feb 18, '05
Feb 11, '05
Jan 29, '05
Jan 15, '05
Jan 8, '05
