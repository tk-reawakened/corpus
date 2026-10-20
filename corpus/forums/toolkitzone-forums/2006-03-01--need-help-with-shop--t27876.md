---
kind: forum-thread
id: "toolkitzone-forums/27876"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Code"
skin: "phpbb2"
thread_id: "27876"
title: "NEED HELP WITH SHOP"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=27876"
written: "2006-03-01T17:52:00"
last_post: "2006-03-04T04:46:00"
date_confidence: "exact"
captured: ["20060322050452", "20060328225443", "20060329203311"]
author: "Skyline1250"
repliers: ["zyrshnikashnu", "Demon Lord Tyrus", "p90m16mp5a4", "femi", "brandan34", "whats a computer"]
authors: ["Skyline1250", "zyrshnikashnu", "Demon Lord Tyrus", "p90m16mp5a4", "femi", "brandan34", "whats a computer"]
posts_present: 8
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_302601_amp_3Bsid_a2c41f0cd531d96db8f7e74e56fdc057", captured: "20060329203311", sha256: "7f6ebba942c8023768f9561d699f8af92b959c5f93ae2f46bdcc3d57b1157556", wayback_url: "https://web.archive.org/web/20060329203311/http://toolkitzone.com/forums/viewtopic.php?p=302601&amp%3Bsid=a2c41f0cd531d96db8f7e74e56fdc057"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_303034_amp_3Bsid_c63b7792e6e9ad37c5da692c8bb932e8", captured: "20060322050452", sha256: "d63ecd71c70bef6d4608974d3ba8f84c5a844252df2aadcb3761e3ab868768db", wayback_url: "https://web.archive.org/web/20060322050452/http://toolkitzone.com/forums/viewtopic.php?p=303034&amp%3Bsid=c63b7792e6e9ad37c5da692c8bb932e8"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_303036_amp_3Bsid_2c706f43526c1b26062a830481a3a574", captured: "20060328225443", sha256: "8452cfd292f06ff8da8248cce2570d6771eedaca2d553dae47a1da4faa7f9e98", wayback_url: "https://web.archive.org/web/20060328225443/http://toolkitzone.com/forums/viewtopic.php?p=303036&amp%3Bsid=2c706f43526c1b26062a830481a3a574"}
links: []
---

# NEED HELP WITH SHOP

### Skyline1250 · 2006-03-01 17:52 · #B302543

Ive recently made a shop using callshop() but it has that stupid bug on it. I was wondering if someone could plz make the code of a shop for me plz?

### zyrshnikashnu · 2006-03-01 21:34 · #B302596

Last I heard, callShop() is broken in 3.0.6.
EDIT:
Heh, sorry. I didn't read the request properly.

### Demon Lord Tyrus · 2006-03-01 22:00 · #B302601

Thats what he said, he said it doesnt work so he wants to know if someone will make one fo him.
I would also like to know how to make one, because I need it but ive tried and its not that straight foward :-\

### p90m16mp5a4 · 2006-03-03 03:48 · #B302970

Very straight forward:
[buying]
Show items for sell
Ask for wich item you want to buy
Check the price for that item
If you have enough, use #GiveItem and #TakeGp
If you don't, go back to the first menu
[selling]
Show an inventory of wich items you own. (#ItemCount + design)
Ask wich item you want to sell
Use #GiveGp and #TakeItem
You will actually need to know very very very very very basic RPGcode to make a shop program, like #Mwin, #If, and #Bitmap.

### Demon Lord Tyrus · 2006-03-03 07:49 · #B303034

Yea that would work but it would mean a totally sperate code for the shop in each town/whereever you have it, I want to know how (assuming you can) write a method for a callshop command similar to the original, for example CallmyShop(Item1$, Item2$).

### femi · 2006-03-03 08:09 · #B303036

Why don';t you stick to the original shop but change your shop by modifieying the defualt shop menu use new colours and stuff init??
Cool

### brandan34 · 2006-03-04 04:23 · #B303316

Make a method. If you look in the referace code on this site you should find some costom shops that are in method form. You just call the method, enter what you want the shop to sell, the name of the shop and you have a costom shop that works. Also in the codeshack you can find wintermoon's methods one of which has a very good shop in it.

### whats a computer · 2006-03-04 04:46 · #B303321

i submitted a shop not too long ago, let me see if i can find the code...
