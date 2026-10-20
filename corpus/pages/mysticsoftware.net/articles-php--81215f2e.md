---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/articles.php?article=10&category=3&mode=1"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/articles.php?category=3&mode=1&article=10"
written: null
date_confidence: "unknown"
updated: null
captured: ["20050220101740"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/articles.php__category_3_mode_1_article_10", captured: "20050220101740", sha256: "c170b93e7d98652f455700f570fd9ae868c2805d20d8279326b718ffa73c8925", wayback_url: "https://web.archive.org/web/20050220101740/http://www.mysticsoftware.net/articles.php?category=3&mode=1&article=10"}
---

# Mystic Software

Part 1: Introduction Part 2: Useful time-systems Part 3: The magical variable Part 4: My *simple* solution Part 5: Closing words Part 1: Introduction Welcome to my tutorial on game-time. Game time is today understimated for TK-games, but actually, an interesting time system, may be a good way to come up with a good game... This tutorial will lead you through the traps, the gaps, and quickly help you make a fun game-time system, perfect for your game... Part 2: Useful time systems There's actually different types of game systems, and all of them may be good... Real-time system: This is a really interesting system, which allows you to have special features, i.e. night in the game when it's nigh outside your house, the Game Time is equal to the world time... This system is built-in in TK... 24-hours time systems: This GameTime system is a special type; each second in the real world is actally a second in the game... Personally, I don't like this type of system, because each time the player plays the game for 24 hours, that will just be one day in the game!!! Minutes-defined time systems: This system is also included in TK, and you can set it up in the Main File-editor. This game system is that when you play a defined number of minutes in the real world, you play one day in your game. Personally, I prefer the last solution, set up as 24 minutes. That means that one second in the real world is set up as one minute in your game... Part 3: The magical variable: How do I get the game time, you may wonder.... Hell, that is easy... It is stored as a variable in toolkit, a variable that any program can access, gameTime!. Also, if you're planning to do a real-time system, you can download my Time-Date plugin located on MrG's code shack (http://mrgoldsoft.mysticsoftware.net) Part 4: My *simple* solution I do believe that at this point, you have alredy decided which system you will use... Real-time system: 1. Get my Time-Date plugin located on MrG's code shack (http://mrgoldsoft.mysticsoftware.net) 2. Use the plugin according to the read-me. 3. Find it out yourself, I have never used this time system... You will need this method if you wish to make a 24-hours system or a minutes-defined system: #Method Modulus(mod_1!,mod_2!,mod_dest!) { #mod_dest!=mod_1!/mod_2! #CastInt(mod_dest!,mod_dest!) #mod_dest!=mod_dest!*mod_2! #mod_dest!=mod_1!-mod_dest! #ReturnMethod(mod_dest!) #Kill(mod_dest!) #Kill(mod_1!) #Kill(mod_2!) } 24-hours time system: Coding: #seconds!=gametime! #CastInt(seconds!,seconds!) #minutes!=seconds!/60 #CastInt(minutes!,minutes!) #Modulus(seconds!,60,seconds!) #hours!=minutes!/60 #CastInt(hours!,hours!) #Modulus(minutes!,60,minutes!) #days!=hours!/24 #CastInt(days!,days!) #Modulus(hours!,24,hours!) Now you have all the variables you need, seconds!, minutes!, hours! + days!. Minutes-defined system: I have only done a 24-minutes day-system Coding: #time!=gametime! #CastInt(time!,time!) #minutes!=time #hours!=minutes!/60 #CastInt(hours!,hours!) #Modulus(minutes!,60,minutes!) #days!=hours!/24 #CastInt(days!,days!) #Modulus(hours!,24,hours!) Now you have the needed variables; minutes!, hours! and days! Tip: If you wish to begin in day 1, just add the following on both examples: #days!=days!+1 or day 2, 3, 9568... Part 5: Closing Words: Hope you found any use of this tutorial. Any comments may be mailed to me(bpetter@cold-blade.com)... you may also use the included modulus-method as you like, it's pretty self-explaining, it just gets the remainder of an integer division.. -BP
- Gametime Tutorial - Written By BP
