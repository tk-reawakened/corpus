---
kind: page
id: "rpgtoolkit.com/rpgtoolkit.com/docs/ver2/help3.htm"
site: "rpgtoolkit.com"
title: "RPGCode Command Reference"
original_url: "http://www.rpgtoolkit.com/docs/ver2/help3.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20010419075747", "20010722131618"]
author: null
repliers: []
authors: []
comments_present: 0
f_format: "This command places a blank line in the Message Window. This command must be used instead of simply placing a blank line in your programs, because blank lines are ignored by the computer. It must appear on a line by itself."
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.com/docs/ver2/help3.htm", captured: "20010419075747", sha256: "89725184ed6e1796552200466d213ac489a70722bfcbd895a302e085e85232c9", wayback_url: "https://web.archive.org/web/20010419075747/http://www.rpgtoolkit.com/docs/ver2/help3.htm"}
  - {path: "wayback/rpgtoolkit.com-asof2005/docs/ver2/help3.htm", captured: "20010722131618", sha256: "d942c57bb3d21443ed1dbf935631fa607bb65e37d35542d0c70956954a834f49", wayback_url: "https://web.archive.org/web/20010722131618/http://www.rpgtoolkit.com/docs/ver2/help3.htm"}
---

# RPGCode Command Reference

Blank Line
At this point, you have learned enough about programming in RPGCode that you can create very flexible programs. There are more commands in RPGCode, however, and many are very useful in creating special effects, or pretty much anything you could think of. All the commands for RPGCode are alphabetically listed and explained in detail in the following pages...
**
@
**
This command places a blank line in the Message Window. This command must be used instead of simply placing a blank line in your programs, because blank lines are ignored by the computer. It must appear on a line by itself.
**
Example:
A blank line will follow this line.
There is a blank line above this.
Comment Specifier**
*
**
***** *Comment*
This symbol is used to tell the computer that a comment follows. Comments are ignored by the program, and are to be used as notes to yourself as to what the program does.
You can put a comment after a command as long as you properly enclose the command parameters in brackets.
**
Example:
* This program was created 2/11/99
#GiveItem("sword.itm") *Gives the player a sword.
Add player to party.**
#AddPlayer
**
#AddPlayer(player_filename$)
This command adds a player to the current party (team). There are a maximum of 5 characters allowed on a team at any time. player_filename$ is a literal value that is the filename of the player to add. If you don’t include the .Tem extension, it is added for you. Also, do not include any directory information as RPGCode will add it for you.
When the player is added, all stats (HP/SMP/DP, etc) are set to their initial values.
**
Example:
* Add player Tano to your team.
#AddPlayer("Tano.tem")
Access internal AI.**
Related Commands:
#RemovePlayer
#AI
**
#AI(level!)
This command causes an enemy to use its internal Artificial Intelligence routines. This command can only be used from an enemy AI program (See enemy editor/tactics). Level! Is a numerical value between 0 and 3. 0 is the lowest AI, 3 is the highest.
**
Example:
*Enemy AI program.
#move!=move!+1
#if(move!==1)
#AI(0)
#if(move!==2)
#AI(3)
#if(move!==3)
#Mwin("Aren’t you getting tired of me?")
#if(move!>3)
#move!=1
Attack all enemies/players.**
Related Commands:
#AttackAll, #DrainAll
**
#AttackAll
**
#AttackAll(fp!)
This command attcaks all enemies or players in battle. When used with a special move, this will damage the group of enemies or players depending upon which group was targeted by the player. Fp! Is a literal value specifying the amount of Fight Power to use.
**
Example:
#AttackAll(100)
Adjust battle speed.**
Related Commands:
#DrainAll
#BattleSpeed
**
#BattleSpeed(speed!)
This command adjusts the speed at which fighting occurs in your game. Speed! Is a numerical value and is a number between 0 and 7. 7 is the fastest speed. 0 is the default.
**
Example:
#BattleSpeed(7)
#FightEnemy("bubba.ene","bkg.bkg")
Display bitmap.**
Related Commands:
#BattleSpeed, #TextSpeed
#Bitmap
**
#Bitmap(file$)
This command displays a bitmap on the screen. file$ is the filename of the graphic (either BMP, WMF, GIF or JPG).
**
Example:
#Bitmap("title.bmp") *Show title screen.
Turn font bold on/off.**
Related Commands:
#ViewBrd
#Bold
**
#Bold("on/off")
This command turns the bold effect on the font on or off. The parameter is just a literal value that says "on" or "off".
**
Example:
#Bold("off")
#MWin("Boring regular text..")
#Bold("on")
#MWin("All of a sudden, I feel bolder!")
#Italics("on")
#MWin("Hey, italics, too!")
#Underline("on")
#MWin("Even an underline!")
#Wait(a$)
Change border color.**
Related Commands:
#Bold, #Color, #ColorRGB, #Font, #FontSize, #Italics, #Mwin, #MWinCls, #Underline, #WinGraphic, #WinColorRGB
#BorderColor
**
#BorderColor(red!, green!, blue!)
This command changes the color of the border surrounding the view window. Red!, Green! And Blue! Are literal values between 0 and 255 and represent the amount of red, green and blue that goes into the color.
**
Example:
#BorderColor(255,0,0)
* Change border to red
Branch Command**
Related Commands:
#Color
**
#Branch
**
**#Branch (** *:label name* **)** is case sensitive, which means that the capital letters and spaces of the label name in the command must match up with the capital letters and spaces in the label name.
This command is used to branch, or skip to another part of the program. Throughout the program, you must create , which identify where the command is to branch to. *labels*
Labels must appear on a line by themselves, and they have a ':' symbol in front of them. is used to skip through the program to these labels. **#Branch**
**
#Branch
**#Branch**
Using the #Branch command is an old way of doing things. It is entirely possible to write programs using if statements and while loops instead.
**
Example:
#Mwin("Line 1")
#MWin("Line 2")
#Branch (:next line)
#MWin("Line 3")
:next line
#MWin("Line 4")
* The words "Line 3" were skipped, because we
* branched to the label :next line before reaching
* "Line 3".
Open player swap window.**
Related Commands:
#Fbranch, #Run
#CallPlayerSwap
**
#CallPlayerSwap()
This command opens the player swap menu. It allows you to remove players from your party and add others. The players that are available to be added are those that were removed with the #RemovePlayer command (not #DestroyPlayer).
**
Example:
#CallPlayerSwap()
Open shop window.**
Related Commands:
#AddPlayer, #RemovePlayer
#CallShop
**
#CallShop("item1.itm", "item2.itm", …)
This command opens a shop window where the player can buy and sell items. The arguments passed are literal values, ecah one is the filename of an item that the shopkeeper sells. The buying and selling prices of items are determined by the values set in the Item Editor.
**
Example:
#CallShop("sword.itm", "shield.itm", "grenade.itm")
* Opens a shop window selling 3 items
Cast floating point numerical to integer numerical.**
Related Commands:
#GP
#CastInt
**
#CastInt(source!, dest!)
This command will take a floating point number (a number with a decimal-- source!) and discard the decimal part, thus placing an integer value in dest!
**
Example:
#CastNum("438",num1!)
#Show(num1!) *Output: 438
#CastLit(1824,lit1$)
#Show(lit1$) *Output: 1824
#CastInt(10.895,num2!)
#Show(num2!) *Output: 10
Cast numerical to literal.**
Related Commands:
#CastLit, #CastNum
#CastLit
**
#CastLit(source!, dest$)
This command will convert a numerical variable (source!) to a literal variable (dest$).
**
Example:
#CastNum("438",num1!)
#Show(num1!) *Output: 438
#CastLit(1824,lit1$)
#Show(lit1$) *Output: 1824
#CastInt(10.895,num2!)
#Show(num2!) *Output: 10
Cast literal to numerical.**
Related Commands:
#CastInt, #CastNum
#CastNum
**
#CastNum(source$, dest!)
This command will convert a literal variable (source$) to a numerical variable (dest!).
**
Example:
#CastNum("438",num1!)
#Show(num1!) *Output: 438
#CastLit(1824,lit1$)
#Show(lit1$) *Output: 1824
#CastInt(10.895,num2!)
#Show(num2!) *Output: 10
Change Program.**
Related Commands:
#CastInt, #CastLit
**
#Change
**
**#Change ("** *program.PRG* **")**
This command changes the program filename of the program currently running. Execution of the current program continues, but when the player touches the program tile again, the new program that was set with will be run instead of the original program. **#Change**
This change remains in effect only during the time that the player is on the board. If the player leaves the board and then returns, the program tile will be reset to its original program.
If The .Prg extentsion is not included, it is added automatically. Also, you shouldn’t include directory information, since the Toolkit will find that for you.
This command may be useful if the player must talk to a certain person on the board more than once during the course of the board. By using , you can change what the person says each time by changing his/her program. **#Change**
**
Example:
* An example of the #Change command.
#MWin("Hello, there. I am happy.")
#Change ("another.PRG")
#MWin("I am still running the original program!!!")
* The initial program continues running
* until its end, and then the next time the player
* touches this program tile, the file "another.PRG"
* will be run instead of this program file.
Adjust character walk speed.**
Related Commands:
#Gone, #Move, #Prg, #Run
#CharacterSpeed
**
#CharacterSpeed(speed!)
This command adjusts the speed at which characters and items move in your game. Speed! Is a numerical value and is a number between 0 and 3. 3 is the fastest speed and is the default.
**
Example:
#CharacterSpeed(0)
Get character from string..**
Related Commands:
#BattleSpeed, #TextSpeed
#CharAt
**
#CharAt("text", position!, dest$)
This command allows you to splice apart a string (literal value) by getting specific characters within it.
"text" is a literal value and it’s the string that this command examines. position! is a numerical value which specifies which position in the text you want (for example, 3 returns character three, which is ‘x’). dest$ is the destination variable to which the character will be placed.
**
Example:
* This makes use of a method which prints text vertically.
#PrintVertical ("Vert. Text!") *Calls method ‘PrintVertical’
#End()
#Method PrintVertical(pv_text$)
#pv_done!=0
#pv_pos=1
#While(pv_done!==0)
#CharAt(pv_text$, pv_pos!, pv_part$)
#If (pv_part$=="")
*Reached the end of the string.
#pv_done!=1
*Breaks out of while loop.
#If (pv_part$~="")
#Print(pv_part$) *Output this character
#pv_pos=pv_pos+1
*Increment the character position.
Check if a button was pressed.**
Related Commands:
#CastInt, #CastLit, #CastNum, #Prompt, #Wait
#CheckButton
**
#CheckButton(x!,y!,buttonNum!)
This command checks if a button set with the #SetButton command was clicked or not. X! and y! are the x and y coordinates of the last mouse click of the screen. You can get these numbers with the #MouseClick command. buttonNum! Is the value that this command returns. If no buttons were pressed, then buttonNum! Is set equal to –1, otherwise, it is set equal to the number of the button that was pressed (as defined by #SetButton).
**
Example:
*Button…
#SetButton("b1.jpg",0,10,10,100,100)
*create a button in slot 0
#done!=0
#While(done!==)
#MouseClick(x!,y!)
#CheckButton(x!,y!,num!) *check if a button was pressed
#if (num!==0)
*button 0 was pressed!
#Mwin("you pressed the button!")
#Wait(a$)
#done!=1
#ClearButtons()
Clear Screen.**
Related Commands:
#ClearButtons, #MouseClick, #SetButton
**
#Clear
**
**#Clear()** can be used to clear the screen to prepare it for large menus, or to prepare it for story sequences in the game when other boards are temporarily placed on the screen in place of the current one.
The command clears the entire screen, making it entirely black. When the program ends, the screen is restored to the way it was before the program began (unless using the command to end the program). **#Clear** **#Done**
**
#Clear
**
Example:
* Clear the screen and place a new board there.
#Clear()
* The screen is now black.
#ViewBrd ("another.BRD")
* Place another board on the screen.
Clear keyboard buffer.**
Related Commands:
#Color, #Fade, #Mem, #Put, #Return, #Scan, #Text, #Viewbrd
**
#ClearBuffer
**
#ClearBuffer()
This command clears the keyboard buffer. Sometimes the internal keyboard buffer gets full and continues to ‘type’ even after the player has finished pressing any buttons. This command wipes the buffer clean to prevent this.
**
Example:
#ClearBuffer()
#Mwin("hello")
#Wait(a$)
Clear buttons from memory.**
Related Commands:
#Get, #Wait
#ClearButtons
**
#ClearButtons()
This command clears all the buttons from memory that were defined with the #SetButton command.
**
Example:
*Button…
#SetButton("b1.jpg",0,10,10,100,100)
*create a button in slot 0
#done!=0
#While(done!==)
#MouseClick(x!,y!)
#CheckButton(x!,y!,num!) *check if a button was pressed
#if (num!==0)
*button 0 was pressed!
#Mwin("you pressed the button!")
#Wait(a$)
#done!=1
#ClearButtons()
Change Color.**
Related Commands:
#CheckButton, #MouseClick, #SetButton
#Color
**
**#Color (** *color code* **)** also changes the color of the color sweep that goes across the screen before a battle.
The command changes the color of the text that will be displayed in the Message Window, as well as the color of the fadeout with the command, and the text that is placed on the screen with the command. **#Color** **#Fade** **#Text**
**
#Color
The is a number used to represent the color you wish to use. This is a number from 0 to 255 representing a color value from the standard Mode 13h DOS Palette. This is more for compatibility with version 1 than anything else. A better choice is #ColorRGB which allows you to define a color based upon its RGB value. *color code*
**
Example:
* Example using the #Color command.
#Color (15)
#MWin("Color code 15. (White)")
#a!=4
#Color (a!)
* Sets the color to 4 (which is the value stored in
* a!). Code 4 is red.
#Mwin("Color code 4. (Red)")
#Wait(a$)
* Wait for the player to press a key.
#Color (15)
* Reset color to 15 (white).
Define RGB Color.**
Related Commands:
#ColorRGB, #Fade, #Text
#ColorRGB
**
**#ColorRGB (red!, green!, blue!)**
This command changes the color of the text that will be displayed in the Message Window, as well as the color of the fadeout with the command, and the text that is placed on the screen with the command. **#Fade** **#Text**
It also changes the color of the color sweep that goes across the screen before a battle.
red!, green! and blue! are numerical values in the range of 0 to 255 which specify the concentrations of red, green and blue pigment in the color. (for example, 0,0,0 is black; 255,255,255 is white; 255,0,0 is bright red, etc)
**
Example:
* Example using the #ColorRGB command.
#ColorRGB (255,255,255)
#MWin("White!")
#ColorRGB (255,0,0)
* Sets the color to bright red.
#Mwin("Bright red!")
#Wait(a$)
* Wait for the player to press a key.
#ColorRGB (255,255,255)
* Reset color to white.
Loads an item into memory.**
Related Commands:
#Color, #Fade, #Text
#CreateItem
**
#CreateItem("filename.itm",itemnum!)
This command loads an item into memory. The filename is a literal value that is the item’s filename. Itemnum! Is a varibale which receives the number of the item loaded into memory (ie, when the item is loaded into memory, it is given a ‘slot’ in memory. This variable saves the number of that slot for later use). This command is very useful, in conjunction with other item commands, to create story sequences.
**
Example:
*Item animation…
#CreateItem("soldier.itm",pos!) *load an item into a slot
#PutItem(pos!,1,1,1) *put the item at 1,1, layer 1
#PushItem(pos!,"E") *move the item
#PushItem(pos!,"E") *move the item
#PushItem(pos!,"E") *move the item
#PushItem(pos!,"E") *move the item
#Mwin("hello!")
#Wait(a$)
#EraseItem(pos!) *remove item from screen
#DestroyItem(pos!) *remove item from memory.
Turn debugger on/off.**
Related Commands:
#DestroyItem, #EraseItem, #PutItem
#Debug
**
#Debug ("on/off")
This command will allow you to turn the internal debugger on or off. When an RPGCode program is running and there is an error in it, the debugger window will popup and tell you what the error is and where it is. You can turn this on or off using this command.
The parameters for this command is simply a literal value that contains the text "on" or "off".
**
Example:
* Turn the debugger on and off.
#Debug("on")
#la la la la() *This will cause an error message in the
*debug window.
#Debug("off")
#another error() *This will also cause an error, but you won’t
*see a message in the Debug window.
Delay for a number of seconds.**
Related Commands:
#RPGCode
#Delay
**
#Delay (seconds!)
This command causes the computer to pause for a specified number of seconds. seconds! is a numeric value that specifies the number of seconds to wait.
**
Example:
#MWin("Before delay...")
#Delay(4) *Wait for 4 seconds.
#MWin("After delay.")
#Wait(a$)
Remove item from memory.**
Related Commands:
#Wait
#DestroyItem
**
#DestroyItem(itemnum!)
This command removes an item from memory, thus freeing its memory slot for other items to be loaded. Itemnum! Is the number (from 0 to 10) of the item, as defined on the board editor, or with the #CreateItem command.
**
Example:
*Item animation…
#CreateItem("soldier.itm",pos!) *load an item into a slot
#PutItem(pos!,1,1,1) *put the item at 1,1, layer 1
#PushItem(pos!,"E") *move the item
#PushItem(pos!,"E") *move the item
#PushItem(pos!,"E") *move the item
#PushItem(pos!,"E") *move the item
#Mwin("hello!")
#Wait(a$)
#EraseItem(pos!) *remove item from screen
#DestroyItem(pos!) *remove item from memory.
Remove a player from the party. Does not store old values.**
Related Commands:
#CreateItem, #EraseItem, #PutItem
#DestroyPlayer
**
#DestroyPlayer("handle")
This command removes a player from the party, but unlike #RemovePlayer, this command destroys all player stats so the player cannot be resotred with the #RestorePlayer or #CallPlayerSwap commands. "handle" is the handle of the player to remove, or the player’s filename.
**
Example:
#AddPlayer("frap.tem")
#DestroyPlayer("Frap")
Directory of saved games.**
Related Commands:
#AddPlayer, #RemovePlayer
#DirSav
**
**#DirSav(dest$) or #DirSav()**
#Dirsav opens a standart file dialog window showing a listing of all the saved games (*.SAV) in the \Saved\ directory. These saved games are made by a player who has been playing a game and who has saved his progress with the command. **#Save**
If you include a literal variable in the parameter list, the filename of the selected file will be stored in that variable. If you do not pass any parameters to this command, the user will see the Save dialog window, will be able to select files, but the filename s/he selects will not be stored anywhere.
It returns CANCEL if the user cancelled the dialog.
**
Example:
* Program to load a saved game.
#DirSav(filename$) *Show saved games and store selected filename
*in filename$.
#If (filename$~="") { #Load(filename$) }
*If a file was selected, then load that filename!
Done program.**
Related Commands:
#Load, #Save, #Prompt
#Done
**
#Done()
The command ends execution of a program, but does not restore the screen to the way it was before the program began. If there is any text in the Message Window, it stays there. If you have put any graphics on the board, they stay there. The changes to the board remain in effect only for the time the player is on the board. If the player leaves and then returns to the board, it will be restored to normal. **#Done**
**
Example:
* Program demonstrating the #Done command.
* First, let's put some graphics on the board.
#Put (5,5,"graphic1.GPH")
#Put (8,8,"graphic2.GPH")
* Usually, at the end of a program these graphics
* would be erased and the board would return to
* normal, but by using the #Done command, we can
* force these graphics to stay.
#Done()
Return to Operating System (Windows).**
Related Commands:
#Clear, #Mem, #Prg, #Put, #Return, #Scan, #Text, #Viewbrd
#Dos
**
#Dos()
This command quits the Translator program and returns to Windows. This is included for compatibility with version 1. Instead you should use the #Windows command to quit to Windows, just to make your code more readable.
**
Example:
* Quit to Windows program.
#MWin("Press any key to quit to Windows...")
#Wait(a$)
* Wait for the user to press a key
#Dos()
Attack all enemies/players.**
Related Commands:
#Reset, #Windows
#DrainAll
**
#DrainAll(smp!)
This command removes smp from all enemies or players in battle. When used with a special move, this will damage the group of enemies or players depending upon which group was targeted by the player. smp! Is a literal value specifying the amount of smp to drain.
**
Example:
#DrainAll(100)
Draw a line.**
Related Commands:
#AttackAll
#DrawLine
**
#DrawLine (x1!, y1!, x2!, y2!)
This command draws a line on the screen from coordinate (x1!, y1!) to (x2!, y2!). All of these values are numerical.
The color of the line is determined by the currently defined color selected by the or commands. **#Color** **#ColorRGB**
**
Example:
* Draw a bunch of lines extending from the origin.
#For (x!=0; x!<=80; x!=x!+5)
#For (y!=0; y!<=80; y!=y!+5)
#ColorRGB(x!,x!,x!)
#drawLine(0,0,x!,y!)
Draw a rectangle.**
Related Commands:
#setPixel, #drawRect, #fillRect
#DrawRect
**
#DrawRect (x1!, y1!, x2!, y2!)
This command draws a rectangle on the screen with corners at coordinates (x1!, y1!) and (x2!, y2!). All of these values are numerical.
The color of the rectangle is determined by the currently defined color selected by the or commands. **#Color** **#ColorRGB**
**
Example:
* Draw a bunch of random rectangles.
#For (count!=0; count!<=15; count!=count!+1)
#Random(255,color!)
#Color(color!)
#Random(608,x1!)
#Random(352,y1!)
#Random(608,x2!)
#Random(352,y2!)
#DrawRect(x1!,y!,x2!,y2!)
Cause an earthquake.**
Related Commands:
#setPixel, #drawLine, #fillRect
#Earthquake
**
#Earthquake(intensity!)
This command causes the earth to shake. Intensity! Is a numerical value that defines the strength and duration of the ‘quake.
**
Example:
#Earhquake(10)
Empty all variables.**
Related Commands:
#Zoom
#Empty
**
#Empty()
This command clears all variables, numeric and literal. Use this command wisely, otherwise all the variables in your game will be cleared.
**
Example:
* Clear all variables.
#test!=12
#MWin("Variable test! before Empty: ")
* Shows contents of test! (which is 12)
#Empty()
* Clears all variables.
#MWin("Variable test! after Empty: ")
* Shows contents of test! (now 0).
End program.**
Related Commands:
#Dos, #Reset, #Windows
#End
**
#End()
This command ends execution of a program, restoring the screen to the way it was before the program began. Also used to denote the end of a function block (used with although this has become archaic with the introduction of the new #Method command). **#Fbranch,**
With proper use of #While and #For loops, this command is not needed.
**
Example:
* Program demonstrating #End
#done!=0
*Continue to do this until the variable done! doesn’t equal zero.
#While (done!==0)
#MWinCls() *Clear message window
#MWin("Press:")
#MWin(" 1- To see message")
#MWin(" 2- To end")
#Wait(key$)
* Wait for a key press
#If (key$=="1")
#MWin("Hello!!! This is a message!")
#Wait(a$) *Wait for user to press key again
*After the user presses a key, the program will go back
*to the top of the While loop, thus showing the menu
*again.
#If (key$=="2")
#End()
*This will end the program. However, I could also
*have set done! equal to some number like 1.
*That would have broken me out of the While loop, thus
*ending the program.
Equip item.**
Related Commands:
#Done, #Dos, #Fbranch, #Over, #Win
**
#Equip
**
#Equip(handle$, body_location!, item_filename$)
This command eqips an item on a player. The player must have the item in the inventory and the item must also be equipable on the player.
handle$ is a literal value that specifies the handle of the player to equip to. "Target" specifies the currently selected player.
body_location! is a numerical value between 1 and 16. It specifies the boady location to equip to. Valid positions are:
1- Head
2- Neck accessory
3- Left Hand
4- Right Hand
5- Body
6- Legs
7-16 Accessories 1-10
item_filename$ is a literal value that specifies the filename or handle of the item to equip.
**
Example:
*Equip a sword on Frap’s right hand.
#GiveItem("sword.itm") * Give a sword.
#Equip("Frap",4,"sword.itm")
Remove item graphic.**
Related Commands:
#GiveItem, #Remove
#EraseItem
**
#EraseItem(itemnum!)
This command removes an item from the screen. The item is still in memory, but is not shown on the screen. Itemnum! Is the number (from 0 to 10) of the item, as defined on the board editor, or with the #CreateItem command.
**
Example:
*Item animation…
#CreateItem("soldier.itm",pos!) *load an item into a slot
#PutItem(pos!,1,1,1) *put the item at 1,1, layer 1
#PushItem(pos!,"E") *move the item
#PushItem(pos!,"E") *move the item
#PushItem(pos!,"E") *move the item
#PushItem(pos!,"E") *move the item
#Mwin("hello!")
#Wait(a$)
#EraseItem(pos!) *remove item from screen
#DestroyItem(pos!) *remove item from memory.
Erase Player graphic.**
Related Commands:
#CreateItem, #DestroyItem, #PutItem
#ErasePlayer
**
#ErasePlayer(handle$)
This command erases a player on your team from the board. You can use this to remove the main character, but this command is really for the teammates in the party. *other*
handle$ is a literal value that specifies which character you are referring to.
**
Example:
* Short story sequence in which Frap and Tano interact.
* Frap is the main character and so is already on the board.
* Let’s say Frap is at 5,5. We’ll have Tano "emerge" from
* this location as if he is popping out of the party.
#PutPlayer("Tano",5,5,1)
#Push("E","Tano")
#Push("E","Tano")
#Push("W","Tano")
#MWinCls()
#Mwin("Tano: Well, here we are in some odd")
#Mwin(" RPGCode story sequence.")
#Wait (a$)
#MWinCls()
#MWin("Frap: Watch this!")
#Wait (a$)
#MWinCls
#Push("N","Frap")
#Push("E","Frap")
#Push("E","Frap")
#Push("S","Frap")
#MWin("Tano: Wow, that’s really great. You can")
#Mwin(" walk. Now I’m going to walk towards")
#Mwin(" you and vanish into your chest somehow.")
#Wait(a$)
#MWin("Frap: Cool.")
#Wait(a$)
#MWinCls()
#Push("E","Tano")
#ErasePlayer("Tano")
Fade out.**
Related Commands:
#PutPlayer, #Push
#Fade
**
#Fade(fade_type!) or #Fade()
#Fade is used to "fade out" the screen. Actually, the screen is blotted out by a growing and shrinking box. The color of the fadeout is determined by the or commands. **#Color** **#ColorRGB**
You can fade out the screen in more than one way. This is determined by passing it a numerical parameter with a value between 0 and 3. If you pass no parameters, the fade type is assumed to be zero.
The different fade types are as follows:
0- Version 1 fading type. A growing and shrinking box blots ot the screen.
1- Better fading type that blots out the screen with vertical lines.
2- "True Fade"; Fades the screen from white to black.
3- A fading line sweeps across the screen.
4- A black circle swoops down and swallows the player.
Once the screen has faded out completely, the screen is completely clear, similar to the way it is using the command. Use to restore the screen to the way it was. **#Clear** **#Return**
The screen will be restored to the way it was at the end of the program (except when the command is used). **#Done**
**
Example:
* Fade out the screen using a blue fadeout.
#ColorRGB (0,0,255)
* Sets the color of the fadeout to bright blue.
#Fade(1)
* Fades the screen using vertical bars.
#ColorRGB (255,255,255)
* Rests color to white.
Function Branch.**
Related Commands:
#Clear, #Color, #Return
**
#FBranch
**
#Fbranch( *:label name* **)**
This command is used in the same manner as the command to skip to other parts of the program. The section to which branches to is defined by the name of the label in parentheses. A corresponding label name must exist somewhere in the program (see command for more information on labels). **#Branch** **#Fbranch** **#Branch**
The sections of program that branches to are called . By using the command, the program can jump to one of these functions and carry out the commands in the function. Once the program encounters the command or the end of the program inside the function, then the program branches back up to , carrying out the lines of code after it. **#Fbranch** *functions* **#Fbranch** **#End** **#Fbranch**
Since the command inside a function will not end the program, you have to use the command to end the program from within the function. In order to mimic what does, however, you must include the command before the command (This restores the screen to the way it looked before the program and then ends the program). See for more info on branching. **#End** **#Done** **#End** **#Return** **#Done** **#Branch**
This is an outdated way of doing things. I reccomend using the command instead to write your own methods instead of using the old fashioned #Franch functions. Not only will you find #Method easier to understand, but it will make yor code more readable. *highly* **#Method**
**
Example:
* Example using #Fbranch.
#MWin("This is the Main part of the program.")
#Wait(a$) *Wait for a keypress.
#Fbranch (:function 1)
* This command goes to the function called
* :function 1, carries out the instructions in
* :function 1, and then returns here automatically.
#MWin("We're back to Main!")
#Fbranch (:end of program)
* This function branch will demonstrate ending the
* program from within a function. A more efficient
* way of doing things would be to have used the #End()
* command here to end the program.
* H E R E A R E T H E F U N C T I O N S:
:function 1
#MWin("Now we are inside function 1.")
#Wait(a$)
#End()
* Jumps back to the position from where
* #Fbranch (:function 1) was used.
:end of program
* This function demonstrates ending a program from
* within a function.
#Return()
* Restores the screen to the way it was before the
* program began.
#Done()
* Ends the program.
Fight Command.**
Related Commands:
#Branch, #Done, #End, #Method, #Reset
**
#Fight
**
#Fight(skill!, "background.bkg")
The command is used to initiate a fight from within a program. Using this command ends execution of the program. **#Fight**
The is the skill level of the enemy to fight. This skill level was determined in the Main Fight File. Once the battle is initiated, the computer randomly selects an enemy to fight of that skill level. The second argument in this command, is a literal parameter which is the background against which the battle will take place. This is the filename of the background file on which to fight. If not extension is supplied, the Toolkit adds one for you. Also, do not include any directory information in the filename- the Toolkit will find that for you. *skill!* *background.BKG*
This command is useful in initiating fights with "bosses" in the game, either by stepping on a tile that leads to the boss's chamber, or by creating a character on the screen that you talk to and then fight. In order to fight one specific enemy, there must be only one enemy of a certain skill level. For example, if you wished your player to fight an enemy called Enemy.ENE, this particular enemy would have to have its very own skill level. Let's say Enemy.ENE has a skill level of 28. In order for this enemy to be fought, he must be the only one with skill 28. This is because when the computer randomly selects an enemy to fight out of all the enemies with a skill of 28, this is the one it will choose every time since it is the only one with a skill level of 28.
**
Example:
* Example using #Fight
* We will use a variable to substitute the
* Background filename.
#bkg$="bground.BKG"
#MWin("Press any key to begin the fight...")
#Wait(a$)
* Wait for user to press a key.
* Now we'll start a fight with someone of skill 49:
#Fight (49,bkg$)
* Starts a fight with an enemy of skill 49, against
* a background called Bground.BKG (the contents of
* bkg$). This command also ends the program.
Fight enemy group.**
Related Commands:
#Color, #FightEnemy
#FightEnemy
**
#FightEnemy("enemy1.ene","background.bkg")
This command changes begins a fight. The first argument is the filename of an enemy to fight. You may have up to four enemy filenames if you wish as four separate arguments. The last value is a filename of the background to fight against. This command ends execution of the program.
**
Example:
#FightEnemy("badguy.ene", "mole.ene", "mybkg.bkg")
* Calls a fight with two enemies.
Change Fight Window graphic.**
Related Commands:
#Fight
#FightMenuGraphic
**
#FightMenuGraphic(filename$)
By default, the Fight Window has a black background. You can put a graphic in the background by using this command. filename$ is a literal value which specifies the filename of the graphic to place in the Fight Window (Bmp, Gif or Jpg).
**
Example:
#FightMenuGraphic("fight.jpg")
Change fighting mode.**
Related Commands:
#Bold, #Color, #ColorRGB, #Font, #FontSize, #Italics, #Mwin, #MWinCls, #Underline, #WinColor, #WinColorRGB
#FightStyle
**
#FightStyle(style!)
This command switches the fighting style between side view and frontal view. If style! Is 0, it is side view. If it is 1, it is front view.
**
Example:
#FightStyle(1) *Switch to front view
Draw a filled rectangle.**
Related Commands:
#Fight, #FightEnemy
#FillRect
**
#FillRect (x1!, y1!, x2!, y2!)
This command draws a filled rectangle on the screen with corners at coordinates (x1!, y1!) and (x2!, y2!). All of these values are numerical.
The color of the rectangle is determined by the currently defined color selected by the or commands. **#Color** **#ColorRGB**
**
Example:
* Draw a bunch of random filled rectangles.
#For (count!=0; count!<=15; count!=count!+1)
#Random(255,color!)
#Color(color!)
#Random(608,x1!)
#Random(352,y1!)
#Random(608,x2!)
#Random(352,y2!)
#FillRect(x1!,y!,x2!,y2!)
Change font.**
Related Commands:
#setPixel, #drawLine, #drawRect
#Font
**
#Font(filename$)
This loads a new font that was created with the Font Editor and uses it as the font in the Message Window and in commands. filename$ is the filename of the font. **#Text**
**
Example:
#MWin("The old font...")
#Font("new.fnt")
#MWin("The new font!!!")
#Wait(a$)
Change font size.**
Related Commands:
#Bold, #Color, #ColorRGB, #FontSize, #Italics, #Mwin, #MWinCls, #Underline, #WinGraphic, #WinColorRGB
#FontSize
**
#FontSize(size!)
This command allows you to change the size of the currently selected font. size! is a numerical vlue that represents the size of the font in pixels. By default, this size is 16 (for compatibility with version 1). 16 is kind of big, so you may want to use a size of 12 or even 8.
**
Example:
#FontSize(8)
#MWin("Small Font.")
#FontSize(16)
#MWin("Big Font.")
#Wait(a$)
For-loop.**
Related Commands:
#Bold, #Color, #ColorRGB, #Font, #Italics, #Mwin, #MWinCls, #Underline, #WinGraphic, #WinColorRGB
#For
**
The For command allows you to initiate a For-loop. For-loops in RPGCode work very similar to those in C or C++.
A For-loop is a number of commands that are executed over and over again for a set number of cycles. This is much more convenient than writing 100 repetitive commands when you can use one For-loop.
Within the parameters of the For-loop are 3 statements that are separated by semicolons(;). is the command that sets the counter variable. For example, let’s say we were making a For-loop that ran 5 times. A logical way to do this is have it count from 1 to 5. So the statement may set some varibale equal to 1- the starting value (ie. count!=1). *initial* *initial*
The next statement- is a condition that the For-loop tests before each loop to see if it should keep running (this is very similar to an If statement). For example, if our loop was going to run for 5 cycles, and count! was the variable we were using to count, then a good condidion would be: count!<=5. In other words, the For-loop will keep running until count! is greater than the number 5. *condition*
The last statement- allows you to increment the counter variable between each cycle. Since we’re going from 1 to 5 in our example, we can use: count!=count!+1, which just adds 1 to the counter variable each cycle. The following example will show a For loop alongside a #Branch loop to show you how much better the For loop is. *increment*
Following the For-Loop, you must enclose the statements you wish to run between { and } brackets. They must appear on lines by themselves.
As a final note, you should not run For loops inside multitask programs (items). It takes up too much computing time and might get caught in an infinite loop.
**
Example:
*For-loop example. Before running the For-Loop, check out
*This using #Branch commands:
#Counter!=1
:top
#Show(Counter!)
#Counter!=Counter!+1
#If(Counter!<=5)
#Branch(:top)
*Will run 5 times.
*OK, so that was using a #Branching loop. Look at how much
*better that is using the For-Loop:
#For(Counter!=1; Counter!<=5; Counter!=Counter!+1)
#Show(Counter!)
*Much better, wouldn’t you agree?
Get value in keyboard buffer.**
Related Commands:
#Branch, #While
#Get
**
#Get(destination$)
This command gets the current value in the keyboard buffer and places it in the literal variable destination$. The keyboard buffer tells you what button is currently being pressed on the keyboard. If no button is being pressed, the value given to destination$ is "" (nothing).
**
Example:
#While(a$=="")
#Get(a$)
#Mwin(a$)
#Wait(b$)
*The above loop does the same thing as the #Wait command.
Return x and y offset of the board.**
Related Commands:
#Wait
#GetCorner
**
#GetCorner(topx!,topy!)
This command tells you what the top corner of the board is currently scrolled to. On a non-scrolling board, this is always 0,0. This command is useful when trying to determine where the board is currently scrolled to. Topx! And topy! are numerical variables that receive the top x and y coordinates of the board. Please note: these coordinates are actually an . This means that when x=0 and y=0, the actual top corner tile is 1,1 (1 more than the offset). *offset*
**
Example:
#GetCorner(x!,y!)
#x!=x!+1
#y!=y!+1
#Mwin("The top x and y coord is: ,")
Get player DP.**
Related Commands:
#Send
#GetDP
**
#GetDP(handle$, dest!)
This command will get the current DP level of a selected player or enemy and place it in a numerical variable. handle$ is a literal value which is the handle of the character to edit. If you use the keyword "Target" as the handle, the player that will be changed is the character that is currently being selected from the internal menu, the fight screen, or even a selected enemy on the fight screen.
dest! is the name of a numerical variable to which the DP level will be placed.
**
Example:
*Getting DP to characters/enemies.
#GetDP("Frap",frapDP!) *Puts Frap’s DP level into variable
*frapDP!
#MWin("Frap’s DP level is: ")
#GetDP("Target",targDP!) *Get the target’s DP (the target
*may be a selected player or enemy.
#MWin("The selected target’s DP is: ")
Get player FP.**
Related Commands:
#GiveHP, #GetHP, #MaxHP, #GetMaxHP, #SMP, #GiveSMP, #GetSMP, #MaxSMP, #GetMaxSMP
#GetFP
**
#GetFP(handle$, dest!)
This command will get the current FP level of a selected player or enemy and place it in a numerical variable. handle$ is a literal value which is the handle of the character to edit. If you use the keyword "Target" as the handle, the player that will be changed is the character that is currently being selected from the internal menu, the fight screen, or even a selected enemy on the fight screen.
dest! is the name of a numerical variable to which the FP level will be placed.
**
Example:
*Getting FP to characters/enemies.
#GetFP("Frap",frapFP!) *Puts Frap’s FP level into variable
*frapFP!
#MWin("Frap’s FP level is: ")
#GetFP("Target",targFP!) *Get the target’s FP (the target
*may be a selected player or enemy.
#MWin("The selected target’s FP is: ")
Get GP level.**
Related Commands:
#GiveHP, #GetHP, #MaxHP, #GetMaxHP, #SMP, #GiveSMP, #GetSMP, #MaxSMP, #GetMaxSMP
#GetGP
**
#GetGP(dest!)
This command puts the current GP level in dest!.
**
Example:
#GetGP(gplev!)
#MWin("You had: GP")
#GiveGP(100)
#GetGP(gplev!)
#MWin("Now you have: GP")
#TakeGP(100)
#GetGP(gplev!)
#MWin("And now you have: GP")
Get player HP level.**
Related Commands:
#GiveGP, #TakeGP
#GetHP
**
#GetHP(handle$, dest!)
This command will get the current HP level of a selected player or enemy and place it in a numerical variable. handle$ is a literal value which is the handle of the character to edit. If you use the keyword "Target" as the handle, the player that will be changed is the character that is currently being selected from the internal menu, the fight screen, or even a selected enemy on the fight screen.
dest! is the name of a numerical variable to which the HP level will be placed.
**
Example:
*Getting HP to characters/enemies.
#GetHP("Frap",frapHP!) *Puts Frap’s HP level into variable
*frapHP!
#MWin("Frap’s HP level is: ")
#GetHP("Target",targHP!) *Get the target’s HP (the target
*may be a selected player or enemy.
#MWin("The selected target’s HP is: ")
Get player Special Move Power level.**
Related Commands:
#GiveHP, #GetHP, #MaxHP, #GetMaxHP, #SMP, #GiveSMP, #GetSMP, #MaxSMP, #GetMaxSMP
#GetSMP
**
#GetSMP(handle$, dest!)
This command will get the current SMP level of a selected player or enemy and place it in a numerical variable. handle$ is a literal value which is the handle of the character to edit. If you use the keyword "Target" as the handle, the player that will be changed is the character that is currently being selected from the internal menu, the fight screen, or even a selected enemy on the fight screen.
dest! is the name of a numerical variable to which the SMP level will be placed.
**
Example:
*Getting SMP to characters/enemies.
#GetHP("Frap",frapSMP!) *Puts Frap’s SMP level into variable
*frapSMP!
#MWin("Frap’s SMP level is: ")
#GetHP("Target",targSMP!) *Get the target’s SMP (the target
*may be a selected player or enemy.
#MWin("The selected target’s SMP is: ")
Get player level.**
Related Commands:
#GiveHP, #GetHP, #MaxHP, #GetMaxHP, #SMP, #GiveSMP, #GetSMP, #MaxSMP, #GetMaxSMP
#GetLevel
**
#GetLevel(handle$, dest!)
This command will get the level of a selected player and place it in a numerical variable. handle$ is a literal value which is the handle of the character to edit. If you use the keyword "Target" as the handle, the player that will be changed is the character that is currently being selected from the internal menu, the fight screen, or even a selected enemy on the fight screen.
dest! is the name of a numerical variable to which the SMP level will be placed.
**
Example:
*Getting level of character.
#GetLevel("Frap",dest!) *Puts Frap’s level into variable
#MWin("Frap’s level is: ")
Get Maximum player HP level.**
Related Commands:
#GiveHP, #GetHP, #MaxHP, #GetMaxHP, #SMP, #GiveSMP, #GetSMP, #MaxSMP, #GetMaxSMP
#GetMaxHP
**
#GetMaxHP(handle$, dest!)
This command works identically to , ecept that it gets the character’s HP level (the maximum the character can have). See for more info. **#GetHP** *maximum* **#GetHP**
**
Example:
*Getting the Max HP.
#GetMaxHP("Frap",frapMax!) *Gets Frap’s max HP level.
#GetHP("Frap",frapHP!) *Gets Frap’s HP level.
#MWin("Frap’s current health: /")
#GetMaxHP("Target",targetMax!") *Gets the target’s max HP
*level.
#GetHP("Target",targetHP!) *Gets target’s HP level.
#MWin("Current health of target: /")
Get Maximum player SMP level.**
Related Commands:
#GiveHP, #GetHP, #MaxHP, #GetMaxHP, #SMP, #GiveSMP, #GetSMP, #MaxSMP, #GetMaxSMP
#GetMaxSMP
**
#GetMaxSMP(handle$, dest!)
This command works identically to , except that it gets the character’s SMP level (the maximum the character can have). See for more info. **#GetSMP** *maximum* **#GetSMP**
**
Example:
*Getting the Max SMP.
#GetMaxSMP("Frap",frapMax!) *Gets Frap’s max SMP level.
#GetSMP("Frap",frapSMP!) *Gets Frap’s SMP level.
#MWin("Frap’s current SMP: /")
Give Gold to player.**
Related Commands:
#GiveHP, #GetHP, #MaxHP, #GetMaxHP, #SMP, #GiveSMP, #GetSMP, #MaxSMP, #GetMaxSMP
#GiveGP
**
#GiveGP(amount!)
This command gives GP to the player.
**
Example:
#GetGP(gplev!)
#MWin("You had: GP")
#GiveGP(100)
#GetGP(gplev!)
#MWin("Now you have: GP")
#TakeGP(100)
#GetGP(gplev!)
#MWin("And now you have: GP")
Give Player HP.**
Related Commands:
#GetGP, #TakeGP
#GiveHP
**
#GiveHP(handle$, HP_to_add!)
This command will give HP to any player on your team or a selected enemy in a fight. handle$ is a literal value which is the handle of the character to edit. If you use the keyword "Target" as the handle, the player that will be changed is the character that is currently being selected from the internal menu, the fight screen, or even a selected enemy on the fight screen.
HP_to_add! is a numerical value which specifies the amount of HP to give to a player/enemy.
**
Example:
*Giving HP to characters/enemies.
#HP("Frap",100) *Sets Frap’s HP level to 100.
#GiveHP("Frap",20) *Frap’s HP level is now 120
#GiveHP("Target",-80) * 80 HP from the Target. *Takes*
Give player item.**
Related Commands:
#GiveHP, #GetHP, #MaxHP, #GetMaxHP, #SMP, #GiveSMP, #GetSMP, #MaxSMP, #GetMaxSMP
#GiveItem
**
#GiveItem(item_filename$)
This command adds an item to the player’s inventory. item_filename$ is the filename of the item to add, and is a literal value. Don’t include any directory info as RPGCode will determine that for you.
**
Example:
*Give the player a sword:
#GiveItem("sword.itm")
#MWin("You got a sword!!!")
#Wait(a$)
Give Player Special Move Power.**
Related Commands:
#Equip, #Remove, #TakeItem
#GiveSMP
**
#GiveSMP(handle$, SMP_to_add!)
This command will give SMP (Special Move Power) to any player on your team or a selected enemy in a fight. handle$ is a literal value which is the handle of the character to edit. If you use the keyword "Target" as the handle, the player that will be changed is the character that is currently being selected from the internal menu, the fight screen, or even a selected enemy on the fight screen.
SMP_to_add! is a numerical value which specifies the amount of SMP to give to a player/enemy.
**
Example:
*Giving SMP to characters/enemies.
#SMP("Frap",100) *Sets Frap’s SMP level to 100.
#GiveSMP("Frap",20) *Frap’s SMP level is now 120
#GiveSMP("Target",-80) * 80 SMP from the Target. *Takes*
Perform DOS command.**
Related Commands:
#GiveHP, #GetHP, #MaxHP, #GetMaxHP, #SMP, #GiveSMP, #GetSMP, #MaxSMP, #GetMaxSMP
#GoDos
**
#GoDos(command$) Gone command.
This command has been removed due to the new security restrictions in version 2.05. To run files, try using the #Start command.
**
#Gone
**
#Gone()
This command ends execution of the current program and removes it from the board (but not its associated graphic). From then on, whenever the player steps on the tile where the program used to be, nothing will happen.
This change is only in effect during the time the player is on this board.
**
Example:
* Example of the #Gone command.
#MWin("Farewell, cruel world!!!")
* Now wait for a key press:
#Wait(a$)
* Now to erase this program:
#Gone()
Set player HP level.**
Related Commands:
#Change, #Move, #Prg
**
#HP
**
#HP(handle$, new_HP!)
This command will set the HP level of any player on your team or a selected enemy in a fight. handle$ is a literal value which is the handle of the character to edit. If you use the keyword "Target" as the handle, the player that will be changed is the character that is currently being selected from the internal menu, the fight screen, or even a selected enemy on the fight screen.
new_HP! is a numerical value which specifies what the new HP level of the character/enemy is.
**
Example:
*Giving HP to characters/enemies.
#HP("Frap",100) *Sets Frap’s HP level to 100.
#HP("Tano",200) *Sets Tano’s HP level to 200.
#HP("Target",150) *Sets the target’s HP level to 150 (may be an
*enemy or a player, depending upon who is
*currently selected).
If... condition testing command.**
Related Commands:
#GiveHP, #GetHP, #MaxHP, #GetMaxHP, #SMP, #GiveSMP, #GetSMP, #MaxSMP, #GetMaxSMP
**
#If...
**
#If ( *condition* **) {** *code to run* **}** can test for six different conditions: equal to (==), greater than (>), less than (<), not equal to (~=), greater than or equal to (>=), and less than or equal to (<=). Here are the formats for each:
#If... is a special command that tests if a variable contains a certain value or not. If it does, then a block of commands is executed.
The is some condition that you are testing. It tests if two values are equal to/not equal to/greater than or less han each other. If they are, then the commands within the enclosed block are run. *condition*
**
#If...
#If ( == ) *val1* *val2*
*
commands to run
#If ( > ) *val1* *val2*
*
commands to run
#If ( < ) *val1* *val2*
*
commands to run
#If ( ~= ) *val1* *val2*
*
commands to run
#If ( >= ) *val1* *val2*
*
commands to run
#If ( <= ) *val1* *val2*
*
commands to run
Between the { and } brackets, you can put more than one command. These commands are run only if the tested conditionis true. Also, you should make sure that the { and } are on lines by themselves to prevent nesting errors!
The old Version 1 form using < and > for the opening and closing of the block is also valid.
**
Example:
* Example showing all forms of the #If... command.
#num1!=12
#text$="Hello"
#num2!=400
* Set up some variables to work with.
#If (num1!==12)
#MWin("num1! equals 12!!!")
* If the value in num1! equals 12, then "num1! equals
* 12!!!" will be displayed in the Message Window.
#If (text$=="Hello") {
#MWin("Here’s what’s in text$:")
#Show(text$)
* If text$ contains the word "Hello" (which it does),
* then the block is performed, which shows the contents of text$
* in the Message Window.
#If (num1! < num2!) { #Text (1,1,"num1! is < num2!") }
* If the value of num! (12) is less than the value of
* num2! (400), which they are, then "num1! is < num2!" is
* displayed at screen position 1,1 using the #Text
* command. Notice that the block can be on the same line as the
* If... statement only if you have one command in the block.
* This is not reccomended.
#If (num1! ~= num2!)
#MWin("num1! doesn't equal num2!")
* If the value in num1! (12) doesn't equal the value in
* num2! (400), then "num1! doesn't equal num2!" is placed in
* the Message Window.
#If (num1! > num2!)
#MWin("num1! is greater than num2!")
* If the value in num1! (12) is greater than the value
* of num2! (400), then "num1! is greater than num2!" is
* displayed in the Message Window.
* Since 12 isn't greater than 400, this message
* isn't displayed.
#Wait(a$)
Include program.**
Related Commands:
#Branch, #Fbranch, #Get
#Include
**
#Include(filename$)
This command loads another program and appends it to the end of the crrently running program. This allows you to import RPGCode libraries that give you access to new commands (such as the "system.prg" library, which allows array manipulation). filename$ is a literal value which is the filename of the program to include.
#Include commands should go at the first of the program, and be repeated more than once by loops (otherwise you’ll run out of program space). **must not**
**
Example:
#Include("system.prg")
*Include system library which gives me access to array commands.
#numSetArray("array",12,999) *Array command that is in the
*system.prg file.
#Show(array[12]!) *Show contents of our array.
Stay at inn.**
Related Commands:
#Method
#Inn
**
#Inn()
This command restores all HP and SMP for all players in the party.
**
Example:
#Inn()
Turn font italics on/off.**
Related Commands:
#HP
#Italics
**
#Italics("on/off")
This command turns the italics effect on the font on or off. The parameter is just a literal value that says "on" or "off".
**
Example:
#Bold("off")
#MWin("Boring regular text..")
#Bold("on")
#MWin("All of a sudden, I feel bolder!")
#Italics("on")
#MWin("Hey, italics, too!")
#Underline("on")
#MWin("Even an underline!")
#Wait(a$)
Count items.**
Related Commands:
#Bold, #Color, #ColorRGB, #Font, #FontSize, #Italics, #Mwin, #MWinCls, #Underline, #WinGraphic, #WinColorRGB
#ItemCount
**
#ItemCount("handle",dest!)
This command counts how many of any particular item the player is carrying. The number of those items is stored in dest!. "handle" can be the handle of the item to count, or the filename.
**
Example:
#ItemCount("cure",numCure!)
#Mwin("You have cures!")
#Wait(a$)
Define item walking speed.**
Related Commands:
#GiveItem
#ItemWalkSpeed
**
#ItemWalkSpeed("slow/fast")
This command defines the speed at which items walk (defined by fast or slow). By default, this value is set to "fast". A slower character walk speed uses better animation.
**
Example:
*Item animation…
#ItemWalkSpeed("Slow")
Kill variable.**
Related Commands:
#WalkSpeed
#Kill
**
#Kill(var$/var!)
This command deletes any variable from memory, thus freeing up memory for other variables. It’s a good idea to #Kill the variables of a method once the method is done.
**
Example:
#a!=12
#Show(a!)
#Kill(a!)
#Show(a!) *This command actually re-creates a! with 0 as
*it’s value.
Load a saved game.**
Related Commands:
#Method
#Load
**
#Load **(Filename$)** ends execution of the current program, and ends the current game. When the command is used, the player is taken to the board from which he/she saved their game, and all variables, literal and numerical are assigned the values that they held when the game was saved.
Throughout the game, the player has the ability to save his/her progress using programs that use the command. In order to play these saved games, however, a program must be run that uses the command to load a saved game. **#Save** **#Load**
The parameter is a literal parameter that is the filename of the saved game. When RPGCode saves a game, it adds a .SAV extension to the filename. If you don’t include the .Sav extention, it is added for you. Also, do not include any directory information as the RPGCode interpreter will find that for you. *filename$*
**
#Load
**#Load****
Example:
* Example using #Load
#Clear()
* Clear the screen.
#DirSav(Filename$)
* Show a directory of all saved games on the drive, and pt
* the selected filename in Filename$.
#If (Filename$ ~= "")
#Load(Filename$)
Run main file.**
Related Commands:
#Dirsav, #Prompt, #Save
#MainFile
**
#MainFile(file$)
This command resets the game and runs the specified main file. file$ is a literal value which represents the filname of the main file. Do not include any directory information as it will be determined for you.
This can be used to start a game with different characters at different locations at startup.
**
Example:
* Example showing some different main files.
#done!=0
#While(done!=0)
#MWinCls()
#MWin("Who would you like to start as?")
#Mwin("1- The good guys.")
#Mwin("2- The bad guys.")
#Wait(opt$)
#If (opt$=="1")
*run the main file of the good guys.
#MainFile("good.gam")
#done!=1
#If (opt$=="2")
*run the main file of the bad guys.
#MainFile("bad.gam")
#done!=1
Set Maximum player HP level.**
Related Commands:
#Reset, #Load, #Save
#MaxHP
**
#MaxHP(handle$, new_maxHP!)
This command works identically to , except that it sets the character’s HP level (the maximum the character can have). See for more info. **#HP** *maximum* **#HP**
**
Example:
*Setting the Max HP.
#GetMaxHP("Frap",frapMaxOld!) *Gets Frap’s max HP level.
#MWin("Frap’s old Maximum HP level: ")
*MaxHP("Frap",400) *Sets Frap’s max HP level to 400.
#GetMaxHP("Frap",frapMaxNew!)
#MWin("Frap’s new Maximum HP level: ")
Set Maximum player SMP level.**
Related Commands:
#GiveHP, #GetHP, #MaxHP, #GetMaxHP, #SMP, #GiveSMP, #GetSMP, #MaxSMP, #GetMaxSMP
#MaxSMP
**
#MaxSMP(handle$, new_maxSMP!)
This command works identically to , except that it sets the character’s SMP level (the maximum the character can have). See for more info. **#SMP** *maximum* **#SMP**
**
Example:
*Setting the Max SMP.
#GetMaxSMP("Frap",frapMaxOld!) *Gets Frap’s max SMP level.
#MWin("Frap’s old Maximum SMP level: ")
*MaxSMP("Frap",400) *Sets Frap’s max SMP level to
*400.
#GetMaxSMP("Frap",frapMaxNew!)
#MWin("Frap’s new Maximum SMP level: ")
Put a scanned tile from memory on the board.**
Related Commands:
#GiveHP, #GetHP, #MaxHP, #GetMaxHP, #SMP, #GiveSMP, #GetSMP, #MaxSMP, #GetMaxSMP
#Mem
**
#Mem (x!, y!, Mem_pos!)
This command places a tile on the board that has been saved in memory with the command. **#Scan**
x! is a numeric value which is the x position (horizontal) on the board grid on which to place the tile. This is a value from 1-19. y! is the y position (vertical) on the board grid on which to place the tile. This is a value from 1-11.
The Mem_pos! is a numeric value from 1-10 stating which tile from memory you wish to place on the board.
**
Example:
* Example showing the #Scan and #Mem commands.
#Scan (3, 8, 2)
* Take the tile at location 3,8 and store it in
* memory position 2.
#x!=1
#y!=1
#Mem (x!, y!, 2)
* Place the tile in memory position 2 at screen
* position 1,1 (these are the values stored in x!
* and y!).
Change Menu graphic.**
Related Commands:
#Put, #Scan
#MenuGraphic
**
#MenuGraphic(filename$)
You can put a graphic in the background of the internal menu by using this command. filename$ is a literal value which specifies the filename of the graphic to place in the Window (Bmp, Gif or Jpg).
**
Example:
#MenuGraphic("wow.bmp")
Define a method.**
Related Commands:
#Bold, #Color, #ColorRGB, #FightMenuGraphic, #Font, #FontSize, #Italics, #Mwin, #MWinCls, #Underline, #WinColor, #WinColorRGB
#Method
**
#Method ( ) *methodname* *parameters* is the name of the method you are defining. Essentially, the method’s name is the same as a command name. If you created a method called DrawHouse, you would call the method in the same way as you would call any command ( ). You replace the methodname with any variable.
The Method command allows you to define a method. Methods are like functions (see ), but are much better reccommended. Using methods, you can infinitely expand the RPGCode language by creating your very own commands. Commands created with the #Method command work in the very same way as the built in commands, and for all prposes, are indistinguishable from the built in commands. **#Fbranch**
*
methodname
*#DrawHouse* **cannot**
The are the variables that get passed to the method. It kind of hard to explain- it’s better if you actually see it, so look at the example below. *parameters*
Unless a method is actually called, the method declaration and following block of commands is ignored by the RPGCode interpreter.
The command allows you to return values to the calling command. It’s a good idea to #Kill variables created inside the method when it’s done. **#ReturnMethod**
**
Example:
* Example displaying methods.
#WalkInCircle("Frap") *This calls the method ‘WalkInCircle’
*and passes the literal value "Frap"
*as a parameter.
#Add(1,1,result!) *This calls the method ‘Add’ and passes
*the values 1, 1, and result! (result! *is the destination variable, though, as
*we will see in the declaration).
*This is the actual method declaration for the ‘WalkInCircle’
*command.
*Notice that the parameter is wic_handle$. This means that when
*the command ‘#WalkInCircle("Frap")’ is performed, the value
*"Frap" gets put into the variable wic_handle$
#Method WalkInCircle (wic_handle$)
#Push("N",wic_handle$)
#Push("E",wic_handle$)
#Push("E",wic_handle$)
#Push("S",wic_handle$)
#Push("S",wic_handle$)
#Push("W",wic_handle$)
#Push("W",wic_handle$)
#Push("N",wic_handle$)
#Kill(wic_handle$)
*This is the method declaration for the ‘Add’ command.
#Method Add (add1!, add2!, add_return!)
#add_return!=add1!+add2!
#ReturnMethod(add_return!)
*Returns add_return! to the calling command. (In this case,
* result! will get the same value as add_return!
#Kill(add1!)
#Kill(add2!)
#Kill(add_return!)
Play midi file.**
Related Commands:
#Include, #Kill, #ReturnMethod
#MidiPlay
**
#MidiPlay (filename$)
This plays a Midi file. filename$ is a literal value that specifies what midi file should be played.
**
Example:
#MidiPlay("castle.mid")
* Plays a file called ‘castle.mid’
Stop midi player.**
Related Commands:
#MidiRest, #MediaPlay, #Start, #Wav
#MidiRest
**
#MidiRest()
This command causes the currently playing mid file to stop playing.
**
Example:
#MidiPlay("castle.mid")
#MWin("Press a key to stop the music")
#Wait(a$)
#MidiRest()
Wait for user to click mouse.**
Related Commands:
#MidiPlay, #MediaPlay
#MouseClick
**
#MouseClick(x!,y!)
This command waits for the user to click the mouse, then puts the x and y coordinates of the location where it was clicked into the variables x! and y!. This command can be used like the #Wait command, except instead of having the player press a key on the keyboard, he will have to click a button defined by the #SetButton command.
**
Example:
*Button…
#SetButton("b1.jpg",0,10,10,100,100)
*create a button in slot 0
#done!=0
#While(done!==)
#MouseClick(x!,y!)
#CheckButton(x!,y!,num!) *check if a button was pressed
#if (num!==0)
*button 0 was pressed!
#Mwin("you pressed the button!")
#Wait(a$)
#done!=1
#ClearButtons()
Wait for user to move mouse.**
Related Commands:
#CheckButton, #ClearButtons, #MouseMove, #SetButton, #Wait
#MouseMove
**
#MouseMove(x!,y!)
This command waits for the user to move the mouse, and then puts the x and y coordinates of the mouse location into x! and y!.
**
Example:
#MouseMove(x!,y!)
#Mwin(You moved to: , ")
#Wait(a$)
Move program location.**
Related Commands:
#MouseClick, #Wait
#Move
**
#Move (x!, y! [,layer!])
This command continues execution of the current program, but moves it to a new location on the board. This means that when this command is used, the next time the player steps on the tile where the program used to be, nothing will happen. If, however, the player steps on the tile that the program was assigned to with the command, then the program will run again. **#Move**
The x! and y! are values stating where on the board the program will be moved to. These are the x and y coordinates of the new location. The x value ranges from 1-19, and the y value ranges from 1-11. The layer! is optional. If it is not included, layer! is assumed to be 1. This allows you to specify what layer on the board it should be moved to, and this is a number from 1-8.
The command remains in effect only during the time that the player is on the board.
**
Example:
* Using the #Move command
#Move (3,8,1)
* Moves this program to the new position 3,8 on layer 1.
#MWin("This program has moved.")
#Wait(a$)
Display text to Message Window.**
Related Commands:
#Change, #Gone, #Prg
#MWin
**
#MWin(text$)
This command displays text in the message window. text$ is a literal value that is the text to place in the message window.
You can also place variables within th text itself by usrrounding the variable name with < and >. For example, so show the variable name$ within the text, you would pass the parameter: "Hello, . How are you?". Variables within the text may be literal or numerical.
**
Example:
*Put some stuff in the message window.
#MWinCls() *Clear message window.
#Prompt("Please enter your name:",name$)
#MWin("Hello, !")
#Wait(a$)
Clear Message Window.**
Related Commands:
@, #Font, #MWinCls, #Text
#MWinCls
**
#MWinCls()
This command clears the contents of the message window and causes it to disappear.
**
Example:
*Put some stuff in the message window.
#MWinCls() *Clear message window.
#Prompt("Please enter your name:",name$)
#MWin("Hello, !")
#Wait(a$)
Adjust message window size.**
Related Commands:
@, #Font, #MWin, #Text
#MWinSize
**
#MWinSize(size!)
This command adjusts the size of the message window. Size! is a numerical value that is the percentage of the screen the window will take up horizontally. The default is 95.
**
Example:
#Mwin("Text before…")
#MwinSize(70)
#Mwin("Text after")
#Wait(a$)
New player.**
Related Commands:
#MWin
#NewPlyr
**
#Newplyr (Filename$)
This command changes the player graphic to the graphic saved as the filename in Filename$. Valid file formats for the new plaer graphic are .Gph, .Cha, or .Tem. You must inclde the extension so that RPGCode knows which one you want.
This command remains in effect until changed with another command. **#Newplyr**
**
Example:
* Change the player graphic.
#MWin("Out with the old...")
#Wait(a$)
#NewPlyr ("player.tem")
* Loads the graphics in "player.tem", and puts it in
* place of the player graphic.
#MWin("In with the new!!!")
#Wait(a$)
Game Over.**
Related Commands:
#Mem, #Put, #Scan
#Over
**
#Over()
This command displays a "Game Over" message, waits for the user to press a key, and resets the game to the startup program.
If a program is going to initiate a "Game Over", you may wish to add special effects using other commands, instead of using . To reset the game to the startup program after doing these special effects, use the command , instead of the command. **#Over** **#Reset** **#Over**
**
Example:
* Oh, no! Your game is over!
#Over()
* Displays a Game Over message, waits for a key
* press, and then resets the game to the startup
* program.
Play avi (full screen)**
Related Commands:
#Reset, #Win
#PlayAvi
**
#PlayAvi(file$)
This command plays an avi file fullscreen. File$ is the filename to open. It is a good idea to stop the background music with #MidiRest before using this command.
**
Example:
#MidiRest()
#PlayAvi("movie.avi")
Play avi (windowed)**
Related Commands:
#PlayAviSmall
#PlayAviSmall
**
#PlayAviSmall(file$)
This command plays an avi file in a window. File$ is the filename to open. It is a good idea to stop the background music with #MidiRest before using this command.
**
Example:
#MidiRest()
#PlayAviSmall("movie.avi")
Show character posture.**
Related Commands:
#PlayAvi
#Posture
**
#Posture(posturenum! [,handle$])
This command shows a custom posture of the character. In the character editor, you can define up to 10 custom postures for your character. This command allows you to use them. Posturenum! Is a number between 0 and 10 that defines which posture number you wish to show, as defined in the character editor. Handle$ is an optional argument that is the character’s handle. By default, it will use the main character, but you can also have secondary characters use this as well.
This command is good for causing the character to do things like tap his foot, or other custom animations. Simply put each frame of the animation in the posture slots and then cycle through them with this command.
**
Example:
*cycle through postures 0-3 (character nodding his head)
#for (t!=0;t!<=3;t!=t!+1)
#Posture(t, "Frap")
Change Program Location.**
Related Commands:
#Push, #Stance
#Prg
**
#Prg (program_num!, x!, y! [,layer!]) or
#Prg(filename$, x!, y! [,layer!])
ny change you make with the command remains in effect only for the time the player is on this board.
This command moves the program assigned to a certain program number to a new location on the board.
The program number for all programs is defined in the Board Editor in the Program Info screen. The program_num! is a number from 0 to 50 which represents which program you are dealing with from the Program Screen of the Board Editor. Alternatively, you may put a filename here.
The x! and y! values are the x and y coordinates on the board where you wish to place the program. The x value is a number from 1-19, and the y value is a number from 1-11. The layer! is an optional value that lets you specify which layer to send it to. If not included, it is assumed to be 1.
*
A
**#Prg****
Example:
#Prg ("test.prg",12,8,1)
* Moves the program "test.prg" to 12, 8, layer 1.
Print text to screen.**
Related Commands:
#Change, #Gone, #Mem, #Put, #Scan
#Print
**
#Print(text$)
This command displays text on the screen at the current text position. The current text position is defined by the command- it is on the line directly floowing the last placement of text using the command. **#Text** **#Text**
Text$ is the text to print.
**
Example:
#Text(5,5,"Line 1")
#Print("Line 2")
#Wait(a$)
Prompt command.**
Related Commands:
@, #Font, #MWin, #Text
#Prompt
**
#Prompt ("Prompt question", dest$)
This command prompts the player with a question, and assigns whatever the player types to a variable (either numerical or literal).
The is a question that is asked of the player. This question appears in a popup window. *prompt question*
The dest$ variable is the variable to which the player's response is saved. It can be either numerical or literal.
**
Example:
* This gets the player's name.
#Prompt ("What is your name?",name$)
#MWin("I know your name. It is: ")
* Shows the contents of name$ (which is what the player
* just typed).
#Wait(a$)
Push player.**
Related Commands:
#Wait
#Push
**
#Push(direction$ [,handle$])
This command forces the player graphic on the screen to walk around. Direction$ is a literal value that specifies what the direction is ("n", "s", "e", "w").
The handle$ is an optional value that specifies character should be pushed. It’s the handle of a player on your team. By default this is if nothing is specified, which means that he Target player (or the player you’re currently using) is pushed. *which* *Target*
Alternatively, you can specify the handle of another player on your team. For example, if a game was playing and the team had two players on it- the first one called Frap and the second one called Tano, I could make Tano walk around using #Push("N","Tano").
This is used to create story sequences in which the characters in your party walk around and interact with one another.
**
Example:
*This program assumes that the team has two characters- the
*main one called Frap and the second one called Tano.
#Push("N") * Pushes Frap North, since Frap is the Target
* player.
#Push("N","Target") *Does the same thing.
#Push("N","Frap") *Does the same thing.
#PutPlayer("Tano",1,1,1) *Put the Tano character at 1,1,1.
#Push("E","Tano") *Pushes Tano East.
Push item.**
Related Commands:
#PushItm, #PutPlayer
#PushItem
**
#PushItem(itemnum!, direction$)
This command forces an item on the board to walk in any direction (it will only show up if the item has walking graphics, though). itemnum! is a numerical value that represents the item number to push, as was defined in the Board Editor. It is a number between 0 and 10.
Alternately, if this is run as part of a multitask program by an item, you could use the keyword "Target" instead of itemnum! to refer to the currently selected item.
direction$ is the direction to walk ("N, S, E or W").
**
Example:
*Let’s say that item 0 is running this as a multitask program:
#PushItem(0,"N") *Pushes itself north.
#PushItem("Target","N") *Does the same thing.
Put graphics tile on board.**
Related Commands:
#Push, #Wander
#Put
**
#Put (x!, y!, filename$)
This command loads a graphics tile and places it on the board at the specified position. This graphic will remain on the board only for the duration of time that the player is on the board.
x! and y! are the x and y coordinates on the board where the graphic is to be placed. The x value ranges from 1-19, and then y value ranges from 1-11.
The filename of the graphic to load, a literal value filename$, must be a valid .Gph filename.
**
Example:
* Puts a graphic at 12,11
#Put (12,11,"tile1.GPH")
* Places the graphic saved as "tile1.GPH" at
* position 12,11 on the board.
Put item graphic on screen.**
Related Commands:
#Mem, #Scan, #Viewbrd
#PutItem
**
#PutItem(itemnum!,x!,y!,layer!)
This command puts an item on the screen at a defined x, y, layer position. This command is useful in conjunction with the #CreateItem command to make temporary animated characters that move around and talk, like in a story sequence. itemnum! Is the number (from 0 to 10) of the item, as defined on the board editor, or with the #CreateItem command. x!, y! and layer! Are the coordinates of the location on which to place the item.
**
Example:
*Item animation…
#CreateItem("soldier.itm",pos!) *load an item into a slot
#PutItem(pos!,1,1,1) *put the item at 1,1, layer 1
#PushItem(pos!,"E") *move the item
#PushItem(pos!,"E") *move the item
#PushItem(pos!,"E") *move the item
#PushItem(pos!,"E") *move the item
#Mwin("hello!")
#Wait(a$)
#EraseItem(pos!) *remove item from screen
#DestroyItem(pos!) *remove item from memory.
Put player garphic somewhere..**
Related Commands:
#CreateItem, #DestroyItem, #EraseItem
#PutPlayer
**
#PutPlayer(handle$, x!, y!, layer!)
This command places any player on your team somewhere on the board. You can use this to put the main character somewhere, but this command is really for the teammates in the party. This command, when used in conjunction with other commands such as and can create story sequences in which your players talk to each other. *other* **#Push** **#ErasePlayer**
handle$ is a literal value that specifies which character you are referring to. x!, y! and layer! are numerical values that specify the board x, y, and layer positon of the player.
**
Example:
* Short story sequence in which Frap and Tano interact.
* Frap is the main character and so is already on the board.
* Let’s say Frap is at 5,5. We’ll have Tano "emerge" from
* this location as if he is popping out of the party.
#PutPlayer("Tano",5,5,1)
#Push("E","Tano")
#Push("E","Tano")
#Push("W","Tano")
#MWinCls()
#Mwin("Tano: Well, here we are in some odd")
#Mwin(" RPGCode story sequence.")
#Wait (a$)
#MWinCls()
#MWin("Frap: Watch this!")
#Wait (a$)
#MWinCls
#Push("N","Frap")
#Push("E","Frap")
#Push("E","Frap")
#Push("S","Frap")
#MWin("Tano: Wow, that’s really great. You can")
#Mwin(" walk. Now I’m going to walk towards")
#Mwin(" you and vanish into your chest somehow.")
#Wait(a$)
#MWin("Frap: Cool.")
#Wait(a$)
#MWinCls()
#Push("E","Tano")
#ErasePlayer("Tano")
Produce a random number.**
Related Commands:
#ErasePlayer, #Push
#Random
**
#Random(range!, dest!)
This command produces a random number and places it in a variable. range! is the range of the random number. For example, if range! were 100, then the random number would be between 1 and 100.
dest! is the numerical variable to which the number should be put.
**
Example:
* Show 5 random numbers.
#For (num!=1; num!<=5; num!=num!+1)
#Random(100,my_number!)
#Show(my_number!)
Remove equipment.**
Related Commands:
None
#Remove
**
#Remove(handle$, body_location!)
This command removes an item that is currently equipped to the player and returns it to the inventory.
handle$ is a literal value that specifies the handle of the player to remove from. "Target" specifies the currently selected player.
body_location! is a numerical value between 1 and 16. It specifies the body location to remove from. Valid positions are:
1- Head
2- Neck accessory
3- Left Hand
4- Right Hand
5- Body
6- Legs
7-16 Accessories 1-10
**
Example:
*remove a sword on Frap’s right hand.
#Remove("Frap",4)
Remove player from party.**
Related Commands:
#GiveItem, #Equip
#RemovePlayer
**
#RemovePlayer(player_filename$)
This command removes a player from the current party (team). There are a maximum of 5 characters allowed on a team at any time. player_filename$ is a literal value that is the filename of the player to remove, or the player’s handle.
Unlike #DestroyPlayer, this command allows to to restore the player later on with #RestorePlayer or #CallPlayerSwap.
**
Example:
* Remove player Tano to your team.
#RemovePlayer("Tano")
Reset to the startup program.**
Related Commands:
#AddPlayer, #DestroyPlayer
#Reset
**
#Reset()
This command resets the game to the first, loading and running the startup program and then beginning on the first board.
**
Example:
* This program resets the game.
#MWin("Restart game.")
#MWin("Are you sure (Y/N)")
#done!=0
#While (done!=0)
#Wait(opt$)
#If (opt$=="y") { #Reset() }
#If (opt$=="n")
#done!=1
*This breaks out of the while loop.
#End()
Restore a previous player.**
Related Commands:
#Over, #Win
#RestorePlayer
**
#RestorePlayer("player.tem")
This command loads a player from a file, but restores the values that player had before he or she was removed from the party.
**
Example:
#AddPlayer("joey.tem")
#RemovePlayer("joey.tem")
#RestorePlayer("joey.tem") *joey is restored to party.
Return Screen.**
Related Commands:
#AddPlayer, #RemovePlayer
#Return
**
#Return()
This command restores the screen to the way it was before the program began, erasing all graphics placed on the board, and removing the Message Window. This is often used in conjunction with the command, which clears the screen. **#Clear**
**
Example:
* Example that clears the screen and then restores it.
#Clear()
#MWin("The screen is cleared.")
#MWin("Press a key...")
#Wait(a$)
#Return()
* Restores the screen to the way it was before #CLEARing it.
#Done()
* Ends execution of the program, but does not
* restore the screen to the way it was before the
* program began (the #Return command already did
* that).
Return method value..**
Related Commands:
#Clear, #Done, #End, #Fade, #Mem, #Put, #Scan, #Text, #Viewbrd
#ReturnMethod
**
#ReturnMethod ( ) *variable$!*
This command is used to return the value of a variable from within a method to the calling command. This allows methods to calculate values and then return them for the program to use.
When a method is called, a number of parameters are passed to it. For example, you can call a method called Add using #Add(1,3,result!). The parameters that are passed are 1,1,result!. What becomes of these values? Well, if you look at the method declaration, you will see: #Method Add (add1!,add2!,add_return!). In this case, the varible add1! gets the value of 1, add2! gets the value of 3 and add_return! gets the value in result!
Inside the method itself, we can use the command . What does this do? Well, you will recall that when the method was called, add_return! got the value that was in result!. Well, now, result! gets the value in add_return!. You can see this in the example below. **#ReturnMethod(add_return!)**
**
Example:
* Example displaying methods.
#Add(1,1,result!) *This calls the method ‘Add’ and passes
*the values 1, 1, and result! (result! *is the destination variable, though, as
*we will see in the declaration).
#Show(result!) *Displays "2" (1+1=2, which is what the Add
*method does!)
*This is the method declaration for the ‘Add’ command.
#Method Add (add1!, add2!, add_return!)
#add_return!=add1!+add2!
#ReturnMethod(add_return!)
*Returns add_return! to the calling command. (In this case,
* result! will get the same value as add_return!
Perform RPGCode command.**
Related Commands:
#Include, #Kill, #Method
#RPGCode
**
#RPGCode (command$)
This command performs any RPGCode command. command$ is a literal value which is the command to run. This is used for debugging purposes- you can input text with the command and run that text as an RPGCode command. You can also use it for creating complex methods that perform complicated tasks (like the library). **#Prompt** *array.prg*
**
Example:
*Let the user type in an RPGCode command.
#Prompt("Please type an RPGCode command:",rpgcode$)
#RPGCode(rpgcode$) *run the inputted command.
#RPGCode("#MWin("good job!")") *Just for fun.
Run Program.**
Related Commands:
#Debug, #Prompt
#Run
**
#Run (filename$)
This command ends execution of the current program, and loads and then runs another program. This command can be used to shorten up large programs by breaking them up into smaller sections.
Also, if your program is too big for the RPGCode environment limits (2000 lines), then on the last line, you can use a command to load another program that picks up where the last one left off. **#Run**
The filename$ is a literal value that specifies the filename of the .Prg file.
**
Example:
* Program that runs another one.
#MWin("I'm in program 1!!!")
#MWin("Press a key to run program 2.")
#Wait(a$)
#Run ("another.PRG")
Save player's progress.**
Related Commands:
#Branch, #Change, #Fbranch, #Load, #Save
#Save
**
#Save (filename$) 's counterpart, , is used to restore saved games.
Throughout the game, the player has the opportunity to save his/her progress to disk, so that they can continue playing the same game at a later date. The command allows you to do this. **#Save**
The filename$ can be any valid filename. If it does not have the .sav extension, it is added automatically. You should use the command to get the filename. **#DirSav**
**
#Save
**#Load****
Example:
* Example using #Save
#DirSav(saveto$)
* Show a directory of all saved games on the drive.
#If (saveto$~="")
#Save(saveto$)
*Save the game!
Scan a graphics tile.**
Related Commands:
#Dirsav, #Load, #Prompt
#Scan
**
#Scan (x!, y!, mem_location!)
This command scans a tile on the board, and saves an image of that tile in an available memory location. That image may be placed on the board using the command. **#Mem**
x! and y! are the x an y coordinates on the board of which tile you wish to scan. The x position ranges from 1-19, and the y position ranges from 1-11.
The mem_location! is a number between 1-10, that chooses which memory location the image is to be saved to. There are 10 possible memory locations.
**
Example:
* Scans a tile at location 12,8 and then puts the
* stored graphic at position 5,5.
#Scan (12, 8, 1)
* Stores an image of the graphic tile at 12,8, and
* stores it at memory location 1.
#Mem (5, 5, 1)
* Puts the stored image in memory location 1 at the
* board position 5,5.
Send player to new board.**
Related Commands:
#Mem, #Put
#Send
**
#Send ("board.brd",x!,y! [,layer!])
This command loads a new board, and puts the player at the x and y coordinates specified on the board. This continues execution of the current program as well. This command can be quite useful when you place doors in the middle of the board somewhere, and a program is needed to send the player to the next board (because manually, the player only moves to another board by moving to the edges of the board. This command allows the player to go to any board from any position on the board).
The filename, , of the board to which the player is being sent is a literal value. The x! and y! are the x and y coordinates where the player will appear on the new board (x ranges between 1 and 19, while y ranges between 1 and 11). *board.BRD*
layer! is the layer of the new board and is optional. If not included, it is assumed to be 1.
**
Example:
* An example of a door program that sends the player
* to another board when the player walks into the
* door.
#Send ("another.BRD", 5, 5, 1)
* Sends the player to "another.BRD", and places them
* at position 5,5, layer 1 on that board.
Set a button on the screen.**
Related Commands:
#Viewbrd
#SetButton
**
#SetButton("face.bmp", bnum!, x!, y!, width!, height!)
This command puts a clickable button on the screen. "face.bmp" is the name of a graphic defining the button (it may be a bmp, gif or jpg). Bnum! Is a number between 0 and 50 defining which button you are creating (you may have up to 50 buttons, but each resides in a different ‘slot’ in memory). X! and y! are the x and y coordinates on which to place the button. Width! And height! Are the width and height of the button (usually the width and height of the face graphic). The use of this command in conjunction with the #MouseClick and #CheckButton commands allows you to work with clickable buttons.
**
Example:
*Button…
#SetButton("b1.jpg",0,10,10,100,100)
*create a button in slot 0
#done!=0
#While(done!==)
#MouseClick(x!,y!)
#CheckButton(x!,y!,num!) *check if a button was pressed
#if (num!==0)
*button 0 was pressed!
#Mwin("you pressed the button!")
#Wait(a$)
#done!=1
#ClearButtons()
Draw a pixel on the screen.**
Related Commands:
#CheckButton, #ClearButtons, #MouseClick
#SetPixel
**
#SetPixel (x!, y!)
This command sets a pixel on the screen using the currently defined color (set with Color or #ColorRGB). **#**
x! and y! are the x an y coordinates on the screen to place the pixel at. They are numerical values. The screen area is defined as 608x352 pixels. Anything within these bounds is ok. The origin (0,0) is located in the top left hand corner.
The pixel will only remain on the screen as long as the program Is running (unless you use the command). **#Done**
**
Example:
* Draws a line of pixels from 0,0 to 0,255
#For (y!=0; y!<=255; y!=y!+1)
#ColorRGB(y!,y!,y!)
#SetPixel(0,y!)
Show variable contents.**
Related Commands:
#drawLine, #drawRect, #fillRect
**
#Show
**
#Show **(variable!$)**
This command displays the contents of any numerical or literal variable in the Message Window. The contents of the variable must appear on a line all by themselves.
A better way of doing this is by using the command. **#Mwin**
**
Example:
* Example of the #Show command.
#var1!=400
#var2$="Hello"
* Puts the value 400 in the variable var1!, and the
* string "Hello" in the variable var2$.
#Show (var1!)
#Show (var2$)
* Outputs contents of var1! (400), and var2$ ("Hello") to
* the Message Window.
#Wait(a$)
Set player Special Move Power level.**
Related Commands:
#Get, #Mwin, #Prompt, #Text
#SMP
**
#SMP(handle$, new_SMP!)
This command will set the SMP (Special Move Power) level of any player on your team or a selected enemy in a fight. handle$ is a literal value which is the handle of the character to edit. If you use the keyword "Target" as the handle, the player that will be changed is the character that is currently being selected from the internal menu, the fight screen, or even a selected enemy on the fight screen.
new_SMP! is a numerical value which specifies what the new SMP level of the character/enemy is.
**
Example:
*Giving SMP to characters/enemies.
#SMP("Frap",100) *Sets Frap’s SMP level to 100.
#SMP("Tano",200) *Sets Tano’s SMP level to 200.
#SMP("Target",150) *Sets the target’s SMP level to 150 (may be
*an enemy or a player, depending upon who is
*currently selected).
Play sound over PC speaker.**
Related Commands:
#GiveHP, #GetHP, #MaxHP, #GetMaxHP, #SMP, #GiveSMP, #GetSMP, #MaxSMP, #GetMaxSMP
#Sound
**
#Sound (Frequency, Duration) Change player stance.
This command used to be used to play sounds through the PC Speaker, but is no longer supported. Use the Multimedia commands such as #Midiplay, #MediaPlay, etc. instead.
**
#Stance
**
#Stance(position! [,handle$]) 1-4 Facing south
This command changes the way the player is standing. Position! Is the player position to use, and is a number between 1 and 43. Handle$ is optional. If you omit it, it is assumed to be Target.
*
Positions:
>
> >
> > >
> > > >
> > > > >
> > > > > >
> > > > > > >
> > > > > > > >
> > > > > > > > 5-8 Facing east
> > > > > > > >
> > > > > > > > 9-12 Facing north
> > > > > > > >
> > > > > > > > 13-16 Facing west
> > > > > > > >
> > > > > > > > 17-20 Fight graphics
> > > > > > > >
> > > > > > > > 21-24 Special move graphics
> > > > > > > >
> > > > > > > > 25-28 Defence graphics
> > > > > > > >
> > > > > > > > 29-32 Dying graphics
> > > > > > > >
> > > > > > > > 33-42 Custom postures
> > > > > > > >
> > > > > > >
> > > > > >
> > > > > > 43 Fight at rest graphic
> > > > > >
> > > > >
> > > >
> > >
> >
>
**
Example:
*cycle thru all graphics:
#for (count!=1;count!<=43;count!=count!+1)
#Stance(count!,"Frap")
Start file using Windows shell.**
Related Commands:
#Posture
#Start
**
#Start(file$)
This command allows you to run file using the Windows’ shell. file$ is a literal value that specifies the filename to run. any
The file can be any valid filetype on the computer, and you must include all the directory information. For example, you can run an AVI movie by using the command . As long as the extension is included, the Operating System will know what you’re talking about and will run it. **#Start("file.AVI")**
This command will not run any file with a .exe, .com, .pif, .bat or .lnk extension. Also, if you do not specify an extension, the command will not work. This is in compliance with the new security rules outlined in version 2.05.
It is valid to put a web address here. So will open up the default web browser and take you to RPG Toolkit Online. **#Start ("http://rpgtoolkit.pyar.com/")**
**
Example:
* Doing stuff with #Start
#done!=0
#While(done!=0)
#MWinCls() * Clear message window.
#MWin("Please select what you want to do:")
#MWin("1- Play AVI file")
#MWin("2- Go to RPG Toolkit Online")
#Mwin("3- Quit this program")
#Wait(opt$)
#If (opt$=="1")
*Play an AVI
#Start ("file.AVI")
#done=1
#If (opt$=="2")
*Go to Awesome RPG Toolkit Online
#Start("http://come.to/awesomesoftware/")
#done=1
#If (opt$=="3")
*Quit program- set done!=1 to break out of the while
*loop
#done=1
Take Gold from player.**
Related Commands:
#MediaPlay, #MidiPlay, #MidiRest, #Wav
#TakeGP
**
#GiveGP(amount!)
This command takes GP from the player.
**
Example:
#GetGP(gplev!)
#MWin("You had: GP")
#GiveGP(100)
#GetGP(gplev!)
#MWin("Now you have: GP")
#TakeGP(100)
#GetGP(gplev!)
#MWin("And now you have: GP")
Take player item.**
Related Commands:
#GetGP, #GiveGP
#TakeItem
**
#TakeItem(item_filename$)
This command removes an item from the player’s inventory. item_filename$ is the filename of the item, and is a literal value. Don’t include any directory info as RPGCode will determine that for you.
You may use the item’s handle instead of the filename.
**
Example:
*Take away a sword:
#TakeItem("sword.itm")
#MWin("You just lost a sword!!!")
#Wait(a$)
Get co-ords of targeted character/enemy.**
Related Commands:
#Equip, #GiveItem, #TakeItem
#TargetLocation
**
#TargetLocation(x!, y!) The x! and y! are literal variables that accept the x and y location.
This command returns the x and y coordinate of the targeted character or enemy in battle. This is useful for programs that run with special moves because you can put an ‘explosion’ graphic or whatever at the enemy’s position.
**
**
Example:
*Target an enemy:
#TargetLocation(x!,y!)
#PutGraphic("boom.gph",x!,y!)
#Wav("boom.wav")
Show text anywhere onscreen.**
Related Commands:
#AttackAll, #DrainAll
#Text
**
#Text (x!, y!, "text")
This command is useful, because it allows you to write text on the screen outside the Message Window. It also allows you to place the values in variables anywhere onscreen.
The range of x! and y! are determined by the size of the font. You cn determine what the range is in this way: For x, divide 608/the font size. For y, divide 352/the font size. You tell the computer where to place the text onscreen by specifying the and . These are values that are the x and y coordinates on the screen to place the text. *screen x pos* *screen y pos*
Note that the screen x and y coordinates are not the same as the board x and y coordinates. The board is divided up into a grid of 19 X 11 tiles, while the screen is divided up into . *text positions*
Wherever you specify the text to be using the x and y coordinates, there is where the text will be placed.
Whatever text you wish to put onscreen must be in the place where is in the above example. *text*
All text you put onscreen will be the color specified by the command. **#Color**
Any text you place on the screen is erased when the program ends, unless you use the command to end the program. **#Done**
**
Example:
* Examples using the #Text command in different situations.
#Clear()
* Clear the screen.
#num!=100
#text$="Hello, player"
* Set up some variables that will be displayed later on.
#Text (1,1,"This is text")
* Puts the line "This is text" in the upper left hand corner of
* the screen (position 1,1).
#Color (1)
* Sets the text color to be blue (color code 1).
#Text (3,8,num!)
* Puts the value stored in num! (100) at screen position 3, 8.
#Text (3,9,text$)
* Puts the string stored in text$ ("Hello, player") at screen
* position 3,9.
Adjust text scroll speed.**
Related Commands:
#Color, #Dirsav, #Show
#TextSpeed
**
#TextSpeed(speed!)
This command adjusts the speed at which text will scroll in your game. Speed! Is a numerical value and is a number between 0 and 3. 3 is the fastest speed and is the default.
**
Example:
#Mwin("Text before…")
#TextSpeed(0)
#Mwin("Text after")
#Wait(a$)
Change tile type..**
Related Commands:
#BattleSpeed, #CharacterSpeed
#TileType
**
#TileType(x!, y!, type$ [,layer!])
Changes the tile type at a specified position on the board. x! and y! specify the x and y position. layer! is an optional numerical value that specifies which layer it is at. It is assumd to be 1 if it’s not specified.
type$ is a literal value that specifies which type it is to be. Valid types are: SOLID, NORMAL, UNDER,
**
Example:
* Change the tile at 10,10,1 to solid
#TileType(10,10,"Solid",1)
Turn under arrow on/off.**
Related Commands:
#ViewBrd, #Prg
#UnderArrow
**
#UnderArrow("on/off")
By default, when a player walks underneath an ‘under’ tile or a layered tile, an arrow is put in place of the player to show where he or she is. This command allows you to turn this arrow on or off. The parameter is a literal value that is ether ‘on’ or ‘off’.
**
Example:
#UnderArrow("off")
Turn font underline on/off.**
Related Commands:
#Bold, #Color, #ColorRGB, #Font, #FontSize, #Italics, #Mwin, #MWinCls, #Underline, #WinGraphic, #WinColorRGB
#Underline
**
#Underline("on/off")
This command turns the underline effect on the font on or off. The parameter is just a literal value that says "on" or "off".
**
Example:
#Bold("off")
#MWin("Boring regular text..")
#Bold("on")
#MWin("All of a sudden, I feel bolder!")
#Italics("on")
#MWin("Hey, italics, too!")
#Underline("on")
#MWin("Even an underline!")
#Wait(a$)
View Board.**
Related Commands:
#Bold, #Color, #ColorRGB, #Font, #FontSize, #Italics, #Mwin, #MWinCls, #Underline, #WinGraphic, #WinColorRGB
#Viewbrd
**
#Viewbrd (Filename$)
This command loads a board, and displays it on the screen, but once the program has ended, the board is erased, and the game goes back to the board it started the program from.
The filename of the board to display, Filename$, is a literal value.
**
Example:
#Viewbrd ("another.BRD")
Wait for key press.**
Related Commands:
#Mem, #Put, #Scan, #Send
#Wait
**
#Wait(dest$)
This command causes the computer to pause and wait for the player to press a key. It puts the resulting keypress in a literal variable (dest$). If the player presses any of the arrow direction keys, the words "UP", "DOWN", "LEFT" or "RIGHT" are put in the destination variable.
**
Example:
#Wait(a$)
#MWin("You pressed: ")
#Wait(a$)
* The second #Wait just pauses the program and waits for the user
* to press a key.
Define character walking speed.**
Related Commands:
#Prompt
#WalkSpeed
**
#WalkSpeed("slow/fast")
This command defines the speed at which the character walks (defined by fast or slow). By default, this value is set to "fast". A slower character walk speed uses better animation.
**
Example:
*Item animation…
#WalkSpeed("Slow")
#Push("S")
#Push("S")
#Push("S")
#WalkSpeed("Fast")
#Push("N")
#Push("N")
#Push("N")
Cause item to wander.**
Related Commands:
#ItemWalkSpeed
#Wander
**
#Wander(itemnum!)
This command forces an item on the board to walk in a random direction (it will only show up if the item has walking graphics, though). itemnum! is a numerical value that represents the item number to wander, as was defined in the Board Editor. It is a number between 0 and 10.
Alternately, if this is run as part of a multitask program by an item, you could use the keyword "Target" instead of itemnum! to refer to the currently selected item.
This command is intended to be used in a multitask program to cause an item to wander around mindlessly on the screen.
**
Example:
*This is an example of a multitask program that causes the item
*to wander around.
:topwander
#Wander("target")
#Branch(:topwander)
* I didn’t use a while loop because multitasking programs cannot
* use them.
Play wav file.**
Related Commands:
#Push, #PushItm
#Wav
**
#Wav(Filename$)
This command opens a Wav file defined in Filename$ and plays it. If you do not specify the .Wav extension, it is added for you. Also, you shouldn’t include any directory information as RPGCode will find that for you.
**
Example:
#Wav("sword.wav")
* Causes the computer to play a Wav file called "sword.wav"
Stop wav file.**
Related Commands:
#MidiPlay, #MediaPlay, #WavStop
#WavStop
**
#WavStop()
This command stops any wave files currently playing.
**
Example:
#Wav("sword.wav")
*Causes the computer to play a Wav file called "sword.wav"
#WavStop()
While-loop.**
Related Commands:
#MidiPlay, #MediaPlay, #Wav
#While
**
#While( ) *condition*
The While command allows you to initiate a While-loop. While-loops in RPGCode work very similar to those in C or C++.
A While-loops is a group of commands that will be executed over and over again until a certain condition is met (a certain variable equals some value).
The is a condition that the While-loop tests before each loop to see if it should keep running (this is very similar to an If statement). For example, you may want the loop to run until the variable done!==1. In this case, the condition would be: done!~=1 (The While loop continues to run while done! isn’t equal to 1). *condition*
Following the While-Loop, you must enclose the statements you wish to run between { and } brackets. They must appear on lines by themselves.
As a final note, you should not run While loops inside multitask programs (items). It takes up too much computing time and might get caught in an infinite loop.
**
Example:
*While-loop example. Before running the While-Loop, check out
*This using #Branch commands:
*Using the #Branch command like this isn’t reccomended at all.
*The code is too hard to read- in programming lingo we call this
*"spaghetti" code.
:top
#MWinCls()
#MWin("What do you want to do?")
#Mwin(" 1- Play")
#Mwin(" 2- Quit")
#Wait(a$)
#If(a$=="1")
#MainFile("game.gam")
#End()
#If(a$=="2")
#Windows()
#End
#Branch(:top)
*Now watch the same thing with a While-loop.
*By using While-loops properly, you can avoid using #Branch
*altogether.
*Let’s say that the loop is done when #done==1
#done!=0
#While(done!~=1)
#MWinCls()
#MWin("What do you want to do?")
#Mwin(" 1- Play")
#Mwin(" 2- Quit")
#Wait(a$)
#If(a$=="1")
#MainFile("game.gam")
#done!=1
*The above will stop the While-Loop.
#If(a$=="2")
#Windows()
#done!=1
*The above will stop the While-Loop.
Win the game.**
Related Commands:
#Branch, #For
#Win
**
#Win()
This command displays a "You beat the game" message in the Message Window, waits for the player to press a key, and then resets the game to the startup program.
This command is used to tell that player that he/she won the game, but you may wish to create more interesting victory sequences, using the command, as well as other graphic oriented commands to show a story sequence for what happens once the game has been beat. You may also show credits with the command. **#Viewbrd** **#Text**
Once the victory sequence has been completed, you may wish to use the command, or you may want to use the command to quit directly to Windows, or use the command to return to the startup program without displaying the "You beat the game" message. **#Win** **#Windows** **#Reset**
**
Example:
* Alright, you beat the game!!!
#Win()
* Ends execution of the program, and resets the game
* to its startup program.
Change Message Window color.**
Related Commands:
#Over, #Reset, #Viewbrd
#WinColor
**
#WinColor(color_code!)
By default, the Message Window has a black background. You can define the color of the message window using this command. color_code! is a numerical value between 0 and 255 that represents a color in the DOS palette.
**
Example:
#MWin("Here we are before the background is changed.")
#WinColor(1)
#MWin("Now with a blue background")
#Wait(a$)
Change Message Window color (RGB).**
Related Commands:
#Bold, #Color, #ColorRGB, #Font, #FontSize, #Italics, #Mwin, #MWinCls, #Underline, #WinGraphic, #WinColorRGB
#WinColorRGB
**
#WinColorRGB(red!, green!, blue!)
By default, the Message Window has a black background. You can define the color of the message window using this command. red!, green! and blue! are numerical values between 0 and 255 that define the concentrations of red, green and blue in the color.
**
Example:
#MWin("Here we are before the background is changed.")
#WinColorRGB(255,0,255)
#MWin("Now with a bright purple background")
#Wait(a$)
Change Message Window graphic.**
Related Commands:
#Bold, #Color, #ColorRGB, #Font, #FontSize, #Italics, #Mwin, #MWinCls, #Underline, #WinGraphic, #WinColor
#WinGraphic
**
#WinGraphic(filename$)
By default, the Message Window has a black background. You can put a graphic in the background by using this command. filename$ is a literal value which specifies the filename of the graphic to place in the Message Window (Bmp or Gif).
**
Example:
#MWin("Here we are before the background is changed.")
#WinGraphic("mwin.bmp")
#MWin("Now with a snazzy graphic!"
#Wait(a$)
Zoom in the screen.**
Related Commands:
#Bold, #Color, #ColorRGB, #Font, #FontSize, #Italics, #Mwin, #MWinCls, #Underline, #WinColor, #WinColorRGB
#Zoom
**
#Zoom(percent!)
This command causes the screen to zoom in. percent! Is a numerical variable that defines the percentage by which the screen should be zoomed in.
**
Example:
#Clear()
#Text(10,10, "Hello")
#For(t!=1;t!<=4;t!=t!+1)
#Zoom(25)
#Wait(a$)
#Return()
**
Related Commands:
#Return
*
Commands Categorized By Task
Below is a list of all the RPGCode commands organized by their tasks.
**
Program Flow
#Branch, #CallShop, #Change, #Done, #End, #Fbranch, #Fight, #For, #Gone, #If, #Method, #Move, #ReturnMethod, #Run, #While
**
Fight Commands
#AttackAll, #DrainAll, #Fight, #FightEnemy, #TargetLocation
**
Manipulate Data (Variables)
#CastInt, #CastLit, #CastNum, #CharAt, #Empty, #GetGP, #Kill, #Random, #ReturnMethod
**
Input/Output
@, #Bold, #CheckButton, #ClearBuffer, #ClearButtons, #Color, #ColorRGB, #DirSav, #Font, #FontSize, #Get, #Italics, #MouseClick, #MouseMove, #Mwin, #MWinCls, #Print, #Prompt, #SetButton, #Show, #Text, #UnderLine, #Wait, #WinColor, #WinColorRGB, #WinGraphic
**
Graphics
#Bitmap, #BorderColor, #Clear, #DrawLine, #DrawRect, #Earthquake, #ErasePlayer, #Fade, #FillRect, #Mem, #Posture, #Push, #Put, #PutPlayer, #Return, #Scan, #SetButton, #SetPixel, #ViewBrd, #Zoom
**
System Commands
#Debug, #Delay, #Dos, #GetCorner, #GoDos, #Include, #Kill, #Load, #MainFile, #Over, #Prg, #Push, #Reset, #ReturnMethod, #RPGCode, #Save, #Send, #Start, #TileType, #Win
**
Character Info and Manipulation
#AddPlayer, #CallPlayerSwap, #DestroyPlayer, #Equip, #ErasePlayer, #GetGP, #GetHP, #GetMaxHP, #GetMaxSMP, #GetSMP, #GiveGP, #GiveHP, #GiveSMP, #HP, #Inn, #MaxHP, #MaxSMP, #NewPlyr, #Posture, #PutPlayer, #Remove, #RemovePlayer, #RestorePlayer, #SMP, #TakeGP, #UnderArrow, #WalkSpeed
**
Item Manipulation
#CreateItem, #DestroyItem, #Equip, #EraseItem, #GiveItem, #ItemCount, #ItemWalkSpeed, #PushItem, #PutItem, #Remove, #TakeItem, #Wander
**
Multimedia
#MediaPlay, #MediaRest, #MidiPlay, #MidiRest, #PlayAvi, #PlayAviSmall, #Wav, #WavStop
