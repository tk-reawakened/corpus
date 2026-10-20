---
kind: doc
id: "toolkitzone.com/64"
site: "toolkitzone.com"
title: "Colin"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=64"
written: "2004-11-30T22:55:00"
date_confidence: "exact"
updated: null
captured: ["20041216141241", "20041216141241", "20060507122959"]
author: "Colin"
repliers: []
authors: ["Colin"]
comments_present: 0
f_author: "Colin"
f_date: "November 30, 2004, 10:55 pm"
f_description: "Detailed overview of the forthcoming object orientated capabilities from the 3.0.5 release onwards. A must read for budding and experienced programmers alike, as well as those who just want to further their knowledge alongside Colin's weekly columns on the subject."
f_section: "RPG Code"
f_title: "RPGCode OOP Overview"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_64", captured: "20041216141241", sha256: "e0aa06fae6b988a83d28841463dbfc97fbcebbcd1a820aa847f7bd9a9f84f81a", wayback_url: "https://web.archive.org/web/20041216141241/http://toolkitzone.com/library.php?mode=read&doc=64"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_64-3e5fcf", captured: "20041216141241", sha256: "e0aa06fae6b988a83d28841463dbfc97fbcebbcd1a820aa847f7bd9a9f84f81a", wayback_url: "https://web.archive.org/web/20041216141241/http://www.toolkitzone.com/library.php?mode=read&doc=64"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_view_cadd_doc_64", captured: "20060507122959", sha256: "e2c323839c4f14eb47678dcafe6860f839da80d02cdf32e7414e7ddca38e3686", wayback_url: "https://web.archive.org/web/20060507122959/http://www.toolkitzone.com:80/library.php?mode=read&view=cadd&doc=64&PHPSESSID=41f26e06b8b6a891a15d685e59e58c0d"}
---

# Colin

