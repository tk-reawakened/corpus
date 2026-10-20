---
kind: doc
id: "toolkitzone.com/168"
site: "toolkitzone.com"
title: "Image resized for better viewing"
original_url: "http://toolkitzone.com/library.php?mode=read&doc=168"
written: "2005-01-25T18:06:00"
date_confidence: "exact"
updated: null
captured: ["20060222120636", "20060314035715", "20060621114632"]
author: "Khin"
repliers: []
authors: ["Khin"]
comments_present: 0
f_author: "Khin"
f_date: "January 25, 2005, 6:06 pm"
f_description: "Khin takes a break from the sprite tutorial to go back to his Turbo C++ development, this time creating a digital and analog clock."
f_section: "Creativity > Khin's Desk"
f_title: "Creating A Clock: Part 1"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_168", captured: "20060222120636", sha256: "023817dad8ce2d6e2210b476754beee3d4827cd126317bf89d3eb615e2a7b00a", wayback_url: "https://web.archive.org/web/20060222120636/http://www.toolkitzone.com:80/library.php?mode=read&doc=168&PHPSESSID=ef05e627eb8c2677174592c2e7f83195"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_view_cadd_doc_168", captured: "20060314035715", sha256: "5ded2afee5203c7dbfbbf176e88542b3253c9f91140975ffdd331f08c69af90a", wayback_url: "https://web.archive.org/web/20060314035715/http://toolkitzone.com:80/library.php?mode=read&view=cadd&doc=168&PHPSESSID=bdcceeefceef8ff863ad82d0d089ece4"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_168-35f613", captured: "20060621114632", sha256: "dc8fb589fd1c8857ce9432ed5d09d7aa6ccdf296689de9f26266ee797963e1e5", wayback_url: "https://web.archive.org/web/20060621114632/http://toolkitzone.com:80/library.php?mode=read&doc=168&PHPSESSID=03782686e23a28da229b5827ca05e03c"}
---

# Image resized for better viewing

