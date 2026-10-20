---
kind: doc
id: "toolkitzone.com/94"
site: "toolkitzone.com"
title: "column"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=94"
written: "2004-12-18T07:20:00"
date_confidence: "exact"
updated: null
captured: ["20050222091919"]
author: "Occasionally_Correct"
repliers: []
authors: ["Occasionally_Correct"]
comments_present: 0
f_author: "Occasionally_Correct"
f_date: "December 18, 2004, 7:20 am"
f_description: "OC continues to outline file manipulation and how it can help you to develop your own save/load system for your game, with code examples included,"
f_title: "Replacing the Systems: Part 2"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_94", captured: "20050222091919", sha256: "2ce04d9cad4da642ffb4eb1968b02a127caa98f6a6e4ee1bcd88e877219521f5", wayback_url: "https://web.archive.org/web/20050222091919/http://www.toolkitzone.com/library.php?mode=read&doc=94"}
---

# column

RPG Code > Tips & Tricks
OC continues to outline file manipulation and how it can help you to develop your own save/load system for your game, with code examples included,
Hi there. OC here, and I've prepared another system for you to replace. Last week, you learned how to use File Manipulation through the File I/O commands. This week, I'll be putting your file manipulation knowledge to work and teach you how to build a very basic save/load system. We'll be using graphics for this article, so if you don't have your own, you can download mine . Now, what is the use of having a custom save/load system? There are plenty of reasons I'm sure you can come up with, so I'll list some of my own. It looks much nicer than just the standard dialog box. Also, it allows you to actually see who's in your party at the time, along with any information about them, without having to load the game. That's always a nice touch. Also, it would allow you to add unlockable features, accessible via the start screen (which, again, can be nice). Right now, we'll stick with the barest of functionality for simplicity and just save and load player 1's profile image and stats. This system will be using four methods (doSave(), doLoad(), saveGameData(), and loadGameData()). We'll be looking into saveGameData() and loadGameData(), first: This is a pretty simple method, if you read last weeks article. It takes one parameter; filename$ (but you won't have to worry about that - doSave() takes care of it). All we're doing is opening a file in output mode (so you can write to it), and then write data into the file. Take a look at the filePrint() commands. First, we print the players name. Next, the HP and max HP of the player are cast to literals via the castLit() command, and are written into the file. Lastly, the amount of GP that the player has. Then we close the file, ending the method. Now we need a method for loading the data so we can show it to the user before they load the game. This is where loadGameData() comes in. This is pretty much the same as the previous method, except it opens the file in input mode, and reads the file (instead of opening it in output mode and writing to it). As expected, this method takes one parameter (filename$). You won't need to worry about this either - doLoad() will take care of it. Moving on, we'll see the two other methods. The first one (doSave()) has the task of asking whether or not the user wants to save, and makes a decision based on user-input. As the comments state, the first thing we need to do is create some local variables (variables that don't need to be kill()'d). key$ is for the users input, and file$ is the file to save to. Next we ask the user what they'd like to do. If the user presses 1, we open up the directory of saved games (using dirSav()), and check if the user clicked cancel or not. If the user didn't click on cancel (and the text field isn't blank), we call the saveGameData() method. It takes 'file$ + "_data.txt"' as it's parameter. That's just the filename of the saved game with an extension (if you look in your Saved folder after running this, it should look something like this: "YourFilename.sav_data"). If the user didn't press 1 when we asked for input, we are forced to show the "angry no message." After this, the method ends. Last but not least, here's the doLoad() method: Again, we create our local variables key$ and file$, which both serve the same purpose as the last method. Then we show our fancy loading graphic on the screen (again, you can download the graphic files ). Now, we open the save/load file dialog and check if the user loaded a game. If so, we call the loadGameData() method, which loads the saved data into some variables for us. Next, we show the data on screen, starting with the profile image. The way this method was written, it is expected that the profile image filename is the name of the player, but you can change that if you would like something different. We then show the name of the player, hp/max hp, and GP. Now we ask the user if this is the right game file to load. If they press 1, it is the right saved game, and we load it (using load()). Else, we show a message, recognizing their choice. After all this is through, we clean up some memory by kill()'ing the variables set by loadGameData(). Since I don't feel like copying and pasting those methods to the last example of the article, let's pretend that we saved them in a file called "SaveLoadSystem.prg." Voila! A working example. There isn't much to explain about it. So instead, why don't you take a look at this screenshot I've prepared of the system in use? You can find it . That's it for today. I hope you enjoyed and learned something from this article. Replacing the custom systems is a great way to spruce up your game, as I've said before. The examples of this weeks system are very basic. You can expand on this idea in many ways. For example, writing the number of players in you party into the file, and the rest of the players stats. That would allow you to retrieve more than just the player you start out with. Input is greatly appreciated. So if you have anything you'd like to say, please do! If there's a certain article you'd like to see in the future, you're welcome to PM me your ideas. **Replacing the internal Systems: The Save/Load System**
**Introduction**
[here](http://www.toolkitzone.com/stuff/files/94/fancy_graphics.zip)
**Examples as usual**
```
method saveGameData(filename$)
{
//Open the file for writing
openFileOutput(filename$, "Saved")
//Some a few stats into the file
filePrint(filename$, playerHandle[0]$)
filePrint(filename$, castLit(getHP(playerHandle[0]$)))
filePrint(filename$, castLit(getMaxHP(playerHandle[0]$)))
filePrint(filename$, castLit(getGP()))
//Close the file
closeFile(filename$)
}
```
```
method loadGameData(filename$)
{
//Open the file for reading
openFileInput(filename$, "Saved")
//Read the data into variables
playerName$ = fileInput(filename$)
playerHP$ = fileInput(filename$)
playerMaxHP$ = fileInput(filename$)
playerGP$ = fileInput(filename$)
//Close the file
closeFile(filename$)
}
```
```
method doSave()
{
//Set up some local variables
local(key$) //The users keypress
local(file$) //The file to save
//Ask if the player would like to save
mwin("Would you like to save your progress?")
mwin("[1] - Yes")
mwin("[2] - No")
key$ = wait()
mwincls()
//Check what they want to do
if(key$ == "1")
{
//The user wanted to save
file$ = dirSav()
if(file$ ~= "CANCEL" && file$ ~= "")
{
//The user didn't cancel
//Save the game data
saveGameData(file$ + "_data.txt")
//Continue saving the actual game
save(file$)
}
}
else
{
//The user didn't want to save
mwin("No? NO?! Ok, then.")
wait()
mwincls()
}
}
```
```
method doLoad()
{
//Set up some local variables
local(key$) //The users keypress
local(file$) //The file to load
//Show some super-fancy graphics
bitmap("fancy_load_graphic.gif")
//Which save does the user want to load?
file$ = dirSav()
if(file$ ~= "CANCEL")
{
//The user didn't cancel
//Load some game data
loadGameData(file$ + "_data.txt")
//Show the information on-screen
setImage(playerName$ + ".gif", 100, 150, 64, 64)
pixelText(100, 220, "Name: " + playerName$)
pixelText(100, 240, "HP: " + playerHP$ + "/" + playerMaxHP$)
pixelText(100, 260, "GP: " + playerGP$)
//Ask if they want to load that game
mwin("Is this the game you would like to load?")
mwin("[1] - Yes")
mwin("[2] - No")
key$ = wait()
mwincls()
//Check what they want to do
if(key$ == "1")
{
//The user wanted to load the game,
//so load the game we shall!
load(file$)
}
else
{
//The user didn't want to load the game
mwin("No? Well, alright.")
wait()
mwincls()
}
}
//Clean up the loaded data
kill(playerName$, playerHP$, playerMaxHP$, playerGP$)
}
```
[here](http://www.toolkitzone.com/stuff/files/94/fancy_graphics.zip)
**A working example**
```
#include("SaveLoadSystem.prg")
doSave()
doLoad()
wait()
```
[here](http://www.toolkitzone.com/stuff/files/94/bob_loading.gif)
**Conclusion**
Occasionally_Correct
December 18, 2004, 11:07 am
For anyone reading, I'd just like to point out that I made a mistake. "if(file$ ~= "CANCEL" && file$ ~= "")" I didn't realize I had left this in here until now. The save/load dialog doesn't let you save or load when the text field is empty. So you can just ignore the 'file$ ~= ""' part. Let's pretend it's not there! :P
Slasher
December 18, 2004, 5:48 pm
...Like always, nice, well thought-out, and informative.
Feb 18, '05
Feb 11, '05
Jan 29, '05
Jan 15, '05
Jan 8, '05
Feb 18, '05
rpg code > tips & tricks
Feb 11, '05
rpg code > tips & tricks
Jan 29, '05
rpg code > tips & tricks
Jan 15, '05
rpg code > tips & tricks
Jan 8, '05
rpg code > tips & tricks
