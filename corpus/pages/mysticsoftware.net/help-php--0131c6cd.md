---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/help.php?article=13&mode=1"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://mysticsoftware.net/help.php?mode=1&article=13"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040504142425"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/help.php__mode_1_article_13", captured: "20040504142425", sha256: "447fd8e093c2e5fb4cf3d322f30e8f78f1bdc68b1c97f5a7ae408f61ad992203", wayback_url: "https://web.archive.org/web/20040504142425/http://mysticsoftware.net/help.php?mode=1&article=13"}
---

# Mystic Software

In many of today's RPG's you see a character travel to a strange mythical land he has never been to before, but when he gets there, he automatically knows the language the people speak. If you want your RPG to be a bit more original, then maybe you would like to have a language system in your game, just like Final Fantasy 10 does. In FF10, as Tidus, you find the Al - Bhed Primers which enable to learn the language. I am now going to show you how to incorporate such a system into your toolkit game. _________________________________________________________________ Ok, let's begin. In this tutorial, there will be three language types; Beginner, Intermediate and Advanced. Once you get the grip of things you can have as many types as you want. The way we can establish the 3 types is through the use of variables. The variable we will use is going to be #language! The number next to it will be either 0, 1, or 2. 0 indicates the language level is Beginner, 1 indicates the level is Intermediate, and 2 indicates the level is Advanced. In your game's start program, insert this line of code: #language!=0 At the start of the game, you character will be a beginner in the language, as you would expect. Now, as your character is a beginner in the language, when he gets into a conversation, you won't want him to be able to understand a thing. To make this happen, do the following. #If(language!=0){#Mwin("ahdksig fgk kdaw fhs?")} #If(language!=1){#Mwin("Hello fgk kdaw you?")} #If(language!=2){#Mwin("Hello how are you?")} #Wait(a$) No doubt you will have noticed the code caters for all 3 language types. This is essential if you want the character to be able to come back and talk to people when he has learnt the language. Now as the character is currently a beginner, we will want him to become Intermediate at the language at some point. The player will learn the next step when he finds a book. To do this, put the following code on the tile where the item is, and make it a Conditional Activation program. #Kill(language!) #language!=1 #Mwin("You became an Intermediate at the --- language!") #Wait(a$) Now when you return to talk to a NPC, they should talk with the #If(language!=1) statement. When you want to make the character advanced at the language, just put #language!=2 and alter the #Mwin message in the above code, and you're all set! ________________________________________________________________ Ok, it's been a pretty brief tutorial; if I happened to miss anything out, don't hesitate to contact me at the following addresses. outlawz_games@hotmail.com http://big-poppa.mysticsoftware.net
- Language Barrier Tutorial - Written By Outlawz
