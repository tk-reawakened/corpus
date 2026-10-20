---
kind: file
id: "toolkitzone.com/900"
site: "toolkitzone.com"
title: "Comment FORMAT: //"
original_url: "http://www.toolkitzone.com/fileman.php?id=10&file=900"
written: null
date_confidence: "unknown"
updated: null
captured: ["20041117224402", "20041117224409", "20060304191347"]
author: null
repliers: []
authors: []
comments_present: 0
f_name: "Comment FORMAT: //"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_900", captured: "20041117224402", sha256: "f6cccaa737661a1254766aff37729e0cacb6b435ed2364cfb528fd169ba837f8", wayback_url: "https://web.archive.org/web/20041117224402/http://www.toolkitzone.com/fileman.php?id=10&file=900"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_900", captured: "20041117224409", sha256: "f1f49e9a84212969c0d1d9d5b220a5f9983ef352834c41a372cd2eb48c17a38b", wayback_url: "https://web.archive.org/web/20041117224409/http://www.toolkitzone.com/fileman.php?id=5&file=900"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_900", captured: "20060304191347", sha256: "4fb1414d84f7696706d5a651576b199e877b62387b8138f8a91498a466e1e749", wayback_url: "https://web.archive.org/web/20060304191347/http://www.toolkitzone.com/fileman.php?id=3&file=900"}
---

# Comment FORMAT: //

