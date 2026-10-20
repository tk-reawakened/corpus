---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/manual/page31.htm"
site: "rpgtoolkit.net"
title: "RPGToolkit 3.1.0 Changelog"
original_url: "http://rpgtoolkit.net/manual/page31.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20120618022101"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/manual/page31.htm", captured: "20120618022101", sha256: "2d3da289ce07aba7d030aef014f9fe91f02e7e77c84bdd68efa79b84b9fb60c0", wayback_url: "https://web.archive.org/web/20120618022101/http://rpgtoolkit.net/manual/page31.htm"}
---

# RPGToolkit 3.1.0 Changelog

Overview
- This document details the changes and new features in RPGToolkit version 3.1.0 from version 3.0.6.
- Also refer to the updated help files at and the RPGCode function reference <http://tk3.toolkitzone.com/help/> [http://tk3.toolkitzone.com/help/page19](http://tk3.toolkitzone.com/help/page19.htm)
RPGToolkit Editor: toolkit3.exe
-
Tileset browser
- The tileset browser on the right-hand toolbar can be horizontally resized by dragging at the right edge of the object.
- Transparent pixels are rendered in "magic pink" (RGB 255, 0, 255).
- Isometric tiles are drawn more compactly.
-
File tree
- The project file tree on the right-hand toolbar can be horizontally resized by dragging at the right edge of the object.
- Improved loading speed.
- New options added to right-click menu: "Rename" and "Delete" are available for files; "Collapse All" collapses open folders; "Load into board editor" is available for animated tiles (TANs) when the board editor is open.
-
Subfolder selection
- Files can now be saved into and selected from subfolders of the default folders (default folders are those created by the Toolkit, e.g. "Bitmap" and "Chrs"). Each filetype (e.g., board or character) has a specific default folder.
- If a file is saved or selected from a folder outside of the default folder for that filetype, you will notified that the file will be copied into the default folder.
- When specifying files in subfolders in editors, include the name of the subfolder in the link, e.g. "village\village1.brd" for "gameName\Boards\village\village1.brd". Only the backslash '\' is valid for separating folders; '/' is not.
- "Default pathfinding algorithm" option added to StartUp Info tab. Use this to set the behaviour of mouse-driven movement, ItemPath() and PlayerPath().
- Vector drawing options added to the Graphics tab. Board and sprite vectors may be drawn in-game for debugging purposes (their colours cannot be changed); the active player's path and destination may be drawn in-game, in the colour specified by the adjacent colour box.
- Movement style control options added to the Project Settings tab. Mouse- and keyboard-controlled movement can be toggled; diagonal keyboard movement can be deactivated; custom movement keys can be defined for the eight possible directions.
-
New graphics window
- Section in which to allocate collision and interaction vectors for characters.
- Vectors are drawn in a similar way as in the board editor. Default shapes can be assigned, or imported from other sprite files.
- Wizard added to complete movement and idle stances.
Item editor
- New graphics window (see Character editor).
-
Toolbar
- Rearranged toolbar: frame delay text box added; frame file text box and browse button added; size option buttons replaced by combo box, includes option to resize to image size.
- Animation resizes to fit image when an image is selected.
-
Animation Wizard
- Create animations from selection of image files or tiles.
- Auto-creation of tile bitmaps for composite tile frames.
- Auto-detection of transparent colour.
- The board editor has been completely rewritten for this release.
-
Features
- Define default board parameters at start-up.
- Vector objects: collision, 'under' (layering), stairs, waypoint types.
- Image objects: images can be placed directly on to layers.
- Lighting objects: manipulable spotlights and gradients.
- Item graphics displayed.
- Object toolbar.
- Links to open files in their respective editors.
- Generic tools: dropper, rectangle, filled rectangle, copy, cut, paste, drag-drop, multi-level undo.
- All layers displayed, show and hide individual layers.
- Variable number of layers.
- Zoom, pan (scroll wheel support).
- Image export.
- Tile bitmaps can now be placed as tiles (the constituent tiles are inserted directly into the tile data and no link to the tile bitmap exists).
-
RPGCode Updater (Tools)
- Routine to upgrade RPGCode programs to improve compatibility with 3.1.0's RPGCode.
- The routine corrects syntax that worked in previous versions but does not work in 3.1.0, either because it is incorrect and the old interpreter does not recognise the error, or because the convention is incompatible with the new RPGCode specification.
- The updater does not guarantee that updated programs will run perfectly, and some user alterations may be required, depending on the quality of the code.
- A backup copy of each updated program is saved in the /Prg/Backup folder.
- All programs should be updated before the game is run, however the updater should never be run again on a program that has been updated.
Known issues
- Conditional activation variables (e.g. initvar = "0") that are uninitialised are set to "".
- Top row of solid tiles do not always convert to vectors properly
RPGToolkit Engine: trans3.exe
With the exception of some low-level graphics routines, the engine has been completely rewritten for this release, which is the justification for the new major version number.
Gameplay
-
- Two new coordinate systems are provided: 'isometric rotated' and 'pixel absolute'.
-
Isometric rotated
- The Cartesian coordinate system is rotated onto the isometric plane, resulting in a more intuitive coordinate system. The original isometric system is hereby known as 'isometric stacked'.
- Caveats of the rotated system: the origin (1,1) is necessarily off-screen, and the coordinate values are dependent upon the board width. That is, changing the board width alters the coordinate values (however, tiles and objects are updated accordingly in the board editor).
-
Pixel absolute
- All objects except tiles are referenced in Cartesian pixel coordinates, regardless of the underlying tile coordinate system (i.e. isometric or 2D).
- Tiles are still referenced in the underlying coordinate system (i.e., for functions accessing tiles).
- It is strongly recommended to use the pixel absolute coordinate system on both 2D and isometric boards.
-
Converting coordinate systems
- Boards may be upgraded to either new coordinate system in the board editor. Board data locations are unaffected, but all positions are given in the new system.
- Updating does not extend to RPGCode programs. All coordinates should be upgraded manually if the coordinate system is changed (this functionality cannot be provided by the RPGCode updater).
-
Movement (see Main File Editor)
- Movement can now be controlled using the mouse. Scrolling the board by moving the mouse to the edge of the screen is not currently supported.
- Custom movement keys can be assigned instead of the cursor keys.
- Dual numberpad-cursor key movement is no longer supported.
-
- The engine features a complete pathfinding system based on the new vector system. The system consists of two routines that implement tile and vector pathfinding, respectively.
- Tile pathfinding encompasses diagonal (8-way) and axial (4-way) movements between fixed grid points. Start and end points may be non-integral but path points will always be fixed. This may limit freedom of movement in comparison to vector pathfinding, especially when using non-tile integral collision vectors.
- Vector pathfinding allows movement in any direction between any points.
- Pathfinding is controlled through PlayerPath() and ItemPath(), and used by mouse movement.
-
Miscellaneous
- 'Target' and 'source' may be given as literal handles in an item's activation program. 'Source' refers to the activated item; 'target' refers to the player. Most sprite functions should now accept literal targets as well as item indices.
- Walking animation frames now change at the speed of the animation, not at a rate determined by the walking speed. **You may need to update your walking animations.**
- 3.1.0 features a novel RPGCode parser and compiler that generates "machine code" (for the RPGCode virtual machine, not the x86) from a raw text program, which is smaller and runs faster than the raw text. The engine also caches compiled programs so that they load more quickly when run again. The interpreter is based on .
New interpreter
-
Syntax alterations
- Use = to assign a value to a variable, use == to compare two values or variables (e.g., in an if statement). **= is not the same as == (the assignment operator is distinct from the equality operator).**
```
x = 12;
if (x == 10)
{
show(x); // Will not show because x == 12.
}
if (x = 10)
{
show(x); // Will show "10" because x = 10 assigns 10 to x and returns x; the if block runs because x ~= 0.
}
```
- **All strings must be quoted.**
```
var = "some string" // Correct.
var = some string // Error.
```
- Lines be terminated with a semi-colon. *may*
```
x = 12; // Valid, good practice.
x = 12 // Valid, but bad practice.
```
- Variable types have been decprecated: variables are now dynamic and can hold literal or numerical values. The literal/numerical identifers $ and ! are no longer required.
- Variables can be concatenated without type casting.
```
mwin("pi is " + 3.14)
```
- C++-style comments added: "//" and "/* comment */"
```
// Single-line comment.
/* Multi
line
comment */
```
- For-loop qualifiers must be semi-colon separated (not comma separated).
```
for(i = 0; i ~= 10; ++i) // Valid.
for(i = 0, i ~= 10, ++i) // Invalid.
```
- '=>' is not the 'greater than or equal to' operator (>=)
-
Alterations to existing functions
- ViewBrd(). Added optional parameter to draw to canvas instead of screen.
```
void viewbrd(string filename [, int x, int y [, canvas cnv]])
```
- PlayerStep(), ItemStep(). Added optional parameter to receive flags. See help files for information on flag usage and valid flags. Item handle may be 'target' or 'source' or index. Player handle may be index. Superseded by playerPath() and itemPath().
```
void playerstep(variant handle, int x, int y [, int flags])
```
- Push(), PushItem(). Added optional parameter to receive flags. Item handle may be 'target' or 'source' or index. Player handle may be index. Superseded by playerPath() and itemPath().
```
void push(string direction [, variant handle [, int flags]])
```
- DirSav(). New parameters to control dialog title, colours, background image. Use 'allowNewFile' to differentiate between loading and saving.
```
str dirSav(str title, bool allowNewFile, int textColor, int backColor, str image)
```
- ClearButtons(). Optional parameters to clear indexed slots.
```
clearbuttons([int slot1, int slot2...])
```
- PlayerStance(), ItemStance(). Added optional parameter for flags. See RPGCode reference for valid flags. Stances may be run from threads, optionally pausing thread execution until the stance ends. When run in a program, the stance persists until the frame is changed, e.g. by movement.
```
playerstance(handle player, string stance [, int flags])
```
- EraseItem(), DestroyItem(), ItemLocation(). Can now receive 'target' or 'source' as item identifiers in item-launched and item-multitasking programs.
- PathFind(). Can no longer pathfind between layers. Superseded by playerPath(), itemPath().
-
New functions: see RPGCode reference for details
- ActivePlayer(). Change the player that the user controls to a different member of the party.
- PlayerLocation().
- GetTickCount(). Milliseconds since Windows started.
- CanvasDrawPart().
- CanvasGetScreen(). Copy the screen to a canvas.
- PlayerPath(), ItemPath(). Supersede Push(), PushItem(), PlayerStep(), ItemStep(), PathFind(). Enables control of sprite movement by position rather than direction. Pathfinding or explicit paths may be defined. See the Vector Overview tutorial for further information.
```
void itemPath(variant handle, int flags, int x1, int y1, ..., int xn, int yn)
void itemPath(variant handle, int flags | tkMV_PATHFIND, int x1, int y1)
void itemPath(variant handle, int flags | tkMV_WAYPOINT_PATH, variant boardpath, int cycles)
void itemPath(variant handle, int flags | tkMV_WAYPOINT_LINK, variant boardpath, int cycles)
```
- PlayerGetPath(), ItemGetPath(). Get the number of points or a specific point in a sprite's path.
```
int playerGetPath(variant handle)
void playerGetPath(variant handle, int index, int &x, int &y)
```
- BoardGetVector(). Get the number of vectors on the board or the properties of a specific vector.
```
int boardGetVector()
void boardGetVector(variant vector, int &type, int &pointCount, int &layer, bool &isClosed, int &attributes)
```
- BoardSetVector().
```
void boardSetVector(variant vector, int type, int pointCount, int layer, bool isClosed, int attributes)
```
- BoardGetVectorPoint(). Get a single point of a vector by index.
```
void boardGetVectorPoint(variant vector, int pointIndex, int &x, int &y)
```
- BoardSetVectorPoint(). Set a single point of a vector, optionally applying the changes in order to regenerate pathfinding information.
```
void boardSetVectorPoint(variant vector, int pointIndex, int x, int y, bool apply)
```
- BoardGetProgram(). As above, for programs.
- BoardSetProgram().
- BoardGetProgramPoint().
- BoardSetProgramPoint().
- SetAmbientLevel(). Supersedes the AmbientRed, AmbientGreen, AmbientBlue reserved variables.
```
void setAmbientLevel(int red, int green, int blue)
```
- PlayerDirection(), ItemDirection(). Gets/sets the sprite direction. Possible directions are reserved constants (tkMV_E...), see RPGCode reference.
```
int playerDirection(variant handle)
void playerDirection(variant handle, int dir)
```
- SetErrorHandler(). Supersedes 'On Error' syntax.
- SetResumeNextHandler().
- ResumeNext().
- SpriteTranslucency(). Set/get the translucency of sprites moving behind objects.
```
void spriteTranslucency(int percent)
int spriteTranslucency(void)
```
-
Obselete functions (including previously obsolete functions)
- Sound() - use Wav() or MediaPlay().
- Win().
- GoDos().
- WalkSpeed() - use PlayerSpeed().
- ItemWalkSpeed() - use ItemSpeed().
- CharacterSpeed() - use GameSpeed().
- BorderColor().
- UnderArrow().
- FightStyle().
- BattleSpeed().
- TextSpeed().
- MwinSize().
- Stance() - use PlayerStance() or ItemStance() instead.
- StaticText().
- Parallax().
- AnimatedTiles().
- SmartStep().
- Autocommand().
- SetConstants().
- ShopColors().
- IIf() - use the following "tertiary" operator:
```
result = (expression ? true part : false part)
result = (5 == 3 ? "five equals three" : "five does not equal three")
```
Graphics
- Partially translucency for sprites. When passing under a tile or image on a higher layer or on an under-vector, only the coincident portion of the sprite will be drawn translucently (see SpriteTranslucency() function).
- Support for animated gifs for sprite animations. [ ] [link](http://tk3.toolkitzone.com/help/page10.htm)
- Ability to place image files (e.g., PNG) on board layers in a similar way to tiles.
- The ambient level is now applied to non-tile images used for sprites and background/layered images (see AmbientLevel()). This does not apply to tile shading/lighting.
Plugins and callbacks
- CBGetPlayerNum(PLAYER_DIR_FACING, ...), CBSetPlayerNum(...). The values assigned to each direction have changed to the following values, which correspond to the new RPGCode constants associated with the PlayerDirection() and ItemDirection() functions:
East
tkDIR_E
Southeast
tkDIR_SE
South
tkDIR_S
Southwest
tkDIR_SW
West
tkDIR_W
Northwest
tkDIR_NW
North
tkDIR_N
Northeast
tkDIR_NW
- CBGetGeneralString(GEN_PLYROTHERHANDLES, GEN_PLYROTHERFILES), CBSetGeneralString(sim.). No mechanism currently exists to restore removed players, so these variables are not stored.
Fixes
- Note: Since the engine has been almost entirely rewritten, these bugs have been implicitly fixed during the rewrite process.
- CreateItem() problems with unoccupied slot numbers.
- ItemLocation() problems in threads.
- Board backgrounds disappearing when moving to the top of a board.
- PlayAvi(), PlayAviSmall() compress dimensions.
Known issues
- Pathfinding is not infallible. Sprites will get stuck in complex and busy environments. Problems can be avoided by using simple sprite and board collision vectors and waypoint paths.
- Switching out of a full-screen game (e.g., using Alt-Tab) will cause the game to crash.
- prompt() does not accept "(".
- CallPlayerSwap() unimplemented.
- #global unimplemented.
Licensing
- The RPGToolkit version 3.1.0 is licensed under the GNU General Public License (GPL) v3. This includes the engine trans3.exe, the editor toolkit3.exe, and the graphics library actkrt3.dll.
Credits
- Colin Fitzpatrick: RPGCode subsystem (including threaded RPGCode), most file readers, most RPGCode functions, plugin subsystem, most plugin callbacks, battle system subsystem, RPGCode update wizard, various trivial things
- Jonathan Hughes (Delano): Board editor, animation wizard, project file tree, sprite graphics window, subfolder file selection. Vector collision, vector movement and pathfinding, coordinate systems, partial sprite translucency, layered images.
- Samuel Bedwell (Occasionally Correct): RPGCode help pages.
- Lorie-Jay Gutierrez (Khin): Board editor icons.
