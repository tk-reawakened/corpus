---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/askxorlak.php?mode=1&question=13"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://mysticsoftware.net/askxorlak.php?mode=1&question=13"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040505103538"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/askxorlak.php__mode_1_question_13", captured: "20040505103538", sha256: "3620c386dcd5b6a7c4be655b1beab8d29e07c435e4bb9788361c0086ab8c831b", wayback_url: "https://web.archive.org/web/20040505103538/http://mysticsoftware.net/askxorlak.php?mode=1&question=13"}
---

# Mystic Software

How would I start a Final Fantasy X style grid level up system?
You would have to store a bunch of info for each node, including what stats it increased and what nodes it connects to: *This one increases your HP by 100 and connects to nodes 2 and 3 HP_inc[1]!=100 MP_inc[1]!=0 Attack_inc[1]!=0 Defense_inc[1]!=0 Magic_inc[1]!=0 Connect_1[1]!=2 Connect_2[1]!=3 Connect_3[1]!=0 Connect_4[1]!=0 *This one increases your Attack by 1 and is at a 4-way intersection HP_inc[2]!=0 MP_inc[2]!=0 Attack_inc[2]!=1 Defense_inc[2]!=0 Magic_inc[2]!=0 Connect_1[2]!=1 Connect_2[2]!=4 Connect_3[2]!=5 Connect_4[2]!=6 You would access the data for each node using the number of the node. For example, HP_inc[current!]!. When moving between nodes, you'd check which nodes the current one is connected to. For the graphical display, you would probably have a method that highlighted a node based on its number by checking some stored x,y positions. As for only using a node once, you'd update a variable, used[current!]!, to indicate that the upgrade is no longer available.
