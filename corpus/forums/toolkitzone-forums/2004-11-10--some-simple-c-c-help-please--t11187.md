---
kind: forum-thread
id: "toolkitzone-forums/11187"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "11187"
title: "Some simple C/C++ help please..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11187"
written: "2004-11-10T03:19:00"
last_post: "2004-11-20T03:26:00"
date_confidence: "exact"
captured: ["20041226222827"]
author: "Grant"
repliers: ["Colin", "Ersuis", "Levi", "khin", "marcos"]
authors: ["Grant", "Colin", "Ersuis", "Levi", "khin", "marcos"]
posts_present: 13
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_127455_amp_", captured: "20041226222827", sha256: "2c3ef85fb5dd6435d9a376a8aec62adf6d96e2f70b8e3c1a52d9fa9e74de9342", wayback_url: "https://web.archive.org/web/20041226222827/http://www.toolkitzone.com:80/forums/viewtopic.php?p=127455&amp"}
links: []
---

# Some simple C/C++ help please...

### Grant · 2004-11-10 03:19 · #B123302

Among my many projects of learning Portuguese and Polish I have decided to try and learn C and C++. Ive tried before and every time I try I get a little further so I hope someone can help me now on this. I am looking for a command in C that is similar to the #branch command in the toolkit or the #run command. I think I realize because Ive been using Sphere lately (I know I know) that you have one main program and it latches off other files you created? I dont know well I am using Dev C++ and I have been having trouble with the For command. I figure it can be used in a similar fashion to #branch.
What is wrong with this it wont run it says there are errors?

**Quote:**

> #include <stdio.h>
> #include <stdlib.h>
> int main()
> {
> int a, b;
> for ( a < 5, a > 5, )
> {
> cout<< "\ [1] Press one to stay.\n";
> cout<< "\ [2] Press two to leave.\n";
> cout<< "\ \n";
> cin>>b;
> if(b==1)
> {
> cout<< "\ Okay you stay... \n";
> system("PAUSE");
> }
> if(b==2)
> {
> a=6;
> cout<< "\Later bye.\n";
> system("PAUSE");
> }
> }
> return 0;
> }

### Colin · 2004-11-10 03:30 · #B123307

for looks like this:
for (type var = initial value; boolean; increment)
/* stuff */ ;
typically like this:

**Code:**

```
for (int idx = 1; idx <= 10; idx++)

   /* stuff with idx */ ;
```

With regards to branching around -- it is EVIL and should be used only when REQUIRED (jumping to display an error message is common). That said, the functionality is achieved like this:

**Code:**

```
goto myPlace;

/* stuff that will not run */

myPlace:

/* stuff that will run */
```

DO NOT USE THIS for casual purposes... there is ALMOST ALWAYS a better way!!! Razz
Also, try this to avoid the message on pause:

**Code:**

```
system("pause > nul");
```

Hope that helps.

### Grant · 2004-11-10 03:35 · #B123311

Yes that really does help, what I had in mind with "for" was to have a starting screen then to go back to the starting screen from somewhere else I'd just make the int = 1 so it goes back to the top. I see what I was doing wrong now, but do I have to have an increment?

**Quote:**

> #include <stdio.h>
> #include <stdlib.h>
> int main()
> {
> int a, b;
> for (int a = 1; a <= 10; a++)
> {
> cout<< "\ [1] Press one to stay.\n";
> cout<< "\ [2] Press two to leave.\n";
> cout<< "\ \n";
> cin>>b;
> if(b==1)
> {
> cout<< "\ Okay you stay... \n";
> a=1;
> system("pause > nul");
> }
> if(b==2)
> {
> a=6;
> cout<< "\Later bye.\n";
> system("pause > nul");
> }
> }
> return 0;
> }
>

Here are the errors it says there are and they make very little sense and I have no idea how to fix them:

**Quote:**

