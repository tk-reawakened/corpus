---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/manual/page7.htm"
site: "rpgtoolkit.net"
title: "[ ]Around the Editor"
original_url: "http://rpgtoolkit.net/manual/page7.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20120618020625"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/manual/page7.htm", captured: "20120618020625", sha256: "fde5c78950be561b7926fec8049775454d8bd71bbbec05baafe8dd8f250770f8", wayback_url: "https://web.archive.org/web/20120618020625/http://rpgtoolkit.net/manual/page7.htm"}
---

# [ ]Around the Editor

Players are the characters in your game that can be controlled by the user, make up party members and fight battles. The user can only direct one character at a time (by default others don't appear on the boards, but can follow the player with the likes of "caterpillar" programs). In many games, the user starts out with control of the main character, and as they progress they meet others characters that join the main character to form a party that moves and fights battles together. The difference between players (made in this editor) and players made from items is that items cannot be controlled by the user, join their team or fight battles.
Character Basics
The character file contains a lot of information about the player, covering the aspects of the game that are specific to each player; that is, their graphics and walking animations, physical attributes (statistics or stats), fighting abilities and experience progression.
The first thing to do when creating a character is to give them walking graphics, so that they can be used to move around in the game. Most character graphics are made using tiles, but tiles cannot be directly selected for player graphics - all the character's graphics are made using either (*.amn) - collections of tiles or images that have a wide range of uses - or (from version 3.1.0). The basic set of player graphics consist of movement animations for North, South, East and West movement; these are required in order for the player to appear! This set can be supplemented with diagonal movements, idle, battle and custom animations. If these aren't created, the TK falls back to the first set. All these settings can be found in the "Graphics" option. [Toolkit Animations](page7.htm) *animated gifs*
With nothing more than movement graphics, the character can get quite far in a game - he can interact with objects on boards, hold and use items and be manipulated using RPGCode. But if they were to get into a battle in this state, they would die straight away!
Character Stats
The rest of the settings in the editor are devoted in some way or other to the character's fighting needs. The basic properties needed for battle are the player's attributes, such as health points and fighting power, which lie on the Stats tab of the editor. These are numerical values that represent the strengths, weaknesses and abilities of the player that dictate how they perform in a fight, and can be lost in battle, boosted by experience or by equipment, and altered by a plethora of RPGCode commands.
The most important stat is, unsurprisingly, the player's health or HP. Two values can be set here, a Starting Health and an Initial Max Health, for the case when you might want the player to be effectively injured at the beginning of the game.
Second are the player's abilities to attack enemies and defend himself during battle; the fight points (FP) and defence points (DP), respectively. In the most basic case, the FP is directly equal to the amount of HP the enemy loses when the player attacks - and the same applies in reverse: an enemy's FP is equal to the number of HP the player loses when the enemy attacks. However, the effect of any attack is reduced since the player (and enemy) can defend themselves (and may be wearing armour, etc.), and so the amount of HP the player loses is reduced by their DP.
The next options are Special Move Power (SMP) settings - SMP points are required to make , and as with health, starting and initial maximum values can be set. The other options are experience settings - a player gains experience as he moves through the game, from fighting or from completing tasks to advance the plot (as determined by the designer). The player's level is a representation of their current experience, the idea being that the player's attributes increase and new abilities become available when they "level-up". [Special Moves](page12.htm)
It is important when choosing values for all these settings that they are consistent and comparable throughout your game, as this will determine how easy or hard the game is. For instance, if you give your player an HP of 100, FP of 10 and a DP of 5, and your initial enemies HP of 80, FP of 30 and DP of 10, users will find themselves dying very quickly because the two combatants are unbalanced. Similarly, if enemies are too weak and the player too strong, fighting will be become easy and most probably boring. It is difficult to strike a good balance, but the results are worth it.
Around the Editor
Stats
- Character Name - The name of the player, which appears in the menu and in battle.
- Starting Experience - Number of experience points the player has at the start of the game, often set to zero.
- Starting Health - Health points at the beginning of the game, not necessarily the same as (but never greater than) the Initial Max Health, and always greater than zero!
- Initial Max Health - The maximum health the player can have at the start of the game. If the player uses health potions to increase his health, it cannot exceed this value. Note this is only an value, and hence can (and in most cases should) increase as the player levels-up. *initial*
- Starting DP - Defence points at the start of the game - this is the "intrinsic" defence ability of the player - it could represent their ability to dodge attacks (for instance), and can be temporarily increased with equipment, or . [Status Effects](page13.htm)
- Starting FP - Intrinsic fighting points at the start of the game ("bare fist fighting!"). You could set this zero and force your player to find a sword before he can attack enemies in battle!
- Starting S Move Power - The SMP points at the start of the game.
- Max Starting S Move Power - The maximum SMP the player can have at the beginning of the game, but can be increased as the player levels up.
- Starting Level - Initial level of the character. While it is often set to zero or one, some people argue that a character will have had some experience fighting prior to the storyline and thus set it higher.
Note that if you have players join your party half way through the game, you may want to give them progressed attributes similar to what the main character might have when he reaches that point.
Advanced - This tab contains a list of RPGCode variables that can be used in-game to obtain their corresponding player stats. The variables have default names, corresponding to the player's name followed by the attribute in square brackets. You can replace these with your own variable names if you wish.
Profile - Sets the profile (portrait) picture of the player, which appears in the default menu and battle systems. The default size is 64x64 pixels; images are stretched or compressed to match this. Tiles and tile bitmaps can also be selected.
Special Moves
Assigns the that the player can use. The "Official name of special moves" is the name that this class of special moves has in your game; for instance they may be Spells. This name appears in the menu of the . To add special moves, double-click an empty slot, or select a slot and hit "Change Special Move" - the special moves must have been created separately. [Special Moves](page12.htm) [default battle system](page15.htm#bs)
Most special moves should only become available to the player when they reach a certain level - this is set for each player in the "Special Move Info" window, (rather than in the special move file itself). Here you can set an experience or level value, or specify a variable that controls whether the player can use the move or not (for instance, they might only be able to use it whilst they possess a certain item or have completed a certain task).
Graphics
In this window animations are assigned to each direction or stance, and the vectors that define how the sprite interacts on the board are created.
Animation list
- The box lists the default directional stances, battle stances (Attack, Defend, Special Move, Die, Rest) and any custom stances that have been defined and the animation(s) associated with each stance. Directional stances may have both walking and idle animations; other stances have only a default animation. Idle directional animations are displayed when a sprite has been motionless for longer than the 'Seconds before the player is considered idle'.
- Text fields and browse buttons are located to the left of the listbox; press the '...' button to select an animation for the highlighted stance. Toolkit animations (*.anm) and animated gifs (*.gif) are valid formats. Animated gifs used in place of .anm's must reside within the GameName/Misc/ folder or subfolders therein, in the /GameName/Bitmap/ folder. If the animation exists it will be show in the preview window. To view the idle animations of directional stances, . **Note:** *not* **Right-click the listbox**
- Custom stances are any additional animations or actions that the sprite can perform, for instance in battle or during a story sequence, and are shown using the PlayerStance() or ItemStance() commands. Create a new custom stance by pressing the 'New Custom...' button and entering a name (handle) for it. The handle can be changed or the stance deleted using the relevant tools. Default stances cannot be renamed or deleted, but may be left empty.
Vector drawing window
- In the same way as collision vectors define solid areas of a board and program vectors define 'trigger' (or 'activation') areas, so collision vectors and activation vectors may be defined for sprites. The collision vector defines the solid area of the sprite's image, whilst the activation vector defines the area in which the player must stand in order to trigger the sprite's activation program. The activation vector should be larger than the collision vector if you want the sprite to be able to interact with the player.
- The Preview window displays the currently highlighted stance animation and the currently selected vector. A crosshair is also displayed, marking the of the sprite on the board. By default, this is placed at the bottom-centre of the sprite's image, and cannot be changed. It is this position that is given when the sprite's location is returned via ItemLocation() or the . *origin* [reserved player variables](page18.5.htm)
- A number of tools are provided for manipulating the vectors. By default, sprites may be given rectangular or diamond-shaped vectors (depending on whether the game's boards are isometric or not). Initially after selecting the animation, a 'Standard' 'Collision' rectangular vector will be assigned - where 'Standard' indicates a non-isometric board. To display the default activation vector, select 'Activation'; a larger rectangle is displayed.
- To assign a default vector, first select the vector type (Collision/Activation) and the coordinate type (Standard/Isometric), and then click 'Default Collision' or 'Default Interaction'. 'Default Collision' assigns a 'small' vector, whilst 'Default Interaction' assigns a large vector, scaled to correspond to a 32 pixel wide sprite.
- To create a custom vector, first select the vector type (Collision/Activation) you want to assign to, and then click the Draw (pencil) tool. Note that the Standard/Isometric setting is irrelevant to custom vectors, except that it causes an offset of the vertically by 8 pixels - this is for backwards compatibility. *origin*
- After selecting the Draw tool, click in the Preview window to start placing vector points. Right-click anywhere on the Preview window to close the vector.
- Points can be moved using the hand tool. Unlike the board editor, simply click and drag to move the nearest point. Click the white square below the hand tool to change the colour of the vector and the origin crosshair.
- The current vector's points are listed next to the tools. Existing points can be edited manually by clicking the value to be altered, hitting Delete or Backspace on the keyboard and entering a new value. Points can be deleted by clicking on the index of the point (in the first column) and hitting Delete or Backspace.
- Vectors can be imported from other sprites by clicking the Import button and browsing to a pre-existing sprite (item or player). Upon confirmation, the present sprite's vectors are replaced by the imported sprite's vectors.
- Note that only collision vector and activation vector can be defined per sprite; separate vectors are created for each direction or stance. **one** **one** *not*
Miscellaneous
- Seconds before the player is considered idle - If the player is not moving for this period of time, the idle animation corresponding to the current direction will begin (if it exists) and loop until movement starts again.
- Seconds between each step - Controls the walking speed of the current player (only!). This is an exact delay rather than a speed, so larger values correspond to slower movement. A value between 0.05s and 0.2s is recommended. For an in-depth discussion of character speeds and solutions to problems, see the . [faq page](page23.htm)
Wizard...
- A wizard tool is provided to allow you to quickly assign directional animations to the sprite, provided that the animations you have created follow a pattern. A template filename is given by the user, such as "start_*.anm", and the wizard substitutes in directions (s, n, e, w, ne, nw, se, sw) for the asterisk, to produce "start_s.anm", for instance.
Equipment
A player can wear equipment or clothing in order to increase their stats or give them special moves. Pieces of equipment are items that must be made "Equippable" to their destined body part. All the effects the equipment has on the player are determined in the . In the current editor, you must choose which areas of the player can receive pieces of equipment - standard areas are given, and further areas can be created using the drop-down Accessories list. [Item Editor](page8.htm)
Levels
As previously stated, levels are a measure of the experience that the player has, and used to reward the player with a steady increase in stats. The mathematical relationship between levels and experience must be set in this window - this will determine how often a player levels up. The numerical increments can be controlled either using percentages (Level-up type: exponentially) or using absolute values (Level-up type: linear)
- Initial exp for level up - The amount of experience required before the player levels up for the first time. A good value for this might be 100.
- Experience required increases by (%) - If the "exponential" level-up type is selected, then this is the percent by which the difference between levels increases for each level. For instance, if the initial exp level is set to 100, and this to 20%, then the extra experience required for the second level would be 120, and for the third level it would be 144 (120 + 20%). The increase in experience requirement is designed to reflect the steadily increasing difficulty of the game, and also to accommodate the increasing experience points that get rewarded for increasingly difficult enemies.
- Experience required increases by (pt) - If the "linear" level-up type is selected, then this is the number of points by which the difference between levels increases for each level. For instance, if the initial exp level is set to 100, and this to 20, then the extra experience required for the second level would be 120, and for the third level it would be 140.
- Level-up type: exponential - All stats increase by percentages.
- Level-up type: linear - All stats increase by absolute values.
- Maximum level - The highest level the player can reach.
- Max Health Increase By (%/pt) - The percentage or number of points by which the players maximum health increases with a level-up. Note that the player's actual health does not increase at level up!
- DP Increase By (%/pt) - The percentage or number of points by which the player's defence points increases with a level-up.
- FP Increase By (%/pt) - The percentage or number of points by which the player's fight points increases with a level-up.
- Max SMP Increase By (%/pt) - The percentage or number of points by which the players maximum special move power increases with a level-up. Note that the player's actual SMP does not increase at level up!
- Level-up RPGCode - If you want other things to happen at level up, such as the player's HP being totally restored or an MWin() message appearing, then you can specify a program to do it here.
