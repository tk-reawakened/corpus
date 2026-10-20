---
kind: page
id: "tk3.toolkitzone.com/tk3.toolkitzone.com/help/?page=21_3"
site: "tk3.toolkitzone.com"
title: "— — Overloading Operators RPGCode Object Oriented Coding"
original_url: "http://tk3.toolkitzone.com/help/?page=21_3"
written: null
date_confidence: "unknown"
updated: null
captured: ["20051225190531", "20070126065501"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/tk3.toolkitzone.com/help__page_21_3_amp_3BPHPSESSID_2c4d403f7bafa7487073861dd736cf98", captured: "20051225190531", sha256: "fec15ad46ee5492a6bd78f5c151c52b72ccbf46c4ba345f8be90d36f036108f4", wayback_url: "https://web.archive.org/web/20051225190531/http://tk3.toolkitzone.com/help/?page=21_3&amp%3BPHPSESSID=2c4d403f7bafa7487073861dd736cf98"}
  - {path: "wayback/toolkitzone.com/tk3.toolkitzone.com/help__page_21_3", captured: "20070126065501", sha256: "4311589737ce94d691cf2224b3dc974cbe07af7dd12c31fc0efad3dc4596da8e", wayback_url: "https://web.archive.org/web/20070126065501/http://tk3.toolkitzone.com/help/?page=21_3"}
---

# — — Overloading Operators RPGCode Object Oriented Coding

Say - using the CDate class - you wanted to reassign an object's date. You might think the following syntax would be legal:
p = CDate(1, 31, 2005)
// Later...
p = CDate(2, 22, 1922)
But all this does is reassigns p to a new object altogether; the original object still exists, but you can no longer access it - this is called a memory leak. But what else can you do? You have no way to access the individual components of the date. Let's remedy that now:
class CDate
{
// Public visibility
public:
// Constructor
method CDate(month!, day!, year!)
// Display the date
method display()
// Interface methods
method getMonth() { returnMethod(m_month!) }
method getDay() { returnMethod(m_day!) }
method getYear() { returnMethod(m_year!) }
// Assignment operator
method operator=(CDate otherDate)
// Private visibility
private:
m_month! // Month
m_day! // Day
m_year! // Year
}
Since the three methods I've added are so short, I've simply placed their bodies in the actual class. Note that the CDate and display methods are not shown again here, but they are still part of the class.
You'll also have noticed that I've added the definition for a method we've not yet coded: operator=. Methods named as operator* (where * is an operator) allow you to code new behavior for operators when used on instances of a class. We'll implement operator= as follows:
// CDate - assignment operator
method CDate::operator=(CDate otherDate)
{
// Copy the other date's members to this date
m_month! = otherDate->m_month!
m_day! = otherDate->m_day!
m_year! = otherDate->m_year!
}
Now the following is valid:
p = CDate(1, 31, 2005)
// Later...
p = CDate(2, 22, 1922)
What if we wanted to display the date ourselves? We could create a function that returns a string and call it, but a more logical approach would be if we could somehow make it possible to use the object where literal variables can be used. We'll place this in the public visibility of CDate:
// Cast to literal
method operator$()
And for its implementation:
// CDate - cast to literal
method CDate::operator$()
{
month[1]$ = "January"
month[2]$ = "February"
month[3]$ = "March"
month[4]$ = "April"
month[5]$ = "May"
month[6]$ = "June"
month[7]$ = "July"
month[8]$ = "August"
month[9]$ = "September"
month[10]$ = "October"
month[11]$ = "November"
month[12]$ = "December"
returnMethod(month[m_month!]$ + " " + CastLit(m_day!) + _
", " + CastLit(m_year!)
}
This makes the following code execute as desired:
p = CDate(1, 31, 2005)
// Output p to the debug window
debugger(p)
p->release()
Note that only one of operator$ and operator! can be overloaded, at present. All operators, with the exception of -> and . can be overloaded.
