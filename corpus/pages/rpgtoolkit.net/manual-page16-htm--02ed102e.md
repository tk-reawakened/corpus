---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/manual/page16.htm"
site: "rpgtoolkit.net"
title: "PakFile"
original_url: "http://rpgtoolkit.net/manual/page16.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20120618020910"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/manual/page16.htm", captured: "20120618020910", sha256: "ae7e3b4bbcc9eba7d3e5ccafcea4677a9ff7922ad182e87f93e93358cf85fd63", wayback_url: "https://web.archive.org/web/20120618020910/http://rpgtoolkit.net/manual/page16.htm"}
---

# PakFile

After you complete and polish your Toolkit game, there are many ways that you can package it for distribution to the outside world. This page details the most commonly employed of those ways.
PakFile
Now largely unused, PakFiles (*.tpk) are archives that can be loaded like Main Files (*.gam), but contain all the information about a project. The obvious disadvantage of using this scheme is that the recipient must have the Toolkit in order to play your game. You can create a PakFile from a in the . [menu](pageed_environment.htm#menus.pak) [main window](pageed_environment.htm)
Native Setup Program
This feature builds you game into a *.zip file which includes a generic installer capable of copying the files to a pre-chosen directory. It too is available from a . Depreciated in favour of standalone executables or third-party utilities. [menu](pageed_environment.htm#menus.setup)
Standalone Executable
Since , the Toolkit can compile your game to a single *.exe file. This file is void of all dependencies (except, of course, the VB runtimes like the TK itself—but these are on just about every Windows system today), and can be distributed with ease. Executables are also built from a . [3.0.4](page29.htm#3.0.4) [menu](pageed_environment.htm#menus.exe)
Third-Party Utility
If you are planning to package your game using a third-party utility (e.g., ), be aware that only a small set of files are required to be included in the directory used. They are as follows: [Install Creator](http://clickteam.com)
- Your main file, which should be located in \Main\Main.gam
- The game project itself, in \Game\YourGame
- trans3.exe—the game engine
- actkrt3.dll—game engine runtime library
- audiere.dll— media player [Audiere](http://audiere.sf.net)
- freeimage.dll— image library [FreeImage](http://freeimage.sf.net)
