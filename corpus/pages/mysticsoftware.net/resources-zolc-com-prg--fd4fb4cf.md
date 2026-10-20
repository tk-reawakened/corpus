---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/resources/zolc-com.prg"
site: "mysticsoftware.net"
title: ""
original_url: "http://mysticsoftware.net/resources/zolc-com.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20221201110641"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/resources/zolc-com.prg", captured: "20221201110641", sha256: "7705e934bb78ca373f46392ab356dd692a66634ae3757fad38811f374d68fb7d", wayback_url: "https://web.archive.org/web/20221201110641/http://mysticsoftware.net/resources/zolc-com.prg"}
---

# (untitled)

lines!+1) {#Branch(:done)} } } #com$="#" #for(pos!=9;chr$~="(";pos!=pos!+1) { #com$=com$+chr$ #charat(prog[line!]$,pos!,chr$) #if(chr$="") {#Branch(:out)} } :out #Redirect(com$,"#"+progname$+"."+com$) #Branch(:nextcommand) :done #kill(line!) #kill(lines!) #kill(com$) #kill(progname$) #kill(prog$) #kill(pos!) #kill(chr$) } #Method WaitFor(key$) { #user$="" #While(user$~=key$) { #Wait(user$) } #kill(user$) #kill(key$) } #Method SetUpZolcos() { #Redirect("#Levelup","#zolc-com.Levelup") #Redirect("#Name","#zolc-com.Name") #Redirect("#zcursor","#zolc-com.zcursor") #Redirect("#GoMulti","#zolc-com.GoMulti") #Redirect("#GlobalInclude","#zolc-com.GlobalInclude") #Redirect("#WaitFor","#zolc-com.WaitFor") }
