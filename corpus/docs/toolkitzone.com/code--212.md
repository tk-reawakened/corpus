---
kind: doc
id: "toolkitzone.com/212"
site: "toolkitzone.com"
title: "Code:"
original_url: "http://toolkitzone.com/library.php?mode=read&doc=212"
written: "2005-04-07T18:02:00"
date_confidence: "exact"
updated: null
captured: ["20051218081045", "20060506162432"]
author: "motar"
repliers: []
authors: ["motar"]
comments_present: 0
f_author: "motar"
f_date: "April 7, 2005, 6:02 pm"
f_description: "New writer Motar enters the fray with his series of rpg code articles focusing on aspects of RPGCode that are generally not covered in most articles and tutorials. Todays piece looks at creating a custom stats system."
f_section: "RPG Code"
f_title: "Miscellaneous RPGCode I"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_212", captured: "20051218081045", sha256: "5e313e5ab89a5ddbcddc14415909a52bdf282b1006cdd8dfc46de7d38101a654", wayback_url: "https://web.archive.org/web/20051218081045/http://toolkitzone.com:80/library.php?mode=read&doc=212&PHPSESSID=22af9c29bceeb94dce4bcfc8b732692e"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_view_cadd_doc_212", captured: "20060506162432", sha256: "514a79abb7a0e28867dd5ee022e6123039812bfe2ab919527b3d095350bfdbe2", wayback_url: "https://web.archive.org/web/20060506162432/http://www.toolkitzone.com:80/library.php?mode=read&view=cadd&doc=212&PHPSESSID=41f26e06b8b6a891a15d685e59e58c0d"}
---

# Code:

Hello, and welcome to the first Miscellaneous RPGCode article. The focus of this series is to hone in on some aspects of RPGCode that are sometimes asked for, but generally most articles or tutorials dont cover. A few things to remember: So, without further ado, today's article: Today will be focused on creating a custom stat system using object oriented programming. The reason I picked this topic was because I have read manycustom battle system tutorials, most of which either assume you have made a stat system already or are going to use the default. I will be assuming you already have some knowledge of how OOP works. To start off, we will need to create a class for the player, which will store the players stats. This is the very base class, and wont do anything until we add some variables and methods to it. So we will now incorporate the very base of stats, HP and MP. So, all we did here was a the HP and MP variables under the private section, and then edited the constructor so it took values for HP! and MP!, then in the constructor we transferred the values of HP! and MP! to the classess variables, then killed HP! and MP!. Now, we are going to throw in a few more stats: Strength, Armor, and Dexterity. This part shouldnt be to hard to understand, we just did the same with Strength, Armor, and Dexterity that we did HP and MP. Now, you may have already noticed that these stats are useless just sitting in the class. So, we will create a method for using the variables outside the class. All this method does is return on of the variables depending on what var$ equals. This method allows you to use one of the variables from the class, like this: Next, we will make a method to change the values of the variables that are still inside the class, because its pretty useless to have a method that gives you the values of the variables if you cant then edit them. This one is slightly more complex than Out(), but all it does is check to see what var$ is, then sees what a_s$ equals to see if it needs to add or subtract, then does the math on the variable. This could be repeated for any stat. You could change up this class to incorporate any other stats you want. You could also use the In() and Out() functions for other variables besides stats. Thank you for reading this article, look forward to more in the future!
Miscellaneous RPGCode, Article 1
- All code will be shown like this:
**Code:**
*While(TRUE) {*
- Each article will begin with a suggested level of experience in RPGCode needed to understand the article, like this:
**Level: Intermediate**
**Level: Intermediate**
The Base Class
**Code:**
* Class Player { Public: Method Player() Private: } Method Player::Player() { }
Adding in the Variables
**Code:**
* Class Player() { Public: Method Player(HP!,MP!) Private: Player_HP! Player_MP! Player_Max_HP! Player_Max_MP! } Method Player::Player(HP!,MP!) { Player_HP! = HP! Player_Max_HP! = HP! Player_MP! = MP! Player_Max_MP! = MP! Kill(HP!) Kill(MP!) }
Some More Stats
**Code:**
* Class Player { Public: Method Player(HP!,MP!,ST!,AR!,DX!) Private: Player_HP! Player_MP! Player_Max_HP! Player_Max_MP! Player_Strength! Player_Armor! Player_Dexterity! } Method Player::Player(HP!,MP!) { Player_HP! = HP! Player_Max_HP! = HP! Player_MP! = MP! Player_Max_MP! = MP! Player_Strength! = ST! Player_Armor! = AR! Player_Dexterity! = DX! Kill(ST!) Kill(AR!) Kill(DX!) Kill(HP!) Kill(MP!) }
The Out() Method
**Code:**
* Method Player::Out(var$) { If(var$ == HP) { ReturnMethod(Player_HP!) } If(var$ == Max_HP) { ReturnMethod(Player_Max_HP!) } If(var$ == MP) { ReturnMethod(Player_MP!) } If(var$ == Max_MP) { ReturnMethod(Player_Max_MP!) } If(var$ == Strength) { ReturnMethod(Player_Strength!) } If(var$ == Armor) { ReturnMethod(Player_Armor!) } If(var$ == Dexterity) { ReturnMethod(Player_Dexterity!) } Kill(var$) }
**Code:**
* Show(Kajen->out(HP) //Or: T/emp_HP! = Kajen->out(HP)
The In() Method
**Code:**
* Method Player::In(var$,a_s$,val!) { f(var$ == HP) { If(a_s$ == +) { Player_HP! = Player_HP! + val! } If(a_s$ == -) { Player_HP! = Player_HP! - val! } } //Add in the If() statements for the other variablesIm too lazy ;) }
Conclusion
*-Motar*
Plasmius
April 8, 2005, 5:40 pm
...s'all greek to me.......
TK Game Boy
April 8, 2005, 6:37 pm
BWAHAHA! Silly Newbies.
motar
April 9, 2005, 10:57 am
@Plasmius: I mention towards the top of the article that you'd need a basic understanding of how OOP works to fully understand the article. did
Plasmius
April 9, 2005, 3:55 pm
What means this mystery acronym, OOP?
Occasionally_Correct
April 9, 2005, 7:08 pm
OOP means 'Object Oriented Programming.' Here's some on it, if you need it.
UltimaWizard
May 8, 2005, 12:49 pm
Do not regard my last comment, I didn't try coding it while reading. It's way more coherent that way. It's fairly effective.
AlienDude
December 7, 2005, 11:57 am
wow it has been a while since i dove into the library here, and saw smth that is a bit hinky: you cant define member functions like method classname::funcname(para), for some reason, you have to defing them inside the class. Why that is i dont know. if you DO do it outside the class the parser does not recognize it.
New writer Motar enters the fray with his series of rpg code articles focusing on aspects of RPGCode that are generally not covered in most articles and tutorials. Todays piece looks at creating a custom stats system.
May 7, '05
Jan 1, '05
Nov 30, '04
May 7, '05
