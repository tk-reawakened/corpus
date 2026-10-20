---
kind: forum-thread
id: "acforum/1435"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "1435"
title: "Yes, another one, but this one I REALLY need...CBM READ(please)"
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=1435"
written: "2001-12-09T26:05:00"
last_post: "2001-12-10T24:46:00"
date_confidence: "exact"
captured: ["20011230224028", "20011230224951"]
author: "Darq"
repliers: ["MrG"]
authors: ["Darq", "MrG"]
posts_present: 2
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1002_mode_1_msg_1435", captured: "20011230224028", sha256: "ae5505a36abc124ec9a0408ec8f16f263dae3af8662b453db81fd5be461feefb", wayback_url: "https://web.archive.org/web/20011230224028/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=1435"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1002_mode_1_msg_1438", captured: "20011230224951", sha256: "e2f761582dbaa49859659d3f3b676b2cde92e641ad011b7e55caf03d4796d66e", wayback_url: "https://web.archive.org/web/20011230224951/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1002&mode=1&msg=1438"}
links:
  - {url: "http://wind.prohosting.com/~darq/index.html", status: "external", local: null}
---

# Yes, another one, but this one I REALLY need...CBM READ(please)

### Darq · 2001-12-09 26:05 · #A1002-1435

OK, Im making a custom battle system. When you kill the enemy, your supposed to get experience. This is what I have set up to do this now:
#Undefined[experience]!=Undefined[experience]!+exp!
It gives the experience, but it doesnt add t to making your char level up.
IE: I hame it so when you kill a wolf, it gives you 150 exp.
When your lvl 1, you need 100exp to level up. It adds the exp, but you dont level up.
Anyway, my suggestion is to make a command to do this, like
#giveexp("playerhandle$",exp!)
But it HAS to add it towards leveling up, or it will be of no use.
If theres any other way to do this, please TELL ME! :)
Thanks
**[Atomic Computers Homepage](http://wind.prohosting.com/~darq/index.html)**

### MrG · 2001-12-10 24:46 · #A1002-1438

**My plugin has that..(more)**

Download it at tkzone.. It's undocumented, but it works for players.. Like so:
#GiveEXP(handle$,amount!)
Tada.
Mike
