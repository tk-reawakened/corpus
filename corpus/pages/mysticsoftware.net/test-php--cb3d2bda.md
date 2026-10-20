---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/test.php?file=files/hpbar.prg&mode=6"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/test.php?mode=6&file=files/hpbar.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040818023458"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/test.php__mode_6_file_files_2Fhpbar.prg", captured: "20040818023458", sha256: "79778b5328de4362f44de84eab1c01e344c8d84473eac79ace6abf34949f6abd", wayback_url: "https://web.archive.org/web/20040818023458/http://www.mysticsoftware.net/test.php?mode=6&file=files%2Fhpbar.prg"}
---

# Mystic Software

#Method HPbar(HPorSMP!, X!, Y!, endY!, Max!, Value!) { #If (HPorSMP!==1) { #Barlength!=Max!+X! #HPLength!=Value!+X! #BarColor!=BarLength!/4 #If (BarColor!>Value!) { #ColorRGB(255,0,0) #Branch(:draw) } #BarColor!=BarColor!+BarLength!/2 #If (BarColor!>Value!) { #ColorRGB(255,255,0) #Branch(:draw) } #ColorRGB(0,255,0) :draw #FillRect(X!, Y!, HPLength!, endY!) #ColorRGB(0,0,0) #DrawRect(X!, Y!, BarLength!, endY!) #Kill(Value!) #Kill(X!) #Kill(Y!) #Kill(endY!) #Kill(Max!) #Kill(BarLength!) #Kill(BarColor!) #Kill(HPorSMP!) } #If (HPorSMP!==2) { #Barlength!=Max!+X! #SMPLength!=Value!+X! #ColorRGB(0,0,255) #FillRect(X!, Y!, SMPLength!, endY!) #ColorRGB(0,0,0) #DrawRect(X!, Y!, BarLength!, endY!) #Kill(Value!) #Kill(X!) #Kill(Y!) #Kill(endY!) #Kill(Max!) #Kill(BarLength!) #Kill(BarColor!) #Kill(HPorSMP!) } }
