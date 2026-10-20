---
kind: forum-thread
id: "toolkitzone-forums/12564"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "12564"
title: "Multiline Comments"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12564"
written: "2004-12-13T20:50:00"
last_post: "2004-12-14T00:54:00"
date_confidence: "exact"
captured: ["20050119034058"]
author: "TheCPPFreak220"
repliers: ["Levi", "Dont_Think_So", "matt72186"]
authors: ["TheCPPFreak220", "Levi", "Dont_Think_So", "matt72186"]
posts_present: 7
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_139225_amp_", captured: "20050119034058", sha256: "7868dd67076d5b417ff8d15675359afa2d46676ede12a77d4973f24a0cfd7479", wayback_url: "https://web.archive.org/web/20050119034058/http://www.toolkitzone.com/forums/viewtopic.php?p=139225&amp="}
links: []
---

# Multiline Comments

### TheCPPFreak220 · 2004-12-13 20:50 · #B139103

I twould be nice if tk3 supported multiline commants, instead of haveing to comment out every line you don't need one by one

### Levi · 2004-12-13 23:39 · #B139180

Do you mean like word wrapping? OR something of that nature?

### Dont_Think_So · 2004-12-13 23:40 · #B139182

/* This is a comment!
So is this!
Whaddya know! So's this! */
ButThisIsn't()

### Levi · 2004-12-13 23:53 · #B139191

Oh Comments. I keep calling those Remarks after the REM statement that I use in QB. Stupid me.
Though a MWin that supports Word WRapping and continued lines would be a cool update. That way we can simply type out a long line of text that the translator would do the rest for us.

### Dont_Think_So · 2004-12-13 23:57 · #B139193

Could easily be done with the new RPGCode commands.
In fact, I'm putting together a bunch of classes for RPGCode, and I'm probably gonna make an MWin class (CWin, actually).

**Code:**

```
MessageWindow = CWin()

MessageWindow << "This is all one line" << "This is the next line"

MessageWindow->Draw()
```

Everything can be customized, such as x!,y!,w!,h!, profiles, background, and even a local font face and size. All of the parameters are optional, however, and have defaults.

### Levi · 2004-12-14 00:00 · #B139195

Cool. Smile I'll remember that when I switch to 3.x

### matt72186 · 2004-12-14 00:54 · #B139225

**TheCPPFreak220 wrote:**

> I twould be nice if tk3 supported multiline commants, instead of haveing to comment out every line you don't need one by one
>

Yeah that would be nice... I'm gonna put my Syntax Highlighter on hold again until I hear word about if this will be implemented...
I keep having to change my highlighter to match the additions to RPG Code Smile
