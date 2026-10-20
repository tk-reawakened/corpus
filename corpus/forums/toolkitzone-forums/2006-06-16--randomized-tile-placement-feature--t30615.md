---
kind: forum-thread
id: "toolkitzone-forums/30615"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Toolkit Discussion"
skin: "phpbb2"
thread_id: "30615"
title: "Randomized tile placement feature."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=30615"
written: "2006-06-16T18:12:00"
last_post: "2006-06-19T12:49:00"
date_confidence: "exact"
captured: ["20060623103512"]
author: "Gooseboy"
repliers: ["spoopryme", "peace", "Icbim"]
authors: ["Gooseboy", "spoopryme", "peace", "Icbim"]
posts_present: 6
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_328868_amp_3Bsid_e15fc88dd625d3ead51650d6d7c0cf8c", captured: "20060623103512", sha256: "ceb360426cbffb234fbe427466ed7a4b7e1cfd99c2b266a236c9c26641ca5402", wayback_url: "https://web.archive.org/web/20060623103512/http://toolkitzone.com/forums/viewtopic.php?p=328868&amp%3Bsid=e15fc88dd625d3ead51650d6d7c0cf8c"}
links: []
---

# Randomized tile placement feature.

### Gooseboy · 2006-06-16 18:12 · #B328216

I had this idea some days ago. Is another board editor feature that allows the user to make some good looking terrain with randomized tiles.
What I mean is that it will be cool to have a little box in some corner of the board editor, with some white empty boxes, where the user places some tiles there. Once he fills that box, he can check a box that says "Randomized Tile Placement" and when the user starts to place tiles in the board, the tiles that are placed are the ones he previously filled the box with. So the editor will randomly choose a tile he placed in the box and place it in the board, and repeat this prosses each time the user places a tile in the board.
Lets say I want to make a field with grass and flowers. So I go to the white box and place a grass tile there. Then I open a tileset that contains some flowers, and place those tiles in the box as well. Then I check the "Random tile placement" box. When I go draw the tiles in the board, the editor will randomly choose a tile in the white box and draw it in the board, so each time I place a tile in the board, the editor will choose a tile randomly again, and place the chosen tile in the board. The result will be a field with flowers scattered arround randomly.
This can lead to a very cool natural bord design and will save a lot of work. I dont know is you people understand what im saying, but we can discuss this cool feature.

### spoopryme · 2006-06-16 18:29 · #B328223

thats a pretty cool idea! would certainly take the tedoius-ness out of trying to make ones field of grass look more random.

### peace · 2006-06-17 08:46 · #B328390

**Gooseboy wrote:**

> I had this idea some days ago. Is another board editor feature that allows the user to make some good looking terrain with randomized tiles.
> What I mean is that it will be cool to have a little box in some corner of the board editor, with some white empty boxes, where the user places some tiles there. Once he fills that box, he can check a box that says "Randomized Tile Placement" and when the user starts to place tiles in the board, the tiles that are placed are the ones he previously filled the box with. So the editor will randomly choose a tile he placed in the box and place it in the board, and repeat this prosses each time the user places a tile in the board.
> Lets say I want to make a field with grass and flowers. So I go to the white box and place a grass tile there. Then I open a tileset that contains some flowers, and place those tiles in the box as well. Then I check the "Random tile placement" box. When I go draw the tiles in the board, the editor will randomly choose a tile in the white box and draw it in the board, so each time I place a tile in the board, the editor will choose a tile randomly again, and place the chosen tile in the board. The result will be a field with flowers scattered arround randomly.
> This can lead to a very cool natural bord design and will save a lot of work. I dont know is you people understand what im saying, but we can discuss this cool feature.
>

This can actually be done with rpg code.
Though you would probably want your graphics to not be part of a tileset.
Instead you want them to be individual tiles in the bitmap folder.
Just name all the related tiles the same except for the number aftwards.
Like grass1.bmp, grass2.bmp, ect...
Next, randomize the number to the number of the highest file.
Afterwards, you combinethe word in this case grass with the literal version of the number into a literal variable.
When then load the tiles to the place on the screen where you want them.

### Gooseboy · 2006-06-18 23:39 · #B328747

yeah i get that, but for lower skilled game makers, it shoud be a really handy tool. and you dont have to clutter up the bitmap folder with a lot of .bmp files.

### peace · 2006-06-19 06:54 · #B328839

**Gooseboy wrote:**

> yeah i get that, but for lower skilled game makers, it shoud be a really handy tool. and you dont have to clutter up the bitmap folder with a lot of .bmp files.
>

That is what the folder is for. Also, you can use gifs and jpgs.
Or, you can create them inside rpg code.
There may also be a plugin to do what you want.
Checkout the plugin page.
There is also shading, change color and scrolling to give them a more random look.
Take the current grass tile offset by scrolling some and you get new tile which looks some what different.

### Icbim · 2006-06-19 12:49 · #B328868

It's be a good idea...but a bitch to clean up if it doesn't look good.
