---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/help.php?article=7&mode=1"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://mysticsoftware.net/help.php?mode=1&article=7"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040504142512"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/help.php__mode_1_article_7", captured: "20040504142512", sha256: "31473657911a946648b517d3a84d6c818304567afe6d3c77cff6db30238f7832", wayback_url: "https://web.archive.org/web/20040504142512/http://mysticsoftware.net/help.php?mode=1&article=7"}
---

# Mystic Software

- Custom Commands- Written By Don't_Think_So This tutorial teaches you how to create custom commands that can be used anywhere, as if they were regular commands. Here is an example that uses three sets of custom commands: #mycommands.glowtext(12,14,1,5,"test") #myotherprghere.blah(1) #someotherproggiehere.ummm(grrr) #thisismyotherproggieofassortedmiscellany.doesn't_this(stink) #wait(a$) Now, you can see how this can get very tedious. Well, with this rather short tut, this will be no more! It is very very very simple. Just #redirect all of your custom commands in your start program. I put it right before it draws the title screen. Here is how it goes in my game: *my custom commands | name of | where the * V new command V method is #redirect(#glowtext,#mycommands.glowtext) #redirect(#randomrange,#mycommands.randomrange) #redirect(#pause,#mycommands.pause) #redirect(#redshade,#mycommands.redshade) #redirect(#greenshade,#mycommands.greenshade) #redirect(#blueshade,#mycommands.blueshade) #redirect(#yesno,#mycommands.yesno) #redirect(#charcount,#mycommands.charcount) #redirect(#findstring,#mycommands.findstring) #redirect(#toggle,#mycommands.toggle) #redirect(#drawbar,#mycommands.drawbar) #redirect(#bossbattle,#mycommands.bossbattle) #redirect(#time,#mycommands.time) #redirect(#slowzoom,#mycommands.slowzoom) #redirect(#virtbutton,#mycommands.virtbutton) #redirect(#virtcheck,#mycommands.virtcheck) #redirect(#virtclear,#mycommands.virtclear) #redirect(#fp,#mycommands.fp) #redirect(#dp,#mycommands.dp) *end of custom commands Now, all of my custom commands can be used as normal. Meanwhile, on another program: #glowtext(12,15,5,1,"Isn't this better?") #redshade(1,5,"because i think so") #greenshade(5,5,"wouldn't you agree?") #yesno(maybeso!) #if(maybeso!==1) { I thought you would } #if(maybeso!==0) { Really? Then you shouldn't be reading this tutorial. } #wait(a$) See, isn't that better than having to remember all of those #include commands at the top of every program? See you on the battlefield (oops, wrong saying). -Dont_think_so
