---
kind: forum-thread
id: "toolkitzone-forums/11107"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "11107"
title: "Curses Library"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11107"
written: "2004-11-07T21:09:00"
last_post: "2004-11-09T09:52:00"
date_confidence: "exact"
captured: ["20041226222553"]
author: "Ersuis"
repliers: ["khin"]
authors: ["Ersuis", "khin"]
posts_present: 2
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_123065_amp_", captured: "20041226222553", sha256: "a679486d5ce6169c026984628ec160cf25b7e37b40d97642796e8c5a5dc24ed8", wayback_url: "https://web.archive.org/web/20041226222553/http://www.toolkitzone.com/forums/viewtopic.php?p=123065&amp="}
links:
  - {url: "http://users.bignet.net/~snoopy37/files/CursesLib.tar.gz", status: "external", local: null}
---

# Curses Library

### Ersuis · 2004-11-07 21:09 · #B122449

In preparation for a rogue-like game I want to start writing someday (hehe), I've been writing my own wrapper for curses implementations, like pdcurses or ncurses. Curses, if you're not familiar, is basically a library to output text to the screen where you need it and capture input.
I've wrote this library basically to make curses a little less C-style and a little more C++ style. The output and input is done through objects and streams. I like using it, at least. It might be a little helpful to some of the console coders here, too.
It's missing a few things, like windows and the ability to redefine colors, but enough of it is there that somebody could use it effectively. If you've been struggling with using color or positioning text in your console programs, you might want to check it out.
CursesLib: <http://users.bignet.net/~snoopy37/files/CursesLib.tar.gz>
My documentation is kinda spotty, so if you have any questions, ask me here, email me at (redacted: email) or (redacted: email), or MSN instant messenger me at my hotmail.
I'm not sure if the Windows compilers (which most of you use) will have a curses library included with them. If you're getting errors in your includes, try downloading PDCurses (Google it) and installing it. You'll have to also make sure you compile CursesLib.cpp with your project. The library uses operator overloading and namespaces, so those of you with ancient compilers might not be able to make use of this (MinGW [Dev C++'s default compiler] and VC++ should be fine).
Here's some sample code using it:

**Code:**

```
#include "CursesLib.h"

using namespace Curses;

int main()

{

  Display screen;

  Input input(CBreakMode, echoOff, true);

  int width, height;

  screen.GetSize(width, height);

  screen << "The screen is " << width << " characters wide and " << height << " characters high.";

  screen << Move(0, 5) << "Please type a character.";

  char ch;

  input >> ch;

  screen.CreateColorPair(1, red, black);

  screen.ColorPairOn(1);

  screen << Move(0, 6) << AttributeOn(bold) << "You typed: " << ch << AttributeOff(bold);

  screen.ColorPairOff(1);

  input.GetCh();

  return 0;

}
```

There's an explanation in my documentation, but you could probably figure out how it works.

### khin · 2004-11-09 09:52 · #B123065

hey what's a "rogue"?..i know that word differently..
