---
kind: forum-thread
id: "toolkitzone-forums/23137"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Code"
skin: "phpbb2"
thread_id: "23137"
title: "Custom Item Menu"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=23137"
written: "2005-09-02T18:03:00"
last_post: "2005-10-05T20:37:00"
date_confidence: "exact"
captured: ["20051231090455"]
author: "Noob From The Grave"
repliers: ["p90m16mp5a4", "Dont_Think_So", "ddl2829"]
authors: ["Noob From The Grave", "p90m16mp5a4", "Dont_Think_So", "ddl2829"]
posts_present: 6
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_253265_amp_3Bsid_9f847637d8a3530c1ce1f2df541e63e2", captured: "20051231090455", sha256: "645e6de7e2475e93c1cd61b5ee6051d927700a6b2a743362d5545962d372e074", wayback_url: "https://web.archive.org/web/20051231090455/http://www.toolkitzone.com/forums/viewtopic.php?p=253265&amp%3Bsid=9f847637d8a3530c1ce1f2df541e63e2"}
links: []
---

# Custom Item Menu

### Noob From The Grave · 2005-09-02 18:03 · #B253169

Ok i've read most of the recent threads to do with this but none give any clear help.
Problem:I need to create a method that gets the item in "Slot1" and puts it into a variable
Problem2:Creating a method that checks what class the item is ie:Equip,menu,battle etc
Problem3:Getting the stats of an item
If i can solve these poblems i can do the rest, but so far i havent been able to think of any ways to achieve the above.

### p90m16mp5a4 · 2005-09-02 22:56 · #B253265

What do you mean by stats? There isn't any way to check what the item does. Neither is there a way to use an item. By making a program that creates a custom-menu friendly item and runs when you pick up one of the default items, you can achieve your goal. Unless the variable is hidden somewhere, there isn't one in RPGcode that you can access the information of items in your bag. You can count how many of one item you have, but thats all. The only items with visible 'slots' are the ones you can equip, 0-16 if I remember right..
Every time you get an item, make a copy of that item in rpgcode. This allows you to literally use items anytime. Now, since you have two copies of the same item, you have to balance them evenly. If you use an item in the default bs or ms, make sure you get rid of one of the virtual items. If you use one of the virtual items, take away the real item.

### Noob From The Grave · 2005-09-03 13:14 · #B253423

Ok thank you for that, i can now get one part done displaying the items, however using them as you said there isnt a command that lets you define what type the item is, so menu usage is impossible.
Can i ask how other people do it? not the code just the general idea, do all games with a CMS have a Custom Item System?

### Dont_Think_So · 2005-09-03 18:44 · #B253478

People generally make a new way of handling items that allows them to grab whatever information they want from them. The best way, in my opinion, is to make classes that represent the items, allowing you to cycle through items (and automatically modify arrays when items created or destroyed). Smile

### Noob From The Grave · 2005-09-03 22:54 · #B253563

I was going to make a custom item system however it wouldn't be fully functionable in battle without a CBS which i'm not prepared to code at this time, thanks for all the help but i'm going to try using the default system of items but finding a way to contain certain information, i'll see what comes out of it.

### ddl2829 · 2005-10-05 20:37 · #B262676

there is a item system program i wrote. it will work with any game. go to my post above and go to the link to get the full code. it uses mrg's misc. plugin though
