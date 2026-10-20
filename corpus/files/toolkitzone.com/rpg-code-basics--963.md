---
kind: file
id: "toolkitzone.com/963"
site: "toolkitzone.com"
title: "RPG Code Basics"
original_url: "http://www.toolkitzone.com/fileman.php?id=10&file=963"
written: "2005-01-02"
date_confidence: "day"
updated: "2005-01-02"
captured: ["20060304081117", "20060312125330", "20060312130113", "20060312130345"]
author: "ericzgao"
repliers: []
authors: ["ericzgao"]
comments_present: 0
f_name: "RPG Code Basics"
f_submitted_by: "ericzgao"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_963", captured: "20060304081117", sha256: "ebb6925eaac6f85d0a428e186de6d3a29254c370692b16e482998b1e0168629a", wayback_url: "https://web.archive.org/web/20060304081117/http://www.toolkitzone.com:80/fileman.php?id=3&file=963&PHPSESSID=9e94a0bfd739af13980670d1e820a329"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_963", captured: "20060312125330", sha256: "3de42ffe5c9593716147fcb2a3dd3089a43a14637ab65e498e9fc9dcf6f6ef7b", wayback_url: "https://web.archive.org/web/20060312125330/http://www.toolkitzone.com:80/fileman.php?id=5&file=963&PHPSESSID=56960325ea1b48eb3bf121ef4207b37f"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_7_file_963", captured: "20060312130113", sha256: "98f34d49665f916b149e283a252fd1ae76d21b004787acfbeed49075fbb5db78", wayback_url: "https://web.archive.org/web/20060312130113/http://www.toolkitzone.com:80/fileman.php?id=7&file=963&PHPSESSID=56960325ea1b48eb3bf121ef4207b37f"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_963", captured: "20060312130345", sha256: "346a89a5c8d0195df6c0373c2f8a314c2987f26078260a612d20e4a9640615a4", wayback_url: "https://web.archive.org/web/20060312130345/http://www.toolkitzone.com:80/fileman.php?id=10&file=963&PHPSESSID=56960325ea1b48eb3bf121ef4207b37f"}
---

# RPG Code Basics

