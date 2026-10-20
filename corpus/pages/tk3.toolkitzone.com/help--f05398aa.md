---
kind: page
id: "tk3.toolkitzone.com/tk3.toolkitzone.com/help/?page=21_4"
site: "tk3.toolkitzone.com"
title: "method someString()"
original_url: "http://tk3.toolkitzone.com/help/?page=21_4"
written: null
date_confidence: "unknown"
updated: null
captured: ["20051225190556", "20070126065513"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/tk3.toolkitzone.com/help__page_21_4_amp_3BPHPSESSID_16b5319d9768e0e57579662221cb53a3", captured: "20051225190556", sha256: "b726233bc72b908a8b35bd13ccf7fde3820deef83a9e027d30499165cab89fc7", wayback_url: "https://web.archive.org/web/20051225190556/http://tk3.toolkitzone.com/help/?page=21_4&amp%3BPHPSESSID=16b5319d9768e0e57579662221cb53a3"}
  - {path: "wayback/toolkitzone.com/tk3.toolkitzone.com/help__page_21_4", captured: "20070126065513", sha256: "c6d96c3d05f561dedf45b2eb9d5102b079b8d351683a6ea59abafc3105d02a76", wayback_url: "https://web.archive.org/web/20070126065513/http://tk3.toolkitzone.com/help/?page=21_4"}
---

# method someString()

Arrays in RPGCode have very limited functionality. They do not have set upper bounds and there are no functions to manipulate arrays. While coding an array class exceeds the scope of this document, returning references does not.
When you overload operator[] you can only take one parameter - the index in the array. People from structured programming backgrounds will find it impossible, therefore, to allow the creator to set items in the array. This, however, is not correct. When you return a reference, you make calling a function a synonym for the variable you return. Consider the following example:
method someString()
{
returnMethod(&g_str$)
}
someString() = "Hello, world!"
show(someString())
wait()
The syntax for using returnMethod in this fashion is as seen above:
method returnMethod(&theVar)
Where theVar is a variable - not a value - that calling the function will become a synonym for.
Using this knowledge we can create a simple array class, like so:
// An array
class CArray
{
// Public visibility
public:
// Constructor
method CArray(upperBound!)
// Subscript operator
// Get the upper bound
method getBound() { returnMethod(m_bound!) }
// Deconstructor
method ~CArray()
// Private visibility
private:
m_data[] // Main data
m_bound! // Upper bound of the array
}
// CArray - constructor
method CArray::CArray(upperBound!)
{
if (m_bound! >= 0)
{
// Bound is okay
m_bound! = upperBound!
}
else
{
// Bound is no good
debugger("Invalid upper bound: " + CastLit(upperBound!))
}
}
// CArray - subscript operator
{
// Check bounds
if (idx! <= m_bound! && idx! >= 0)
{
// Within bounds
returnMethod(&m_data[idx!])
}
else
{
// Out of bounds
debugger("Out of array bounds: " + CastLit(idx!))
g_null! = 0
returnMethod(&g_null!)
}
}
// CArray - deconstructor
method CArray::~CArray()
{
On Error Resume Next
local(i!)
for (i! = 0; i! <= m_bound!; i!++)
{
this[i!]->release()
kill(this[idx!]!)
}
}
You may notice the use of this. Said, this, is just the current object, and, as you'd expect, this! is a unique number representing the object.
It's also worth nothing that the array index does not need to be numerical - it can be literal, or even an object.
The CArray class also shows an example of composition, that is, having objects as members of classes. This example which makes an array of dates, illustrates this:
// Create a new array
array = CArray(1)
// Fill it with two CDates
array[0] = CDate(2, 12, 1234)
array[1] = CDate(1, 1, 1999)
// Iterate over the array
ub! = array->getBound()
for (i! = 0; i! <= ub!; i!++)
{
// Show this date
text(1, 1 + i!, array[i!])
}
// Wait for a key
wait()
// Clean up
array->release()
kill(i!, ub!, array!)
If you'll check back at CArray's deconstructor, you'll see that it releases its members automatically so we don't need to release the two dates.
Note: This class has a problem that would be experienced when attempting to copy the object through an assignment or when passed as a parameter; we will explore this problem in . [Copy Constructors](?page=21_5)
As you can see, returning references is a very powerful tool.
