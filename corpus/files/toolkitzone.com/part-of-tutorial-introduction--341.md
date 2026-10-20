---
kind: file
id: "toolkitzone.com/341"
site: "toolkitzone.com"
title: "#Part_Of_Tutorial[Introduction!]$"
original_url: "http://www.toolkitzone.com/fileman.php?id=10&file=341"
written: null
date_confidence: "unknown"
updated: null
captured: ["20041031022227", "20041105205520", "20060312092728"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_341", captured: "20041031022227", sha256: "43b0287a7a15c78b2a2ff1dd33e2df76ac85b34ff20975cf39d1217ad6e022b8", wayback_url: "https://web.archive.org/web/20041031022227/http://www.toolkitzone.com/fileman.php?id=3&file=341"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_341", captured: "20041105205520", sha256: "4b7275a3b92063272014ce4c5772e6f0827e74a42ce908693d8e0b1313669e18", wayback_url: "https://web.archive.org/web/20041105205520/http://www.toolkitzone.com/fileman.php?id=5&file=341"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_341", captured: "20060312092728", sha256: "63dddd06a2779a7124b0a083d6948aa43ffb3d534ca0dd9eab2283dc259bb307", wayback_url: "https://web.archive.org/web/20060312092728/http://www.toolkitzone.com/fileman.php?id=10&file=341"}
---

# #Part_Of_Tutorial[Introduction!]$

Hello all you crazy kids. OC here again, bringing you another, more advanced tutorial on arrays. Today you'll learn how to make confusing if statements with arrays, loops, and more. This is here to show you some of the many things you can do with arrays. First, we will review the last program I had on the previous tutorial. So, shall we begin?
#Part_Of_Tutorial[If_and_Arrays!]$
An If statement is probably one of the best things you can learn about programming, because it allows you to do a large number of amazing things. But to take that even further, you can use arrays. Now, as we covered in the last tutorial, arrays are pretty much the same thing as variables, except they can store multiple values under the same name. Here's the program once more...
#Slot!=0 #Item[Slot!]$="" #If(Item[Slot!]$="") { #Item[Slot!]$="Bob" #Slot!=Slot!+1 } #Item[Slot!]$=""
As you know, this sets the numeric variable Slot! to 0. Then, puts the value of Slot! into the array Item[], making it Item[0]. Item[0] equals nothing, so the computer checks to see if that's true. If so, it sets Item[0]'s value to Bob, then adds 1 to Slot!, making it 1. So now Item[1] is presented. And the same thing happens over again. Now, let's take this a step further by making it sort of like an item checking system. What will be different about this is it will check multiple things. Take a look:
#Slot!=0 #Item[Slot!]$="" #If(haveitem$="Potion") { #Item[Slot!]$="Potion" #Slot!=Slot!+1 } #If(haveitem$~="Potion") { #If(haveitem$="Sword") { #Item[Slot!]$="Sword" #Slot!=Slot!+1 } #If(haveitem$~="Sword") { #End } }
There you have it. It's a bit more confusing then the last one, so take a while to look at it. You may be a little confused by the ~ symbol if you're still learning how to program, so I'll explain that. When you see ~= it means not equal to. So, as you can plainly see, haveitem$~="sword" is like saying "If Have Item does not equal "Sword", do the next line of code." So basically, the program checks if you have "Potion". If so, it adds that to Item[0] and then adds 1 to 0 making it 1. Then, it checks if you have a "Sword". Well, you get the jist of it. This is just a small example of an item checking program. Doing something like this is good for making item lists in custom menu's and battle systems (speaking of which, I'll cover some stuff on battle systems later).
#Part_Of_Tutorial[Loop_Arrays!]$
Well, you've learned how to make if statements incorperating arrays, so now lets try something a little different. Here, we're going to be using a For Loop. The #For command makes your life easier because you can have the effect of doing something 100 times in a very small block of code. Whereas if you wanted to do that all by hand, it would take a lot longer. Here's an example of using the #For command to set values for arrays:
#Arrays!=0 #Arrays[x!]!=Arrays! #For(x!=0; x!<10; x!=x!+1) { Arrays[x!]!=Arrays!+1 }
That sets the value of Arrays[0]! to 0. Then, 1 is added to both x! and Arrays!. So Arrays[0]! = 0, Arrays[1]! = 1, and so on and so forth. If you aren't familiar with the #For command, then you might be asking yourself, what do all of the statements inside the ( and ) mean? Here's your answer: The first part declares a variable and gives it a value. I used x!=0 for that (x! being the variable, and 0 being the value). The next part is like an #If command, because it asks if the condition is bleah bleah bleah. Here I used x!<10. Right here it stops, and then the commands inside of the { and } are run. Then, the last statement in the #For command is run. The last statement is usually adding or subtracting from the variable you set in the first part of the command. So, it adds 1 to x!. Then, the #For command loops back up and does it all over again until x! is equal to 10. After that, the loop ends.
#Part_Of_Tutorial[Profiles!]$
Well, you've seen loops, if statements, what next? To answer that, profiles. Now you're going to get to see how to make an enemy profile (hp, smp, etc.) using arrays. You might be thinking "Why is this important?" And again, to answer that, custom BS's. If you want to make a totally custom battle system, you'll need to learn some good ways of managing Enemies. The way I do this is making an Enemy database, sorted by level. Each level gets their own separate file. Here's an example of what I mean:
#name!=0 #hp!=1 #smp!=2 #dp!=3 #fp!=4 #exp!=5 #gold!=6
This gives each variable a value from 0 to 6. You'll use these variables inside of the arrays so each one, like always, has a slot. Let's say we have an enemy called Ninja, his HP is 50, SMP is 10, etc.. Here's how we'll set it using the above and arrays:
#Ninja[name!]$="Ninja" #Ninja[hp!]!=50 #Ninja[smp!]!=10 #Ninja[dp!]!=10 #Ninja[fp!]!=10 #Ninja[exp!]!=50 #Ninja[gold!]!=25
See how that works? Instead of just using 0, 1, 2, 3, etc. as the slots, I set variables as the slots and used those instead. Think of how confusing it would be to just use the numbers. You'd have to remember which order everything went in and that's just not very fun (or easy) if you're doing it at three in the morning. Now, you can use those same variables again and again for the rest of the enemies. This is a very good way to store enemy information for a custom battle system.
Ready for something a little harder? This next part will show you how to make your enemies even more custom by using arrays to show battle animations, keep track of special moves, and things like that.
This block of code is stores information on the enemies special move. The three arrays I'm using for this are the special moves name, the moves FP, and the SMP it uses up.
#NinjaSpecialMove[0]$="SuperFancyKick" #NinjaSpecialMoveFP[0]!=100 #NinjaSpecialMoveSMP[0]!=5
Alright. Now we've stored the information for the enemies special move. Note that I put 0 in the array, marking it as the enemies first special move. You can add more if you want to. The next part stores the information on what the animations for the special move are. You can do this with normal variables, but since the tutorial is about arrays, we'll use those!
#NinjaSpecialMoveAnm[0]$="SuperFancyKick.anm"
Now that you've made that, you can view it with the #Animation or #SizedAnimation commands in battle. If the enemy uses this in battle, you should write some AI for him so his SMP is reduced. Here's a little example on how to do that:
#NinjaTurn!=1 #While(NinjaTurn!=1) { #Random(2,move!) #While(move!=1) { #If(Ninja[smp!]!<5) { #move!=2 } #If(Ninja[smp!]!=>5) { #Animation(NinjaSpecialMoveAnm[0]$,x!,y!) #Ninja[smp!]!=Ninja[smp!]!-NinjaSpecialMoveSMP[0]! #GetHP(target$,targethp!) #targethp!=targethp!-NinjaSpecialMoveFP[0]! #HP(target$,targethp!) #NinjaTurn!=0 } } }
That's a pretty big block of code there. So let's take this step by step. First, I set the variable NinjaTurn! to 1. When NinjaTurn! is 1, the Ninja gets to do a move. Next, it uses a while loop and uses the #Random command which randomizes a number and puts it into the variable next to it. Here I used the variable move!. Then, we use another while loop to see if it chose 1. If so, it checks to see if the Ninja has enough SMP to do the move. If not, it goes to the regular move that doesn't consume SMP. If the enemy does have enough SMP, it runs the animation with the #Animation command, then it subtracts the SMP that the move uses. After that, it gets the HP of a certain target (the player that the enemy is attacking) and stores the HP into the variable targethp!. Then, the FP value of the special move is subtracted from targethp!, making the player lose that amount of HP. Next, NinjaTurn! becomes 0 and it's no longer the Ninja's turn to attack.
#Part_Of_Tutorial[Bye_bye!]$
And there you have it! You've used If statements with arrays, loops that set values for arrays, AND you just made your custom enemy attack the player. This is a really really important part of making a battle system. But I won't go into battle systems anymore, because that's not the tutorials focus. If you've read this and the previous tutorial I wrote, then you've learned a heck of a lot about variables, arrays, and a number of ways to use them! This concludes my array tutorial, so I hope you can put everything I've written to good use. Bye bye!
#Part_Of_Tutorial[Credits!]$
Written by Samuel (A.K.A., Occasionally Correct) Occasionally Correct Productions, 2004 Special thanks to... My girlfriend, once again. Love ya! All the staff at TKZ (No, I didn't forget you this time, Mr. Code Manager ^_^) CBM for making the toolkit And anyone else who reads this
