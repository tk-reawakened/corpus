---
kind: doc
id: "toolkitzone.com/80"
site: "toolkitzone.com"
title: "Function definition of drawMenu()"
original_url: "http://toolkitzone.com/library.php?mode=read&doc=80"
written: "2004-12-14T17:34:00"
date_confidence: "exact"
updated: null
captured: ["20060325172303"]
author: "Khin"
repliers: []
authors: ["Khin"]
comments_present: 0
f_author: "Khin"
f_date: "December 14, 2004, 5:34 pm"
f_description: "Khin furthers the Turbo C++ tutorial from two weeks ago that looked at creating a menu system, and this time it's all about adding one those little extras we all take for granted, highlight selection."
f_section: "Creativity > Khin's Desk"
f_title: "Menu with Highlight Selection"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_80", captured: "20060325172303", sha256: "5309c55b74a48e6c7cb232ffb6ed6ba23a3868a5c9ed89b5b5ace49c60b87488", wayback_url: "https://web.archive.org/web/20060325172303/http://toolkitzone.com:80/library.php?mode=read&doc=80&PHPSESSID=bdcceeefceef8ff863ad82d0d089ece4"}
---

# Function definition of drawMenu()

Menu with Highlight Selection
In our tutorial , you have been introduced to the basics of menu making. These basics are essential everytime you make a menu. [Creating a Basic Menu Program](http://toolkitzone.com/library.php?mode=read&doc=63)
Assuming you have read the previous tutorial, or you have prior knowledge regarding programming basic text-based menus, let's start building a more eye-friendly one.Instead of asking users to type in the letter or number of choice, we could just build a menu so that it highlights the choices given. This being put into mind, we should familiarize ourselves with colors...basic DOS colors.The basic DOS colors are the 15 colors ranging from black to white. Here is the complete listing of the standard DOS palette:
COLORS (text mode)
Constant
Value
Background?
Foreground?
Sample
BLACK
YES
YES
BLUE
YES
YES
GREEN
YES
YES
CYAN
YES
YES
RED
YES
YES
MAGENTA
YES
YES
BROWN
YES
YES
LIGHTGRAY
YES
YES
DARKGRAY
YES
LIGHTBLUE
YES
LIGHTGREEN
YES
LIGHTCYAN
YES
LIGHTRED
YES
LIGHTMAGENTA
YES
YELLOW
YES
WHITE
YES
These are the colors we can use in our program. Using your own common sense, you should be able to visualize what the colors look like.Anyway, let us start building the menu.
Let's make a function that will display a menu. First off, the prototype:
int drawMenu(void);
This function is meant to return a value to the calling program. It should return the index of the highlighted option. Basing on my design, the lowest value is 1, and the highest is n-1, where n is the number of options. Alright, let's define the function:
**Function definition of drawMenu()**
int drawMenu(void){ int choicePtr=0; char charVal='*'; window(1,1,80,25); textbackground(BLACK); textcolor(BLACK); clrscr(); textcolor(YELLOW); textbackground(BLUE); window(10,2,30,10); clrscr(); gotoxy(1,1); cprintf(" -----===MENU==-----"); cprintf("\r\n"); charVal=' '; if(choicePtr==0){ textcolor(LIGHTGREEN); charVal='*'; } else textcolor(WHITE); cprintf("\r\n [%c]Choice 1",charVal); charVal=' '; if(choicePtr==1){ textcolor(LIGHTGREEN); charVal='*'; } else textcolor(WHITE); cprintf("\r\n [%c]Choice 2",charVal); charVal=' '; if(choicePtr==2){ textcolor(LIGHTGREEN); charVal='*'; } else textcolor(WHITE); cprintf("\r\n [%c]Choice 3",charVal); }
//Holds the value of the selected choice
/*Depending on the value of choicePtr, this text may or may not come out as LIGHTGREEN, also, there may be an asterisk(*) somewhere between the '[' and the ']', as contained within charVal.*/
/*Depending on the value of choicePtr, this text may or may not come out as LIGHTGREEN, also, there may be an asterisk(*) somewhere between the '[' and the ']', as contained within charVal.*/
/*Depending on the value of choicePtr, this text may or may not come out as LIGHTGREEN, also, there may be an asterisk(*) somewhere between the '[' and the ']', as contained within charVal.*/
The function isn't fully done yet. What do you think is missing? If you are following through you'll notice that there's no way of changing the value of . The text colors depend on it and yet, it wouldn't be changed. Besides, where's the loop and switch statements found in most menu programs?Before we add the switch statements, picture this: if you are to test for the value that the user entered, to what values are you going to test it? On our previous tutorial, we tested the buffer variable to the values like 1,2,3,etc.., or to 'a','b','c', etc. That's because those inputs are what we expect from the user. This time however, what inputs are you expecting from the user? Methinks it's the Arrow Keys and ENTER, or ESCAPE. *choicePtr*
One problem now comes to mind: how are we going to detect whether the user pressed UP, DOWN, LEFT, RIGHT, etc? They are definitely not characters nor any integer value. If you look up into the ASCII table, they're not there--so how do we test for their values?Luckily, you can create a program that will ask for a character and prints it, in character format(using the getche() can accomplish this). If you press the UP key, some sort of character should be displayed on the screen...that's the character equivalent of the UP key.However, we are not going to use that method. Observe this:
#define UP 0x048 #define DOWN 0x050 #define LEFT 0x04b #define RIGHT 0x04d #define ESC 27 #define ENTER '\r'
I assume you are familiar with the #define directive. If not, go read a book for beginners. The #define directive declares constants, meaning unchangeable values/variables. Technically I couldn't call them variables because the term variable is applicable to identifiers whose contents vary depending on the program. The identifiers UP, DOWN, LEFT, RIGHT, ESC, and ENTER contain values that could never be changed. The values they contain are the character, integral, or hexadecimal values next to each. For example, the identifier UP contains the hexadecimal value of 0x048. The compiler will substitute this value for every instance of the identifier UP it may find. Basically UP is like a variable that holds a value(0x048). You would use UP as how you would use any variables, except its value cannot be changed.Those hexadecimal values are the values that are signaled to the computer whenever a keypress occur. Of course different key presses signals different hex values. Those that are listed are the exact values that are signaled to the computer for every press of those keys. Notice that ESC is assigned a value of 27, which is not in hexadecimal. This is just to show that those hex characters can be represented in integer format. Also, ENTER is assigned a character value '\r', or as you should have known, an escape sequence for carriage return. Actually, a combination of '\n''\r' gets returned whenever we press the ENTER key. That'll be 2 bytes, but we can afford getting just one byte, since no other key returns a '\r' or a '\n'.Okay, let's update the program:
**Defining constant values**
#include //for console-related commands
#define UP 0x048 #define DOWN 0x050 #define LEFT 0x04b #define RIGHT 0x04d #define ESC 27 #define ENTER '\r'
int drawMenu(void);
int drawMenu(void){ int choicePtr=0; char charVal='*'; window(1,1,80,25); textbackground(BLACK); textcolor(BLACK); clrscr(); textcolor(YELLOW); textbackground(BLUE); window(10,2,30,10); clrscr(); gotoxy(1,1); cprintf(" -----===MENU==-----"); cprintf("\r\n"); charVal=' '; if(choicePtr==0){ textcolor(LIGHTGREEN); charVal='*'; } else textcolor(WHITE); cprintf("\r\n [%c]Choice 1",charVal); charVal=' '; if(choicePtr==1){ textcolor(LIGHTGREEN); charVal='*'; } else textcolor(WHITE); cprintf("\r\n [%c]Choice 2",charVal); charVal=' '; if(choicePtr==2){ textcolor(LIGHTGREEN); charVal='*'; } else textcolor(WHITE); cprintf("\r\n [%c]Choice 3",charVal); charVal=' '; if(choicePtr==3){ textcolor(LIGHTGREEN); charVal='*'; } else textcolor(WHITE); cprintf("\r\n [%c]Exit",charVal); }
//Holds the value of the selected choice
/*Depending on the value of choicePtr, this text may or may not come out as LIGHTGREEN, also, there may be an asterisk(*) somewhere between the '[' and the ']', as contained within charVal.*/
/*Depending on the value of choicePtr, this text may or may not come out as LIGHTGREEN, also, there may be an asterisk(*) somewhere between the '[' and the ']', as contained within charVal.*/
/*Depending on the value of choicePtr, this text may or may not come out as LIGHTGREEN, also, there may be an asterisk(*) somewhere between the '[' and the ']', as contained within charVal.*/
/*Depending on the value of choicePtr, this text may or may not come out as LIGHTGREEN, also, there may be an asterisk(*) somewhere between the '[' and the ']', as contained within charVal.*/
Okay, so how do we get the user input? Obviously we have prepared how the menu would respond based on the input, but so far no input-trapping has occured yet. In this type of menu, the getch() function works best because we do not need to display the key everytime the user presses the keyboard; we only need a character, and getch() best serves this purpose.We add this code:
switch(getch()){ case UP: case DOWN: case ENTER: case ESC: }
You noticed that i used getch() as an argument for the switch command. If you're not comfortable with this, try this version:
char keyInput; keyInput=getch(); switch(keyInput){ case UP: case DOWN: case ENTER: case ESC: }
The result would still be the same, but I prefer the first version, simply because it saves typing effort, plus a byte of memory ;). Anyway, to explain it, the getch() function gets executed first. Knowing what getch() does, our program will go to a halt and will not continue unless a keypress is detected. It shall then return the value of the key which was pressed. That returned value shall be caught by the switch() statement and shall be tested against the test cases(UP, DOWN, ENTER, and ESC). Remember that these keywords were defined by us and thus you should understand what they mean.
When the user pressed the UP key, choicePtr must be decremented only if it is greater than zero. Otherwise, the menu shouldn't respond...or, if you want, you can move it to the last available item on the menu, as in a looping selection. the variable choicePtr will be incremented at the DOWN key press. The ESC key should cause our menu to exit. The ENTER key shall make our program return the value of choicePtr to the caller, it should then know what to do with it.
Let's further the program:
switch(getch()){ case UP: if(choicePtr>0)choicePtr--; break; case DOWN: if(choicePtr < 3)choicePtr++;
/*3 is the number of items, so this value is likely to change depending on the number of items on your selection list.*/
break; case ENTER: return choicePtr; case ESC: return 3; }
Let's rewrite the whole program:
**Adding switch block for changing choicePtr**
#include //for console-related commands
#define UP 0x048 #define DOWN 0x050 #define LEFT 0x04b #define RIGHT 0x04d #define ESC 27 #define ENTER '\r'
int drawMenu(void);
int drawMenu(void){ int choicePtr=0; char charVal='*'; window(1,1,80,25); textbackground(BLACK); textcolor(BLACK); clrscr(); textcolor(YELLOW); textbackground(BLUE); window(10,2,30,10); clrscr(); gotoxy(1,1); cprintf(" -----===MENU==-----"); cprintf("\r\n"); charVal=' '; if(choicePtr==0){ textcolor(LIGHTGREEN); charVal='*'; } else textcolor(WHITE); cprintf("\r\n [%c]Choice 1",charVal); charVal=' '; if(choicePtr==1){ textcolor(LIGHTGREEN); charVal='*'; } else textcolor(WHITE); cprintf("\r\n [%c]Choice 2",charVal); charVal=' '; if(choicePtr==2){ textcolor(LIGHTGREEN); charVal='*'; } else textcolor(WHITE); cprintf("\r\n [%c]Choice 3",charVal); charVal=' '; if(choicePtr==3){ textcolor(LIGHTGREEN); charVal='*'; } else textcolor(WHITE); cprintf("\r\n [%c]Exit",charVal); }
//Holds the value of the selected choice
/*Depending on the value of choicePtr, this text may or may not come out as LIGHTGREEN, also, there may be an asterisk(*) somewhere between the '[' and the ']', as contained within charVal.*/
/*Depending on the value of choicePtr, this text may or may not come out as LIGHTGREEN, also, there may be an asterisk(*) somewhere between the '[' and the ']', as contained within charVal.*/
/*Depending on the value of choicePtr, this text may or may not come out as LIGHTGREEN, also, there may be an asterisk(*) somewhere between the '[' and the ']', as contained within charVal.*/
/*Depending on the value of choicePtr, this text may or may not come out as LIGHTGREEN, also, there may be an asterisk(*) somewhere between the '[' and the ']', as contained within charVal.*/
** switch(getch()){ case UP: if(choicePtr>0)choicePtr--; break; case DOWN: if(choicePtr < 3)choicePtr++;
** break; case ENTER: return choicePtr; case ESC: return 3; } /*3 is the number of items, so this value is likely to change depending on the number of items on your selection list.*/
Well, what else do we need? Oh right, a loop. We need to once again enclose the entire menu system in a loop.
**Adding a loop**
#include //for console-related commands
#define UP 0x048 #define DOWN 0x050 #define LEFT 0x04b #define RIGHT 0x04d #define ESC 27 #define ENTER '\r'
int drawMenu(void);
int drawMenu(void){ int choicePtr=0; char charVal='*'; window(1,1,80,25); textbackground(BLACK); textcolor(BLACK); clrscr(); textcolor(YELLOW); textbackground(BLUE); window(10,2,30,10); clrscr(); gotoxy(1,1); cprintf(" -----===MENU==-----"); cprintf("\r\n"); charVal=' '; if(choicePtr==0){ textcolor(LIGHTGREEN); charVal='*'; } else textcolor(WHITE); cprintf("\r\n [%c]Choice 1",charVal); charVal=' '; if(choicePtr==1){ textcolor(LIGHTGREEN); charVal='*'; } else textcolor(WHITE); cprintf("\r\n [%c]Choice 2",charVal); charVal=' '; if(choicePtr==2){ textcolor(LIGHTGREEN); charVal='*'; } else textcolor(WHITE); cprintf("\r\n [%c]Choice 3",charVal); charVal=' '; if(choicePtr==3){ textcolor(LIGHTGREEN); charVal='*'; } else textcolor(WHITE); cprintf("\r\n [%c]Exit",charVal); switch(getch()){ case UP: if(choicePtr>0)choicePtr--; break; case DOWN: if(choicePtr < 3)choicePtr++; break; case ENTER: return choicePtr; case ESC: return 3; } }
**while(1){**
**}**
We're almost done. What we need now is to put them all together and build a main() function:
**Putting together**
#include
#define UP 0x048 #define DOWN 0x050 #define LEFT 0x04b #define RIGHT 0x04d #define ESC 27 #define ENTER '\r'
int drawMenu(void);
** void main(){ int menuReturn=0; _setcursortype(_NOCURSOR); menuReturn=drawMenu(); switch(menuReturn){ case 0: printf("\nYou selected option 1"); getch(); break; case 1: printf("\nYou selected option 2"); getch(); break; case 2: printf("\nYou selected option 3"); getch(); break; case 3: return; } }
//end program
int drawMenu(void){ int choicePtr=0; char charVal='*'; while(1){ window(1,1,80,25); textbackground(BLACK); textcolor(BLACK); clrscr(); textcolor(YELLOW); textbackground(BLUE); window(10,2,30,10); clrscr(); gotoxy(1,1); cprintf(" -----===MENU==-----"); cprintf("\r\n"); charVal=' '; if(choicePtr==0){ textcolor(LIGHTGREEN); charVal='*'; } else textcolor(WHITE); cprintf("\r\n [%c]Choice 1",charVal); charVal=' '; if(choicePtr==1){ textcolor(LIGHTGREEN); charVal='*'; } else textcolor(WHITE); cprintf("\r\n [%c]Choice 2",charVal); charVal=' '; if(choicePtr==2){ textcolor(LIGHTGREEN); charVal='*'; } else textcolor(WHITE); cprintf("\r\n [%c]Choice 3",charVal); charVal=' '; if(choicePtr==3){ textcolor(LIGHTGREEN); charVal='*'; } else textcolor(WHITE); cprintf("\r\n [%c]Exit",charVal); switch(getch()){ case UP: if(choicePtr>0)choicePtr--; break; case DOWN: if(choicePtr < 3)choicePtr++; break; case ENTER: return choicePtr; case ESC: return 3; } } }
In the above example, the main() function called the drawMenu() function. Remember that this user-defined function shall return a value signifying the index of the currently selected choice, therefore such value must be assigned to a particular variable of a compatible data type so that it wouldn't go to waste. We assigned such value to menuReturn, and this variable is tested against the possible values it may have. Our main() function carries out different actions based on this returned value. Finally, at the value of 3, our main(0 function shall terminate causing the program itself to terminate.
The _setcursortype() is part of the conio.h library and, as suggested by its name, sets the cursor appearance. Normally we wouldn't want a blinking cursor on such type of menu, unlike in our previous menu program where a cursor is needed. There you have it. A menu with selection highlights.
Please note however, that this program may not run on Visual C++, and Borland C++ in windows mode. If you still want to try this though, replace all cprintf() with printf(); change the "\r\n" combination to '\n' only; remove all textcolor() and textbackground() commands; and add stdio.h to your header file list. Windows-based compilers are not designed for such kinds of programs unlike a DOS-based compiler.
If you have any questions, comments, suggestions, or reactions, just e-mail me atpiartsco@yahoo.com
back to top
Khin furthers the Turbo C++ tutorial from two weeks ago that looked at creating a menu system, and this time it's all about adding one those little extras we all take for granted, highlight selection.
Mar 30, '05
Mar 1, '05
Feb 22, '05
Feb 8, '05
Jan 25, '05
Sep 1, '05
Jul 11, '05
Mar 30, '05
Mar 1, '05
Feb 22, '05
