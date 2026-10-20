---
kind: file
id: "toolkitzone.com/402"
site: "toolkitzone.com"
title: "Isometric Tiles Basic Tutorial For TK3."
original_url: "http://www.toolkitzone.com/fileman.php?id=10&file=402"
written: null
date_confidence: "unknown"
updated: null
captured: ["20041107090153", "20041107090314", "20060612062645"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_402", captured: "20041107090153", sha256: "a43adfbb03618357d9c7bf57c1b2ba3adc5825dea9bec6fcd33380f1f9ed2798", wayback_url: "https://web.archive.org/web/20041107090153/http://www.toolkitzone.com/fileman.php?id=5&file=402"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_402", captured: "20041107090314", sha256: "1872d32bfdf9688f3d2fe8d25fdf5e7ca4f1379fb5cf74009b60199b02e02207", wayback_url: "https://web.archive.org/web/20041107090314/http://www.toolkitzone.com/fileman.php?id=10&file=402"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_402", captured: "20060612062645", sha256: "9d21c632456f24deef5fc6ab2caea15dee19252e07fa27a74af4dc868441a6b3", wayback_url: "https://web.archive.org/web/20060612062645/http://www.toolkitzone.com/fileman.php?id=3&file=402"}
---

# Isometric Tiles Basic Tutorial For TK3.

By: Randy Phillips (Razor)
Welcome to my first tutorial (It probably wont be all that special.)
I have sent a few files with this tutorial to help. The basic stuff like the sides template.
Ok, now the tutorial starts. To start off, open a new tile in TK3. (File>new>tile) After that the tile editor is obviously open. On the left is the tool commands, and on the bottom is colors and preview like stuff. Since we are making a tutorial for isometric tiles, I wont even talk about the regular 2d tiles. In the alpha version, the FILL tool (circled below as well as the isometric preview screen) will lock up the tk. (Found out for myself)
![](fileman/images/214.png)
Now that you can see what I am talking about, we will make a sides template. This will tell you what side/corner is where in the actual tile editor. First choose a color. ANY color you want. Then make a triangle in the upper left. Then choose another color and the upper right, and so on so forth for the other corners. It should look like this.
![](fileman/images/215.png)
Now, choose black by clicking Color>Dos Palette then choose the first color. Now select the line tool on the left. Then Drag the line from the Upper Left arrow to the Upper Right arrow, From the Upper right to lower right, lower right to lower left, and lower left to upper left. These are obviously the outside lines, but to tell you now, the lower right to lower left is the left bottom part in isometric form. This leaves the upper left to right being the top right, I think you can get what the others are. After you are done, it should look something like this.
![](fileman/images/216.png)
When that is completed, Make Two DIAGANLE lines, One from the top left to the bottom right, and one from the top right to the bottom left. The top left to bottom right is the top to bottom in this case. Top right to bottom left is a straight line across. It should look like this. (*** Note the top right to bottom lefts middle most line is deleted to get the true isometric tiles. Make the line bigger by putting a line on each side of it to see the line in the preview. ***)
![](fileman/images/217.png)
There you have it. 4 steps to make an Isometric template. Ok, Now I am going to make a very short, and not so long wall for you all. It will use 2 colors. Black and Grayish yellow. It is really simple to get the point of the wall, or the outside of a building. Take the grayish yellow and fill up the sides of the top right and bottom left, excluding the bottom and left side lines from the template, and wabam!!! You have a point of wall or the outside of the building. Looks like this when done. DO NOT USE THE FILL TOOL!! (At least if you are using TK3 alpha)
![](fileman/images/218.png)
Now, I know your thinking, THAT DOESNT LOOK LIKE A BUILDING CORNER. And youre right, it has no top to the building. It also needs the sidewalls. To get a full 3d looking Isometric tile, It truly takes 4 tiles. (Actually 3, but that is excluding half of the side wall tiles.) Now to finish the side walls remove the middle line and have it the same color as the wall. Then remove one of the side lines. (I will show it with the bottom being removed.) With the remaining side, place a black line on the other side. (This is for 1 tile tall structures. 2 or more dont put the line on the other side.) It will look like this.
![](fileman/images/219.png)
Then just rotate it (tools>rotate) once to get the bottom and top lines without the sides. This gives you the other wall. Now to make a simple roof, just fill a tile with black. (Use filled square option till fill is fixed {box with blue inside of it on the left.) Now you have a decent enough amount of tiles to take it to the board builder. Click File>New>Board. On the left now you will see the map commands. Look for a Diamond shape inside of a button and click it to turn it to Isometric form. (Click ok after clicking the button in alpha version) Then make your board. I will include some files with the Iso tut that I made. Some grass a tree, so on and so forth. I am also going to add bricks and stuff like that to the walls, so it is an outside setting.
Ok, Now I am going to tell you how to batch import Isometric tiles. This requires a graphics program that will let you rotate at custom degree integers. Photoshop is what I use, so I will tell you how in photoshop standards.
You have your picture that is larger than 32x32 pixels, so lets say it is 64x64. To get it to stand straight up like a tree (I have included one with the files.) make sure the secondary color is the exact same color as the background (more than likely black or white) then click Image>Rotate Canvas>Arbitrary then set the number to 45. (That is negative forty five, or positive 315.) Now back in the tile editor at the top, click import>grab tiles. When in there, click open then browse to your picture. (Many files types are supported.) When you have opened the picture, it will appear below inside the white box. Click get transparent click ok, then click on the color that will be transparent. Now all that is left is to click batch import either 32x32, or 16x16, name the file, and wait till it is done.
In the alpha version, you can not use gph (batch import) file types for regular tiles, so you must use tk2 to save them as tst and copy them to your tk3 folders.
Look below for a pic of a board I made really quickly. I added the brick, grass, dirt, and window tiles. (the buildings are made with the same techniques I just used, except I added graphics to the basic colors. Remember that diagonal is actually straight.
![](fileman/images/220.png)
