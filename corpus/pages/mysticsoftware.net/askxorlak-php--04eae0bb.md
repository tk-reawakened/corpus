---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/askxorlak.php?mode=1&question=10"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://mysticsoftware.net/askxorlak.php?mode=1&question=10"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040505102902"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/askxorlak.php__mode_1_question_10", captured: "20040505102902", sha256: "44d50e99099db854c32c78ec2675b63f59ccaa432ad858fab8454a3bdf93d673", wayback_url: "https://web.archive.org/web/20040505102902/http://mysticsoftware.net/askxorlak.php?mode=1&question=10"}
---

# Mystic Software

What does #for() do?
#for is useful if you want to repeat a certain block of code multiple times. Say you wanted to give the player 100 potions. You could do: #giveitem("potion.itm") #giveitem("potion.itm") #giveitem("potion.itm") ... 100 times, but that's a mess. You can do it much quicker with a #for loop: #for(i!=0;i! < 100;i!=i!+1) { #giveitem("potion.itm") } #for is especially useful with arrays. For example, if I wanted to check if Vance is in the player's party: #inparty!=0 #for(i!=0;i! < 5;i!=i!+1) { #if(playerHandle[i!]$="Vance") { #inparty!=1 } } That will check playerHandle[0]$, playerHandle[1]$, etc. for each value of i! up to 4.
