---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/manual/page15.htm"
site: "rpgtoolkit.net"
title: "Systems"
original_url: "http://rpgtoolkit.net/manual/page15.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20120618021055"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/manual/page15.htm", captured: "20120618021055", sha256: "157cabb88b40306ff36667eb5f318225132c5153e253f611192a96b88c9571cf", wayback_url: "https://web.archive.org/web/20120618021055/http://rpgtoolkit.net/manual/page15.htm"}
---

# Systems

While the RPGToolkit allows you to create your own systems via , or an external language, this may not be appropriate for all situations (e.g., your first game). As a result, competent default menu and battle systems are included for your usage. This page covers the appearance and functionality of these systems within the trans3 game engine. [RPGCode](page17.htm)
The Menu System
If your game uses the default menu system, and you press the (generally ENTER), then you will be greeted with the main menu screen. [menu activation key](page3.htm#rpgcode.menuActivationKey)
In the centre of the screen, the stats of your active party are displayed, along with their profile pictures; the top-right features some miscellaneous information. To enter a new section of the menu, use your arrow keys, and press ENTER to choose an option.
Items
The sub-menu enables players to manage their inventories. A number in the corner informs users which page they are viewing. *Items*
- Use — Using an item invokes its effects on a select player.
- Info — which is set in the can be viewed by using this option. [Information](page8.htm#editor.description) [Item Editor](page8.htm)
- Drop — Dropping an item permanently removes it from your inventory.
- Return — Choosing closes the menu, and returns you to the game. *Return*
- Back — The choice returns the player to the main menu. *Back*
Equip
After choosing equip, and selecting the player whom you plan to set up, you are whisked to the equipment sub-menu.
- Equip — After selecting this option, select a slot, then the item to equip to that slot, and it will be equipt.
- Remove — Select a slot after choosing , and the item will be removed from that slot, and returned to your inventory. *Remove*
- Back — Returns you to the main menu.
Abilities
After choosing abilities and selecting the player whom you plan to set up, you are whisked to the abilities sub-menu.
- Use — Use an ability.
- Info — Read the set in the for a given abilty. [blurb](page12.htm#editor.description) [Special Move Editor](page12.htm)
- Back — Returns you to the main menu.
Save
The option allows you to save your progress to a *.sav file, if progress saving is enabled on the current board. *Save*
Load
allows players to restore their progress from a previously saved file. *Load*
Quit
If players choose , trans3 closes, and they are returned to Windows. *Quit*
The Battle System
Based on the odds, pool, and other information set in the , when walking around you will be thrust into a battle. The screen will look something like this: [Main File Editor](page3.htm)
The sections A, B, and C mark distinctive parts of the battle screen.
- A — The player's party
- B — The enemy party
- C — Party statistics (players get turns when their bars reach capacity)
Enemies also have "charge bars", though you cannot see them, and when they fill, an enemy will attack you. When your bars fill, a menu appears in the centre of the screen.
- Fight — Perform a "normal" (conventionally physical) attack
- Special Move (Eagle Eye) — Use an ability available to the player; the name of this is set in the [Character Editor](page7.htm)
- Items — Use an item from your inventory on an enemy or fellow party member
- Run (aka ) — Attempt to escape the fight *Flee*
The fight continues until either party is completely dead, or you flee.
- Enemies dead — You win! Experience and gold are handed out; the game proceeds
- Players dead — The runs, which typically restarts the game [game over program](page3.htm#rpgcode.gameOver)
- Fled successfully — The game proceeds, but you gain no experience or gold