Detailed overview of the forthcoming object orientated capabilities from the 3.0.5 release onwards. A must read for budding and experienced programmers alike, as well as those who just want to further their knowledge alongside Colin's weekly columns on the subject.
**Object Oriented Programming in RPGCode** Yes, it's the day we all thought would never come object oriented programming in the RPGToolkit 3's internal scripting language RPGCode. Unlike the weak design you saw at 3.03's release, you'll be pleased to find RPGC3 has almost become a language separate from its predecessor. Such an improvement means new features like references, inherit ance, polymorphism and the like all of which, by the time you finish this document you will be able to use to your advantage.
**RPGCode Programming of the Old** RPGC3 attempts to provide new more intuitive ways to structure your code. For example, observe how you might code a date entity previously // February 22nd, 2004 -- date index 1 dateMonth[1]! = 2 dateDay[1]! = 22 dateYear[1]! = 2004 // Show the date showDate(1) // Method to show a date method showDate(idx!) { month[1]$ = "January" month[2]$ = "February" month[3]$ = "March" month[4]$ = "April" month[5]$ = "May" month[6]$ = "June" month[7]$ = "July" month[8]$ = "August" month[9]$ = "September" month[10]$ = "October" month[11]$ = "November" month[12]$ = "December" saveScreen() clear() pixelText(10, 7, month[dateMonth[idx!]!]$) pixelText(14 + getTextWidth(month[dateMonth[idx!]!]$), 7, _ CastLit(dateDay[idx!]!) + ", " + CastLit(dateYear[idx!]!)) wait() restoreScreen() }
While this approach may work, it has a number of flaws. First, and most serious, the names of the globals you use the set the date may not be easy to remember especially to programmers other than yourself who are trying to use your code. While you could create functions to set these vars, the resulting overhead would be unacceptable. And if you decided to change how a date was implemented at a later time, changing the globals used, for example, you would have to manually modify the code everywhere a date was used. What is needed is some way to keep the data and the functions surrounding it tightly knit.** Classes
**
Classes provide a way in which to define data and functions that operate on the data in one location. When you create a class, you are creating a new data type that can be created like any other type of variable (namely numerical and literal as RPGCode goes). ing classes, we could re-write the dat entity as follows: // A date class CDate { // Public visibility public: // Constructor method CDate(month!, day!, year!) // Display the date method display() // Private visibility private: m_month! // Month m_day! // Day m_year! // Year }
// CDate - constructor method CDate::CDate(month!, day!, year!) { // Copy over to members m_month! = month! m_day! = day! m_year! = year! } // Display the date method CDate::display() { month[1]$ = "January" month[2]$ = "February" month[3]$ = "March" month[4]$ = "April" month[5]$ = "May" month[6]$ = "June" month[7]$ = "July" month[8]$ = "August" month[9]$ = "September" month[10]$ = "October" month[11]$ = "November" month[12]$ = "December" saveScreen() clear() pixelText(10, 7, month[m_month!]$) pixelText(14 + getTextWidth(month[m_month!]$), 7, _ CastLit(m_day!) + ", " + CastLit(m_year!)) wait() restoreScreen() }
The code you see above may seem complicated, but really it's not. **class CDate** line defines a beginning a class CDate. Within a class we have two visibilities public and private. Using **public:** **private:** lines changes the current visibility. In the public visibility you should place the declarations of methods (and optionally their code, but this is not recommended for complicated classes), whereas the private visibility houses variables and functions that cannot be accessed from outside the class. **Special Class Methods****
There are several reserved functions that have special purposes.
method CDate(month!, day!, year!)
**constructor** is a function that is called when a new variable of type CDate is created (you still don't know a way to create such variables, see **Using Classes** for this information). This function is always named the same as the class itself. Its argument list is provided by the creator when the variable or object (an instance of a class), more specifically is created*
method ~CDate() This function the **deconstructor** was not required in the implementation of CDate, but takes the format **~className** and never has arguments. As the name insinuates, this function is called when an object of type CDate is destroyed. Note that the member variables still have their values when this function is called so you can use them in deinitialization tasks, they will not be killed until the call finishes. method release() **release** function is automatically a member of every class you need never code it. Calling the release function calls an object's deconstructor, kills its members variables, then the object itself. method getType() As with the last method, you should never provide code for **getType** , rather every class automatically has as a member This function returns the type of the object as a human readable, capital, string. **Using Classes****
**
Now that you know how to create classes, you'll need to know how to use them in your code. The most important task will be, of course, to create an object. This is accomplished by using the class' name as a function This returns object said typ calling its constructor with the arguments provided if it requires any. Armed with this function, you can now use the CDate class at a basic level: // Create a new date: January 31st, 2005 p =
CDate( 1, 31, 2005) // Display the date p->display() // Free the date p->release()
As you see, the **->** operator is used for calling class methods.
You'll note that object names do not contain a type declaration character. You can, however, append a **!** when referencing an object to obtain a unique number representing that object. This function may seem like all you need to operate your classes, but some potential problems exist.
**Overloading Operators** Say using the CDate class you wanted to reassign an object's date. You might think the following syntax would be legal: p = CDate 1, 31, 2005) // Later... p = CDate
2, 22, 1922) But all this does is reassigns **p** to a new object altogether; the original object still exists, but you can no longer access it this is called a memory leak. But what else can you do? You have no way to access the in dividual components of the date. et's remedy that now class CDate { // Public visibility public: // Constructor method CDate(month!, day!, year!) // Display the date method display() // Interface methods method getMonth() {returnMethod(m_month!)} method getDay() {returnMethod(m_day!} method getYear() {returnMethod(m_year!)} // Assignment operator method operator=(
otherDate ) // Private visibility private: m_month! // Month m_day! // Day m_year! // Year }
Since the three methods I've added are so short, I've simply placed their bodies in the actual class. Note that the **CDate** **display** methods are not shown again here, but they are still part of the class. You'll also have noticed that I've added the definition for a method we've not yet coded:
**operator=** . Methods named **operator*** where * is an operator allow you to code new behavior for operators when used on instances of a class. We'll implement **operator=** as follows: // CDate - assignment operator method CDate::operator=(otherDate) { // Check for correct type if (otherDate->getType() == CDATE) { // Copy the other date's members to this date m_month! = otherDate->getMonth() m_day! = otherDate->getDay()
m_year! = otherDate->g etYear() } }
Now the following is valid:
p = CDate 1, 31, 2005) // Later... x = CDate
2, 22, 1922) p = x! x->release()
There are a couple of things to note here.
**x!** rather than **x** is assigned to **p** This is because **x** has no numerical value (unless we code **operator!)**
We use a temporary variable to prevent memory lo ss. What if we wanted to display the date ourselves? We could create a function that returns a string and call it, but a more logical approach would be if we could som ehow make it possible to use the object where literal variables can be used. We'll place this in the public visibility of CDate:
// Cast to literal method operator$()
And for its implementation:
// CDate - cast to literal method CDate::operator$() { month[1]$ = "January" month[2]$ = "February" month[3]$ = "March" month[4]$ = "April" month[5]$ = "May" month[6]$ = "June" month[7]$ = "July" month[8]$ = "August" month[9]$ = "September" month[10]$ = "October" month[11]$ = "November" month[12]$ = "December" returnMethod(month[m_month!]$ + " " + CastLit(m_day!) + _ ", " + CastLit(m_year!) }
This makes the following code execute as desired:
p = CDate 1, 31, 2005) // Output p to the debug window debugger(p) p->release()
Note that only one of **operator$** **operator!** can be overloaded, at present. All operators, with the exception of **->** **.** can be overloaded.
**R** **eturning References** Arrays in RPGCode ha very limited functionality. They do not have set upper bounds and there are no functions to manipulate arrays. While coding an array class exceeds the scope of this document , returning references does not. When you overload **operator[]** you can only take one parameter the index in the array. People from structured programming backgrounds will find it impossible, therefore, to allow the creator to set items in the array . This, however, is not correct. When you return a reference, you make calling a function a synonym for the variable you return. Consider the following example: method someString() { returnMethod(&g_str$) } someString() = "Hello, world!" show(someString()) wait()
The syntax for using **returnMethod** this fashion is as seen above:
method returnMethod(&theVar)
Where **theVar** is a variable not a value that calling the fun ction will become a synonym Using this knowledge we can create a simple array class, like so:
// An array class CArray { // Public visibility public: // Constructor method CArray(upperBound!) // Subscript operator method operator[](idx!) // Get the upper bound method getBound() {returnMethod(m_bound!)} // Deconstructor method ~CArray() // Private visibility private: m_data[] // Main data m_bound! // Upper bound of the array } // CArray - constructor method CArray::CArray(upperBound!) { if (m_bound! >= 0) { // Bound is okay m_bound! = upperBound! } else { // Bound is no good debugger("Invalid upper bound: " + CastLit(upperBound!)) } } // CArray - subscript operator method CArray::operator[](idx!) { // Check bounds if (idx! <= m_bound! && idx! >= 0) { // Within bounds returnMethod(&m_data[idx!]) } else { // Out of bounds debugger("Out of array bounds: " + CastLit(idx!)) g_null! = 0 returnMethod(&g_null!) } } // CArray - deconstructor method CArray::~CArray() { On Error Resume Next
local(idx!) for (idx! = 0; idx! <= m_bound!; idx!++) { this[idx!]->release() } }
You may notice the use of **this** . Said, **this** , is just the current object, and, as you'd expect, **this!** is a unique number representing the object.
It's also worth nothing that the array index does not need to be numerical it can be literal, or even an object.
**CArray** class also shows an example of **composition** , that is, having objects as members of classes. This example which makes an array of dates, illustrates this:
// Create a new array array =
CArray( 1) // Fill it with two CDates array[0] =
CDate( 2, 12, 1234) array[1] =
CDate( 1, 1, 1 999 ) // Iterate over the array ub! = array->getBound() for (i! = 0; i! <= ub!; i!++) { // Show this date text(1, 1 + i!, array[i!]) }
// Wait for a key wait() // Clean up array->release() kill(i!,
ub!, array!) If you'll check back at CArray's deconstructor, you'll see that it releases its members automatically so we don't need to **release** the two dates. As you can see, returning references is a very powerful tool. **Polymorphism** Something you often need do in programming is express a relationship between types. Whether it be different types of numbers, jobs in an office, one class should be somehow expressed as a type of another.
In object oriented programming we often express this relationship using **inheritance** **inheritance** inheriting class or **derived** class obtains all the functions and variables of the class being inherit **base** class. In RPGCode, classes can have an unlimited number of bases and they are set like this: class CDerived [: CBaseOne, CBaseTwo, ...]
Take this number class, for example:
// A number class CNumber { // Public visibility public: // Constructor method CNumber(num) // Cast to numerical method operator!() {returnMethod(m_val!)} // Alter the number method operator=(newVal) // Private visibility private: m_val! // Value of the number } // CNumber - constructor method CNumber::CNumber(num) { // Copy value to a member
m_val! = num!
// CNumber - assignment operator method CNumber::operator=(newVal) { if (newVal->getType() == "") { // It's a number m_val! = newVal! } else { // It's an object -- hope for numerical cast m_val! = newVal } }
The CNumber class provides basic functionality for a number . It does not, however, have functions specific to the type of number being manipulated . If you want to manipulate a fraction, for example, you might code a class like this: // A fraction class CFraction: CNumber { // Public visibility public: // Constructor method CFraction(top!, bottom!) // Get the top method getTop() {returnMethod(m_top!)} // Get the bottom method getBottom() {returnMethod(m_bottom!)} // Override the = operator method operator=(newVal) // Private visibility private: m_top! // Top of the fraction m_bottom! // Bottom of the fraction } // CFraction - constructor method CFraction::CFraction(top!, bottom!) { // Copy params to members
m_top! = top! m_bottom! = bottom! m_val! = m_top! / m_bottom!
// CFraction - assignment operator method CFraction::operator=(newVal) { if (newVal->getType
== CFRACTION) { m_top! = newVal->getTop() m_bottom! = newVal->getBottom() // Also set the base class' value member m_val! = m_top! / m_bottom! } }
Note how the derived class can override the base class' methods. As shown, polymorphism makes it easy to express relationships between classes.
**Fin** What you've read over the last few pages represents incredible progress in RPGCode a language that once consisted of less than a dozen simple commands and only allowed numbered variables. RPGCode is growing up and I'm glad you could be a part of it!
Colin
December 1, 2004, 3:09 am
Please forgive any run-on sentences, my convertor stripped - and --. I'll fix that as soon as possible!
Mystinar
December 6, 2004, 1:09 am
I did not understand any of it. Will the help files include a more user-friendly tutorial? If not, I suggest it does.
Dec 12, '04
toolkit 3.x > tk3 amelioration
Dec 6, '04
toolkit 3.x > tk3 amelioration
Nov 28, '04
toolkit 3.x > tk3 amelioration
Nov 21, '04
toolkit 3.x > tk3 amelioration
