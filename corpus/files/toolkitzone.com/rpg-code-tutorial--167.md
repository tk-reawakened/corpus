---
kind: file
id: "toolkitzone.com/167"
site: "toolkitzone.com"
title: "Rpg-Code tutorial"
original_url: "http://www.toolkitzone.com/fileman.php?id=10&file=167"
written: null
date_confidence: "unknown"
updated: null
captured: ["20041030004632", "20041107060543", "20041107060643"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_167", captured: "20041030004632", sha256: "c92cf25ef6e972708946088323333a1ebaef67567ce66f5d7c25e6d0a6af48bb", wayback_url: "https://web.archive.org/web/20041030004632/http://www.toolkitzone.com/fileman.php?id=3&file=167"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_167", captured: "20041107060543", sha256: "ce29ceadadfebae7421c11d2b53b8ba29474e92e2e997d1cff413daed859d058", wayback_url: "https://web.archive.org/web/20041107060543/http://www.toolkitzone.com/fileman.php?id=5&file=167"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_167", captured: "20041107060643", sha256: "ab1065e1c5c6ffae65467f6c751a0f55eb0a6321c520ac907c37c22e50214888", wayback_url: "https://web.archive.org/web/20041107060643/http://www.toolkitzone.com/fileman.php?id=10&file=167"}
---

# Rpg-Code tutorial

In this tutorial I will show you how to make a bank account. You can use it to store items or money or something else in it. This program might look hard to some people because it can be quite long and have lots of commands and variables in it, but it's not as hard as is looks. **#if**
At first the commands I will use in this tutorial:
** #mwin() #mwincls() #delay() @ #wait() #if() #get() #getgp() #takegp() #branch() #prompt() #end()
If there are commands that you don't know, check the help files in RPG-Toolkit.(Help-->RpgCode Command Reference)
To start, make a little conversation where you are asked what you want:
** :top #mwin("What do you want to do?") #delay(1) @ #mwin("1 - View account") #mwin("2 - Withdraw money") #mwin("3 - Deposit money") #mwin("4 - Never mind") #wait(choice!) #mwincls()
Now you have the part where the player can choose what he wants. Now, we have to make the part that will happen when the player presses 1, 2, 3 or 4:
** #if(choice!==1) { #mwin("You have money in your account.") #wait() #mwincls() #branch(:top) }
Somewhere else in the game you have set the account! variable. It probably starts with and when you deposit money on it, it will be more. Now let's take a look at the Withdraw money command: **account!==0**
** #if(choice!==2) { #prompt("How much money do you want to withdraw?", money!) #if(money!=>account!) { #mwin("I'm sorry, you don't have that much money in your account") #wait() #mwincls() #branch(:top) } #if(money!<=account!) { #givegp(money!) #account!=account!-money! #mwin("You withdrew money.") #wait() #mwincls() #branch(:top) } }
Now this may be the part where you don't understand it anymore, don't worry, I'll explain. At first, you have to type how much money you want to withdraw. This will be saved in the money! variable. Now, let's say you have 50gp in your account and you want to withdraw 60. This is not possible since you don't have that much (or less). In the sentence the program checks if you want to withdraw more (>) money then you have. If you want to withdraw more then you have, it goes further in that statement. If you have less money, it skips that part and goes to the sentence . This sentence checks if you have less or equal money in your account then you want to withdraw. If this is true, it goes further in that statement. **#if(money!=>account!)** **#if** **#if(money!<=account!)** **#if**
The sentence gives you the money that you wanted to withdraw. This shouldn't be to hard to understand, but the next sentence might be. In case we forgot: **#givegp(money!)**
account!= the money you have in your account money! = the money you want to withdraw
So what the sentence does, is subtracts the money you have in your account with the money you want to withdraw. If we would put it in words, it would be like this: **#account!=account!-money!**
Account we have now! Will become Account we have now! minus the money we withdrew!.
I hope that's clear enough, since I don't know how to explain it better :). Now, we go to the deposit part:
** #if(choice!=3) { #getgp(gphold!) #prompt("How much money would you like to deposit?", money!) #if (money!=>gphold!) { #mwin("Sorry, you don't have that much money.") #wait() #mwincls() #branch(:top) } #if (money!= money.") #wait() #mwincls() #branch(:top) } }
This is exactly the opposite of the withdraw part. I don't think this should be to hard if you've read the withdraw part carefully. Now the last part:
** #if(choice!=4) { #end() }
Easy huh? This just ends the program. Nothing not to understand about it I think.
Here is the complete program:
** :top #mwin("What do you want to do?") #delay(1) @ #mwin("1 - View account") #mwin("2 - Withdraw money") #mwin("3 - Deposit money") #mwin("4 - Never mind") #wait(choice!) #mwincls()
** #if(choice!==1) { #mwin("You have money in your account.") #wait() #mwincls() #branch(:top) }
** #if(choice!==2) { #prompt("How much money do you want to withdraw?", money!) #if(money!=>account!) { #mwin("I'm sorry, you don't have that much money in your account") #wait() #mwincls() #branch(:top) } #if(money!<=account!) { #givegp(money!) #account!=account!-money! #mwin("You withdrew money.") #wait() #mwincls() #branch(:top) } }
** #if(choice!=3) { #getgp(gphold!) #prompt("How much money would you like to deposit?", money!) #if (money!=>gphold!) { #mwin("Sorry, you don't have that much money.") #wait() #mwincls() #branch(:top) } #if (money!= money.") #wait() #mwincls() #branch(:top) } }
** #if(choice!=4) { #end() }
