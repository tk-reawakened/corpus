---
kind: file
id: "toolkitzone.com/312"
site: "toolkitzone.com"
title: "password"
original_url: "http://toolkitzone.com/fileman.php?id=10&file=312"
written: null
date_confidence: "unknown"
updated: null
captured: ["20040705035722", "20040705035722", "20040705035722", "20040720173552", "20040720173552", "20040720173552", "20041114084247"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_312", captured: "20040705035722", sha256: "3538fb4fdb127bfd2d54070faca7d13520d4bda51bfde16e591083734cd7b34c", wayback_url: "https://web.archive.org/web/20040705035722/http://toolkitzone.com/fileman.php?id=3&file=312"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_312-7afbe3", captured: "20040705035722", sha256: "3538fb4fdb127bfd2d54070faca7d13520d4bda51bfde16e591083734cd7b34c", wayback_url: "https://web.archive.org/web/20040705035722/http://www.toolkitzone.com/fileman.php?id=3&file=312"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_312-fbcbf0", captured: "20040705035722", sha256: "3538fb4fdb127bfd2d54070faca7d13520d4bda51bfde16e591083734cd7b34c", wayback_url: "https://web.archive.org/web/20040705035722/http://toolkitzone.com/fileman.php?id=3&file=312"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_312", captured: "20040720173552", sha256: "b0b08e51e8613655a9e53a4ecb9e2fa2e210244b19dcf2798fd62f867542f7ea", wayback_url: "https://web.archive.org/web/20040720173552/http://toolkitzone.com/fileman.php?id=10&file=312"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_312-6ba5f6", captured: "20040720173552", sha256: "b0b08e51e8613655a9e53a4ecb9e2fa2e210244b19dcf2798fd62f867542f7ea", wayback_url: "https://web.archive.org/web/20040720173552/http://www.toolkitzone.com/fileman.php?id=10&file=312"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_312-dca729", captured: "20040720173552", sha256: "b0b08e51e8613655a9e53a4ecb9e2fa2e210244b19dcf2798fd62f867542f7ea", wayback_url: "https://web.archive.org/web/20040720173552/http://toolkitzone.com/fileman.php?id=10&file=312"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_312", captured: "20041114084247", sha256: "820ecb55595bccc8f04a021f177e03a426403b8641a1abbe839528b598eae715", wayback_url: "https://web.archive.org/web/20041114084247/http://www.toolkitzone.com/fileman.php?id=5&file=312"}
---

# password

beta version - report any problems to (redacted: email)
-------------------------------------------------------------
KSNiloc's VB SDK FAQ
For those of use who like things simple
-------------------------------------------------------------
---Introduction---
Up until recently, Plugins had to be written in C++ or Delphi. The reason is quite simple: The RPGToolkit has no support for the only type of DLL Visual Basic could compile- ActiveX DLLs. Also, Visual Basic only had "Class Modules" not a full-blown object-oriented system. But thanks to Truiken, we can now write plugins in VB.
---Understanding the System---
The system works by using one plugin (similar to multiplug) to call other plugins. However, unlike Multiplug it requires a config file, namely "plugins.ini". In case you are not familiar with .ini files, here's the lowdown:
There are always section titles, written like this:
[Section]
This tells the program reading the file where specific settings are stiored. There are "keys" or sorts, or settings. They are added below the sections like so:
Setting=Value
The left of the equals sign the what the value on the right is being put into.
You can "comment" out a line with a ";". This is similar to RPGCode's *, except, I believe, it can only be placed at the beginning of a line.
[Test] testval=testset ;oldval=oldset
---Sections and Keys of Plugins.ini---
At the top of plugins.ini, you're always going to have a [Config] section. In that section we'll define which folders we're going to put the different types of plugins in. Here are this section's keys...
TKPlugDir= Folder where regular TK Plugins go StdDllDir= Folder where "Standard DLLs" go ActiveXDllDir=Folder where ActiveX DLLs go
Also in the section are several misc. options:
ShowStartupScreen=1 or 0 - Whether or not to show a screen allowing you to choose which plugins to launch.
LogErrors=1 or 0 - If set to 1 a log file will be kept in the "Plugin" folder.
From there on, you'll declare you plugins as sections (i.e. [MyPlugin.dll]. There are a few keys you'll need for each of these sections too...
Name=The name of the plugin
Type=The type of plugin ("TKPlugin", "Standard Dll", or "ActiveX Dll")
CLSID=The kicker for VB Plugins. The class ID... this would be something like "ProjectName.ClassName".
EnabledByDefault=1 or 0 - Set to 1 if you want to use the plugin without the menu.
Author= -These two are things you can set to display AuthorEmail= stuff on the startup screen.
---Closing Words---
Now that I've written this, I won't be including explicit instructions on how to setup my VB Plugins anymore. But you'll know how...
--KSNiloc (redacted: email)
