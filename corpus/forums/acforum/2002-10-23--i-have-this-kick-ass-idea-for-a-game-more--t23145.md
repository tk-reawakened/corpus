---
kind: forum-thread
id: "acforum/23145"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "23145"
title: "i have this kick ass idea for a game.... more"
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=23145"
written: "2002-10-23T19:21:00"
last_post: "2002-10-23T22:37:00"
date_confidence: "exact"
captured: ["20021128063035", "20021128063337", "20021128063456", "20021128063811"]
author: "goldenretrogamer"
repliers: ["qwerty", "mrsaturn"]
authors: ["goldenretrogamer", "qwerty", "mrsaturn"]
posts_present: 4
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_23145", captured: "20021128063337", sha256: "183c48a3afd362726c6e6541da7dd0b949f5791fbc80b532c18c3062ff8acfb7", wayback_url: "https://web.archive.org/web/20021128063337/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=23145"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_23146", captured: "20021128063035", sha256: "19aea8b033f5433a8a065c08f637fc0deb65d639b77c642ccad43da27d78e4d6", wayback_url: "https://web.archive.org/web/20021128063035/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=23146"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_23151", captured: "20021128063811", sha256: "489e8071c932010c5bcd30b5a164874e7c8b1493a26327b0eda763d4db85d1ab", wayback_url: "https://web.archive.org/web/20021128063811/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=23151"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_23160", captured: "20021128063456", sha256: "0cb96d99bc64bec59eaf3ebb2a9356db39c682bd279180f00c1a7cb335169bea", wayback_url: "https://web.archive.org/web/20021128063456/http://www.rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=23160"}
links: []
---

# i have this kick ass idea for a game.... more

### goldenretrogamer · 2002-10-23 19:21 · #A1001-23145

its called teacups. its on the classic apple machines, and its so adictive.
the aim of the game is to sell tea!!. yea tea! i wanna make this game in toolkit, but i dont know where to start.
this is how the game works. it has 2 different types of days, sunny and rain. you start off with some money, say 10 pounds.
at the start of the game, 1 cup of tea would cost around 10 to make and would sell for something like 15p. each level the tea cost more to make.
you are more likely to sell tea on a sunny day.
there are some events stopping you from selling tea like-
#walls ice cream vans stole your trade
#theer was a freak thunder storm etc etc.
the amount of teas you sell is random, but you are more likely to sell more teas when its sunny, the opposite for rain.
i really wanna make this game, itill make my day.
i have tried playing around with toolkit, but i dont really no where to start.
thank you very much for any help!
keep it ReTrO

### qwerty · 2002-10-23 19:25 · #A1001-23146

**um... great game!(sarcastic) (nt)**

*(no text captured)*

### goldenretrogamer · 2002-10-23 19:55 · #A1001-23151

**ha hato scared to put your real name. dumass.**

keep it ReTrO

### mrsaturn · 2002-10-23 22:37 · #A1001-23160

**Will this help?**

If you want it to randomly choose whether it is raining or sunny, you might want to place a program somewhat like this at the exit of your guy's house:
#Random(2,dest$)
#If(dest$==1)
{
#Mwin("Yay, it's sunny outside!")
#Send("sunny_town.brd",5,5,1)
}
#If(dest$==2)
{
#Mwin("Oh no, it's raining!")
#Send("rainy_town.brd",5,5,1)
}
Hop that helps!
