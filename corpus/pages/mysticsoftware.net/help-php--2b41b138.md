---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/help.php?article=14&mode=1"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/help.php?mode=1&article=14"
written: null
date_confidence: "unknown"
updated: null
captured: ["20041106123721"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/help.php__mode_1_article_14", captured: "20041106123721", sha256: "62d141cbb63b8c141c54caf4aaa09e2d808f723ab8af6a47b4a564a45ffd0123", wayback_url: "https://web.archive.org/web/20041106123721/http://www.mysticsoftware.net/help.php?mode=1&article=14"}
---

# Mystic Software

If your like me, then maybe at some point or another you have wanted to change a command very slightly, like if you wanted to know the current font size, you could look at a variable (say fontsize!) that was automatically stored with the #fontsize command. So, maybe you want something like this: #mwin("The current font size is
- Modified Commands- Written By Don't_Think_So
!") #prompt("What would you like it to be?",picksize!) #fontsize(picksize!) #mwin("Here is font size . Do you think it is better?") As you could see, this has quite some ability. For example, you could make a #save command that doesnt save cheats. Ok, now do I have your attention? Good. So, we start by making a method. Following our #fontsize command... #method modifiedfontsize(size!) { #fontsize!=size! #killredirect(#fontsize) #fontsize(size!) #redirect(#fontsize,#mymodcommands.modifiedfontsize) } Now, most people would, at this point, take you step-by-step through this bit of code, but I think your smart enough to know that it basically puts the variable size! into fontsize!, then runs the command as normal, through the #redirect and #killredirect commands. If you are lost, here is another example: #method modifiedsav(destsave$) { #if(cheathpmod!=1) { #givehp("You",-900) *this assumes that you made a cheat that gave you 900 health, and it only *worked once. } #killredirect(#save) *gives the toolkit the ability to use the normal command #save(destsave$) *uses the normal command #redirect(#save,#mymodcommands.modifiedsave) *makes the toolkit run through this same process next *time. } Just read the comments. You'll understand. -Dont_Think_So
