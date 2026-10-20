---
kind: page
id: "codebible.toolkitzone.com/codebible.toolkitzone.com/index.php?title=Reserved_Variables"
site: "codebible.toolkitzone.com"
title: "Reserved Variables"
original_url: "http://codebible.toolkitzone.com/index.php?title=Reserved_Variables"
written: null
date_confidence: "unknown"
updated: null
captured: ["20100621051449"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/codebible.toolkitzone.com/index.php__title_Reserved_Variables", captured: "20100621051449", sha256: "23a7882a499fff2ea487b3cbb7404aebb57d0dfb0c3fa1274c93d9ed8e678851", wayback_url: "https://web.archive.org/web/20100621051449/http://codebible.toolkitzone.com/index.php?title=Reserved_Variables"}
---

# Reserved Variables

There are a number of variables and constants that the RPGToolkit's engine automatically creates when you start your game which pertain to various things like players and boards. Each are accessible independently, though there are function alternatives to retrieving and setting some of them (the preferred way).
Player Variables
- â returns the handles (names) of any player in your party. index is a value **playerHandle[index]**
between 0 and 4 (0 is the first player, 1 is the second, et cetera).
- â returns the x coordinate of any player in your party currently on the board. index **playerX[index]**
is a value between 0 and 4. Alternatively, the playerLocation() function can be used to obtain this value and others.
- â returns the y coordinate of any player in your party currently on the board. index **playerY[index]**
is a value between 0 and 4. Alternatively, the playerLocation() function can be used to obtain this value and others.
- â returns the layer of the board that the player is currently on. index is a value **playerLayer[index]**
between 0 and 4. Alternatively, the playerLocation() function can be used to obtain this value and others.
Board Variables
- â returns the fight background of the current board. **boardBackground**
- â returns the fighting skill of the enemies on the current board. **boardSkill**
- â returns the titles assigned to the board layers. index is a value between 0 and **boardTitle[index]**
the number of layers on the board.
- â returns the board constants. index is a value between 0 and the number of **constant[index]**
constants set for the board.
- â returns the filename of the music that is playing on the current board. **music**
- â returns the handles of the threads on the board. index is a value between 0 and **threads[index]**
however many threads have been set.
Other Variables
- â returns or sets the ambient RGB colors. The values can range **ambientRed, ambientGreen, ambientBlue**
from -255 to 255. Alternatively, the setAmbientLevel() function can be used to set these. If it is not used, you must call forceRedraw() before the ambient color changes take affect.
- â returns the handle of a canvas which can be rendered on and off using the renderNow() **cnvRenderNow**
function.
- â returns the total game time in seconds. **gameTime**
Retrieved from " " <http://codebible.toolkitzone.com/index.php?title=Reserved_Variables>
