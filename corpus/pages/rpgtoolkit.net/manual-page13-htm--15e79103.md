---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/manual/page13.htm"
site: "rpgtoolkit.net"
title: "Status Effect Basics"
original_url: "http://rpgtoolkit.net/manual/page13.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20120618195748"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/manual/page13.htm", captured: "20120618195748", sha256: "03a5cdba0bf21f890101a7428f046bf266f2de924807e35b04a2dbc5ff9560e6", wayback_url: "https://web.archive.org/web/20120618195748/http://rpgtoolkit.net/manual/page13.htm"}
---

# Status Effect Basics

A Status Effect (*.ste) is a condition that alters the attributes a player or enemy in battle for a short period of time, as the result of a or attack. For instance, it could be the result of a spell that reduces the enemy's response time or completely immobilises them for a number of turns. Several effects have options set up in the editor, whilst others can be crafted in RPGCode and run when the effect is applied. [special move](page12.htm)
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
