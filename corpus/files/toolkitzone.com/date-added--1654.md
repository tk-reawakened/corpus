---
kind: file
id: "toolkitzone.com/1654"
site: "toolkitzone.com"
title: "Date Added"
original_url: "http://toolkitzone.com/files.php?file=1654"
written: null
date_confidence: "unknown"
updated: null
captured: ["20090123022944"]
author: "Johnstein"
repliers: []
authors: ["Johnstein"]
comments_present: 0
uploader: "Johnstein"
f_category: "All Categories Audio | -- Background | -- Effects | -- Other Graphics | -- Animations | -- Battle Backgrounds | -- Other | -- Tilesets | -- | -- Buildings (Exterior) | -- | -- Buildings (Interior) | -- | -- Characters | -- | -- Collections | -- | -- Items | -- | -- Monsters | -- | -- Other | -- | -- Terrain RPG Code | -- Custom Systems | -- Methods | -- Other | -- Plugins"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/files.php__file_1654", captured: "20090123022944", sha256: "56e1c9e389a7adf10ce24457e19f477c8180a34db986e5378acef76ae4e67daf", wayback_url: "https://web.archive.org/web/20090123022944/http://toolkitzone.com/files.php?file=1654"}
---

# Date Added

GetSaveData Plugin
This plugin allows you to extract data from a save file (*.sav). It can be usd with the to get a list of all save files, and display a custom save/load screen with some relevant data for each save like game time or the name/stats of party members. You have a number of options from returning a single variable to dumping a list of the variables to a plain text file. It has been recently updated in response to with the ability to find stray variables that the RPG Toolkit Garbage Collector can take up to an hour to clean up. [File Browser Plugin](http://www.toolkitzone.com/files.php?file=1652)
[![TBD](thumb.php?src=forum/images/avatars/15384843094781c08f3c0d7.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=328)
This only extracts Numerical, Object, and Literal data from the .sav file. (For those who've memorized the file-format, these are the first 3 sections). I'll try to add more of the file in the future, but really, with the current version, anything not accessible directly can be 'saved' to a variable prior to saving, and then read later. See the README for details, and PLEASE, let me know if anyone has any questions, bugs, or suggestions. EDIT: Critical Update to v1.1! It was bugging out with the object variables. v1.1 fixes this, and a couple other minor issues. There's also now an "Optional" 3rd parameter to specify an ASCII dump of the variables (numerical, object, and literal only, so far). This is useful for debugging purposes (so you can get a reality check on if the variable is being saved correctly, in addition to the fact that it's kinda cool to see the guts of your *.sav file) EDIT2: v1.2 provides Array support. Simplifies things when looking up multiple variables. EDIT3: v1.3 fixed a MAJOR bug if the bytecount of the *.sav file is greater than 32768. (yea, oops). Also, based on fury's feedback and to remain consistent with the way TK currently saves *.sav files, the default path has been moved to the ..\..\Saved directory, rather than the gamepath Finally, new commands have been added. void DumpASCII(SavFile, OutputFile) just creates an output file without having to specify a variable to look up. int GetGarbage(SavFile, OrphanArrayName, [OutputFile]) This will read a SavFile, find all the orphaned variables (private member variables of unreferenced objects) and save them in the OrphanArrayName[]. If OutputFile is indicated, the output of the Sav file, along with information on the active and orphaned variables, will be saved in the Saved directory. GetGarbage returns the ubound of the new OrphanArrayName (lbound = 1)
Who's Online: , , , , , , , , , [EB](community.php?user=84) [Geep4W](community.php?user=13474) [Khin](community.php?user=157) [Lawck](community.php?user=2988) [Moo Of Doom](community.php?user=334) [Mr Picso](community.php?user=3699) [Nick-Champagne](community.php?user=23445) [Rhodes.](community.php?user=2214) [slipknot_hellraiser](community.php?user=4090) [zyrshnikashnu](community.php?user=254)
