---
kind: page
id: "codebible.toolkitzone.com/codebible.toolkitzone.com/index.php?title=Program_Flow"
site: "codebible.toolkitzone.com"
title: "This article is a incomplete. You can help Code Bible by . expanding it"
original_url: "http://codebible.toolkitzone.com/index.php?title=Program_Flow"
written: null
date_confidence: "unknown"
updated: null
captured: ["20100621051439"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/codebible.toolkitzone.com/index.php__title_Program_Flow", captured: "20100621051439", sha256: "88bd80e2dc9b099e6284b795177a7003acb4454296a88a736aa4e35cbea0347f", wayback_url: "https://web.archive.org/web/20100621051439/http://codebible.toolkitzone.com/index.php?title=Program_Flow"}
---

# This article is a incomplete. You can help Code Bible by . expanding it

Program Flow
*This article is a incomplete. You can help Code Bible by . [expanding it](http://codebible.toolkitzone.com/index.php?title=Program_Flow&action=edit)*
What is program flow?
Program flow is simply the order in which your code gets executed. By default the code you write will be evaluated from top to bottom, one line at a time. There are times that you're going to need to manipulate the way your code gets run, and several statements exist in RPG Code to do this.
Program Flow Statements
if (condition) { //Code }
You will use If to branch over code when the condition evaluates to false.
Sample Code:
```
if (gotKey ~= true) {
mWin("Here, take this key");
giveItem("key.itm");
gotKey = true;
} else {
mWin("You already received the key from me!");
}
```
for (initial; condition; increment) { //Code }
A for loop has you initialize a variable, and it will loop as long as the condition evaluates to true. At the end of each loop it will perform the statement defined in increment.
Sample Code:
```
mWin("Let's count to 10!");
for (i = 1; i <= 10; i++) {
mWin(i);
}
```
In this advanced example, you can use the for loop parameters to execute code in a class containing a list of objects. The class portrayed here is a classic example of how you might code a list.
Advanced Example:
```
for (itm = obj->reset(); !obj->atEnd(); itm = obj->next()) {
mWin("This item is " + itm->getName());
}
```
while (condition) { //Code }
In a while loop your code is looped as long as the condition evaluates to true.
Sample Code:
```
mWin("You can't leave until you hit ENTER");
while (get() ~= "ENTER") {
// You're trapped here until get() is "ENTER"
}
```
until (condition) { //Code }
Similar to a While loop only it will repeat the code until the condition evaluates to true.
Sample Code:
```
answer = false;
until (answer) {
mWin("Can I have a dollar?");
key = wait();
if (key == "Y") {
answer = true;
}
}
```
Retrieved from " " <http://codebible.toolkitzone.com/index.php?title=Program_Flow>
