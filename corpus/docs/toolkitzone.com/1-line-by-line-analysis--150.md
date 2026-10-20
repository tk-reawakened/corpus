---
kind: doc
id: "toolkitzone.com/150"
site: "toolkitzone.com"
title: "1: Line by line analysis"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=150"
written: "2005-01-26T17:40:00"
date_confidence: "exact"
updated: null
captured: ["20060521140427"]
author: "Talyn"
repliers: []
authors: ["Talyn"]
comments_present: 0
f_author: "Talyn"
f_date: "January 26, 2005, 5:40 pm"
f_description: "Talyn provides his debugging techniques as well as others than you can adopt to help squash those niggling bugs in your code before they drive you insane."
f_section: "Toolkit 3.x"
f_title: "The Art of Debugging"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_150", captured: "20060521140427", sha256: "f832739be922a32544829840698fb6c357c1326a935c573eef18cbd85eb1338c", wayback_url: "https://web.archive.org/web/20060521140427/http://www.toolkitzone.com:80/library.php?mode=read&doc=150&PHPSESSID=49eb2e17f9e455e1205f36438de58609"}
---

# 1: Line by line analysis

A very much neglected aspect of many games is debugging. Looking around these forums you see a lot of queries about programming, tile design and so on but very little about debugging. So this article is going to explain the basics of getting a good error checking system going. So you've finished your game and you think it's ready for release. However, if you were to play it now, you'd probably run up against enough errors to make the game unplayable. This is something many people don't consider and even if your code is word pefect, there will still be errors which the Trans engine will throw up of it's own accord. Things like characters facing the wrong way, or NPC's appearing on solid tiles are all things which detract from the realism and profeesionalism of your game. So how do you combat these errors? I find that there are four ways in making your game bug free enough for a release, which catch as many errors as possible. This is the most boring part of any debugging run, but you can catch over 60% of errors this way. Go through all your programs line by line and check for obvious mistakes. Things like missing out parentheses marks (""). These little marks can be vital to the trans engine and will make the difference between the code running right, or not. Other things like spelling are a good one to check here. I always find it helpful to have Word open as well and if there's a spelling you're unsure of, type it in there and see whether it's correct or not. Spelling mistakes in code can be deadly too. mis-spelling the word will cause the debugger to come up at run-time and woul will lose those lines of dialogue. Another thing to check is variable control. Have notepad open and list all the variables you use within a program and then make sure you kill them at the end. Your game will run significantly faster if there are fewer variables kicking around. Also check for never ending loops and make sure they are given a definitive ending (unless you're using TK3's multi-threading of course). Last, but not least, check the programs decision code (things like ). Make sure that the variable you are checking is the same one that the is being told to look at. When many people think of errors, they tend to think of the program code, but graphical errors can be just as much of a nuisance. Part of the graphical checking process needs to be done at run-time, but for the moment, open up each and every board in your game and look for obvious problems. Tiles missing, or tiles which have been erased. This is especially important when using layered boards, as these can very quickly become confused and messy. If you have any concept art with you, keep checking back to that and see where you've gone wrong. Errors with graphics don't need to be game hindering, they could just be a board which plainly doesn't fit in with the games overall style. Check your tile types. All too often you'll find yourself traversing the wall of a house because you forgot to make some tiles solid. This is again important when thinking about layered boards. Say you have a house built on layer 2, but at run-time you want it to be solid on layer 1. Make sure the corresponding tiles on layer 1 are in fact solid! Otherwise you'll end up underneath the house. Also check for things such as entrances and exits to boards. Do you have warp tiles to take you about and are they correct? Are the directional links correct? Do both the starting board and the destination board point towards each other? You should be asking yourself these questions all the time when checking a board for movement problems. This is also tedious, but no-one ever said that debugging was fun. Open up every item, every character and every enemy and check that you've filled everything you need to in. Also check things like spelling on the items description. Open up your special moves and check that everything is correct there as well. Make sure the special moves have been assigned to characters or enemies, otherwise it was pointless you making them. Another common problem is enemies. People tend to think that once you've created an enemy it's automatically entered into the game. WRONG! You must add the enemy into the game using that great big button at the bottom. Without this, the trans engine will have a hell of a job sorting out battles, creating more errors. There is quite a lot to think about with these elements of the game, and you are bound to have missed something. Do items have a selling price? Have you specified where a piece of equipment can go on the body? Do your characters have the correct special moves? Do the Status Effects have animations? Everything here needs to be gone over with a fine toothed comb, as these errors are incredibly annoying when playing games. For example, if you buy a 3000GP sword and find out that it does nothing to your stats when you equip it because the games creator forgot to do it, you're not a happy player. These are all simple things, but it will take time. Here's the dangerous one. People often just do this as their error checking, but there's a lot more to think about here than meets the eye. Firstly, before you even hit that green triangle to start playing, get yourself organised. Have a pen and a good wodge of paper ready. Yep, pen and paper. If you find that a never ending loop freezes your computer up, how are you going to type that in Notepad? Errors can come thick and fast in battles, so be ready with the pen in your hand at all times. Now you can start playing. First rule of run-time checking: Try . As the games designer, you're in a privileged position because you know the fastest route through the game and it's very tempting to do just that, take the fastest route. Don't. Test absolutely everything in as many ways as possible to try and catch as many bugs as possible. Things like; "What happens if I fight this boss with this armour on?", "What happens if I open the menu here?", "How about if I go this way instead of that?" I can guarentee that you will get bored very quickly, but this is essential to a games success. However, now might be a good time to bring in a limited test run of your game on other people. Compile it all into whatever form you will use and then burn it to say three CD's. Then find three friends who have nothing better to do and get them to test it. If possible, make sure they all have different spec computers and ranging abilities with computers. (This is also a good point to test things like installers). Get them to write down any problems they have and any suggestions to make it better. (As an incentive, teel them that they will get their names on the credits as testers). This type of advice is invaluable, as these people are essentially your target audience. When you get back their comments, ACT ON THEM! There will be some comments which cannot be done, such as "I don't like the main characters hair." but you usually get some very good ideas coming out of things like this. Comments such as: "A savepoint there would be helpful", "After that sequence, the dialogue feels a bit shakey", "You can't access that area if you have the rusty armour equipped" are extremely helpful, and usually fairly easy to solve. Sometimes there are things which just cannot be fixed. These can be internal errors in the trans engine itself, or just bugs which are a necessary evil. To combat these, I always find it useful to put in your start program: This means that you won't get any irritating pop up messages during game play. Only include this line once you've finished your debugging though, otherwise you'll be error checking blindly. Once you've finished your game, do not release it for at least a week. Spend that week rigorously checking it and making sure that everything works. If you don't, then you'll regret it when the reviews come back in saying that there's a major bug sitting just before your final, heartbreaking scene which means that your character turns blue and you spend the whole scene laughing at him.
The Art of Debugging
**1: Line by line analysis**
**Mwin**
**If** **If**
**2: Graphical Error Checking**
**3: Character, NPC, Enemy, Item, Spc Move, Status Checking**
**4: Actually play it!**
*everything*
**And if the worst comes to the worst?**
**#Debugger(off)**
**A final rule of thumb**
*Talyn*
TK Game Boy
January 26, 2005, 8:07 pm
OI. I didn't knew variables! slow down your game. Ack. Well this tutorial is great but boring to follow. Ack. Your popularity has just dropped by 1 point you dork.
Alex0Xander
January 27, 2005, 1:24 pm
TKGB you a hole.. =] Arg, not the heartbraking scene! Thats the scene where the main characters heart breaks and he dies!
John@aljo
January 28, 2005, 8:55 pm
I would like to add to this that #show is your friend. If you can't figure out why something is going wrong. Show the variables that are running around in the background. They will tell you more of the story than just running the program or even analyzing the code because in your mind your code may run a lil differnt from what it actually does and a visual analysis of the code line by line isn't always the best approach to solving this.
Talyn
January 29, 2005, 4:13 am
Very true John. I forgot to add that one.
Talyn provides his debugging techniques as well as others than you can adopt to help squash those niggling bugs in your code before they drive you insane.
Sep 4, '05
Apr 5, '05
Dec 23, '04
Dec 12, '04
Oct 25, '05
Sep 19, '05
Jun 2, '05
May 2, '05
Apr 8, '05
