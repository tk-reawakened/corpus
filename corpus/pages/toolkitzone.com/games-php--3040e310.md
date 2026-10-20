---
kind: page
id: "toolkitzone.com/toolkitzone.com/games.php?news=3222"
site: "toolkitzone.com"
title: "Greckel"
original_url: "http://www.toolkitzone.com/games.php?news=3222"
written: "2006-05-16T08:50:00"
date_confidence: "exact"
updated: "2006-05-16T08:50:00"
captured: ["20060518114625"]
author: "greckel"
repliers: []
authors: ["greckel"]
comments_present: 0
f_description: "A Land that was once peaceful was overturned by a man who thought he was doing good. He concernes of himself and only himself. Now one boy must step up and take on the king. An epic adventure!"
f_led_by: "greckel"
f_rating: "1 vote cast"
f_status: "Design"
f_toolkit_version: "3.x"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/games.php__news_3222", captured: "20060518114625", sha256: "731fd3dd674528910298a6d291dcd589435ed92536025365d1c8da89e753c02d", wayback_url: "https://web.archive.org/web/20060518114625/http://www.toolkitzone.com:80/games.php?news=3222&PHPSESSID=ac3f85c25607dc8e7520991b5dda131f"}
---

# Greckel

May 16, 2006, 8:50 am
Design
A Land that was once peaceful was overturned by a man who thought he was doing good. He concernes of himself and only himself. Now one boy must step up and take on the king. An epic adventure!
**Greckel**
by greckel **Just starting and statistics junk**
May 6 2006, 9:31 am
I have pretty much gotten all of my thoughts together. There will be four "Levels" before you get to the king. One being a cave on top of a mountain, Boss is a Necro Mancer. A Pyramid, have not figured out the boss (taking Suggestions) A Underground river lake thing, Boss is a large serpant. And the last is the castle were the king will be. Note: I would like to have the three bosses before that drop 3 keys so that the castle is locked until then, since I'm newer to TK I still have yet to figure out how to make a lock system, but I think I have an idea of how to. I am taking any suggestions anyone may have and I'm waiting for someone to upload a real time that'll keep you on the board, but if not I'll use the default or a random real time -That is it for now
May 6 2006, 10:51 am
A mummy pharo boss? Just a sudgestion. You could have skellingtons, mummies, pharoes, snakes, those little beatly thingies that's name is evading me right now. The list just goes on and on for the pyramid.
May 6 2006, 3:45 pm
Just set a variable like KEYS! for the keys. Once each boss is defeated, you gan use a GiveItem() command to give the player a key and then write KEYS! += 1 And, at the entrance to the boss's castle, just write: If (KEYS! = 3) { send(board title and tile) } else() { mwin("The door is locked...") wait() mwincls() } Or something like that...
May 6 2006, 6:10 pm
Thanks a ton Fuzz I've been wondering that all day!
May 7 2006, 3:47 pm
You're welcome. :)
1 vote cast
[![Cliff Village](games/phpThumb.php?src=../mygames/images/1970/6157.jpg&w=175)](games.php?image=6157)
