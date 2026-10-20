---
kind: forum-thread
id: "toolkitzone-forums/24035"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Programming"
skin: "phpbb2"
thread_id: "24035"
title: "Guess who's learning C++"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=24035"
written: "2005-10-04T03:44:00"
last_post: "2005-10-04T23:26:00"
date_confidence: "exact"
captured: ["20060111131507"]
author: "Dont_Think_So"
repliers: ["p90m16mp5a4", "TheCPPFreak220", "Colin"]
authors: ["Dont_Think_So", "p90m16mp5a4", "TheCPPFreak220", "Colin"]
posts_present: 5
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_262460_amp_3Bsid_66f7a85c64583cbb779004febec1e1c5", captured: "20060111131507", sha256: "6f744061d684e8983c41035a3b14863e03ceb54606741b7fd882300b2246bffc", wayback_url: "https://web.archive.org/web/20060111131507/http://www.toolkitzone.com/forums/viewtopic.php?p=262460&amp%3Bsid=66f7a85c64583cbb779004febec1e1c5"}
links:
  - {url: "http://www.toolkitzone.com/stuff/files/101/astar.cpp", status: "never-captured", local: null}
---

# Guess who's learning C++

### Dont_Think_So · 2005-10-04 03:44 · #B262182

Well, it's been a few years since I touched a line of C++, and I decided that I wanted to learn it again. I never really was good at it, and thought it would be best to start off with a clean slate.
So, here I am. I have understood everything (I think...) that I have read, and decided the best thing to get me going would be to write a program. This is my first real program (read: one not created because of a tutorial), and of all the possibilities I picked to program the A* Pathfinding algorithm (for those who don't know, it's used in games like Starcraft and other RTS games to find the path from one point to another, while walking around obstacles that lie in the path). Everything was moving along just dandy when, for some reason that I can't quite put my finger on, my program "encounters a problem":

**Quote:**

> astar.exe has encountered a problem and needs to close. We are sorry for the inconvenience.
>

Naturally, I wouldn't turn for your guys' help unless I absolutely couldn't figure things out for myself, and, well, here I am. I must give you warning: this code probably has "beginner" written all over it, and I probably do several unneccessary, ugly, half-arsed things throughout. But if you could, please bare with me. Smile
I didn't even get to programming the algorithm itself yet. Bah.
[The source](http://www.toolkitzone.com/stuff/files/101/astar.cpp)
example 'map' file:

**Code:**

```
     SSSS

SSS   SSS S S

SS    SSS  SS

SS SSSS   SSS

SS   SSS

SSSS    SSS

   SSSS  SS

        SSS

SSSS

```

### p90m16mp5a4 · 2005-10-04 08:49 · #B262252

I'm in no knowledge to debug your code, but, I can tell you aren't using VC++, so, I took the liberty of giving you the error messages I got.

**Quote:**

> --------------------Configuration: fs - Win32 Debug--------------------
> Compiling...
> ASAF.CPP
> c:\fs\asaf.cpp(73) : error C2039: 'strcmp' : is not a member of 'std'
> c:\fs\asaf.cpp(73) : error C2039: 'strcmp' : is not a member of 'std'
> c:\fs\asaf.cpp(85) : error C2039: 'atoi' : is not a member of 'std'
> c:\fs\asaf.cpp(85) : error C2039: 'atoi' : is not a member of 'std'
> c:\fs\asaf.cpp(85) : error C2039: 'atoi' : is not a member of 'std'
> c:\fs\asaf.cpp(85) : error C2039: 'atoi' : is not a member of 'std'
> Error executing cl.exe.
> ASAF.OBJ - 6 error(s), 0 warning(s)
>

The debugger is my friend, I never used strcmp or atoi, so I don't know if they are real or not Smile I hope this helps, or maybe my compiler isn't set up right for this program.

### TheCPPFreak220 · 2005-10-04 10:55 · #B262256

The string functions (inclusive of the converting functions as well), are in the global namespace. (Just in case you where wondering where they were, if not in the std namespace. Smile )
You compiler should have picked up on that, what one are you using?

### Colin · 2005-10-04 13:01 · #B262272

Actually, the <cstring> header is effectively this:

**Code:**

```
namespace std

{

#include <string.h>

}
```

Which means that the string functions are in the std namespace if you include them that way.
The actual bug is dereferencing a wild pointer. I don't feel like tracking it down but a good start might be fixing the various sillinesses like get() functions that return pointers. The whole point of get() functions is that you can get a value but not change it.

### Dont_Think_So · 2005-10-04 23:26 · #B262460

**Quote:**

> The string functions (inclusive of the converting functions as well), are in the global namespace. (Just in case you where wondering where they were, if not in the std namespace. Smile )
>

As Colin said, the cstring library places the string functions in the std namespace. Really, I only did that so I could get into the habit of using namespaces, which is why I didn't put "using namespace std" at the top of my program.

**Quote:**

> The actual bug is dereferencing a wild pointer. I don't feel like tracking it down but a good start might be fixing the various sillinesses like get() functions that return pointers. The whole point of get() functions is that you can get a value but not change it.
>

Thanks for the tip, I'll get on that, but is there a better way to call functions of members of a class, without returning a pointer? The way I have it set up now is:

**Code:**

```
#include <iostream>

class CMember

{

public:

     void function() { std::cout << "Hey look, a function.\n"; }

};

class CClass

{

public:

     CMember* getMember() { return &m_member; }

private:

     CMember m_member;

};

int main()

{

     CClass aclass;

     (*aclass.getMember()).function();

}
```

Which makes for very ugly pointers...
<Edit>I found the source of the problem; it appears that I can't have a 1024x1024 array of tiles. Guess I'll have to settle for something smaller - 100x100 should do. Thanks guys.
