---
kind: doc
id: "toolkitzone.com/181"
site: "toolkitzone.com"
title: "What is inheritance?"
original_url: "http://toolkitzone.com/library.php?mode=read&doc=181"
written: "2005-02-11T17:26:00"
date_confidence: "exact"
updated: null
captured: ["20051218071503"]
author: "Occasionally_Correct"
repliers: []
authors: ["Occasionally_Correct"]
comments_present: 0
f_author: "Occasionally_Correct"
f_date: "February 11, 2005, 5:26 pm"
f_description: "With the addition of Object Oriented Programming to TK3, many new concepts were introduced. One of which is inheritance. Today, OC will be explaining the basics of inheritance; an important feature for object oriented programs."
f_title: "The basics of inheritance"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_181", captured: "20051218071503", sha256: "03d7156e712d58208a8f86a5f416d62bbbb82cd4c67abc74901dc038258d2dd9", wayback_url: "https://web.archive.org/web/20051218071503/http://toolkitzone.com:80/library.php?mode=read&doc=181&PHPSESSID=22af9c29bceeb94dce4bcfc8b732692e"}
---

# What is inheritance?

Hi there. OC here, covering basic inheritance. With the addition of Object Oriented Programming to TK3, many new concepts were introduced. One of which is inheritance. Today, I'll be explaining the basics of inheritance; an important feature for object oriented programs. Inheritance is used to express a relationship between classes. This allows us to 'inherit' one classes members ('members' refers to methods and data in a class) and use them in another. For example, let's say we have two classes: CShape and CRectangle. CShape has one method (draw()), and two member variables (m_width! and m_height!). If CRectangle is derived from (inherits) CShape, it will inherit these members. The syntax for inheritance is the following: As you can see, you use a colon (':') after the class name (which is refered to as the 'derived class'), followed by the name of the class that it inherits from (refered to as the 'base class'). Now any members of the CShape class are available in the CRectangle class. This is sometimes called an 'is-a' relationship (a rectangle is a shape; a car is a vehicle, etc.). This example works as expected. It creates the object, sets m_var! to 9 (via the setVar() method), and then shows that value on the screen. Since CDerivedClass inherited all the members of CBaseClass, it was allowed to use it's method and variable. You might already know that you can pass an object into a method. However, since you have to specify the objects type in the parameter list, you can't pass an object of a different type into the method. Example: In that example, you have to pass in an object of type CSomeClass. You wouldn't normally be able to pass in an object of type COtherClass. However, using inheritance changes this. Using the same class as we did in the first real example, take a look at this: In this example we create a method that takes an object of type CBaseClass as one of it's parameters. When we call the method, an object of type CDerivedClass is passed in, instead of CBaseClass. This is allowed because CDerivedClass inherits all members from CBaseClass. And since it's guaranteed to have a setVar() method, calling someMethod() should always work correctly, no matter what instance of CDerivedClass you use. Well, that's it for today. I hope you enjoyed the article and learned something from it. Inheritance can be very useful when utilized in the right situations, and there's more to it than what was shown today. Though, that'll have to wait for another article. Questions or comments anyone? I'm open to input. **The Basics of Inheritance** **Introduction**
**What is inheritance?**
```
class CRectangle : CShape
{
public: } // Code
```
**A quick example**
```
class CBaseClass
{
public:
method setVar {
m_var! = var!
}
private:
m_var!
} class CDerivedClass: CBaseClass
{
public:
method show {
show wait }
} pTest = CDerivedClass pTest->setVar pTest->show pTest->release //------------------------------
// CBaseClass declaration
//------------------------------ (var!) //------------------------------
// CDerivedClass declaration
//------------------------------ (m_var!) // Create an instance of CDerivedClass // Use a method from CBaseClass (9) // Now, a method from CDerivedClass // Destroy the object
```
**Passing in a different object**
```
method someMethod {
p->someOtherMethod } (CSomeClass p!)
```
```
method someMethod {
p->setVar } pTest = CDerivedClass someMethod pTest->show pTest->release (CBaseClass p!, num!) (num!) // Create an instance of CDerivedClass,
// which inherits CBaseClass // Pass pTest into the method (pTest, 3) // Now, show the value of m_var! (should be 3) // destroy the object
```
**Conclusion**
TheCPPFreak220
February 11, 2005, 7:14 pm
I have not gone into RPGCode Classes yet, but isn't there a protected keyword? If so, then m_var! would be hidden from all derived classes and you would have to use the protected keyword instead of private to share it, would you not? Nice column.
Occasionally_Correct
February 11, 2005, 7:44 pm
There's only public and private in RPGCode. :p Thanks!
Colin
February 12, 2005, 12:02 am
C++'s protected == RPGCode's private.
**Column**
RPG Code > Tips & Tricks
With the addition of Object Oriented Programming to TK3, many new concepts were introduced. One of which is inheritance. Today, OC will be explaining the basics of inheritance; an important feature for object oriented programs.
**Past Columns**
Feb 18, '05
Jan 29, '05
Jan 15, '05
Jan 8, '05
Dec 31, '04
Feb 18, '05
Jan 29, '05
Jan 15, '05
Jan 8, '05
Dec 31, '04
