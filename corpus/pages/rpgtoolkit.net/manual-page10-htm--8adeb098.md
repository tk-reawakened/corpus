---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/manual/page10.htm"
site: "rpgtoolkit.net"
title: "[ ]Toolbars"
original_url: "http://rpgtoolkit.net/manual/page10.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20120618021039"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/manual/page10.htm", captured: "20120618021039", sha256: "66c1feac2d41903743658344447dd4e609e66a31a0816baa63f3b91e52ecb07b", wayback_url: "https://web.archive.org/web/20120618021039/http://rpgtoolkit.net/manual/page10.htm"}
---

# [ ]Toolbars

Animation Basics
Animations (*.anm) are simply a sequence of 'still' images that are displayed consecutively to give the impression of motion, just like films or television. Animations are used for player and item movements, player and enemy actions in battles, and can be used for animated intro sequences and menu objects.
Animations can be composed of image files, such as jpg or gif or tiles, or (collections of tiles). The format itself only consists of links to the frame images rather than the images themselves, so the Toolkit keeps the images you include in the game's \Bitmap folder. [Tile Bitmaps](page11.htm)
Note regarding animated gifs: As of 3.1.0, animated gifs are supported wherever Toolkit animations (.anm) are used; when an animation is required, a .gif may be substituted for a .anm, e.g. in the sprite graphics windows. The animated gif file must reside within the \Misc folder (or subfolders), in the \Bitmap folder like other images. An animated gif cannot be loaded into a Toolkit animation (only the first frame will be used). **not**
Around the Editor
The current frame is displayed in the centre of the editor. To load or change the frame image, click the frame and a dialog will appear allowing you to select images or tiles. Tiles must reside in the \Tiles folder and images in the \Bitmap folder (or subfolders); files that do not are copied by the Toolkit.
When starting, the animation has zero frames, as indicated by counter in the lower toolbar, displaying current and total frame numbers. After adding a frame, the frame count is increased to 1 of 1. To add a second frame, click the "Next Frame" button in the left-hand toolbar and repeat the process.
Most animations you will be making will require some portion of them to be transparent, and each frame in the animation has an individual transparent colour associated with it. To set the transparent colour for a frame, hit the "Select" button in the toolbar, and click the transparent colour in the image. As a useful touch, the transparent colour of the previous frame is set when a new frame is added.
The frame delay - that is, the speed of the animation - is set by the Frame Delay text box and the slider on the toolbar.
Often when creating characters and enemies using tiles the image takes up more than one tile, however you may discover that it is not currently possible to place more than one tile in an animation's frame at a time - so how is it possible to create character animations with more than one tile? The answer is to use Tile Bitmaps - which can be chosen as images for frames like the other image types. See the for more information. [Tile Bitmap Editor](page11.htm)
All these elements are encapsulated in the Animation Wizard, launched from the toolbar.
Toolbars
Previous Frame - Displays the previous frame in the animation.
Next Frame - Displays the next frame in the animation, and used to add new frames to the end of the animation.
Play Animation - Plays the animation through once.
Insert Frame - Inserts a new frame before the current frame.
Delete Frame - Deletes the current frame and moves subsequent frames up.
Lower Toolbar
- Size - Sets the dimensions of the animation. Width vs height can be manually specified, or the drop-down list used to set pre-defined dimensions or revert to the image's exact dimensions. When an image is loaded, the animation automatically resizes to the image's dimensions. (Different frames of the animation cannot have different sizes; frames are resized to match the animation's dimensions.)
- Frame Delay - Sets the length of time each frame of the animation is shown for, in seconds, using the text field or slider.
- Frame transparent colour - The transparent colour of the current frame (can be different for each frame). Hit the "Select" button and then click the required area on the frame to set the transparent colour.
- Frame File - Displays the filename of the current frame image; click '...' to browse for another.
- Sound - A sound clip can be chosen to play with each frame, chosen from the \Media folder.
Wizard
The animation wizard provides an easy way of compiling animations from images or tiles, negating the need to add frames image by image.
To create an image- or tile bitmap-based animation:
- Select the "Image files or existing bitmaps" radio button.
- Click "Select Files" to display a . *multi-select dialog*
- Hold down Control or Shift whilst clicking files to select multiple files.
- Click "Open". The selected files are added in alphabetical order.
- To add more files, select the slot in the list located the position you want to insert new files at, and repeat the process. *above*
To create a tile-based animation:
- Select the "Single or multiple tiles per frame" radio button. The last opened tileset is displayed (click the open button to select a new tileset).
- Use the scrollers to set the number of frames in the animation and scroll to the desired current frame.
- Click a tile in the tileset and then click on the 4x4 grid to the left to add the tile to the current frame. Start in the top-left corner.
- If a frame contains more than one tile, a tile bitmap file (.tbm) must be generated to store the array of tiles. Use the "Filename template for tile bitmaps" field to specify a template for the tile bitmaps that will be created (the wizard saves these automatically), including any subfolders within the \Bitmap folder. The default template is "tbms\npc1.tbm": this means that the first frame will be saved as "npc1_000.tbm" in the folder "\GameName\Bitmap\tbms", and the second will be "npc1_001.tbm", etc.
Upon exiting, the wizard resizes the animation to the dimensions of the first frame, and sets the transparent colour to the top-left pixel of the first frame.