Turbo C/C++ - Creating a Digital and Analog Clock
Good day. Today we take a break from sprite works and take a look at programming. I know you are anticipating more sprite tutorials, but this is all I could do with my spare time--and I think you'd find this useful too.
This article shall discuss the procedures of making a digital and analog clock in Turbo C++. Once again, we'll most probably use constructs ranging from C to C++ so compatibility with a wide number of compilers isn't assured.
This tutorial takes advantage of Turbo C++'s simplistic graphics system. Such graphics system enables programmers to create NES-like environments-- 16 colors to mix and match, each can be customized by giving them RGB values, or you can simply leave the default colors(discussed in the previous tutorial).
If you're wondering how would you apply this tutorial in your game or general programming, then I think it's safe to say that this would make a good learning material for you beginning programmers out there. Plus, the logic and algorithm that will be used can easily be applied to any programming language(e.g. RPGCode)! Yes, all you have to do is change the commands, but if you keep the logic in tact you'll be making an analog clock for your game in no time.
Alright, enough introduction. Let's get it started. First and foremost, our included header files:
#include[stdio.h] #include[conio.h] #include[graphics.h] #include[string.h] #include[math.h] #include[dos.h]
I don't know about other compilers, but this style of writing a directive is completely valid in Visual C++, Borland C++, and Turbo C++.
is required in most cases when writing programs that will make use of the standard input/output stream. In our case, we need this for the function which shall be used to convert numbers to strings. **stdio.h** *sprintf()*
is ever needed for commands such as **conio.h** *getch()*
is a header file only found in Turbo C++, along with all the graphics library. Actually it can be found in the package too, but Borland will simply refuse to compile it becase it does not support it. If you found a way to do it in Borland then congratulations, and please tell me how. **graphics.h** ***Borland*** ***C++***
contains functions for string manipulations such as copying string, concatenating strings and so fort. C isn't as flexible when it comes to strings as other Object Oriented Programming languages. In Visual C++ however, there are already constructs for a CString class, but we're after simpler things here, so we'll simply use a to achieve what we want. **string.h** *character array*
is required for trigonometric/geometric computations. Yes folks, trigonometry. Don't turn your backs though, we won't be tackling hardcore trigonometry here(at least not in this program). We'll only need the legendary (Hypotenuse). **math.h** *Pythagorean Theorem*
is needed for some subtle functions such as delay, as well as getting the system time. We could have used too, but I prefer this method for the sake of this tutorial. **dos.h** **time.h**
Now that the required header files are in place, let's start constructing our structures. If you're in C++, you could refer to this as a , but there would be some adjustments that you'd want to make. Same goes with . I haven't studied OOP support well enough to find out how similar it is with C++ though. You may want to ask Colin about it. *class* [RPGCode](http://toolkitzone.com) [RPGCode's](http://toolkitzone.com)
Here's a structure for time. The data members are all in , which we shall refer to as a . *character array* *string*
struct timeStruct{ char sHour[3],sMin[3],sSec[3],AmPm[3]; char time[20]; };
, , shall hold values for hour, minute, and second respectively. shall hold a string value indication whether the time of the day is in Am or Pm. The variable shall hold the complete string for the time. It's the combined values of the previous variables mentioned. *sHour* *sMin* *sSec* *AmPm* *time*
int maxx,maxy;
It has been accustomed for me to get the boundaries of my drawing canvas. he variables and shall hold values for the screen's width and height respectively. Obviously they should be integral. *maxx* *maxy*
And now, our function. This program will only use one function, which is the main one. *main()*
void main(){ struct time t; struct timeStruct theTime; int gdriver = VGA,gmode=VGAMED,errorcode,page=0; initgraph(&gdriver, &gmode,"c:\\tc\\bgi"); errorcode = graphresult(); if (errorcode != grOk) { printf("Graphics error: %s\n", grapherrormsg(errorcode)); printf("Press any key to halt:"); getch(); } closegraph(); }
What we actually did here is initialize Turbo C++'s graphics environment. Remember that by default, when running C++ programs that are DOS-based, our machine switches to mode. Simply put, we get transfered from to and therefore using graphics commands that are otherwise easy in RPGCode , Java, and VB are not that easily done here. After the initialization everything will be a breeze though. *8086 emulation* *Windows* *DOS*
To enable the graphics mode, we use the command . The protoype is as follows: *initgraph()*
void far initgraph(int far *graphdriver, int far *graphmode, char far *pathtodriver);
the function takes three parameters. The first one is a pointer to the driver to be used. Turbo C++ has a predefined set of macros for these drivers. They are as follows:
Macro
Value
DETECT
0 (requests autodetection)
CGA
MCGA
EGA
EGA64
EGAMONO
IBM8514
HERCMONO
ATT400
VGA
PC3270
As you can see, Turbo C++ supports multiple graphics drivers. each of them have different resolutions, colors, and number of pages. For our standard video, we normally use mode. If you have better graphics card, feel free to experiment on other modes. **VGA**
The second parameter to is the graphics mode specific to a graphics driver. The driver for example, has 3 modes: and . *initgraph* **VGA** *VGALO, VGAMED,* *VGAHI*
Normally is used due to it's performance. *VGAMED*
Here's a table showing and graphics drivers and their respective graphics modes along with the properties. **VGA** **EGA**
Driver
Modes
Value
ColumnxRow(Resolution)
Palette
Pages
EGA
EGALO
640x200
EGAHI
640x350
EGA64
EGA64LO
640x200
EGA64HI
640x350
EGAMONO
EGAMONOHI
640x350
1**
EGAMONOLO
640x350
2**
VGA
VGALO
640x200
VGAMED
640x350
VGAHI
640x480
* 64K on EGAMONO card ** 256K on EGAMONO card
For this material we shall use because we need at least two pages for animation. **VGAMED**
The last parameter to initgraph is the path to the graphics driver. You see, graphics mode cannot be initialized without the dependencies. They must be properly addressed, kinda like how you retrieve the source for an image in an HTML page. Just put within the third parameter the path to the folder labeled . t is normally within the root directory of Turbo C++, along with the . ***BGI*** *bin* and folders *include*
struct time t; struct timeStruct theTime; int gdriver = VGA,gmode=VGAMED,errorcode,page=0;
Using the old C-style declaration, we create a object and named it . We also created an object of type and named it . The structure is predefined within and is required for programs that will retrieve system time in this manner. Here's the breakdown of the sructure: *time* **t** *timeStruct* **theTime** *time* *dos.h*
struct time { unsigned char ti_min; /* minutes */ unsigned char ti_hour; /* hours */ unsigned char ti_hund; /* hundredths of seconds */ unsigned char ti_sec; /* seconds */ };
We shall discuss retrieving system time later. For now, let us concentrate on the initialization of the graphics environment.
As previously stated, we use the function to initialize the graphics environment. To make this possible, we must create variables of type and give them values either from the macros or their numerical values. We then put them as parameters to but take note, we must prepend them with the sign to denote that we are passing the . Very technical term for some. To understand it you must have knowledge about data structures and stuff such as pointers, arrays, memory, etc. PM me and I'll explain them to you if you want. *initgraph* *int* *initgraph* **&** *memory location*
int gdriver = VGA,gmode=VGAMED,errorcode,page=0; initgraph(&gdriver, &gmode,"c:\\tc\\bgi");
As you can see, our program uses driver in mode. the variable page shall hold the number of the current page that is being used. Remember that in VGAMED we have two pages for usage. Think of them as virtual canvases where we can draw and flip. **VGA** **VGAMED**
It is assumed that the loading of graphics drivers are successful with , but as programmers, safety should always be a priority. We must check whether or not the graphics drivers has indeed loaded. *initgraph*
errorcode = graphresult(); if (errorcode != grOk) { printf("Graphics error: %s\n", grapherrormsg(errorcode)); printf("Press any key to halt:"); getch(); }
As you can see, is a function we can use to determine the result of . *graphresult()* *initgraph()*
int far graphresult(void);
returns the error code for the last graphics operation that reported an error, then resets the error level to grOk. *graphresult*
The enumerated type graphics_errors defines the error codes.The variable maintained by graphresult is reset to 0 after graphresult has been called. Therefore, you should store the value of graphresult into a temporary variable and then test it.
Error code | graphics_errors constant | Corresponding error message string ------+-------------------+----------------------------------------------- 0 ¦ grOk ¦ No error -1 ¦ grNoInitGraph ¦ (BGI) graphics not installed (use initgraph) -2 ¦ grNotDetected ¦ Graphics hardware not detected -3 ¦ grFileNotFound ¦ Device driver file not found -4 ¦ grInvalidDriver ¦ Invalid device driver file -5 ¦ grNoLoadMem ¦ Not enough memory to load driver -6 ¦ grNoScanMem ¦ Out of memory in scan fill -7 ¦ grNoFloodMem ¦ Out of memory in flood fill -8 ¦ grFontNotFound ¦ Font file not found -9 ¦ grNoFontMem ¦ Not enough memory to load font -10 ¦ grInvalidMode ¦ Invalid graphics mode for selected driver -11 ¦ grError ¦ Graphics error -12 ¦ grIOerror ¦ Graphics I/O error -13 ¦ grInvalidFont ¦ Invalid font file -14 ¦ grInvalidFontNum ¦ Invalid font number -15 ¦ grInvalidDeviceNum¦ Invalid device number -18 ¦ grInvalidVersion ¦ Invalid version number
After getting the graphics result, we test the placeholder variable if it's not equal to . If it is, then it means *errorcode* *grOk* *initgraph* was successful. If not, then we must discontinue using the graphics mode for it may cause harm on our system.
If the graphics initialization was successful then we should continue.
maxx=getmaxx(); maxy=getmaxy(); int x,y,ctr; char buffer[50];
These are placeholder variables that will be used throughout the program. You'll realize their use as we continue.
To get the width of the screen, we use the command . is for getting the height of the screen. Remember that the width and height depend on the resolution as set by the graphics mode used. *getmaxx()* *getmaxy()*
This program is animated, so we'll use a loop. A loop has been my personal choice for this. *while()*
gettime(&t);
Getting the system time is as easy as typing this command. gets the system time and stores it in the address of a variable of type . Recall that we defined a variable earlier. This variable shall hold information about the time we just retrieved. *gettime()* *struct time* *t*
while(!kbhit()){ gettime(&t); if(t.ti_hour==0)t.ti_hour=12; if(t.ti_hour>12){ t.ti_hour-=12; strcpy(theTime.AmPm,"PM"); } else{ strcpy(theTime.AmPm,"AM"); } sprintf(theTime.sHour,"%d",t.ti_hour); sprintf(theTime.sMin,"%d",t.ti_min); sprintf(theTime.sSec,"%d",t.ti_sec); sprintf(theTime.time,"%02d:%02d:%02d %s",t.ti_hour,t.ti_min,t.ti_sec,theTime.AmPm); delay(1000); }
What we just did is we formatted the time we retireve into a form that would be proper for our program. After getting the system time and storing it to . We now have the variables at our disposal. is in 24-hour format so we just did a bit of tweaking to make it not 24-hours. If the value within is greater than twelve then we simply subtract 12 from it. This would make the hour 23 become 1, for example. Also, in accordance to that, if the time exceeds 12, then it's just proper to set the *t* *t.ti_hour, t.ti_min, t.ti_sec* *t.ti_hour* *t.ti_nour* *AmPm* data member of our object to "PM". If hour is less or equal to 12, then it's "AM". Take note of the command . This function is used to copy the string from the second parameter to the first parameter. I wish it would be as easy as using the '=' operator, but we don't have time to overload it, so we must make do with this function. Other OOP languages however allows you to copy a string with the '=' operator, as in . No can do in C though. *theTime* *strcpy()* **theTime.AmPm="PM"**
A series of are required to convert the values to string. Recall that all values stored in the structure are numerical. We can't display it if they stay numerical, so we have to convert them to strings. The function does the trick. It's a bit complicated to explain, but I'll try to narrow it down to our usage. *sprintf()* *t* *sprintf()*
Generally, sprintf() converts one data type to string conveniently using the standard I/O stream. The first parameter to sprintf() is the destination string, meaning an array, or a pointer. The second parameter contains the value to be placed on the destination string. Anything typed between the "" shall be copied to the destination--anything but the character converters that is. In C, we have character converters like . These character converters are for and respectively. If you need the sign written to the string in sprintf, then you should use . The suceeding parameters are the source variables that you'd like to be converted. It has variable lengths, meaning you can have one, two, three or more parameters succeeding the second one. It depends on how many variables you want converted and stored within the string . **%d, %c, %s, %f** **decimals(integers), characters, strings,** **floating-points** **%** **%%** **all at once**
To simplify, take this command for example:
sprintf(theTime.sSec,"%d",t.ti_sec);
Fairly simple. What it did is that it converted the value from to string and stored the new value to . A conversion symbol of is used to denote that the source variable is of type. Had been a floating point, we should put instead *t.ti_sec* *theTime.sSec* **%d** **integral** *t.ti_sec* **%f**
Another example:
sprintf(theTime.time," %02d %02d %02d ",t.ti_hour,t.ti_min,t.ti_sec,theTime.AmPm);
I color-coded the characters that will be stored within the variable theTime.time as is. They are in RED. These characters will be saved in the variable as they are written. The green characters are converters. The symbol simply means that the computer should make the number at least 2 digits. If there's only one digit then prepend the number with a zero(0). The first converts into string and store it in . The following refers to and so on. **%02d** **%02d** *t.ti_hour* *theTime.time* *t.ti_min*
Let us create an example. Supposed yielded the following values: *gettime*
LET:
t.ti_hour=10
t.ti_min=30 t.ti_sec=1
Applying the codes we've discussed, and using the variable will have the value: *sprintf()* *theTime.time*
10:30:01 AM
There you go. A digital clock engine running on text mode.
The last part of the code is the function that shall delay the program in a given milliseconds. So to summarize, our program shall keep on running because of the loop, it shall get the time at each loop, formats it, waits for a second delay, then repeat everything. It shall continue until a keyboard hit was detected, as trapped by the function. This function returns if a key was pressed from the keyboard. *delay()* *kbhit()* **a non-zero value**
Right now, the program has no output. That's just the engine. Let's beef it up and give it some life, shall we?
void main(){ struct time t; struct timeStruct theTime; int gdriver = VGA,gmode=VGAMED,errorcode,page=0; initgraph(&gdriver, &gmode,"c:\\tc\\bgi"); errorcode = graphresult(); if (errorcode != grOk) { printf("Graphics error: %s\n", grapherrormsg(errorcode)); printf("Press any key to halt:"); getch(); } while(!kbhit()){ setactivepage(page); gettime(&t); if(t.ti_hour==0)t.ti_hour=12; if(t.ti_hour>12){ t.ti_hour-=12; strcpy(theTime.AmPm,"PM"); } else{ strcpy(theTime.AmPm,"AM"); } sprintf(theTime.sHour,"%d",t.ti_hour); sprintf(theTime.sMin,"%d",t.ti_min); sprintf(theTime.sSec,"%d",t.ti_sec); sprintf(theTime.time,"%02d:%02d:%02d %s",t.ti_hour,t.ti_min,t.ti_sec,theTime.AmPm);
setcolor(LIGHTBLUE); setcolor(WHITE); setfillstyle(1,LIGHTGRAY); bar(5,0,10+strlen(theTime.time)*10,30); rectangle(5,0,10+strlen(theTime.time)*10,30); setfillstyle(1,BLUE); bar(7,1,8+strlen(theTime.time)*10,10); rectangle(7,1,8+strlen(theTime.time)*10,10); setcolor(DARKGRAY); line(5,30,10+strlen(theTime.time)*10,30); line(5,0,5,30); line(7,1,8+strlen(theTime.time)*10,1); line(8+strlen(theTime.time)*10,1,8+strlen(theTime.time)*10,10); settextstyle(0,0,1); setcolor(BLACK); outtextxy(10,15,theTime.time); setcolor(CYAN); outtextxy(10,maxy-20,"Press any key to exit..."); setvisualpage(page); page=1-page; delay(50); } getch(); closegraph(); }
Yes, the code got long, but there is little to be explained actually. Here are the graphics commands made available by **graphics.h**
arc bar bar3d circle cleardevice clearviewport closegraph detectgraph drawpoly ellipse fillellipse fillpoly floodfill getarccoords getaspectratio getbkcolor getcolor getdefaultpalette getdrivername getfillpattern getfillsettings getgraphmode getimage getlinesettings getmaxcolor getmaxmode getmaxx getmaxy getmodename getmoderange getpalette getpalettesize getpixel gettextsettings getviewsettings getx gety graphdefaults grapherrormsg _graphfreemem _graphgetmem graphresult imagesize initgraph installuserdriver installuserfont line linerel lineto moverel moveto outtext outtextxy pieslice putimage putpixel rectangle registerbgidriver registerfarbgidriver registerbgifont registerfarbgifont restorecrtmode sector setactivepage setallpalette setaspectratio setbkcolor setcolor setfillpattern setfillstyle setgraphbufsize setgraphmode setlinestyle setpalette setrgbpalette settextjustify settextstyle setusercharsize setviewport setvisualpage setwritemode textheight textwidth
Roughly as long as the TK2 library. Don't expect me to discuss them all though. Maybe on another time.
-Sets the line color to light blue. Previous tutorial enumerates all 16 default colors in C. -Applies to putpixel(), line(), and outtext(), rectangle(), ellipse(), etc.. -Sets the fill style to 1(solid fill) and color to light gray -Applies to bar(), fillellipse(), fillpoly(), etc.. -Draws and fills a rectangular region following the current fill settings described by the most recent cal to setfillstyle() -First two parameters are the x, y location of the upper-left corner; 3rd and 4th parameters describes the coordinates (x,y) of the lower-right corner. -Draws and a rectangular region following the current line settings described by the most recent cal to setcolor() and setlinestyle() -First two parameters are the x, y location of the upper-left corner; 3rd and 4th parameters describes the coordinates (x,y) of the lower-right corner. -Draws a line from x1,y1 to x2,y2. Appearance depends on setlinestyle() and setcolor() calls. -Sets the text style. Loads a predefined Font(non-TTF compatible). Orientation may be either 0 or 1; size may vary. -Outputs text on a specified x,y coordinate. Draws and fills an ellipse with its center at (centerx,centery). The horizontal radius is described by xradius while the yradius parameter refers to the vertical radius. A perfect circle should have xradius=yradius. Border color depends on a previous call to setcolor(), fill color and style depends on a previous call to setfillstyle(). Effective for certain graphics drivers only. It sets which page is visible to the user. VGA cards running on VGAMED mode have 2 pages. In this case, page may either be 0 or 1. -Sets the active page to which all graphics output shall be directed. Not neccessarily the visible page. setcolor(LIGHTBLUE);
setfillstyle(1,LIGHTGRAY);
bar(x1,y1,x2,y2);
rectangle(x1,y1,x2,y2);
line(x1,y1,x2,y2);
settextstyle(Font,Orientation,Size);
outtextxy(x,y,"text");
fillellipse(centerx,centery,xradius,yradius); -
setvisualpage(page); -
setactivepage(page)
Here's the output of the program so far...
![](library/images/docs/283.gif)
*Image resized for better viewing*
Hopefully you've learned something in this tutorial. We'll pause here for a while so that I'll have something more to write next week. Next week we're going to discuss in detail about making an analog clock. The difference simply lies on the presentation anyway. The way of retrieveing system time will stay the same.
Colin
January 26, 2005, 10:36 am
I can't think of very many langauges that let you set strings with "=". C++'s std::string, all .NET's system::string, but those are classes, not languages.
Icbim
February 18, 2005, 10:25 pm
wow a clock would really help for event planning
Khin takes a break from the sprite tutorial to go back to his Turbo C++ development, this time creating a digital and analog clock.
Mar 30, '05
Mar 1, '05
Feb 22, '05
Feb 8, '05
Jan 11, '05
Sep 1, '05
Jul 11, '05
Mar 30, '05
Mar 1, '05
Feb 22, '05
