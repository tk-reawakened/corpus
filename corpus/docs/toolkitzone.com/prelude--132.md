---
kind: doc
id: "toolkitzone.com/132"
site: "toolkitzone.com"
title: "Prelude"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=132"
written: "2005-01-02T17:48:00"
date_confidence: "exact"
updated: null
captured: ["20060206163629"]
author: "Colin"
repliers: []
authors: ["Colin"]
comments_present: 0
f_author: "Colin"
f_date: "January 2, 2005, 5:48 pm"
f_description: "Colin argues strings are something too often taken for granted in high-level programming, the details are abstracted to the point where many high-level coders don't even have the slightest clue what a string really is. Certainly an article for the more experienced programmers to ponder."
f_title: "The Evil that is Strings"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_132", captured: "20060206163629", sha256: "50b715ef0c43ea7e25a80e9d4440f21cb3e12af97e3a4aeb6c5d03a83456867d", wayback_url: "https://web.archive.org/web/20060206163629/http://www.toolkitzone.com:80/library.php?mode=read&doc=132&PHPSESSID=6c1f0d3aa43a19d10f2020f481c20c7a"}
---

# Prelude

Strings are something too often taken for granted in . The ability to store a series of numbers, letters and symbols; to add to this series, search throughout it, compare to others, even to change it. The details are abstracted to the point where many high-level coders don't even have the slightest clue what a string is. But how can this be a bad thing? Isn't the idea of abstraction that you don't have to worry about the details? If it works - it works; right? Wrong. Only by understanding the very method in which a high-level entity works can we learn to fear it. Consider the RPGCode function ; to the untrained eye, this function may seem completely harmless and without fault, but once you begin to understand its nature, you move towards friendlier program-flow constructs. As you may have guessed from its title, this article will explain exactly why . An exaggerated claim, perhaps, but, after reading this document, the fear that rattles you from the very of using a string will be justly founded. RPGCode makes strings very easy to use. To many people, this seems all well and good. However, in reality it prevents the coder from understanding what they cannot see. Consider the following RPGCode sample: Those two, innocent, lines set a string to ``Hello, world!'' and display it on the screen. It's . The problem lies in what you cannot see. The following code is the same thing in C, using macros which hide all the same details. This snippet performs a task similar to the RPGCode above. Note that the 255 sent to is the length of the string to allocate (it will be a fixed length string). simply deletes a string (similar to the RPGCode function , but mandatory). Unfortunately, C does not natively provide these macros. I have coded the macros as follows: The statement, which is fairly self-explanatory, sets the type to be a . simply invokes the standard C function and calls another standard C function. Right away we can see that many more function calls are involved that meet the eye and costs precious execution time. I've intentionally ignored . Let's take a look at it: Since this macro is blatantly convoluted, observe how allocating a string might be expanded, for clarity: The intrinsic function returns the size, in bytes, a type occupies in memory - in this case, one character. We multiply the result by 255 to calculate the size in memory of a 255 character string. Using ASCII C Strings, the result is 255 as characters occupy one byte. RPGCode, however, uses UNICODE for its strings, where every character occupies two bytes. The intrinsic function allocates a memory block and returns its address - we pass in the size calculated above to allocate a 255 character string. Here we cast the above memory address to type , defined above as a . Finally, we use standard function (also intrinsic) to copy the initial value into the string. But wait a moment! How does that function work? How does it know the length of the source string? Without knowing the length, it might (and will) copy the incorrect number of bytes to the destination string - possibly both reading writing memory incorrectly. But it doesn't, so there's obviously something else going on here. In C, every string encased in double quotes (``'') automatically has a post fixed to it so functions like know where it ends. This means, however, that functions working with strings must before they can do safely with the string. Imagine the time this takes on string operation. You might code such a null-searching function like this: This function has to walk until it locates the null terminator (`\0'). In relative terms, that takes a time (the astute reader might ask why we don't just use a memory searching function - the answer is simple; these functions can only search for a certain number of characters and the of this function is to obtain the length of a string). Keep in mind that this function will have to be called, be it directly or indirectly, by other string related function; the milliseconds add up quickly. Armed with this function, the copy function seen above is easy to implement: Note that because this function wants to copy the , we need to add one to the result of the length function - this takes yet time. Consider the following RPGCode line: This line first allocates the string ``Hello, ``. Next, it allocates the string ``world!'' and appends it to the previously allocated string. Sometime in here, the latter string is freed. Finally, the result of the appending is copied to a newly allocated string ( ) and, along with the ``Hello, `` string, is freed itself. A function used to do the appending might look somewhat like this: As you can see, this function features calls to the length function, addition! And this is if we keep ignoring how is implemented (which, fortunately, we will)! Do the huge execution costs strings bestow upon you mean that you should never use them? Of course not, but you should use them and , especially when a better alternative exists. Consider this script: Code similar to this is not a rare sight. Unfortunately for the creator, the above code is . There is absolutely no logical reason to use strings for this task! The recently released version 3.05 provides grounds for a very nice alternative: Simply using constants preserves all the pros of the above code, namely having logical labels for the directions, but loses the outrageous overhead of using strings. High-level languages make performing tasking like string manipulation amazingly easy - but at what cost? Because they cannot see how something is implemented, people assume it can be used without contemplation of its cost. Unfortunately, this is not true, and using features like strings for tasks that can be done without wastes valuable execution time. Always consider the low-level costs of an entity before you use it - If something sounds too good to be fast (or even if it doesn't), it likely is. Hopefully, I'll see you all again next week.
TK3 Amelioration VII The Evil that is Strings
**Prelude****
branch *strings are evil* *thought*
**Allocation****
str$ = "Hello, world!" text(1, 1, str$)
*painfully easy*
STRING str = STRING_ALLOC(255, "Hello, world!\n"); STRING_PRINT(str); STRING_FREE(str);
STRING_ALLOC STRING_FREE kill()
typedef char *STRING; #define STRING_FREE(x) free(x) #define STRING_PRINT(x) printf("%s", x)
typedef STRING *pointer to data of type* *char* STRING_FREE free STRING_PRINT *every single call* STRING_ALLOC
#define STRING_ALLOC(x, y) (strcpy((( STRING )malloc(sizeof(char) * x)), y))
*greatly*
const size_t size = sizeof(char) * 255;
sizeof(
const void *pMem = malloc(size);
malloc()
STRING str = (STRING)pMem;
STRING *pointer to characters*
strcpy(str, "Hello, world!\n");
strcpy() *and*
**Null Termination****
NULL strcpy() *locate the* *NULL* *anything* *alone* *every*
size_t strlen(const STRING str) { size_t i = 0;
while (str[++i] != '\0'); return i; }
*every character* *long* *point* *every* *very*
STRING strcpy(STRING strDest, const STRING strSource) { return memcpy(strDest, strSource, strlen(strSource) + 1); }
*including* NULL *also* *more*
str$ = "Hello, " + "world!"
str$
STRING strcat(STRING strDest, const STRING strSource) { return memcpy(strDest + strlen(strDest), strSource, strlen(strSource) + 1); }
*two* *and* memcpy()
**Alternatives**
*sparingly* *with great care*
method moveDirection(dir$) { // Note that comparisons take extra time, yet again! switch (dir$) { case ("N") g_y!-- case ("E") g_x!++ case ("W") g_x!-- case ("S") g_y!++ } }
*garbage*
#global DIR_N! 1 #global DIR_E! 2 #global DIR_W! 3 #global DIR_S! 4 method moveDirection(dir!) { switch (dir!) { case (DIR_N!) g_y!-- case (DIR_E!) g_x!++ case (DIR_W!) g_x!-- case (DI
_S!) g_y!++ } }
**Conclusion**
Levi
January 3, 2005, 12:21 am
Again you show an interesting view on the way people program. I agree with what you say, I basically have no choice. Though I still wouldn't call them evil. Just necessary only when relating user friendly messages, and facts to the user.
Talyn
January 3, 2005, 4:52 am
Very interesting. It's true, I've never worried about strings before, but now I'm going to try and avoid them as you suggest.
**Column**
Toolkit 3.x > TK3 Amelioration
Colin argues strings are something too often taken for granted in high-level programming, the details are abstracted to the point where many high-level coders don't even have the slightest clue what a string really is. Certainly an article for the more experienced programmers to ponder.
**Past Columns**
Feb 28, '05
Feb 13, '05
Feb 7, '05
Jan 30, '05
Jan 16, '05
Feb 28, '05
Feb 13, '05
Feb 7, '05
Jan 30, '05
Jan 16, '05
