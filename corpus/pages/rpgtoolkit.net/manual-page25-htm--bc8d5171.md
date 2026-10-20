---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/manual/page25.htm"
site: "rpgtoolkit.net"
title: "There are three specific issues that you should read before continuing!"
original_url: "http://rpgtoolkit.net/manual/page25.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20120630014942"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/manual/page25.htm", captured: "20120630014942", sha256: "3cde76b6233b6c7aca2e5a9d9d17318f81f0352dd82d58bf3a6aa4b105a361a5", wayback_url: "https://web.archive.org/web/20120630014942/http://rpgtoolkit.net/manual/page25.htm"}
---

# There are three specific issues that you should read before continuing!

If you're having problems running the Toolkit, first check the page to ensure you have the correct components; then have a look through the following questions. If you cannot find the solution here, you can post a message on the Toolkit Support forums at . [System Requirements](page26.htm) [ToolkitZone](http://toolkitzone.com)
There are three specific issues that you should read before continuing!
- First, ensure that you have DirectX version 8.0 or above installed. To find out which DirectX version you have, either: If you have an earlier version, you can download the latest at . Even if you have a version greater than or equal to 8, but the remainder of these steps cannot rectify your problem, consider downloading the most recent release.
- Open the Control Panel and navigate to the DirectX properties window.
- Go to Start > Run... and type "dxdiag" (without quotes) in the text field and hit return.
- Second, if you are a Windows 9x user (95, 98, 98SE, ME), and are experiencing the following graphical problems, then there are at present ( ) no solutions to these problems. These problems are due to inconsistencies in the (Graphics Device Interface) of earlier Windows versions, which vary from machine to machine. Many Windows 9x users can run the Toolkit without any problems, and it's hit-and-miss whether a particular system will have these problems. However, the developers are working on solutions, and if you do encounter any of these problems please report them on the support forums, supplying as much information about your system specifications as possible. [3.0.6](page29.htm#3.0.6)
- Characters replaced by "fuzzy" or coloured squares.
- Transparent areas of characters or images replaced by colours or random images (often the cursor map hand).
- Horizontal lines across boards.
- Distortions in the default menu background and images placed using the image commands.
- Last, please ensure you have the of the Toolkit installed before consulting this page or reporting bugs. The Toolkit is under constant development, and it is possible that any problems you are having have been fixed in subsequent releases. **latest version**
Common Issues
Does the Toolkit support Linux, Solaris, or other Unix-based, Mac, or non-Windows operating systems?
Currently, no. The Toolkit is heavily dependent on Microsoft's DirectX and the Windows API, so ports to other OSs require reliance on Windows API implementations such as , or a substantial rewriting. As of version 3, the Toolkit is an project, and so anyone is free to port the Toolkit to other platforms if they wish. [Wine](http://winehq.org) [Open Source](http://opensource.org)
Is it possible to play TK games on a console or PDA?
Microsoft's operating system included with some has, albeit little, support for the Windows API and may run the TK to a degree. Unfortunately, other PDAs such as Palm Pilots, as well as consoles, have no chance due to the dependency on Windows. [Windows CE](http://microsoft.com/windowsce) [PocketPCs](http://microsoft.com/pocketpc) *very*
I get a very low frames-per-second rate (fps), and my players move very slowly. What can be done to improve this?
Fps is dependent on a number of factors, mainly memory and processor speed. The Toolkit requires both standard RAM and Video RAM (VRAM—as provided by a graphics card)—ideally you need around 64MB RAM and several MB of VRAM, which will be shared between all open applications you are running. Try closing any other open applications (for instance, media player or web browser) to free up system resources—both memory and processor.
Speed is also dependent on the graphics mode you run your games in: in general, full-screen games run faster than windowed, and lower resolutions are faster than higher ones. Also, colour depth sometimes makes a difference; generally speaking 32-bit colour is slightly faster than 24- or 16-bit.
I get the message, "A required .DLL file, MSVBVM60.DLL, was not found," when I try to install or run the Toolkit.
You require the VB Runtimes, which have been removed from the download because of their size. Most users will have these installed anyway, but if you are a Windows 95 user, or you experience this problem, download these from Microsoft and install. [files](http://microsoft.com/downloads/details.aspx?FamilyID=bf9a24f9-b5c5-48f4-8edd-cdf2d29a79d5)
I'm having trouble installing Toolkit 3.0.6+; the installer crashes half-way through or doesn't place all the files in the installed directory.
Some people have this problem with installing; for workarounds, see this tkz library document: [toolkitzone.com/library.php?mode=read&doc=104](http://toolkitzone.com/library.php?mode=read&doc=104)
When I use the flood fill tool in the Board or Tile Editors, tiles are erased or transparent pixels turn black.
In the Board Settings menu of the , and the Draw menu of the there are "Use Recursive Flood" options—enabling either of these should solve the problem. Note that with this enabled, you may not be able to flood large areas of large boards (approximately greater than 100x100). [Board Editor](page4.htm) [Tile Editor](page5.htm)
I'm not a Windows 9x user, but I still encounter graphical errors, including a flashing screen in fullscreen mode.
Try turning on the Vertical Sync option in your graphics card settings (if it has one), or turning down hardware acceleration, in Control Panel > Display > Settings > "Advanced" window.
My computer satisfies the system requirements, but the Toolkit still doesn't run properly!
There are probably a lot of answers to such a broad question, but in terms of technical issues, make sure you have the latest drivers for all your hardware components (especially the graphics card).
