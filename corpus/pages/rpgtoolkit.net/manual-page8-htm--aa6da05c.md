---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/manual/page8.htm"
site: "rpgtoolkit.net"
title: "[ ]Around the Editor"
original_url: "http://rpgtoolkit.net/manual/page8.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20120618022345"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/manual/page8.htm", captured: "20120618022345", sha256: "51b76bb649f1fd7883271ea9081a8a0c709746eb2ac9fc17dc89f5e96e587780", wayback_url: "https://web.archive.org/web/20120618022345/http://rpgtoolkit.net/manual/page8.htm"}
---

# [ ]Around the Editor

Items (*.itm) are the most versatile objects in the Toolkit, and have a range of uses including NPCs (non-player characters), inventory and trading items, clothing and equipment articles, and anything the player might need to use in the game.
Item Basics
The first application is on the board: items can be represented on boards using tiles or images, and even given complete sets of movement graphics in order for them to be used as NPCs. In order for an item to be used on boards, the "Board-Driven" option must be selected in this editor (note items can still be placed on boards without this option selected, but they cannot be activated by the player), and with this comes options for dictating how the item behaves on the board by using RPGCode. Further RPGCode options are available when the item is set in the , such as how the player interacts with it. [Board Editor](page4.htm)
Their second major use are as inventory items - objects that the player can pick up, carry and use. Any items that the player acquires (e.g., by the GiveItem() command) automatically appear in the Items page of the - this is the player's inventory. Any type of item can be given to the player and the player can hold multiple copies of the same item at once, but only "Menu-Driven" items can be used from the (default) menu. When an item is used, either pre-defined effects can be applied (for instance a health boost with the classic potion) or a program can be run. Once an item is used, it is considered "used up" and removed from the inventory. [default menu](page15.htm#ms)
A subset of inventory items is equipable items - that is, items that the player can wear in order to alter his stats whilst he is wearing (or holding) them. By default, players are able to equip items to several parts of the body (see > Equipment), and further areas can be created. In order for items the player carries to be used as equipment, the items must be "Equipable" (but not necessarily "Menu-Driven"). A range of effects can be selected in the Equipable Edit screen, as well as RPGCode programs. Also, you may want any equipment the player carries or wears to be depicted through their graphics - there is an option here to specify an alternative fighting animation, but you may also want the player's animations to be altered in normal gameplay. The way to achieve this is to create a new character file with a new set of graphics and use the NewPlyr() command to change the character's graphics to those of the new file's - this doesn't change any other data associated with the player. [Character Editor](page7.htm)
Inventory items can also be used in if the "Battle-Driven" option is selected. Items used in battle have the same choices of effect as for items used from the menu; target stat alterations or RPGCode programs. Use of an item in battle takes one turn of the player, and after use it is removed from the inventory. [battle](page15.htm#bs)
You will most likely want many inventory items to be bought and sold by the player during the game, and each item can be given buying and selling prices for use with the internal shop program, CallShop(). Note that prices can only be set in this editor, and not through CallShop(), although you could potentially set up any system with a custom written shop.
Around the Editor
Item Name (Handle) - The name by which the item is referred to in RPGCode. Note that items on boards are referred to by their item slot number on the current board, as set in the , or when they are placed in RPGCode. [Board Editor](page4.htm)
Equipable - Enable this tick-box if the player is able to wear or hold this item. If equipable, the item will appear in a list in the default menu. The Equip submenu lists the available parts of the body that items can be equipped to, and lists of eligible items in the inventory will appear when a particular area is selected. The "Edit" button shows a window containing the following options:
- Equipable to - Select the areas of the body with which the item can be used. Choosing "Special Accessory", you can define a name for this in the corresponding textbox, to appear in the menu.
- Effects of Equipping Item - Lists several player attributes that can be altered only whilst the player is wearing the item (stats return to their previous value when item is removed). For instance, a heavy sword might increase a player's fight power (FP) by a number of points, but reduce his defence power (DP) slightly because of its weight.
- RPGCode - Programs can be run when the item is equipped or removed, and an animation can be specified to be used in battle if the item is equipped to a hand (for instance, for a special weapon).
Menu-Driven - Select if the item can be "Used" from the menu. Note all items the player acquires will appear in their inventory, but only those with this option can be used from it. Once an item is used it is removed from the inventory.
- Effects of Using - Lists a couple of the attributes of the target player that the item can boost with its use.
- RPGCode - A program can also be run when the item is used, for a more complex result.
Board-Driven - Select in order for the player to be able to interact with the item if placed on the board. Items can still be placed on the board without this option, but linked RPGCode programs will not run.
- Program to run while item is on board - This specifies a multitasking program that controls the actions of the item for the whole time it is on the board when it is not interacting with the player. For instance, assign "wander.prg" to this slot for the item to walk randomly around the board. The program is launched as a Board Thread (non-persistent).
- Program to run when item is picked up - When the player interacts with the item (walks into or hits the activation key beside), this program is run.
Battle-Driven - Enable this option if the item can be used in battle. Enabled items appear in the "Items" submenu of the default battle system, if the item is in the player's possession.
- Effects of Using - Lists a couple of the attributes of the target player that the item can boost with its use.
- RPGCode - A program can also be run when the item is used, for a more complex result.
Purchase Price - The price paid by the player when the item is bought from the shop (CallShop()).
Selling Price - The money the player receives for selling the item in the shop.
Description - A short description that appears when the "Info" option is selected in the default menu, along with the possible uses and effects of the item.
Key Item - Enable this option to prevent players from dropping this item (i.e., removing from the inventory).
Used By All Characters - All characters can use and equip this item.
Used By Defined Characters - Only certain characters can use or equip this item. Use the drop-down list that appears to choose up to 50 characters by writing their handles in the text box.
Graphics
The graphics associated with items are almost identical to those associated with characters. Since items can be used as NPCs, they may be assigned walking graphics and custom stances in the same manner. They may also be assigned the same types of vector bases (collision and activation), so that they may interact with players. The item graphics window works in the same way as the ; see this for further details. [character graphics window](page7.htm#graphics)
