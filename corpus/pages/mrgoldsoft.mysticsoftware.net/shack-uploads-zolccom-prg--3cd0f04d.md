---
kind: page
id: "mrgoldsoft.mysticsoftware.net/mrgoldsoft.mysticsoftware.net/shack/uploads/zolccom.prg"
site: "mrgoldsoft.mysticsoftware.net"
title: ""
original_url: "http://mrgoldsoft.mysticsoftware.net/shack/uploads/zolccom.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20030905043537"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/mrgoldsoft.mysticsoftware.net/shack/uploads/zolccom.prg", captured: "20030905043537", sha256: "e398fb5a3f038aced7f49ec149df16d1e8eec9cbb7022e7920c6cc205b216cff", wayback_url: "https://web.archive.org/web/20030905043537/http://mrgoldsoft.mysticsoftware.net/shack/uploads/zolccom.prg"}
---

# (untitled)

lines!+1) {#Branch(:done)} } } #com$="#" #for(pos!=9;chr$~="(";pos!=pos!+1) { #com$=com$+chr$ #charat(prog[line!]$,pos!,chr$) #if(chr$="") {#Branch(:out)} } :out #Redirect(com$,"#"+progname$+"."+com$) #Branch(:nextcommand) :done #killmore("line!,lines!,com$,progname$,prog$,pos!,chr$") }
