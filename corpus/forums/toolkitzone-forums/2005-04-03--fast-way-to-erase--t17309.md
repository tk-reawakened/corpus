---
kind: forum-thread
id: "toolkitzone-forums/17309"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "sprites"
skin: "phpbb2"
thread_id: "17309"
title: "Fast way to erase?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=17309"
written: "2005-04-03T20:04:00"
last_post: "2005-04-04T16:20:00"
date_confidence: "exact"
captured: ["20050406051051", "20051031001055", "20051107040144", "20051112081510", "20051112091546", "20051112093941"]
author: "Hero of Winds"
repliers: ["The Envy", "OBCT"]
authors: ["Hero of Winds", "The Envy", "OBCT"]
posts_present: 7
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_189887_amp_3Bsid_673da8786cca5c27d64895df9a6b2ac2", captured: "20051031001055", sha256: "384840894ca1158d9162bd033e9ed9b477bae713fbf55fe2e2ead7f72033b2bc", wayback_url: "https://web.archive.org/web/20051031001055/http://www.toolkitzone.com/forums/viewtopic.php?p=189887&amp%3Bsid=673da8786cca5c27d64895df9a6b2ac2"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_189891_amp_3Bsid_673da8786cca5c27d64895df9a6b2ac2", captured: "20051107040144", sha256: "595bc538052690c270c3c613958c77d99987e5368d647e21553efde48b42b135", wayback_url: "https://web.archive.org/web/20051107040144/http://www.toolkitzone.com/forums/viewtopic.php?p=189891&amp%3Bsid=673da8786cca5c27d64895df9a6b2ac2"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_189906_amp_3Bsid_673da8786cca5c27d64895df9a6b2ac2", captured: "20051112081510", sha256: "0442aeb0d9d9802c8c9b39680e7098dfe6e45d9883361542e18a5dfe4761b1ec", wayback_url: "https://web.archive.org/web/20051112081510/http://www.toolkitzone.com/forums/viewtopic.php?p=189906&amp%3Bsid=673da8786cca5c27d64895df9a6b2ac2"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_189911_amp_3Bsid_673da8786cca5c27d64895df9a6b2ac2", captured: "20051112093941", sha256: "0c4b9ca09ad7c6c013a290d85e8fd49c0736788f1b1e56cf56673adafcd19fbc", wayback_url: "https://web.archive.org/web/20051112093941/http://www.toolkitzone.com/forums/viewtopic.php?p=189911&amp%3Bsid=673da8786cca5c27d64895df9a6b2ac2"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_190214", captured: "20051112091546", sha256: "588946facf5bd55ffc66325297bad6066edc17d612a81e2bcc22eca14a7dd799", wayback_url: "https://web.archive.org/web/20051112091546/http://www.toolkitzone.com/forums/viewtopic.php?p=190214"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_190214_amp_", captured: "20050406051051", sha256: "c28493694ffa52a14bd00a21487a5415220e8dd33463522de75bd423ae0669ec", wayback_url: "https://web.archive.org/web/20050406051051/http://www.toolkitzone.com/forums/viewtopic.php?p=190214&amp="}
links: []
---

# Fast way to erase?

### Hero of Winds · 2005-04-03 20:04 · #B189876

Is it possible to erase areas of white quickly, because I'm importing images from Paint into the Tile Editor and want to get rid of everything but the sprite itself, so that the background around it is transparent. Help, thanks!

### The Envy · 2005-04-03 20:10 · #B189887

Change the background color in paint to a color not used in the sprite, such as standard blue, and then set the color as a transparent color in TK. Then import. See if that works.

### Hero of Winds · 2005-04-03 20:15 · #B189891

Thanks, I'll try that. Also, is there a way to convert multiple files into .gph. I'm looking for timesavers here, that's all.
Note: Can't find anything like that for some reason...

### The Envy · 2005-04-03 20:35 · #B189906

By the way, there's a game here called Winds. Your username makes you sound like your obsessed with it, and not Zelda. Just so you know...

### Hero of Winds · 2005-04-03 20:43 · #B189911

I can't find anything that sets a color as transparent. Can you point me in the right direction?

### OBCT · 2005-04-03 23:12 · #B189986

Grab tiles. it's much easier than importing them. grabbing tiles takes a group of tiles, and sticks them into a tileset all ready for you to work with. here's how to do it:
I'm assuming that you're using TK3. if not, get it.
1) On the menu bar, click File -> New... -> Tile. a window will come up with a 32*32 grid of transparent squares. (transparency appears as half gray and half white, in a checkered pattern)
2) Notice that the menu bar changed. Now go to Image -> Grab tiles. You should get a welcome message. you can read it, or just click OK.
3) In the tile grabber, you should see buttons at the bottom. Click on the 'Open graphic' button (top row, first button) to select your image.
4)After the image is loaded, find the 'Get transparent color' button (top row, third button).
5) Click OK when the message pops up, then select your transparent color.
6) The transparent color will appear below the 'Get transparent color' button.
7) Click 'Batch Grab 32x32', then select the tileset that you want the tiles to go in.
there you go. you will now have a tileset composed of your picture, with some pixels transparent.
on a side note, the transparent color is located in the tile editor, directly to the right of the color selection box, at the bottom. you can use the 'Fill rectangle tool' with the transparent color to erase a large area quickly.

### Hero of Winds · 2005-04-04 16:20 · #B190214

Thanks, but I found out that I can transparent a certain color out during animations. I'll probably use hot pink for most animations.
