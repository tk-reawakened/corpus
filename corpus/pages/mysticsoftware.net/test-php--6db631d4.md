---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/test.php?file=uploads/C_Lib1.prg&mode=6"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/test.php?mode=6&file=uploads/C_Lib1.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20051103143751"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/test.php__mode_6_file_uploads_2FC_Lib1.prg", captured: "20051103143751", sha256: "c6b4019eec9752fd9dffeeb96e27125b4f8c0332470234e4540689a11e4d683e", wayback_url: "https://web.archive.org/web/20051103143751/http://www.mysticsoftware.net/test.php?mode=6&file=uploads%2FC_Lib1.prg"}
---

# Mystic Software

************************************************************* * ---------------------------------------------------- * * FLASH SCREEN METHOD BY ULTIMATE_COCKATEIL * * * * INCLUDE THIS FILE IN YOUR PROGRAMS AND TYPE IN * * * * #flashscreen(ar!, ag!, ab!, br!, bg!, bb!, cr!, cg!, cb!)* * * * AS A COMMAND. ar!, ac!, and ab! are the red, green, and * *blue of the first color. br, bg, bb are the second color * * RGBs, and cr, cg, cb are the third color RGBs * ************************************************************* #Method flashscreen(ar!, ag!, ab!, br!, bg!, bb!, cr!, cg!, cb!) { #SaveScreen() #For (x!=1;x!<=4;x!=x!+1) { #Colorrgb(ar!, ag!, ab!) #fillrect(0,0,1008,1352) #Delay(0.1) #Colorrgb(br!, bg!, bb!) #fillrect(0,0,11008,1352) #Delay(0.1) #Colorrgb(cr!, cg!, cb!) #fillrect(0,0,11008,1352) #Delay(0.1) } #RestoreScreen() #ColorRGB (255, 255, 255) } ************************************************************* * ---------------------------------------------------- * * SUPER INN METHOD BY ULTIMATE_COCKATEIL * * * * INCLUDE THIS FILE IN YOUR PROGRAMS AND TYPE IN * * * * #SuperInn (moneyneeded!) * * * * AS A COMMAND. MONEYNEEDED! IS THE AMOUNT OF GP IT COSTS * * TO SLEEP IN THE INN * ************************************************************* #Method SuperInn(moneyneeded!) { { #Include "system.prg" #MWin ("Welcome! It will be GP to spend the night.") #Pause() #MWinCls #MWin ("Would you like to?") #MWin ("1-Yes") #MWin ("2-no") #Wait (a$) #MWinCls #If (a$=="1") { #GetGP ("money!") #If (money!
Order it Today!