Command Reference
NAME: Comment FORMAT: //
Two slashes tells the computer to ignore the rest of the line. This is used for adding comments to your code. Comments are used as ways of explaining what some parts of a program do. Comments can appear on the same line as a command as long as the comment is to the right side of the command. The * ('asterisk' or 'star') symbol can also be used for commenting programs. The upside to C++ style comments ('//') is that the Toolkit will not mistake it for a math operation (as it does when you use * comments on the same line as an equation).
```
*This is a comment. *It gets ignored by the computer. Mwin("Woo hoo!") //This is another comment. a! = 10 //This is a C++ style comment.
```
NAME: Application Path FORMAT: dest$ = AppPath()
This command retrieves the file path of the RPGToolkit3 and returns it to dest$. - dest$ is the returned path.
```
//Show the application path... Show(AppPath())
```
NAME: ASCII FORMAT: dest! = Asc(char$)
Asc() converts characters to and from ASCII characters. - char$ is the character(s) to replace with an ASCII character(s). - dest! is the returned ASCII.
```
ascii! = Asc(char$)
```
NAME: Auto Local FORMAT: AutoLocal()
This command automatically sets all implicitly declared variables to local scope.
```
AutoLocal()
```
NAME: Character FORMAT: char$ = Chr(char!)
Chr() returns a character to char$ from an ASCII character(s). - char! is the key number to detect.
```
spc$ = Chr(8) //Detects the backspace key. tab$ = Chr(9) //Detects the tab key.
```
NAME: Close a file FORMAT: CloseFile(file$)
Closes an open file opened in either append, input, output, or binary mode. - file$ is the file to close.
```
OpenFileInput("start.brd","Boards") //Opens a file in 'input mode' CloseFile("start.brd") //Close the file
```
NAME: Create Canvas FORMAT: CreateCanvas(sizex!, sizey![, id!])
Creates a canvas of sizex! and sizey! (in pixels), and returns the ID so you can refer to it later. - sizex!, sizey! are the width (x) and height (y) of the canvas. - id! is the id of the canvas.
```
cnvTitle! = CreateCanvas(64, 64) //Create a new canvas... Bitmap("title.bmp", cnvTitle!) //Put an image in the canvas. DrawCanvas(cnvTitle!, 0, 100) //Draw the canvas on screen. KillCanvas(cnvTitle!) //Now, kill the canvas once I'm done with it.
```
NAME:Create Cursor Map FORMAT: id! = CreateCursorMap()
A Cursor Map is a mini-menu that the user can create. It allows the user to specify a spot on the screen where a pointer image will appear, letting them scroll through options with the keyboard. - id! is the id of the cursor map.
```
PixelText(300, 180, "New Game") PixelText(300, 210, "Load Game") PixelText(300, 230, "Quit") done! = 0 While(done! == 0) { cMap! = CreateCursorMap() //Create a cursor map with the id cMap! //Set where the cursor can go to... CursorMapAdd(295, 180, cMap!) CursorMapAdd(295, 210, cMap!) CursorMapAdd(295, 230, cMap!) res! = CursorMapRun(cMap!) //Run the selected cursor map position KillCursorMap(cMap!) //Kill the cursor map id } Switch(res!) { Case(0) { //New game } Case(1) { //Load game } Case(2) { //Quit } }
```
NAME: Cursor Map Add FORMAT: CursorMapAdd(x!, y!, id!)
Adds a new cursor map position. Use this to specify where the pointer image can go on the screen. When the user presses an arrow key on the keyboard, the cursor will 'jump' to the next/previous map (if one exists). - x!, y! are the x and y coordinates (in pixels) to place the cursor. - id! is the id of the cursor map.
```
PixelText(300, 180, "New Game") PixelText(300, 210, "Load Game") PixelText(300, 230, "Quit") done! = 0 While(done! == 0) { cMap! = CreateCursorMap() //Create a cursor map with the id cMap! //Set where the cursor can go to... CursorMapAdd(295, 180, cMap!) CursorMapAdd(295, 210, cMap!) CursorMapAdd(295, 230, cMap!) res! = CursorMapRun(cMap!) //Run the selected cursor map position KillCursorMap(cMap!) //Kill the cursor map id } Switch(res!) { Case(0) { //New game } Case(1) { //Load game } Case(2) { //Quit } }
```
NAME: Change Cursor Map Hand FORMAT: CursorMapHand(file$[, stretchYN!])
Changes the hand image used on the menu, cursor maps, etc. to the specified file. Optionally, you can stretch it to 32x32 pixels. To change the hand to the original image, type "Default" instead of a filename. - file$ is the filename of the image to use. - stretchYN! is an optional parameter used to stretch the image.
```
CursorMapHand("hand.bmp") //Set a new cursormap hand
```
NAME: Cursor Map Run FORMAT: dest! = CursorMapRun(id!)
Runs the currently selected cursor map position. Returns the index of the selected cursor map position. - id! is the id of the cursor map. - dest! is the selected cursor map.
```
PixelText(300, 180, "New Game") PixelText(300, 210, "Load Game") PixelText(300, 230, "Quit") done! = 0 While(done! == 0) { cMap! = CreateCursorMap() //Create a cursor map with the id cMap! //Set where the cursor can go to... CursorMapAdd(295, 180, cMap!) CursorMapAdd(295, 210, cMap!) CursorMapAdd(295, 230, cMap!) res! = CursorMapRun(cMap!) //Run the selected cursor map position KillCursorMap(cMap!) //Kill the cursor map id } Switch(res!) { Case(0) { //New game } Case(1) { //Load game } Case(2) { //Quit } }
```
NAME: Debugger Message FORMAT: Debugger(text$)
Calls the debug window with a message inside of it. A very useful command for error handling. To use the debug window, debugging must be enabled. - text$ is the message to be placed inside of the debug window.
```
Method FileExists(file$, folder$) { //Declare the variable 'exists!' Local(exists!) //Assume the file exists exists! = 1 On Error Goto :error //Try to open the file. If it doesn't exist, //it will cause an error. OpenFileInput(file$, folder$) //Close the file just incase it was opened, but //don't trigger another error. On Error Resume Next CloseFile(file$) //Return the result ReturnMethod(exists!) //End the method so the error handler isn't run End() :error //If we get here, there was an error exists! = 0 Resume Next } If(FileExists("SomePrg.prg","Prg") == 1) { Mwin("There was no error!") } Else() { Debugger("Error opening file!") }
```
NAME: Draw Canvas FORMAT: DrawCanvas(id!, x!, y![, sizex!, sizey!, destId!])
Draws a canvas to the screen or to another canvas. - id! is the id of the canvas. - x!, y! are the x and y coordinates to draw the canvas to. - sizex!, sizey! (if specified) are the width and height (in pixels) to scale the canvas to. - destId! (if specified) is the destination id to draw the canvas to.
```
cnvTitle! = CreateCanvas(64, 64) //Create a new canvas... Bitmap("title.bmp", cnvTitle!) //Put an image in the canvas. DrawCanvas(cnvTitle!, 0, 100) //Draw the canvas on screen. KillCanvas(cnvTitle!) //Now, kill the canvas once I'm done with it.
```
NAME: Else FORMAT: Else()
The Else command executes a block of code inside it's opening and closing braces as long as the preceeding If statement and/or ElseIf statement is false.
```
If(x! == 12) { Mwin("x! is 12") } ElseIf(x! < 12) { Mwin("x! is less than 12") } Else() { Mwin("x! is higher than 12") }
```
NAME: Else If FORMAT: ElseIf()
The ElseIf command executes a block of code inside it's opening and closing braces as long as it's true. However, it will not execute if the preceeding If statements condition's are true. If you have more than one ElseIf statement, only one will run.
```
If(x! == 12) { Mwin("x! was 12") } ElseIf(x! == 15) { Mwin("x! was 15") } Else() { Mwin("x! was neither 12 nor 15!") }
```
NAME: End Animation FORMAT: EndAnimation(id!)
Ends execution of an animation started with the Animation() or SizedAnimation() commands. - id! is the ID of the animation to end.
```
EndAnimation(anmID!)
```
NAME: End of File FORMAT: dest! = FileEOF(file$)
Checks to see if the end of an open file has been reached. If so, it returns 1. If not, it returns 0. The supported mode for this command is "input mode". - file$ is the file to check. - dest! is the returned value.
```
OpenFileInput("mymethods.prg","Prg") //Opens a file in input mode dest! = FileEOF("mymethods.prg") //Has the end of the file been reached? CloseFile("mymethods.prg") //Close the file when done
```
NAME: File Get FORMAT: dest! = FileGet(file$)
Gets binary data from a file. The supported mode for this command is "binary mode". - file$ is the file to check. - dest! is the returned data.
```
OpenFileBinary("mymethods.prg","Prg") //Opens a file in binary mode dest! = FileGet("mymethods.prg") //Get some data from the program! CloseFile("mymethods.prg") //Close the file when done
```
NAME: File Input FORMAT: dest$ = FileInput(file$)
Returns data from an open file. The supported mode for this command is "input mode". - file$ is the file to get input from. - dest$ is the returned value.
```
OpenFileInput("mymethods.prg","Prg") //Opens a file in input mode dest$ = FileInput("mymethods.prg") //Return data CloseFile("mymethods.prg") //Close the file when done
```
NAME: File Print FORMAT: FilePrint(file$, data$)
Prints data into a file. The supported mode for this command is "append mode". - file$ is the file to append to. - data$ is the data to append to the file.
```
OpenFileAppend("mymethods.prg","Prg") //Opens a file in append mode FilePrint("mymethods.prg", "yay") //Print this data to the file CloseFile("mymethods.prg") //Close the file when done
```
NAME: File Put FORMAT: FilePut(file$, data$)
Puts binary data into a file. The supported mode for this command is "binary mode". - file$ is the file to put binary data in. - data$ is the data to put into the file.
```
OpenFileBinary("mymethods.prg","Prg") //Opens a file in input mode FilePut("mymethods.prg",binarydata$) //Put this binary data in the file CloseFile("mymethods.prg") //Close the file when done
```
NAME: Game Speed FORMAT: GameSpeed(speed!)
The new GameSpeed command replaces #WalkSpeed, #CharacterSpeed, #ItemWalkSpeed, and #BattleSpeed. You no longer have to set up all of these commands in order to have the game run as fast or slow as you want. Just use GameSpeed() - speed! is a numeric value between 0 and 3. 0 being the slowest, and 3 being the fastest.
```
GameSpeed(0) //Sets the speed of the game to slow.
```
NAME: Get Board Name FORMAT: dest$ = GetBoardName()
This command gets the board name and stores it in dest$ for later use.
```
boardName$ = GetBoardName()
```
NAME: Get Item Cost FORMAT: dest! = GetItemCost(filename$)
Gets the buying price of an item and returns it to dest!. - filename$ is the filename of the item. - dest! is the returned value.
```
dest! = GetItemCost("my_item.itm") Mwin("This item costs .") Wait() Mwincls()
```
NAME: Get Item Description FORMAT: dest$ = GetItemDesc(filename$)
Gets the description of an item and returns it to dest$. - filename$ is the filename of the item. - dest$ is the returned value.
```
dest$ = GetItemDesc("my_item.itm") Mwin("Item ") Wait() Mwincls()
```
NAME: Get Item Name FORMAT: dest$ = GetItemName(filename$)
Gets the handle (name) of an item and returns it to dest$. - filename$ is the filename of the item. - dest$ is the returned value.
```
dest$ = GetItemName("my_item.itm") Mwin("You have recieved !") Wait() Mwincls()
```
NAME: Get Item Selling Price FORMAT: dest! = GetItemSellPrice(filename$)
Gets the selling price of an item and returns it to dest!. - filename$ is the filename of the item. - dest! is the returned value.
```
dest! = GetItemSellPrice("my_item.itm") Mwin("You may sell this item for .") Wait() Mwincls()
```
NAME: Get Thread ID FORMAT: id! = GetThreadID()
Gets the thread id of the currently running multitask program. This is useful when you want to kill a thread. - id! is the id of the thread to return.
```
tID! = Thread("mythread.prg", 0) //Run the thread "mythread.prg" KillThread(tID!) //Kill the thread when done
```
NAME: Create Global Variable FORMAT: Global(varName[, value])
By default, the Toolkit sets all variables to Global scope. Global variables can be read from anywhere in your game unless you Kill() them. If you create a variable with the Local() command and you meant to create it globally, you can use the Global() command to re-declare it as global. - varName is the name of the variable. - value is the value to assign to the variable.
```
AutoLocal() //Since I've specified that all implicitly delcared variables //are automatically 'local', I'll need to use Global() to make //a global variable. Global(x!) //Declare the x! as global
```
NAME: In String FORMAT: dest! = InStr(string1$, string2$)
Checks to see if there is an occurance of one part of a string inside of another and returns either 1 or 0 to dest!. - string1$ is the first string. - string2$ is the string to compare string1$ to. - dest! is the outcome. Returns 1 if there is an occurance of string1$ in string2$. Returns 0 if there isn't.
```
dest! = InStr("Hello world!", "Hello") //Finds out if there is any similarities in sometext1$ //and sometext2$. If there is, it returns 1. If not, it //returns 0. Mwin("Look at that, sometext1$ and sometext2$ both have the word") Mwin("Hello in them. That means InStr will return 1!") Mwin("I'll prove it: . See?!") Wait() Mwincls()
```
NAME: Kill Canvas FORMAT: KillCanvas(id!)
Kills a canvas id. Remember that you should always kill a canvas when you're done with it, because canvases take up a lot of memory and can easily slow your game down. - id! is the id of the canvas.
```
cnvTitle! = CreateCanvas(64, 64) //Create a new canvas... Bitmap("title.bmp", cnvTitle!) //Put an image in the canvas. DrawCanvas(cnvTitle!, 0, 100) //Draw the canvas on screen. KillCanvas(cnvTitle!) //Now, kill the canvas once I'm done with it.
```
NAME: Kill Cursor Map FORMAT: KillCursorMap(id!)
Kills a cursor map specified by id!. Use this when you're done with your cursor map. - id! is the id of the cursor map to kill.
```
PixelText(300, 180, "New Game") PixelText(300, 210, "Load Game") PixelText(300, 230, "Quit") done! = 0 While(done! == 0) { cMap! = CreateCursorMap() //Create a cursor map with the id cMap! //Set where the cursor can go to... CursorMapAdd(295, 180, cMap!) CursorMapAdd(295, 210, cMap!) CursorMapAdd(295, 230, cMap!) res! = CursorMapRun(cMap!) //Run the selected cursor map position KillCursorMap(cMap!) //Kill the cursor map id } Switch(res!) { Case(0) { //New game } Case(1) { //Load game } Case(2) { //Quit } }
```
NAME: Kill Thread FORMAT: KillThread(id!)
Stop execution of a multitask program (thread). - id! is the id of the thread to kill.
```
tID! = Thread("mythread.prg", 0) //Run the thread "mythread.prg" KillThread(id!) //Kill the thread when done
```
NAME: Lower Case FORMAT: dest$ = LCase(string$)
Casts a string of characters to all lower-case characters and returns it to dest$. - string$ is the string of characters to cast to lower-case. - dest$ is the returned string.
```
string$ = Prompt("What's your name?") name$ = LCase(string$) Mwin("Hello, ")
```
NAME: Left FORMAT: Left(text$, amount!)
Takes characters from the left side of a string. - text$ is the text to take characters from. - amount! is the number of characters to take from the left side of text$.
```
Show( Left("I love you!", 4) + "athe" + Right("I love you!", 5) ) //Result: "I loathe you!" Wait()
```
NAME: Length FORMAT: dest! = Length(string$)
Gets the length of a string and returns the value to dest!. - string$ is the text to get the length of. - dest! is the number of characters in the string.
```
dest! = Length("Hello!") //Finds out how many characters are in the string //"Hello!". A string is just a fancy way to say //text. Mwin("There are characters in the string 'hello!'") Wait() Mwincls()
```
NAME: Create Local Variable FORMAT: Local(varName[, value])
By default, the Toolkit sets all variables to Global scope. Global variables can be read from anywhere in your game unless you #Kill them. With the #Local command, you can create a local variable which will only be accessible in the program that you declare it in. When the program ends, the variable will be destroyed. - varName is the name of the variable. - value is the value to assign to the variable.
```
Local(x!) //Create a local variable x!
```
NAME: Mid FORMAT: dest$ = Mid(string$, start!, length!)
Finds characters in a string starting at start! and ending at length!. It then returns it to dest$. - string$ is the string of characters to search in. - start! is the starting character position. - length! is the ending character position. - dest$ is the returned string.
```
newString$ = Mid("Awesome", 4, Length("Awesome")) Show(newString$) //Shows: "some" in the message window.
```
NAME: Message Box FORMAT: dest! = MsgBox(text$[, title$, type!, textColor!, bgColor!, bgPic$])
Pops up a message box with a combination of buttons. It then returns a number depending on which button was pressed. - text$ is the message to appear in the box. - type! is the type of button combintation. Check below the example for a list of combinations. - textColor! is the color of the text. - bgColor! is the background color of the box. - bgPic$ is an optional parameter for a background image in the message box. The different 'types' of message box bottom combinations are as follows: 0 - diplays 'OK' only. 1 - displays 'Yes' and 'No'. The returned values are as follows (the returned value depends on what the user pressed): 'OK' returns 1. 'Yes' returns 6. 'No' returns 7.
```
//Shows a message box where you can //only choose 'ok'. Heh heh... ret! = MsgBox("Aren't these message boxes cool?", "MsgBox", 0)
```
NAME: Multi-Run FORMAT: MultiRun() { }
*commands*
This command runs multiple commands in a thread without the thread losing control. - is the block of code to run.
*commands*
```
//MultiRun() will execute all commands before //handing control over to something else. MultiRun() { SomeMethod() AnotherMethod() }
```
NAME: Check if player is On Board FORMAT: dest! = OnBoard(pNum!)
This command checks to see if the player is on the board. - pNum! is the slot of the player (0 - 4) - dest! is the returned value. 1 is returned if the player is on the board, 0 if not.
```
If(OnBoard(0) == 0) { PutPlayer(playerHandle[0]$, 3, 5, 1) }
```
NAME: On Error Go to Label FORMAT: On Error Goto :label_name
Branches to a label inside of a method when an error occurs. When you branch to an error using the On Error command, do not resume the program normally. Use "Resume Next" to resume the line of code after the error. - :label_name is the name of the label to branch to. The labels must be inside of the method and you must not indent the labels.
```
Method FileExists(file$, folder$) { //Declare the variable 'exists!' Local(exists!) //Assume the file exists exists! = 1 On Error Goto :error //Try to open the file. If it doesn't exist, //it will cause an error. OpenFileInput(file$, folder$) //Close the file just incase it was opened, but //don't trigger another error. On Error Resume Next CloseFile(file$) //Return the result ReturnMethod(exists!) //End the method so the error handler isn't run End() :error //If we get here, there was an error exists! = 0 Resume Next } If(FileExists("SomePrg.prg","Prg") == 1) { Mwin("There was no error!") } Else() { Debugger("Error opening file!") }
```
NAME: On Error Resume Next FORMAT: On Error Goto :label_name
If you use this command, any errors after this line of code will be "nullified" per se. It will act as if there was no error and resume the next line of code.
```
Method FileExists(file$, folder$) { //Declare the variable 'exists!' Local(exists!) //Assume the file exists exists! = 1 On Error Goto :error //Try to open the file. If it doesn't exist, //it will cause an error. OpenFileInput(file$, folder$) //Close the file just incase it was opened, but //don't trigger another error. On Error Resume Next CloseFile(file$) //Return the result ReturnMethod(exists!) //End the method so the error handler isn't run End() :error //If we get here, there was an error exists! = 0 Resume Next } If(FileExists("SomePrg.prg","Prg") == 1) { Mwin("There was no error!") } Else() { Debugger("Error opening file!") }
```
NAME: Open File in Append mode FORMAT: OpenFileAppend(file$, folder$)
Opens a file in append mode. Append mode writes to the end of a file specified by file$. If the file does not exist, it will be created. - file$ is the file to open. - folder$ is the game folder to get the file from.
```
OpenFileAppend("start.brd","Boards") //Opens a file in 'append mode' CloseFile("start.brd") //Close the file
```
NAME: Open File in Binary mode FORMAT: OpenFileBinary(file$, folder$)
Opens a file in binary mode. Binary mode accesses a file as binary. If the file does not exist, it will be created. - file$ is the file to open. - folder$ is the game folder to get the file from.
```
OpenFileBinary("start.brd","Boards") //Opens a file in 'binary mode' CloseFile("start.brd") //Close the file
```
NAME: Open File in Input mode FORMAT: OpenFileInput(file$, folder$)
Opens a file in input mode. Input mode reads blocks of code in a program starting from the top and ending at a line break (a space between two blocks of code). - file$ is the file to open. - folder$ is the game folder to get the file from.
```
OpenFileInput("start.brd","Boards") //Opens a file in 'input mode' CloseFile("start.brd") //Close the file
```
NAME: Open File in Output mode FORMAT: OpenFileOutput(file$, folder$)
Opens a file in output mode. Output mode overwrites any existing data in the file. If the file does not exist, it will be created. - file$ is the file to open. - folder$ is the game folder to get the file from.
```
OpenFileOutput("start.brd","Boards") //Opens a file in 'output mode' CloseFile("start.brd") //Close the file
```
NAME: Pixel Movement FORMAT: PixelMovement(ON/OFF)
This command turns pixel movement for players and items on and off. - ON/OFF is a literal value that can be either "ON" or "OFF".
```
PixelText("on")
```
NAME: Pixel Text FORMAT: PixelText(x!, y!, text$[, cnvId!])
This command displays text on the screen the same way the Text() command does, except it uses pixel coordinates. The color of the text is defined with the ColorRGB() command. - x!,y! are the x and y coordinates on the screen to place the text. - text$ is the text to display on the screen. - cnvId! is an optional parameter to draw the text to a canvas.
```
PixelText(100, 100, "This text is at the pixel coordinates: 100, 100")
```
NAME: Render Screen FORMAT: RenderNow(on/off)
When you start a game with the Toolkit, a canvas is created called 'cnvRenderNow!'. This command will constantly render that canvas, meaning you can constantly render custom HP bars for a real-time effect, and other things. Note that this command only works for the cnvRenderNow! canvas. - on/off can either be on or off.
```
RenderNow(on)
```
NAME: Replace FORMAT: dest$ = Replace(expression$, find$, replace$)
The Replace command replaces the specified character(s) in find$ with replace$. It then returns the string to dest$. - expression$ is the string of text in which to find the characters defined with find$. - find$ are the characters in expression$ to replace. - replace$ is what will replace the characters in find$. - dest$ is the returned string of characters.
```
var$ = "newVar$" Show(var$) //Shows the value "newVar$" dest$ = Replace(var$, "$", "!=1") RPGCode(dest$) Show(newVar!) //Shows the value 1 Wait()
```
NAME: Restore Screen Array FORMAT: RestoreScreenArray(pos![, x1!, y1!, x2!, y2!, xdest!, ydest!])
Restores a screen from the screen buffer array. All parameters after pos! are optional. If they leave them out, it will restore the entire screen from the buffer position. - pos! is the array position to restore the screen from. - x1!,y1! are the starting coordinates (from left and from top) on the screen (in pixels) to draw from. - x2!,y2! are the ending coordinates on the screen to draw from. - xdest!,ydest! are the coordinates to draw to.
```
SaveScreen(0) //Save the screen... Push("W,N,N,N") //Now change the screen by pushing the character. RestoreScreenArray(0) //Restore the entire screen.
```
NAME: Resume Next Line FORMAT: Resume Next
Resumes the next line of code after branching to a label with On Error.
```
Method FileExists(file$, folder$) { //Declare the variable 'exists!' Local(exists!) //Assume the file exists exists! = 1 On Error Goto :error //Try to open the file. If it doesn't exist, //it will cause an error. OpenFileInput(file$, folder$) //Close the file just incase it was opened, but //don't trigger another error. On Error Resume Next CloseFile(file$) //Return the result ReturnMethod(exists!) //End the method so the error handler isn't run End() :error //If we get here, there was an error exists! = 0 Resume Next } If(FileExists("SomePrg.prg","Prg") == 1) { Mwin("There was no error!") } Else() { Debugger("Error opening file!") }
```
NAME: Right FORMAT: Right(text$, amount!)
Takes characters from the right side of a string. - text$ is the text to take characters from. - amount! is the number of characters to take from the right side of text$.
```
Show( Left("I love you!", 4) + "athe" + Right("I love you!", 5) ) //Result: "I loathe you!" Wait()
```
NAME: Set Constants FORMAT: SetConstants()
Updates the values of the constants in the RPGToolkit. The 'constants' are the reserved variables which are automatically created for you. For a list of the reserved variables, check the RPGCode Primer.
```
//A useful example of using the SetConstants() command. //Updates the player location and returns it to you. Method GetPlayerCoords(slot!, px!, py!) { SetConstants() px! = playerx[slot!]! py! = playery[slot!]! ReturnMethod(px!) ReturnMethod(py!) Kill(slot!, px!, py!) }
```
NAME: Change Shop Colors FORMAT: ShopColors(pos!, r!, g!, b!)
This command changes the colors of the shop window. - pos! is the area to change. 0 for background, 1 for foreground. - r!,g!,b! are the RGB color values used to change the color of the window.
```
ShopColors(0, 0, 0, 0) ShopColors(1, 255, 255, 255) CallShop("sword.itm", "potion.itm")
```
NAME: Split FORMAT: Split(text$, delimiter$, array[])
Splits a string of text into a new array when it reaches the string delimiter. - text$ is the text to split. - delimiter$ is the the point in text$ where it gets split into a new array. - array[] is the name of the array to use to store the split text.
```
Split("Nice to see you again!", " ", "nice[]$") //This stores "Nice" in the array 'nice[0]$', //"to" in the array 'nice[1]$', etc. //The delimiter is " " (a space), so each word //is split into a different array.
```
Note: the array name must be in quotation marks for it to work.
NAME: Switch FORMAT: Switch(var! or var$ or command())
The Switch command makes checking for true conditions even easier than using a bunch of If statements. It uses 'Cases' to check for values. - var!, var$, or command() is the parameter for checking.
```
Switch(x!) { Case(1) { //If x! is equal to 1, do this //block of code. Show(x!) } Case(Else) { Mwin("x! was not 1) } }
```
NAME: Tell Thread FORMAT: return = TellThread(id!, command$)
This command lets you run a command or method inside of the currently running multitask program (or "threaded" program) from an outside program. - id! is the id of the thread. - command$ is the RPGCode command or method to run. - return is an optional parameter which can be either literal or numeric that returns a value from the command that was passed into the thread.
```
tID! = Thread("mythread.prg", 0) //Run the thread "mythread.prg" ret! = TellThread(id!, "Talk()") //Runs the method "Talk()" //and returns a value. KillThread(tID!) //Kill the thread when done
```
NAME: Thread FORMAT: id! = Thread(program$, persist!)
This command runs a multitasking program (or "threaded" program), which means the player can still walk around and interact while the program is running. - program$ is the multitask program to run. - persist! is a numeric value between 0 and 1. If 0, the thread will stop when the player leaves the board. If 1, the thread will loop and run when the player is on another board too. - id! is an optional parameter that holds the returned ID of the thread.
```
id! = Thread("my_program.prg", 0) //Sets the multitask program "my_program.prg". //Only runs while player is on the board.
```
NAME: Thread Sleep FORMAT: ThreadSleep(id!, duration!)
This stops a multitask program (thread) for a certain amount of time specified by duration!. - id! is the id of the thread. - duration! is the time (in seconds) for the thread to sleep.
```
id! = Thread("mythread.prg", 0) //Run the thread "mythread.prg" ThreadSleep(id!, 60) //Make the thread sleep for 60 seconds //Oh no, an event came up! Wake up the thread! ThreadWake(id!) KillThread(id!) //Kill the thread when done
```
NAME: Thread Sleep Remaining FORMAT: remain! = ThreadSleepRemaining(id!)
Gets the time (in seconds) that remains until a sleeping thread wakes up. - id! is the id of the thread. - remain! is a returned value that stores the remaining time.
```
id! = Thread("mythread.prg", 0) //Run the thread "mythread.prg" ThreadSleep(id!, 60) //Make the thread sleep for 60 seconds tSeconds! = ThreadSleepRemaining(id!) //Get the seconds remaining KillThread(id!) //Kill the thread when done
```
NAME: Thread Wake FORMAT: ThreadWake(id!)
Makes a sleeping thread 'wake up' and become active once again. - id! is the id of the thread.
```
id! = Thread("mythread.prg", 0) //Run the thread "mythread.prg" ThreadSleep(id!, 60) //Make the thread sleep for 60 seconds //Oh no, an event came up! Wake up the thread! ThreadWake(id!) KillThread(id!) //Kill the thread when done
```
NAME: Trim FORMAT: dest$ = Trim(text$)
Trims tabs and/or spaces off of the ends of a string of text. - text$ is the text to trim the spaces/tabs off of. - dest$ is the returned trimmed text.
```
someText$ = " La la la. " someText$ = Trim(someText$) Wait() //Trims the sides of the string so it'll look //like this: "La la la." //Example 2: Show( Trim("Yay! ") ) //Shows "Yay" instead of "Yay! ".
```
NAME: Upper Case FORMAT: dest$ = UCase(string$)
Casts a string of characters to all upper-case characters and returns it to dest$. - string$ is the string of characters to cast to upper-case. - dest$ is the returned string.
```
string$ = Prompt("What's your name?") dest$ = UCase(string$) Mwin("Hello, ")
```
NAME: Until FORMAT: Until(condition) { commands }
This command acts almost the same way as a While loop does. It loops through a block of commands until a condition is met. - condition is the condition to meet to break the loop. - commands is the block of code to run.
```
//Example of the Until Loop. //Leaving the variable alone as the condition //is the same as 'Until(done! == 1)'. Until(done!) { var!++ //Increment var! Show(var!) If(var! > 1) { done! = 1 //Break out of the loop. } }
```
NAME: With FORMAT: With(file$)
This command allows you to use methods from within a file without having to include the file directly, or use implicit includes. Instead, you specify which file to use methods from and access them by typing a period ('.') followed by the name of the method. - file$ is the name of the file.
```
With("System") { Mwin("Just testing the With command!") .Pause() }
```
