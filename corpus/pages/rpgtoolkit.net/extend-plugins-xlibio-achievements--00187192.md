---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/extend/plugins/xlibio/achievements/"
site: "rpgtoolkit.net"
title: "July 22nd, 2014"
original_url: "http://rpgtoolkit.net/extend/plugins/xlibio/achievements/"
written: "2014-07-22"
date_confidence: "day"
updated: null
captured: ["20141120150844"]
author: null
repliers: []
authors: []
comments_present: 0
duplicate_of: "rpgtoolkit.net/rpgtoolkit.net/extend/plugins/xlibio/"
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/extend/plugins/xlibio/achievements/index", captured: "20141120150844", sha256: "114439b06861c12d05581d636dbde3aeb7bec5a226bca1a212b904228124f3f2", wayback_url: "https://web.archive.org/web/20141120150844/http://rpgtoolkit.net/extend/plugins/xlibio/achievements/"}
---

# July 22nd, 2014

Fishbate the Worm / Grindalf & Lotusware
[![Xavier](thumb/80/community/images/avatars/upload/202350491243172dcbd2811.png)](member/xavier/)
Released
**July 22nd, 2014**
Viewed times **347**
Downloaded times **62**
comments have been written **0**
Developed by Xavier
xLib.IO
**Read and write functionality to text files.**
Provides more concise commands for easy writing and reading, especially as the Toolkit 3.2 input/output commands are broke.
id = ioOpen(filename, mode)
Filename is relative to your game directory, so you can include a path (e.g. Misc/file.txt). Mode is either r (read), w (write, overwrites any existing file), or a (append, adds to any existing file). If the file doesn't exist, it creates it for you. The command returns a numerical id for referencing with future commands.
ioWrite(id, text)
Writes the next line.
text = ioRead(id)
Reads the next line.
end = ioEndOfFile(id)
Whether you've reached the end of the file when reading lines, 1 = yes, 0 = no
ioClose(id)
Close the file when you're done with it, releasing memory.
ioDelete(filename)
Delete a file for good. Filename is relative to your game directory, so you can include a path (e.g. Misc/file.txt).
