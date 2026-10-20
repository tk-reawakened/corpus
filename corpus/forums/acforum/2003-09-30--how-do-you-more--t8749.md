---
kind: forum-thread
id: "acforum/8749"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "8749"
title: "How do you ..... More"
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=8749"
written: "2003-09-30T21:41:00"
last_post: "2003-10-01T24:38:00"
date_confidence: "exact"
captured: ["20031023234432", "20031023234816", "20031023235404", "20031023235601", "20031023235819", "20031023235958", "20031024000019"]
author: "janova144"
repliers: ["levi", "kronical", "alex0xander", "nick"]
authors: ["janova144", "levi", "kronical", "alex0xander", "nick"]
posts_present: 7
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_8749", captured: "20031023234432", sha256: "a87746b1181b0400b9e5f6f871df7048825a91362cdf2b580cfb84328044a428", wayback_url: "https://web.archive.org/web/20031023234432/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=8749"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_8751", captured: "20031023234816", sha256: "ae601c1e540b081ab8a2287162908d1fd3ffc8be46d3285b220827a20c8b5bc0", wayback_url: "https://web.archive.org/web/20031023234816/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=8751"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_8759", captured: "20031023235404", sha256: "a804d95625ba0a0d5785336a0fc5d7fdb8162c08d1811a39151e48bdbb75c553", wayback_url: "https://web.archive.org/web/20031023235404/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=8759"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_8760", captured: "20031023235819", sha256: "7a3d7289a6269f8a5a04757136f58fa076fbda41ef3a5a1ae69294b283383ac2", wayback_url: "https://web.archive.org/web/20031023235819/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=8760"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_8762", captured: "20031023235601", sha256: "18521cfa574afe856acd93fd274498ae44f25f609b43751a361060c72c2ef67d", wayback_url: "https://web.archive.org/web/20031023235601/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=8762"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_8764", captured: "20031023235958", sha256: "f56ca7ba9ee5408ce838b1ccdee1db9a979443a05aafa1b33bc340e3ad61eee0", wayback_url: "https://web.archive.org/web/20031023235958/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=8764"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_8765", captured: "20031024000019", sha256: "db5ae63c2ea9fce8734f653c46f52c6d1ff00f365da3fabbebb3413a2688abec", wayback_url: "https://web.archive.org/web/20031024000019/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=8765"}
links: []
---

# How do you ..... More

### janova144 · 2003-09-30 21:41 · #A1001-8749

How do you make a Timed boared you know like you have this much time to finish the board whats the name of that command Thanks
Matt

### levi · 2003-09-30 24:22 · #A1001-8751

**General idea...be better if someone else answered**

All I can tell you right now is that I wish I knew of a command to test time but I guess for that you'll have to use a continuous for loop that countinues to loop then branches to any other programs you have running on the board like NPC(non-playable characters in case you didn't know). I believe the branch command is #FBranch. So yeah like for #TotalTime! = the number of times you want to loop i would guess something like 3000 wouldn't be bad depending on how long you want it to go. But here is a general idea.
#For(TotalTime!=1; TotalTime!<=3000; TotalTime!=TotalTime!+1)
{
#FBranch
}
#Send (board.brd,x!,y! [,layer!])
And send him to a new board when time is up. This program would be the start up program for the board. And that's the general idea. That's all you would need to do. I'm guessing this is for a bonus round or something. Well I hope someone will shed more light on this subject for you. But thanks for the programming practice. Hope you get what you need. Later
"God Rules, Jesus Saves, and I don't care if you don't agree" Thank you and Have a nice day. Levi The tax collector.

### kronical · 2003-10-01 19:58 · #A1001-8759

**Do you discourage yourself in every post? :P (nt)**

---
HELO!1111 OMG MAH NMA IS KR0NICUL AND I PREFER CHIKEN OV3R PEI!111!!11 WTF I DONT AV3N LIEK PEI11111!11 OMG PEI TASTAS LIEK DA CRYPT!1!!!111 OMG

---
AIM: kronspik
MSN: (redacted: email)
EMAIL: (redacted: email)

---

The Toilet Man

Kronical

Daddy look! A real live loser!

### levi · 2003-10-01 20:04 · #A1001-8760

**For the most part why?-nt**

"God Rules, Jesus Saves, and I don't care if you don't agree" Thank you and Have a nice day. Levi The tax collector.

### alex0xander · 2003-10-01 21:57 · #A1001-8762

**Hmmm(mOre)**

Theres no command other than the built in variable for the ridiculous clock(the one in the menu)
You'll have to DL Mr.G's Miscellenous Pack, and use the command #Gettime(time$)
heres how you use it:

```
#GetTime(time1$)          *it doesnt matter what this is

**on another program**

#GetTime(time2$)          *again doesnt matter

#results!=time2!-time1!

#If(reults!>25)           *say the player had 25 seconds to

{                         *get to this place

*what you want to happen

}

#If(result!<=25)          *say the player made it on time

{

*what u want to happen

}
```

hope that helped

### nick · 2003-10-01 23:51 · #A1001-8764

**You should give yourself more credit. -nt**

---

### kronical · 2003-10-01 24:38 · #A1001-8765

**Or at least dont put yourself down in every post. :P (nt)**

---
HELO!1111 OMG MAH NMA IS KR0NICUL AND I PREFER CHIKEN OV3R PEI!111!!11 WTF I DONT AV3N LIEK PEI11111!11 OMG PEI TASTAS LIEK DA CRYPT!1!!!111 OMG

---
AIM: kronspik
MSN: (redacted: email)
EMAIL: (redacted: email)

---

The Toilet Man

Kronical

Daddy look! A real live loser!
