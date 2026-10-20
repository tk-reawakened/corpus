---
kind: doc
id: "toolkitzone.com/63"
site: "toolkitzone.com"
title: "column"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=63"
written: "2004-11-30T23:58:00"
date_confidence: "exact"
updated: null
captured: ["20041216140532", "20041216140532"]
author: "khin"
repliers: []
authors: ["khin"]
comments_present: 0
f_author: "khin"
f_date: "November 30, 2004, 11:58 pm"
f_description: "Menu systems are very important in most applications such as database programs and games, allowing high-level interaction between the user and the program. In this weeks discussion, Khin takes you through creating a menu system in C."
f_title: "Creating a Basic Menu Program"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_63", captured: "20041216140532", sha256: "3fb54d841f426b46067325eb1555cbffceb9be921bbddd3b10de5ef6e2616fc2", wayback_url: "https://web.archive.org/web/20041216140532/http://toolkitzone.com/library.php?mode=read&doc=63"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_63-304f8d", captured: "20041216140532", sha256: "3fb54d841f426b46067325eb1555cbffceb9be921bbddd3b10de5ef6e2616fc2", wayback_url: "https://web.archive.org/web/20041216140532/http://www.toolkitzone.com/library.php?mode=read&doc=63"}
---

# column

Creativity > Khin's Desk
Menu systems are very important in most applications such as database programs and games, allowing high-level interaction between the user and the program. In this weeks discussion, Khin takes you through creating a menu system in C.
Creating a Basic Menu Program
A menu system is very important in most applications. Database programs, as well as games use menu systems. It enables high-level interaction between the user and the program. This discussion will teach the basics of creating a menu system.
The objective of our menu is simple: prompt the user for a choice by typing numbers that corresponds to the item desired. After the selection, the program shall carry out the instructions based on the selected operation. If in case the input is invalid, an invalid warning shall appear.
> This tutorial teaches basic menu programmming using Turbo C++ v5. It's an old compiler, but C++ in essence is still a hot item. Note however, that the constructs and proptotypes we'll be using shall follow the older C format, not C++.
So let us begin. First, what you should bear in mind is what our program have. Let us collect the requirements for the program, and build our model.
Well, it's obvious there is output. Prompting the user for a choice requires output, therefore will be inevitable. *printf()*
Take note that the program will require input. The part where the user will be asked for a choice requires the user to input a character/number from the keyboard, therefore input is required. We have a vast array of functions to be used for user input: . For the purpose of this discussion, we shall go with the more basic function . *getch(), getche(), getchar(), scanf()* *scanf()*
Another important aspect of the program is selection, or decision-making. You know that after the user inputs a character/number, the program should be able to carry out instruction based on the input. The program must be able to look at the input and decide what to do next based on it. Decision-making can be done using or . *if...else* *switch*
Well, it's almost done. One last thing to note is that the program . The program should not end until the user selected the or option. After the program carries out instruction, it must again display the list and prompt the user for a choice. After selecting it will carry out the instructions again and goes back to displaying the list. The process goes on and on until the exit option is selected. You should have realized by now that a technique is required. Looping is achieved by using , , , and loop. **should not terminate on one run** **quit** **exit** *looping* *goto label* *while* *do...while* *for...*
After filtering out what commands we'll probably use, we can start building the menu. of course, let's start typing the common prerequisites in building a C program:
**Including header files and preparing the block *main***
#include #include
void main(void){
You already know that the header file is required for the and functions. will also be used because later in the program we'll use the function. *stdio.h* *printf()* *scanf()* *conio.h* *getch()*
Now that it's been laid down, we have to think about the variables that we have to use. We are aware that there is user input, so a variable placeholder for the input is required. What type of variable will we use? Recall that there are a number of data types: , among pointers and arrays. Before we take care of that, let us build the menu first. *int, char, double, float*
**Using the function to display the menu *printf()***
#include
#include
void main(void){
clrscr(); printf(" \"Menu\""); printf("\n[1]Option A"); printf("\n[2]Option B"); printf("\n[3]Option C");
Now that the menu has been built, it's time to ask the user for a choice. Remember that since in the menu, you used numbers to denote the options(1-3), it is understandable that the values the user would have to input is of numerical value. SInce we need a numerical value for input, we need a numerical variable.
**Using the function to get user input *scanf()***
#include
#include
void main(void){ clrscr(); printf(" \"Menu\""); printf("\n[1]Option A"); printf("\n[2]Option B"); printf("\n[3]Option C");
int choice;
printf("\nInput your choice(1-3): "); scanf("%d",&choice);
After the program executes the function, our variable is now holding a number representing what the user typed/pressed on the keyboard. It's now time to and make the program decide on what to do next based on the input. As said earlier, we can use either or . Since this is a menu program, it is more appropriate to use . *scanf()* *choice* *look at the value* *if..else* *switch* *switch*
**Making the program and decide based on the input *think***
#include
#include
void main(void){ int choice;
clrscr(); printf(" \"Menu\""); printf("\n[1]Option A"); printf("\n[2]Option B"); printf("\n[3]Option C"); printf("\nInput your choice(1-3): "); scanf("%d",&choice);
switch(choice){ case 1: printf("\nYou selected Option A."); break; case 2: printf("\nYou selected Option B");
break; } getch();
case 3: printf("\nYou selected Option C");
break;
: printf("\nInvalid!!"); default
break;
It's pretty easy, isn't it? The program will print if the user pressed . It will do other things if other options were selected. Finally, it will display if the user pressed any other keys not similar to 1,2, or 3. The function before the end of the block will cause the program to stop and wait for a key press before terminating. Any key will do, as we just need to see the output. If you try to run the program without the function, you wouldn't be able to see anything(Note however, this isn't true for C compilers). *You selected Option A* *1* *Invalid!!* *getch()* *main* *getch()* **all**
Supposing you run the program as it is now. You will notice it runs as expected, but after selecting and having seen the program's response, your program terminates. That's because we're not using any looping techniques yet. For the program to go over and over, we need to loop through it. Any of the aforementioned looping techiques will do, but it is preferrable to use infinite or loop. The can still be used, but it has gone unpopular and is considered to be used only be amateur and lazy programmers. Anyway, let's try it in all three loops. *while* *for* *goto label*
**Using the looping technique *goto label***
#include
#include
void main(void){ int choice;
clrscr(); printf(" \"Menu\""); printf("\n[1]Option A"); printf("\n[2]Option B"); printf("\n[3]Option C");
LOOP_HERE:
printf("\n[4]Exit"); scanf("%d",&choice); switch(choice){ case 1: printf("\nYou selected Option A."); case 2: printf("\nYou selected Option B");
printf("\nInput your choice(1-4): ");
getch(); goto LOOP_HERE;
getch(); goto LOOP_HERE;
} getch();
case 3: printf("\nYou selected Option C");
getch(); goto LOOP_HERE;
case 4: printf("\nYou selected Exit"); break;
: printf("\nInvalid!!"); default
getch(); goto LOOP_HERE;
As you can see, a fourth option was added. This is necessary or else our program will be trapped in an infinite loop. The fourth option is the option which will make the program escape out of the loop. Accordingly, each other options leads back to which is the starting point for the loop. Why is there a before the ? It is necessary so that the user would be able to see what gets displayed before clearing the screen. If it was to be removed and run, the user will quickly loop back to the label just after displaying the result and effectively clears the screen, display the menu and waits for a keypress. In short, the user will never get the chance to see the output. Instead, he/she will only catch the menu everytime since the program only stops and wait at the part after the menu was displayed. It is therefore obvious that we must make the program stop and wait before it clears the screen. All options have a statement in place of the statement; all except for that is. If the user typed 4, the program shall display and then exits the and comes across a command which will cause it to wait for a keypress before ultimately terminating. **exit** **LOOP_HERE** *getch()* *goto label* *goto label* *break* *case 4* *You selected Exit* *switch* *getch*
**Using the looping technique *while...***
#include
#include
void main(void){ int choice;
clrscr(); printf(" \"Menu\""); printf("\n[1]Option A"); printf("\n[2]Option B"); printf("\n[3]Option C");
while(1){
printf("\n[4]Exit"); scanf("%d",&choice); switch(choice){ case 1: printf("\nYou selected Option A."); case 2: printf("\nYou selected Option B");
printf("\nInput your choice(1-4): ");
break;
break; } getch();
case 3: printf("\nYou selected Option C");
break;
case 4: printf("\nYou selected Exit"); return;
: printf("\nInvalid!!"); default
break;
It's much simpler to look at using a loop. All you have to do is enclosed the whole program flow in an infinite loop and only exits when option 4 is selected. Note that the statement is used to make the program terminate prematurely. Normally, makes a function end, but since we only have our function, our program effectively ends. Making a loop was made possible by issuing a command. If you look at the condition closer, it says that . Since 1 will always be equal to 1, the condition remains true. *while* *return* *return* *main* *while* *while(1)* **while 1=1**
**Using the looping technique *for...***
#include
#include
void main(void){ int choice;
clrscr(); printf(" \"Menu\""); printf("\n[1]Option A"); printf("\n[2]Option B"); printf("\n[3]Option C");
printf("\n[4]Exit"); printf("\nInput your choice(1-4): ");
scanf("%d",&choice); switch(choice){ case 1: printf("\nYou selected Option A."); break;
case 2: printf("\nYou selected Option B"); } getch(); }
break;
case 3: printf("\nYou selected Option C"); break;
case 4: printf("\nYou selected Exit"); return; : printf("\nInvalid!!"); break;
default
There you have it. You are now capable of building a basic console-based menu. Be reminded that there are still several ways to achieve the same output by utilizing the different capabilities of the looping techniques as well as different selection techniques.
If you have any questions, comments, suggestions, or reactions, just e-mail me (redacted: email)
Colin
December 1, 2004, 12:09 am
I hate C. :) C++ is far better. Oh, and "while (1)" means "while (1 != 0)" not while it is 1.
TheCPPFreak220
December 1, 2004, 12:55 am
Agreed. Still a good tutorial.
Dec 14, '04
Dec 7, '04
Nov 24, '04
Dec 14, '04
creativity > khin's desk
Dec 7, '04
creativity > khin's desk
Nov 24, '04
creativity > khin's desk
