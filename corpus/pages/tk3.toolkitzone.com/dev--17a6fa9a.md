---
kind: page
id: "tk3.toolkitzone.com/tk3.toolkitzone.com/dev/?page=code"
site: "tk3.toolkitzone.com"
title: "Coding Guidelines"
original_url: "http://tk3.toolkitzone.com/dev/?page=code"
written: null
date_confidence: "unknown"
updated: null
captured: ["20060207132740", "20070519231920"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/tk3.toolkitzone.com/dev__page_code_amp_3BPHPSESSID_427b61816e37ab356a274a9ce28879da", captured: "20060207132740", sha256: "50b9a53c718fe84beed87224425e3e696d5d17bff7801d5e1b4af74cd6dc81c5", wayback_url: "https://web.archive.org/web/20060207132740/http://tk3.toolkitzone.com/dev/?page=code&amp%3BPHPSESSID=427b61816e37ab356a274a9ce28879da"}
  - {path: "wayback/toolkitzone.com/tk3.toolkitzone.com/dev__page_code", captured: "20070519231920", sha256: "2c766c0441e4506fc1af8b4a56295cf8e715f01fdf462f3d684d7996c60339e6", wayback_url: "https://web.archive.org/web/20070519231920/http://tk3.toolkitzone.com/dev/?page=code"}
---

# Coding Guidelines

Language specifics:
Table of Contents
1. Hypocrisy
Because the RPGToolkit has been in development for years—many of which it was not open source, large portions of the source do not follow the rules entailed within this document. These portions should be brought into the loop only when convenient, and when doing so does not have adverse cascading effects (i.e., changing a name in Visual Basic is safe because the IDE will ensure that all references are also changed).
Although such hypocrisy is detrimental to the consistency of the sources, we feel the hassle to manually modify them when irrelevant outweighs the benefits. Changing an identifier's name in C, for example, would require every location that references that name to be manually brought up-to-date. This is a predicament in which nothing but new problems and conflicts can arise. Avoid it. We believe that in time the source will evolve to being completely in agreement with this standard.
2. Common Principles
Regardless of the language a particular segment of code is being authored in, a set of common principles should be applied to its formation. Such principles allow this standard to be extended even to languages which is does not explicitly detail. This is the true mark of consistency, and the setup which we desire.
2.1. General Elegance
When writing, write correctly the first time. Do not commit a mess, and then return later to correct it. Such demeanour is key to keeping the project organized and terse. The clauses within this section take only moments to follow, and result in largely more readable code. Do not be lazy when it could hurt the project; sacrifice a little.
Indentation
In this project, we will be indenting with tabs. A new trend seems to be emerging (especially in VB) to not indent within functions. We do not want to do this.
```
extern "C"
{
int func(void)
{
int x = 0;
if (x == 0)
{
for (unsigned int i = 0; i < 90; i++)
{
x++;
}
}
if (x == 99)
{
x++;
}
return x;
}
}
```
Put Spaces Between Tokens
Code typed without spaces between tokens is considered bad programming practice; it may save all of three seconds, but in the process, it creates completely unreadable, and unmaintainable code. Note that we do not place spaces before or after curly braces or parenthesis. In the following examples, the first line is wrong, and the next line is a corrected version.
```
for(int i=0;i<5;i++);
for (int i = 0; i < 5; i++);
func(x+1,func(y+1));
func(x + 1, func(y + 1));
int x[]={1,2,3};
int x[] = {1, 2, 3};
```
2.2. Naming
For this project, the majority of identifiers will use interCaps (unless they have their own guidelines). You should not deviate from this convention. Fine points:
- The first letter is lowercase; the first letter of new words is capital
- Do not capitalize acronyms or abbreviations ( , not ) drawCnv drawCNV
Type warts (e.g., dwVar) are permitted only in files that deal intrinsically with Windows.
Constants and Types
Constants and types should be named in ALL CAPITALS, with underscores between words. Examples:
```
BOARD
VERY_LONG_NONEXISTENT_CONSTANT
```
Variables specified with the C++ const keyword are, for the purposes of this document, normal variables, and should not be named as definitions.
Enumerations
Enums are like constants, but with a two letter prefix (plus an underscore) representative of the enumeration's name on each member.
```
enum GAME_STATE
{
GS_IDLE,
GS_PAUSE,
GS_MOVEMENT
};
```
Classes
The first letter in a class name should be a capital 'C'. The next letter should also be capital, as with the first letter of new words. Examples:
```
CFile
CLongNonexistentClass
```
Class members should be prefixed with a 'm_'. Examples:
```
m_dataType
m_state
```
Globals
To distinguish globals from other variables, prefix them with a 'g_'. Examples:
```
g_gameState
g_hMainWnd
```
2.3. Variables
Use variables in moderation, especially globals. Globals are evil, and should be avoided unless a good reason exists to do otherwise.
Variable Size
Because 99% of the developers and users of this software are on 32-bit architectures, we will be using exclusively 32-bit variables unless there is a compelling reason to do otherwise. Examples:
```
Dim i As Long
unsigned int i = 0;
```
2.4. Encapsulation
Functions, modules, and classes especially should be very well encapsulated. Each should keep within itself as much as possible, and as few globals as possible should be accessed. Do not tightly connect files, especially if they are unrelated.
3.5. Commenting
In this project, we do indeed want to comment. All comments should be complete sentences including a period.
- Include a space after one-line comment indicators (e.g., ', //)
- If using the C style multiline comment, include a * at the left of new lines that lines up with the one in the comment opener.
Try to document extensively enough that anyone could grasp your code after only reading its comments, but avoid documenting trivialities (e.g., 'add 1 to i'). Additionally, every function, struct, class, etc. should be preceded by a header which provides enough information to use it without actually looking over its source.
```
/*
* Open a file into memory.
*
* fileName (in) - file to open.
* return (out) - handle to file.
*/
FILE_HANDLE openFile(const std::string fileName);
```
Structures, enumerations, and classes should state the meaning of each of their members with single line comments.
```
/*
* An enum that does something.
*/
enum SOME_ENUM
{
SE_SOMETHING, // Makes something happen.
SE_ELSE // Makes something else happen.
};
```
When many blocks close at a common location, or if they span a great enough distance to not see both the opening and closing construct at once, comment the ending construct.
```
End If ' if (bLongBlock)
Loop ' Do While (True)
End Sub ' Public Sub longSub()
```
3. Visual Basic 6
The editor, among other things, is written in Visual Basic 6 (VB6). VB is a language which is practically designed for the lazy coder; do not fall into this trap.
3.1. Keyword Omission
Do not omit optional keywords, such as redundant scope specifiers. The following examples show first wrong then the corrected way:
```
Sub func(x As Long)
Public Sub func(ByRef x As Long)
Const SOME_CONST = 3
Private Const SOME_CONST = 3
```
3.2. GoTo and GoSub
It is universally accepted that these are forbidden constructs—don't use them! They can create so-called spaghetti coding that is impossible to follow or maintain.
3.3. Syntax
While...Wend
Don't use this. Instead, use Do While...Loop.
Type Definition Characters
Don't use them.
Brackets
Include optional brackets on language constructs. The following examples show first wrong then the corrected way:
```
If x = 3 Then
If (x = 3) Then
Do While True
Do While (True)
```
3.4. Strings
Strings in VB6 are something of a modern day evil. To help decrease the lasting effect they have on our code, use them as indicated here.
Checking for Emptiness
Use . This is the fastest method for testing whether a string is empty. LenB()
```
If (LenB(str) = 0) Then
' String is empty.
End If
If (LenB(str)) Then
' String is not empty.
End If
```
Case Insensitive Comparison
Use (or , it doesn't really matter). Don't dream of using something evil like . UCase$() LCase$() Option Compare Text
```
If (UCase$(x) = UCase$(y)) Then
' They're equal.
End If
```
Clearing
Set them to , rather than "". vbNullString
```
str = vbNullString
```
Don't, however, be tempted to compare to . See above. vbNullString
Pass ByRef
Passing strings is slow. Don't do it. ByVal
Manipulation
Use only the real string functions (that is, ones with a $ at the end). Also, use the binary ( , , etc.) versions of functions unless you have a compelling reason to do otherwise. MidB$ LeftB$
4. C++
The engine and the editor's runtime library, among other things, are written in C++. C and C++ are great, highly flexible, simple languages. Unfortunately, their simplicity paves the way for sloppy, unorganized code. Just because you can do something doesn't mean you should do something.
4.1. Style
C is a language renowned for its elegance; let's use it like it was made to be used.
Curly Braces on the Next Line
Always place curly braces on the next line; this helps maintain consistency in the project. Do not place them at the end of the first line—this makes it harder to match opening and closing braces. Also, the braces should be intended to the depth of their respective constructs.
```
if (x == 0)
{
}
```
Don't Omit Curly Braces
While the C compiler will never know whether you've included an optional curly brace, we will. Omitting them makes code completely impossible for other people to work on. Don't do it.
```
if (x == 0)
{
justOneThing();
}
```
The exception to this rule is if the construct is all on one line. In that case, never include the braces.
```
if (x == 0) justOneThing();
```
Use C++ Casts
C++ provides much nicer casts than C. Use them. The following lines show wrong then right:
```
const int x = (double)y;
const int x = double(y);
const int *x = (int *)y;
const int *x = reinterpret_cast(y);
```
Avoid Dangerous Things
Use std::string, not pointers to character arrays. In fact, don't use arrays at all. The general rule is thus:
Use pointers when you ; use alternatives when you . **must** **can**
Empty Parameter Brackets
If a function contains empty parameter brackets, the intent of the author is ambiguous. Traditionally, empty brackets mean that a function takes unlimited parameters, but it is more likely that no parameters was what was meant. To rectify this, always put something within the parameter brackets.
If unlimited parameters were meant, use the ellipsis:
```
void func(...);
```
If no parameters were meant, use the keyword: void
```
void func(void);
```
Structs
Create structs using standard C tag, typedef style. Define a pointer to the struct prefixed with LP (no underscore), if required.
```
typedef struct tagSomeStruct
{
int someMember; // Some member.
int anotherMember; // Another member.
} SOME_STRUCT, *LPSOME_STRUCT;
```
4.2. Always Initialize
No variable should lack a default value, even if it's to be set one line later. Always, always initialize.
4.3. Be Const Correct
Being Const Correct, for the uninitiated, is using the C++ const keyword in all the correct places. Structure your code so that variables need not be changed, and make them const. Likewise, absolutely all parameters should be const.
4.4. Protect Headers
All header files should be protected with ... .. . Do not use . VC++ may support it, but it is obsolete. #ifndef #define #endif #pragma once
```
#ifndef _HEADER_NAME_H_
#define _HEADER_NAME_H_
/*
* Content here.
*/
#endif
```
should be a unique name for each header file. HEADER_NAME
