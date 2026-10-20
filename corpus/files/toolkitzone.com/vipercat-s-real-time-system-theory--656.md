---
kind: file
id: "toolkitzone.com/656"
site: "toolkitzone.com"
title: "ViperCat's Real Time System theory"
original_url: "http://www.toolkitzone.com/fileman.php?id=10&file=656"
written: null
date_confidence: "unknown"
updated: null
captured: ["20041101052411", "20041106165103", "20041106165204"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_656", captured: "20041101052411", sha256: "8901bcc977c8e5a2e95d188d6b62f4a58e9f93366f5f41ae581687517f72a09f", wayback_url: "https://web.archive.org/web/20041101052411/http://www.toolkitzone.com/fileman.php?id=3&file=656"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_656", captured: "20041106165103", sha256: "2b668d03b35fa8083b2717515dbd678438a03c76538a7377bdddf2db7745c3f2", wayback_url: "https://web.archive.org/web/20041106165103/http://www.toolkitzone.com/fileman.php?id=5&file=656"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_656", captured: "20041106165204", sha256: "6f898c9b8be34e6a4204dabfaa58f6bc7302a07913eaf10e141f200b4dbe89fb", wayback_url: "https://web.archive.org/web/20041106165204/http://www.toolkitzone.com/fileman.php?id=10&file=656"}
---

# ViperCat's Real Time System theory

You must set your character somewhere -
#Send("Brd.brd",19,11,1)
Ok when you have your enemy , wich must be an item , turn it's coords into variables like so -
#PutItem("Itm.itm",1,3,1,)
#1=x!
#2=y!
Now that you've done that you must have to program the Enemie's A.I.,Just make a manual walk for the item do not use wander! -
Put #walk!=0 at the beginning of the walk code.
:top
#Push("Itm.itm","N")
#y!=y!-1
That you would do if the enemy went North. The following will explain all directions an the variable reaction -
North - #y!=y!-1
West - #x!=x!-1
South - #y!=y!+1
East - #x!=x!+1
But now we have to make the character be able to walk while the item is walking -
First,after all the walking sequence for the item is coded at the end put - #walk!=1 - then put a while - #While(walk!=0),Then your character can move while the item is moving.
Now we have to make the item attack the character -
#If(playerX[0]!,playerY[0]!==x!,y!+5)
#atk!=0
#Animation("Atk.anm",x!,y!+1)
#Animation("Atk.anm",x!,y!+2)
#Animation("Atk.anm",x!,y!+3)
#Animation("Atk.anm",x!,y!+4)
#Animation("Atk.anm",x!,y!+5)
#GiveHP("
#Branch(:top)
Well I've kinda ran short of time so,I'll just submit this and be on my way. I'll try to expand on this later,and I hope you will too.See yah -
-ViperCat-
