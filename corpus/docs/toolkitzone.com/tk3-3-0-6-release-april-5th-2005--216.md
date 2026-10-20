---
kind: doc
id: "toolkitzone.com/216"
site: "toolkitzone.com"
title: "TK3 3.0.6 Release: April 5th, 2005"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=216"
written: "2005-04-05T09:13:00"
date_confidence: "exact"
updated: null
captured: ["20060515200451", "20060521140638"]
author: "Xavier"
repliers: []
authors: ["Xavier"]
comments_present: 0
f_author: "Xavier"
f_date: "April 5, 2005, 9:13 am"
f_description: "Official final list of fixes for Toolkit 3.0.6."
f_section: "Toolkit 3.x"
f_title: "Official 3.0.6 Changes"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_216", captured: "20060515200451", sha256: "fa80a2109691639f646f6ed9b74c9dfb6cd25f100477135fb525cf45bf0c5248", wayback_url: "https://web.archive.org/web/20060515200451/http://www.toolkitzone.com/library.php?mode=read&doc=216"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_view_cadd_doc_216", captured: "20060521140638", sha256: "af29cd22cc190b76d8c47bf078d9cf3ee8a67e072c696f3b56e5af62fc3c14bc", wayback_url: "https://web.archive.org/web/20060521140638/http://www.toolkitzone.com:80/library.php?mode=read&view=cadd&doc=216&PHPSESSID=49eb2e17f9e455e1205f36438de58609"}
---

# TK3 3.0.6 Release: April 5th, 2005

This is the complete bug fix list for the release of RPG Toolkit version 3.0.6. All items listed here are guarenteed to be present in the release..
Contributors for this release, in alphabetical order: Colin, Delano and Occasionally_Correct. Development testers for this release, in alphabetical order; Ashe, Caliber Mengsk, Codester, Khin, oblivious_casualty, RDemusX and Serge.
Toolkit Game Engine (trans3)
Bug Fixes + Various bugs with produced EXEs + Stretching of images is poor. + Diagonal solidity in tile movement + Minor default battle system bugs + callshop() broken + Internal copy should physically copy objects, not handles. + board backgrounds smaller than screen are not centred. + Other party characters cause jumpy player movement sometimes. + Parsing problems between array brackets. + North-South and East-West tiletypes ineffective.
+ Calling an outside method from within a class that accesses variables named as class members indirectly causes crashing. + Linking to boards with solid edges sometimes render the player immobile when moving to new board. + Player and item animation sounds don't work. + DrawCanvasTransparent() partially broken. + Kill() with multiple variables doesn't kill first one. + Negative numbers don't work properly in all situations. + Assignment operators other than "=" don't work in the middle of equations. + Members "double" in inheritance sometimes (?). + Slow rpgcode graphic commands. + Threads almost completely broken. + Get() buggy. + RestoreScreenArray(), SaveScreen() broken + TileType() broken + PushItem(), ItemStep() always moves the zeroth item + elseif and else broken + Day/Night system partially dysfunctional -- removed + Disable Progress Saving board option ineffective -- Default menu updated + Players & items freeze when colliding diagonally with other items (tile movement only) + Board player position should default > 1,1,1 + mp3s aren't handled correctly + Music playback jumpy (?) + fps-in-title-bar problems + idle animation delays + Critical hits + Ambience problem with character sprites + PlayerSpeed, PlayerStance cannot receive the player handle, or "target"/"source". ItemSpeed, ItemStance can now receive "target"/"source" + Subscript operator used on objects + "garbage collection" problem + PlayAvi, PlayAviSmall sizing and ending issues + Transparency problems with animations + Mwin() should have a variable translucency setting -- setMwinTranslucency(percent!) adde
Known Issues + callPlayerSwap() needs to be written (suggestions?) + Plugins sometimes don't work + The windows 9x bug + Alt-Tabbing out of a fullscreen game, the game cannot be reactivated
Toolkit Editor (toolkit3)
Bug Fixes + Editors should be able to window + Isometric boards size incorrectly in editor at certain resolutions + Editing tools for isometric tiles enabled: rotate / flip, scroll (diagonally), layer tile. + Flood fill in board/tile editor broken for some Win9x users + Board Editor "Delete layer" option ineffective + Tile bitmap editor + the two small buttons in the board editor under the currently selected tile don't work + switching between board editors while an animated tile is open gives problems + When choosing tiles using "L", the tile is sometimes placed under the point clicked in the tileset window + Animated tile editor does not save correctly + Comments "flow" onto the next line in the RPGCode editor + RPGCode editor colouring defects after switching to and from another document + Environment doesn't change completely after creating a new project + Editors should show an error when trying to save Read-Only files + Tileset browser on right sometimes displays sets starting at the wrong row + Placing a partly transparent tile on a board doesn't erase the replaced tile from the screen + "select colour" dialog in tile editor doesn't work with multiple tiles open + Editors sometimes window themselves + Creating an animation with tiles, deleting, altering the tiles, remaking, the tiles aren't updated + Animation editor adds extra frames + Board editor cannot flood large boards (> 100 x 100) + Problems pasting into/copying out of rpgcode editor + Cannot open isometric tiles using "L" + Layering tiles sometimes converts tile to isometric + Switching between tile editors, tile data sometimes converts to isometric + Tile grabber sometimes misses isometric tiles + Editor will not load after "Tip of the Day" (several reports) + Isometric scrolling of tiles + White trails on isometric tile blurs + Background image unavailable + No way to view rgb colours in tile and animation editors + Lacking a "real" blur in the tile editor
Miscellaneous Items + Updated quick reference + Crashes for some people during install (may still cause problems) + Help files rewritten
The Envy
April 6, 2005, 5:38 pm
I hated that when I was making some early tiled boards for basic layouts...Good thing it's fixed! *+ When choosing tiles using "L", the tile is sometimes placed under the point clicked in the tileset window*
sephy
April 11, 2005, 6:24 pm
so we only can move by tiles?
Official final list of fixes for Toolkit 3.0.6.
Sep 4, '05
Jan 26, '05
Dec 23, '04
Dec 12, '04
Apr 25, '06
Jan 5, '06
Dec 15, '05
Sep 15, '05
Aug 24, '05
