---
kind: forum-thread
id: "acforum/7294"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "7294"
title: "Help me please?"
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=7294"
written: "2002-02-04T09:03:00"
last_post: "2002-02-04T10:59:00"
date_confidence: "exact"
captured: ["20020214082813", "20020214090305"]
author: "Zaedite"
repliers: ["~Bløb dÙdÉ~"]
authors: ["Zaedite", "~Bløb dÙdÉ~"]
posts_present: 2
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_7294", captured: "20020214090305", sha256: "7268eb5c6d1a75bd85560f4275ffafd93e701689f0cb522626d6a65c2b89db3b", wayback_url: "https://web.archive.org/web/20020214090305/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=7294"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_7296", captured: "20020214082813", sha256: "38bb7b0d36c0f67bca0e751a002d76d53c4b44fcf067b933d7d4882778f3ab81", wayback_url: "https://web.archive.org/web/20020214082813/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=7296"}
links:
  - {url: "http://www.angelfire.com/rpg2/the-blobs/Blobs_link_Banner.txt", status: "external", local: null}
---

# Help me please?

### Zaedite · 2002-02-04 09:03 · #A1001-7294

Can someone help me please?
I made simple programs for two additional people to join the team. I simply made them both appear as images of people, and set their tiles to solid. Here is the first problem: After one person joins, the other is nowhere to be seen, and their program will not activate, leaving a blank square which cannot be walked over. I tried activating one, and it worked but the second vanished (they are on different screens), then reopened and tried the other one first, but then the first one vanished.
Also, I was wondering if someone can help me with the code a bit. If, for example, there was an item called Eggnog (that'll do for the sake of the hypothetical situation), and a person was saying "How I'd love an eggnog...". Then if you talk to them while carrying it, it disappears and the person joins your group, or gives you gold and xp (different quests), what would the code be? I've tried many types, but none worked.
Another problem is that no matter what I try, I cannot get it to make a character move about and vanish. That's why I was using a standard image on a solid tile for the programs of those who join the team.

### ~Bløb dÙdÉ~ · 2002-02-04 10:59 · #A1001-7296

**try this....**

#Mwin("GUY: i'd love some eggnog...")
#wait
#if(goteggnog!=1)
{
#Mwin("GUY: hey you've got some eggnog! i love u!")
#wait
#addplayer(eggnog guy.tem)
#end
}
#If(goteggnog!=0)
{
#Mwin("GUY: Bah, come bak when u have some eggnog!")
#wait
}
Now all u gotta do is make a program to run when u pick up the item(eggnog), with the varible #goteggnog!=1 in it. thats it.
[![](http://www.angelfire.com/rpg2/the-blobs/Blobs_link_Banner.txt)
Action, Disguises and a whole host of weird characters!
