---
kind: doc
id: "toolkitzone.com/183"
site: "toolkitzone.com"
title: "Column"
original_url: "http://www.toolkitzone.com/library.php?mode=read&doc=183"
written: "2005-02-13T17:16:00"
date_confidence: "exact"
updated: null
captured: ["20060209100021", "20060612033016", "20070308231737"]
author: "Colin"
repliers: []
authors: ["Colin"]
comments_present: 0
f_author: "Colin"
f_date: "February 13, 2005, 5:16 pm"
f_description: "Another small foray into optimising the performance of your classes for the programming conscious among you."
f_title: "Optimizing RPGCode, Part II"
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/library.php__mode_read_view_cadd_doc_183", captured: "20060209100021", sha256: "6dfe2cb4f7ab41ea5a5bd73e2f78bd7d9c7e330a65ef26366f809df0917725fa", wayback_url: "https://web.archive.org/web/20060209100021/http://www.toolkitzone.com:80/library.php?mode=read&view=cadd&doc=183&PHPSESSID=6c1f0d3aa43a19d10f2020f481c20c7a"}
  - {path: "wayback/toolkitzone.com/library.php__mode_read_doc_183", captured: "20060612033016", sha256: "1884c86b0ea6245708906afeb1929eb613cdf8b22a45ccc12a0eed48a5c7bb79", wayback_url: "https://web.archive.org/web/20060612033016/http://www.toolkitzone.com/library.php?mode=read&doc=183"}
  - {path: "wayback/toolkitzone.com/library.php__doc_183_highlight_", captured: "20070308231737", sha256: "eab0582a476376399c021cd0326d252eddbdb0cbf6bd763f163809072e9ae7c5", wayback_url: "https://web.archive.org/web/20070308231737/http://www.toolkitzone.com:80/library.php?doc=183&highlight"}
---

# Column

TK3 Amelioration XI  Optimizing RPGCode, Part II
Perhaps the most counterproductive practice enjoyed by people, in this community, and elsewhere, is making encapsulation seem forced; that is, to use a class as a holder for multiple variables and make a get and set type function for each. This article will focus on using logic to make encapsulation feel natural, and not just lengthen the time accessing variables takes.
In some cases, poorly designed classes are easy to observe. Other times, however, an often needlessly complex entity can be challenging to debunk. If you were to make a string class, hopefully the underlying string would not be modified painfully through functions. Such a designed class might resemble this: *poorly*
class CString
// Public visibility (*bad* getting and setting)
public:
// Get the string
method getString()
// Just return the member
returnMethod( m_str$
// Set the string
method setString( rhs$
// Copy into member
m_str$ = rhs$
// Private visibility ("protected" variable)
private:
// The string
m_str
Remembering back to some of my earlier columns, encapsulation is intended to protect members with functions. This class offers no protected whatsoever  the string is still being directly accessed, and now the [pointless] overhead of functions is introduced. Lets take a look at some general rules that should be followed:
- Do allow direct getting of integral data (canvases, other objects, etc) *not*
- *Never* provide functions to directly set members
- The containing class provide functions to call contained objects methods *must*
While the first two rules are self-explanatory, the third deserves explanation. Consider the following code:
class CContainer
// Public visibility
public:
// Poor method that returns our member
method getObject()
// Directly expose the member
returnMethod( m_obj!
// Private visibility
private:
// Some object
// (pretend that it's set)
m_obj
A person using the class wanting to call a method of its member will do something like this:
someContainer->getObject()->someMethod()
This is bad because it makes the implementation of the class obvious. The creator should not care how the class is implemented, in case it is changed. A more correct version of the class would be as follows:
class CContainer
// Public visibility
public:
// Call some method on our object (good)
method someMethod()
m_obj->someMethod()
// Private visibility
private:
// Some object
// (pretend that it's set)
m_obj
Classes like this  classes that successfully hide their implementation are the classes that you should be designing. While we do not want to expose the private scope, we also do not want to merely create additional overhead. Before madly making hundreds of useless functions, contemplate what the most efficient way to design the interface is. Good luck!
Colosseus
February 14, 2005, 10:57 am
Interesting. While some of this is beyond my understanding, most of it actually makes sense when I think about it. Good one!
Levi
February 14, 2005, 3:36 pm
Ummm...It's been a while and so I have one question method someMethod() { m_obj->someMethod() } What does that mean? Is it simply returning M_obj into the someMethod name like we do with a function in the Basic language? Or what? It's been too long since I've seen the -> symbol.
Pests
February 14, 2005, 8:54 pm
Are you sure thats good design? Adding a function or removing one will then require you to remove / add that function to all classes that use that object. Your also saying "someContainer->getObject()->someMethod()" is bad. Why provide the getObject in the first place? You could just end up doing: var = someContainter->getObkect() var->someMethod()
UltimaWizard
June 8, 2005, 1:13 pm
@ Levi: RPGCode is really more like C++. Don't even try to connect this tutorial with BASIC, it won't work. All the -> thing does (to my knowledge) is allow the object (in this case, whatever the variable was) to use the member function. It's not a function though; that's what the method by-and-large is. @ Colin: This is a good tutorial. I didn't get it at first, but I still have yet to try it, so that's okay. I thinks you've got several good points about OOP, even though I'm a OOP newbie. Very nice.
**Column**
Toolkit 3.x > TK3 Amelioration
Another small foray into optimising the performance of your classes for the programming conscious among you.
**Past Columns**
Feb 28, '05
Feb 7, '05
Jan 30, '05
Jan 16, '05
Jan 2, '05
Feb 28, '05
Feb 7, '05
Jan 30, '05
Jan 16, '05
Jan 2, '05
