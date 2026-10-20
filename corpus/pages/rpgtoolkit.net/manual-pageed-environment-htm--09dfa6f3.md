---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/manual/pageed_environment.htm"
site: "rpgtoolkit.net"
title: "[ | ]ToolbarsMenus"
original_url: "http://rpgtoolkit.net/manual/pageed_environment.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20120618021154"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/manual/pageed_environment.htm", captured: "20120618021154", sha256: "7ddcc8a419703e8cf65360d19f5052789793bc078f26d4a3cbdbabc8b01ecc70", wayback_url: "https://web.archive.org/web/20120618021154/http://rpgtoolkit.net/manual/pageed_environment.htm"}
---

# [ | ]ToolbarsMenus

When you launch the Toolkit for the first time the Toolkit splash screen appears followed by a Tip of the Day box, which contains a lot of useful information about the editors and the TK. Upon closing this, you are greeted with a large grey screen with a few toolbars around the edges - not particularly attractive (although that can be changed through the config)!
Editor Basics
The Toolkit editor comprises many editors and other tools for creating all the components of your game. Editors open into the centre of the screen and appear in a tab bar below the main toolbar. In most cases multiple files of the same type can be edited simultaneously with a new editor opening for each file (with the exception of the , since only one game can be edited at a time). The name of the active editor, the current file and the current game are displayed in the program bar at the top of the screen. [Main File Editor](page3.htm)
Files
Most Toolkit games are made up of a large number of different files, all of which are organised into within the Toolkit folder, with a new set of folders created for each new game. These are located in the Toolkit3\Game\gameName folder, the contents of which is displayed in the Toolkit in a file tree located in the right-hand toolbar, from which files can be opened. The one exception is the game's Main File; this file contains all the settings and start-up information for the game and resides in the Toolkit3\Main folder (not visible in the tree). *reserved folders*
As of 3.1.0, files can also be placed in subfolders of the default folders, which enables a better organisation of your files. When you link files to one another in an editor (e.g., when assigning an animation to a character) the Toolkit knows which reserved folder the file should lie in (e.g., board files go in the \gameName\Board folder), and you need only to specify the of the file. If your file is in a subfolder, you need to prefix the subfolder's name (e.g., for the file "gameName\Board\village\village1.brd", specify "village\village1.brd"). When specifying subfolders, only the '\' slash is valid; the '/' is not. *relative path* **Important:**
Most files you make will automatically be placed in the right folder, but sometimes you may want to use files that lie outside this folder system (for instance, music or image files). However, you shouldn't need to do any copying yourself; when you are selecting these files they will be automatically copied to the proper location.
Around the Editor
Toolbars
Main Toolbar
New File - Click the arrow next to this to show a list of new files to create.
Edit Main File - Opens the . [Main File Editor](page3.htm)
Open File - Use this to open any kind of file by browsing.
Save File - Saves the file in the active editor.
Save All - Saves all open files.
Launch the Bard - The Bard is a music playback program that can be used to listen to your game music and sound effects.
Toolkit Online - Opens the Toolkit's in the TK's own internet browser. [homepage](http://toolkitzone.com)
Edit Config - Shows the config screen, where you can choose an image to use as the background for the editor.
Edit Tileset - Launches the . [Tileset Editor](page5.htm#tileset)
Run Game - Launches the currently loaded game. Remember to save any files you're currently working on otherwise your latest changes won't appear when you test run!
Left Toolbar
This toolbar contains the tools associated with the active editor - see each editor page for individual details.
Right Toolbar
Project List - Shows a file tree that lists all the files and folders in the current project (all the files contained in the Toolkit3\Game\gameName folder). Double-click to open a file; if the file isn't a Toolkit file, it should open in its default editor (for instance, *.txt files will open in Notepad). After opening a file this list will auto-collapse. The width of the project list can be altered by click-dragging the left-hand edge of its container.
A number of right-click options are available:
- Open, Rename, Delete: Applies to files only.
- Refresh: Recreates the file tree.
- Collapse All: Closes all open folders.
- Select Into Board Editor: Applies to animated tiles (TANs) when the board editor is active. The selected file is loaded into the tile 'brush' and may be drawn like other tiles.
New Editor - Shows a list of buttons with "Edit..." captions, which open new files in each editor. After opening an editor, this list will auto-collapse.
Tileset Browser - Displays the last opened tileset. A new tileset can be opened with the "Open File" button above the tileset. This tileset browser can be used for selecting tiles in a range of editors, most usefully in the and editors. If the active editor does not make use of the browser, or there is no editor open, clicking a tile will load that tile into a new . The width of the browser can be altered by click-dragging the left-hand edge of its container. [Board](page4.htm) [Tile Bitmap](page11.htm) [Tile Editor](page5.htm)
Menus
File
New Project - Starts a new game. A window is shown that allows you to specify a name for the project, that will appear in the title bar and the *.gam main file and gameName folder (unless otherwise specified). Default files are included with the Toolkit, which are free to use and are placed in the game folders if the option is selected (these files can be found in the demo game folders or in the Game\Basic folders).
New... - Starts a new file of the chosen type.
Open Project - Changes the current game project.
Open - Use this to open any kind of file by browsing.
Save - Saves the file in the active editor.
Save As... - Save the file in the active editor under a different name.
Save All - Saves all open files.
Close - Closes the active editor.
Exit - Quits the Toolkit.
Test Game - Runs the current game (see above).
Select Language - Changes the language used throughout the editor. Note currently only English is available.
Show Splash Screen - Enables/disables the screen shown before the Toolkit opens.
Show Tips - Enables/disables the Tip of the Day feature.
Build
Create Pak File - Packages the game for release and places the game's files into one file called a PAK file that can't be accessed by users. Note this is a feature of version 2 of the Toolkit that has been superseded by a stand-alone executable (see below). Additional details are available . [here](page16.htm#pak)
Make EXE - Packages the game for release into a single executable file (.exe). More information can be found . [here](page16.htm#exe)
Create Setup - Standard method for game release - packages the game in a ZIP file that contains all the game files in the same folder structure as in the Toolkit3 directory. See for more information. [here](page16.htm#setup)
Window
Show/Hide Tools - Shows/Hides the left-hand toolbar.
Show/Hide Project List - Shows/Hides the file list in the right-hand toolbar.
Help
Users' Guide - Shows this manual
Tutorial - Shows a 9 step tutorial for getting started with the Toolkit.
About - Screen containing information about the developers, contributors, and components of the RPGToolkit.
