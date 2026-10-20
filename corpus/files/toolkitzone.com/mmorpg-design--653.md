---
kind: file
id: "toolkitzone.com/653"
site: "toolkitzone.com"
title: "MMORPG Design"
original_url: "http://www.toolkitzone.com/fileman.php?id=10&file=653"
written: null
date_confidence: "unknown"
updated: null
captured: ["20041106165254", "20041106165501", "20060304162121"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_653", captured: "20041106165254", sha256: "3bb0ce4ad42161724eeda94f4a5c20a081ce7bbed17fd3fe2805e98986982504", wayback_url: "https://web.archive.org/web/20041106165254/http://www.toolkitzone.com/fileman.php?id=10&file=653"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_5_file_653", captured: "20041106165501", sha256: "f5a86d7614ffaebf50ca7cf50ea8fc7ef49da3ea983afa6305471b6d62c6c042", wayback_url: "https://web.archive.org/web/20041106165501/http://www.toolkitzone.com/fileman.php?id=5&file=653"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_653", captured: "20060304162121", sha256: "ccebc1313f161f3721221a73b5ca2dde864908f4855ec025815124bddc6e5f11", wayback_url: "https://web.archive.org/web/20060304162121/http://www.toolkitzone.com/fileman.php?id=3&file=653"}
---

# MMORPG Design

```
MMORPG Design
Part 1
Basically, you have to realize that the internet is slow. You also have to realize that we all don't have dual-processor Mac G5's. So to make up for this, you need to have a server that will handle all of this for you.
Currently, I am finishing the development of such a server which I will distribute for free later on, but here is how it works:
The game structure is divided into a grid. TK makes it easy because it allows you to make different map areas. This is perfect. Name all of your maps with a 'signature'. This signature consists of a decimal. To generate this signature, think of what cell the map would be in if it were contained in a grid. For example, if it would be 1, 1 then the signature would be 1.1, or if it were 31, 46 then the signature would be 31.46 .
Now that each map has a signature, you need to develop the server. Make an array for each signature. Then create a command such as "%m ##,##" where each # represents a number in the signature the array represents. This command will be sent by the client when he/she moves into a new area. For example, a user in area 12.54 moving into 12.55 would send "%m 12,55" to the server. Have the server recognize this, and take the user's name off the array for 12.54 and move them to the array for 12.55 .
Next, have the server have a 'mail' feature. This will deliver all re-location information for a specific signature. This is the feature that really speeds things up. When a user sends something like "%s 12,55::24,20"
Let's break that down:
%s
Declares that we are sending information
12,55
States the signature of the users to send the mail to
Specifies the user's name so that the correct avatar is moved.
24,20
Moves the avatar to tile 24,20
Now because we have maps and signatures, the client is not slowed down from monitoring all user positions in the game. The server manages this, and even then, in a basic pattern, leaving behind a minimal footprint (compared to what we normally expect).
Building upon this concept, you may develop interesting new ideas such as multi-player battling through internet team effort (I know it has already been made....). If I get around to it, the next part will talk about designing a user login system.
bastawhiz
```
