---
kind: doc
id: "toolkitzone.com/136"
site: "toolkitzone.com"
title: "Recent Forum Topics"
original_url: "http://toolkitzone.com/library.php?mode=read&doc=136"
written: "2005-01-08T14:37:00"
date_confidence: "exact"
updated: null
captured: ["20060312120229"]
author: "matt72186"
repliers: []
authors: ["matt72186"]
comments_present: 0
f_author: "matt72186"
f_date: "January 8, 2005, 2:37 pm"
f_description: "It's another class from Matt72186 on object-orientated programming with the Toolkit, concentrating on references and encapsulation this time around."
f_title: "References and Encapsulation"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_136", captured: "20060312120229", sha256: "44b7d3074bd9c1d3954c7789d4e9097c9fda18d1a6bbd52d084f557c94c10ee4", wayback_url: "https://web.archive.org/web/20060312120229/http://toolkitzone.com:80/library.php?mode=read&doc=136&PHPSESSID=bdcceeefceef8ff863ad82d0d089ece4"}
---

# Recent Forum Topics

-
RPG Code Class 1
References and Encapsulation
Posted By: Colin Posted By: reignofmagic **Recommended Links**
**Recent Forum Topics**
Today we are going to check out references. I will teach you what they are and how to use them. We will also go over a fundamental of object-oriented programming, known as encapsulation.
- As a pointer points, a reference, references a variable. **Reference**
- Encapsulation is a practice of object-oriented programming. It's purpose is to keep a class discrete and self-contained. It allows a class to be implemented and changed without affecting another class. **Encapsulation**
```
- Rectangle Class
- Public Scope
- Method Rectangle
- Method ResizeTo
- Method MoveTo
- Method ResizeBy
- Method MoveBy
- Private Scope
- Method refX1
- Method refY1
- Method refX2
- Method refY2
- Variable m_x1!
- Variable m_y1!
- Variable m_x2!
- Variable m_y2!
- Rectangle class
- public:
- Rectangle Method ( , , , ) x1! y1! x2! y2!
- ResizeTo Method ( , ) width! height!
- MoveTo Method ( , )
- ResizeBy Method ( , ) dwidth! dheight!
- MoveBy Method ( , ) dx! dy!
- private:
- refX1 Method
- refY1 Method
- refX2 Method
- refY2 Method
- m_x1!
- m_x2!
- m_y1!
- m_y2!
- ///////////////////////////
- // Rectangle Constructor
- ///////////////////////////
- Rectangle Rectangle Method ( , , , ) x1! y1! x2! y2!
- refX1() x1!
- refY1() y1!
- refX2() x2!
- refY2() y2!
- ///////////////////////////
- // Resize Rectangle To
- ///////////////////////////
- Rectangle ResizeTo Method ( , ) width! height!
- refX2() refX1() + width!
- refY2() refY1() + height!
- ///////////////////////////
- // Move Rectangle To
- ///////////////////////////
- Rectangle MoveTo Method ( , )
- = - refX1() dx!
- = - refY1() dy!
- MoveBy this ( , ) dx! dy!
- ///////////////////////////
- // Resize Rectangle By
- ///////////////////////////
- Rectangle ResizeBy Method ( , ) dwidth! dheight!
- refX2() refx2() + dwidth!
- refY2() refY2() + dheight!
- ///////////////////////////
- // Move Rectangle By
- ///////////////////////////
- Rectangle MoveBy Method ( , ) dx! dy!
- refX1() dx!
- refY1() dy!
- refX2() dx!
- refY2() dy!
- ///////////////////////////
- // Reference to X1
- ///////////////////////////
- Rectangle refX1 Method
- ReturnMethod( ) m_x1!
- ///////////////////////////
- // Reference to Y1
- ///////////////////////////
- Rectangle refY1 Method
- ReturnMethod( ) m_y1!
- ///////////////////////////
- // Reference to X2
- ///////////////////////////
- Rectangle refX2 Method
- ReturnMethod( ) m_x2!
- ///////////////////////////
- // Reference to Y2
- ///////////////////////////
- Rectangle refY2 Method
- ReturnMethod( ) m_y2!
- ///////////////////////////
```
Here we are creating a rectangle class. We define a few methods, that allow the initial variables of the class to be changed. We also have four private methods: refX1, refY1, refX2, and refY2. I'll go more into detail about them later.
```
- Rectangle class
- public:
- Rectangle Method ( , , , ) x1! y1! x2! y2!
- ResizeTo Method ( , ) width! height!
- MoveTo Method ( , )
- ResizeBy Method ( , ) dwidth! dheight!
- MoveBy Method ( , ) dx! dy!
- private:
- refX1 Method
- refY1 Method
- refX2 Method
- refY2 Method
- m_x1!
- m_x2!
- m_y1!
- m_y2!
```
You may or may not have noticed that all the variables here are private. This is a key piece to .encapsulation
First is the standard Constructor that every class will have, but wait, notice that none of the class variables are being directly accessed (m_x1!, m_y1!, m_x2!, m_y2!). Instead we are calling the private ref functions.
```
- ///////////////////////////
- // Rectangle Constructor
- ///////////////////////////
- Rectangle Rectangle Method ( , , , ) x1! y1! x2! y2!
- refX1() x1!
- refY1() y1!
- refX2() x2!
- refY2() y2!
```
These methods are pretty simple. They are just modifying the x1, y1, x2, and y2 variables in order to resize and move the rectangle. Pay attention still to the fact that none of the variables are being directly accessed.
```
- ///////////////////////////
- // Resize Rectangle To
- ///////////////////////////
- Rectangle ResizeTo Method ( , ) width! height!
- refX2() refX1() + width!
- refY2() refY1() + height!
- ///////////////////////////
- // Move Rectangle To
- ///////////////////////////
- Rectangle MoveTo Method ( , )
- = - refX1() dx!
- = - refY1() dy!
- MoveBy this ( , ) dx! dy!
- ///////////////////////////
- // Resize Rectangle By
- ///////////////////////////
- Rectangle ResizeBy Method ( , ) dwidth! dheight!
- refX2() refx2() + dwidth!
- refY2() refY2() + dheight!
- ///////////////////////////
- // Move Rectangle By
- ///////////////////////////
- Rectangle MoveBy Method ( , ) dx! dy!
- refX1() dx!
- refY1() dy!
- refX2() dx!
- refY2() dy!
```
Finally I get to explain what's going on here. Each "ref" method is using a ReturnMethod to return a variable of the class. The & operator that precedes each variable will return a to the variable, rather than a copy of it. What this accomplishes is that when the "ref" method is called, the variable it returns will pretend to be the actual variable. That is if you change anything about it, the variable will be affected. Also if you read it's data, it will be the same as the variable passed. So when refX1() is called, you're getting a to the class' m_x1! variable.referencereference
```
- ///////////////////////////
- // Reference to X1
- ///////////////////////////
- Rectangle refX1 Method
- ReturnMethod( ) m_x1!
- ///////////////////////////
- // Reference to Y1
- ///////////////////////////
- Rectangle refY1 Method
- ReturnMethod( ) m_y1!
- ///////////////////////////
- // Reference to X2
- ///////////////////////////
- Rectangle refX2 Method
- ReturnMethod( ) m_x2!
- ///////////////////////////
- // Reference to Y2
- ///////////////////////////
- Rectangle refY2 Method
- ReturnMethod( ) m_y2!
- ///////////////////////////
```
The reason we made these is to make work. By having methods like resize/move/ref we eliminate the need to ever access the actual variables. The key element here is that anyone who uses this class will only need to know that it works and what it can do. There is no need for anyone to care about how it does anything (other than for study purposes). At any time how the class works may be changed, but no matter what changes about how the class works, it should still get the same things done, without the person who uses it having to worry if it will break the code.encapsulation
Suppose we changed the class to store a rectangle by it's position and size rather than by the position of each corner. Is there a way we can completely change the way the class works, without breaking any other code that may already be using our old rectangle code?
```
- Rectangle Class
- Public Scope
- Method Rectangle
- Method ResizeTo
- Method MoveTo
- Method ResizeBy
- Method MoveBy
- Private Scope
- Method refX
- Method refY
- Method refWidth
- Method refHeight
- Variable m_x!
- Variable m_y!
- Variable m_width!
- Variable m_height!
- Rectangle class
- public:
- Rectangle Method ( , , , ) x1! y1! x2! y2!
- ResizeTo Method ( , ) width! height!
- MoveTo Method ( , )
- ResizeBy Method ( , ) dwidth! dheight!
- MoveBy Method ( , ) dx! dy!
- private:
- refX Method
- refY Method
- refWidth Method
- refHeight Method
- m_x!
- m_x!
- m_width!
- m_height!
- ///////////////////////////
- // Rectangle Constructor
- ///////////////////////////
- Rectangle Rectangle Method ( , , , ) x1! y1! x2! y2!
- refX() x1!
- refY() y1!
- refWidth() - x2! x1!
- refHeight() - y2! y1!
- ///////////////////////////
- // Resize Rectangle To
- ///////////////////////////
- Rectangle ResizeTo Method ( , ) width! height!
- refWidth() width!
- refHeight() height!
- ///////////////////////////
- // Move Rectangle To
- ///////////////////////////
- Rectangle MoveTo Method ( , )
- refX()
- refY()
- ///////////////////////////
- // Resize Rectangle By
- ///////////////////////////
- Rectangle ResizeBy Method ( , ) dwidth! dheight!
- refWidth() dwidth!
- refHeight() dheight!
- ///////////////////////////
- // Move Rectangle By
- ///////////////////////////
- Rectangle MoveBy Method ( , ) dx! dy!
- refX() dx!
- refY() dy!
- ///////////////////////////
- // Reference to X
- ///////////////////////////
- Rectangle refX Method
- ReturnMethod( ) m_x!
- ///////////////////////////
- // Reference to Y
- ///////////////////////////
- Rectangle refY Method
- ReturnMethod( ) m_y!
- ///////////////////////////
- // Reference to Width
- ///////////////////////////
- Rectangle refWidth Method
- ReturnMethod( ) m_width!
- ///////////////////////////
- // Reference to Height
- ///////////////////////////
- Rectangle refHeight Method
- ReturnMethod( ) m_height!
- ///////////////////////////
```
The most important thing to see here is the fact that not a single public method was changed in how it works, every public method still accomplishes the same thing just in a different way. Since no parameters were changed a coder could choose to use either the old Rectangle class or the new one, but either way it wouldn't matter because they work the same. By taking out access to the variables and using methods to modify them instead, we were able to add and remove variables to the code.
That's all for now on encapsulation. Tune in next time for a lesson on pointers, and more uses of references.
Until next time folks, Code On!
Colin
January 8, 2005, 4:23 pm
This tactic is a good one, but not the best. Say you want setting the object to have an effect? Rather than returning the var itself, you might return a wrapper object with an assignment operator. A properly designed class needs no get/set functions, best of all. (Directly returning vars actually encapsulation) Good writing, though, Matt. I look forward to your next column.
*defeats*
reignofmagic
January 8, 2005, 8:39 pm
Yay, another good tut.
John@aljo
January 9, 2005, 8:08 am
# private: * Method refX() * Method refY() * Method refWidth() * Method refHeight() * m_x! * m_x! // TYPO shouldn't declare a variable private twice * m_width! * m_height! also I don't see the point in referencing the variables. Unless in c++ (i have never used classes in c++) when you access the variables in a class they will go for the whole class and the next time you access the class your erase the old versions of that variable. Lets say you had a rectangle B and a rectangle C If inside my rectangle class I said m_X1 = x1 what would be wrong with that? Im sorry but I come from a Java classes background where we never had to refrence although I have used it in c++ but never learned classes in it.
Colin
January 9, 2005, 1:04 pm
You're right, John. What Matt is showing here is kinda bad, because it defeats the whole point of encapsulation - all it does it creaes extra work (as I said above). If you design a class properly, however, no data should need to be exposed and it should feel much more "natural" than just having a million reference functions that are the same as directly accessing the var.
**Column**
RPG Code > RPG Code Class 101
It's another class from Matt72186 on object-orientated programming with the Toolkit, concentrating on references and encapsulation this time around.
**Past Columns**
Jan 1, '05
Jan 1, '05
