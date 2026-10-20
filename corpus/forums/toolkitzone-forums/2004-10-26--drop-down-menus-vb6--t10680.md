---
kind: forum-thread
id: "toolkitzone-forums/10680"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "10680"
title: "Drop Down Menus (VB6)"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=10680"
written: "2004-10-26T20:57:00"
last_post: "2004-10-27T01:23:00"
date_confidence: "exact"
captured: ["20041226085948"]
author: "Mainiac"
repliers: ["Levi", "Colin", "Compugeek", "nova11"]
authors: ["Mainiac", "Levi", "Colin", "Compugeek", "nova11"]
posts_present: 9
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_117521_amp_", captured: "20041226085948", sha256: "4e9976b90e15769d219871cbf15522afa46ee3e419653feb19f9ad94cbc137ef", wayback_url: "https://web.archive.org/web/20041226085948/http://www.toolkitzone.com/forums/viewtopic.php?p=117521&amp="}
links: []
---

# Drop Down Menus (VB6)

### Mainiac · 2004-10-26 20:57 · #B117402

How do you create a drop down menu in VB6? if so how?

### Levi · 2004-10-26 21:50 · #B117420

Drop down menu? Do you mean when you right click a menu appears?
Or a regular menu like you see on other programs? Because a regular menu is easy enough just use the menu editor. I'm not sure about the other way. I can look it up though.

### Colin · 2004-10-26 21:53 · #B117421

Use the PopupMenu function...
Call PopupMenu(theMenu)

### Levi · 2004-10-26 22:29 · #B117449

Ah yes, the PopUpMenu method. Thank you KNSiloc.
If you don't get what KNSiloc put up let me go into depth.
On your menu bar, you more than likely put stuff like File Edit and so on. Now you also probably named them like, mnuFile and mnuEdit
Well with the PopupMenu you call
PopupMenu mnuEdit
and it will pull up the edit menu at the position of the mouse.
Each menu must have a submenu attached to it.
If you want menu options that aren't on your main menu bar simply create the menus like normal except change their visible properties to off. Basically deselect the menu.
And wallah you have a popupmenu.

### Colin · 2004-10-26 22:33 · #B117454

The word is volia + accent grave on the last letter.
People, learn the spell Razz

### Levi · 2004-10-26 23:24 · #B117471

I want wallah...Its my way of doing it. Like wallah wallah washington.

### Compugeek · 2004-10-26 23:54 · #B117483

**KSNiloc wrote:**

> The word is volia + accent grave on the last letter.
> People, learn the spell Razz
>

If I'm not mistaken, it should be voilà Razz
Your last sentence is ironic.

### nova11 · 2004-10-27 01:21 · #B117518

KSN nevers does things spontanous. Or wrong.

### Levi · 2004-10-27 01:23 · #B117521

Neither do I...of course that's by opinion alone. Its rare for humans to get things right, even when they do it tends to be wrong.
I like programming as an example, there is always an easier way to do things in the end, but its the long ways that make for the best programming. And then its the long ways that leave you open to more errors.
