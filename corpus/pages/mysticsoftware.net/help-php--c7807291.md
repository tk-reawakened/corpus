---
kind: page
id: "mysticsoftware.net/mysticsoftware.net/help.php?article=21&mode=1"
site: "mysticsoftware.net"
title: "Mystic Software"
original_url: "http://www.mysticsoftware.net/help.php?mode=1&article=21"
written: null
date_confidence: "unknown"
updated: null
captured: ["20041106104519"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/mysticsoftware.net/help.php__mode_1_article_21", captured: "20041106104519", sha256: "4beab1c0f59ce4a9d4211908d01d2122daadd5a55fbf87318fedbe777a3a12b6", wayback_url: "https://web.archive.org/web/20041106104519/http://www.mysticsoftware.net/help.php?mode=1&article=21"}
---

# Mystic Software

---Introduction--- Up until recently, Plugins had to be written in C++ or Delphi. The reason is quite simple: The RPGToolkit has no support for the only type of DLL Visual Basic could compile- ActiveX DLLs. Also, Visual Basic only had "Class Modules" not a full-blown object-oriented system. But thanks to Truiken, we can now write plugins in VB. ---Understanding the System--- The system works by using one plugin (similar to multiplug) to call other plugins. However, unlike Multiplug it requires a config file, namely "plugins.ini". In case you are not familiar with .ini files, here's the lowdown: There are always section titles, written like this: [Section] This tells the program reading the file where specific settings are stiored. There are "keys" or sorts, or settings. They are added below the sections like so: Setting=Value The left of the equals sign the what the value on the right is being put into. You can "comment" out a line with a ";". This is similar to RPGCode's *, except, I believe, it can only be placed at the beginning of a line. [Test] testval=testset ;oldval=oldset ---Sections and Keys of Plugins.ini--- At the top of plugins.ini, you're always going to have a [Config] section. In that section we'll define which folders we're going to put the different types of plugins in. Here are this section's keys... TKPlugDir= Folder where regular TK Plugins go StdDllDir= Folder where "Standard DLLs" go ActiveXDllDir=Folder where ActiveX DLLs go Also in the section are several misc. options: ShowStartupScreen=1 or 0 - Whether or not to show a screen allowing you to choose which plugins to launch. LogErrors=1 or 0 - If set to 1 a log file will be kept in the "Plugin" folder. From there on, you'll declare you plugins as sections (i.e. [MyPlugin.dll]. There are a few keys you'll need for each of these sections too... Name=The name of the plugin Type=The type of plugin ("TKPlugin", "Standard Dll", or "ActiveX Dll") CLSID=The kicker for VB Plugins. The class ID... this would be something like "ProjectName.ClassName". EnabledByDefault=1 or 0 - Set to 1 if you want to use the plugin without the menu. Author= -These two are things you can set to display AuthorEmail= stuff on the startup screen. ---Closing Words--- Now that I've written this, I won't be including explicit instructions on how to setup my VB Plugins anymore. But you'll know how... --KSNiloc cjf@mail15.com
-------------------------------------------------- KSNiloc's VB SDK FAQ For those of use who like things simple --------------------------------------------------
