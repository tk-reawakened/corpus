---
kind: forum-thread
id: "toolkitzone-forums/25808"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Programming"
skin: "phpbb2"
thread_id: "25808"
title: "Question about my C code"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=25808"
written: "2005-12-16T14:37:00"
last_post: "2005-12-16T21:59:00"
date_confidence: "exact"
captured: ["20051230034148"]
author: "Ross L."
repliers: ["Marc", "Notsosuperhero"]
authors: ["Ross L.", "Marc", "Notsosuperhero"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_279995_amp_3Bsid_5328a2466eba999e8fe7a001f925d625", captured: "20051230034148", sha256: "6cffc2c63e737a659092fe23970526a796084d564fd48b7ce75d0e689b78b96b", wayback_url: "https://web.archive.org/web/20051230034148/http://toolkitzone.com/forums/viewtopic.php?p=279995&amp%3Bsid=5328a2466eba999e8fe7a001f925d625"}
links: []
---

# Question about my C code

### Ross L. · 2005-12-16 14:37 · #B279919

**Code:**

```
#include <stdio.h>

main ()

{

     int c, i, nwhite, nother;

     int ndigit[10];

     nwhite = nother = 0;

     for (i = 0; i < 10; ++i)

         ndigit[i] = 0;

     while ((c = getchar()) !=EOF)

           if (c >= '0' && c <= '9')

              ++ndigit[c-'0'];

           else if (c == ' ' || c == '\n' || c == '\t')

                ++nwhite;

           else

               ++nother;

     printf ("digits =");

     for (i = 0; i <20; ++i)

         printf(" %d", ndigit[i]);

     printf(", white space = %d, other = %d\n",

               nwhite, nother);

}
```

I am under the impression that I should be getting some kind of output after inputing data and it's not happening. Any ideas?

### Marc · 2005-12-16 20:31 · #B279978

Sorta like displaying the charactor on the screen? Like after you type it?
If so, getch() is not the function. sprintf() probably is..
If somthing else, tell me..

### Notsosuperhero · 2005-12-16 21:59 · #B279995

getch() just waits for a key to be pressed. sprintf() is to put text in a buffer. If you want to display text on the screen you want printf().
EDIT: If you want to print out the character that was pressed use getche().

**Code:**

```
int ch = getch();
```

Will not output anything

**Code:**

```
int ch = getche();
```

will print out the character pressed.
