---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/files/gametime.prg"
site: "mysticsoftware.net"
title: ""
original_url: "http://mysticsoftware.net/files/gametime.prg"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040504142325"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/files/gametime.prg", captured: "20040504142325", sha256: "2110c2e0b8bc4a6765c422d815dced9dfa2aa0e2f17dfb0f280db07ba4166f74", wayback_url: "https://web.archive.org/web/20040504142325/http://mysticsoftware.net/files/gametime.prg"}
---

# (untitled)

") *#Text(46,42.8,"Days: Time: : ") ********************************* #Method GameTime() { #ttime!=GameTime! #CastInt(ttime!,ttime2!) #hour2!=ttime2!/3600 #min2!=ttime2!/60 #day2!=ttime2!/86400 #CastInt(hour2!,hour!) #CastInt(min2!,min!) #CastInt(day2!,day!) :time #IF(hour!>23) { #hour!=hour!-24 #Fbranch(:time) } #If(min!>59) { #min!=min!-60 #Fbranch(:time) } } **********NOTE********** *To do FF type time (ie hours:minutes, without days) *just comment out the entire #IF(hour!)etc command and don't put in the *day! variable in the #Text command that displays time, example: *comment it out like this... *#IF(hour!>23) *{ *#hour!=hour!-24 *#Fbranch(:time) *} ************************ *and the Text command should look like this... *#Text(46,42.8,"Time: : ")
