---
kind: forum-thread
id: "toolkitzone-forums/7028"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "general help"
skin: "phpbb2"
thread_id: "7028"
title: "battle system help"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=7028"
written: "2004-08-12T00:41:00"
last_post: "2004-08-12T00:41:00"
date_confidence: "exact"
captured: ["20040915043252"]
author: "Frankster_13"
repliers: []
authors: ["Frankster_13"]
posts_present: 1
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_73620_amp_", captured: "20040915043252", sha256: "9d15e077ccb585f14cc6cdf5aee0da18f7b3da32cc9abf2500213d8c3f3e5d3a", wayback_url: "https://web.archive.org/web/20040915043252/http://www.toolkitzone.com/forums/viewtopic.php?p=73620&amp="}
links: []
---

# battle system help

### Frankster_13 · 2004-08-12 00:41 · #B73620

i have been making a battle system 4 1 of my games but when i put that whole create cursor thing it puts that and the rest of my program into mwin what is wrong Sad. heres my program
_____________________________________________________________
#MidiPlay("SPLASH.wav")
#SetImage("Battle 0.bmp", 210, 170, 200, 100)
#Delay(.05)
#SetImage("Battle 1.bmp", 210, 170, 200, 100)
#Delay(.05)
#SetImage("Battle 2.bmp", 210, 170, 200, 100)
#Delay(.05)
#SetImage("Battle 3.bmp", 210, 170, 200, 100)
#Delay(.05)
#SetImage("Battle 4.bmp", 210, 170, 200, 100)
#Delay(.05)
#SetImage("Battle 5.bmp", 210, 170, 200, 100)
#Delay(.05)
#SetImage("Battle 6.bmp", 210, 170, 200, 100)
#Delay(1.0)
#DrawEnemy("goblin.ene", 10, 1)
#AI(3)
#SetImage("newfightmenu.bmp", 1, 1, 190, 164)
cMap! = CreateCursorMap()
CursorMapAdd(45, 38, cMap!)
CursorMapAdd(45, 70, cMap!)
CursorMapAdd(45, 105, cMap!)
res! = CursorMapRun(cMap!)
KillCursorMap(cMap!)
if(res! == 0)
#MWin("which direction? N S E W")
#wait(q$)
#MWinCls()
#If(q$ == "up")
#Push("N", "Aeron")
end
#AI(3)
#If(q$ == "down")
#Push("S", "Aeron")
end
#AI(3)
#If(q$ == "Left")
#Push("W", "Aeron")
end
#AI(3)
#If(q$ == "Right")
#Push("E", "Aeron")
end
#AI(3)
#Branch("#SetImage" newfightmenu.bmp", 1, 1, 190, 164")
if(res! == 1)
#Animation("aeron att.anm", 210, 170)
#AttackAll(10)
end
#AI(3)
#Branch("#SetImage" newfightmenu.bmp", 1, 1, 190, 164")
if(res! == 2)
#SetImage("fightmenumagic.bmp", 1, 1, 190, 164)
cMap! = CreateCursorMap()
CursorMapAdd(45, 38, cMap!)
CursorMapAdd(45, 70, cMap!)
CursorMapAdd(45, 105, cMap!)
res! = CursorMapRun(cMap!)
KillCursorMap(cMap!)
if(res! == 0)
#Earthquake(5)
#Animation("aeron fire.anm", 210, 170)
#AttackAll(15)
end
#AI(3)
#Branch("#SetImage" newfightmenu.bmp", 1, 1, 190, 164")
if(res! == 1)
#Earthquake(5)
#Animation("aeron ice.anm", 210, 170)
#AttackAll(15)
end
#AI(3)
#Branch("#SetImage" newfightmenu.bmp", 1, 1, 190, 164")
if(res! == 2)
#Earthquake(5)
#Animation("aeron bolt.anm", 210, 170)
#AttackAll(15)
end
#AI(3)
#Branch("#SetImage" newfightmenu.bmp", 1, 1, 190, 164")
