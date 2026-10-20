---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/askxorlak.php?mode=1&question=9"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://mysticsoftware.net/askxorlak.php?mode=1&question=9"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040505105526"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/askxorlak.php__mode_1_question_9", captured: "20040505105526", sha256: "2df54cf6f6bd6e75869d454993de21f67638498103c2dd4bbabd89c695fc7582", wayback_url: "https://web.archive.org/web/20040505105526/http://mysticsoftware.net/askxorlak.php?mode=1&question=9"}
---

# Mystic Software

How do I add stamina to my battle system?
Stamina is usually a pretty simple addition, but it adds a nice touch. In , for example, I set it up as a damage multiplier that causes your physical attacks to do less damage the lower the stat goes. I've seen other variations as well (be creative!) First, (after initializing stamina! to its max value) you need to take away some stamina after each attack: #stamina!=stamina!-st_use! Of course if you have multiple characters, you'll probably want to set the variable up as playername[Stamina]! or something to that effect. Now when you calculate damage (actually you proably want to do this before taking stamina away), do something like: #ratio!=stamina!/max_stamina! #damage!=damage!*ratio! #castint(damage!,damage!) In this case, if the player's ST is 900 and his Max ST is 1000, ratio! will be 0.9 and damage! will be 90% of its original value. There are plenty of other ways to do stamina as well. You could have it cause damage when the player attacks if it gets too low for example. In Final Fantasy 3, it's a stat that blocks instant kill moves, while it determines the number of times you can attack in Crono Cross. [Dark Age 2](http://darkage.mysticsoftware.net)
