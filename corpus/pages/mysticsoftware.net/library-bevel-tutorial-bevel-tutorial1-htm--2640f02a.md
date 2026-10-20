---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/library/bevel_tutorial/bevel_tutorial1.htm"
site: "mysticsoftware.net"
title: "Taking the \"edge\" off of wall tiles By Wasteland WHAT THE BEVEL?"
original_url: "http://mysticsoftware.net/library/bevel_tutorial/bevel_tutorial1.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20021225143756"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/library/bevel_tutorial/bevel_tutorial1.htm", captured: "20021225143756", sha256: "61197f573b8a52d5679e247c3c2311d1a6cb7d409d9cda07f7bb446af95702c3", wayback_url: "https://web.archive.org/web/20021225143756/http://mysticsoftware.net/library/bevel_tutorial/bevel_tutorial1.htm"}
---

# Taking the "edge" off of wall tiles By Wasteland WHAT THE BEVEL?

![](../../images/top-nw.gif)
![](../../images/top-n.gif)
![](../../images/top-ne.gif)
![](../../images/top-w.gif)
![](../../images/top-e.gif)
![](../../images/top-sw.gif)
![](../../images/top-s.gif)
![](../../images/top-se.gif)
![](../../images/top-nw.gif)
![](../../images/top-n.gif)
![](../../images/top-ne.gif)
![](../../images/top-w.gif)
![](../../images/Bullet7.gif) [In Development](../../indev.htm)
![](../../images/Bullet7.gif) [Library](../../library.htm)
![](../../images/Bullet7.gif) [Media](../../media.htm)
![](../../images/Bullet7.gif)[ Forum
![](../../images/Bullet7.gif) [Plug-ins](http://tkzone.net/toolkitzone/dls/plg/plugins.htm)
![](../../images/Bullet7.gif) [Tileset Archive](../../tilesets.htm)
![](../../images/Bullet7.gif) [Staff List](../../staff.htm)
![](../../images/Bullet7.gif) - - - Fighters Destiny - Demensions - Amusement Park -
![](../../images/top-e.gif)
![](../../images/top-sw.gif)
![](../../images/top-s.gif)
![](../../images/top-se.gif)
![](../../images/top-nw.gif)
![](../../images/top-n.gif)
![](../../images/top-ne.gif)
![](../../images/top-w.gif)
Taking the "edge" off of wall tiles By Wasteland **WHAT THE BEVEL?**
Hi. I'm Geoff Bohrer, president, chief designer, and head cook and bottlewasher at Wasteland Games, better known around the gaming world as Wasteland. I love games…I love playing them, but I especially love designing them. Unfortunately for me, games require visual appeal- and I'm no artist. The other two members of my staff are, but really lack the are busy enough with other artistic chores that they don't really have the time to sit and make tiles. So I'm always on the lookout for ways to cover up my lack of artistic talent. In the case of sprites, I use a 3d renderer….it can draw what I tell it to. In the case of terrain, I look for shortcuts and apply my general knowledge of the world.
The Wall Dilemma
One of the biggest problems with tilebased game makers is that your smallest discrete unit to draw with is the tile. You can change what's ON the tile, using a tile editor (for the purposes of this tutorial, we'll be using the RPG Toolkit's integral tilemaker…but the theory will transfer to any tile editor, image editor, or icon editor) but once you've made your tiles, you're more or less stuck with them. This can lead to a "blocky" appearance, especially when you're creating buildings with interiors and exteriors: Looking at this picture, you can see that the walls and floor are fairly detailed, but that the detailed appearance is largely spoiled by the big, blocky wall tiles. But what can we do about it? We have to define the walls, and they're going to be solid tiles anyway…
![](../../images/bevel_tutorial1.jpg)
Light and Shading
Look at ancient Egyptian paintings. They're pretty good, right? You can pretty much tell what they're supposed to be. But they're missing something; they look flat. Now look at a Renaissance portrait. Looks almost three-dimensional, doesn't it? So what's the difference? The difference is that the Renaissance painter studied light and the way it changed the colors he was looking at. This is called shading, and it's the way you create an illusion of depth in a two-dimensional picture. There's many ways to do this, and without being an artist, most of the time you won't be able to reproduce it on a tile. But you can use one specific technique to quite easily add the illusion of depth to your boards.
Beveling
To a carpenter or a metalworker, a bevel cut is a cut at an angle to the surface he's working with. To a pixel artist, it's using shading to create the illusion of that angled cut. Look at these two buttons:
![](../../images/bevel_tutorial2.jpg)
![](../../images/bevel_tutorial3.jpg)
Which one appeals more to the eye? The one on the right, right? It has beveled edges. Not that Microsoft makes use of beveling (or rounding) in all of their buttons. This produces an illusion of depth: it make the image APPEAR to be three-dimensional, even though it's two dimensional.
Look at the house above, with the edges of the walls beveled:
![](../../images/bevel_tutorial4.jpg)
It makes the whole house seem to stand up from the ground, right? Notice how it also separates the types of tiles, making it clear that the tops of the walls are a whole different kind of tile. Finally, it leads the eye down onto the walls that show, enhancing the illusion that the other walls are also there. The depth illusion is even more pronounced with shadowing: Now, instead of a cartoon of a house, you've got almost a model suitable for miniatures play.
![](../../images/bevel_tutorial5.jpg)
How'd you DO that?
The best part of using beveling as a pixel art technique is that it's easy. The first part of the job is to determine where your light is coming from. Unless different parts of your game happen at different times of day, you should ALWAYS use the same light direction in all the art you do for the game. If you don't, the player's eye will know something's wrong. They may not be able to tell you what that is, but they'll know. I usually place my light source in the southwest. The means that all my shadows will point northeast, and that all my south and west edges will be lit, while all my north and east edges will be dark.
Now, choose the colors you're working with. Note that I say colors; you'll be using three shades of the same hue (hue is the color mix that makes up a color; shade is the amount of white mixed in). I used grey in the above example, so I selected three close shades of grey: (circled in red)
![](../../images/bevel_tutorial6.jpg)
I nearly always use the DOS 256-color palette; it makes matching colors MUCH easier.
Now, flood fill your tile with the MIDDLE color. Then use the filled rectangle tool to color the WESTMOST (leftmost) three columns of pixels the lighter shade, and the EASTMOST (rightmost) three columns the darker shade:
![](../../images/bevel_tutorial8.jpg)
(If you're using TK v2.17 or lower, of if your tile/image/icon editor doesn't have a fill rectangle tool, you'll have to do this pixel by pixel.) Save to your tileset, rotate the image so that the light color is on the south (bottom) side, and save it again (as a separate tile). Your first two tiles are done!
And that's the downside of this technique. When you just had a simple grey tile for the tops of your walls, one was all you needed, right? To have beveled walls, you actually need:
1 vertical 1 horizontal 4 2-way corners 4 3-way corners 1 4-way crosspiece 2 vertical ends 2 horizontal ends
And most of these have to be made individually- remember, the direction of the light is very important, so you can't just flip and rotate for most of these. If you have to do it pixel by pixel, it can be time consuming; but with a filled rectangle tool, is' a matter of minutes to make each tile. (All the tiles for this tutorial were made from scratch. The process took a total of 25 minutes.)
Making corners will be the most time consuming part, since it's best done pixel by pixel. Simply make a diagonal line from the corner of the tile, in three pixels:
![](../../images/bevel_tutorial7.jpg)
Just make sure you remember which faces are lit and which are dark: it's easy to get confused.
Doing the bevel technique is easiest with greys, because you usually have a large selection of greys from which to choose. But it works with any color, as long as you've got three shades to choose from:
![](../../images/bevel_tutorial9.jpg)
Here we've picked three shades of brown, and it seems to work out fairly well:
![](../../images/bevel_tutorial10.jpg)
Now, you're ready to use your tiles. You can try and build the house above in your board editor, and see how it looks. The effect is even more pronounced in multi-room boards:
![](../../images/bevel_tutorial11.jpg)
Notice how the grey tends to dominate the other colors. The eye also tends to follow the grey, because it's smooth…it looks more like the path of a maze than the walls. Now look at it with beveled walls:
![](../../images/bevel_tutorial12.jpg)
The grey is still the dominant color, but it's "lifted above" the floor. The eye is led smoothly into the walls, and it's clearer that the invisible walls are there. Also, because of the "raised" effect, it's obvious that these are barriers, not pathways.
Enjoy!
It's a lot of fun making games…and it's even more fun when others enjoy playing them. Good graphics can't make a bad game good…but they can enhance an already good game. With this technique, and a few others, even a non-artist can create games that look as good as they play!
![](../../images/top-e.gif)
![](../../images/top-sw.gif)
![](../../images/top-s.gif)
![](../../images/top-se.gif)
![](../../images/top-nw.gif)
![](../../images/top-n.gif)
![](../../images/top-ne.gif)
![](../../images/top-w.gif)
![](../../images/top-e.gif)
![](../../images/top-sw.gif)
![](../../images/top-s.gif)
![](../../images/top-se.gif)
