---
kind: doc
id: "toolkitzone.com/231"
site: "toolkitzone.com"
title: "Beginner"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=231"
written: "2005-05-07T19:10:00"
date_confidence: "exact"
updated: null
captured: ["20060612052536", "20060612052536"]
author: "motar"
repliers: []
authors: ["motar"]
comments_present: 0
f_author: "motar"
f_date: "May 7, 2005, 7:10 pm"
f_description: "Latest tutorial from Motar, with beginners to RPG Code in mind, which focuses on creating a custom item system."
f_section: "RPG Code"
f_title: "Miscellaneous RPGCode II"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_231", captured: "20060612052536", sha256: "00dfddc84a6504859df30f4b68bf231fb532b022c5b7ecefc94efd80cc0e025f", wayback_url: "https://web.archive.org/web/20060612052536/http://toolkitzone.com/library.php?mode=read&doc=231"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_231-b02d2d", captured: "20060612052536", sha256: "00dfddc84a6504859df30f4b68bf231fb532b022c5b7ecefc94efd80cc0e025f", wayback_url: "https://web.archive.org/web/20060612052536/http://www.toolkitzone.com/library.php?mode=read&doc=231"}
---

# Beginner

Todays article, the second in this series, will be focusing on creating a custom item system, which, similarly to my previous article about a custom stat system, is something that most battle system/menu tutorials overlook, either expecting you to use the default or create your own. The experience level for this tutorial is: Note: I was originally going to make this article intermediate and teach it using OOP, but I got some complaints from people saying they had no idea what OOP was. So, for this article, I wont use OOP, but I may make a similar tutorial later incorporating it. Even though this tutorial is for beginners, I still recommend you be somewhat acquainted with how RPGCode works (Variables, Arrays, Conditionals, etc.).
Miscellaneous RPGCode II
**Beginner**
A classic RPG-style item system usually allows you to have a certain amount of room in your pack, in which you can store any items you throughout the game. You can then use these items on a player or whatever else their use is, which will then free up space in your pack. To start out, well make a method that sets up all the variables we will need: This is pretty self explanatory: The Item[#]$ variables will hold the names of the different items in the pack, and the Item_Open! variable is used to show which Item[#]$ variable a new item should be put into. The Item_Quan[#]! variables show how many of there is of the corresponding Item[#]$ variable. The Item_Open! variable might not make sense now, but it will become more clear through the article. This method will allow an item to be added to the pack. Lets walk through the method: The for loop at the top is used to check through all the Item[#]$ variables to see if any of them match with Handle$. If one of them does, it increases the number of that item by one and makes v! equal 1. It next checks to see it v! equals zero, and if it does, it means that a match was not found between Handle$ and one of the Item[#]$ variables. If v! does equal zero, it checks to see if Item_Open is less than or equal to 10 (because 10 is the max amount of items you can have in your pack), and if it is, then it changes the Item[#]$ variable that corresponds with the Item_Open! variable. It then increases the Item_Open variable by one, so the next time a new item is added, it will add it to the end of the items in the pack (Confused? Read this over a couple times and you should get it). This method will allow the player use one of the items that has been added to the pack. Lets look at it: First the method takes Item_Quan[slot!]! and subtracts one from it to signify that it used one of that item (slot! is a number 1-10, representing which item we are using). The method then checks if the quantity of the item used is zero, because if it is, all the items need to be shifted up one space. The for loop on the next line takes care of that( I dont want to explain it, because it will take a long time. Look at it for a minute, and it should make sense). After the for loop, it makes the tenth slot variables equal to nothing, because if the items are shifted up one, the tenth one is automatically going to be empty. Then the method subtracts one from Item_Open!, because the items were shifted up one. Note: This method will only change the variables that represent the item, they wont actually do anything to the player or whatever the player is using the item on. To do that, the method would look something like this: These method could be expanded, to like I showed above, to actually do something. They could also have more than ten items, to do this you would have to tweak the methods and variables. Happy coding!
The Main Methods and Variables
**Code:**
* Method Setup_Item_Variables() { Item[1]$ =  Item[2]$ =  Item[3]$ =  Item[4]$ =  Item[5]$ =  Item[6]$ =  Item[7]$ =  Item[8]$ =  Item[9]$ =  Item[10]$ =  Item_Quan[1]! = 0 Item_Quan[2]! = 0 Item_Quan[3]! = 0 Item_Quan[4]! = 0 Item_Quan[5]! = 0 Item_Quan[6]! = 0 Item_Quan[7]! = 0 Item_Quan[8]! = 0 Item_Quan[9]! = 0 Item_Quan[10]! = 0 Item_Open! = 1 }
The Give Method
**Code:**
* Method Tut_Give_Item(Handle$) { v! = 0 For(t!=1,t! < =10,t!=t!+1) { If(Item[t!]$ == Handle$) { Item_Quan[t!]! = Item_Quan[t!]! + 1 v! = 1 } If(v! == 0) { If(Item_Open! < = 10) { Item_Quan[Item_Open!]! = Item_Quan[Item_Open!]! + 1 Item[Item_Open!]$ = Handle$ Item_Open!++ } } Kill(t!,v!,Handle$) }
The Use Method
**Code:**
* Method Tut_Use_Item(slot!) { Item_Quan[slot!]!-- If(Item_Quan[slot!]! == 0) { For(y!=1,y! < =10,y!++) { For(t!=y!,t! < =9,t!++) { v! = t! + 1 Item_Quan[t!]! = Item_Quan[v!]! Item[t!]$ = Item[v!]$ } } Item_Quan[10]! = 0 Item[10]$ =  Item_Open!-- } Kill(y!,slot!,t!,v!) }
**Code:**
* Method Tut_Use_Item(slot!) { Item_Quan[slot!]!-- //This is where you would insert the method that would use the item on whatever the player is using it on. If(Item_Quan[slot!]! == 0) { For(y!=1,y! < =10,y!++) { For(t!=y!,t! < =9,t!++) { v! = t! + 1 Item_Quan[t!]! = Item_Quan[v!]! Item[t!]$ = Item[v!]$ } } Item_Quan[10]! = 0 Item[10]$ =  Item_Open!-- } Kill(y!,slot!,t!,v!) }
Conclusion
* -Motar
Colin
May 7, 2005, 8:33 pm
Any way I say this is going to sound insulting, so I won't try to hard to euphemize. Please use RPGCode a little longer before teaching it. The document does have some nice content which can be extracted, though. Good work!
TK Game Boy
May 8, 2005, 12:23 am
Wow. This tutorial reminds me of my tutorials. Except mine is longer and more in depth.
OBCT
May 8, 2005, 11:07 am
Ouch. At least have a variable to keep a count of the number of different items. That's a lot of hard coding to change every time you add a new item.
motar
May 8, 2005, 5:18 pm
Er...Well, the Item_Open! variable does keep a count, if you mean what I think you do.
Plasmius
May 23, 2005, 12:39 pm
TKGB's tuts are better because they can be understood by even the dumbest of dunderheads. Like me.
Fuzzman
September 10, 2005, 1:13 pm
That's not a nice thing to say to yourself! But yes, I agree. I'm glad someone made a menu tutorial, because I would never learn otherwise.
Latest tutorial from Motar, with beginners to RPG Code in mind, which focuses on creating a custom item system.
Feb 4, '06
Apr 7, '05
Jan 1, '05
Nov 30, '04
Apr 7, '05
