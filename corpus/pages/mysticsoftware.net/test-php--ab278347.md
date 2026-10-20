---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/test.php?file=files/cselection.prg&mode=6"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/test.php?mode=6&file=files/cselection.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040910092852"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/test.php__mode_6_file_files_2Fcselection.prg", captured: "20040910092852", sha256: "3fd62eb7bb159ce0ccd19639571eb421e71e581062bf142a3931f97306d50db0", wayback_url: "https://web.archive.org/web/20040910092852/http://www.mysticsoftware.net/test.php?mode=6&file=files%2Fcselection.prg"}
---

# Mystic Software

#ChooseCharacter() #Method ChooseCharacter() { #h!=35 #h2!=h!+100 #h3!=h!+200 #pich!=91 #picw!=64 #ClearButtons() #Bitmap("Space2.jpg") #DestroyPlayer("Warrior.tem") * Place Pictures/Profiles of characters #SetButton("Angel2.jpg",0,12,h!,picw!,pich!) #SetButton("Archer2.jpg",1,86,h!,picw!,pich!) #SetButton("Barbarian2.jpg",2,160,h!,picw!,pich!) *#SetButton("Cleric2.jpg",3,234,h!,picw!,pich!) *#SetButton("Fairy2.jpg",4,308,h!,picw!,pich!) #SetButton("Monk2.jpg",5,382,h!,picw!,pich!) *#SetButton("Ninja2.jpg",6,456,h!,picw!,pich!) *#SetButton("Noble2.jpg",7,530,h!,picw!,pich!) *#SetButton("Paladin2.jpg",8,12,h2!,picw!,pich!) *#SetButton("Priest2.jpg",9,86,h2!,picw!,pich!) #SetButton("Red Mage2.jpg",10,160,h2!,picw!,pich!) *#SetButton("Serf2.jpg",11,234,h2!,picw!,pich!) *#SetButton("Knightess2.jpg",23,308,h2!,picw!,pich!) **#SetButton("Serj Tankian2.jpg",12,308,h2!,picw!,pich!) *#SetButton("Thief2.jpg",13,382,h2!,picw!,pich!) #SetButton("Warrior2.jpg",14,456,h2!,picw!,pich!) *#SetButton("White Mage2.jpg",15,530,h2!,picw!,pich!) #SetButton("Assassin2.jpg",17,12,h3!,picw!,pich!) *#SetButton("Pikeman2.jpg",18,86,h3!,picw!,pich!) *#SetButton("Mercenary2.jpg",19,160,h3!,picw!,pich!) *#SetButton("Mechanic2.jpg",20,234,h3!,picw!,pich!) *#SetButton("Wrestler2.jpg",21,308,h3!,picw!,pich!) *#SetButton("Shepherd2.jpg",22,382,h3!,picw!,pich!) **#SetButton("Scientist2.jpg",22,456,h3!,picw!,pich!) **#SetButton("Malkil2.jpg",24,12,h3!,picw!,pich!) **#SetButton("Captain Matey2.jpg",25,86,h3!,picw!,pich!) **#SetButton("Goru2.jpg",26,160,h3!,picw!,pich!) *#SetButton("menu next.jpg",27,480,319,128,32) * Place Command that tracks mouse clicks #mchar!=0 #While(mchar!=0) { #MouseClick(x!,y!) #Bitmap("loading.jpg") #CheckButton(x!,y!,num!) #if (num!==0) { #AddPlayer("Angel.tem") #playerHandle[0]$="Angel" #mchar!=1 } #if (num!==1) { #AddPlayer("Archer.tem") #playerHandle[0]$="Archer" #mchar!=1 } #if (num!==2) { #AddPlayer("Barbarian.tem") #playerHandle[0]$="Barbarian" #mchar!=1 } #if (num!==3) { #AddPlayer("Cleric.tem") #mchar!=1 } #if (num!==4) { #AddPlayer("Fairy.tem") #mchar!=1 } #if (num!==5) { #AddPlayer("Monk.tem") #playerHandle[0]$="Monk" #mchar!=1 } #if (num!==6) { #AddPlayer("Ninja.tem") #mchar!=1 } #if (num!==7) { #AddPlayer("Noble.tem") #mchar!=1 } #if (num!==8) { #AddPlayer("Paladin.tem") #mchar!=1 } #if (num!==9) { #AddPlayer("Priest.tem") #mchar!=1 } #if (num!==10) { #AddPlayer("Red Mage.tem") #playerHandle[0]$="Red Mage" #mchar!=1 } #if (num!==11) { #AddPlayer("Serf.tem") #mchar!=1 } #if (num!==12) { #AddPlayer("SerjTankian.tem") #mchar!=1 } #if (num!==13) { #AddPlayer("Theif.tem") #mchar!=1 } #if (num!==14) { #AddPlayer("Warrior.tem") #playerHandle[0]$="Warrior" #mchar!=1 } #if (num!==15) { #AddPlayer("White Mage.tem") #mchar!=1 } #if (num!==17) { #AddPlayer("Assassin.tem") #playerHandle[0]$="Assassin" #mchar!=1 } #if (num!==18) { #AddPlayer("Pikeman.tem") #mchar!=1 } #if (num!==19) { #AddPlayer("Mercenary.tem") #mchar!=1 } #if (num!==20) { #AddPlayer("Mechanic.tem") #mchar!=1 } #if (num!==21) { #AddPlayer("Wrestler.tem") #mchar!=1 } #if (num!==22) { #AddPlayer("Shepherd.tem") #mchar!=1 } #if (num!==23) { #AddPlayer("Knightess.tem") #mchar!=1 } } :done #Prompt("Enter player\'s name:",playerName[0]$) #ClearButtons() #mchar!=1 #mchar2!=1 #Kill(h!) #Kill(h2!) #Kill(h3!) #Kill(pich!) #Kill(picw!) #Kill(pagewait!) #Kill(mchar!) #Kill(mchar2!) #Kill(num!) #Kill(x!) #Kill(y!) #Done() #End() }
