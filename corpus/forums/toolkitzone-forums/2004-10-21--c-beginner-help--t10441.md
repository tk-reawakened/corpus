---
kind: forum-thread
id: "toolkitzone-forums/10441"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "10441"
title: "C++ beginner help"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=10441"
written: "2004-10-21T04:59:00"
last_post: "2004-10-22T01:37:00"
date_confidence: "exact"
captured: ["20041226085714"]
author: "Gnarf"
repliers: ["Colin", "matt72186", "khin", "Levi", "Marc", "sivart"]
authors: ["Gnarf", "Colin", "matt72186", "khin", "Levi", "Marc", "sivart"]
posts_present: 15
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_114941_amp_", captured: "20041226085714", sha256: "adb3cdc60d443a1df360510537c4661180beee072ffa2e034726c547b962c102", wayback_url: "https://web.archive.org/web/20041226085714/http://www.toolkitzone.com/forums/viewtopic.php?p=114941&amp="}
links:
  - {url: "http://www.darkBASIC.com", status: "external", local: null}
---

# C++ beginner help

### Gnarf · 2004-10-21 04:59 · #B114248

Not much of help with a program but what some of this code means...
I was reading some tutorials and am using DevC++...
Anyway, the tutorials were talking about constants...
Constants.............. ... ... ... ...
Errr. This whole "constant" thing is starting to aggrevate me!
I don't understand it. They keep mentioning it but I keep telling myself I will find out later on. Well, I haven't. I just want to understand it now so I don't get lost...
Also, the escape codes...which I semi-understand...and the data types for variables...what's the difference between each data type and what are they for...
I'd be very grateful if someone could help me, I just started learning last night and they are introducing some alien language to me...
Anyone have more of a noob friendly tutorial? Or can anyone please answer my questions...maybe some examples or something.
Thanks! Smile

### Colin · 2004-10-21 05:02 · #B114250

const tells the compiler the var will not be modified; volatile tells the compiler it will be modified in ways it could never guess.
...
I don't feel like sorting through the whole post -- that's the only good question, anyway Razz

### Gnarf · 2004-10-21 05:04 · #B114251

**KSNiloc wrote:**

> const tells the compiler the var will not be modified; volatile tells the compiler it will be modified in ways it could never guess.
> ...
> I don't feel like sorting through the whole post -- that's the only good question, anyway Razz
>

I guess it sorta helps...
const declares constants before I use them like int and such right?
But what are constants in general...and whats the different between int, float, bool, etc.?

### matt72186 · 2004-10-21 05:43 · #B114269

they are consistent throughout the program, like if you make a constant equal 5, it will always equal 5, it won't be anything else, they are used for things you don't need to change, but you'll refer to often, like PI
usually programmers using PI will set it as a constant so that whenever they need PI in a calculation, they just type PI
const float PI = 3.14
I think it's like that

### khin · 2004-10-21 08:27 · #B114285

Well a programming language is built around the sets of rules, and those you mentioned are part of those rules.
Constants
KSN and matt72186(hooray! I memorized it) already explained constants, why and how they are used.
Let's say you need to calculate the area of a circle. You need to follow the formula PI*(radius*radius). PI is a constant. We all know it's approximately 3.14. radius on the other hand is what we call a variable. It's value can be changed depending on the program, user input, file input, etc..
Translating this in C++ code, we're going to need variables such as Pi and radius.
We declare them like so:

**Code:**

```
const float Pi;

int radius;
```

Using them in our program...

**Code:**

```
#include<iostream.h>

void main(){

float area;

const float Pi=3.14;//cannot be modified

int radius;

area=Pi*(radius*radius);//you may remove the ( )

cout<<"The area is "<<area;

}
```

If you try to modify the value of Pi, you'll recieve a compiler error. Constant data types can only be given values through initialization, like the one I did.

**Code:**

```
#include<iostream.h>

void main(){

float area;

const float Pi=3.14;//cannot be modified

int radius;

Pi=3.143121;//ERROR

area=Pi*(radius*radius);//you may remove the ( )

cout<<"The area is "<<area;

}
```

