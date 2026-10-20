---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/test.php?file=files/selectionprompt.prg&mode=6"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/test.php?mode=6&file=files/selectionprompt.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040910092856"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/test.php__mode_6_file_files_2Fselectionprompt.prg", captured: "20040910092856", sha256: "38812e3ffb2052e95f03dc404b7657939b39ec03e19f3d75d678ec47168f9afc", wayback_url: "https://web.archive.org/web/20040910092856/http://www.mysticsoftware.net/test.php?mode=6&file=files%2Fselectionprompt.prg"}
---

# Mystic Software

#MAXANSWER!=2 *change this to change number of max responses #answer!=1 #while(a$~="ENTER") { *These are your answers to the question *if you need more answers to a question add more if satements *If you get to many answers try either a sorta scrolling deally *or #text command but if you need help with that email me at (redacted: email) #if(answer!==1) { #mwin("How are you feeling?") #mwin(">good!") #mwin("-Go to hell!") #wait(a$) #mwincls() } #if(answer!==2) { #mwin("How are you feeling?") #mwin("-good!") #mwin(">Go to hell!") #wait(a$) #mwincls() } *Tells the promp to goto top of list when Down is pressed *at bottom of the list #if(a$=="DOWN") { #answer!=answer!+1 #if(answer!==MAXANSWER+1) { #answer!=1 } } *Tells promt to goto bottom of list when Up is pressed *at top of the list #if(a$=="UP") { #answer!=answer!-1 #if(answer!==0) { #answer!=MAXANSWER! } } } ************************************************************************ *here is where you put all the responses to the answer of the question.* ************************************************************************ #mwincls() #if(answer!==1) { #mwin("Well thats good!!") } #if(answer!==2) { #mwin("Same to you buddy!!") } ************************************************************************ #wait(a$)
