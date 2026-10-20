---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/help.php?article=16&mode=1"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/help.php?mode=1&article=16"
written: null
date_confidence: "unknown"
updated: null
captured: ["20041106125728"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/help.php__mode_1_article_16", captured: "20041106125728", sha256: "5ded1f871ab34e6c9872006f1480b45c1df192556b60497343af94714137a624", wayback_url: "https://web.archive.org/web/20041106125728/http://www.mysticsoftware.net/help.php?mode=1&article=16"}
---

# Mystic Software

Many people are exuberant about the tile animation in 2.20, but what some people don't realize is that tile animation is already possible. It's possible through the TK's limited, but functional multitasking engine. This animation is fairly simple: make an item with no graphics, and for its Program to Run While Item is On Board, put something like this: :top #LayerPut(5,2,1,"fire.tst1") #LayerPut(5,2,1,"fire.tst2") #Branch(:top) And whala, you have a simple tile animation (use your own gfx names and coords of course.) But what most people claim is that this is simply too slow to be worth anything. However, what most everyone does not realize, is that there are things you can do to speed up your multitasking performance. This tutorial will cover some of those methods. First, you have to learn a little of how the multitasking in the TK works. Basically it takes your Program to Run While the Item is On Board (your multitasking program), and runs it one line at a time. Every time it gets a chance (the player stops walking, the other multitasking programs stop for a breather), it runs another line. There are tricks, however, hidden within this engine. - First, make sure your multitasking speed is as low as possible. The "speed" is the amount of time the TK takes between running the game and running your multitasking program. Therefore, you want it to be as low as possible so it runs as quick as possible. Go into the Main File Editor, Project Settings, and move your Multitasking Speed all the way to the left. - Yes, the TK runs multitasking programs one command at a time, but it runs commands with brackets like everything inside the brackets is one command! That means that with something like: #If(bob!=0) { #LayerPut(5,2,1,"fire.tst1") #LayerPut(5,2,1,"fire.tst2") } The TK will run both those #LayerPut commands at once, if bob! is 0. Cool, no? This means that if you have a bunch of animation you want to run, and you don't want to plod along one line at a time, you can stick it in #If brackets, like this, with meaningless variables so you'll be sure it will run: :top #If(bob!=0) { #LayerPut(5,2,1,"fire.tst1") #LayerPut(5,2,1,"fire.tst2") } #If(bob!=0) { #LayerPut(5,2,1,"fire.tst3") #LayerPut(5,2,1,"fire.tst4") } #Branch(:top) A word of warning.. Be sure you don't stick everything in one #If, or you bog the game down and give the player less time to walk.. A good rule of thumb is to take the amount of actual commands you have, divide by two, and use that many #If brackets. - It's better if you don't use methods at all in a multitasking program, but sometimes you have to. For instance, if you start getting too many #Ifs inside #Ifs in a multitasking program, the game will slow down considerably. So if you find your big multitasking programs suddenly stop working for odd reasons, check your #If count and see if a method is in store. Well, that's it, but you'll find these little tips and hints can make a big difference in your multitasking performance. Granted, the engine needs work, but with a little tweaking, give it a try and see if you're not a believer!
- Multitasking - By MrG
