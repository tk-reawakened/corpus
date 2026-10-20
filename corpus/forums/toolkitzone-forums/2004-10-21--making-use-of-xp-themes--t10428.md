---
kind: forum-thread
id: "toolkitzone-forums/10428"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "10428"
title: "Making Use of XP Themes"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=10428"
written: "2004-10-21T00:01:00"
last_post: "2004-10-25T08:07:00"
date_confidence: "exact"
captured: ["20041226085658"]
author: "Compugeek"
repliers: ["Colin", "Marc", "Colosseus"]
authors: ["Compugeek", "Colin", "Marc", "Colosseus"]
posts_present: 8
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_116663_amp_", captured: "20041226085658", sha256: "52fc395c5f089e4687c086aa3f6959ff5bc27e4c470eb6685113ec317adad39e", wayback_url: "https://web.archive.org/web/20041226085658/http://www.toolkitzone.com/forums/viewtopic.php?p=116663&amp="}
links:
  - {url: "http://vbnet.mvps.org/index.html?code/forms/vbidexp.htm", status: "external", local: null}
---

# Making Use of XP Themes

### Compugeek · 2004-10-21 00:01 · #B113994

In Visual Basic 6, you are pretty much stuck with the old Windows 98 look and feel, right? Wrong, thanks to this article Cool
<http://vbnet.mvps.org/index.html?code/forms/vbidexp.htm>
Now, assuming you are running Windows XP, you can give your controls and even final .exe files the XP look and feel!

### Colin · 2004-10-21 00:57 · #B114064

You're kidding right?
Many people knew about embedding manifest files as resources ages ago -- in fact in non-.net langauges you still have to do it.

### Marc · 2004-10-21 00:58 · #B114066

Was Ages and Ages ago 5 minutes for me?

### Colin · 2004-10-21 01:02 · #B114072

What I meant was compugeek made this sound like something revolutionary and new Razz

### Marc · 2004-10-21 01:16 · #B114080

Oh. Why am I taking things the wrong way lately?

### Colosseus · 2004-10-24 23:02 · #B116421

Bah, giving it the XP look was a cakewalk in delphi =P
All I needed was to compile the manifest into a .RES file, then add the .RES file to the design-time VCL package, and include the following line in my app:
{$R WindowsXP.RES}
That's how easy it's supposed to be! =D

### Colin · 2004-10-25 00:02 · #B116463

That's how easy it is in VB too. I hate VB, Colosseus, but if you want to make Delphi sound good, know what you are talking about, yes? Smile

### Colosseus · 2004-10-25 08:07 · #B116663

Damn. My secret intentions were disclosed. Plan B, plan B!
... However, I never ever said VB couldn't do that too, I just said Delphi indeed could. So I know what I'm talking about ;=p
