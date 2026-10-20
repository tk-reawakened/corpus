---
kind: doc
id: "toolkitzone.com/189"
site: "toolkitzone.com"
title: "Creating An Analog Clock"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=189"
written: "2005-03-01T17:46:00"
date_confidence: "exact"
updated: null
captured: ["20060313225810", "20060612052711"]
author: "Khin"
repliers: []
authors: ["Khin"]
comments_present: 0
f_author: "Khin"
f_date: "March 1, 2005, 5:46 pm"
f_description: "Khin completes tutorial for creating a digital clock in Turbo C/C++, as well as with Java and Visual Basic."
f_section: "Creativity > Khin's Desk"
f_title: "Analog Clock Tutorial"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_view_cadd_doc_189", captured: "20060313225810", sha256: "392aa123cdc63fc589bd6fbf5967a43cab9bc45026a24e353e1cd57938c9400e", wayback_url: "https://web.archive.org/web/20060313225810/http://toolkitzone.com:80/library.php?mode=read&view=cadd&doc=189&PHPSESSID=bdcceeefceef8ff863ad82d0d089ece4"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_189", captured: "20060612052711", sha256: "ba5ab59117f4fe4679e45fccb30af1453e4434f9e9dff44b341c273f64bc3bff", wayback_url: "https://web.archive.org/web/20060612052711/http://www.toolkitzone.com/library.php?mode=read&doc=189"}
---

# Creating An Analog Clock

