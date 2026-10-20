---
kind: file
id: "toolkitzone.com/598"
site: "toolkitzone.com"
title: "Authored by: TriLex"
original_url: "http://www.toolkitzone.com/fileman.php?id=10&file=598"
written: null
date_confidence: "unknown"
updated: null
captured: ["20041031232226", "20041103132510", "20041106041337"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_598", captured: "20041031232226", sha256: "95bc67bb3bc0c31a078086c5ccc987f97814f5a3c70172a4e1b3b71548a0b082", wayback_url: "https://web.archive.org/web/20041031232226/http://www.toolkitzone.com/fileman.php?id=3&file=598"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_598", captured: "20041103132510", sha256: "e05ed652c6f4b7dd68aa491d5455b7cdd1ae90126e2a007d38088bdcc50bcec4", wayback_url: "https://web.archive.org/web/20041103132510/http://www.toolkitzone.com/fileman.php?id=5&file=598"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_598", captured: "20041106041337", sha256: "b63c43b3fd955ae8b6c89531ff54780dd4aa40a996a0a9ed91cab19494d112c8", wayback_url: "https://web.archive.org/web/20041106041337/http://www.toolkitzone.com/fileman.php?id=10&file=598"}
---

# Authored by: TriLex

***A 52team Document***
***52team***
***Steps to making a decent Battle system***
***Example Code Version***
***vol. 1***
***Volume 1***
***Introduction***
***ch.1 The beginning***
***s1.1Preparation***
***s1.2Programming Set-up(part 1)***
***s1.3Programming Set-up(part 2)***
***ch.2 Menu Programming***
***s2.1Graphic Lay-out***
***s2.2Menu Animation and Input***
***s2.3Menu Sections** -*Note: this section is not thoroughly explained*
***ch.3 Graphics Programming***
***s3.1Animation***
***s3.2Features***
***Volume 2***
***ch.4 Enemy Programming***
***s4.1Attacking***
***s4.2Enemy A.I.***
***ch.5 Mathimatical Programming***
***s5.1Calculating Strikes***
***s5.2Other Features***
***ch.6Features***
***s6.1Battle End***
***s6.2Cut-scenes***
***s.6.1Interrupted battles***
***Conclusion***
***Introduction***
**Welcome to the steps to making a decent battle system tutorial. This tutorial was made for those who understand rpgcode and know the commands atleast at an interdemediate level. This tutorial version will show you step by step how to make a decent turn-based battle system. It was made to ease the transition from the default battle system to your own custm battle system and so more custom batte systems could be made in a shorter amount of time. This tutorial is split into two volumes further split into five chapters with each chapter usually containing two to three sections. Since this is the example version most of this tutorial will be actual code.**
***Chapter 1: The Beginning***
**s1.1 Preparation**
**The first few steps to making a battle systems are very simple in almost any case. First thing's first...notes. Always remember to have your notes ready. This is better done with a paper and pencil. Notes will usually consist of a list of all variables, what they do or hold, and names of monsters and their variables etc. To prepare is to already have enough graphics to complete your entire battle system (you do not always need all of your graphics finished but you do need enough to test the bs.) My battle system set up is different from others. This setup is the one I recommend but not nessicarily the best. First have all program files starting with the same word. One example is to have all files starting with "bs.enterwordhere.prg". When this format is used all of the files of the battle system will be located next to each other and will increase organization beacuse of the "bs.".**
**s1.2 Programming Set-up(part 1)**
**Yes, you are technically programming now. What you should do in this section is set up all variables and methods. First, most of the variables should be stored in a file that you will be able to remember. Once again the same first letters will be used for the filename. Example: "bs.variable.prg". Here in this file is where you will enter most of your numerical(!) variables and your constant($) variables. Be sure to make your variable's some how related to it's usage. Here is an example list of variables.**
***********************
***bs.variable.prg***
***-------------------------------------------------------------------------------------------------------------------------**
***#plyrspeed!==4***
***#attack0!==Orion[fight]!***
***#health0!==Orion[health]!***
***#defence0!==Orion[defence]!***
***#special0!==Orion[smpower]!***
***#if(enemyn!==2)***
***#enemy1$=="Boulder"***
***#enemy1hp!==1***
***#enemy1fp!==0***
***#enemy1dp!==3***
***#enemy1sp!==0***
***#enemy1mp!==0***
***#enemy2$=="Green Jik[2]"***
***#enemy2hp!==63***
***#enemy2fp!==10***
***#enemy2dp!==9***
***#enemy2sp!==10***
***#enemy2mp!==0***
***-------------------------------------------------------------------------------------------------------------------------**
**Those are all of the varibles that will be declared in this program file. Once you see your variables you should be able to instantly recongnize it and what it holds. It is alot easier if you give almost every enemy on the battle field a variable. the variable enemyn! is equal to the number of enemies that you are battling. Every enemy should have a type id number. This is represented by variables. The Boulder's id number is 1. The Green Jik's id number is 2 and so forth. This is where notes should come in to help you with the id numbers. This example program is kept simple by including only two different enemies.**
**Now we will add actual commands and methods to these variables to get the battle ready to begin. Here is a commented example of a bs.variable.prg program file.**
*****Note: "bs.variable.prg" is NOT the first file that will be run in your battle system. There is another program file that randomizes the battle. That will be introduced later. This file will not run properly by itself.*****
***********************
***bs.variable.prg***
***-------------------------------------------------------------------------------------------------------------------------**
***#plyrspeed!==4 *1) This is a variable to see who will attack first***
***#Send(battle$,22,4,1) *2) Send to the board "battle$"***
***#CharacterSpeed(3) *3) Its just the charcter walk speed***
***#Newplyr("orionfight.tem") *4) Basically changes the charcter's graphics to include a sword***
***#getenemystats() *Runs the methods to declare enemies and give them stats***
***#getenemystat2() ****
***#bsm.start()***
***#push("W") *5) The start of the fight...pushes the chracter***
***#push("W") * The start of the fight...pushes the chracter***
***#push("W") * The start of the fight...pushes the chracter***
********************Char. One***
***#attack0!==Orion[fight]! *6) I took my main character's variables and***
***#health0!==Orion[health]! * put them in other variables so I can safely modify them.***
***#defence0!==Orion[defence]!***
***#special0!==Orion[smpower]!***
***#run("bs.main.prg") *10) Run's the main battle system, when that program is run***
**** This file is not to be run again until the next battle***
****************************************
***#method getenemystats()***
***#if(enemy1!==1)***
***#put(6,4,"boarditm.tst31.gph") *7) The graphics for the boulder***
***#put(5,4,"boarditm.tst33.gph")***
***#put(4,4,"boarditm.tst32.gph")***
***#enemy1$=="Boulder"***
***#enemy1hp!==1 *8) The boulde's hit points***
***#enemy1fp!==0 * The boulder's attack***
***#enemy1dp!==3 * The boulder's defense***
***#enemy1sp!==0 * The boulder's special power***
***#enemy1mp!==0 * The boulder's magical power***
******************************
****Any other thing you***
****may want to add in***
******************************
***#method getenemystats2()***
***#if(enemyn!==2) *9) Checks to see if there is more than 1 enemy***
***#if(enemy2!==3)***
****Green jik*******
****11,4***
***#LayerPut(9,5,2,"hhhhh000.gph") *8) Basically the same as above***
***#LayerPut(10,5,2,"hhhhh001.gph")***
***#LayerPut(9,6,2,"hhhhh025.gph")***
***#LayerPut(10,6,2,"hhhhh026.gph")***
***#enemy2$=="Green Jik[2]"***
***#enemy2hp!==63***
***#enemy2fp!==10***
***#enemy2dp!==9***
***#enemy2sp!==10***
***#enemy2mp!==0***
************************
***-------------- END ------------------------**
***Here are the explanations.***
***1) "plyerspeed!" is a variable that will be used later on. It's function is to hold the value of the speed of the main character. This will be compared to the enemy's speed variable and that will determine who attacks first. This will be introduced later.***
***2) "battle$" is the variable that contains your battle location/board name. This is where your player get sent once a battle has begun. Using a board for your battle systems is alot easier than using bitmaps. Try each out for yourself to understand why.***
***3) Changes your charcter's walk speed eg. when you are walking to attack.***
***4) This changes ALL of your chacter graphics to that of "orionfight.tem" That is basically his fighting graphics.***
***5) This just pushes the character 3 spaces west.***
***6) These are all of your character's battle variables(yu could get it by going into edit character, then click on the advanced tab). I have put them in other variables just to be safe. Now if you lose hp instead of the main variable "Orion[health]!" getting lower the sidekick variable or pointer variable "health0!" gets lowered. Then the main variable ("Orion[health]!") is then made to equal the pointer variable ("health0!").***
***7) The premade graphics for the enemy, in this case a practice boulder.***
***8) The enemy's stats, in this case boulder.***
***9) All it does is checks to see if there is more than 1 enemy.***
***10) "bsm.prg" holds some methods and those methods will be introduced later. The method "#start" (in bsm.prg) will just start the music and get everthing ready.***
***11) Run's the main battle and brings up the selcet menu.***
**s1.3 Programming Set-up(part 2)**
**Alright you now have almost enough information to get the battle started. But now you need some more information including variables for music, battlescene, and enemy choices.This is fairly easy to make. "bs.random.prg" is just one big random program. It should look something like this...**
***********************
***bs.random.prg***
***-------------------------------------------------------------------------------------------------------------------------**
***#orx!==playerX[0]! *1)Gets the player's x and y coordinates.***
***#ory!==playerY[0]!***
***#random(3,battle!) *2) randomizes the variable "battle!"***
***#if(battle!==1)***
***#battle$=="Enter name here.brd" *3)Saves the battling board in "battle$"***
***#if(battle!==2)***
***#battle$=="Enter name here.brd" *3)Saves the battling board in "battle$"***
***#if(battle!==3)***
***#battle$=="Enter name here.brd" *3)Saves the battling board in "battle$"***
****and so forth***
***#random(2,enemyn!) *4)Randomizes the variable "oos!"***
***#if(enemyn!==1) *5) Usage stated below***
***{ *5) Usage stated below***
***#random(2,enemy1!) ****
**********************
****And so forth***
**********************
****************************
***#if(enemyn!==2) *6) Usage stated below***
***{ *6) Usage stated below***
***#random(2,enemy2!) ****
***#run("bs.variable.prg") *7) Runs "bs.variable.prg"***
***-------------------------------------------------------------------------------------------------------------------------**
***Here are the explanations.***
***1) All it does it sends the main coordinate x and y variables ("playerX[0]!"and"playerY[0]!") to "orx!" and "ory!". This is done because once you are sent to a different board (eg. when the battle starts) the variables("playerX[0]!"and"playerY[0]!") change to your new coordinates. Because we made "orx!" and "ory!" equal to your original coordinates before you were sent to a new board you still have your coordinates in our own variables ("orx!" and "ory!").***
***2) This just randomizes the battle location. The 3 in "#random(3,battle!)" can be any number of you want the character to be sent to. (But then you have to make a few changes tto the code).***
***3) After the #random command has taken effect the #if command will then take effect. If it is randomized to one then the first board's handle or name will be saved into "battle$". If it is randomized to two then the second board then the second boards handle or name will be saved int "battle$". And so forth. As you can see in "bs.variable.prg" the "battle$" variable is where you were sent.***
***4) This just randomizes the the number of enemies. You couldn't exactly tell that just by looking at the code. For now you will use a maximum of two enemies.***
***5) From the randomization of step 4 it will then check if the random command turned ot to be two. If it is you will have two enemies. The randomization of enemy1! will then be used to to randomized who your 1st enemy will be.***
***6) Basically the same as step four but in this case it is for enemy 2.***
***7) Runs "bs.variable.prg"***
***Alright you already have everything set-up. You are almost ready to start the battle. You just need to let the user play and allow time for input. And that is covered in the next chapter***
***Chapter 2: Menu Programming***
**s2.1 Graphic Lay-out**
**Most people start programming their battle systems by first constructing the menu, then start programming what we already have programmed. But not in this tutorial, for the most part we will go in chronological order, just like the actual battle. Menu programming is not that difficult at all. Its basically programming a menu system. All you have to do is choose your base color, then display the options the player will be able to select (attack,special,etc.) For now here is a good base rectangle. As always all of this will be explained later.**
**Note: To keep this tutorial simple we will not use bitmaps**
********************
***bs.main.prg***
***-------------------------------------------------------------------------------------------------------------------------**
***#method main()***
***#colorrgb(40,40,160)***
***#fillrect(1,230,606,350)***
***#color(0)***
***#drawrect(0,320,300,351)***
***#drawrect(0,321,300,351)***
***#drawrect(300,230,606,350)***
***#drawrect(301,230,606,350)***
***#drawrect(0,229,607,351)***
***#fontsize(28)***
***#colorrgb(255,255,255)***
***#text(13,9.7,"Attack")***
***#text(13,10.9,"Magic")***
***#text(13,12.1,"Ability")***
***#text(18,9.7,"Defend")***
***#text(17.9,10.9,"Special")***
***#text(18.4,12.1,"Item")***
***#fontsize(22)***
***#text(1.2,11.7,"")***
***#text(1.2,12.9,"")***
***#text(1.2,14.2,"")***
***#fontsize(14)***
***#text(1.2,24.1,"HP:")***
***#text(1.2,25.1,"SP:")***
***#text(9.2,24.1,"MP:")***
***#text(9.2,25.1,"LP:")***
***#bold("on")***
***#text(18.2,24.1,"Orion")***
***#bold("off")***
***#main***
***#wait***
***-------------- END ------------------------**
**s2.2 Menu Animation and Input**
**As you can see the above will make a dark blue, final fantasy style menu. The options will include attack, magic, special, item, defend, and ability. This menu will also show your health in the lower left corner and your enemy name's in a little window. This is basic enough, but it still does not do anything, our battle system still has no actual user input in it. To get user input you should already know that you have to use the "#wait" command and a variable. And if you want some animation you should not only program new rectangles you should also make rectangles the same color to cover existing rectangles. This hard to explain so I won't. So, now that we have a menu let's animate and accept input like this...**
***********************
***bs.main.prg***
***-------------------------------------------------------------------------------------------------------------------------**
***#method main()***
***#colorrgb(40,40,160) *1) Selects the backround menu color***
***#fillrect(1,230,606,350) *2) Helps make the menu***
***#color(0) *3) Selects the menu subsection box color***
***#drawrect(0,320,300,351) *4) Makes either the black outline of the menu or black subsections***
***#drawrect(0,321,300,351) ****
***#drawrect(300,230,606,350) ****
***#drawrect(301,230,606,350) ****
***#drawrect(0,229,607,351) ****
***#fontsize(28) *5) Chooses the font size***
***#colorrgb(255,255,255) *6) Chooses the color white for the words***
***#text(13,9.7,"Attack") *7) An user picked menu option in this case attack***
***#text(13,10.9,"Magic") *7) An user picked menu option in this case magic***
***#text(13,12.1,"Ability") *7) An user picked menu option in this case ability***
***#text(18,9.7,"Defend") *7) An user picked menu option in this case defend***
***#text(17.9,10.9,"Special") *7) An user picked menu option in this case special***
***#text(18.4,12.1,"Item") *7) An user picked menu option in this case item***
***#fontsize(22) *8) Chooses the font size***
***#text(1.2,11.7,"") *9) Shows the first enemy's name in a subsection box***
***#text(1.2,12.9,"") *9) Shows the second enemy's name in a subsection box***
***#text(1.2,14.2,"") *9) Shows the third enemy's name in a subsection box***
***#fontsize(14) *10) Chooses the font size***
***#text(1.2,24.1,"HP:") *11) Shows the users remaining health***
***#text(1.2,25.1,"SP:") *11) Shows the users remaining special power***
***#text(9.2,24.1,"MP:") *11) Shows the users remaining magic points***
***#text(9.2,25.1,"LP:") *11) Shows the users remaining life points***
***#bold("on") *12) Turns bold on***
***#text(18.2,24.1,"Orion") *13)Displays the player's name in a subsection box***
***#bold("off") *12) Turns bold off***
**************************
***#method cover() *14) Declares the method "#cover()".***
**** The entire method will be covered below.***
***#colorrgb(40,40,160) ****
***#drawrect(310,274,440,241) ****
***#drawrect(311,274,441,241) ****
***#drawrect(310,274,440,309) ****
***#drawrect(311,274,441,309) ****
***#drawrect(310,344,440,309) ****
***#drawrect(311,344,441,309) ****
***#drawrect(455,344,578,309) ****
***#drawrect(454,344,579,309) ****
***#drawrect(455,274,578,309) ****
***#drawrect(454,274,579,309) ****
***#drawrect(455,274,578,241) ****
***#drawrect(454,274,579,241) ****
***#main() *15) Runs the earlier declared method above "#main()"***
***************************************
***:attack *16) Creates a branch label named ":attack"***
***#cover *17) Runs the earlier declared method above "#cover()"***
***:no *18) Creates a branch label named ":no"***
***#color(0)***
***#drawrect(390,190,500,200) *19) Displays a rectangle on the screen the color black***
***#drawrect(310,274,440,241) *19) Displays a rectangle on the screen the color black***
***#drawrect(311,274,441,241) *19) Displays a rectangle on the screen the color black***
***#wait(move$) *20) Waits for the user to press a button***
***#if(move$=="UP") *21) Checks to see if the user press the button "UP"***
***#branch(:no) *22) Branches to ":no" or #18***
***#if(move$=="DOWN") *21) Checks to see if the user press the button "DOWN"***
***#branch(:magic) *22) Branches to ":magic"***
***#if(move$=="RIGHT") *21) Checks to see if the user press the button "RIGHT"***
***#branch(:defend) *22) Branches to ":defend" or #26***
***#if(move$=="LEFT") *21) Checks to see if the user press the button "LEFT"***
***#branch(:no) *22) Branches to ":no" or #18***
***#if(move$=="ENTER") *21) Checks to see if the user press the button "ENTER"***
***#savescreen() *23) Saves the screen for later use with "#restorescreen"***
***#run("bs.attack.prg") *24) Runs the program file "bs.attack.prg"***
***************************************
***:defend *25) Creates a branch label named ":defend"***
***#colorrgb(40,40,160)***
***#cover *26) Runs the method "#cover()"***
***:nod *27) Creates a branch label named ":nod"***
***#color(0)***
***#drawrect(455,274,578,241) *28) Draws a rectangle on the screen***
***#drawrect(454,274,579,241) ****
****---------------------------------------------------------------------------------------------------****
****THE REST OF THIS FILE IS BASICALLY THE SAME AS ABOVE****
****---------------------------------------------------------------------------------------------------****
***#wait(def$)***
***#if(def$=="RIGHT")***
***#branch(:nod)***
***#if(def$=="UP")***
***#branch(:nod)***
***#if(def$=="DOWN")***
***#branch(:special)***
***#if(def$=="LEFT")***
***#branch(:attack)***
***#if(def$=="ENTER")***
****************************************
***:special***
***#cover***
***:nos***
***#color(0)***
***#drawrect(455,274,578,309)***
***#drawrect(454,274,579,309)***
***#wait(spe$)***
***#if(spe$=="DOWN")***
***#branch(:item)***
***#if(spe$=="RIGHT")***
***#branch(:nos)***
***#if(spe$=="UP")***
***#branch(:defend)***
***#if(spe$=="LEFT")***
***#branch(:magic)***
****************************************
***:item***
***#cover***
***:noi***
***#color(0)***
***#drawrect(455,344,578,309)***
***#drawrect(454,344,579,309)***
***#wait(ite$)***
***#if(ite$=="UP")***
***#branch(:special)***
***#if(ite$=="RIGHT")***
***#branch(:noi)***
***#if(ite$=="LEFT")***
***#branch(:ability)***
***#if(ite$=="DOWN")***
***#branch(:noi)***
***************************************
***:ability***
***#cover***
***:noabi***
***#color(0)***
***#drawrect(310,344,440,309)***
***#drawrect(311,344,441,309)***
***#wait(abi$)***
***#if(abi$=="UP")***
***#branch(:magic)***
***#if(abi$=="DOWN")***
***#branch(:noabi)***
***#if(abi$=="RIGHT")***
***#branch(:item)***
***#if(abi$=="LEFT")***
***#branch(:noabi)***
***************************************
***:magic***
***#cover***
***:nomag***
***#color(0)***
***#drawrect(310,274,440,309)***
***#drawrect(311,274,441,309)***
***#wait(mag$)***
***#if(mag$=="UP")***
***#branch(:attack)***
***#if(mag$=="RIGHT")***
***#branch(:special)***
***#if(mag$=="DOWN")***
***#branch(:ability)***
***#if(mag$=="LEFT")***
***#branch(:nomag)***
***#if(mag$~"ENTER")***
***#branch(:attack)***
***********************************************************************************************************************
************************************
***-------------- END ------------------------**
***Here are the explanations.***
***** The first line just declares the method "#main()". Remember, "#main()" is the graphical part of the menu. It has nothing to do with user input. It displays all of your options eg. attack, defend, magic, etc., some of your stats, and even your enemy's names.***
*********
***1) Uses colorrgb() to select the backround color. In this case "40,40,160" is a darkish-blue color.***
***2) This makes the backround rectangle of the menu.***
***3) Uses the command "#color" to select the color "0" (which is black)***
***4) These rectangles are used to make the sub-sections of the menu. In this case all of the lines are of the color black.***
***5) Chooses the font size.***
***6) Uses colorrgb() to select the backround color. In this case "255,255,255" is white.***
***7) Displays text the color white. This text is the text ou will be able to see while running. It shows your selectable options (attack, magic, ability, defend, special, item,)***
***8) Chooses the font size.***
***9) Displays the enemys' name in a subsection box. Because it uses variables, if there is only one enemy the rest will by default be empty.***
***10) Chooses the font size.***
***11) Display's the player's stats. The player's remaining health, SP, MP, and LP are all shown in a subsection-box.***
***12) Turns bold on***
***13) Displays the player's name, in this case "Orion"***
***14) Declares the method "#cover". This method is used obviously to cover something. But what it's main purpose is to cover the selector rectangles. When ever you press an arrow key a rectangle should move to wherever the direction you pressed. But if there were no cover method in this battle system the rectangle would leave a trail of white rectangles whenever you move. So, the cover method justs prevents this by happening by covering over wherever the trail of the selector rectangle is.***
***15) Runs "#main()" which was declared ealier.***
***16) Creates a branch label name ":attack"***
***17) Runs "cover()" which was declared ealier.***
***18) Creates a branch label name ":no"***
***19) Creates black rectangles on the screen.***
***20) Waits for the user to press a button and stores that in "move$"***
***21) Checks to see what the user pressed. Either one of the directional keys or enter can be pressed to have an effect.***
***22) Branches to ":no" if "UP" was pressed. Meaning from there you cannot go up and you must re-select.***
***All the other directional keys also have effects. You can also press enter on attack to run "bs.attack.prg".***
***23) Saves the screen with the "#savescreen()"command and can later be re-opened with the "#restrorescreen()" command.***
***24) Runs the program file "bs.attack.prg"***
***25) Creates a branch label name ":defend"***
***26) Runs "cover()" which was declared ealier.***
***27) Draws a rectangle on the screen***
*********
***The rest of the file is almost exactly the same. It just contains modified versions of what you have just read. So, if you had already read the above you do not need any further explanations.***
*********
***Alright, good job you have made it this far. The above is what you need to get player input. The next section will explain menu sections; What happenes when the player presses enter?***
**s2.3 Menu Sections**
**Now that you could accept user input and animate the selector box...what happens when the user presses enter and wants to attack? This section will cover that. It is basically accepting user input like the above, but in this case it will allow the player to go to different sections of the bs. Allowing the user to analize his or her options. So, you could call these mini menus or sub menus, but whatever you call it, here is my way of programming it.**
***NOTE: This section is not commented at all. So, this tutorial can bdered incomplete. I will "complete" it in the next update. But the basics are it shows the enemies names, your name, your health. Andlows for the selection of the enemy to attack**
***********************
***bs.attack.prg ***
***-------------------------------------------------------------------------------------------------------------------------**
***#adraw()***
***#adraw2()***
***#color(0)***
***#text(1,2,"")***
***#text(1,3,"")***
***#text(1,4,"")***
***#text(1,5,"")***
***#text(1,6,"")***
***#colorrgb(255,255,255)***
***#fontsize(22)***
***#text(1.2,11.7,"")***
***#text(1.2,12.9,"")***
***#text(1.2,14.2,"")***
***#fontsize(28)***
***#colorrgb(255,255,255)***
***#text(12.3,9.34,"Back")***
***#fontsize(14)***
***#text(1.2,24.1,"HP:")***
***#text(1.2,25.1,"SP:")***
***#text(9.2,24.1,"MP:")***
***#text(9.2,25.1,"LP:")***
***#bold("on")***
***#text(18.2,24.1,"Orion")***
***#bold("off")***
***:att***
***#cover()***
***#drawrect(200,245,299,245)***
***#drawrect(200,244,299,244)***
***#kill(att$)***
***#wait(att$)***
***#if(att$=="ENTER")***
***#attack***
***#if(att$=="RIGHT")***
***:att2***
***#cover()***
***#drawrect(440,261,304,233)***
***#drawrect(441,261,305,233)***
***#wait(att2$)***
***#if(att2$=="LEFT")***
***#branch(:att)***
***#if(att2$=="ENTER")***
***#run("battlesys1.prg")***
***#if(att$=="DOWN")***
***#if(enemyn!==1)***
***#kill(att2$)***
***#kill(att$)***
***#branch(:att)***
***#if(enemyn!==2)***
***:ene2***
***#cover()***
***#kill(att2$)***
***#kill(att$)***
***#drawrect(200,270,299,271)***
***#drawrect(200,270,299,271)***
***#wait(spi$)***
***#if(spi$=="RIGHT")***
***#branch(:att2)***
***#if(spi$=="ENTER")***
***#attack2()***
***#if(spi$=="UP")***
***#branch(:att)***
***#if(spi$~"DOWN")***
***#branch(:ene2)***
***#if(spi$=="DOWN")***
***#branch(:att)***
***#method killav()***
***#kill(ah!)***
***#kill(ahy!)***
***#kill(ahyl!)***
***#kill(ad!)***
***#method attack()***
***#color(0)***
***#ah!==199***
***:pooph***
***#ah!==ah!-4***
***#drawrect(ah!,245,200,245)***
***#drawrect(ah!,244,200,244)***
***#if(ah!<150)***
***#branch(:poh)***
***#branch(:pooph)***
***:poh***
***#ad!==ah!+1***
***#ahy!==245***
***#ahyl!==ahy!***
***:jj***
***#drawrect(ah!,ahy!,ah!,244)***
***#drawrect(ah!,ahyl!,ah!,244)***
***#color(0)***
***#ahy!==ahy!-.5***
***#ahyl!==ahyl!+.5***
***#if(ahy!<231)***
***#branch(:pohl)***
***#branch(:jj)***
***:pohl***
***:seri***
***#ah!==ah!-1***
***#drawrect(ah!,232,ah!,231)***
***#drawrect(ah!,258,ah!,259)***
***#if(ah!<2)***
***#branch(:ll)***
***#branch(:seri)***
***:ll***
***#sel!==1***
***#command!==1***
***#killav()***
***#run("bs.attack.cal.prg")***
***#method attack2()***
***#color(0)***
***#ah!==199***
***:poolph***
***#ah!==ah!-4***
***#drawrect(ah!,271,200,270)***
***#drawrect(ah!,271,200,270)***
***#if(ah!<150)***
***#branch(:polh)***
***#branch(:poolph)***
***:polh***
***#ad!==ah!+1***
***#ahy!==270***
***#ahyl!==ahy!***
***:jjl***
***#drawrect(ah!,ahy!,ah!,271)***
***#drawrect(ah!,ahyl!,ah!,271)***
***#color(0)***
***#ahy!==ahy!-.5***
***#ahyl!==ahyl!+.5***
***#if(ahy!<258)***
***#branch(:polhl)***
***#branch(:jjl)***
***:polhl***
***:seril***
***#ah!==ah!-1***
***#drawrect(ah!,282,ah!,281)***
***#drawrect(ah!,258,ah!,259)***
***#if(ah!==2)***
***#branch(:lll)***
***#branch(:seril)***
***:lll***
***#command!==2***
***#killav()***
***#run("bs.attack.cal.prg")***
******************************
***#method cover()***
***#colorrgb(40,40,160)***
***#drawrect(200,270,299,271)***
***#drawrect(200,270,299,271)***
***#drawrect(440,261,304,233)***
***#drawrect(441,261,305,233)***
***#drawrect(200,245,299,245)***
***#drawrect(200,244,299,244)***
***#color(0)***
***#method adraw()***
***#colorrgb(40,40,160)***
***#fillrect(1,230,606,350)***
***#fontsize(28)***
***#colorrgb(255,255,255)***
***#method adraw2()***
***#color(0)***
***#drawrect(0,320,300,351)***
***#drawrect(200,245,299,245)***
***#drawrect(200,244,299,244)***
***#drawrect(300,230,606,350)***
***#drawrect(0,321,300,351)***
***#drawrect(301,230,606,350)***
***#drawrect(0,229,607,351)***
***#colorrgb(255,255,255)***
***-------------- END ------------------------**
***Chapter 3: Graphics Programming***
**s3.1 Animation**
**This is the section that will be explaining animation. This is different from the input section because this does not deal with the menu. Instead, it deals with what happens after you press the enter button on attack. This type of animation is or atleast should be the most important. This maybe the simpilest part of the entire battle system. Basically all it is is using the "push" command to push the charater west and change his/her (or whatever's) posture.**
********************
***bs.walk.prg***
***-------------------------------------------------------------------------------------------------------------------------**
***#method tilecover()***
***#Put(21,4,"swordangleo.gph")***
***#Put(12,3,"grass.gph")***
***#Put(10,4,"grass.gph")***
***#method battlewalk()***
***#push("w")***
***#push("w")***
***#push("w")***
***#tilecover()***
***#Put(12,4,"orion.tst38.gph")***
***#Put(11,4,"orion.tst37.gph")***
***#delay(.2)***
***#Put(11,4,"grass.gph")***
***#Put(12,4,"orion.tst35.gph")***
***#Put(12,3,"orion.tst36.gph")***
***#delay(.7)***
***#tilecover()***
***#push("e")***
***#push("e")***
***#push("e")***
***#push("e")***
***#push("w")***
***#battlewalk()***
***#run("bs.main.prg")***
***-------------- END ------------------------**
**Well, that's it for animation. The posture change allows the player to "animate" his/her attack. As you may notice it will link back to the beginning, causing it to allow the player to choose another action, thus for now completing the battle system loop.**
**s3.2 Features**
**This section is basically some features that aren't really features. Showing the amount of damage for me is classified as an mandatory feature. Also, allowing the**
********************
***bs.walk.prg***
***-------------------------------------------------------------------------------------------------------------------------**
***#method tilecover()***
***#Put(21,4,"swordangleo.gph")***
***#Put(12,3,"grass.gph")***
***#Put(10,4,"grass.gph")***
***#method battlewalk()***
***#push("w")***
***#push("w")***
***#push("w")***
***#tilecover()***
***#Put(12,4,"orion.tst38.gph")***
***#Put(11,4,"orion.tst37.gph")***
***#delay(.2)***
***#Put(11,4,"grass.gph")***
***#Put(12,4,"orion.tst35.gph")***
***#Put(12,3,"orion.tst36.gph")***
***#delay(.7)***
***#tilecover()***
***#push("e")***
***#push("e")***
***#push("e")***
***#push("e")***
***#push("w")***
***#savescreen()***
***#colorrgb(170,20,20)***
***#fontsize(19)***
***#if(command!==2)***
***#text(11.5,8,"")***
***#if(super!==15)***
***#text(16,10,"Effective Strike!")***
***#delay(1)***
***#branch(:hgfh)***
***#branch(:hgfh)***
***#text(7.5,5,"")***
***#if(super!==15)***
***#text(12,7,"Effective Strike!")***
***#delay(1)***
***:hgfh***
***#zzzzzzz.adraw()***
***#zzzzzzz.adraw2()***
***#fontsize(22)***
***#zzz.attackb***
***#fontsize(14)***
****#text(16.4,8,"")***
***#delay(1)***
***#restorescreen()***
***#if(enemy1hp!<.01)***
***#enemy1$==enemy1$+"-Destroyed"***
***#enemy1l!==1***
***#if(enemyn!==1)***
***#run("win1battle.prg")***
***#if(enemy2hp!<.01)***
***#enemy2$==enemy2$+"-Destroyed"***
***#enemy2l!==1***
***#if(enemy1l!==1)***
***#run("win1battle.prg")***
***#if(enemy3hp!<.01)***
***#enemy3$==enemy3$+"-Destroyed"***
***#enemy3l!==1***
***#if(enemy2l!==1)***
***#run("win1battle.prg")***
***#run("enemyturn.prg")***
***#battlewalk()***
***#Newplyr("l.tem")***
***-------------- END ------------------------**
**This should be able to allow the player to see the amount of damage he/she takes away. These features will be added upon in a future update.**
**Conclusion**
**Well, this is the end of Volume 1. It should have gave you some ideas to what your battle system should include, or help with your battle system. This file will be updated very soon to add more explainations and to allow the user to see a usable version of the battle system.**
