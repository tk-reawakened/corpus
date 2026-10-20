---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/manual/page19.htm"
site: "rpgtoolkit.net"
title: "RPGCode Function Reference"
original_url: "http://rpgtoolkit.net/manual/page19.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20120618021615"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/manual/page19.htm", captured: "20120618021615", sha256: "738f89305fa58266762804d6e4f185f13a9d5ebd56385c190e371feb482f5ff2", wayback_url: "https://web.archive.org/web/20120618021615/http://rpgtoolkit.net/manual/page19.htm"}
---

# RPGCode Function Reference

[ | ]Collapse AllExpand All
```
- b [ ] +
- c [ ] +
- d [ ] +
- e [ ] +
- f [ ] +
- g [ ] +
- h [ ] +
- hp
- i [ ] +
- k [ ] +
- l [ ] +
- m [ ] +
- n [ ] +
- newPlayer
- o [ ] +
- p [ ] +
- r [ ] +
- s [ ] +
- t [ ] +
- u [ ] +
- v [ ] +
- viewbrd
- w [ ] +
- z [ ] +
- zoom
```
Variable types
- — Array: a collection of variables using the same identifer [ ] **array** [link](page18.1.htm#variables.array)
```
array[0] = "first entry";
array[1] = "second entry";
split("split,by,commas",",",array);
show(array[0]); // Shows "split"
```
- — Boolean: true or false **bool**
```
bVar = true; // Note: no quotes
```
- — Canvas: the handle (pointer) to an off-screen bitmap. Must be generated with createCanvas() and freed using killCanvas() **canvas**
```
cnv = createCanvas(640, 480);
bitmap("image.jpg", cnv);
drawCanvas(cnv, 0, 0);
killCanvas(cnv);
```
- — Cursor map: handle (pointer) to a cursor map object as created by createCursorMap() and destroyed using killCursorMap(). A cursor map consists of points on the screen at between which the cursor can be moved using the arrow keys **cursor_map**
```
cmap = createCursorMap();
cursorMapAdd(320, 240, cmap);
res = cursorMapRun(cmap);
killCursorMap(cmap);
```
- — Double: alias of int (floating point) **double**
- — Handle: sprite or object handle (identifier). Possible values vary depending on context **handle**
```
// Item handles may be numerical (their index in the board item array) or, *in their multitasking program*, "source" or "target".
itemDirection(3, tkDIR_W);
itemPath("source", 0, 123, 456);
// Player handles may be literal or numerical or "source" or "target" (in multitasking program).
playerStance("bob", "attack");
```
- — Numerical: integer or floatin point [ ] **int** [link](page18.1.htm#variables.num)
```
iVar = 12;
iVar = 3.14;
```
- — Label: a program line identifier. Used in conjunction with branch() to cause program execution to jump unconditionally to the point indicated by the label. Used in error handling in conjunction with setErrorHandler to execute code when an error occurs [ ] **label** [link](page18.5.htm)
```
mwin("Line one");
branch(":skip");
mwin("Line two");
:skip
mwin("Line three");
// Prints:
// Line one
// Line three
```
- — Literal: any character (must be quoted) [ ] **string** [link](page18.1.htm#variables.str)
```
sVar = "RpgTK3.1.0";
```
- — Thread: a handle (pointer) to a thread, created with thread() and destroyed with killThread() **thread**
```
tid = thread("thread.prg", 0);
killThread(tid);
```
- — Variant: may be numerical or literal (see handle) **variant**
- — Void: the function does not return a value [ ] **void** [link](page18.1.htm#functionsii.ret)
activePlayer
```
activePlayer( handle) void variant
```
```
activePlayer(void) handle
```
Set or get the active player, by handle.
addPlayer
```
addPlayer( file) void string
```
Add a player to the party.
```
ai( level) void int
```
Have the source enemy use the internal AI.
animatedTiles
```
animatedTiles() void
```
Toggle animated tiles.
applyStatus
```
applyStatus( target, file) void string string
```
Apply a status effect to a fighter.
appPath
```
appPath([ &dest]) string string
```
Retrieve the path of trans3.exe, without the final backslash.
asc
```
asc( chr[, &ret]) int string int
```
Get the ASCII value of a character.
attackAll
```
attackAll( fp) void int
```
Deal the specified amount in HP to all the members of the target's party.
autoCommand
```
autoCommand() void
```
Obsolete.
autoLocal
```
autoLocal( bEnabled) void bool
```
Set the default scope for variable resolution. When autolocal() is not enabled, variables are assumed to be global unless a local variable has been defined. When autolocal() is enabled, variabes are assumed to be local unless a global variable has been defined.
Note that if autolocal() is enabled and variables that are not global are referenced outside of any function, these variables are local to the program. When the program ends, they will be deleted.
battleSpeed
```
battleSpeed( speed) void int
```
Obsolete.
bitmap
```
bitmap( file, [ cnv]) void string canvas
```
Fill a surface with an image.
boardGetProgram
```
boardGetProgram( programIndex, &program, &pointCount, &layer, &isClosed, &attributes, &distanceRepeat) void int string int int bool int int
```
```
boardGetProgram() int
```
- Returns the properties of a given program.
- Returns the number of programs on the board.
boardGetProgramPoint
```
boardGetProgramPoint( programIndex, pointIndex, &x, &y) void int int int int
```
Get a single point on a board program. x, y are always pixel values.
boardGetVector
```
boardGetVector() int
```
```
boardGetVector( vector, &type, &pointCount, &layer, &isClosed, &attributes) void variant int int int bool int
```
- Returns the number of vectors on the board.
- Returns the properties of a given vector.
boardGetVectorPoint
```
boardGetVectorPoint( vector, pointIndex, &x, &y) void variant int int int
```
Get a single point on a board vector. x, y are always pixel values.
boardSetProgram
```
boardSetProgram( programIndex, program, pointCount, layer, isClosed, attributes, distanceRepeat) void int string int int bool int int
```
Sets the properties of a given program; creates a new program if one-past-the-end index is given. Use val = boardGetProgram() to get the next index. distanceRepeat in pixels always.
Possible flags: tkPRG_STEP, tkPRG_KEYPRESS, tkPRG_REPEAT, tkPRG_STOPS_MOVEMENT.
boardSetProgramPoint
```
boardSetProgramPoint( programIndex, pointIndex, x, y) void int int int int
```
Set/move a single point on a board program. x, y are always pixel values.
boardSetVector
```
boardSetVector( vector, type, pointCount, layer, isClosed, attributes) void variant int int int bool int
```
Sets the properties of a given vector. Creates a new vector if an existing one is not found - if a numeric variable is supplied, it will be set to the new index (one-past-end).
- Possible types are: tkVT_SOLID, tkVT_UNDER, tkVT_STAIRS, tkVT_WAYPOINT.
- Possible attributes: tkVT_BKGIMAGE, tkVT_ALL_LAYERS_BELOW, tkVT_FRAME_INTERSECT.
boardSetVectorPoint
```
boardSetVectorPoint( vector, pointIndex, x, y, apply) void variant int int int bool
```
Set/move a single point on a board vector. x, y are always pixel values. Set apply = true for last change, to improve speed.
bold
```
bold( enable) void bool
```
Toggle emboldening of text.
borderColor
```
borderColor( r, g, b) void int int int
```
Obsolete.
branch
```
branch( lbl) void label
```
Jump to a label.
callplayerswap
```
callplayerswap(...) void
```
Unimplemented in 3.1.0.
callshop
```
callshop( item1, item2, item3, ...) void string string string
```
Displays a basic shop interface that allows the buying of the items given as parameters and the selling of items in the player's inventory.
canvasDrawPart
```
canvasDrawPart( cnv, x, y, xSrc, ySrc, width, height[, cnvDest]) void int int int int int int int canvas
```
Draw part of a canvas.
canvasGetScreen
```
canvasGetScreen( cnvDest) void canvas
```
Copy the screen onto a canvas.
castInt
```
castInt( x, [ &ret]) int variant int
```
Cast the specified value to an integer (i.e., a number in the sequence ...-2, -1, 0, 1, 2...). This is useful for removing fractional parts of numbers. Note that this function does not round.
castLit
```
castLit( x, [ &ret]) string variant string
```
Cast the specified value to a string. There is really no need to do this ever. RPGCode by itself will cast values passed to functions to the correct types as required.
castNum
```
castNum( x, [ &ret]) double variant double
```
Cast the specified value to a number (double). There is really no need to do this ever. RPGCode by itself will cast values passed to functions to the correct types as required.
change
```
change( program) void string
```
Change this program so that next time it is triggered, a different program runs instead. Change() is active only while the player remains on the board (i.e., leaving the board causes programs to return to normal).
characterSpeed
```
characterSpeed() void
```
Obsolete.
charAt
```
charAt( str, pos, [ &ret]) string string int string
```
Get a character from a string. The first character is one. The value of the parameter must be in the closed interval [1, length]. **pos**
chr
```
chr( asc, [ &ret]) string int string
```
Get the character represented by the ASCII code passed in.
clear
```
clear([ cnv]) void canvas
```
Clear a surface. clear() blanks the screen. clear(cnv) blanks the canvas whose handle is 'cnv'.
clearBuffer
```
clearBuffer() void
```
Clear the keyboard buffer.
clearbuttons
```
clearbuttons([ slot1, slot2...]) void int int
```
Clear buttons set by SetButton(). Clear specific slot(s) if supplied, else clear all slots.
closeFile
```
closeFile( file) void string
```
Close a file.
color
```
color( dos) void int
```
Change to a DOS colour.
colorRgb
```
colorRgb( r, g, b) void int int int
```
Change the active colour to an RGB value.
cos
```
cos( x, [ &ret]) double double double
```
Calculate cosine x.
createCanvas
```
createCanvas( width, height, [ &cnv]) canvas int int canvas
```
Create a canvas.
createCursorMap
```
createCursorMap([ &ret]) cursor_map cursor_map
```
Create a cursor map.
createItem
```
createItem( filename[, &pos]) int string int
```
Load an item and return the slot into which it was loaded.
cursorMapAdd
```
cursorMapAdd( x, y, map) void int int cursor_map
```
Add a point to a cursor map.
cursorMapHand
```
cursorMapHand( cursor[, stretch = true]) void string bool
```
Change the cursor used everywhere cursors are used (e.g. cursor maps, the menu, the battle system), optionally not stretching it to 32 by 32 pixels.
The string "default" restores the default image.
cursorMapRun
```
cursorMapRun( map, [ &ret]) int cursor_map int
```
Run a cursor map.
debug
```
debug( enable) void bool
```
Toggle whether to show debug messages.
debugger
```
debugger( message) void string
```
Show a debug message.
delay
```
delay( time) void double
```
Delay for a certain number of seconds.
destroyitem
```
destroyitem( handle) void variant
```
Remove an item from memory. Warning: do not destroy an item through it's own multitasking thread.
destroyPlayer
```
destroyPlayer( handle) void string
```
Permanently remove a player from the party.
dirSav
```
dirSav( title, allowNewFile, textColor, backColor, image) string string bool int int string
```
Allow the user to choose a *.sav file from the "Saved" directory. For historical reasons, returns "CANCEL" if no file is chosen, not "".
done
```
done() void
```
End the program.
drainAll
```
drainAll( fp) void int
```
Deal the specified amount in SMP to all the members of the target's party.
drawCanvas
```
drawCanvas( cnv, x, y, [ width, height, [ dest]]) void canvas int int int int canvas
```
Blit a canvas forward.
drawCanvasTransparent
```
drawCanvasTransparent( cnv, x, y, r, g, b[, width, height[, dest]]) void canvas int int int int int int int canvas
```
Blit a canvas forward, but don't blit one colour (the transparent colour).
drawCircle
```
DrawCircle( x, y, radius [, canvas]) void int int int int
```
Draw a circle at x,y, optionally to a canvas. Previously an arc could be defined but this never worked, so the two parameters have been cut and the optional canvas is now the fourth parameter.
drawEnemy
```
drawEnemy( file, x, y, [ cnv]) void string int int canvas
```
Draw an enemy.
drawLine
```
drawLine( x1, y1, x2, y2, [ cnv]) void int int int int canvas
```
Draw a line.
drawRect
```
drawRect( x1, y1, x2, y2, [ cnv]) void int int int int canvas
```
Draw a rectangle.
earthquake
```
earthquake( intensity) void int
```
Shake the screen.
empty
```
empty() void
```
Clear all globals.
end
```
end() void
```
End the program.
endAnimation
```
endAnimation( animationID) void int
```
End a multitasking animation.
equip
```
equip( handle, location, item) void variant int string
```
Equip an item from the inventory (by handle or filename) to a location on the player's body.
- 1 - Head
- 2 - Neck accessory
- 3 - Right hand
- 4 - Left hand
- 5 - Body
- 6 - Legs
- 7+ - Custom accessories
eraseitem
```
eraseitem( handle) void variant
```
Erase an item from the screen, but keep it in memory. Warning: erasing an item in it's own multitasking thread will pause the thread.
eraseplayer
```
eraseplayer( handle) void string
```
Erase a party player from the screen.
fade
```
fade( type) void int
```
Perform a fade using the current colour. There are several different types of fades.
- 0 - the screen is blotted out by a growing and shrinking box
- 2 - fades from white to black
- 3 - line sweeps across the screen
- 4 - black circle swallows the player
- 5 - image fade to black
fight
```
fight( skill, background) void int string
```
Start a skill level fight.
fightEnemy
```
fightEnemy( enemy, enemy, ... background) void string string string
```
Start a fight.
fightMenuGraphic
```
fightMenuGraphic( image) void string
```
Choose an image for the fight menu graphic.
fightStyle
```
fightStyle() void
```
Obsolete.
fileEof
```
fileEof( file, [ &ret]) bool string bool
```
Check whether the end of a file has been reached.
fileGet
```
fileGet( file, [ &ret]) string string string
```
Get a byte from a file.
fileInput
```
fileInput( file, [ &ret]) string string string
```
Read a line from a line.
filePrint
```
filePrint( file, line) void string string
```
Write a line to a file.
filePut
```
filePut( file, byte) void string string
```
Write a byte to a file.
fillCircle
```
FillCircle( x, y, radius [, canvas]) void int int int int
```
Draw a filled circle at x, y, to screen or canvas.
fillRect
```
fillRect( x1, y1, x2, y2, [ cnv]) void int int int int canvas
```
Draw a filled rectangle.
font
```
font( font) void string
```
Load a true type font. TK2 fonts are not supported.
fontSize
```
fontSize( size) void int
```
Set the font size.
forceRedraw
```
forceRedraw() void
```
Force a redrawing of the screen.
gamespeed
```
gamespeed( speed) void int
```
Set the overall walking speed. Changes the walking speed proportionally. +ve values increase speed, -ve decrease, by a factor of 10% per increment. Allowed values range from -MAX_GAMESPEED to +MAX_GAMESPEED.
get
```
get([ &ret]) string string
```
Get a key from the queue.
getBoardName
```
GetBoardName([ ret]) string string
```
Get the current board's file name.
getBoardTile
```
getBoardTile( x, y, z, [ &ret]) string int int int string
```
Get the file name of the tile at x, y, z.
getBoardTileType
```
getBoardTileType( x, y, z[, &ret]) string int int int string
```
Get the type of a tile.
getColor
```
getColor( &r, &g, &b) void int int int
```
Get the current colour.
getCorner
```
getCorner( &topX, &topY) void int int
```
Get the corner of the currently shown portion of the board.
getDp
```
getDp( handle, [ &ret]) int string int
```
Get a fighter's dp.
getFontSize
```
getFontSize([ &ret]) int int
```
Get the current font size.
getFp
```
getFp( handle, [ &ret]) int string int
```
Get a fighter's fp.
getGp
```
getGp([ &ret]) int int
```
Return the amount of gold pieces held.
getHp
```
getHp( handle, [ &ret]) int string int
```
Get a fighter's hp.
getItemCost
```
getItemCost( fileName[, &ret]) int string int
```
Get an item's cost.
getItemDesc
```
getItemDesc( fileName[, &ret]) string string string
```
Get an item's description.
getItemName
```
getItemName( fileName[, &ret]) string string string
```
Get an item's handle.
getItemSellPrice
```
getItemSellPrice( fileName[, &ret]) int string int
```
Get the price for which an item sells.
getLevel
```
getLevel( handle[, &ret]) int string int
```
Get the level of a player.
getMaxHp
```
getMaxHp( handle, [ &ret]) int string int
```
Get a fighter's max hp.
getMaxSmp
```
getMaxSmp( handle, [ &ret]) int string int
```
Get a fighter's max smp.
getPixel
```
getPixel( x, y, &r, &g, &b, [ cnv]) void int int int int int canvas
```
Get the colour of the pixel at (x, y).
getRes
```
getRes( &x, &y) void int int
```
Get the screen's resolution.
getSmp
```
getSmp( handle, [ &ret]) int string int
```
Get a fighter's smp.
gettextheight
```
gettextheight( text) int string
```
Get the height of a string of text in pixels, relative to the current font and size.
gettextwidth
```
gettextwidth( text) int string
```
Get the width of a string of text in pixels, relative to the current font and size.
getThreadId
```
getThreadId([ &ret]) thread thread
```
Get the ID of this thread.
getTickCount
```
getTickCount() int
```
Get the number of milliseconds since Windows started.
giveExp
```
giveExp( handle, amount) void string int
```
Give experience to a player.
giveGp
```
giveGp( gp) void int
```
Give gold pieces.
giveHp
```
giveHp( handle, add) void string int
```
Increase a fighter's current hp.
giveItem
```
giveItem( itm) void string
```
Add an item to the inventory.
giveSmp
```
giveSmp( handle, value) void string int
```
Increase a fighter's smp.
goDos
```
goDos( command) void string
```
Obsolete.
gone
```
gone() void
```
Remove the currently running program from the board until the board has been left.
```
hp( handle, value) void string int
```
Set a fighter's hp.
iif
```
iif(condition, true, false) void
```
Obsolete. Use the tertiary operator result = (expression ? true part : false part)
inn
```
inn() void
```
Fully heal the player party.
inStr
```
inStr( haystack, needle[, offset]) int string string int
```
Returns the first occurence of needle within haystack, optionally starting from an offset. Both the return value and the offset are one-based.
internalMenu
```
internalMenu( menu) void int
```
Show a menu using the menu plugin.
- 0 - main menu
- 1 - item menu
- 2 - equip menu
- 4 (sic) - abilities menu
italics
```
italics( enable) void bool
```
Toggle italicizing of text.
itemCount
```
itemCount( fileName[, &ret]) int string int
```
Count the number of a certain item in the inventory.
itemDirection
```
itemDirection( handle) int variant
```
```
itemDirection( handle, dir) void variant int
```
- Returns the item direction.
- Sets the item direction.
See playerDirection() for direction indices.
itemGetPath
```
itemGetPath( handle) int variant
```
```
itemGetPath( handle, index, &x, &y) void variant int int int
```
- Get the number of points in the sprite's path.
- Get the coordinates of a point in the sprite's path.
itemlocation
```
itemlocation( handle, &x, &y, &layer) void variant int int int
```
Get the location of an item.
itemPath
```
itemPath( handle, flags, x1, y1, ... , xn, yn) void variant int int int int int
```
```
itemPath( handle, flags | tkMV_PATHFIND, x1, y1) void variant int int int
```
```
itemPath( handle, flags | tkMV_WAYPOINT_PATH, boardpath, cycles) void variant int variant int
```
```
itemPath( handle, flags | tkMV_WAYPOINT_LINK, boardpath, cycles) void variant int variant int
```
Causes the sprite to walk a path between a given set of co-ordinates, depending on the flags parameter. 'handle' must be a board index value or 'target' or 'source', not the item's internal handle.
- Sprite walks the explicit path given by x1, y1 to xn, yn. Required flag: none.
- Sprite walks to x1, y1 via the shortest route (by pathfinding). Required flag: tkMV_PATHFIND.
- Sprite walks a board-set waypoint vector. Required flag: tkMV_WAYPOINT_PATH. The points of the vector are added to the sprite's queue.
- A link is made between sprite and waypoint vector. Required flag: tkMV_WAYPOINT_LINK. Set cycles = 0 to walk infinitely. Set boardpath = -1 to clear link to waypoint vector before cycles expires. The sprite will resume the the path if other movement commands are given to it, after completion.
Possible flags for all options:
- tkMV_PAUSE_THREAD: Hold thread execution until movement ends.
- tkMV_CLEAR_QUEUE: Clear any previously queued movements.
itemspeed
```
itemspeed( handle, speed) void variant int
```
Set the delay in seconds between an item's steps.
itemstance
```
itemstance( item, stance [, flags]) void handle string int
```
Animate an item's custom stance.
Possible flags tkMV_PAUSE_THREAD: Hold thread execution until animation ends.
itemstep
```
itemstep( handle, x, y [, flags]) void variant int int int
```
Causes the item to take one step in the direction of x, y following a route determined by pathFind.
Possible flags
- tkMV_PAUSE_THREAD: Hold thread execution until movement ends.
- tkMV_CLEAR_QUEUE: Clear any previously queued movements.
itemWalkSpeed
```
itemWalkSpeed() void
```
Obsolete.
kill
```
kill( &var, ...) void variant
```
Delete variables.
killCanvas
```
killCanvas( cnv) void canvas
```
Kill a canvas.
killCursorMap
```
killCursorMap( map) void cursor_map
```
Kill a cursor map.
killThread
```
killThread( id) void thread
```
Kill a thread.
layerput
```
layerput( x, y, layer, tile) void int int int string
```
Place a tile on the board for the duration the player is on the board.
lcase
```
lcase( str, [ &ret]) string string string
```
Convert a string to lowercase.
left
```
left( str, amount[, &ret]) string string int string
```
Get characters from the left of a string.
len
```
len( str[, &ret]) int string int
```
Get the length of a string.
load
```
load( file) void string
```
Load the game state from a file.
log
```
log( x, [ &ret]) double double double
```
Returns such that = . **n** **e** **n** **x**
mainFile
```
mainFile( gam) void string
```
Load a new main file.
maxHp
```
maxHp( handle, value) void string int
```
Set a fighter's max hp.
maxSmp
```
maxSmp( handle, value) void string int
```
Set a fighter's max smp.
mediaPlay
```
mediaPlay( file) void string
```
Play the specified file as the background music.
mediaStop
```
mediaStop() void
```
Stop the background music.
mem
```
mem( x, y, pos) void int int int
```
Lay a scanned tile on the screen at the specified position. @deprecated
menuGraphic
```
menuGraphic( image) void string
```
Choose an image for the menu.
mid
```
mid( str, start, length[, &dest]) string string int int string
```
Obtain a substring. The offset is one-based.
mouseclick
```
mouseclick( &x, &y [, noWait]) void int int bool
```
Wait for a mouseclick or immediately retrieve the last and return the x, y location (pixel values relative to the window).
mouseCursor
```
mouseCursor( file, x, y, red, green. blue) void string int int int int int
```
Change the mouse cursor. "TK DEFAULT" or "" restores the default cursor.
mousemove
```
mousemove( &x, &y) void int int
```
Wait for the mouse to move and return the x,y location in pixels from the window corner.
move
```
move( x, y, [ z = 1]) void int int int
```
Move this board program to a new location on the board. The effect lasts until the board has been left.
mp3pause
```
mp3pause() void
```
Play a sound effect and pause the engine until it finishes.
msgBox
```
msgBox( text [, title [, style [, textColor [, backColor [, bitmap]]]]]) int string string int int int string
```
Display a message box containing one or two buttons, handled using a cursor map (keyboard input only). The background is drawn translucently using the MWin() translucency value. Any background image supplied is stretched to the size of the box.
- style = 0: 'OK' button; function returns 1.
- style = 1: 'Yes' and 'No' buttons: 'Yes' returns 6 and 'No' returns 7.
multirun
```
multirun() void
```
Multirun()'s behaviour depends on the program's context. In a thread: No action. In a program (non-thread): All sprite movements called are queued up and movement begins after the closing brace of the function, thereby allowing simultaneous movement. Previously occurring movements are cleared.
mwin
```
mwin( str) void string
```
Show the message window.
mwinCls
```
mwinCls() void
```
Clear and hide the message window.
mwinsize
```
mwinsize( percent) void int
```
Obsolete.
newPlayer
```
newPlayer( file) void string
```
Change the graphics of the main player to that of the file passed in. The file must be a character file (*.tem)
onBoard
```
onBoard( handle) int variant
```
Return whether a player is being shown on the board.
openFileAppend
```
openFileAppend( file, folder) void string string
```
Open a file for appending.
openFileBinary
```
openFileBinary( file, folder) void string string
```
Obsolete.
openFileInput
```
openFileInput( file, folder) void string string
```
Open a file in input mode.
openFileOutput
```
openFileOutput( file, folder) void string string
```
Open a file in output mode.
over
```
over() void
```
Displays a game over message and resets the game. Because you can (and should) set a game over program, this function is pointless.
parallax
```
parallax( setting) void int
```
obsolete.
pixelMovement
```
pixelMovement([ pixelMovement [, pixelPush]]) bool bool bool
```
Toggles pixel movement and push() et al. in pixels. Returns whether pixel movement is being used. pixelPush is ineffective for tile movement.
pixelText
```
pixelText( x, y, str, [ cnv]) void int int string canvas
```
Displays text on the screen using pixel coordinates.
playAvi
```
playAvi( movie) void string
```
Play a movie full screen. Supported types are *.avi, *.mpg, and *.mov.
playAviSmall
```
playAviSmall( movie) void string
```
Play a movie at actual size, centred. Supported types are *.avi, *.mpg, and *.mov.
playerDirection
```
playerDirection( handle) int variant
```
```
playerDirection( handle, dir) void variant int
```
- Returns the player direction.
- Sets the player direction.
Directions are assigned the following constants:
- East: tkDIR_E
- Southeast: tkDIR_SE
- South: tkDIR_S
- Southwest: tkDIR_SW
- West: tkDIR_W
- Northwest: tkDIR_NW
- North: tkDIR_N
- Northeast: tkDIR_NE
playerGetPath
```
playerGetPath( handle) int variant
```
```
playerGetPath( handle, index, &x, &y) void variant int int int
```
- Get the number of points in the sprite's path.
- Get the coordinates of a point in the sprite's path.
playerlocation
```
playerlocation( handle, &x, &y, &layer) void variant int int int
```
Get the location of a player.
playerPath
```
playerPath( handle, flags, x1, y1, ... , xn, yn) void variant int int int int int
```
```
playerPath( handle, flags | tkMV_PATHFIND, x1, y1) void variant int int int
```
```
playerPath( handle, flags | tkMV_WAYPOINT_PATH, boardpath, cycles) void variant int variant int
```
```
playerPath( handle, flags | tkMV_WAYPOINT_LINK, boardpath, cycles) void variant int variant int
```
Causes the sprite to walk a path between a given set of co-ordinates, depending on the flags parameter.
- Sprite walks the explicit path given by x1, y1 to xn, yn. Required flag: none.
- Sprite walks to x1, y1 via the shortest route (by pathfinding). Required flag: tkMV_PATHFIND.
- Sprite walks a board-set waypoint vector. Required flag: tkMV_WAYPOINT_PATH. The points of the vector are added to the sprite's queue.
- A link is made between sprite and waypoint vector. Required flag: tkMV_WAYPOINT_LINK. Set cycles = 0 to walk infinitely. Set boardpath = -1 to clear link to waypoint vector before cycles expires. The sprite will resume the the path if other movement commands are given to it, after completion.
Possible flags for all options:
- tkMV_PAUSE_THREAD: Hold thread execution until movement ends.
- tkMV_CLEAR_QUEUE: Clear any previously queued movements.
playerspeed
```
playerspeed( handle, speed) void string int
```
Set the delay in seconds between a player's steps.
playerstance
```
playerstance( player, stance [, flags]) void handle string int
```
Animate a player's custom stance.
Possible flags tkMV_PAUSE_THREAD: Hold thread execution until animation ends.
playerstep
```
playerstep( handle, x, y [, flags]) void variant int int int
```
Causes the player to take one step in the direction of x, y following a route determined by pathFind.
Possible flags
- tkMV_PAUSE_THREAD: Hold thread execution until movement ends.
- tkMV_CLEAR_QUEUE: Clear any previously queued movements.
posture
```
posture( id [, player]) void int handle
```
Show a custom player animation named "Custom" + str(id) (e.g. "Custom1") This command is obsolete - use playerStance() instead.
prg
```
prg( program. x, y, [ z = 1]) void string int int int
```
Move a program on the current board to a new location. This stays in effect until the board is left.
print
```
print( text) void string
```
Write the specified string one line down from the last call to text().
prompt
```
prompt( question, [ &ret]) string string string
```
Ask the player a question and return the result.
push
```
push( direction [, handle [, flags]]) void string variant int
```
Push the player with the specified handle, or the default player if no handle is specified, along the given directions. The direction should be a comma delimited, but if it is not, it will be delimited for backward compatibility. These styles are accepted, and can be mixed even within the same directonal string:
- N, S, E, W, NE, NW, SE, SW
- NORTH, SOUTH, EAST, WEST, NORTHEAST, NORTHWEST, SOUTHEAST, SOUTHWEST
- 1, 2, 3, 4, 5, 6, 7, 8
Possible flags
- tkMV_PAUSE_THREAD: Hold thread execution until movement ends.
- tkMV_CLEAR_QUEUE: Clear any previously queued movements.
pushItem
```
pushItem( item, direction [, flags]) void variant string int
```
The first parameter accepts either a string that can be either "target" or "source" direction or the number of an item. The syntax of the directional string is the same as for [[push()]].
Possible flags
- tkMV_PAUSE_THREAD: Hold thread execution until movement ends.
- tkMV_CLEAR_QUEUE: Clear any previously queued movements.
put
```
put( x, y, tile) void int int string
```
Puts a tile at the specified location on the board. The tile persists only until the program ends. Use LayerPut() to place a tile for the duration the user is on the board. x and y are specified in tile coordinates.
putitem
```
putitem( handle, x, y, layer) void variant int int int
```
Place the item on the board at the given location.
putplayer
```
putplayer( handle, x, y, layer) void string int int int
```
Place the player on the board at the given location.
random
```
random( max, [ &ret]) int int int
```
Generate a random number from one to the supplied maximum, inclusive.
regExpReplace
```
regExpReplace( subject, pattern, replace) string string string string
```
Replace using a regular expression.
remove
```
remove( handle, location) void variant int
```
Remove an equipped item and return it to the inventory.
removePlayer
```
removePlayer( handle) void string
```
Remove a player from the party [to an old player list].
removeStatus
```
removeStatus( target, file) void string string
```
Remove a status effect from a fighter.
rendernow
```
rendernow( draw) void bool
```
Controls rendering of the cnvRenderNow reserved canvas. The canvas is drawn every frame above all board elements (e.g. tiles, sprites, animations). Access the canvas by passing 'cnvRenderNow' to the drawing functions. Do not call CreateCanvas() or KillCanvas() on cnvRenderNow.
replace
```
replace( str, find, replace[, &dest]) string string string string string
```
Replace within a string.
reset
```
reset() void
```
Reset the game.
restorePlayer
```
restorePlayer( filename) void string
```
Restore a player who was previously on the team.
restorescreen
```
restorescreen([ x1, y1, x2, y2, xdest, ydest]) void int int int int int int
```
Draw a buffered screen capture to the screen. The canvas drawn is the first in the screen array. x1, x2 specify the bottom- right corner of the screen, so that width = x2 - x1, etc.
restorescreenarray
```
restorescreenarray( pos [, x1, y1, x2, y2, xdest, ydest]) void int int int int int int int
```
Draw a buffered screen capture to the screen. x1, x2 specify the bottom-right corner of the screen, so that width = x2 - x1, etc.
resumeNext
```
resumeNext() void
```
Return to the statement after the statement where an error occurred.
right
```
right( str, amount, [ &ret]) string string int string
```
Get characters from the right of a string.
rpgCode
```
rpgCode( line) void string
```
Independently run a line of RPGCode.
run
```
run( program) void string
```
Transfer control to a different program.
save
```
save( file) void string
```
Save the current game state to a file.
savescreen
```
savescreen([ position = 0]) void int
```
Save the current screen onto a canvas that can be restored at a later time.
scan
```
scan( x, y, pos) void int int int
```
Save the tile specified to a buffer identified by pos. There is no particular number to pick for pos; any will do. @deprecated
send
```
send( file, x, y, [ z = 1]) void string int int int
```
Send the player to a new board.
setAmbientLevel
```
setAmbientLevel( red, green, blue) void int int int
```
Set the global ambient level. Valid values range from -255 to + 255.
setbutton
```
setbutton( file, slot, x, y, width, height) void string int int int int int
```
Create and draw a clickable button at screen pixel co-ords x, y that persists until clearButtons() is called.
setconstants
```
setconstants(...) void
```
Description.
setErrorHandler
```
setErrorHandler( lbl) void label
```
Set an error handler for the current function. This propagate up the call stack! Refer to the language features section of the manual for more information. *does not*
setImage
```
setImage( str, x, y, width, height, [ cnv]) void string int int int int canvas
```
Set an image.
setImageAdditive
```
setImageAdditive( file, x, y, width, height, percent[, cnv]) void string int int int int double canvas
```
Set an image with a tint of the specified percent.
setImageTranslucent
```
setImageTranslucent( file, x, y, width, height, [ cnv]) void string int int int int canvas
```
Set an image translucently.
setImageTransparent
```
setImageTransparent( file, x, y, width, height, r, g, b, [ cnv]) void string int int int int int int int canvas
```
Set an image with a transparent colour.
setMwinTranslucency
```
setMwinTranslucency( percent) void int
```
Set the translucency of the message window. 0% is invisible; 100% is opaque.
setPixel
```
setPixel( x, y, [ cnv]) void int int canvas
```
Set a pixel in the current colour.
setResumeNextHandler
```
setResumeNextHandler() void
```
Cause errors in the current function to be silently ignored. This propagate up the call stack! *does not*
setvolume
```
setvolume( percent) void int
```
Set the volume of all music and sound using a value between 0 and 100.
shopcolors
```
shopcolors( index, r, g, b) void int int int int
```
Set the colors used in CallShop(). This function is obsolete from 3.1.0.
sin
```
sin( x, [ &ret]) double double double
```
Calculate sine x.
smartStep
```
smartStep() void
```
Toggle "smart" stepping.
smp
```
smp( handle, value) void string int
```
Set a fighter's smp.
sound
```
sound() void
```
Obsolete.
sourcehandle
```
sourcehandle([ &ret]) string string
```
Get the handle of the source object.
sourcelocation
```
sourcelocation( &x, &y) void int int
```
Get the location of the source object.
spliceVariables
```
spliceVariables( str) string string
```
Replaces substrings within angle brackets by the value of variables with respective names.
e.g. "" would be replaced by the value of "x".
split
```
split( str, delimiter, arr) int string string array
```
Splits a string at a delimiter. Returns the number of upper bound of the array (i.e. the index of the last set element).
spriteTranslucency
```
spriteTranslucency( percent) void int
```
```
spriteTranslucency(void) int
```
Set the degree to which sprites drawn underneath other objects are visible. Specify a value between 0 (invisible) and 100 (opaque).
sqrt
```
sqrt( x, [ &ret]) double double double
```
Calculate the square root of x.
stance
```
stance( id [, player]) void int handle
```
Show a player stance. This command is obsolete - use playerStance() instead.
start
```
start( file) void string
```
Open a file with the shell.
There is unfortunately no default directory for this function and assuming one will only break backward compatibility in some obscure manner.
Note also that previous incarnations prevented the launching of executables and shortcuts, but this is a nonsensical security measure when plugins no longer display a silly warning box, and this function can be trivially modified by someone who intends to be malicious.
staticText
```
staticText() void
```
obsolete.
takeGp
```
takeGp( gp) void int
```
Take gold pieces.
takeItem
```
takeItem( itm) void string
```
Remove an item from the inventory.
tan
```
tan( x, [ &ret]) double double double
```
Calculate tangent x.
targethandle
```
targethandle([ &ret]) string string
```
Get the handle of the target object.
targetlocation
```
targetlocation( &x, &y) void int int
```
Get the location of the target object.
tellThread
```
tellThread( id, code) variant thread string
```
Execute code in the context of a thread (e.g., to run a method located in another thread). TellThread() returns the value returned by the function called in the thread.
text
```
text( x, y, str, [ cnv]) void double double string canvas
```
Displays text on the screen.
textSpeed
```
textSpeed( speed) void int
```
Obsolete.
thread
```
thread( file, persist, [ &ret]) thread string bool thread
```
Start a thread.
threadSleep
```
threadSleep( id, seconds) void thread double
```
Put a thread to sleep.
threadSleepRemaining
```
threadSleepRemaining( id, [ &ret]) double thread double
```
Check how much sleep remains for a thread.
threadWake
```
threadWake( id) void thread
```
Wake up a thread.
tileType
```
tileType( x, y, type, [ z = 1]) void int int string int
```
Change a tile's type. Valid types for the string parameter are "NORMAL", "SOLID", "UNDER", "NS", "EW", "STAIRS#". Do not use when using vectors - use vector tools instead.
trim
```
trim( str, [ &ret]) string string string
```
Trim whitespace from a string.
ucase
```
ucase( str, [ &ret]) string string string
```
Convert a string to uppercase.
underArrow
```
underArrow() void
```
Toggle the under arrow.
underline
```
underline( enable) void bool
```
Toggle underlining of text.
viewbrd
```
viewbrd( filename [, x, y [, cnv]]) void string int int canvas
```
Draw a board to the screen or to a canvas, starting at co-ordinates topX, topY.
wait
```
wait([ &ret]) string string
```
Wait for a key to be pressed, and return the key that was.
walkSpeed
```
walkSpeed() void
```
Obsolete.
wander
```
wander( target, [ restrict = 0]) void variant int
```
The first parameter accepts either a string that can be either "target" or "source" or the number of an item. The selected item will take a step in a random direction, or as restricted by the optional parameter. The allowed values for said parameter are:
- 0 - only north, south, east, and west on normal boards, only diagonals on isometric boards (default)
- 1 - only north, south, east, and west
- 2 - only diagonals
- 3 - all directions
wav
```
wav( file) void string
```
Play a wave file (e.g. a sound effect).
wavstop
```
wavstop() void
```
Stop the current sound effect.
win
```
win() void
```
Obsolete.
winColor
```
winColor( dos) void int
```
Set the message window's colour using a DOS code.
winColorRgb
```
winColorRgb( r, g, b) void int int int
```
Set the message window's colour.
windows
```
windows() void
```
Exit to windows.
winGraphic
```
winGraphic( file) void string
```
Set the message window background image.
wipe
```
wipe( file, effect [, speed]) void string int int
```
Wipe' a graphic to the screen. file: filename of the image to wipe to. effect: numeric value between 1 and 12. The valid types are: speed: default is 1, set higher to increase wipe speed.
- 1 - Right
- 2 - Left
- 3 - Down
- 4 - Up
- 5 - NW to SE
- 6 - NE to SW
- 7 - SW to NE
- 8 - SE to NW
- 9 - Right 'zelda' style
- 10 - Left 'zelda' style
- 11 - Down 'zelda' style
- 12 - Up 'zelda' style
zoom
```
zoom( percent) void int
```
Zoom into the centre of the board by the specified percent.
