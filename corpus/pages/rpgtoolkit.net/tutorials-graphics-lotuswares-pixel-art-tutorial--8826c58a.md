---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/tutorials/graphics/lotuswares-pixel-art-tutorial/"
site: "rpgtoolkit.net"
title: "February 5th, 2010"
original_url: "http://rpgtoolkit.net/tutorials/graphics/lotuswares-pixel-art-tutorial/"
written: "2010-02-05"
date_confidence: "day"
updated: null
captured: ["20110318071530"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/tutorials/graphics/lotuswares-pixel-art-tutorial/index", captured: "20110318071530", sha256: "995c968602430a6a6c994ecb0af207fc3f193a54b968cca15513e149711be38e", wayback_url: "https://web.archive.org/web/20110318071530/http://rpgtoolkit.net/tutorials/graphics/lotuswares-pixel-art-tutorial/"}
---

# February 5th, 2010

[![Lotus](thumb/80/community/images/avatars/upload/16831567934d3083782e989.jpg)](member/lotus/)
Published
**February 5th, 2010**
Read times **1,085**
Written by Lotus
Lotusware's Pixel Art Tutorial
**Detailed look at the creation of tiles from Lotusware, covering techniques such as shadows, palettes, light source, ratios and joint tiles.**
1. Part 1: Basics
2. Part 2: Scenery
3. Part 3: Sceneery ii
**::[** **Lotusware's Pixel Art Tutorial for Game Creation ]::**
>
> >
> > >
> > > > *All of the art aspects for this series were and thus can be created in , so don't worry about fancy programs here. Those will be in some sort of **MS Paint*** *Board Illustration tutorial and will not be covered. Anyway, lets get started. Just to let you know, I'll be designing all these tiles in a , but you can use the same techniques to make or take the 16x16 tiles that you make and bump them up to 32x32, which I'll get into later. **resolution of 16x16** **32x32 tiles** **So lets begin!***
> > > >
> > >
> >
>
~ **~ Part 1: Basic Tiles**
In this section, we'll be dealing with the basic tiles and techniques used in the creation of a typical scene
**
Tiles
[ Grass - C liffs - Water ]
**
Tips/Techniques
[ Palettes - Light Source - Ratios - Tile Joints ]
**
Tip 1 Choosing a Palette and a light source
>
> There isn't really any wrong palette to pick (aside from a few horrendous colors), but keep in mind that you should keep in a consistent range from tile-to-tile and board-to-board, or else when you combine them, they may not mesh very well and some elements will be too distracting! So if you decide to go for a vibrant palette-- ! Same goes for darker palettes or muted palettes. I prefer to go with a muted palette of limited shades, that way all my tiles seem consistent all the way through the game, not to mention from tile-to-tile. **STICK WITH IT**
>
> >
> > >
> > > *
> > >
> > > *![Palette Used for EraFlux](vault/images/35_1.png)*
> > >
> >
>
> Another important thing to remember is ! I can't stress this enough. If you design your sprites with the light coming in from the left, do the same with your tiles. Although tiles themselves are flat, you can still give the illusion of shape with your lighting. Keeping a consistent light source on all of your objects help push that illusion into the game and makes your scene more and . **keep the lighting consistent** **believable** **dynamic**
> ![Lighting](vault/images/35_2.png)
>
**Tile 1 The Grass Tile**
> No joking around when I say this, but a grass tile can pretty much make or break your project and a good grass tile is generally hard to acheive.
>
>
> > ![Grass Tiles](vault/images/35_3.png)
> >
>
**Tile 2 The Cliff Tile**
> Depending on how you want to make your cliff (type of stone, wear, jaggedness, etc) there are a few ways to go about shaping them. But at this moment, you still need to design them. So here we go.
>
>
> > ![Cliffs](vault/images/35_4.png)
> >
>
**Tile 3 The Water Tile**
> This is a little harder to get to work. I came up with a method, albeit it creates a simple-structured water, so don't expect anything crazy awesome or realistic. But this is a two frame technique and its pretty effective.
>
> > ![Water Tiles](vault/images/35_5.png)
> >
>
**
Tip 2 Acheiving a Ratio
>
> So now, you have a tileset built out of 16x16 tiles and you have a choice. You can either of these tiles making them 32x32 or you could to make one larger 32x32 tile. To give a comparison between the difference, look at everything on the left column (double-sized) and the right column (groups of 4). Usually, the double-sized tiles are used if you want your game to have a retro feel, as most modern games would have them at a 1:1 ratio rather than the 2:1 ratio of the double-sized tiles. **double the size** **arrange four mini-tiles** **ONLY**
>
Now, using the tiles we just created, we're going to make a board...so here we go. I'll use both proportion methods to give you a better judgement as to which kind of ratio you want to use for your game. It all comes down to the ammount of detail you want, which may be important later on, because for large objects that decorate your board, you should know how much detail you want for them.
>
> >
> > > ![Comparison](vault/images/35_6.png)
> > >
> >
>
**Tip 3 Jointing Tiles**
> So, the above looks very bland and really terribly put together because the tiles aren't joined properly. The transitions are flat lines--you can't even tell where the raised platform cuts off. Even with an amazing tileset, if you fail at making your tiles work together, then sadly the board and thus the tiles fail as well. **ONLY**
>
> The easiest technique is to erase the edge of a tile up until some of the darker pixels, then add a darker rim around the edge. This goes for pretty much any kind of tile. For water though, it depends on the surface that it is trying to join into. Since we're dealing with a cliff-to-water tile, it will be the example I'll be showing you. But basically, it depends on the . **contour of the surface**
>
> > ![Joints](vault/images/35_7.png)
> >
>
Now that you have all your joints done, lets rebuild the same scene above with our extra tile joints and see how it works. ? I hope you still have it, because we can use that as the shadow from the cliff! **Remember that grass tile I told you to save**
>
> >
> > > ![Shadows](vault/images/35_8.png)
> > >
> >
>
>
> > ![Closing](vault/images/35_9.png)
> >
>
**::[** **Lotusware's Pixel Art Tutorial for Game Creation ]::**
>
> >
> > >
> > > > *All of the art aspects for this series were and thus can be created in , so don't worry about fancy programs here. Those will be in some sort of **MS Paint**** Board Illustration tutorial and will not be covered.
> > > > **So lets begin!**
> > > >
> > >
> >
>
~ **~ Part 1: Objects in a Scene**
In this section, we'll be dealing with the objects that decorate your board to give it a less tiled feel
** Tiles
[ Trees - Paths ]
**
Tips/Techniques
[ Shadows ]
So you've been walked through the basics and you should have a few techniques (and a tile set) under your belt at this point. Now your boards need some emotion. Aesthetically, static objects that are arranged on the board help to push your player into the world you create--and the practical side of it is to cover up tiles where "the grid" is visible. As far as objects go, I'll be designing using a , and for those of you who forgot what I mean by this, I'll be designing the tiles at a 32x32 resolution, . *small* **1:1 ratio** **rather than 16x16 and then stretching into 32x32 tiles**
**Tile 4 Trees**
** Step 1
** Step 2 Step 3 Step 4 Step 5
** Step 5 Step 6 Step 7 Step 8 Step 9 Step 10
![](vault/images/35_10.png)
.
Start by placing a rectangle in the dimensions that you want your tree to fill (this is mainly to ensure that you don't go beyond the tile co-ordinates by a few pixels). Now, you take the large brush if you're using MS Paint, if not...then make sure your brush is about or so. You then draw out the shape of the tree in a dark color b swatch in your palette, because you'll need that later. Then, with the same brush, add lighter areas here and there. At this point, you have to take into account the shape of your tree, because you'll need to leave little bits of the darker color underneath to give the tree some layers. A good number of layers to have is about 3, regardless of the size or shape of the tree (unless you're going with a huge tree). Also, leave some of the dark along the sides, more so at the bottom of the tree. Based on your determined direction of lighting, you then add more of the highlights on the side that the light is hitting, leaving both the dark green and mid green from the previous steps. . To hit a higher level of realism with your tree, you now have to dither. If done correctly, you can blend two colors very well. now, you want to take your dark green and dither into the mid green, keeping in little wave patterns. You then do the same with the mid green and dither into the light green. From here, your tree is basically finished. You just need to do some final detailing with the the green that is one swatch darker than the darkest green in your tree. So now you want to make an outline around the bottom half of the tree or so, and you can leave the top, but make sure that you have none of the highlights touching the edge. Using the leaves and stuff that you just created for your tree, you draw a trunk under it, and remember how a tree trunk is shaped. A good way to do it is draw one rounded pole down to the bottom of your rectangle, then add two curves and then draw a flat line from the bottom of the two poles to the center. Okay so, you then draw a shadow on your trunk. Keep your lit side pretty much untouched and leave a bit of lighter color in a triangle shape on the base of the unlit side. Then you dither around the dark, more so at the bottom of the shadow. And dither a little triangle on the base of the lit side. Add highlights onto your trunk. A little sliver along the lit side and a half-tear-shaped highlight on the lit side of the middle root. Then you dither the middle one into the darker side and a little bit at the top. Then add the texture of the trunk onto what you created. Just alternate lines of pixels. But make sure you do not connect the lines! You're pretty much done at this point **7 pixels wide** **ut not the darkest**
**You should see the three layers very clearly at this point**
**Dithering is basically drawing half-tone dots in a checkerboard pattern in-between two shades to give the illusion of an extra shade.**
*Just to note, I'm combining two steps into one from here.*
need to adjust where the leaves are placed on the trunk (if you made your shadow too low).
>
> Make sure that you place the trunk of the tree If you don't you may end up having the the trunk split in two and then you'll have gaps of grass that are , where you just want the one tile (base of the tree) to be solid. So if you have an entire tree that has a width of 64 pixels, place it in the center of a box that is 96 pixels. **THIS IS VERY IMPORTANT!** **in the middle of the 32*32 tile!** **solid** **This will make sure that the trunk is centrally located.**
>
> ![Different Trees](vault/images/35_11.png)
>
> Trees can be really any sort of size, shape or color. Just keep in mind, I've seen this so many times before, and it always looks terrible. They're more of a egg shape, so keep that in mind. Bushes can be designed by stopping before you get to doing the trunk. **TREES AREN'T SPHERE SHAPED!**
>
**Tip 3 Adding a Shadow to Trees**
> You've added shadows that were cast from a cliff onto grass already, but now you have to add a shadow onto the grass that works with a tree. And you have a few options...you can either go with darkening the grass or building a shadow that sets on top of the grass.
>
> ![](vault/images/35_12.png)
>
> On the left you have a tree and shadow using elements from the grass to create the shadow. This style works very well, but its downfall is that you have to create a new shadow with every shade of grass, plus, you can't put this shadow overtop of other scene changes, such as a path or water, so you'll have to design shadows for those as well.
>
> On the right you have a generic shadow. This shadow will work overtop of any surface decently. Make sure that you don't choose black because black will tend to overpower most surfaces... so lean towards a dark gray. the only problem with this is that it works only decently on all surfaces, rather than working well on at least one. If you're lazy or short on time, you may as well go with this style.
>
> ![](vault/images/35_13.png)
>
** Tile 5 Paths
**
Step 1
**![](vault/images/35_14.png)**
Okay, well you don't really have to start with a dark or a light shade of your selected path color, but if you start with a dark color, add a light dither and vice versa. Basically, just make a little horizontal rough patch and then copy and paste it over and over again on top of your base color to give it a grainy texture.
Step 2
![](vault/images/35_15.png)
From there you want to create a box and place a white circle that is 32x32 overtop of it. This will give you a clipping mask with which you can erase the corners of the base tile you just created. from there, you split your circle up into quarters and split your square into quarters as well. This will give you the building blocks for the next step.
Step 3
![](vault/images/35_16.png)
Okay, so you then arrange your 16x16 pieces to form two shapes like the one pictured to the left (a rounded square and a rounded cross). These are your basic tiles for making paths. We now move onto the detailing.
Step 4
![](vault/images/35_17.png)
Roughen up the edges of your corner tiles to give them a less cut-out look and more dirty. Then, your points on the cross will be the ends of paths. For the horizontal beam, you want to draw horizontal strokes across it a few pixels in and if you want, you can add a few "holes". Do the same with the vertical beam except with vertical stokes.
Step 5
![](vault/images/35_18.png)
Now, do give your path some depths against the grass it will most likely be placed on, add a dark rim onto it. THIS IS IMPORTANT! Make sure you ONLY darken pixels that have a white pixel directly on top of it. If there are no pixels to the immediate north of the pixel on the edge, LEAVE IT ALONE! This is to ensure your illusion of depth.
Now that you've done up paths and trees and paths, you have finished all of the common elements in a typical RPG board. So, with our newly made tileset, lets do up a basic scene.
>
> > ![](vault/images/35_19.png)
> >
> > * Looking nice!
> >
> Thanks for reading up to thus far, I hope that this tutorial is a big help to you all thus far. What I'm planning for in the next part will be objects in water, rocks, ladders and raised patches of grass. I hope that you'll stick around!
>
> --Lotusware
>
**::[** **Lotusware's Pixel Art Tutorial for Game Creation ]::**
>
> >
> > >
> > > > *All of the art aspects for this series were and thus can be created in , so don't worry about fancy programs here. Those will be in some sort of **MS Paint**** Board Illustration tutorial and will not be covered.
> > > > **So lets begin!**
> > > >
> > >
> >
>
~ **~ Part 3: Additional Objects in a Scene**
In this section, we'll be continuing with the objects that decorate your board to give it a less tiled feel
**Tiles**
**[ Tall Grass - Stairs ]**
**Tips/Techniques**
**Objects in Water**
**Tip 4 Putting Objects in Water**
> Occasionally, you'll want objects in the water that aren't just cliff faces. The most important thing to remember is that the object that you drop in will always be "3D", meaning that the object. **the water or other liquid will have to curve around**
>
> ![](vault/images/35_20.png)
>
> By drawing a some slices across the object, you can somewhat accurately define where the water will come up to. With spheres, its very easy, because they're a regular shape and thus have a predictable region. In most cases, you won't have a perfect object to work with, but the advantage to that is, it doesn't have to be rendered perfectly anyway.
>
> ![](vault/images/35_21.png)
> After clipping the submerged region off, you then place the object onto your water tiles.
>
> ![](vault/images/35_22.png)
> You don't have to stick the element in accordance to proper 32 x 32 co-ordinates mainly because there will be no interaction between elements in the water and the player themselves Start by adding whiter elements around the base of the object, contouring around the shape of the object. Then finally add rippling effects that spread out away from the object, keeping in mind the shape of the object and the direction of the flow of water. In this example, the water is flowing from North to South, so the ripples are on the back end of the object.
>
**Tile 6 Tall Grass Patches**
>
> Tall grass is another staple element in board design. Having the elevation reinforces the of your board and helps with , and allows for small objects to be concealed, just waiting for a would-be treasure hunter to come along and find. **depth** **suspension of belief**
>
> ![](vault/images/35_23.png)
> start off by taking the basic grass palette, tiles and corner edge tiles that you already created. You have to from the tile by replacing it with the middle shade and then come up with a dark green that is somewhat in-between the darkest shade of green and the edging on the corner tiles for your cliff grass. **eliminate the lightest shade of green**
> ![](vault/images/35_24.png)
> For the edges and corners, what you want to do is replace the dark border on the north, east and west sides with the slightly lighter green you created. Then, add a rough 4 pixel strip along the bottom edge to give the illusion of the side of the blades of grass. You can convert all your cliff edge and corners into this tall grass that not only stands out from the normal grass, but also looks very nice and consistent!
>
**Tile 7 Stone-cut Stairs**
> A good way to make your board designs really pop is by adding elevations and tiers of accessible areas to your boards. You can create stairs that will allow navigation and exploration throughout multiple layers of your board, adding levels of complexity and interactivity to your puzzles that would have previously been restricted to one single plane of the field.
>
> ![](vault/images/35_25.png)
> Begin by stacking a series of light and dark rectangles alternating from top to bottom, starting with a light and finishing with a dark. Ideally, you want to 2-3 per tile, but I find it usually works out if you work in a 32 x 64 area. Then add darker artifacts onto each side.
> ![](vault/images/35_26.png)
> Add some more detail here and there...make sure to take advantage of dithering to give it a grainy texture!
> ![](vault/images/35_27.png)
> Finish up by adding very dark elements and the light to simulate sharp edges, cracks and the like. Then add a darker arc onto the side to simulate the shadow cast by the dimensions of the stairs and the cliff that the stairs are cut into.
>
> As far as application goes, you have to remember, that , this means that not only would the span up, they'd span in. An appropriate way to go about doing this would be have the stairs extend the cliff face by one tile. Kind of like this... **the stairs are cut INTO the rock**
>
> ![](vault/images/35_28.png)
>
And that concludes of this tutorial, stay tuned for which will cover more elements that go into making your board as believable and beautiful as possible! **part 3** **part 4**
--Lotusware
{"twitter":[{"text":"Site is up and running, seems any initial problems are solved. See you on the forums :)","date":"Thursday at 2:55pm"},{"text":"New site is online but many of you will see a white screen, it's a problem with the PHPBB software. Trying to fix it, stay patient :)","date":"Thursday at 2:17pm"},{"text":"Site is online, little initial bug so apologies to those in the first 5 minutes who wondered why everything was broke :) Should be okay now.","date":"Thursday at 1:50pm"}]}
