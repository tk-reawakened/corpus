---
kind: doc
id: "toolkitzone.com/188"
site: "toolkitzone.com"
title: "Introduction"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=188"
written: "2005-02-18T18:07:00"
date_confidence: "exact"
updated: null
captured: ["20060312124317", "20060612052526", "20060612052526"]
author: "Occasionally_Correct"
repliers: []
authors: ["Occasionally_Correct"]
comments_present: 0
f_author: "Occasionally_Correct"
f_date: "February 18, 2005, 6:07 pm"
f_description: "Last week OC covered the basics of inheritance, a feature that classes let us take advantage of. Today, he will continue with the more advanced things you can do with inheritance - namely multiple inheritance and using pure virtual methods."
f_title: "More about Inheritance"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_view_cadd_doc_188", captured: "20060312124317", sha256: "472fa0f7b4e7126bf5c455d7fdb12a3d373e48d4e1772ccb77f8e7d192887b45", wayback_url: "https://web.archive.org/web/20060312124317/http://toolkitzone.com:80/library.php?mode=read&view=cadd&doc=188&PHPSESSID=bdcceeefceef8ff863ad82d0d089ece4"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_188", captured: "20060612052526", sha256: "7ac3a237d07dab02e32636e92d8aa09fa8d72043a40b8c79cef73ff6475b4682", wayback_url: "https://web.archive.org/web/20060612052526/http://toolkitzone.com/library.php?mode=read&doc=188"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_188-269576", captured: "20060612052526", sha256: "7ac3a237d07dab02e32636e92d8aa09fa8d72043a40b8c79cef73ff6475b4682", wayback_url: "https://web.archive.org/web/20060612052526/http://www.toolkitzone.com/library.php?mode=read&doc=188"}
---

# Introduction

Hi there. OC here. Last week I covered the subject of inheritance, a feature that classes let us take advantage of. Today, I'll be continuing last weeks article with more advanced things you can do with inheritance (namely multiple inheritance and using pure virtual methods). Single inheritance (covered last week) is a great feature, as it provides the ability to create an 'interface' of sorts for other classes. After using it for a while, though, you may be faced with a situation where you want to inherit more than one class. This is where multiple inheritance comes in. Multiple inheritance allows you to derive a class from more than one base class. The syntax for multiple inheritance is as follows: As usual, you declare the class using the class keyword, followed by the name of the class, a colon, then the names of the base classes separated by commas. Here's a quick example: As you can see, this example uses three classes (CBaseOne, CBaseTwo, and CDerived), all of which have one method. The first two classes act as base classes for CDerived, so their methods are inherited. This isn't a very useful example, but it shows you how things are done. Let's move on... Base classes don't usually need to be instantiated. In fact, most of the time all they do is provide an interface for classes that derive from them. If that's the case with a class you're designing, a good idea would be to use pure virtual methods. Pure virtual methods are member methods of a class that have no implementation (they don't do anything). So, the class that inherits the pure virtual methods must provide it's own implementation for each method. Since the pure virtual methods in the base class don't have any implementation, it is impossible to make an instance of that particular class. Take a look at this example: There are two classes: The base class, IShape, has one method (draw()) which is initialized to 0. Using the equals sign and 0 signifies that the method is a pure virtual method. Because of this, IShape can't be instantiated (which is ideal, since a shape is a concept. Circles, squares, and rectangles are implementations of this concept). The other class, CRectangle, has two methods (the constructor and draw()). The constructor sets a few initial values, and the draw() method draws a rectangle on the screen. That's it for today. I hope that you've enjoyed the article and learned something from it. As I'm sure I and others have mentioned, object oriented programming (OOP) is a very big subject. Understanding the key elements and features of OOP is a big step in the right direction for developing reusable, easy to understand programs for your games. Inheritance is just one of many topics that can be covered (though, it's an important one). If you have any comments or questions, feel free. Input is always welcome. **More about Inheritance**
**Introduction**
**Multiple Inheritance**
```
class CDerived: CBaseOne, CBaseTwo, etc...
{
// code
}
```
```
class CBaseOne
{
public:
method show(value$)
{
show(value$)
}
}
class CBaseTwo
{
public:
method show(value!)
{
show(value!)
}
}
class CDerived: CBaseOne, CBaseTwo
{
public:
method show()
{
debugger("Error! show() has no data elements!")
}
}
pShow = CDerived()
pShow->show("hello world!") // output: hello world!
pShow->show(42) // output: 42
pShow->show() // error message!
pShow->release()
```
**Pure Virtual Methods**
```
class IShape
{
public:
method draw() = 0
}
class CRectangle: IShape
{
public:
method CRectangle(x1!, y1!, x2!, y2!)
{
m_x1! = x1!
m_y1! = y1!
m_x2! = x2!
m_y2! = y2!
}
method draw()
{
drawRect(m_x1!, m_y1!, m_x2!, m_y2!)
}
private:
m_x1!
m_y1!
m_x2!
m_y2!
}
```
**Conclusion**
Allan@Aljo
February 28, 2005, 9:44 am
what do you gain by using the pure virtual method?
**Column**
RPG Code > Tips & Tricks
Last week OC covered the basics of inheritance, a feature that classes let us take advantage of. Today, he will continue with the more advanced things you can do with inheritance - namely multiple inheritance and using pure virtual methods.
**Past Columns**
Feb 11, '05
Jan 29, '05
Jan 15, '05
Jan 8, '05
Dec 31, '04
Feb 11, '05
Jan 29, '05
Jan 15, '05
Jan 8, '05
Dec 31, '04
