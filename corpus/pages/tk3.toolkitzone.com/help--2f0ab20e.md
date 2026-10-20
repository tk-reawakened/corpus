---
kind: page
id: "tk3.toolkitzone.com/tk3.toolkitzone.com/help/?page=4.1"
site: "tk3.toolkitzone.com"
title: "Around The Editor [ | | | | ] Board Basics"
original_url: "http://tk3.toolkitzone.com/help/?page=4.1"
written: null
date_confidence: "unknown"
updated: null
captured: ["20081008233301"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/tk3.toolkitzone.com/help__page_4.1", captured: "20081008233301", sha256: "384240dacb46907c58788126eea773f160006844e0ee63d62b0489e1fbb5aabc", wayback_url: "https://web.archive.org/web/20081008233301/http://tk3.toolkitzone.com/help/?page=4.1"}
---

# Around The Editor [ | | | | ] Board Basics

New Board WindowLeft-hand ToolbarRight-hand ToolbarPropertiesMenus
The board editor may be broken down into a number of sections: the New Board screen, the Board and Properties tabs, the left-hand toolbar, the right-hand toolbar and the menus.
New Board screen
After opening the board editor (see for ways to do this), you will be presented with the 'New Board' options window, which allows you to specify the properties of the new board. [Editor Environment](?page=ed_environment)
- The option buttons allow you to either choose a new set of parameters or to load a pre-existing board - for instance, you could create a template board with a number of common properties and specify it here.
- The coordinate system choices specify the grid and perspective of the board; see the for a description of the choices. Once the coordinate system is set you cannot alter it, except to upgrade from isometric stacked to rotated, or from tile to pixel (see Menu below). [Board Basics page](?page=4)
- The X and Y dimensions are always specified in tile values, even if the 'Use pixel coordinates' option is ticked. The resulting pixel dimensions of the board are specified below the tile dimensions.
- The Background Image may be any type of non-tile image file, and is drawn below the first layer of tiles.
- This window remembers all its settings, so if you tick the 'Do not show this form on startup' box, a new board will be automatically created with the last set of parameters. To reshow the form, choose the relevant option in the Board > Preferences... menu.
Board Tab
After selecting 'OK' on the New Board window, a black area will appear in the middle of the screen (unless a background image or pre-existing board was selected!); this is the board showing its default background colour.
Left-hand Toolbar
The toolbar on the left-hand side contains the tools used to draw and edit the various objects placed on the board. Each button has a keyboard shortcut key, denoted in brackets.
The first is a set of general tools:
Grid On/Off (G) - Toggles drawing of the tile grid.
Undo (Ctrl+Z) - Undoes the last user operation. Only the most relevant operations are undoable; a multiple-undo stack is maintained, so multiple operations up to a particular number can be undone.
Toggle Auto-Tiler (H) - Auto-Tiling is an option found in some RPG makers that uses specially drawn and arranged tilesets to make the task of creating bounded tile areas simpler. To use this feature you must have an auto-tile tileset open. This option turns auto-tiling on or off - turned off, you can place auto-tiles normally, when turned on any tiles placed form enclosed areas dependent on their neighbouring tiles. Auto-tilesets must either be downloaded or created using the "Auto-Tiler" tool - follow for more information. [this link](http://toolkitzone.com/fileman.php?id=3&file=865)
The second group of tools are associated with creating and editing each particular object type. The buttons are interlinked so that only one can be selected at any one time. The specific action on each object is then determined by the selected button in the third group. When one of the last six buttons is selected (vector to lighting), the currently selected object of that type is highlighted on the board, indicated either by a thick line for vectors or a bounding box for sprites and images.
Scroll board (Q) - Allows the board to be scrolled using the mouse buttons. Left-click and hold (LMB) on the board and drag the mouse to scroll the board. Tip: Scrolling can also be achieved at any time by using the mouse wheel. Scrolling the wheel causes either horizontal or vertical scrolling; clicking the middle mouse button/wheel (MMB) switches between horizontal or vertical scrolling. The Scroll board tool need not be selected to do this.
Zoom (W) - Allows the board to be zoomed in or out. LMB zooms in, right-click (RMB) zooms out. A finite number of zoom levels are provided. Tip: Zooming can also be achieved by scrolling the mouse wheel whilst holding the Ctrl key down. The Zoom tool need not be selected to do this.
Tile tools (T) - Selects tile editing. Note the current tileset can be opened in a pop-up browser by pressing the 'L' key.
Vector tools (V) - Selects vector editing (including collision and waypoint, excluding program).
Program tools (P) - Selects program vector editing (excluding threads).
Sprite tools (S) - Selects sprite (item) editing.
Image tools (I) - Selects image editing (excluding background image).
Shading tools (Y) - Selects tile shading editing (excluding ambient levels and lighting).
Lighting tools (U) - Selects light editing (excluding ambient levels).
The third is a group of generic tools whose function and action depend on the selected button of the second group. Note: when the selected button in the second group is changed, the selected tool in the third group defaults to Draw. Not all tools are applicable to all objects, those that are not are disabled when the object's button is selected.
Draw (D)
- Tile:
- LMB - Places the currently selected tile on the selected layer at the location clicked. If a tile bitmap (.tbm) is selected, the tiles of the tbm are placed onto the board, with the top-left tile placed at the location clicked. The tile bitmap itself is not associated with the board in any way.
- Vector, Program:
- LMB - Creates a new vector and sets the first point by entering 'drawing mode'. A dashed line extends to the mouse pointer, and subsequent LMB clicks draw new points on the vector. If the coordinate system is not in pixels, vector points are placed at gridpoints.
- RMB - If in 'drawing mode', a RMB the vector by joining the first and last points and exits drawing mode (a subsequent LMB will start a new vector). A LMB near the first point does not have the same effect. *closes*
- RMB+Ctrl - If in 'drawing mode', exits drawing mode without closing the vector.
- LMB+Ctrl - If in a pixel coordinate system, causes vector points to snap to gridpoints; if in tile coordinate system, prevents snap-to-gridpoints.
- LMB+Shift - If in drawing mode, aligns the next point to the nearest axis or diagonal.
- LMB+Alt - When not in drawing mode, edits the selected vector in the following ways:
- If click is near a point, the point is deleted (where 'near' means within ~16 pixels).
- If click is near a line and far from a point, the line is subdivided and a new point is created.
- If click is far from a line, drawing mode is entered and a new point added to the end of the vector and the vector is unclosed.
- Sprite, Image, Light:
- LMB - Creates a new sprite, image or light, respectively. The new object is blank or is given the default parameters for its type. Blank sprites and images are represented by 32x32 pixel black or white squares. If tile coordinates are selected, a sprite is aligned to the grid. Lights are represented by vectors as well as by the shades they cast.
- Shading:
- LMB - Places the currently selected shade on the shading layer at the location clicked. If any tiles are on layers below the shading layer at the same location, the shade is applied to them.
Select (A)
- Tile:
- LMB+drag
- Creates a selection box that resizes to align with the grid.
- Performed on a selection box, causes the selected tiles to be moved to the new location (equivalent to a Cut-Paste operation).
- LMB+Ctrl+drag on a selection causes the original tiles to be preserved (equivalent to a Copy-Paste operation).
- RMB - Erases the selection box.
- Vector, program:
- LMB - Highlights (selects) the nearest vector (by the nearest point, rather than line).
- LMB+drag - Draws a selection box. If any points of the selected vector fall inside the box, a number of operations can be performed on these selected points.
- LMB+drag - Moves/drags selected points.
- (Del, Backspace) - Deletes selected points.
- (Z) - Subdivides selected lines. If two or more consecutive points are selected, new points are created at the midpoints of selected lines.
- (X) - Extends selected point. If the vector is not closed and the start or end point is selected, drawing mode is entered beginning from the selected point.
- RMB - Erases the selection box.
- Sprite, Image:
- LMB - Highlights (selects) the targeted object.
- LMB+drag - If originating within the selected object's bounds, drags/moves the selected object. If in tile coordinates, sprites are forced to align to the grid.
- Shading: Controls are identical to the tile controls listed above.
- Lighting: Light vectors can be edited in the same way as other vectors with the exception that points cannot be added or deleted.
Flood (F)
- Tile, Shading:
- LMB - Floods the selected bounded area with the current tile or shade.
Erase (E)
- Tile, Shading:
- LMB - Erases the selected tile or shade.
Rectangle (R)
- Tile, Shading: Note: Unavailable in Stacked Isometric mode.
- LMB - Draws a hollow rectangle with the selected tile or shade.
- LMB+Ctrl - Draws a filled rectangle.
- Vector, Program:
- LMB - Creates a new, rectangular closed vector (rotated to align with axes in isometric mode).
Dropper (O)
- Tile, Shading:
- LMB - Sets the selected tile or shade.
The fourth group of tools control the visibility of the board.
Current layer - Selects the current layer, onto which tiles, vectors, programs, sprites, items and images are drawn.
Toggle visible layers - A list of layers and their visibility status. An asterisk next to a layer number indicates the layer as visible. Click a layer on the list to toggle its visibility. The current layer cannot be hidden. 'B' denotes the background image.
Hide all layers except current (J) - Overrides the visible layers list.
Show all layers (K) - Overrides the visible layers list.
Selected tile - Click on the box to change the selected tile. Possible types that can be placed are *.tst, *.iso, *.tan (animated tile) and *.tbm (tile bitmap).
Right-hand Toolbar
The right-hand toolbar contains three permanent buttons that are described on the . When the board editor is open, a fourth button appears - this is the , and displays the properties of all the objects on the board. The toolbar has five tabs, one for each object group: vectors, programs, sprites, images and lighting. Selecting one of these tools from the left-hand toolbar causes the matching tab to be shown on the Board Toolbar. The first four tabs contain a drop-down box listing all the current objects of that type on the board. The properties of the selected object are then displayed in the panel below. Each of the first four tabs also contains a checkbox to toggle whether the objects of that type are displayed in the board editor, and a 'Delete' button to erase the currently selected object. The currently selected object is highlighted if the object type's button is selected in the left-hand toolbar. If no objects of the type exist, all controls on the tab are disabled. [Editor Environment page](?page=ed_environment) *Board Toolbar*
Tip: The Board Toolbar can be hidden or shown using the Ctrl+B shortcut. The tileset toolbar can be hidden or shown using Ctrl+L. A pop-up tileset browser can also be displayed by pressing L when the board has the focus.
Vectors (Alt+V)
- The vectors tab displays information for all vector types except programs.
- The drop-down list displays the and of the each vector. Both index and handle can be used to access a vector in RPGCode. Click the text area of the drop-down list to begin entering a new handle for the current vector (do not enter the index or colon first, these are automatically added). Two vectors cannot share the same index or handle. *index* *handle*
- Solid, under, stairs and waypoint: valid vector types; see for a full a description of each. [link](?page=4.2)
- Closed vector: Determines whether the vector forms a closed loop or not.
- Include background: A sprite standing on an under-vector on any layer will appear 'behind' the background image, if one exists.
- Include all layers below: A sprite will appear behind any tiles or images on any layers below an under-vector, in addition to those on the current layer.
- Trigger on frame intersect: The sprite will appear behind an under-vector area when its intersects the vector, rather than its collision vector. See for an example of its usage. *image frame* [this link](?page=4.2)
- Layer: layer the vector is located upon; sprites will only interact with a vector if it is on the same layer as the sprite.
- Stairs to layer: Layer to move sprites to when they intersect a stair-vector.
- Slot index: The numeric index of the vector on the board, as shown in the drop-down list. Use the buttons to move the current vector up or down in the list.
- Points list: a list of the vector's points in pixel coordinates. In order to change a point's coordinates: To delete a point, click the point's index in the first column and press the Delete or Backspace key. Vector points are always stored in pixel coordinates regardless of the board's coordinate system.
- click the value to be changed;
- press the Delete or Backspace key;
- enter the new coordinate;
- press the Enter key.
Programs (Alt+P)
- Once a program's vector has been drawn, it becomes listed in the program tab's drop-down list.
- The drop-down box lists the program index and filename/inline RPGCode of each program. It cannot be edited via the drop-down box. If no filename/code is given '' is displayed, and the program will not be loaded in the engine.
- Program filename/inline RPGCode: Specify a program's filename or a line of RPGCode to run when the program is activated. Use the '...' button to the right to browse for programs, and the blank button below to open the program, if the file exists. When specifying a program, it must exist within the game's 'Prg\' folder or subfolders within it. If the program is in a subfolder then subfolder's name must also appear in the textbox (e.g., for the file 'Prg\system\pause.prg', the text 'system\pause.prg' should be written). When specifying subfolders, only the '\' slash is valid; the '/' is not. These principles apply when choosing any files in subfolders throughout the Toolkit.
- Layer: layer the program is located upon; players will only interact with a program if it is on the same layer as the player.
- Activation by step-on: The program will run as soon as a player walks onto (intersects with) the program's vector.
- Activation by key-press: The program will run only when the player is standing on or in the program's vector and the user presses the activation key (see ). [Main File Editor](?page=3)
- Trigger every x pixels: Causes the program to run after a player has walked a given number of pixels in or on a program vector. When the user leaves the vector, the count is reset.
- Activation stops movement: Running the program causes the player to stop moving (for instance, when using mouse movement).
- Run once: Causes the program to be run only once for the entire duration of the game.
- Run program if variable 'x' = 'y': Causes the program to be run only if the RPGCode variable specified in the first box has the value specified in the second box. Cannot be used in conjunction with the 'Run Once' checkbox.
- After program finishes, set variable 'x' = 'z': Optional - when the program ends, the RPGCode variable named in the first box is given the value in the second.
- Points list: see the vector points list, above.
Sprites (Alt+S)
- The drop-down box lists the item index and filename of each sprite, the text field cannot be edited. If no filename is specified, '' is displayed.
- Sprite filename: Filename of the item (players cannot currently be specified). Click the '...' button to browse for an item, and the blank button to open the file, if it exists.
- Location: The x, y and layer coordinates of the sprite. Given in tile coordinates unless using pixel coordinates. If using tile coordinates, sprites are 'snapped' to the grid. When using pixel coordinates, the x, y values refer to the bottom-centre of the sprite's frame. For historical reasons, in isometric mode, the y-value is offset down by 8 pixels.
- Slot index: The numeric index of the sprite on the board, as shown in the drop-down list. Use the buttons to move the current sprite up or down in the list.
- Override program to run on activation: Specify a program or a line of RPGCode to run when the user interacts with the sprite, instead of any program specified in the item's Board Options (see ). [Item Editor](?page=8)
- Override multitasking program: Specify a program or a line of RPGCode to run whilst the sprite is on the board, instead of any program specified in the item's Board Options.
- Activation by step-on: The sprite's activation program will run as soon as a player walks into (intersects with) the sprite's activation vector (see ). [Item Editor](?page=8)
- Activation by key-press: The sprite's activation program will run only when the player is standing on or in the sprite's activation vector and the user presses the activation key (see ). [Main File Editor](?page=3)
- Show sprite when board loads if variable 'x' = 'y': Causes the sprite to be visible only if the RPGCode variable specified in the first box has the value specified in the second box. The sprite's data is still loaded and the sprite can be shown at any time using PutItem().
- Run program if variable 'x' = 'y': Causes the sprite's activation program to be run only if the RPGCode variable specified in the first box has the value specified in the second box.
- After program finishes, set variable 'x' = 'z': Optional - when the sprite's activation program ends, the RPGCode variable named in the first box is given the value in the second.
Images (Alt+I)
- The drop-down box lists the image index and filename of each image, the text field cannot be edited. If no filename is specified, '' is displayed. The background image is not listed here, see the Properties Tab below.
- Image filename: Filename of the image, see the relevant comments about the Program filename field for subfolder information.
- Location: x, y and layer coordinates of the image. The x and y values refer to the top-left corner of the image and are always given in pixel coordinates.
- Transparent colour: The transparent colour on the image. To set the transparent colour, click 'Select' and then click on the area of the image on the board that you wish to be transparent. When using some image formats (such as jpg), you may find that only parts of the transparent area become transparent; this is due to image compression altering the values of the other areas. You will need to resave your image at a higher quality or in a different format to rectify this issue.
Lighting (Alt+L)
The lighting tab contains information for both tile shading and lighting.
- Cast onto tiles on layer x and below: specifies the layer above which the tile shading layer and any lights are positioned. This style of lighting and shading cannot be applied to images and cannot be applied at a sub-tile level.
- Lighting: the first drop-down box lists the current lights on the board by their index and light type. The selected light is displayed here, and if the lighting button is selected on the left-hand toolbar, the selected light's vector is highlighted on the board.
- The smaller drop-down box lists the possible light types of the current light. These are:
- Elliptic spotlight: Creates a circular or elliptic spotlight defined by three points and two colours. Its vector consists of two lines defining the semi-major and semi-minor axes (whichever is longer and shorter, respectively). The angle of the semi-minor axis with respect to the semi-major is immaterial, only its length is used. One colour is applied to the centre of the ellipse and one to the boundary, and all points in the ellipse are shaded with a gradated mix of the two colours.
- Gradient: A linear gradient that fills the whole screen, defined by two points and two colours. The gradient is applied in parallel to the line joining the points, extending perpendicularly across the whole board. Beyond either point, the board is shaded with the colour of the closer point.
- Clipped gradient: Similar to Gradient, the Clipped gradient extends perpendicularly across the whole board, but is clipped in the parallel direction at either point.
- The next section defines the colours of the current light.
- A colour box displays the shade.
- '...' button sets the shade for this point to the Current Shade (see below).
- The accompanying text describes the associated point of the light and its RGB (red, green, blue) value.
- Convert: Converts the light to tile shading by rendering the light to the tile shading layer. The light is combined additively with any current tile shading and the light object is removed from the board. Once the light is removed, its shape cannot be altered.
- Delete: Removes the current light from the board.
- Current Shade: displays the shade used for drawing tile shading and for assigning shades to lights.
- RGB textboxes: Individual RGB values can be input in the range -255 to +255. Positive numbers lighten tiles and negative numbers darken.
- Slider: Sets the RGB to the same value.
- Zero RGB: Sets the RGB to [0, 0, 0].
Properties Tab
The properties tab displays miscellaneous attributes of the board not associated with the objects listed above.
- Directional links: When the player reaches the edge of a board they may move to a new location. One way of doing this is to specify a directional link for that edge of the board; one textbox is provided for each edge or direction. A program may instead be run when the player reaches the edge. Click the '...' button to browse for a board or program file, and the blank button to open the file, if it exists.
- Background image: Specify a non-tile image for the background; click the '...' to browse for a file (files must be located in the 'Bitmap\' folder or subfolders therein.
- Background color: The colour of the board beneath the background image and tiles, defaulting to black. Click the '...' to select a colour.
- Background music: Specify a music file that plays and loops for the duration the player is on the board; click the '...' to browse for a file (files must be located in the 'Media\' folder or subfolders therein.
- Threads: As mentioned in , threads are programs that are run in the background of the game and allow gameplay to continue whilst they execute, in contrast to other programs. A set of board threads may be specified here that are launched when the board is entered and terminated when the board is left, unless they have already done so. Use the 'Add...' and 'Remove' buttons to create or delete board threads, and the 'Open' button to open the selected file, if it exists. [Board Basics](?page=4)
- Dimensions: Width and Height describe the dimensions of the board in at all times. The coordinate system types are displayed but cannot be altered (except through the menu option, see below). *tiles*
- Constants: Two arrays of RPGCode constants may be defined on a board. One is a set of generic constants that can be used to hold any data, entitled 'constant[x]' where x is a number (see ). The second is a set of strings that may hold the names or titles for each layer (but may hold anything else you need), entitled 'boardtitle[x]' where x is a number. To create a new constant, select the blank entry from the end of the drop-down list. The number of boartitle[] constants is fixed to the number of layers (when changing the number of layers, switch back to the Board tab to update this list). The value of the selected constant is displayed in the accompanying textbox. [RPGCode Reference](?page=18.5)
- Battle settings:
- Enable fighting on this board: Check this box to allow random battles to occur at the frequency or probability determined in the . [Main File Editor](?page=3)
- Board skill: Sets the skill level of enemies encountered during random battles, as assigned to enemies in the Main File Editor.
- Battle background: The .bkg background file to display when running random battles.
- Disable progress saving: one can prevent players from saving their game on the current board by enabling this option - for instance, if you don't want them to be able to save during a series of battles. With this option enabled, the "Save" option in the default menu is inactive.
- Program to run when entering board: set this if you want a program to run as soon as the player steps onto the board, before he is allowed to move. Note that any board threads are launched before this program is run.
- Ambient RGB: A uniform shade that is applied to the board. These values combine additively with the global Ambient Level applied through setAmbientLevel(). Individual red, green and blue values are specified in the range -255 to +255, where negative numbers darken and positive numbers lighten the scene. Useful for creating dark rooms, for instance.
Menus
Edit
- Undo (Ctrl+Z): Undoes the last action; a multiple undo stack is provided storing a certain number of previous changes. Not all operations are undoable.
- Redo (Ctrl+Y): Redoes an Undo action.
- Copy (Ctrl+C): Copies the selected object to the board clipboard. A selection of the desired object(s) must be made using the Selection tool on the left-hand toolbar. The object type corresponding to the selected object button on the left-hand toolbar is copied. Groups of tiles and shades can be copied, or whole vectors, programs sprites and images. Partial vectors (point groups) and lights cannot be copied. In addition, text in textboxes can be copied, cut and pasted from outside the editor.
- Cut (Ctrl+X): Cuts the currently selected object.
- Paste (Ctrl+V): Pastes the current object on the clipboard.
- Select All (Ctrl+A): Creates a selection box around the current object, or around the whole board (in tile or shading mode).
Board
- Preferences (Ctrl+F): Board editor preferences applied to all boards.
- Color options: Lists the colours used to display particular objects in the editor. Click the colour itself to choose a new colour.
- Revert to draw after flooding: After flooding tiles or shades, the current tool switches to Draw.
- Show vector indices: Draw numbers by the points of vectors.
- Use recursive flooding: If you experience problems with the flood tool, such as tiles being erased rather than placed, enable this option. This may happen on earlier versions of Windows. Note that with this option enabled, you cannot flood large boards (approximately greater than 100x100). This option is linked to the option in the . [Tile Editor](?page=5)
- Show New Board dialog window: Show the New Board window when opening the board editor.
- Show player start location on initial board only: display the starting location only if the board's name matches the initial board specified in the main file editor, otherwise the start locations (if defined) are displayed on each board.
- Set Player Start Location (Ctrl+D): Use this to set the location where the player will begin at the beginning of the game. Choose this option and then click the required position on the board. The location is highlighted by a cross and text detailing the chosen layer. If tile coordinates are used, the location will snap to a grid square.
- Set As Initial Board (Ctrl+G): Alters the initial board field in the main file to the current board's name.
- Convert Coordinates
- to isometric rotated (Ctrl+I): Converts isometric stacked boards to isometric rotated.
- to pixel (Ctrl+P): Converts from tile-based coordinates to pixel.
- Export Image
- Current Screen: Saves the currently visible board area in an image file. The image appears exactly as the board appears in the editor. Possible filetypes are png, jpg and bmp.
- Entire Board: Saves the entire board to an image file. The image will not include vectors, programs, gridlines, object outlines or scaling for zooming. It will include sprites, images and shading unless disabled in the Board Toolbar tabs.