> Line 6: 'for' loop initial declaration used outside C99 mode
> Line 9" 'Cout' undeclared (first use in this fuction)
> Line 12: 'Cin' undeclared (first use in this function)

### Ersuis · 2004-11-10 03:52 · #B123319

To use cout and cin, you have to include iostream, like so:
#include <iostream>
Then, to use it like you're trying to use it, you'll have to add 'using namespace std;' at the top of your program.
I've never seen that first error before, though; make sure you're saving your source files as .cc or .cpp, as opposed to .c. That error almost looks like it's trying to compile your C++ program as a C program, which you just can't usually do.
Why are you escaping the beginning of your strings in your cout statements? It's not something that needs to be done.

### Colin · 2004-11-10 04:25 · #B123331

It could be because some compilers don't like the var for for loops to be declared elsewhere - so I've heard, at least - VC++ is all I ever use and it doesn't care, though.

### Levi · 2004-11-10 04:50 · #B123336

Hmmmm....Which version of Dev-C++ are you using? Because I've encountered a few odd problems with the v5 betas. That's why I use Dev-C++ 4. Actually now that I have VC++ I use that but when I'm helping with Dev I use Dev.
Yeah other than the escaping before the text in your cout statements I never got any errors. It works fine. Though the fact that it is programmed as an infinite loop is a bit irritating.
Unlike with VC++ Dev-C++ does not require the use of "Using NameSpace std;"
But yeah, if you want to exit out of this loop the way you currently have it if the enter two, just set a = 10. That is as soon as you get the for loop working.

### Colin · 2004-11-10 04:52 · #B123337

Of course you need the "using". You're probably just confused like I once was; let me explain:
iostream.h - this file harbours the now obsolete stream classes which are in the global namepace
iostream - this file harbours the more correct stream classes which are in the std namespace.
For the record, it's:
"using namespace std;"
(case does matter)

### Levi · 2004-11-10 05:19 · #B123341

Yes case does matter, but not the forums unless they plan on simply copying and pasting. Or if you just want to be as correct as possible 24/7. Either way.
But Dev-C++ uses a different compiler for C++ development, that was made differently. Now I'm not sure why it doesn't require using the "using namespace std;" maybe because they made it use that as a standard addition. Something the compiler assumes you'll be using. Rather inconvenient at times, but still. Dev-C++ doesn't need to have it called. I know, I use it. You don't.
It won't harm the compiler to call it however. And it is good practice to do so when using the iostream, I agree. That's what I was taught in my C++ class which used VC++.

### Colin · 2004-11-10 22:37 · #B123562

No, std:: is a much better practice. If you use "using" you defeat the whole purpose of namespaces Razz

### Levi · 2004-11-10 23:48 · #B123610

True, I'm just lazy. Man having to type std:: before every cout and cin and every other statment that needs it. Man that can get annoying. Smile
But yeah short-cut is using, better way just add std::. Up to you really.

### khin · 2004-11-11 11:01 · #B123847

You get errors because:
you declared two int a
the variable you declare inside a for() loop initialisation does not become a local variable inside that loop. In your case, that a inside the for loop was recognized as part of the main() function. Therefore you have duplicate declarations for the same variable. Remove the one on the for() loop, or the one before it.
To use cout and cin, you must include the header file iostream.h. The other folks have already helped you well on this Smile
Remove that backspace character "\" on the beginning of all your strings. It's an escape sequence and will cause your program to behave undesirably. If you want a backspace character to be displayed, use double backspace (\\).

### Colin · 2004-11-11 16:46 · #B123903

You want to include iostream. No .h. The .h one is obsolete in VC++ 7 and higher.

### marcos · 2004-11-20 03:26 · #B127455

**Grant wrote:**

> Among my many projects of learning Portuguese and Polish...
>

Por que você quer aprender Português?
(Why do you want to learn Portuguese?)
Pergunte-me se você tiver dúvidas.
(Ask me if you have questions.)
