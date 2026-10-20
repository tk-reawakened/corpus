---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/manual/page3.htm"
site: "rpgtoolkit.net"
title: "Project settings"
original_url: "http://rpgtoolkit.net/manual/page3.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20120618200808"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/manual/page3.htm", captured: "20120618200808", sha256: "5d1c53188adf4257f8389ab5b6817d2a76ecaecc93d004fcb2e9e3d08ccd2e64", wayback_url: "https://web.archive.org/web/20120618200808/http://rpgtoolkit.net/manual/page3.htm"}
---

# Project settings

A game's main file (*.gam) contains the all the information and settings to start up your game. A game's main file is located separately from the rest of the game's folders in the \Toolkit3\Main folder, along with any others.
Project settings
Project Name — The name of the game. This name appears in the title bar of the engine during gameplay.
Project Path — The location of the game files within the \Toolkit3 directory.
Enable Joystick — A joystick can be used to control the player and navigate the menus instead of or as well as the keyboard.
Cursor Sounds — You can assign sounds effects from the \Media folder to the listed cursor (mouse) actions.
Use Keyboard — Toggles use of the keyboard for player movement. Key assignments must be made on the adjacent grid for each direction.
Use Mouse — Toggles use of the mouse for player movement.
Allow Diagonal Movement — Toggles the feature where diagonal movement can be caused by attempting to move in two 'axial' directions on the keyboard.
Startup info
Initial Board File — The first board the player appears on. This board is loaded immediately after the start program finishes running; if you wish to load a board during the start program (using the Send() command) that persists when it ends, you can leave this field empty.
Note: Make sure you set a start location for your player on the board, otherwise your player may not appear in the location you wish! ( > Board Settings > Set Player Position). You can only set the player start position if the board is specified as the Initial Board File. [Board Editor](page4.htm)
Initial Character File — The main player in the game; the player that is controlled by the user at the start. This must be set before running the game or the game will not work!
Additional Speed Adjustment — This slider controls the overall speed of movement in the game, relative to the speeds assigned to each individual character or item. Since it is possible to give each object its own speed, you should not need to use this setting when testing your game; instead it is intended to be used by the player to adjust the speed on their machine during the game (for instance, through a run-time key or menu option).
The setting takes values from -4 to +4, where negative numbers decrease (-10% per step) and positive increase gamespeed (+10%). This setting is equivalent to the GameSpeed() command, which takes the same argument.
Note: if movement is slow even with low individual walk delays (or you have a low fps), increasing this value will increase the movement speed, since your computer will already be running as fast as it can — to the contrary it can cause some adverse movement problems. More information can be found . ***not*** [here](page23.htm#faq_4.2)
Movement Style — The minimum step by which players and items move around the board. Tile movement refers to old-style block movement, where a single step takes a player to the next tile. Pixel movement reduces the minimum step to a pixel value determined by the frame rate (down to one pixel per step).
If you select pixel movement, an option becomes available to use movement commands in pixel increments — that is, to move players and items in quarter-tile increments or full tile. This option is controlable through the PixelMovement() command.
Mouse Cursor — The Toolkit gives you the option to create a custom mouse icon from an image file or tile. First you must choose the required option from the radio buttons at the bottom of the window — "Default" (blue arrow), "None" (no cursor) or "Custom" — other buttons only become live when you select Custom. The text box specifies the file to be used.
Default Pathfinding Algorithm — The advent of vector collision and true pixel based movement facilitate a number of movement styles when pathfinding. The differences between the options are most readily observed when moving the player using the mouse. This setting affects ItemPath(), ItemPath(), but not Pathfind() or Wander(). See the .
- Axial - Possible paths are confined to the axes of the board (e.g., North-South and East-West) and path points are restricted to tile centres.
- Diagonal - Possible paths are confined to the axes and diagonals and path points are restricted to tile centres.
- Vector - Paths may follow any direction (angle, or orientation) and visit any coordinates.
RPGCode
Run-time Program — this a program that can be run at any point during the game by pressing a certain "run-time" key (see below). For instance, the main menu is a run-time program with a reserved key, that can be accessed at any time. (Optional)
Startup Program — the first program run in your game, every time it starts. A place to put start menus and intro sequences. (Required for the game to work!)
Game Over Program — This is run after a battle when your player's health reaches zero.
Run-time Program Activation Key — The key to press to run the program assigned in the above field. Selecting "More" will bring up a window of extended run-time keys — you can set up as many as 50 other run-time programs this way (not all keys on the keyboard can be used).
Built-in Menu Activation Key — To launch the default menu.
General Activation Key — The key for interacting with objects in the game; for instance talking to an NPC or opening a chest (for which you need to select the "Player presses activation key beside item" option when setting an item on the board — see ). [Board Editor](page4.htm)
Fighting
The option here disables or enables fighting throughout the game (you also need to enable fighting on each board you want it on). The "More" button shows the window that controls the main aspects of fighting.
Enemy Skill Level — The listbox shows the enemies that can be randomly encountered in the game. To add an enemy (.ene file that must have been created — see ), double-click an empty slot. For each enemy you must assign a Skill Level in the adjacent text box. This is the level that the player must achieve before he is able to encounter this type of enemy. [Enemy Editor](page9.htm)
Fighting Type — This defines how often standard battles occur. "Planned" battles occur after an exact number of steps, as specified in the text box. "Random" battles do not have an exact gap in between, but every move there is a probability of fighting, again set in the text box.
Built-In Fighting System — The Toolkit comes with a (the "tk3fight.dll" plugin in the Game\Plugins folder and set in the Plugin tab — see below), but many people write their own or download them, either in or using the TK Plugin SDKs. If you have an RPGCode battle system you can specify it here. [default battle system](page15.htm#bs) [RPGCode](page17.htm)
Graphics
Colour Depth — A higher bit depth corresponds to more a bigger range of colours. The game engine tends to run faster in 16- or 32-bit colour; note however that this setting only takes effect in full screen mode — in windowed mode the colour depth will not change from its "desktop" setting.
Screen Style — Generally, fullscreen mode is faster than windowed.
Resolution / Custom — Lower screen resolutions are generally faster. Note that custom resolutions may not be supported by all video cards, and may cause problems (especially in fullscreen mode).
Frames-per-second option — Tick this to display the fps (frames per second) in the title bar (only visible in full-screen mode). This is only a measure of the speed during movement (not during programs or menus). A low fps (< 20) is indicative of slow movement and you may not notice an increase in walking speed above the default setting (nor will GameSpeed() help).
Draw board vectors — Toggles drawing of board vectors (e.g., collision, program...) in-game. The particular colours are unchangable; this feature is intended for debugging purposes only.
Draw sprite vectors — Toggles drawing of sprite collision vectors in-game. The particular colours are unchangable; this feature is intended for debugging purposes only.
Draw active player path — Toggles drawing of the player's pending movement path. The colour may be defined using the adjacent colour box.
Draw active player destination — Toggles drawing of an ellipse at the player's destination. The colour may be defined using the adjacent colour box.
Plugins
If you have downloaded (or even written!) a plugin, it must be added here before it can be used. Plugins go in the Game\Plugins folder; a short description of the plugin appears when one is added. Additionally, you can specify plugins to be used in place of the default menu and fight plugins. For more information on Plugins, click . [here](page18.4.htm#adv.e)
