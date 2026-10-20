---
kind: page
id: "rpgtoolkit.com/rpgtoolkit.com/dev_repo/docs/perspective.htm"
site: "rpgtoolkit.com"
title: "Maintaining Perspective In An RPG"
original_url: "http://rpgtoolkit.com/dev_repo/docs/perspective.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20010410012522"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.com/dev_repo/docs/perspective.htm", captured: "20010410012522", sha256: "611053bf04d35934f598c4ece6c4ddff8c47fc9a9130be28e3bf2c4467769b3c", wayback_url: "https://web.archive.org/web/20010410012522/http://rpgtoolkit.com/dev_repo/docs/perspective.htm"}
---

# Maintaining Perspective In An RPG

**
Maintaining Perspective In An RPG
When creating an RPG (or any game, for that matter), you must consider the issue of for your game. Perspective is the ‘viewpoint’ of the player. With the RPG Toolkit, the viewpoint is already set at an overhead view. There are many different types of overview perspective, however. *perspective*
Before even drawing the first tile for your game, you should have a pretty good idea of the type of overhead perspective that you will be using. It’s important to stay consistent throughout the game, and you must also make your perspective . *realistic*
**
The Final Fantasy Perspective
The overhead perspective that I like the best is the Final Fantasy style. My game demo for the Toolkit uses this style of overhead perspective.
![](Image1.png)
The FF style assumes that the player is not overhead. Instead, the player is slightly above the horizon looking down on the scene at an angle. *directly*
This means that if the player is looking at a house, he will only see the front part of the house, the front part of the roof, and only a portion of the back part of the roof.![](Image2.png)
Take a look at the screenshot of Final Fantasy 3 here. The player can see the entire front of the building. But notice the roof. We only see the front part of the roof, and a very small portion of the back part. This perspective is maintained with the barrels behind the building—we can see the entire front of the barrels, and can see the top, but can’t see anything behind.
How do you reproduce this perspective in a game? There are a few rules that you should follow…
First of all, your buildings should have relatively tall faces. That is, a house might have a face as tall as three or four tiles.
Second, the roof of a building must take equal or up less screen space than the building itself. That’s because the player’s viewpoint is only slightly above the roof, and so the player can still see the face of the building better than the roof. So, if a building’s face takes up three tiles, then the roof should only take up two.
Third, if the roof slopes in the back, you must see less of the backwards slope than the slope in the front (i.e.- if the roof takes up three tiles, the first two rows should be the front part of the roof, and only the last row should be the back part of the roof).
![](Image3.png)
It’s also a good idea to make the last row of the building type ‘under’. In this case, it would appear as if the player is walking behind the structure.
There are other things you can do to make this view more realistic. Adding a shadow to the right side of the building, shifted up one tile from the base of the structure usually looks good. You might even extend the shadow around the back of the building (although this sets your perspective slightly higher in the air that’s just above the rooftop).
![](Image4.png)
You can extend these concepts to the interior of a building, as well. Notice the picture of the castle interior: The rear walls are taller than the ‘roof’ (the black tile).
Also, the columns are much taller than the ceiling tile as well. You may also notice that the player should be able to walk the columns. To simulate this, I have made the first tile at the base of each column solid, then the rest of the column ‘under’. This allows the player to walk ‘behind’ the columns. *behind*
Note also the use of shadows to reinforce the concept of perspective in this room.
**
The Zelda Perspective
![](Image5.png)
Another extreme of the overhead perspective is an or overhead view. In this type of perspective, the player is much higher in the air than the building itself. Rather, the player is directly overhead looking straight down. *entirely* *mostly*
This means that the player sees more of the than the sides of the building. *roof*
With this perspective, the player can see four walls of a room simultaneously, by skewing them inward creating the illusion of depth.![](Image6.png)
This is what I would call ‘true perspective’, because this viewpoint tries to simulate what you might actually see if you lifted the roof off a house and looked inside. Unfortunately, this perspective doesn’t work very well on the exterior of buildings. That’s because the player would see all roof and barely any building face. I suspect that for this reason, the makers of the Legend of Zelda have used a Final Fantasy style perspective for outdoors shots.
This perspective is relatively easy to create. You must simply make a series of tiles creating the correct visualization of depth. For example, if you look at the Zelda screenshot, you will see that at the top of the wall, the bricks are quite large, but as they get closer and closer to the floor, they get smaller and smaller. This effect is achieved by creating tiles for each depth of the screen. This graphic appears to use 3 or 4 different depth levels.
Also, for each depth level at each corner, you must create tiles that realistically create corner style scenes. This is really easy to do with the Toolkit. You can take two tiles, lets say one with bricks running west-east, and one with bricks running north-south, and merge them. First you must take the west-east tile and cut off the bottom right corner (this is done in the Tools menu). Then, after you save that, you can open up the north-south tile and layer the cut east-west tile on top of it. This creates a northeast corner tile.
This method of perspective is a little more time consuming, and you will likely have to resort to the Final Fantasy style on outdoors buildings, but it looks really good.
No matter what style of perspective you choose, make sure that it remains throughout the game. This will ensure that your game flows as one piece of work, and that it seems more realistic. *consistent*
Of course, there are other styles of overhead perspective than the ones mentioned here. These two styles are what I would call three-dimensional styles of overhead perspective. They try to emulate a three dimensional surface as best as possible.
A much uglier style of perspective is a two dimensional style where there is no attempt made at a three dimensional surface—rather, buildings are just two dimensional images that are flat against the ground. Although this style may be the easiest to create, the quality of your game will likely suffer.
Christopher B. Matthews