Finally I've had enough time to continue and finish off my Clock Making Tutorial. Last time we finished creating a digital clock using Turbo C/C++. This time around we're going to make an analog clock using the same compiler plus I'll show a similar example of how to do it with Java and Visual Basic. Okay, first you'll need to review the Pythagorean Theorem. Yes, like I said before there's going to be geometry/trigonometry here. It's simply inevitable. Yes, you may not like it, and believe me I don't have that much interest in math but we cannot avoid it in programming , just as a paper is indispensable to an artist.
![](library/images/docs/510.gif)
Remember the equations well, because we'll need them later! Now why did I ask you to remember them? Observe this:
![](library/images/docs/511.gif)
Concentrating on just a hand of a clock, you'll notice that as it moves clockwise, it forms a right triangle in this manner:
![](library/images/docs/512.gif)
Showing more lapses, you'll notice that the angle to which the hand moves is constant. This makes it easier for us to calculate the remaining variables. Let's transfer to the program and leave math for a while. In Turbo C, drawing a line is possible through the command line(x1, y1, x2, y2); where x1 and y1 are the first point source and x2, y2 are the second point source. As you can see, that's all we need to supply in order to draw a line. the problem is, how do we draw the line based on the info we had? Well it is quite easy to get one point source. All of the clock's hands one end are at the center of the clock itself, so there we have it-- our x1, y1 could be any number that would make one point of our line get drawn at a desired location. The problem now is the other point (x2, y2) because it changes, and we wouldn't know exactly where they should get drawn. To make matters worse, they must be kept within a circular path, so a linear equation will not do to compute for the endpoint. This is where our equation comes in. Observe this drawing:
![](library/images/docs/513.gif)
Hmmmm...what can we make of this? Like I said before, we already have x1, y1, now recall that we also found out that the angle (theta) to which the hand moves is constant, so that another variable we could use. What's the value you ask? Well a whole circle is 360 deg, and our hand, supposing this is either the second or the minute hand, will complete the circle at 60 ticks. To get the theta, just divide 360 by 60. 360 / 60 = 6. that means that each time, the hand will move 6 degrees. For the hour hand that would be 360 / 12 = 30 degrees. Going back to the equation, we have yet another constant value! We get to decide how long the line would be(r), so there's another constant value we obtained. The equation is now complete.
y = r sin (theta) x = r cos (theta)
We get to supply r and theta, so the rest is just direct substitution. Turbo C offers math functions(included in Math.h) like sin() and cos(). We simply use them as the equation above appeared.
double cos(double x); double sin(double x);
Where x is the angle required for the computation. Take note that they should be in radian. Wait, now what is radian? You see all this time that we are discussing the program, we are referring to theta(the angle) in degrees(as in 30 deg, 6 deg). The trouble with this is that these C funstions will compute based on the given value in radian. Don't worry. We simply convert the theta to radian. We use this equation:
rad = (deg * PI) / 180
Simply multiply our theta with PI(3.14159) then divide the product with 180. The resulting radian number can then be supplied as the argument to the sin() and cos() functions.
Alright, let's put this into code. Here is the code fragment for computing and displaying the second clock hand:
y = 80 * sin(t.ti_sec * 6/57.32); x = 80 * cos(t.ti_sec * 6/57.32); setcolor(BLACK); setlinestyle(0, 1, 1); line(maxx / 2, maxy / 2, maxx / 2 + y, maxy / 2 - x);
Let's analyze this. y -> the y-coordinate of the second endpoint that we need 80 -> the desired length of the hand(r) t.ti_sec -> retrieved by using Turbo C's time manipulation function. Details can be found on the PREVIOUS TUTORIAL. A variable that changes constantly, causing the result to change. Without it, the result would remain the same throughout. 6 -> the constant angle to which the second hand moves 57.32 -> PI / 180 maxx, maxy -> discussed in the PREVIOUS TUTORIAL maxx / 2 -> the desired x1 location. Basically the middle of the screen maxy / 2 -> the desired maxy location. Basically the middle of the screen maxx / 2 + y -> desired x2 location. The computed y value is added to it to determine the endpoint. maxx / 2 - x -> desired y2 location. The computed x value is added to it to determine the endpoint.
Wait a minute, why is the y value added to the x2 coordinate? Because by nature, we are viewing our triangle in a rotated angle. In the original formula, the triangle is viewed as this:
![](library/images/docs/510.gif)
While in our program, the triangle formed looks like this:
![](library/images/docs/513.gif)
Now why is the x value subtracted from the y2 coordinate? Because by default, the angle of rotation in mathematics forms a complete revolution (360 deg) in counter-clockwise direction. Since we are running in clockwise direction, we must reverse the polarity.
And now, for the rest of the program. The same logic is applied to the minute and hour hand, with the hour hand slightly different in terms of angle.
The Code Fragment for the Analog Clock
//---------------draw the clock's body/frame-----------------//
setlinestyle(0, 1, 1); setfillstyle(1, RED); setcolor(LIGHTRED); fillellipse(maxx / 2, maxy / 2, 150, 110); setlinestyle(0, 1, 3); setcolor(DARKGRAY); setfillstyle(1, WHITE); fillellipse(maxx / 2, maxy / 2, 140, 102); setcolor(LIGHTGRAY); ellipse(maxx / 2, maxy / 2, 180, 360, 140, 102); setcolor(BLACK); settextstyle(TRIPLEX_FONT, 0, 1); outtextxy(maxx / 2 - strlen("S I K O") * 8 / 2, maxy / 2 - 50, "S I K O"); settextstyle(GOTHIC_FONT, 0, 1); outtextxy(maxx / 2 - 10, maxy / 2 - 100, "12"); outtextxy(maxx / 2 - 10, maxy / 2 + 80, "6"); outtextxy(maxx / 2 - 130, maxy / 2 - 13, "9"); outtextxy(maxx / 2 + 120, maxy / 2 - 13, "3");
//--------------compute for the second hand and draw it-----------------//
y = 80 * sin(t.ti_sec * 6 / 57.32); x = 80 * cos(t.ti_sec * 6 / 57.32); setcolor(BLACK); setlinestyle(0, 1, 1); line(maxx / 2, maxy / 2, maxx / 2 + y, maxy / 2 - x);
//--------------compute for the minute hand and draw it-----------------//
y = 85 * sin(t.ti_min * 6 / 57.32); x = 85 * cos(t.ti_min * 6 / 57.32); setcolor(LIGHTBLUE); setlinestyle(0, 1, 3); line(maxx / 2, maxy / 2, maxx / 2 + y, maxy / 2 - x);
//--------------compute for the hour hand and draw it-----------------//
y = 105 * sin(t.ti_hour * 30 / 57.32); x = 105 * cos(t.ti_hour * 30 / 57.32); setcolor(RED); setlinestyle(0, 1, 3); line(maxx / 2, maxy / 2, maxx / 2 + y, maxy / 2 - x);
//--------------some more clock decor-----------------//
setlinestyle(0, 1, 1); setcolor(BLACK); setfillstyle(1, LIGHTGRAY); fillellipse(maxx / 2, maxy / 2, 10, 7); setfillstyle(1, WHITE); setcolor(LIGHTGRAY); fillellipse(maxx / 2 + 3, maxy / 2 - 2, 6, 3);
Let's rewrite the whole program and add this fragment to our previously created program.
The Finished Clock Program
#include #include
#include
#include
#include
#include
struct timeStruct{ char sHour[3], sMin[3], sSec[3], AmPm[3]; char time[20]; };
int maxx, maxy;
int main(){ struct time t; struct timeStruct theTime; int gdriver = VGA,gmode = VGAMED, errorcode, page = 0; initgraph(&gdriver, &gmode, "c:\\tc\\bgi"); errorcode = graphresult(); if(errorcode != grOk){ printf("Graphics error: %s\n", grapherrormsg(errorcode)); printf("Press any key to halt:"); getch(); return 0; } maxx = getmaxx(); maxy = getmaxy(); int x, y, ctr; char buffer[50]; while(!kbhit()){ setactivepage(page); //--draw on this active page gettime(&t); if(t.ti_hour == 0)t.ti_hour = 12; if(t.ti_hour > 12){ t.ti_hour -= 12; strcpy(theTime.AmPm, "PM"); } else{ strcpy(theTime.AmPm, "AM"); } sprintf(theTime.sHour, "%d", t.ti_hour); sprintf(theTime.sMin, "%d", t.ti_min); sprintf(theTime.sSec, "%d", t.ti_sec); sprintf(theTime.time, "%02d:%02d:%02d %s", t.ti_hour, t.ti_min, t.ti_sec, theTime.AmPm);
setcolor(LIGHTBLUE); setcolor(WHITE); setfillstyle(1, LIGHTGRAY); bar(5, 0, 10 + strlen(theTime.time) * 10, 30); rectangle(5, 0, 10 + strlen(theTime.time) * 10, 30); setfillstyle(1, BLUE); bar(7, 1, 8 + strlen(theTime.time) * 10, 10); rectangle(7, 1, 8 + strlen(theTime.time) * 10, 10); setcolor(DARKGRAY); line(5, 30, 10 + strlen(theTime.time) * 10, 30); line(5, 0, 5, 30); line(7, 1, 8 + strlen(theTime.time) * 10, 1); line(8 + strlen(theTime.time) * 10, 1, 8 + strlen(theTime.time) * 10, 10); settextstyle(0, 0, 1); setcolor(BLACK); outtextxy(10, 15, theTime.time); setcolor(CYAN); outtextxy(10, maxy - 20, "Press any key to exit...");
//---------------draw the clock's body/frame-----------------//
setlinestyle(0, 1, 1); setfillstyle(1, RED); setcolor(LIGHTRED); fillellipse(maxx / 2, maxy / 2, 150, 110); setlinestyle(0, 1, 3); setcolor(DARKGRAY); setfillstyle(1, WHITE); fillellipse(maxx / 2, maxy / 2, 140, 102); setcolor(LIGHTGRAY); ellipse(maxx / 2, maxy / 2, 180, 360, 140, 102); setcolor(BLACK); settextstyle(TRIPLEX_FONT, 0, 1); outtextxy(maxx / 2 - strlen("S I K O") * 8 / 2, maxy / 2 - 50, "S I K O"); settextstyle(GOTHIC_FONT, 0, 1); outtextxy(maxx / 2 - 10, maxy / 2 - 100, "12"); outtextxy(maxx / 2 - 10, maxy / 2 + 80, "6"); outtextxy(maxx / 2 - 130, maxy / 2 - 13, "9"); outtextxy(maxx / 2 + 120, maxy / 2 - 13, "3");
//--------------compute for the second hand and draw it-----------------//
y = 80 * sin(t.ti_sec * 6 / 57.32); x = 75 * cos(t.ti_sec * 6 / 57.32); setcolor(BLACK); setlinestyle(0, 1, 1); line(maxx / 2, maxy / 2, maxx / 2 + y, maxy / 2 - x);
//--------------compute for the minute hand and draw it-----------------//
y = 85 * sin(t.ti_min * 6 / 57.32); x = 70 * cos(t.ti_min * 6 / 57.32); setcolor(LIGHTBLUE); setlinestyle(0, 1, 3); line(maxx / 2, maxy / 2, maxx / 2 + y, maxy / 2 - x);
//--------------compute for the hour hand and draw it-----------------//
y = 105 * sin(t.ti_hour * 30 / 57.32); x = 90 * cos(t.ti_hour * 30 / 57.32); setcolor(RED); setlinestyle(0, 1, 3); line(maxx / 2, maxy / 2, maxx / 2 + y, maxy / 2 - x);
//--------------some more clock decor-----------------//
setlinestyle(0, 1, 1); setcolor(BLACK); setfillstyle(1, LIGHTGRAY); fillellipse(maxx / 2, maxy / 2, 10, 7); setfillstyle(1, WHITE); setcolor(LIGHTGRAY); fillellipse(maxx / 2 + 3, maxy / 2 - 2, 6, 3);
setvisualpage(page); //--now show the page after the drawing is done page = 1 - page; //--flip the page so that we can draw on the hidden one delay(50); } getch(); closegraph(); return 0; }
By the way, if you have Turbo C++ and indeed run this program, you'll notice that the clock is like a flattened oval. This is because of the aspect ratio cause by the VGA resolution. Simply adjust the coordinates until you become satisfied.
Output:
![](library/images/docs/516.gif)
Here's the same program using Java.
The Clock Program in Java(Applet)
import java.awt.*; import java.applet.*; import java.util.*;
public class JavaClock extends Applet implements Runnable { //---Class definition for the Clock---// class CLOCK{ int hour, minute, second; int hX, hY; //--hour endpoint int mX, mY; //--minutes endpoint int sX, sY; //--seconds endpoint } //---Global variables---// CLOCK theClock; Thread runner; String strTime, AmPm; Image offImg; Graphics off; int maxx, maxy; Date today = new Date(); public void start(){ if(runner == null){ runner = new Thread(this); runner.start(); } } public void stop(){ if(runner != null){ runner.stop(); runner = null; } } //---this method is the workhorse of the program, so we put the conputations here---// public void run(){ while(true){ today = new Date(); //--Initiate the system Date theClock.hour = today.getHours(); //--Get the current hour theClock.minute = today.getMinutes(); //--Get the current minute theClock.second = today.getSeconds(); //--Get the current second //-----Format the necessary strings--------// AmPm = "AM"; if(theClock.hour > 12){ theClock.hour -= 12; AmPm = "PM"; } strTime = theClock.hour + ":" + today.getMinutes() + ":" + today.getSeconds() + " " + AmPm; //----precompute the coordinates of the respective endpoints------// theClock.hX = (int)(50.0f * Math.cos(theClock.hour * 30 / 57. 32)); theClock.hY = (int)(50.0f * Math.sin(theClock.hour * 30 / 57.32)); theClock.mX = (int)(60.0f * Math.cos(theClock.minute * 6 / 57.32)); theClock.mY = (int)(60.0f * Math.sin(theClock.minute * 6 / 57.32)); theClock.sX = (int)(70.0f * Math.cos(theClock.second * 6 / 57.32)); theClock.sY = (int)(70.0f * Math.sin(theClock.second * 6 / 57.32)); repaint(); delay(30); } } public void init(){ maxx = size().width; maxy = size().height; offImg = createImage(maxx, maxy); off = offImg.getGraphics(); theClock = new CLOCK(); }
public void paint(Graphics out){ try{ //Erase the canvas off.setColor(new Color(120, 200, 200)); off.fillRect(0, 0, maxx, maxy); //Write the system time off.setFont(new Font("Verdana", Font.BOLD, 15)); off.setColor(Color.WHITE); off.drawString(strTime, 10, 20 ); off.setColor(Color.BLACK); off.drawString(strTime, 11, 19 ); //Draw the clock off.setColor(Color.BLACK); off.fillOval(maxx / 2 - 101, maxy / 2 - 101, 202, 202); off.setColor(Color.RED); off.fillOval(maxx / 2 - 100, maxy / 2 - 100, 200, 200); off.setColor(new Color(100,0,0)); off.fillOval(maxx / 2 - 90, maxy / 2 - 90, 180, 180); off.setColor(new Color(152, 152, 152)); off.fillOval(maxx / 2 - 85, maxy / 2 - 85, 170, 170); off.setColor(Color.WHITE); off.fillOval(maxx / 2 - 80, maxy / 2 - 80, 160, 160); off.setColor(new Color(100, 100, 100)); off.fillOval(maxx / 2 - 78, maxy / 2- 78, 156, 156); off.setColor(Color.WHITE); off.fillOval(maxx / 2 - 75, maxy / 2 - 75, 150, 150); off.setColor(Color.BLACK); off.setFont(new Font("Times New Roman", Font.BOLD, 15)); off.drawString("12", maxx / 2 - 7, maxy / 2 - 60); off.drawString("3", maxx / 2 + 60, maxy / 2 + 7); off.drawString("6", maxx / 2 - 7, maxy / 2 + 70); off.drawString("9", maxx / 2 - 70, maxy / 2 + 7); //Draw the hands off.setColor(Color.BLACK); off.drawLine(maxx / 2, maxy / 2, maxx / 2 + theClock.hY, maxy / 2 - theClock.hX); off.fillOval(maxx / 2 + theClock.hY - 3, maxy / 2 - theClock.hX - 3, 6, 6); off.setColor(Color.RED); off.drawLine(maxx / 2, maxy / 2, maxx / 2 + theClock.mY, maxy / 2 - theClock.mX); off.fillOval(maxx / 2 + theClock.mY - 3, maxy / 2 - theClock.mX - 3, 6, 6); off.setColor(Color.BLUE); off.drawLine(maxx / 2, maxy / 2, maxx / 2 + theClock.sY, maxy / 2 - theClock.sX); off.fillOval(maxx / 2 + theClock.sY - 3, maxy / 2 - theClock.sX - 3, 6, 6); off.setColor(new Color(130, 130, 130)); off.fillOval(maxx / 2 - 5, maxy / 2 - 5, 10, 10); off.setColor(new Color(200, 200, 200)); off.fillOval(maxx / 2 - 2, maxy / 2 - 5, 7, 7); out.drawImage(offImg, 0, 0, this); }catch(Exception e){} } public void update(Graphics out){ paint(out); } public void delay(int milli){ try{ Thread.sleep(milli); }catch(Exception e){} } }
Output:
![](library/images/docs/514.gif)
Here's the same program using Visual Basic and its simplistic shapes and drawing methods. No advanced concepts like DirectX or Win32 GDI applied.
Clock program in Visual Basic
Option Explicit Dim theClock As CLOCK Dim theTime As Date
Private Sub cmdExit_Click() End End Sub
Private Sub Form_Activate() tmrTime_Timer End Sub
'Manually call the timer upon form activation
Private Sub Form_Load() Me.tmrTime.Enabled = True End Sub
Private Sub tmrTime_Timer() theTime = Time theClock.hour = DateTime.hour(Time) theClock.min = DateTime.Minute(Time) theClock.sec = DateTime.Second(Time) If theClock.hour > 12 Then theClock.hour = theClock.hour - 12 theClock.AmPm = "PM" Else theClock.AmPm = "AM" End If lblTime.Caption = theClock.hour & ":" & theClock.min & ":" & theClock.sec & " " & theClock.AmPm Caption = "VB CLock - [" & theClock.hour & ":" & theClock.min & ":" & theClock.sec & " " & theClock.AmPm & "]" theClock.hX = 50 * Cos(theClock.hour * 30 / 57.32) theClock.hY = 50 * Sin(theClock.hour * 30 / 57.32) theClock.sX = 65 * Cos(theClock.sec * 6 / 57.32) theClock.sY = 65 * Sin(theClock.sec * 6 / 57.32) theClock.mX = 60 * Cos(theClock.min * 6 / 57.32) theClock.mY = 60 * Sin(theClock.min * 6 / 57.32) linHour.X2 = linHour.X1 + theClock.hY linHour.Y2 = linHour.Y1 - theClock.hX linSecond.X2 = linSecond.X1 + theClock.sY linSecond.Y2 = linSecond.Y1 - theClock.sX linMinute.X2 = linMinute.X1 + theClock.mY linMinute.Y2 = linMinute.Y1 - theClock.mX End Sub
'Get the time
'Format the time manually
'Update the display
'Compute for the X2,Y2 positions of each clock hand
'Update the coordinates
Output:
![](library/images/docs/515.gif)
Here's the text file for the form I used in VB, so you could use as reference when putting the needed components:
The frmClock.frm Form in ASCII text
VERSION 5.00 Begin VB.Form frmClock BorderStyle = 1 'Fixed Single Caption = "VB Clock - []" ClientHeight = 4470 ClientLeft = 45 ClientTop = 330 ClientWidth = 5790 LinkTopic = "Form1" MaxButton = 0 'False MinButton = 0 'False ScaleHeight = 298 ScaleMode = 3 'Pixel ScaleWidth = 386 StartUpPosition = 3 'Windows Default Begin VB.CommandButton cmdExit Caption = "E&xit" BeginProperty Font Name = "Verdana" Size = 9 Charset = 0 Weight = 700 Underline = 0 'False Italic = 0 'False Strikethrough = 0 'False EndProperty Height = 495 Left = 4440 TabIndex = 5 Top = 3840 Width = 1215 End Begin VB.Timer tmrTime Enabled = 0 'False Interval = 1000 Left = 0 Top = 3960 End Begin VB.Shape Shape2 BackColor = &H00C0C0C0& BackStyle = 1 'Opaque Height = 255 Left = 2760 Shape = 3 'Circle Top = 2040 Width = 255 End Begin VB.Label lblTime AutoSize = -1 'True BackStyle = 0 'Transparent Caption = "0:0:0 PM" BeginProperty Font Name = "Verdana" Size = 12 Charset = 0 Weight = 700 Underline = 0 'False Italic = 0 'False Strikethrough = 0 'False EndProperty Height = 270 Left = 240 TabIndex = 4 Top = 240 Width = 1155 End Begin VB.Label Label4 AutoSize = -1 'True BackStyle = 0 'Transparent Caption = "9" BeginProperty Font Name = "Times New Roman" Size = 9.75 Charset = 0 Weight = 700 Underline = 0 'False Italic = 0 'False Strikethrough = 0 'False EndProperty Height = 225 Left = 1800 TabIndex = 3 Top = 2040 Width = 105 End Begin VB.Label Label3 AutoSize = -1 'True BackStyle = 0 'Transparent Caption = "3" BeginProperty Font Name = "Times New Roman" Size = 9.75 Charset = 0 Weight = 700 Underline = 0 'False Italic = 0 'False Strikethrough = 0 'False EndProperty Height = 225 Left = 3840 TabIndex = 2 Top = 2040 Width = 105 End Begin VB.Label Label2 AutoSize = -1 'True BackStyle = 0 'Transparent Caption = "6" BeginProperty Font Name = "Times New Roman" Size = 9.75 Charset = 0 Weight = 700 Underline = 0 'False Italic = 0 'False Strikethrough = 0 'False EndProperty Height = 225 Left = 2760 TabIndex = 1 Top = 3120 Width = 105 End Begin VB.Label Label1 AutoSize = -1 'True BackStyle = 0 'Transparent Caption = "12" BeginProperty Font Name = "Times New Roman" Size = 9.75 Charset = 0 Weight = 700 Underline = 0 'False Italic = 0 'False Strikethrough = 0 'False EndProperty Height = 225 Left = 2760 TabIndex = 0 Top = 1200 Width = 210 End Begin VB.Line linSecond BorderColor = &H00FF0000& BorderWidth = 2 X1 = 192 X2 = 224 Y1 = 144 Y2 = 88 End Begin VB.Line linMinute BorderColor = &H000000FF& BorderWidth = 2 X1 = 192 X2 = 200 Y1 = 144 Y2 = 88 End Begin VB.Line linHour BorderWidth = 2 X1 = 192 X2 = 192 Y1 = 144 Y2 = 104 End Begin VB.Shape shpClock BackStyle = 1 'Opaque Height = 2295 Left = 1560 Shape = 3 'Circle Top = 1080 Width = 2655 End Begin VB.Shape Shape1 BackColor = &H000000FF& BackStyle = 1 'Opaque Height = 2775 Left = 1320 Shape = 3 'Circle Top = 840 Width = 3135 End End Attribute VB_Name = "frmClock" Attribute VB_GlobalNameSpace = False Attribute VB_Creatable = False Attribute VB_PredeclaredId = True Attribute VB_Exposed = False Option Explicit Dim theClock As CLOCK Dim theTime As Date
Private Sub cmdExit_Click() End End Sub
Private Sub Form_Activate() 'Manually call the timer upon form activation tmrTime_Timer End Sub
Private Sub Form_Load() Me.tmrTime.Enabled = True End Sub
Private Sub tmrTime_Timer() 'Get the time theTime = Time theClock.hour = DateTime.hour(Time) theClock.min = DateTime.Minute(Time) theClock.sec = DateTime.Second(Time) 'Format it time manually If theClock.hour > 12 Then theClock.hour = theClock.hour - 12 theClock.AmPm = "PM" Else theClock.AmPm = "AM" End If 'Update the display lblTime.Caption = theClock.hour & ":" & theClock.min & ":" & theClock.sec & " " & theClock.AmPm Caption = "VB CLock - [" & theClock.hour & ":" & theClock.min & ":" & theClock.sec & " " & theClock.AmPm & "]" 'Compute for the X2,Y2 positions of each clock hand theClock.hX = 50 * Cos(theClock.hour * 30 / 57.32) theClock.hY = 50 * Sin(theClock.hour * 30 / 57.32) theClock.sX = 65 * Cos(theClock.sec * 6 / 57.32) theClock.sY = 65 * Sin(theClock.sec * 6 / 57.32) theClock.mX = 60 * Cos(theClock.min * 6 / 57.32) theClock.mY = 60 * Sin(theClock.min * 6 / 57.32) 'Update the coordinates linHour.X2 = linHour.X1 + theClock.hY linHour.Y2 = linHour.Y1 - theClock.hX linSecond.X2 = linSecond.X1 + theClock.sY linSecond.Y2 = linSecond.Y1 - theClock.sX linMinute.X2 = linMinute.X1 + theClock.mY linMinute.Y2 = linMinute.Y1 - theClock.mX End Sub
See? When you've done it in a programming language, you basically can do them on any other language provided they can supply the tools you require. I'd love to show a similar program done in Assembly, but that's very long. Plus Assembly is too technical; might get boring for some ;)
For questions, comments, or reactions, just PM me, e-mail me at (redacted: email) or simply contact me through TKZ.
Khin completes tutorial for creating a digital clock in Turbo C/C++, as well as with Java and Visual Basic.
Mar 30, '05
Feb 22, '05
Feb 8, '05
Jan 25, '05
Jan 11, '05
Sep 1, '05
Jul 11, '05
Mar 30, '05
Feb 22, '05
Feb 8, '05
