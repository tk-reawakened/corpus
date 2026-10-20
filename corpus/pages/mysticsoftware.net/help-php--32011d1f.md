---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/help.php?article=1&mode=1"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/help.php?mode=1&article=1"
written: null
date_confidence: "unknown"
updated: null
captured: ["20041105223150"]
author: "MrG"
repliers: []
authors: ["MrG"]
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/help.php__mode_1_article_1", captured: "20041105223150", sha256: "fd58db0ad68b27513ad1f59c55c09aff09381b397b8a31fb8432c3375ca0000a", wayback_url: "https://web.archive.org/web/20041105223150/http://www.mysticsoftware.net/help.php?mode=1&article=1"}
---

# Mystic Software

Arrays aren't really that hard to figure out, you just need to be able to connect things together in your mind. First off, make sure you understand how variables work. This isn't a variables tutorial, and we're assuming at least a basic knowledge of their function, how they work, etc. That being said, let's look at a simple array that we all know and love: playerhandle[x]$. In case you don't know, the playerhandle variables store the handles of every player on your team. They're stored in an array. An array is, basically, a collection of variables grouped together in a collection. This is how an array works, in a simple little formula: variable name + [ + reference number + ] + ! or $ Obviously, the variable name is the name of the array, like any old variable name. The "reference number" is how we figure out which variable inside the array we're looking at. There are 5 player handles, right? So we need to put a number in here to tell the program which player handle we want. Finally we have whether the array is a numerical (!) or a string ($) variable. So what's the point of arrays? So far they act just like any other variable, you use playerhandle[0]$ and you get the handle of the first player, no big deal. The cool thing about arrays, though, is that you can use a variable as a reference numbers. This means you can do: #bob!=5 #handle$=playerhandle[bob!]$ And RPGCode will know what you're talking about. You can even use strings for the reference "number" (these arrays are actually called maps, but don't worry about that..) So if you wanted, you could do this: #dog$="puppy" #age!=ageofdogs[dog$]! Pretty neat, no? Arrays drastically cut down your code size and speed up your program, and whenever you're using collections of variables, be on the lookout to see if you can use arrays instead. Here's an example: #If(playerhandle[0]$~="") { #GetHP(playerhandle[0]$,hp0!) #GetSMP(playerhandle[0]$,smp0!) } #If(playerhandle[1]$~="") { #GetHP(playerhandle[1]$,hp1!) #GetSMP(playerhandle[1]$,smp1!) } #If(playerhandle[2]$~="") { #GetHP(playerhandle[2]$,hp2!) #GetSMP(playerhandle[2]$,smp2!) } *etc. Ugh. Why do that when you can use a simple little loop instead! (For the sake of simplicity, we'll use a #While loop instead of a #For loop.. ;) ) #playernum!=0 #While(playernum! < =4) { #GetHP(playerhandle[playernum!]$,hp[playernum!]!) #GetSMP(playhandle[playernum!]$,smp[playernum!]!) #playernum!=playernum!+1 } Much smaller, better, just plain more delicious! Thus concludes our lesson on arrays. Now go out and change all your super huge programs to use these cool things! And be glad you don't have to do it the old way! :D
- Arrays -
By MrG