..i realized you said you were just starting last night, so are you referring to the const modifier or the constants in C++?
Constants, besides the const modifier are those values in C++ that are non-changeable. Examples of constants are:
1,2,3,4,5..... for numbers(or type int
'a','b','C'......for characters(type char
"This is a string"......for string(technically, there's no string data type in C++, either character array, pointer, or building a string class)
1.2,3.5,4.7,6.8......for floating-point, or double(either float or double
true, false for boolean(bool)
They are not variables, instead they are fixed numbers, or constants in a sense. We also have those character constants AKA character escape sequences.
'\n'-newline. Use it to make the cursor move to the next line
'\r'-carriage return. Use it to move the cursor at the start of the line
'\b'-backspace. Use it to emulate the backspace.
There are more, but i guess they should be in the book you are reading. These escape sequences are useable to any function/method that can manipulate characters(e.g. displaying text on the screen)

**Code:**

```
cout<<"First Line"<<"\n"<<"second line";
```

or

**Code:**

```
cout<<"First Line\nsecond line";
```

Data Types
Data types are, well, a way to separate each type of value in C++. Hmmm..you know rpgCode, right? Data types are needed because technically they reserve certain amount of memory from our RAM. Here are the basic data types:
int-numbers, can have a value from -32,768 to 32,767
char-characters, can have a value of 0-255
float-floating point. Numbers with decimal places. I forgot the exact range.
double-same as float but with wider range
Those are the four basic data types, also known as primitives. From them, other data types are derived.
Remember that a variable is a placeholder for a certain value. If that is the case, then it is logical for a variable to know how big is the value that it is going to hold. Hence, the requirement for the data type.
Here are the number of bytes occupied by each primitive:
int-2 bytes
char-1byte
float-4 bytes
double-8 bytes
That means that for every variable that you use, you are borrowing a specific amount or memory from your RAM. Recall the circle program that we did. If we sum up the memory usage of all variables we used, it'd turn out that we consumed 10 bytes of RAM. Of course we're not counting all elements of the whole program, but that proves the point about variable usage.

**Code:**

```
#include<iostream.h>

void main(){

int x;

char ch;

float f;

x=10;//gives x the value of 10

cout<<"x="<<x<<endl;//should display 10

ch='a';//gives ch the value of 'a'(ASCII for 97)

cout<<"ch="<<ch<<endl;//sould display 'a' w/o quotes

f=72.5;//gives f the value 72.5

cout<<"f="<<f<<endl;//sould display 72.5 with trailing 0's

x=73.7;/*this is actually not valid for an integer type, but C++ can convert it, so x shall recieve the value 73*/

cout<<"x="<<x<<endl;//should display 73

ch=98;//gives ch the value 98

cout<<"ch="<<ch<<endl;/*sould display 'b'(ASCII value for 98) w/o quotes*/

f=10;/*another improper amount. This shall be converted to approx. 10.00000*/

cout<<"f="<<f<<endl;//sould display 10.0 with trailing 0's

}
```

I may have skipped some things. I'll let someone else correct me. Smile

### matt72186 · 2004-10-21 08:41 · #B114287

Ah, just thought a good description
when you use
const float PI = 3.14
you can pretty much find wherever PI is in your code and write 3.14 instead and it'll give the same effect, C++ just substitutes your constant in for wherever you write it.

### Colin · 2004-10-21 13:42 · #B114347

"you can pretty much find wherever PI is in your code and write 3.14 instead and it'll give the same effect, C++ just substitutes your constant in for wherever you write it."
NO. Only #define macros have that effect, const vars all still vars.
" either character array, pointer, or building a string class"
What about BSTRs (pointer to a pointer of an array of two-chars, three bytes back from the pointer is the length of the string in bytes -- also the type of string VB uses)? Wink

### Levi · 2004-10-21 15:04 · #B114399

Though I'm pretty sure its well explained and all, and that this person will figure it out. It is a good thing to mention that you must set a constant's value as soon as you designate the variable.
It's not when you first set it to something that it becomes constant but when its first made...
const float PI; //sets PI to zero or NULL
//after this you cannot change PI it will always be zero so you need to declare it like this.
const float PI=3.14; //sets PI to 3.14

### Levi · 2004-10-21 15:05 · #B114400

Oh by the way, what tutorials are you using? Sometimes things can be made easier by different tutorial help.
I started with C++ for Dummies book, then went to cplusplus.com. Not the best but it definatly helped.

### Marc · 2004-10-21 18:54 · #B114501

Since we are on the beginner subject of C++, does any one know any good tutorials for making classes (with a load of examples) using pointers and using refrences '&'?

### Gnarf · 2004-10-21 22:43 · #B114779

Thanks a bunch everyone, especially Khin, the description was very helpful...
I understand what they are now, kinda like stating a var before you use it. Then the var can be used throughout the program like a global var...correct?
Levi: I was using the ones that DevC++ considered...forgot what they are called.

### sivart · 2004-10-21 23:10 · #B114809

Awsome! gettin into codin , eh? Razz

### Gnarf · 2004-10-21 23:20 · #B114817

**sivart wrote:**

> Awsome! gettin into codin , eh? Razz
>

Yep
No VB for me though Sad
I can't find my Visual Studios CD...
I got it for free from a friend though. I am assuming my brother took it with him to college, the CDs.
Anyway, getting DarkBASIC...sometime this week, in the mail. It is jam packed with awesome stuff!
check it out and read the list of what it has...
[DB (Scroll down and read the feature)](http://www.darkBASIC.com)
PS: I'm coming on MSN, discuss some of this.

### khin · 2004-10-22 01:35 · #B114936

**KSNiloc wrote:**

> What about BSTRs (pointer to a pointer of an array of two-chars, three bytes back from the pointer is the length of the string in bytes -- also the type of string VB uses)? Wink
>

hmmm..i don't think beginners need to know that yet(even arrays, pointers and classes are not for starters). you know when that topic should be learned. Wink

### Marc · 2004-10-22 01:37 · #B114941

**KSNiloc wrote:**

> What about BSTRs (pointer to a pointer of an array of two-chars, three bytes back from the pointer is the length of the string in bytes -- also the type of string VB uses)? Wink
>

What The Fuck! As if C++ wasn't hard enough without that.

**khin wrote:**

> hmmm..i don't think beginners need to know that yet(even arrays, pointers and classes are not for starters). you know when that topic should be learned. Wink
>

Your my new best buddy Very Happy.
