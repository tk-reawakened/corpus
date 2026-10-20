---
kind: file
id: "toolkitzone.com/1652"
site: "toolkitzone.com"
title: "Date Added"
original_url: "http://toolkitzone.com/files.php?file=1652"
written: null
date_confidence: "unknown"
updated: null
captured: ["20090123022933"]
author: "Johnstein"
repliers: []
authors: ["Johnstein"]
comments_present: 0
uploader: "Johnstein"
f_category: "All Categories Audio | -- Background | -- Effects | -- Other Graphics | -- Animations | -- Battle Backgrounds | -- Other | -- Tilesets | -- | -- Buildings (Exterior) | -- | -- Buildings (Interior) | -- | -- Characters | -- | -- Collections | -- | -- Items | -- | -- Monsters | -- | -- Other | -- | -- Terrain RPG Code | -- Custom Systems | -- Methods | -- Other | -- Plugins"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/files.php__file_1652", captured: "20090123022933", sha256: "d6cc335a078634303465690b2999bc78c2bab98608c7edcaa6c3951856eaee27", wayback_url: "https://web.archive.org/web/20090123022933/http://toolkitzone.com/files.php?file=1652"}
---

# Date Added

FileBrowserPlugin
In under a day Johnstein has managed to create a plugin in response to a . This plugin can display a file browser to the user that allows one or multiple files to be selected and returns the result to be used in RPG Code. Alternatively you can also retrieve the list of files in a directory without prompting the user. This can be very useful for custom item/enemy/save systems or for debugging programs. Updated with three new commands have been added: FileExist, DirExist, and GetFilename. The first two are self explanatory, GetFilename will return a filename with the path stripped off. Also some general improvements and fixes. [forum discussion](http://www.toolkitzone.com/forum/viewtopic.php?t=42265&start=40)
![TBD](templates/default/images/icons/rating_blue_3.5.gif)
*3 votes cast.*
I down loaded this and compared it to John@aljo's Plugin as it is the only other one that will do this. For testing this plugin is easier for a novice to use and most advanced users are probably into the easy set up. An advanced user who has taken the time to make a decent file viewer with the shell and RPGcode might be happier with the shell as it has filters and allows you to do some things that this will not do and I am not sure it can be made to do. As far as use in a completed game the shell is the only way to go if you want it in style with the rest of your game and it is possible with the shell to keep players from messing up. With this I can see several ways for users to mess up if they get out of the files where they should be and off hand I do not see anyway to keep them from selecting the wrong type of file. The major plus with this is simple to use where as the shell has a step learning curve. Over all for testing a useful plugin, but is not something that I would advise to use in a finished game. [Shell](http://www.toolkitzone.com/files.php?file=169)
[![TBD](thumb.php?src=forum/images/avatars/15384843094781c08f3c0d7.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=328)
Thanks for the review brandon34. Yea, I'm no shell programmer. I just needed a simple way to get a list of files from a directory (something I hope default TK can do one day). I'd agree that the graphical portion would not be useful in a game and more useful when debugging, but I *DO* think the FileList() command can be quite useful in a finished game. In fact, I'm using it quite extensively on my save and load class to retrieve a list of all the *.sav files in the Saved directory. (no user input) So I would still advise people to use the FileList() command if they want a simple solution on getting a list of files but I'll agree that if they want something that looks fancy, this isn't the way to go. Thanks again P.S. Oh yea, and v1.2 has been released with a couple of functions to see if files or directories exist, along with returning the filename. Probably could be done in RPGcode, but it was feeling clunky so I did it in the plugin.
[![TBD](thumb.php?src=forum/images/avatars/625094848457cf1f58da78.gif&w=60&h=60&iar=false&bw=1)](forum/profile.php?mode=viewprofile&u=14726)
The graphical solutions is useful for debugging your game... You as a developer can select specific files to test out, which I thing is very useful. I can imagine a script where you select a board, a player, and some items, and test them all out together at the end of the program.
None found.
Who's Online: , , , , , , , , , [EB](community.php?user=84) [Geep4W](community.php?user=13474) [Khin](community.php?user=157) [Lawck](community.php?user=2988) [Moo Of Doom](community.php?user=334) [Mr Picso](community.php?user=3699) [Nick-Champagne](community.php?user=23445) [Rhodes.](community.php?user=2214) [slipknot_hellraiser](community.php?user=4090) [zyrshnikashnu](community.php?user=254)
