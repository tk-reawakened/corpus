---
kind: blog
id: "toolkitzone.com/2317"
site: "toolkitzone.com"
title: "3/16/05 Going out to the world for the first time"
original_url: "http://toolkitzone.com/blog.php?mode=view&entry=2317"
written: "2005-03-16"
date_confidence: "day"
updated: null
captured: ["20060618040422", "20060621145835"]
author: "John@aljo"
repliers: []
authors: ["John@aljo"]
comments_present: 0
f_interests: "puters"
f_joined: "January 28, 2004"
f_location: "(redacted: location)"
f_username: "John@aljo"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/blog.php__mode_view_entry_2317", captured: "20060618040422", sha256: "48b3ec9794ab02ac84ab395660aea311afa7849399822defc23c956a411d655f", wayback_url: "https://web.archive.org/web/20060618040422/http://toolkitzone.com:80/blog.php?mode=view&entry=2317&PHPSESSID=44bc58a5568eb5ae2253d29aa35da30b"}
  - {path: "wayback/toolkitzone.com/blog.php__mode_view_view_comment_entry_2317", captured: "20060621145835", sha256: "f25398f919d15bf6cf49b9f095f5dd3708578e83b309ae338466b6847c5cc1c2", wayback_url: "https://web.archive.org/web/20060621145835/http://toolkitzone.com:80/blog.php?mode=view&view=comment&entry=2317&PHPSESSID=44bc58a5568eb5ae2253d29aa35da30b"}
---

# 3/16/05 Going out to the world for the first time

by John@aljo on March 16, 2005
Well all I been doing today is working on this chat of mine. I kinda dred that I got work tommarrow because I am so close to finishing for the first release of the chat. It isn't going to sport that admin panel but it does include wonderful things such as talking, whispering, emoting, kicking, and banning (temporarily or endless). Atm can't think of everything that it has and hopefully am not forgetting anything really important, but I do know this. It worthy of being used. Maybe Ill stay ulp and add a few more things so I can get it out soon. I can't tommarrow or friday because they are early to bed and early to rise type days. This day has been a good day for the chat. Allan and I went snooping around for bugs and found a few. I was able to add the blocking system. Talk about being a pain in the ass. The concept of it allowing to block a person for a certain amount of time was a tricky one. Now an admin can type in something along the lines of "/ban Word32 15" to ban Word32 for 15 minutes. If the server for some reason has to be shut down, every banned user is saved and when the server comes back up, is resumed where they left off on their time limit. If you neglect the time limit or type something other than a number it will set the ban limit for FOREVER. in which case you must type /unban user to undo. I spent 2 hours in that area alone trying to find why I was logging out when I unbanned someone. turned out I forgot to add a break; to the end of the case statement so it was moving on to the DISCONNECT case. That is what most of the day was spent on right there was the Banning capability. I just want to see this thing working out in the real world... and soon.
March 17 2005, 11:27 am
Sounds good. /Ban Vampz 15 :P
March 17 2005, 11:27 am
Just 15? /ban R043482 043482
March 17 2005, 1:09 pm
Jokes on you! I'll... log onto another account! Huzzah! (Something you should fix where people are banned from the chat from their IP. Not account)
March 17 2005, 3:37 pm
or Both. People that have dial up change IP every time he/she connects.
March 18 2005, 4:37 am
one problem with banning by Ip. some people have more than one person using a connection. Take my example, Allan and I both use the same cable connection so lets say I get banned, so does Allan
March 18 2005, 11:07 am
But you two aren't going to get banned. :P It'll be an 'unfortunate' side effect that when, for example, word32 gets banned, so does his 'brother' Master_RPG
![](forums/images/avatars/854920603444e76d660439.png)
Aug 24, 2005
Aug 18, 2005
