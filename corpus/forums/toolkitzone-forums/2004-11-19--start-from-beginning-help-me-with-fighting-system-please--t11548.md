---
kind: forum-thread
id: "toolkitzone-forums/11548"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "editor help"
skin: "phpbb2"
thread_id: "11548"
title: "Start from beginning; help me with fighting system, please"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11548"
written: "2004-11-19T21:29:00"
last_post: "2004-11-19T23:55:00"
date_confidence: "exact"
captured: ["20050111163047"]
author: "The Beginner"
repliers: ["Dont_Think_So"]
authors: ["The Beginner", "Dont_Think_So"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_127330_amp_", captured: "20050111163047", sha256: "7c81a4cdb93fed28524f695a89d6cd68fe473970d6ea6c3e307e3dd95b89f6fb", wayback_url: "https://web.archive.org/web/20050111163047/http://www.toolkitzone.com/forums/viewtopic.php?p=127330&amp="}
links: []
---

# Start from beginning; help me with fighting system, please

### The Beginner · 2004-11-19 21:29 · #B127268

I'm a noob and i can't get this fighting system right..
What should I do?
Do u guys have any fighting systems for me ?
Thx

### Dont_Think_So · 2004-11-19 23:55 · #B127330

Just think about what you want to do in your battle system. What order will things happen in, and under what circumstances? An average Battle System will follow a pattern sort of like this:

**Code:**

```
DrawBKG() //Draw background

DrawEnemies() //Draw Enemies and players

DrawGUI(0) //Draw GUI

Kill(GameOver!)

Until(GameOver!)

{

If(FindTurn() == "Player")  //Who's turn is it?

{

DrawGUI(1) //Draw Player's menu

StartChoice() //Let the player choose what they want to do

DoAction() //Perform whatever action the player chose.

}

If(FindTurn() == "Enemy")

{

DrawGUI(2) //Draw enemy's turn

PerformAI() //Choose what the computer does

DoAction() //Perform whatever action the computer chose.

}

If(ChecKWinConditions()) //Did the player win?

{

GameOver! = 1 //End the Battle system.

Winner! = 0 //Player won

}

If(ChecKLoseConditions()) //Did the enemy win?

{

GameOver! = 1 //End the Battle system.

Winner! = 1 //Enemy one

}

DrawBKG() //Draw background

DrawEnemies() //Draw Enemies and players

DrawGUI(0) //Draw GUI

}
```

Then, you can think of the battle system in pieces, instead of all at once. So, at the bottom, add the DrawBKG() method, which handles the background. Go down the list and fill out each item.
