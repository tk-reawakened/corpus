---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/resources/zolccom.prg"
site: "mysticsoftware.net"
title: ""
original_url: "http://www.mysticsoftware.net/resources/zolccom.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20220126072149"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/resources/zolccom.prg", captured: "20220126072149", sha256: "e398fb5a3f038aced7f49ec149df16d1e8eec9cbb7022e7920c6cc205b216cff", wayback_url: "https://web.archive.org/web/20220126072149/http://www.mysticsoftware.net/resources/zolccom.prg"}
---

# (untitled)

lines!+1) {#Branch(:done)} } } #com$="#" #for(pos!=9;chr$~="(";pos!=pos!+1) { #com$=com$+chr$ #charat(prog[line!]$,pos!,chr$) #if(chr$="") {#Branch(:out)} } :out #Redirect(com$,"#"+progname$+"."+com$) #Branch(:nextcommand) :done #killmore("line!,lines!,com$,progname$,prog$,pos!,chr$") }
