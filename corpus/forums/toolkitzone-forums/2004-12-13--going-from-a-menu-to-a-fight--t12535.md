---
kind: forum-thread
id: "toolkitzone-forums/12535"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12535"
title: "Going from a menu to a fight"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12535"
written: "2004-12-13T00:19:00"
last_post: "2004-12-14T22:29:00"
date_confidence: "exact"
captured: ["20041228072605"]
author: "st_jimmy"
repliers: ["Village Idiot"]
authors: ["st_jimmy", "Village Idiot"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_139688_amp_", captured: "20041228072605", sha256: "605b9045c88b6a184262839fb5c1f70738f56690658d092e948f043aa680e6e5", wayback_url: "https://web.archive.org/web/20041228072605/http://www.toolkitzone.com/forums/viewtopic.php?p=139688&amp="}
links: []
---

# Going from a menu to a fight

### st_jimmy · 2004-12-13 00:19 · #B138759

(a bit of background) Two characters are going through a cave, the background starts shaking and then they get into a fight. Before the fight I want to enter the menu so I can make all necassary equips, then after that there's a bit of talking then it goes right into the fight. After the fight it send them to a new board.
Here's the code I've written so far...
*This is where the talking starts:
MWin("Tre:")
MWin("What the hell happened here?")
Wait()
MWinCls
MWin("McNyrea:")
MWin("Looks like there was some sort of massacre.")
MWin("We better not forget to equip our weapons!")
Wait()
*First Earthquake
Earthquake(3)
MWin("This cave is pissing me off...")
Earthquake(3)
Wait()
MWinCls
MWin("Tre:")
MWin("What is that?")
Wait()
MWinCls
MWin("McNyrea:")
MWin("What is what?")
Wait()
MWinCls
MWin("Tre:")
MWin("THAT!?!?!")
Earthquake(3)
Wait()
MWinCls
MWin("McNyrea")
MWin("I don't know what's going on!")
MWin("We better get our weapons equipped!")
Wait()
MWinCls
Earthquake(3)
*This is where it enters the menu
#InternalMenu(0)
*Then after this the program stops running.
MWin("Tre:")
MWin("Here we go!")
Wait()
MWinCls
FightEnemy("rock_warrior_1", "cave.bkg")
MWin("Tre:")
MWin("Maybe this wasn't a good idea!")
MWin("Let's turn back!")
Earthquake(5)
Wait()
MWinCls
MWin("McNyrea:")
MWin("These shakes are getting worse!")
Earthquake(7)
Send("Cave1.2.brd",22,11,1)
Wait()
MWin("...That last one caved in the entrance!")
Wait()
MWinCls
MWin("Tre:")
MWin("Well, I guess all we can do now is go deeper...")
Wait()
MWincls
The problem: it cuts off directly after exiting the menu and the rest of the code is just ignored. How do I exit the menu and have the program continue?

### Village Idiot · 2004-12-14 22:29 · #B139688

What if you made it an If statement, but set the variable to true to begin with?
#Earthquake(3)
scene! == 1
#if (scene! ==1)
{ *call your menu, then end the IF statement
}
#Mwin("whatever you put")
I think this might work. I'm kinda new at rpgcode, too, but i also know Visual Basic, and that helps a little. Let me know if it works, okay?
