---
kind: forum-thread
id: "toolkitzone-forums/12618"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "general chat"
skin: "phpbb2"
thread_id: "12618"
title: "Questions about GAM files"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12618"
written: "2004-12-14T20:21:00"
last_post: "2004-12-15T23:09:00"
date_confidence: "exact"
captured: ["20041228072812"]
author: "Setu_Firestorm"
repliers: ["TheCPPFreak220", "Levi", "Metallic Ego", "Dont_Think_So", "John@aljo", "Brad"]
authors: ["Setu_Firestorm", "TheCPPFreak220", "Levi", "Metallic Ego", "Dont_Think_So", "John@aljo", "Brad"]
posts_present: 10
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_139811_amp_", captured: "20041228072812", sha256: "8273e271dd4eee373026a061b04ed70229f40327b6933ea6e24731d793b6fc67", wayback_url: "https://web.archive.org/web/20041228072812/http://www.toolkitzone.com/forums/viewtopic.php?p=139811&amp="}
links: []
---

# Questions about GAM files

### Setu_Firestorm · 2004-12-14 20:21 · #B139592

Now, I'm completely new to the toolkit, so please bear with me if my questions are kinda dumb.
Firstly, I believe, unless I'm mistaken, that GAM files are the game's filetype, yet I've noticed that in some games I've downloaded, there were multiple GAM files. This posed two questions:
1) Would you have to create GAM files just for minigames that would be in your RPG? ...and
2) If that IS true, then is it possible to span your RPG across multiple GAM files?
I appreciate the help.

### TheCPPFreak220 · 2004-12-14 20:24 · #B139595

Thos multiple GAM files are only there, because people forgot to delete them. All your main game data is stord in one GAM file.

### Setu_Firestorm · 2004-12-14 20:46 · #B139601

Okay, with that being said, would you have to create a GAM file for minigames and call it with RPGCode?

### Levi · 2004-12-14 21:29 · #B139635

Minigames can be made in RPGCode. No need to run a whole new game file. RPGCode can control boards, items, characters, enemies, battles. Anything. THat's what makes it so great for making games.

### Metallic Ego · 2004-12-14 23:04 · #B139699

You will never need to have more then one .GAM file for a super-long game either, unlike some makers. Your game can be as large as you have room on your hard drive.

### Dont_Think_So · 2004-12-15 01:41 · #B139811

Although, you COULD make more than one game file and call it with RPGCode.
Just remember that variables aren't carried over.

### Setu_Firestorm · 2004-12-15 22:56 · #B140273

Thank you, Dont think so. That's what I was wanting to know.
Reason for my asking is:
I'm making a game that is based off of my original manga series, but I wanted to release the game in individual episodes yet make it where you can go on to the next episode without having to restart a new game.
Which leads me to a question of curiousity: Is it possible, by means or manipulation, to use a SAV file from one game in another game? In the OHRRPGCE engine, you could manipulate this by renaming your SAV file after the RPG filename of the new game you wanted to play.
However, taking into account that it won't carry variables, that's a roadblock that I'm glad I was made aware of, so I know what I could probably do to get around that.

### John@aljo · 2004-12-15 23:00 · #B140283

yes its very possible to use one save game on another game... what the save file does is save every variable in game such as your position, what board you are on,.... everything.

### Brad · 2004-12-15 23:06 · #B140294

Yup, just as long as it has the same tilesets and everything, becuase if you delete some it would end up looking like a white square or tv static.

### Setu_Firestorm · 2004-12-15 23:09 · #B140299

Groovetacular. Thanks for the help guys! I very much appreciate it.
