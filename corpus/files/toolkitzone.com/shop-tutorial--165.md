---
kind: file
id: "toolkitzone.com/165"
site: "toolkitzone.com"
title: "Shop Tutorial"
original_url: "http://www.toolkitzone.com/fileman.php?id=10&file=165"
written: "2003-12-31"
date_confidence: "day"
updated: "2003-12-31"
captured: ["20051018034954", "20051031045025", "20051212212512", "20051216020115"]
author: "Sander"
repliers: []
authors: ["Sander"]
comments_present: 0
f_author_source: "Woozy"
f_name: "Shop Tutorial"
f_submitted_by: "Sander"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_165", captured: "20051018034954", sha256: "56bd1ed6bea017262d0d38db2503cc78cf620cb4f8ff4cafc3f029aa86a47131", wayback_url: "https://web.archive.org/web/20051018034954/http://www.toolkitzone.com/fileman.php?id=3&file=165"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_7_file_165", captured: "20051031045025", sha256: "6737118bf0aabe6b4eab4809a6b4aac6602b3c99c06f3a924ab6eb4bc3137232", wayback_url: "https://web.archive.org/web/20051031045025/http://www.toolkitzone.com/fileman.php?id=7&file=165"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_165", captured: "20051212212512", sha256: "bc8fedc4de8838a28d36d01ca34668102b5c1ce9617dc1b919e3bbf744be4620", wayback_url: "https://web.archive.org/web/20051212212512/http://www.toolkitzone.com/fileman.php?id=5&file=165"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_165", captured: "20051216020115", sha256: "3f5700e61127d937ac2367c79e53472f2e52e2bd7d069fec9956c0c4ef5793d3", wayback_url: "https://web.archive.org/web/20051216020115/http://www.toolkitzone.com/fileman.php?id=10&file=165"}
---

# Shop Tutorial

One of a series of well written tutorials from Woozy taking you through the various commands and stages behind putting together your own programs, in this case using the default shop, and also good way of learning important commands.
**Rpg-code tutorial**
In this tutorial I will show you how to make a shop program, it's a very simple program and I won't use more difficult commands then the command. **#if**
At first, here are the commands I will use in the tutorial:
** #mwin() #mwincls() @ #delay() #wait() #if() #callshop() #end()
You should check the help-files for how to use this commands. (Help-->RpgCode Command Reference)
At first, you should make a little conversation where the shop owner asks you what you want:
** #mwin("Owner: What do you want?") #delay(1) @ #mwin("1 - buy/sell") #mwin("2 - never mind") #wait(a!)
Because there is now something in the wait command, it will wait AND save the key you press. Therefore, you have to make a command for if you press 1 and 2: **#if**
** #if(a!==1) { #callshop("item1.itm","item2.itm","item3.itm") }
** #if(a!==2) { #mwin("Come back anytime!") #wait() #mwincls() #end() }
So you'll end with this:
** #mwin("Owner: What do you want?") #delay(1) @ #mwin("1 - buy/sell") #mwin("2 - never mind") #wait(a!)
** #if(a!==1) { #callshop("item1.itm","item2.itm","item3.itm") }
** #if(a!==2) { #mwin("Come back anytime!") #wait() #mwincls() #end() }
Of course, you can also use some variations in this, like you can choose between items, armor and weapons. This is also very easy:
** #mwin("Owner: What do you want to buy?") #delay(1) @ #mwin("1 - weapons") #mwin("2 - armor") #mwin("3 - items") #mwin("4 - never mind") #wait(a!)
** #if(a!==1) { #callshop("weapon1.itm","weapon2.itm","weapon3.itm") }
** #if(a!==2) { #callshop("armor1.itm","armor2.itm","armor3.itm") }
** #if(a!==3) { #callshop("item1.itm","item2.itm","item3.itm") }
** #if(a!==4) { #mwin("Come back anytime!") #wait() #mwincls() #end() }
See what I did? You can choose between armor, weapons and items. What you do is create a different for them and put them into different commands. **#callshop** **#if**
**Browse Sections**