A detailed tutorial for the basics of RPGCode. It is intended for RPG Toolkit 2, but much of it can be carried over to RPG Toolkit 3, as the tutorial explains. Certainly useful for beginners, and more in-depth than the TK2 help files. If you're new to RPGCode, check this out.
RPG code basics, #mwin to #if
Table of contents
- Introduction to RPG code
- #Mwin
- #Wait
- #Mwincls
- Variables
- #If, #else, #elseif
- #While, #branch
- Other RPG code commands
- Review
1. Introduction to RPG code
RPG code can be used in your Toolkit RPG game to display what you want a certain NPC to say, what item you get when your player finds an item, and other events. Coding for RPG toolkit version 2 is mostly the same as RPG toolkit version 3. You might want to take off the # sign before all the codes or variables, because RPG toolkit version 3 does not require those. An asterisk, or *, is still used for comments in RPG toolkit version 3, but two slashes, or // is also used for comments
2. #Mwin
#Mwin changes the text that appears in a box at the top of your RPG game during game play. For example, if you had an NPC on the board, and you wanted it to say something when the player bumps into the NPC, then this might be the program you would write.
*this asterisk or * is a comment mark.
*the computer does not read comment marks.
*comment marks are used for comments.
*the text that is displayed when this program runs
*is inside the parentheses and the quotes.
*#mwin(text)
#mwin(Hi.)
#wait(a$)
This program would go into the activation program for an item, which can be set by right clicking where an item is in the board editor, left clicking info, left clicking the button by the item name, left clicking advanced, and setting the activation program which is the set in the next box after the box where you set your item. If your NPC is a program with graphic, then you go through the same steps, but left click the button by the RPG code program instead of the button by the item name, and set the RPG code program in the box. Then, left click advanced, and choose a graphic in the box after where you set the RPG code program.
3. #Wait
You might have noticed that there was a #wait command in the previous program. That lets the computer know that it should wait for the player to press any key before clearing the #mwin text. Otherwise, the #mwin text only stays for about a second before disappearing. The usual format of the #wait command is:
#wait(a$)
Other uses of #wait will be mentioned in the #if section of this tutorial.
4. #Mwincls
#Mwincls() clears the text box. For example:
#mwin(Hi.)
#wait(a$)
#mwincls()
*after the player pressed any key,
*the text clears and displays the
*next line of text.
#mwin(How are you?)
#wait(a$)
*#mwincls() is not required at the end of a program,
*because the text clears after you press any key
*(you should still include a #wait) at the end of a
*program.
You could choose to display the text at the same time:
#mwin(Hi.)
#mwin(How are you?)
#wait(a$)
You could also choose not to clear the original line of text after its displayed:
#mwin(Hi.)
#wait(a$)
#mwin(How are you.)
#wait(a$)
5. Variables
You might have noticed the a$ in the parenthesis of the #wait command. a$ is a variable. a is the name of the variable, and $ defines the variable as a text variable. ! would define a variable as a number. Numeric variables can be used to add and subtract:
#variable!=1
#variable2!=2
*variable3!=1+2
#variable3!=variable!+variable2!
*variable3!=3+1
#variable3!=variable3!+1
*display variables with #mwin by putting the variable name and numeric or text symbol in side < and >.
*for example:
#mwin(Variable 3 equals )
#wait(a$)
6. #If, #else, #elseif
Variables are used for #if commands:
*if condition is true, then
#if (variable3!=4)
*run RPG code inside the { and }.
#mwin(Variable 3 equals 4.)
#wait(a$)
*if condition is true, then
#if (variable3!~=4)
*run RPG code inside the { and }.
#mwin(Variable 3 does not equal 4.)
#wait(a$)
The standard format is:
#if (condition) is true,
then this.
Here is an example:
#variable!=1
#variable2!=2
#variable3!=variable!+variable2!
#variable3!=variable3!+1
*variable3!=4
#if (variable3!=4)
*because variable3!=4, the RPG code inside { and } is displayed.
#mwin(Variable 3 equals 4.)
#wait(a$)
This is how #if can be used. One program is written:
#if (variable!=0)
#mwin(Hi.)
#wait(a$)
#if (variable!=1)
#mwin(Have a nice day.)
#wait(a$)
The other is written:
#variable!=1
If you place the original program somewhere, and the second program somewhere else, the first program would display something different after the event of activating the second program.
The #wait command can be used the #if command. For example:
#mwin(What would you like to do?)
#mwin(-1- say hi)
#mwin(-2- say how are you)
#mwin(-3- not talk)
*#wait tells the computer to wait for the player to press a key, and saves
*the key that was pressed into the variable inside the ( and ), which
*should be a text variable (for example, variable$)
#wait(variable$)
*put quotes around the key that is pressed in #if statements.
*for example, #if (variable$=1)
#if (variable$=1)
*if the player pressed 1, then the RPG code in { and } is run.
#mwincls()
#mwin(Hi.)
#wait(a$)
#if (variable$=2)
*if the player pressed 2, then the RPG code in { and } is run.
#mwincls()
#mwin(How are you?)
#wait(a$)
#if (variable$=3)
*if the player pressed 2, then the RPG code in { and } is run.
*nothing happens, and program ends, because the program is over.
This program can also be written with #elseif and #else in RPG toolkit version 3 (the # is not required before commands or variables in RPG toolkit version 3):
mwin(What would you like to do?)
mwin(-1- say hi)
mwin(-2- say how are you)
mwin(-3- not talk)
*#wait tells the computer to wait for the player to press a key, and saves
*the key that was pressed into the variable inside the ( and ), which
*should be a text variable (for example, variable$)
wait(variable$)
*put quotes around the key that is pressed in #if statements.
*for example, #if (variable$=1)
if (variable$=1)
*if the player pressed 1, then the RPG code in { and } is run.
mwincls()
mwin(Hi.)
wait(a$)
*if condition one is not true, then test the second condition
elseif (variable$=2)
*if the player pressed 2, then the RPG code in { and } is run.
mwincls()
mwin(How are you?)
wait(a$)
*if none of these conditions are true, then run the RPG code inside
*the { and } of the #else() statement
else()
*if the player pressed 3, then the RPG code in { and } is run.
*nothing happens, and program ends, because the program is over.
7. #While, #branch
In the previous example, the player might have pressed something other than 1 or 2, and then no RPG code would have been run. #While statements may be used to fix this:
#mwin(What would you like to do?)
#mwin(-1- say hi)
#mwin(-2- say how are you)
#mwin(-3- not talk)
*make sure the variable you use for your #while statement isnt used
*somewhere else in your game. loop!, which is the variable used in the
* #while statement, should be set to zero every time this program is run.
#loop!=0
*as long as loop!=0, following inside the #while statement will keep
*on running.
#while (loop!=0)
*place #wait at the beginning inside the { and } of the #while
*statement.
#wait(variable$)
#if (variable$=1)
#mwincls()
#mwin(Hi.)
#wait(a$)
*loop does not equal 0, so the loop stops after the rest of the
*RPG code runs.
#loop!=1
#if (variable$=2)
#mwincls()
#mwin(How are you?)
#wait(a$)
*loop does not equal 0, so the loop stops after the rest of the
*RPG code runs.
#loop!=1
#if (variable$=3)
*loop does not equal 0, so the loop stops after the rest of the
*RPG code runs.
#loop!=1
The #branch command can be used to branch back to a certain point. The usual format for a #branch statement is the following.
*the :any_name before the #branch statement is where the #branch
*statement branches to. this can be called any name, but has to have a :
*or colon before the name.
:any_name
*inside the ( and ) of the branch statement is the place to branch to. the
*: or colon should be included.
#branch(:any_name)
#Branch can be used for purposes like this:
#mwin(What would you like to do?)
#mwin(-1- say hi)
#mwin(-2- say how are you)
#mwin(-3- not talk)
#loop!=0
#while (loop!=0)
#wait(variable$)
#if (variable$=1)
*branch to :loop
#branch(:loop)
#if (variable$=2)
*branch to :loop2
#branch(:loop2)
#if (variable$=3)
*branch to :loop3
#branch(:loop3)
:loop
#mwincls()
#mwin(Hi.)
#wait(a$)
*branch to :loop3, which is the end of the program
#branch(:loop3)
:loop2
#mwincls()
#mwin(How are you?)
#mwincls()
*program ends because the program is over
:loop3
#Branch can also be used like a #while statement with #else and #elseif in RPG toolkit version 3:
:loop
mwin(What would you like to do?)
mwin(-1- say hi)
mwin(-2- say how are you)
mwin(-3- not talk)
wait(variable$)
if (variable$=1)
mwincls()
mwin(Hi.)
wait(a$)
elseif (variable$=2)
mwincls()
mwin(How are you?)
wait(a$)
elseif (variable$=3)
else()
*the player did not press 1, 2, or 3, so the text is cleared, and the
*the program branches to :loop.
mwincls()
branch(:loop)
8. Other RPG code commands
Now that you know the basics to RPG code, you might want to know some commands to use in RPG code programs. The first line is the format for RPG toolkit version 2, and the second line is for RPG toolkit version 3.
#Inn()
Inn()
Restores player stats
Example:
#mwin(Welcome to an inn.)
#wait(a$)
#mwincls()
#inn()
#mwin(Players stats restored)
#wait(a$)
#mwincls()
#mwin(Have a nice day.)
#wait(a$)
mwin(Welcome to an inn.)
wait(a$)
mwincls()
inn()
mwin(Players stats restored)
wait(a$)
mwincls()
mwin(Have a nice day.)
wait(a$)
#Givegp(gp!)
Givegp(gp!)
Give player gp, gp! stands for a numeric amount such as 10 with no quotes around the numeric amount (no )
Example:
#if (getgp!=1)
#mwin(No gp)
#wait(a$)
#if (getgp!=0) {
#givegp(10)
#mwin(Player found 10 gp)
#wait(a$)
#getgp!=1
if (getgp!=1)
mwin(No gp)
wait(a$)
if (getgp!=0) {
givegp(10)
mwin(Player found 10 gp)
wait(a$)
getgp!=1
#Giveitem(itemfilename.itm)
Giveitem(itemfilename.itm)
Give player an item. itemfilename is the filename of the item with .itm.
Example:
#if (getitem!=1)
#mwin(no item)
#wait(a$)
#if (getitem!=0)
#giveitem(item.itm)
#mwin(Player found an item)
#wait(a$)
#getitem!=1
if (getitem!=1)
mwin(no item)
wait(a$)
if (getitem!=0)
giveitem(item.itm)
mwin(Player found an item)
wait(a$)
getitem!=1
#takegp(gp!)
takegp(gp!)
Take gp from player, gp! stands for amount of gp to take from player with no quotes (no )
Example:
#takegp(10)
#givegp(10)
takegp(10)
givegp(10)
#takeitem(itemfilename.itm)
takeitem(itemfilename.itm)
Take item from player, itemfilename is the filename of the item with .itm
Example:
#takeitem(item.itm)
#giveitem(item.itm)
takeitem(item.itm)
giveitem(item.itm)
#send(boardfilename.brd, x!, y!, layer!)
send(boardfilename.brd, x!, y!, layer!)
Puts player at another position on the same or on another board, boardfilename is the filename of the board you want the player to be put on with .brd, x! is the first coordinate that you want the player to be put on (for example: 5, 5 the first number is x!, the second number is y!), y! is the second coordinate that you want the player to be put on, layer! is the layer you want the player to be put on (if you dont use layers in your game, then layer! can equal 1
Example:
#send(board.brd, 5, 5, 1)
send(board.brd, 5, 5, 1)
#callshop(itemfilename.itm, itemfilename2.itm)
callshop(itemfilename.itm, itemfilename2.itm)
Opens a shop window, itemfilename is the file name of a item in a shop, itemfilename2 is the file name of a second item in a shop, there is no limit for how many items there can be in a shop
Example:
#callshop(item.itm, item2.itm)
callshop(item.itm, item2.itm)
9. Review
#Mwin: message box, #mwin(text)
#Wait: tells computer to wait for player to press any key, key is saved into variable inside ( and ) of #wait statement, #wait(a$)
#Mwincls: message box clears
Variables: ! for numeric variable, $ for text variable
#If, #else, #elseif: if condition is true, then RPG code between { and } of #if statement is run, else, if other condition is true, then RPG code between { and } of #elseif statement is run, else, if none of the conditions are true, then RPG code between { and } of #else statement is run,
#if (variable!=0)
rpg code to be run
for RPG toolkit version 3 only
elseif (variable!=1)
rpg code to be run
else()
rpg code to be run
#While, #branch: while condition is true, then RPG code between { and } of #while statement is run, #branch: run program starting from the point that #branch branches to
variable!=0
#while (variable!=0)
rpg code to be run
:branch
#branch(:branch)
Other RPG code commands:
#inn()
#givegp(gp!)
#giveitem(itemfilename.itm)
#takegp(gp!)
#takeitem(itemfilename.itm)
#send(boardfilename.brd, x!, y!, layer!)
#callshop(itemfilename.itm, itemfilename2.itm)
**Browse Sections**
