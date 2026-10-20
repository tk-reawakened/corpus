---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/manual/page9.htm"
site: "rpgtoolkit.net"
title: "[ ]Around the Editor"
original_url: "http://rpgtoolkit.net/manual/page9.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20120618194803"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/manual/page9.htm", captured: "20120618194803", sha256: "8919fc4fb51991b41cbf9a4c0874e7ee84445406d2b247befd1c2e6c2f6f7e8b", wayback_url: "https://web.archive.org/web/20120618194803/http://rpgtoolkit.net/manual/page9.htm"}
---

# [ ]Around the Editor

Enemy Basics
Enemies are the staple of most role-play games and are normally either encountered randomly or in planned scenes (for instance, the boss at the end of a level). In the Toolkit, random battles occur spontaneously when they are allowed; that is, enemies aren't visible on the board before a battle and players are transported to the battle system when a battle is triggered (unless, of course, you code your own battle system). This is a reflection of the idea that the players are confronted by enemies without warning whilst they move around the game.
Around the Editor
Basic Info
- Name - Name of the enemy, that appears in the enemy list in battle.
- Max Health Points - Starting and maximum HP.
- Special Move Power - Starting and maximum SMP.
- Fighting Power - Attack strength.
- Defence Power - Defensive strength.
Fighting Conditions
- Player can run from enemy - In most situations, you may want the player to be able to run from a battle rather than finishing it, but in planned battles (for instance with bosses) you may want to disable this option. If enabled, you can specify a program to be run when this happens, for instance to penalise the player for running instead of fighting (e.g., he could drop money).
- Chances of critical hit on enemy - The probability that an attack by the player on this enemy causes maximum damage; that is, the enemy's defence is ineffective and the DP is not subtracted from the FP.
- Chances of critical hit on player - As above, for the attacks by the enemy on the player.
Graphics - Shows a window where you can set (*.anm) for several actions the enemy can make. Select the type from the list on the left, and hit "Browse" to select an animation. All enemy graphics must be saved as animations, even for single-frame images. Custom actions can be added using the "Add" and "Remove" buttons. [animations](page10.htm)
Special Moves - Enemies can also make , just like players. Create special moves for enemies in the same way as for characters and assign them in the left-hand list in this window. Enemies will use their special moves randomly, dependent on their AI and amount of SMP. Remember to give the enemy enough SMP for the moves he has! You can also make the enemy susceptible to certain moves; that is, such moves inflict more damage than they normally would. Add these to the "Weaknesses" list on the right. [special moves](page12.htm)
Tactics - Enemies are controlled by the computer, and must be given some kind of instruction in order to act as enemies in battle and attack the players. Enemies use basic AI (artificial intelligence) from the Toolkit, which has four levels:
- Low - Enemy attacks random players with a random combination of standard (physical) attacks and special moves (if it can make these).
- Medium - Enemy attacks random players, but uses special moves (if it has any) until its SMP is exhausted, at which point it reverts to normal attacks.
- High - Enemy attacks the weakest player with a random combination of standard attacks and special moves.
- Very High - Enemy attacks the weakest player with special moves until SMP is exhausted.
You may want to write your own AI instead of using the presets - if so, select the option here and specify the RPGCode program in the text box.
Rewards - One of the main reasons for fighting is so that the player can gain the experience required to earn him further abilities and skills needed to advance through the game. The amount of experience the player is rewarded with is normally proportional to the difficulty of the enemy and the scaling of the player's skill levels. As well as this players can also be rewarded with physical objects; money can be given via the GP text box and a program can be specified for other rewards such as items.
Add Enemy To Game - This opens the edit fighting window. [Main File Editor](page3.htm)
