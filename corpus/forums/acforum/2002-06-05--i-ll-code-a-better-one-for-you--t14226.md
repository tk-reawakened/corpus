---
kind: forum-thread
id: "acforum/14226"
site: "rpgtoolkit.com"
board: "rpgtoolkit.com acforum"
forum: null
skin: "acforum"
thread_id: "14226"
title: "I'll code a better one for you.."
original_url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=14226"
written: "2002-06-05T24:12:00"
last_post: "2002-06-05T24:12:00"
date_confidence: "exact"
captured: ["20020618214558"]
author: "jer1400"
repliers: []
authors: ["jer1400"]
posts_present: 1
pages_present: []
pages_total: null
posts_per_page: null
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: null, start: null, end: null, url: "http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=14214", reason: "never-captured", note: "earlier post in this thread (msg 14214)"}
source_captures:
  - {path: "wayback/rpgtoolkit.com/cgi-bin/acforum.cgi__forum_1001_mode_1_msg_14226", captured: "20020618214558", sha256: "afc8c4687fdd53c10ca3d08884236d23c2df0e391e9945f44b87a25988760549", wayback_url: "https://web.archive.org/web/20020618214558/http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=14226"}
links: []
---

# I'll code a better one for you..

> [!missing] gap:earlier · http://rpgtoolkit.com/cgi-bin/acforum.cgi?forum=1001&mode=1&msg=14214 · never-captured
> earlier post in this thread (msg 14214) was not recovered.

### jer1400 · 2002-06-05 24:12 · #A1001-14226

:ask
#mwincls()
#mwin("What would you like to do?")
@
#mwin("1. Withdraw")
#mwin("2. Save")
#mwin("3. Cancel")
#w!=1
#while(w!=1)
{
:bank
#wait(i$)
#if(i$="1")
{
#if(savedgp!=0)
{
#mwincls()
#mwin("You must deposit money first!")
#wait()
#branch(:ask)
}
#if(savedgp!>0)
{
:withdraw
#mwin("You have saved gp.")
#wait()
#mwincls()
#prompt("How much would you like to withdraw?",takengp$)
#castnum(takengp$,takengp!)
#if(takengp!>savedgp!)
{
#mwin("You can't take more than you have saved!")
#wait()
#mwincls()
#branch(:withdraw)
}
#savedgp!=savedgp!-takengp!
#givegp(takengp!)
#mwin("You have withdrawn gp.")
#wait()
#branch(:ask)
}
}
#if(i$="2")
{
#getgp(gp!)
#if(gp!<1)
{
#mwin("You have no gp to deposit!")
#wait()
#branch(:ask)
}
:save
#mwin("You have gp with you.")
#wait()
#mwincls()
#prompt("How much would you like to save?",givengp$)
#castnum(givengp$,givengp!)
#if(givengp!<1)
{
#mwin("There is no point to deposite nothing.")
#wait()
#mwincls()
#branch(:save)
}
#if(givengp!>gp!)
{
#mwin("You don't have that much gp.")
#wait()
#mwincls()
#branch(:save)
}
#savedgp!=savedgp!+givengp!
#takegp(givengp!)
#mwin("You deposited gp.")
#wait()
#branch(:ask)
}
#if(i$="3")
{
#mwincls()
#mwin("Please come again.")
#wait()
#mwincls()
#w!=2
}
}
#end()
Its glitch free, and I hope you like it! :)
