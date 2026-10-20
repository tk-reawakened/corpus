---
kind: file
id: "toolkitzone.com/594"
site: "toolkitzone.com"
title: "Setting up OCXes"
original_url: "http://www.toolkitzone.com/fileman.php?id=10&file=594"
written: "2004-05-13"
date_confidence: "day"
updated: "2004-05-13"
captured: ["20051226180921", "20060312125821", "20060312130311"]
author: "Colin"
repliers: []
authors: ["Colin"]
comments_present: 0
f_author_source: "KSNiloc"
f_name: "Setting up OCXes"
f_submitted_by: "Colin"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_594", captured: "20051226180921", sha256: "852759f2bb7a03d08b8ff649f76bc8562a54afc0e15034b2e417d2c781594e04", wayback_url: "https://web.archive.org/web/20051226180921/http://www.toolkitzone.com/fileman.php?id=3&file=594"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_7_file_594", captured: "20060312125821", sha256: "2f72b41caea09f0d784a13e3f246ba6a7aafbfdce49cab04be20fe277fc4ad27", wayback_url: "https://web.archive.org/web/20060312125821/http://www.toolkitzone.com:80/fileman.php?id=7&file=594&PHPSESSID=9e94a0bfd739af13980670d1e820a329"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_594", captured: "20060312130311", sha256: "bcfcd4e421eef04f327a4f0f932e56bf288c1f4142120fb3d80046ea3aa77a1c", wayback_url: "https://web.archive.org/web/20060312130311/http://www.toolkitzone.com:80/fileman.php?id=10&file=594&PHPSESSID=9e94a0bfd739af13980670d1e820a329"}
---

# Setting up OCXes

A small document explaining how to update OCX's. Could use a little bloating but I guess it's short and sweet.
-----------------------------------------------------------------------
Setting up OCXes
For those of us who hate the way windows works
-----------------------------------------------------------------------
---Opening---
In order to express how many times I have had people experiencing problems related to OCXes I would need to use scientific notation to a very high power. But this simple tutorial should clear up those questions once and for all!
---Toolkit Related Problems---
Question: I install the toolkit but when it opens you recieve errors about OCXes. How do I fix this?
Answer: More likely than not you're attempting to install the TK on a system where you don't have administrive powers (i.e. a school). Windows prevents the control from being setup properly.
Question: I don't use the TK but I just downloaded a game and when I tried to launch it I got problems to do with OCXes.
Answer: Locate the folder of the game and run the file regocx.bat. Provided you have administrive powers, this will fix the problem.
---Other Problems---
Before you proceed: Make a folder in the root of your C drive called "OCXes".
Whenever you recieve an error regarding on OCX (read *every* error carefully), follow these steps. These may included opening an RPGCode editor or many other situations.
1. Write down the name of the OCX mentioned in the error.
2. Obtain the OCX. There are several ways to acomplish this.
a) Search on Google for "download " then the OCX. b) Search your hard-drive
3. Place your OCX in the "C:\OCXes" folder.
5. Click Start --> Run and type in:
"regsvr32.exe C:\OCXes\[ocx name]"
---Closing---
I hope this helps everyone. Thank you for reading!
--KSNiloc (redacted: email)
**Browse Sections**
