---
kind: forum-thread
id: "toolkitzone-forum/33217"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "33217"
title: "A problem retaining variable values..."
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=33217"
written: "2006-10-22T03:42:00"
last_post: "2006-11-09T20:33:00"
date_confidence: "exact"
captured: ["20070320195538"]
author: "Steve-o"
repliers: ["Levi"]
authors: ["Steve-o", "Levi"]
posts_present: 5
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_355913", captured: "20070320195538", sha256: "cac1374172fee298889e994a7caa6f611c5f810a4f65025501cd8ec855b3d5ac", wayback_url: "https://web.archive.org/web/20070320195538/http://toolkitzone.com/forum/viewtopic.php?p=355913"}
links: []
---

# A problem retaining variable values...

### Steve-o · 2006-10-22 03:42 · #K355904

I am currently programming my own custom menu.
I have a save and load feature in this menu.
You can only save in one of four slots.
I run an If Statement, to check if there is a save in each of the four slots.
If there is, then the default graphic No_Data.PNG is replaced by another graphic, map location, etc.
The problem is, that when you quit, and restart the game again, the variables are set back to the default value of 0.
So, when I go to load or save a game, No_Data.PNG is still there, even if there is a save.
Can anyone help me with this ordeal?
If so, reply to this.
Thanks. Very Happy

### Levi · 2006-10-22 03:58 · #K355908

Look in the manual for file save routines.
Save the relevant menu info into a file that you load everytime you start the game.
This way the variables are reset as needed.

### Steve-o · 2006-10-22 05:02 · #K355913

I'm not finding anything in the manual about it...
How would I save variables into a file?
And what type of file?
A .prg file??

### Levi · 2006-10-22 05:53 · #K355920

User's Guide, Function reference, IO (Input/Output).
You'll see the following commands.
OpenFileOutput
OpenFileInput
OpenFileBinary
OpenFileAppend
FileInput
FilePut
FilePrint
FileGet
FileEOF
CloseFile.
These are all functions you can use to help yourself there.
Basically each time you save a game and update your menu. Update the file as well.
Here's an example of writing to the file.
Method SaveGameData()
{
OpenFileOuput("SaveData.txt","Misc") //Opens file SaveData.txt in folder Misc for saving
//Next we'll save the status of each save game slot
//replace SaveSlot#status$ with the variable that represents
//each save slot's status.
FilePrint("SaveData.txt", SaveSlot1Status$)
FilePrint("SaveData.txt", SaveSlot2Status$)
FilePrint("SaveData.txt", SaveSlot3Status$)
FilePrint("SaveData.txt", SaveSlot4Status$)
CloseFile("SaveData.txt")
}
And then when you need to retreive the Data for updating the save game slots.
Method GetGameData()
{
OpenFileInput("SaveData.txt","Misc")
//SaveSlot#Status$ once again is the status variable for each
//Saved slot file.
SaveSlot1Status$ = FileInput("SaveData.txt")
SaveSlot2Status$ = FileInput("SaveData.txt")
SaveSlot3Status$ = FileInput("SaveData.txt")
SaveSlot4Status$ = FileInput("SaveData.txt")
ClostFile("SaveData.txt")
}
You call GetGameData() when the game first starts so that you have all of the relevant info you need when the game starts.
And you call SaveGameData() each time the save slots are updated so that the relevant info is up to date.
These aren't fully functional methods for two reasons.
1.) they assume a lot about how you determine the save slot status. You have to edit these as you need.
2.) You need to have the file "SaveData.txt" already made in your Misc folder or else you'll recieve an error.

### Steve-o · 2006-11-09 20:33 · #K359090

Couldn't I do this with a .prg file instead of a .txt file??
I got the variable to save, but I couldn't recall it!
Does anyone have any solutions to this problem?
