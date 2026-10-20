---
kind: forum-thread
id: "toolkitzone-forums/22013"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Code"
skin: "phpbb2"
thread_id: "22013"
title: "Paperdoll Tutorial"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=22013"
written: "2005-08-01T12:00:00"
last_post: "2005-08-03T15:04:00"
date_confidence: "exact"
captured: ["20051212120151", "20051212120218", "20060108101353"]
author: "William"
repliers: ["Noob From The Grave"]
authors: ["William", "Noob From The Grave"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_240476_amp_3Bsid_574e6977300314576ef6f8c13247fa59", captured: "20051212120151", sha256: "94a17ccbb4aecc6ebebbd576983fabd6142ffa70acee10dfae71dd6aef0b6999", wayback_url: "https://web.archive.org/web/20051212120151/http://www.toolkitzone.com/forums/viewtopic.php?p=240476&amp%3Bsid=574e6977300314576ef6f8c13247fa59"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_240479_amp_3Bsid_574e6977300314576ef6f8c13247fa59", captured: "20051212120218", sha256: "8bb20e1fdb26d4f922f40c96fb138413e74f8fcf1c663ec5d756aa2a913724b7", wayback_url: "https://web.archive.org/web/20051212120218/http://www.toolkitzone.com/forums/viewtopic.php?p=240479&amp%3Bsid=574e6977300314576ef6f8c13247fa59"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_241194_amp_3Bsid_574e6977300314576ef6f8c13247fa59", captured: "20060108101353", sha256: "5eba0cc6dcf0cf11dfbd9680c34da2750f403421f9457d9dfcd6512cba205817", wayback_url: "https://web.archive.org/web/20060108101353/http://www.toolkitzone.com/forums/viewtopic.php?p=241194&amp%3Bsid=574e6977300314576ef6f8c13247fa59"}
links: []
---

# Paperdoll Tutorial

### William · 2005-08-01 12:00 · #B240476

By: William
Difficult: 8/10
Description: Not a full copy and paste tutorial.
This is very easy way to make a paperdoll effect, not sure it works thought. And I kind of forgot the commands and names for it. But I try to explain. First make sure you have a sprite with no cloths, and items that fit good on him.
Then find the commands for the thing that runs while the character walk. You know you can code rain, snow etc.. that kind of commands that make it run at the same time. And it still run even if you walk to another map.
So, in that command. Put something like this (by the way you need a custom item system or you might be able to run a command like this in the item when it's equipped: armor!=1):

**Code:**

```
if armor! = 1

{

GetPlayerDir(dir$)

If dir$ = "SOUTH"

{

Getplayercorrds(map$,x!,y!)

setimagetransparent("armorsouth.bmp",x!,y!...)

}

}
```

And check so that it is on the right place on the character.

### Noob From The Grave · 2005-08-01 12:06 · #B240479

How would you do walking anims though capes and swords etc arnt static when walking,Good though, although all the armours,swords and other items have to be excatly the same size for it to work.

### William · 2005-08-03 15:04 · #B241194

For moving the items, just type them out with a tiny delay:

**Code:**

```
If dir$ = "SOUTH"

{

Getplayercorrds(map$,x!,y!)

setimagetransparent("armorsouth.bmp",x!,y!...)

minidelay(25)

setimagetransparent("armorsouth1.bmp",x!,y!...)

minidelay(25)

setimagetransparent("armorsouth2.bmp",x!,y!...)

}

method minidelay(index!)

{

for (loop! = 1; loop! < index! ; loop! < index!)

{

'keep this empty

}

}
```

I'm a little bit blury since I'm coding all VB now, so I kind of want to write: If dir$ = "SOUTH" then and all those things. So you might need to change it more. But it should do the walking.

**Quote:**

> although all the armours,swords and other items have to be excatly the same size for it to work.
>

Same size? not really..
Going to update the tutorial if more people is interested. Any other coding requests (no bs or ms).
