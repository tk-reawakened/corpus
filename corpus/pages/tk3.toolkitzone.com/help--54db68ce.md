---
kind: page
id: "tk3.toolkitzone.com/tk3.toolkitzone.com/help/?page=4.2"
site: "tk3.toolkitzone.com"
title: "Open vs. closed vectors"
original_url: "http://tk3.toolkitzone.com/help/?page=4.2"
written: null
date_confidence: "unknown"
updated: null
captured: ["20071014202712"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/tk3.toolkitzone.com/help__page_4.2", captured: "20071014202712", sha256: "96861939e811ea0510740f9236c08666a530110dd18146206368b5d114ef026e", wayback_url: "https://web.archive.org/web/20071014202712/http://tk3.toolkitzone.com/help/?page=4.2"}
---

# Open vs. closed vectors

Vector overview [ | | | | ] [Board Basics](?page=4)
CollisionProgramGraphicalMovementCreating Vectors
This document provides an introduction to the Toolkit's vectors, including how they work, how to create them in the board editor, how to edit them in-game and how to optimise their usage.
Introduction To Vectors
Vectors have been introduced into the Toolkit in version 3.1.0 principally as an upgrade of the tile collision system. Previously, the smallest solid object that could be defined was a tile, which limited the interaction potential of the player with the game's environment; the same applied to programs. Vectors address this by allowing users to define arbitrary collision and interaction regions. Additionally, vectors lay the foundations for mouse-driven movement and the ability to move sprites along arbitrary paths.
So what are vectors? Put simply, a vector is a set of points connected by lines to form an open or closed shape. An open vector is one whose ends are not connected; the ends of a closed vector are connected, thus forming at least one internal area. Using a small amount of maths, between vectors can be detected - between sprites and board objects, or sprites and sprites - and the associated action or event triggered. An intersection is defined as either a crossing of edges or the complete containment of one vector by another. *intersections*
*Open vs. closed vectors*
*Intersecting vectors*
Applications
- : Vectors designated as collidable cannot be crossed or entered by other collision vectors. Sprites are given collision vectors ( ) to allow them to interact in this way.Collision *bases*
- : An RPGCode Program may be launched from a board when the player moves onto a program vector. The event occurs when the program vector intersects the player's . A Program associated with a sprite is launched when the player's collision base intersects the sprite's , which is distinct from the sprite's collision base.Program *collision base* *activation base*
- : Vectors may also be used to enhance graphical aspects of the game. "Under" vectors cause sprites that move within them to be drawn as if they are vertically under the area of the board the vector covers - this is the same effect as occurs when images or tiles are placed on layers above the layer the player moves on.Graphical
- : An easier way to script sprite movement than by supplying a large set of directions or coordinates is to supply the sprite with a waypoint vector along which to walk. Complex routines can then be created visually in the board editor.Movement
Collision Vectors
Sprite movement ends when a sprite's intersects another collision vector, be it a board vector or another sprite's collision base. When the player is controlled using the keyboard, the sprite may be seen to 'slide' along the edges of a board vector in an attempt to circumvent the object, if the angle between the movement direction and the edge is below a quarter turn. *collision base*
*Collision vectors*
Optimisation
As mentioned above, the intersection of two vectors can be calculated quite easily, but, depending on the numbers of points in the vectors, it can be quite a time-consuming operation. Whilst the of a vector itself has no bearing on the speed of the calculations, the of the vector is important. The of the vector is defined to be smallest rectangle that contains the vector, and computational time can be saved by only testing for an intersection when a sprite's collision base is inside a vector's bounding box. *shape* *size* **bounding box**
*The bounding box of a vector*
When the vector is made up of only a few points, there isn't a big difference, but when vectors contain a lot of points and a fair number of sprites are moving on the board, the difference may be appreciable. However, if large vectors are broken up into many small vectors, the engine may slow down because of an excessive number of bounding box checks when intersection checks may be faster. The best advice to give is to keep complex vectors smaller and simple vectors larger.
As an example of the issue, consider the following designs for the walls of a room; the first uses one large vector whose bounding box covers the entire floor of the room (please use your imagination to explain why the room has such deformed walls!). Wherever the player moves it will be inside the bounding box, and hence an intersection check against a large number of points is always performed. In the second design, the walls are broken down into four smaller vectors, and their bounding boxes leave the centre of the room uncovered. When the player moves around, an intersection check will either not be required or will be performed on a smaller number of points.
Note: the room could not be constructed from one closed vector, because the sprite would not be able to move inside the vector (its collision base would always intersect).
*Walls of a room made with one open vector (with bounding box)*
*Walls of a room made with four open vectors (with bounding boxes)*
Program Vectors
Board programs are launched when the player's collision base intersects the programs' vectors, when its activation base intersects (the player's activation base is presently unused). A program vector may be open or closed, and the same principle of complexity versus size when computing intersections applies (however, intersections are only evaluated for the selected player). A sprite's associated program is launched when the player's collision base intersects the sprite's activation base, but only when the player is moving - a sprite that walks up to the player (or another sprite) will not trigger its own program (or the other sprite's). **not**
*Program vector trigger*
*Sprite activation base trigger*
Board program vectors possess several features that control their interaction, including options to launch a program when the user presses the activation key (see ) whilst intersecting the vector, or to trigger the program repetitively (after a certain number of steps) whilst the player walks across the vector. For a full description of these options, see the . [Main File Editor](?page=3) [Board Editor](?page=4.1#righttoolbar)
Graphical (Under)
Vectors can be used graphically to provide the illusion that the player moves underneath them. Any board graphics bounded by an are drawn translucently over the player as he moves over the vector. Under vectors are, therefore, necessarily closed. *Under vector*
Two methods of interaction are available: vector intersection and frame intersection, toggled by the 'frame intersection' option on the right-hand toolbar in the Board Editor. Frame intersection causes the bounded graphics to be drawn translucently whenever the sprite's animation frame intersects the under vector; vector intersection causes the effect whenever the sprite's collision base intersects. The former emulates the function of layered images and tiles on higher layers; the latter enables sprites to move both in front of and behind objects whilst still on the same layer. Consider the following column on the background image. The player should be able to walk in front of the object without appearing beneath it, but should appear beneath it when behind it.
*Behaviour in vector intersect mode*
*Behaviour in frame intersect mode*
Note that in order to apply the effect to the background image, the 'Include Background Image' option must be enabled in the Board Editor.
Optimisation
Optimisation is a little different for under vectors: the number of points on an under vector is irrelevant to its performance - you can make it as detailed as you like, but its size is important. For each vector created an image canvas must be allocated in the computer's memory, as large as the vector's bounding box. If a vector's bounding box contains a lot of unbounded space, more memory than is strictly needed is being used. For instance, the following shape can be better represented using two under vectors:
*The bounding box contains large unbounded areas*
*Unbounded areas within the bounding boxes are reduced*
As before, a balance must be struck between the number of vectors use and their size. An excessive number of tiny vectors will be as inefficient as a couple of large vectors. Note that under vectors that intersect each other do not reduce the translucency of sprites that move over both at once.
Movement
Version 3.1.0 takes full advantage of the movement potential of vectors, through both pathfinding and scripting.
Pathfinding
Pathfinding routines are used to generate the shortest route between two points given a set of obstacles in between. In the Toolkit these obstacles are collision vectors and sprite collision bases. The most obvious use of pathfinding is for - the user clicks a point on the board and the player walks to it, avoiding any obstructions. If the destination cannot be reached, the player may attempt to get as close to the that point as possible. *mouse-driven movement*
Three different alogrithms are provided for pathfinding, each producing a different style of movement (see ). [Main File Editor](?page=3)
- Axial - Possible paths are confined to the axes of the board (e.g., North-South and East-West) and path points are restricted to tile centres.
- Diagonal - Possible paths are confined to the axes and diagonals and path points are restricted to tile centres.
- Vector - Paths may follow any direction (angle, or orientation) and visit any coordinates.
*Axial pathfinding*
*Diagonal pathfinding*
*Vector pathfinding*
Note that, presently, axial and diagonal pathfinding round all locations to tile-integral coordinates. This may cause scenes that are navigable in vector mode to be impassable in these modes, since sprite paths must coincide with tile-integral coordinates. The possible 'grid size' of diagonal and axial pathfinding may be changable at a later date, but it will be at the expense of performance.
Pathfinding may also be used explicitly through RPGCode; see the examples below.
Scripting
Up to version 3.0.6, movement could only be achieved by giving sprites directions in which to move, such as "South" or "NorthEast", using the Push() and PushItem() commands. In version 3.1.0, this movement system (one that does not involve coordinates) has been depreciated in favour of an movement system, relying on coordinates, in which sprite's movements are effectively stored as vectors (note that Push() and PushItem() are still valid). *relative* *absolute*
Two new functions are provided to handle this 'absolute' system:
There are three ways in which these may be used: to follow an explicit (coordinate-specified) path; to pathfind to a location; or to move on a waypoint vector. Firstly, the common code between these uses should be mentioned:
playerPath(variant handle, int flags, ...)
itemPath(variant handle, int flags, ...)
If you are unfamiliar with this , see the (this is code that can be run in the engine). The parameter is the same as found in other sprite functions; the parameter is something that hasn't been seen in RPGCode before. Flags are a simple way of controlling options without needing to add lots of boolean (true/false) optional parameters to the end of a function. Each option has its own , which is a with a particular value, assigned in such a way that multiple flags can be passed to a function through one parameter. The user does not need to define flags, they are allocated by the engine. Flags can be combined using the boolean OR operator "|"; the order of combination is unimportant. *function definition notation* [RPGCode reference](?page=18.3) **not** *handle* *flags* **flag** [reserved constant](?page=18.6)
playerPath("default", FLAG_1);
playerPath("default", FLAG_2 | FLAG_3);
flags = FLAG_1 | FLAG_2 | FLAG_3;
playerPath("default", flags);
playerPath("default", 0);
If no flags are required, pass a zero. Functions that accept flags will only accept a specific set and combination of flags, the details of which are described in the RPGCode function reference. PlayerPath() and ItemPath() have two basic flags that may be used in any of their three applications:
tkMV_CLEAR_QUEUE
tkMV_PAUSE_THREAD
playerPath("default", tkMV_CLEAR_QUEUE | tkMV_PAUSE_THREAD);
As mentioned, sprite paths are now stored as vectors, or more specifically, queues. A sprite may have a queue of points that it must visit in turn. When a sprite receives a new set of points to move to, those points are placed at the end of its queue; if it is moving at that time, the current set of movements will be preserved. To clear these current movements, include the tkMV_CLEAR_QUEUE flag.
Movement can occur in threads; in 3.0.6 a thread's execution continues immediately after a movement command is called, when the movement itself finishes. This may cause some undesirable effects. Therefore you can include the tkMV_PAUSE_THREAD flag to make the thread execution halt until the movement is complete. When movement occurs in a non-threaded program, program execution automatically halts until the movement ends, unless is used. **not** [multiRun()](?page=19#multirun)
As for the three specific uses:
- Explicit path: The sprite walks between the points specified by (x1, y1) to (xn, yn). The ellipsis (...) indicates that any number of coordinate pairs may be specified. For instance: The sprite will walk in straight lines (i.e., vectorially, not diagonally or axially) between the points; that is, it will pathfind between them. As a result, the sprite will disregard any board collision vectors and (though not other sprites).
itemPath(variant handle, int flags, int x1, int y1, ... , int xn, int yn)
itemPath(0, tkMV_CLEAR_QUEUE, 35, 100, 60, 122, 208, 154, 400, 78);
*not* *walk straight through them*
- Pathfinding: Here, indicates that the tkMV_PATHFIND flag must be specified, optionally along with any other compatible flags (i.e., tkMV_CLEAR_QUEUE and/or tkMV_PAUSE_THREAD). The sprite will pathfind to the supplied coordinate (x1, y1), for example:
itemPath(variant handle, int flags | tkMV_PATHFIND, int x1, int y1)
*flags | tkMV_PATHFIND*
itemPath(0, tkMV_PATHFIND, 400, 78);
playerPath("default", tkPAUSE_THREAD | tkMV_PATHFIND, 400, 78);
- Waypoint path: Sprites may walk along board vectors denoted as 'waypoints'. To achieve this, include the tkMV_WAYPOINT_PATH or tkMV_WAYPOINT_LINK flags (but not both; these flags are incompatible with the tkMV_PATHFIND flag, but not the basic flags). Refer to the board path (waypoint vector) using either its slot index or vector handle, both found on the in the Board Editor. specifies the number of times to walk around the vector. If the vector is open, movement will end at the last point, if closed it will end at the first point. The sprite will pathfind to the first point of the vector if it is located elsewhere. If the tkMV_WAYPOINT_PATH is used The points of the waypoint vector are copied into the sprite's queue and the player is in no way linked to the vector. Here, the sprite walks around the vector with handle "wpCircle" twice. Here, a link is made between the sprite and the vector whose index is 1. The points of the vector are added to the sprite's queue individually as each section is completed. The benefit of this link is threefold: first, the sprite can infinitely walk the vector by specifying zero cycles. Second, any changes to the waypoint vector propagate to the sprite's movements. Third, the sprite will that it is walking the path; that is, the user can pass a set of new movement commands to the sprite, which will resume the waypoint path once those movements have been completed. For example, the waypoint path may be set as a sprite's multitasking program with a movement command set in its activation program: Note that the call in the activation program must include the tkMV_CLEAR_QUEUE flag for this to work. The link between vector and sprite is broken when the specified number of cycles is complete. In the case of an infinite path, pass -1 as the waypoint vector handle:
itemPath(variant handle, int flags | tkMV_WAYPOINT_PATH, variant boardpath, int cycles)
itemPath(variant handle, int flags | tkMV_WAYPOINT_LINK, variant boardpath, int cycles)
playerPath("default", tkMV_WAYPOINT_PATH, "wpCircle", 2);
itemPath(2, tkMV_WAYPOINT_LINK, 1, 2);
*remember*
// Multitasking program.
itemPath("source", tkMV_WAYPOINT_LINK, "wpCircle", 0);
// Activation program.
itemPath("source", tkMV_CLEAR_QUEUE | tkMV_PATHFIND, 256, 384);
itemPath("source", tkWAYPOINT_LINK, -1, 0);
The coordinates stored in a sprite's queue can be obtained using or . For instance, [playerGetPath()](?page=19#playergetpath) [itemGetPath()](?page=19#itemgetpath)
count = playergetpath(0);
for (i = 0; i < count; ++i)
{
playergetpath(0, i, x, y);
mwin(x + ", " + y);
}
outputs the player's pending movements to the screen.
As previously mentioned, itemPath() and playerPath() supersede the previous movement functions push(), pushItem(), playerStep(), itemStep() and pathfind(); however these may still be used. Push(), playerStep() and corresponding item functions may also take the basic movement flags outlined above through an optional parameter with similar effect:
// void playerstep(variant handle, int x, int y [, int flags])
// void push(string direction [, variant handle [, int flags]])
playerStep(0, 120, 233, tkMV_CLEAR_QUEUE);
push("S,S,S", "default", tkMV_CLEAR_QUEUE | tkMV_PAUSE_THREAD);
Note that in playerStep(), x and y are interpreted based on the board's Pixel Absolute setting. Pathfind() should no longer be used for pathfinding; use playerPath() with tkMV_PATHFIND instead. Pathfind() only returns a directional string and hence only pathfinds in axial mode.
*A sprite walks a waypoint vector. When it encounters a sprite blocking the path, it pathfinds around the sprite and resumes the waypoint vector path.*
Creating Vectors
In The Board Editor
Making vectors in the board editor is a quick and intuitive process, with lots of mouse and keyboard shortcuts to help you out. After laying down some graphics, select the Vector Editing tools option in the left toolbar, and select the Draw tool from the second set of icons (when changing toolsets, the active tool defaults to Select). Then, to start drawing, left-click and release on the board to place the first point. A dashed line now connects the first point to the cursor.
*1. Vector tools, 2. Draw tool, 3. First point.*
To place the second point, left-click again. To delete the vector, right-click (after the first point only). Once the last point has been placed, right-click to close the vector: the last and first points are connected. To finish an open vector, right-click whilst holding the Ctrl key down.
*Second point*
*Last point*
*Right-click to close*
*Ctrl + Right-click to leave open*
If the board's includes the Pixel Absolute setting, vector points will be created at the exact mouse location; if it is not included, vector points will snap to the closest grid point. In order to invert this feature, hold down the Ctrl key while placing points. In order to draw lines that are aligned to the axes and diagonals, hold down the Shift key whilst placing points. Rectangles can be drawn straight off using the Rectangle tool found below the Draw icon. In isometric mode, these rectangles are rotated accordingly. [coordinate system](?page=4#coordinates)
*Hold Ctrl to invert snap-to-gridpoints*
*Hold Shift to align to axes*
*Rectangle tool in isometrics*
In order to edit vectors, use the Select tool. Left-clicking the board will select the vector with the nearest point (not line). The selected vector is highlighted with a thick outline. Left-clicking and dragging creates a selection box; a number of operations can be performed on the points within the selection box: left-click-drag to move the selected points; press the Delete key to erase the points; press Z to subdivide an edge; press X when the first or last points are selected to resume drawing. *of the selected vector*
*Selection box*
*Move points (drag)*
*Subdivide edge (Z)*
*Resume drawing (X)*
Similar tasks can be achieved in Draw mode whilst holding the Alt key down and left-clicking.
- Clicking near a point deletes that point.
- Clicking near a line subdivides that line, adding a point at the mouse location.
- Click away from a point or line resumes drawing from the last point
In this context, 'near' means 'within 16 pixels'.
These principles also apply to program vectors. For further command options, see . [Around The Editor](?page=4.1)
Using RPGCode
A number of new functions are provided to access board vectors and programs. Due to the nature of RPGCode it is necessary to access a vector's points individually (rather than by array or other method), hence single-point access functions are given.
To get the properties or points of a vector, pass variables to boardGetVector() or boardGetVectorPoint(), respectively; for instance,
boardGetVector(0, type, points, layer, closed, attributes);
if (points > 3)
{
boardGetVectorPoint(0, 3, x, y);
mwin("The fourth point is (" + x + ", " + y + ")");
}
may display . Note that point indexing starts at zero, and that points are always specified in pixels regardless of the Pixel Absolute coordinate setting. *The fourth point is (123, 456)*
To create a vector, first call boardSetVector(), followed by boardSetVectorPoint() for each of the vector's points. Set 'apply' to true for the last point to update pathfinding information.
// boardSetVector(variant vector, int type, int pointCount, int layer, bool isClosed, int attributes)
// boardSetVectorPoint(variant vector, int pointIndex, int x, int y, bool apply)
boardSetVector("newHandle", tkVT_UNDER, 4, 1, true, tkVT_BKGIMAGE);
boardSetVectorPoint("newHandle", 0, 32, 32, false);
boardSetVectorPoint("newHandle", 1, 64, 32, false);
boardSetVectorPoint("newHandle", 2, 64, 64, false);
boardSetVectorPoint("newHandle", 3, 32, 64, true);
Possible type and attribute (flags) constants:
type = tkVT_SOLID, tkVT_UNDER, tkVT_STAIRS, tkVT_WAYPOINT
attributes = tkVT_BKGIMAGE | tkVT_ALL_LAYERS_BELOW | tkVT_FRAME_INTERSECT
The attribute flags apply to under vectors only. For stair vectors, set the attribute parameter as the destination layer.
The same principles apply to program vectors. New programs must be created in the one-past-last slot (programs do not currently have handles). The value of the one-past-last slot can be obtained using boardGetProgram():
// boardSetProgram(int programIndex, string program, int pointCount, int layer, bool isClosed, int attributes, int distanceRepeat)
newIndex = boardGetProgram();
boardSetProgram(newIndex, "program.prg", 6, 1, false, tkPRG_STEP | tkPRG_REPEAT, 100);
boardSetProgramPoint(newIndex, 0, 32, 32);
// etc.
initialises a new program in the next board slot. The following flags are valid for attributes:
attributes = tkPRG_STEP | tkPRG_KEYPRESS | tkPRG_REPEAT | tkPRG_STOPS_MOVEMENT
Either tkPRG_STEP or tkPRG_KEYPRESS should be supplied; other flags are optional. Specify a positive value to distanceRepeat if tkPRG_REPEAT is specified. See the section of the Board Editor for more information. [right-hand toolbar](?page=4.1#righttoolbar)
For further information on vectors, please see the and pages. [Board Basics](?page=4) [Around the Editor](?page=4.1)
*— Delano*
