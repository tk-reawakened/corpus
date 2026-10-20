---
kind: doc
id: "toolkitzone.com/190"
site: "toolkitzone.com"
title: "Column"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=190"
written: "2005-02-28T12:01:00"
date_confidence: "exact"
updated: null
captured: ["20060209061404", "20060612033028", "20070308231628"]
author: "Colin"
repliers: []
authors: ["Colin"]
comments_present: 0
f_author: "Colin"
f_date: "February 28, 2005, 12:01 pm"
f_description: "One of the key aspects of user / developer interaction is that of bug reporting, but often simply stating X does not work isn't enough to help fix an issue or actually identify it as a bug in the first place."
f_title: "Filing RPGCode Bug Reports"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_view_cadd_doc_190", captured: "20060209061404", sha256: "d31e16e643d5ed4688fa722018af585703930f82cf4d3f26d1eca8781ae98cef", wayback_url: "https://web.archive.org/web/20060209061404/http://www.toolkitzone.com:80/library.php?mode=read&view=cadd&doc=190&PHPSESSID=6c1f0d3aa43a19d10f2020f481c20c7a"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_190", captured: "20060612033028", sha256: "869a3f9344d19f699e7864e9e56f5926fb8eb5a04569510c08f69b7d8c24f9a5", wayback_url: "https://web.archive.org/web/20060612033028/http://www.toolkitzone.com/library.php?mode=read&doc=190"}
  - {path: "wayback/toolkitzone.com/library.php__doc_190_highlight_", captured: "20070308231628", sha256: "1d279131ae1b74a6bb75bc9c376d924036b4df131b6896760796d111c6d68ad7", wayback_url: "https://web.archive.org/web/20070308231628/http://www.toolkitzone.com:80/library.php?doc=190&highlight"}
---

# Column

TK3 Amelioration XI Filing an RPGCode Bug Report
Prelude
The RPGToolkits internal scripting language, RPGCode, isnt exactly bug proof. Bugs exist. And they arent rare. If youve found one, we commend you—and wed like to fix it. Unfortunately, just being told "x command doesnt work" or "my program [ 500 lines here ] has undesired behaviour y" just doesnt do us—or yourself—any good at all. Sometimes what you may be claiming to be a bug isnt even!—Or perhaps, you arent on the latest version. Before you post a bug, please follow these steps.
Rationale
Yes, I'm aware the better part of these steps sound may like common sense. However, a general, organized list of common sense is never a bad thing. Especially the earlier steps may sound really obvious, but it's better than hearing "you never told us". ;) Please bear with me.
1) Have the Latest Version
If youre planning on filing a bug report, have the latest version of the 3.x series before doing so. Unfortunately, TK2 is long since obsolete and no longer supported, and it is pointless to address problems from outdated versions of 3.x since they may—and probably are—sorted in latter releases. That said; please have the latest version of the RPGToolkit before reporting any bug. If you have the current release, proceed to step two.
2) Make Sure Its a Bug
Is the problem in question actually a bug? Find out. Are other people successfully performing a task which you just cannot? If so, ask them if, perhaps, youre doing something wrong. Maybe youre using a feature in a generally incorrect manner; consider reading available material to confirm you are indeed doing everything the intended way.
3) Narrow it Down
If your battle system doesnt work, do not post this. Instead, isolate the actual problem; use a method like repeatedly calling debugger() or mwin(). Perhaps, in this stage, youll realize that it was something completely different than you ever suspected. If you are, without a doubt, confident that you know the actual problem, proceed to the next step.
4) Create a New Program
Huge programs are no fun to write. Theyre even less fun to debug, and we dont want to debug for you. After youve isolated the problem, prepare a whole new program that shows nothing but the problem. This program should be free of superfluous details, and have dependencies on absolutely no other files. Mark the problem area using a comment in a very blatant fashion.
5) Post a Competent, Useful Report
After completing the above, please do not just post your bug exploiting program. Instead, logically provide relevant details. Open with how you discovered the bug; cover how, exactly, it was narrowed down; affirm that you have the latest version. Detail what your program is intended to show—point to the (marked) problem area. Describe the behaviour that you are witnessing.
Conclusion
Bugs make programming in RPGCode difficult, and this is not good. Being programmers ourselves, we would like to ensure your experience coding in RPGCode is as pleasurable as possible. However, in order to remedy issues you may have, we need to fully understand the problem and speed all our time fixing it, rather than finding it within your programs. A good bug report is filed using the latest version, really does cover a bug, and, in its intelligent post, provides a small program was illustrates the problem. In order to ensure a quick solution to your problem, we appreciate your following this suggested template. Thank you, and good luck programming in RPGCode!
**Column**
Toolkit 3.x > TK3 Amelioration
One of the key aspects of user / developer interaction is that of bug reporting, but often simply stating X does not work isn't enough to help fix an issue or actually identify it as a bug in the first place.
**Past Columns**
Feb 13, '05
Feb 7, '05
Jan 30, '05
Jan 16, '05
Jan 2, '05
Feb 13, '05
Feb 7, '05
Jan 30, '05
Jan 16, '05
Jan 2, '05
