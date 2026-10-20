---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/test.php?file=files/pests_hpsmp.prg&mode=6"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/test.php?mode=6&file=files/pests_hpsmp.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040818023231"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/test.php__mode_6_file_files_2Fpests_hpsmp.prg", captured: "20040818023231", sha256: "2d0e1640261c3baac9d7b246e3fcd5a2e18b60f6002f2ce41c7b147ea140a286", wayback_url: "https://web.archive.org/web/20040818023231/http://www.mysticsoftware.net/test.php?mode=6&file=files%2Fpests_hpsmp.prg"}
---

# Mystic Software

* HP/SMP Bar * -Made by Pests * * Only difference between the HpBar and SmpBar * is that the SmpBar is always the same color * * x1!,x2!,y1!,y2! - Coords for the bar * current! - current hp/smp he has * max! - the maximum hp/smp they can have * * x2! - x1! = width * y2! - y1! = height #Method HpBar(x1!, x2!, y1!, y2!, current!, max!) { #FillRect(x1!, y1!, x2!, y2!) #fill! = current! / max! #difference! = x2! - x1! #howmuch! = difference! * fill! #fillwhat! = howmuch! + x1! #color(1) #if(fill! <= .70){ #ColorRGB(255,255,0) } #if(fill! <= .30){ #Color(4) } #FillRect(x1!, y1!, fillwhat!, y2!) #colorRGB(255,255,255) #drawrect(x1!,y1!,x2!,y2!) } #Method SmpBar(x1!, x2!, y1!, y2!, current!, max!) { #FillRect(x1!, y1!, x2!, y2!) #fill! = current! / max! #difference! = x2! - x1! #howmuch! = difference! * fill! #fillwhat! = howmuch! + x1! #color(1) #FillRect(x1!, y1!, fillwhat!, y2!) #colorRGB(255,255,255) #drawrect(x1!,y1!,x2!,y2!) } #clear() #HpBar(50, 150, 25, 35, 50, 100) #SmpBar(50, 150, 100, 110, 3, 100) #wait(a$)
