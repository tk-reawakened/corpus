---
kind: forum-thread
id: "acforum/14254"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "14254"
title: "Character Join"
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=14254"
written: "2002-06-05T28:26:00"
last_post: "2002-06-05T28:43:00"
date_confidence: "exact"
captured: ["20020620164807", "20020620164944"]
author: "orangesoda"
repliers: ["jer1400"]
authors: ["orangesoda", "jer1400"]
posts_present: 2
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_14254", captured: "20020620164807", sha256: "3a4a9382e8d4379c6e681af56a8dd76b47fd046eacc503018e6b0905f484c584", wayback_url: "https://web.archive.org/web/20020620164807/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=14254"}
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_14255", captured: "20020620164944", sha256: "cc897d29566891aaff815d09d3803d1d4a54c17e060786e7f68056dc2033d4b6", wayback_url: "https://web.archive.org/web/20020620164944/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=14255"}
links: []
---

# Character Join

### orangesoda · 2002-06-05 28:26 · #A1001-14254

I have entered this code that someone gave me, and I cant figure out how to fix it:
#if fightB! = 0
{
#MWin("I tell ya wut, fight me and I'll come along.")
#wait(a$)
#MWinCls
#delay(1)
#fightenemy(B.tem, Fight1.bkg)
#fightcory.tem! = 1
#end
}
*Yes, the player must talk to "B" again
#MWin("Okay I'm a coming.")
#wait(a$)
#addplayer("B.tem")
#MWin("B joined!")
#wait(a$)
#MWinCls
*next part for if u used item for guy on the board
#EraseItem(0)
#DestroyItem(0)
*0=the item slot any # from 0-9
*makes the item go away (never come back 2 run prg)
This code is supposed to have Char.A Fight Char.B, and if Char.A wins, Char.B joins the party. I of course created a new character and filled in "B" with the correct program. Can someone either fix this program, or create a new one?
Game name: Legahn's Legacy. Percent complete: .2%. Hero: Legahn

### jer1400 · 2002-06-05 28:43 · #A1001-14255

**there are so many things wrong with that...**

...so I'll make a new one.
#if(won!=1)
{
#mwin("Wow! Your tough! Ok, I'll join you.")
#wait()
#addplayer("bob.tem")
#mwin("Bob joined your party!")
#wait()
#mwincls()
#end()
}
#if(won!=0)
{
#mwin("I'll join your party...if you can beat me!")
#wait()
#mwincls()
#fightenemy("bob.ene","fight.bkg")
}
Then you have to make the following program the program that runs when you beat bob in battle. You can set it in the enemy editor.
#won!=1
Thats it! I hope this helps you!
