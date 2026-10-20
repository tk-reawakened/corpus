---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/test.php?file=uploads/Showtime.prg&mode=6"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/test.php?mode=6&file=uploads/Showtime.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040819081636"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/test.php__mode_6_file_uploads_2FShowtime.prg", captured: "20040819081636", sha256: "4c6443719778e9ebdd8bc2f8a3c2bf3b17f1704c0b405f229f03ecaa4ffac201", wayback_url: "https://web.archive.org/web/20040819081636/http://www.mysticsoftware.net/test.php?mode=6&file=uploads%2FShowtime.prg"}
---

# Mystic Software

***Copy-Paste this program in your system.prg ***Add the line #Include("system.prg") on other programs that will ***use this method #Method ModDiv(dividend!,divisor!,remainder!) { #a!=dividend!/divisor! #CastInt(a!,a!) #b!=a!*divisor! #remainder!=dividend!-b! #ReturnMethod(remainder!) } #Method ShowTime(x!,y!) { #hours!=GameTime!/3600 #CastInt(hours!,hours!) #ModDiv(GameTime!,3600,newtime!) #minutes!=newtime!/60 #CastInt(minutes!,minutes!) #ModDiv(newtime!,60,seconds!) #CastInt(seconds!,seconds!) #Text(x!,y!,"::") #Kill(newtime!) #Kill(hours!) #Kill(minutes!) #Kill(seconds!) } #Showtime(2,2)
