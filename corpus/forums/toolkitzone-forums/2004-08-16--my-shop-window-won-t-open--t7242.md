---
kind: forum-thread
id: "toolkitzone-forums/7242"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "7242"
title: "My shop window won't open"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=7242"
written: "2004-08-16T01:20:00"
last_post: "2004-08-16T08:00:00"
date_confidence: "exact"
captured: ["20040925161850"]
author: "imbeingstocked"
repliers: ["guest 2", "Guest"]
authors: ["imbeingstocked", "guest 2", "Guest"]
posts_present: 4
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_76417_amp_", captured: "20040925161850", sha256: "766201f4a3b0c17e732ae8d258a5aa1cbab1d97141586d9fbfbf4184e945a510", wayback_url: "https://web.archive.org/web/20040925161850/http://www.toolkitzone.com:80/forums/viewtopic.php?p=76417&amp"}
links: []
---

# My shop window won't open

### imbeingstocked · 2004-08-16 01:20 · #B76238

i have set up a shop on my board and a with a small conversation. the conversation comes up but the shop window doesnt!!!

### guest 2 · 2004-08-16 01:25 · #B76243

u did put the program 2 open a store on right

### Guest · 2004-08-16 01:45 · #B76258

Here is an ok code for it change the coversation if u want
#mwin("Owner:What do you want to buy?")
#delay(1)
@
#mwin("1 - weapons")
#mwin("2 - armor")
#mwin("3 - items")
#mwin("4 - never mind")
#wait(a!)
#if(a!==1)
{
#callshop("wooden sword.itm","Short sword.itm","Long sword.itm")
}
#if(a!==2)
{
#callshop("armor1.itm","armor2.itm","armor3.itm")
}
#if(a!==3)
{
#callshop("Herb.itm","Pixy dust.itm","Super Herb.itm")
}
#if(a!==4)
{
#mwin("Owner:Come back anytime!")
#wait()
#mwincls()
#end()
}

### imbeingstocked · 2004-08-16 08:00 · #B76417

well, im using that prg for my shop, its much better than the one i had!! but once i press the number for my decision, it doesnt do anything. the text just goes off the screen and I can walk freely around Sad what is the program 2 thingy that you were talking about?
