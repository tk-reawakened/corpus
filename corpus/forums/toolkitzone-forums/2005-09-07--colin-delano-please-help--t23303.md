---
kind: forum-thread
id: "toolkitzone-forums/23303"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Toolkit Discussion"
skin: "phpbb2"
thread_id: "23303"
title: "COLIN, DELANO please help!"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=23303"
written: "2005-09-07T22:25:00"
last_post: "2005-09-24T13:36:00"
date_confidence: "exact"
captured: ["20051231090752"]
author: "corim123"
repliers: ["p90m16mp5a4", "Talyn", "Colin"]
authors: ["corim123", "p90m16mp5a4", "Talyn", "Colin"]
posts_present: 10
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_255114_amp_3Bsid_45355ac42e289003771624a4fbcf2992", captured: "20051231090752", sha256: "a93dc1d0a2cc9794ee12eadf194b80e7a05f6da4ab69d1d62d44c022918d7975", wayback_url: "https://web.archive.org/web/20051231090752/http://www.toolkitzone.com/forums/viewtopic.php?p=255114&amp%3Bsid=45355ac42e289003771624a4fbcf2992"}
links: []
---

# COLIN, DELANO please help!

### corim123 · 2005-09-07 22:25 · #B255086

Is it possible to make a game that has a preset kill time in the game that will only run once? If so how do I do this?

### p90m16mp5a4 · 2005-09-07 22:58 · #B255108

You could, but the person could just reinstall the demo and it resets everything.
Actually, lol!! .. Hm...
You would have to open a pre-made file each time, because #DirSav doesn't automatically save.
My idea was, check the gametime, ( gametime is constant numerical variable that keeps how long you have played the game in seconds ) then save, then quit the game. The next time you start the game, you will be forced to load that save game, then the game will quit. But, #DirSave *prompts* you to save. WIch means, you will have to use file I/O ( in rpgcode )to automatically save/load. Sorry, the human could easily figure this out and just reinstall the game.

### corim123 · 2005-09-07 23:02 · #B255114

yes, I already knew this, but it there anyway to force an uninstall of the game when the timer runs out, but how do I even make the timer and is it possible to delete or corrupt the game file when it is done

### p90m16mp5a4 · 2005-09-07 23:21 · #B255126

Ask Colin or Delano.

### corim123 · 2005-09-07 23:26 · #B255129

colin, or delano I need help and that small hosting thing is still on for who ver helps me enough to do this or does it themselves FIRST, there is no second place!

### p90m16mp5a4 · 2005-09-07 23:32 · #B255136

This would most likely be a good task for a regular application, getting it to work on the toolkit, I have no idea, but, if somebody knows how, it would be at least one of those two.

### corim123 · 2005-09-08 12:12 · #B255283

but, do you understand what I'm saying? I want the game to exit after about 10 minutes and then corrupt itself, like someway to place something in the kill code, so as it quits it screws up all toolkit files in the directory

### Talyn · 2005-09-09 14:05 · #B255600

Firstly, what a bloody stupid thing to want to do. Is there any point? Re-installing would fix it immediately.
It would require a plugin, no-one is going to build in a feature like that.

### Colin · 2005-09-10 16:48 · #B256003

I can't see the use for it, as Talyn said. If you want something like shareware, you could use a plugin and not start the game after time runs out, but there's no way to make the game uninstall itself.

### corim123 · 2005-09-24 13:36 · #B259925

Colin, what you said is exactly what I want! How do I do it?
