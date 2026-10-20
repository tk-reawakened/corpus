---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/opensource/submission.html"
site: "rpgtoolkit.net"
title: "Source Code"
original_url: "http://www.rpgtoolkit.net/opensource/submission.html"
written: null
date_confidence: "unknown"
updated: null
captured: ["20050217064244"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/opensource/submission.html", captured: "20050217064244", sha256: "b6083977198fd9f07e65d70e8e768adb1992ffe3c806e89a2ee2da3b2d9e96ab", wayback_url: "https://web.archive.org/web/20050217064244/http://www.rpgtoolkit.net/opensource/submission.html"}
---

# Source Code

Licenses
Sending me the chages: Thank you for your support of this project! If you have made changes to TK3 and would like them included in the official distribution, follow these steps: Making changes: RPG Toolkit Development System, Version 3 Main Distribution Submission Guidelines
- It's probably a good idea to copy the source tree of TK3 into an entirely new folder, and make changes in that folder. That way you can make changes and still compare them against the original source tree you got from this site.
- If you create new subs or functions, try to give them comments at the top that explain what each argument to the sub/function do. If you create new RPGCode commands, make sure the comments at the top of the sub/function are the same type that are at the top of other RPGCode commands.
- If at all possible, make calls to the windows API if it will stop you from adding new OCX components to the project. I will be cautious about adding new OCX components to the project for a few reasons:
- I can't be sure I am legally entitled to reistribute them.
- They increase the size of the TK3 download.
- They can stop the TK from working properly if not comfigured correctly on the user's system.
- Make another new directory on your computer.
- In that directory, copy the files that you have *modified*. Do send me the entire source tree. not
- If you don't know which files you have modified, get a program like and compare your 'modified' source tree to the 'official' source tree (note: if you specify two *directories* in winmerge, it will show you which files have been modified between them). [WinMerge](http://winmerge.sourceforge.net/)
- Please copy only the files you have modified, and copy them in such a way that they retain their path information (for instance, if you modified v3\vb\tkCommon\modules\CommonAnimation.bas, copy it into a folder called v3\vb\tkCommon\modules\ in the tree you are preparing for me.
- At the root level of the new folder, copy LICENSE.txt, which is distributed with the source code form this.
- If you do not perform this step, your code will be rejected. I have to take a hard line on this because it's a legal thing. It indicates that you are releasing your modifications under the same source code license that TK3 has.
- At the root level of the folder, create a file called history.txt, and put some descriptions of the changes you made (if there are new RPGCode commands, explain how they work and give an example).
- Finally, zip up the new folder and email it to me. In the email, say who you would like this contribution credited to (either your real name or your screen name).
- I will code-review your changes. If everything is in order, they will be added to the main TK3 distribution! If there are problems, I'll write you back and ask you to fix things.
