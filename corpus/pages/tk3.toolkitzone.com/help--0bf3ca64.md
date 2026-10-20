---
kind: page
id: "tk3.toolkitzone.com/tk3.toolkitzone.com/help/?page=13"
site: "tk3.toolkitzone.com"
title: "Status Effect Basics"
original_url: "http://tk3.toolkitzone.com/help/?page=13"
written: null
date_confidence: "unknown"
updated: null
captured: ["20051027180027", "20070123120228"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/tk3.toolkitzone.com/help__page_13_amp_3BPHPSESSID_16097a3a6f8dae38d835cae025f2adc4", captured: "20051027180027", sha256: "6b408b56ed7f73dc904811a590eb08e7bb1ad3cc40545ebfc647a911e2022c75", wayback_url: "https://web.archive.org/web/20051027180027/http://tk3.toolkitzone.com/help/?page=13&amp%3BPHPSESSID=16097a3a6f8dae38d835cae025f2adc4"}
  - {path: "wayback/toolkitzone.com/tk3.toolkitzone.com/help__page_13", captured: "20070123120228", sha256: "457de86a834a05e26ddc806933b771a4d4926a537b6d66a8465ff577180622c0", wayback_url: "https://web.archive.org/web/20070123120228/http://tk3.toolkitzone.com/help/?page=13"}
---

# Status Effect Basics

A Status Effect (*.ste) is a condition that alters the attributes a player or enemy in battle for a short period of time, as the result of a or attack. For instance, it could be the result of a spell that reduces the enemy's response time or completely immobilises them for a number of turns. Several effects have options set up in the editor, whilst others can be crafted in RPGCode and run when the effect is applied. [special move](?page=12)
Status effects can also be applied through RPGCode using the ApplyStatus() and RemoveStatus() commands (for instance, if you are writing your own battle system in RPGCode).
Around the Editor
Status Effect Name - Name that appears when the effect occurs.
Number of Rounds Until Effect is Removed - In turn-based fighting a round constitutes one attack by all participants, in real-time fighting this would be the number of turns the target takes.
Speed Target Charge Time - This effect decreases the "charge time", the time the target must wait (to recharge his strength) in between moves.
Slow Target Charge Time - This effect increases the "charge time".
Disable Target - Stops the target from charging, preventing them from taking a turn and effectively disabling them.
Remove HP - The amount of hit points (HP) the target loses (or gains if set negative) . *each round*
Remove SMP - The amount of SMP the target loses (or gains if set negative) each round.
Run RPGCode Program - You may want to apply more specialised or complex effects than those provided above, and you can do this through RPGCode by attaching a program here.
