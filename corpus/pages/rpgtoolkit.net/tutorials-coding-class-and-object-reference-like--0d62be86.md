---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/tutorials/coding/class-and-object-reference/like/"
site: "rpgtoolkit.net"
title: "April 19th, 2011"
original_url: "http://rpgtoolkit.net/tutorials/coding/class-and-object-reference/like/"
written: "2011-04-19"
date_confidence: "day"
updated: null
captured: ["20130407083520"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/tutorials/coding/class-and-object-reference/like/index", captured: "20130407083520", sha256: "90608bdac99455c8854be23172246e0998e39c84c0230866d3088b9e48eaa8b5", wayback_url: "https://web.archive.org/web/20130407083520/http://rpgtoolkit.net/tutorials/coding/class-and-object-reference/like/"}
---

# April 19th, 2011

The Lost Epic / 7LegionArmy
[![Occasionally_Correct](thumb/80/community/images/avatars/upload/20303561264ab1310bc4b88.png)](member/occasionally-correct/)
Published
**April 19th, 2011**
Read times **4,128**
Written by Occasionally_Correct
Class and Object Reference
**Concise, technical overview of how classes and objects work in RPGCode.**
About this document
Hi there! OC here, and today I have a new (very lengthy) article about some RPGCode things.
As the name implies, this is a technical document about the syntax and semantics behind classes (and therefore structs) and objects in RPGCode. I aim to be as brief and clear as possible, so in interest of that this is not a tutorial-style article: I'm not going to spend much time on theories or why these features are good to use. If you don't already have the basics down, feel free to read this alongside a tutorial. (But even if you don't, there are code examples throughout!)
An important note about document structure: It isn't meant to be read in any particular order. That makes it a lot easier to write because I don't have to worry about "dependency issues" (must cover topics a, b, and c before mentioning d, e, or f), but at the same time I have tried to avoid overlap as much as I can without compromising the examples. The best way to read it is to just jump in, jump around, and absorb little pieces as you go.
With that said, there some logical order to the sections where possible. *is*
Differences between classes and structs
There aren't any big differences. A class defaults to private scope and a struct defaults to public scope. Because of this one tiny difference between the two, we're just going to focus on classes because they get the most widespread use. Moving right along... :)
Class definitions
Classes are defined in much the same way that functions are. The most barebones class you can have is simply:
```
AnEmptyClass class
```
The keyword defines a new class. The next part is the name of the class. The last part is a set of curly braces that contain the of the class (in the above example, the body is empty). This is the least amount of information you need to provide to have a valid class. (Just because it's valid doesn't mean it's useful. Well, good thing the document doesn't end here!) class *body*
Method definitions
Class methods[ ] can either be defined within the class body itself, or declared and then defined outside. Consider these two examples:1
```
SomeClass someMethod sum a b a b
1
2
3
4
5
6
7
8
9
10
class public function mwin "Here I am!" function return
```
```
SomeClass someMethod sum a b SomeClass someMethod SomeClass sum a b a b
1
2
3
4
5
6
7
8
9
10
11
12
13
class public function (); function function mwin "Here I am!" function return
```
In the first example, a method is defined within the class body. In the second, a method is declared in the class body, but it is defined outside. Note that instead of just using the method's name, you must type the class name, followed by the scope resolution operator, then finally the name of the method. There are no noticeable differences when running the code, but there are practical differences when reading it (eg., being able to look at what methods the class defines without having to see their implementation details). Whichever you choose is up to your preferences.
The scope resolution operator
The scope resolution operator—seen in the above example—is used to define a method that belongs to a class. It looks suspiciously like two colons: . Its left operand is the name of the class and its right operand is the name of the method. ::
Type hinting
Although RPGCode is a dynamically typed language, it allows type hinting to be used with function parameters (much like PHP). allows you to force an argument to be of a specific type, or else an error will be raised. Note that the must be a class; you can't hint a parameter to be a "built in" type like a string or integer. To require a specific type, you only have to write a class name before the parameter. Example: *Type hinting* *type*
```
hint SomeClass o o someMethod hint SomeClass hint
1
2
3
4
5
6
7
8
9
function (); // This works: ()); // An error: "test"
```
One thing to watch out for is that type hinting has no bearing on overloaded functions (that is to say, for example, that you cannot overload a function with and ). f(A obj) f(B obj)
Things that might matter
- Class methods can appear in both the public and private sections of a class. Private methods can only be accessed internally.
- Because of the way function calls are handled in RPGCode in 3.1.0, class methods may not share their names with built-in functions. Eg., and conflict[ ]. show(x) o->show(x)2
- Class methods cannot be inlined. You are still allowed to put the keyword before the method—it will not throw an error or give you any kind of warning—but it will be ignored when running the code. inline
- RPGCode will define a few different methods for you when an object is created. Amongst these are the default constructor, default destructor, and the method. These will be explained later. release
- Besides inline expansion, all the usual utilities apply: returning and passing by reference, function overloading, hinting, et cetera.
Known bugs regarding methods
- The constructor method cannot take an object as its first argument.
[1] Method? Function? Difference?
Users of pre-3.1.0 RPGCode will remember that functions were defined with the keyword. In Object Oriented Programming terminology, class-level functions are called "methods," so when you see the word in this article, that's what it means (and not the old keyword). The keyword was introduced in 3.1.0 with the thought that might be phased out some time in the distant future, but whether that will ever happen is unknown at this point. For now, use whichever keyword you're comfortable with. method function method
[2] On the semantics of function calls...
Calling will call the built-in function with two arguments: The object and the variable . This is an error because only accepts one argument. , therefore, is equivalent to . Try it! (Note that you actually have to define a function within your class first.) o->show(x) show o x show o->show() show(o) show()
The reason? Behind the scenes, the notation passes the object as the first argument of . In a sense, class methods have at least one parameter; it is just implicit. The "implicit first parameter" is referred to in code as . o->f() o f *all* this
Variable definitions
Variables (called "member variables") can be defined inside a class in both the public and private sections. In its most basic form, you can declare a variable inside a class just by writing its name:
```
SomeClass someVariable anotherVariable
1
2
3
4
class
```
However, the preferred way is to use the keyword. This keyword was introduced in version 3.1.0 and only has meaning inside the body of a class (ie., elsewhere it can be used as a variable name). var
```
SomeClass someVariable anotherVariable
1
2
3
4
class var var
```
The following definitions are all possible:
- Define a variable: example
- Define an array: example[]
- Define a variable with the keyword: var var example
- Define an array with the keyword: var var example[]
- Define an array with an upper bound[ ][ ]:12 var example[3]
- Define a list of variables[ ]:1 var example, example2, example3
For the remainder of the document, variables will be defined exclusively using the keyword. var
[1] Only with var...
You can only use this syntax with the keyword. For the sake of consistency, it is best to always use . (It also looks nice, provides a visual cue in a sea of definitions, and was added out of love.) var var
[2] No respect!
While it's possible to define a member variable as an array with an upper bound, the upper bound isn't respected. For example, if you access outside that bound, trans3 isn't going to yell at you. However, this syntax can be used to provide meaning if you do intend to force a hard upper bound.
Constructors and destructors
Constructors are methods that initialize the class. They allow you to set values for member variables or perform any other setup that needs to happen. The constructor of a class is called when an object is being instantiated. A constructor is declared by naming a function after the class itself.
Destructors are methods[ ] that get rid of resources used by a class. They are called when an object is freed with the method. A destructor is declared by naming a function after the class preceded by a tilde ( ).1 release() ~
```
SomeClass SomeClass SomeClass foo SomeClass foo release
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
class public function mwin "The object is being initialized!" function mwin "The object is being cleaned up!" // Call the constructor. (); // Call the destructor. (); wait ();
```
Every class has a constructor and destructor (and method) whether you write them or not. A default constructor doesn't do anything special. A default destructor simply frees what data it can. For most classes that you write, you will want to define your own constructor (or several depending on what you're doing). However, you can usually safely ignore writing your own destructor[ ]. (The exception to this is when your class keeps special resources—canvases, threads, cursor maps, or resources allocated by plugins, for example—which are not freed by the default destructor.) release()2
Known bugs regarding constructors and destructors
- The constructor method cannot take an object as its first argument.
- An object that has an explicitly defined destructor will stay in memory until the garbage collector removes it (even if is called). release()
[1] We're all the same on the inside
Note that although constructors and destructors have special implications for the instantiation and destruction of objects, they are, after all, normal functions that can take advantages of the niceties of RPGCode (function overloading, pass by reference, et cetera, et cetera). You can even have multiple destructors that can be called by feeding different numbers of parameters. (Of course, there's usually no reason do that with destructors, but it's good to know, right?) release() *to*
[2] Garbage collection...
As of 3.1.0, RPGCode sports a garbage collector that will clean up most resources used by objects once those objects go out of scope (that is, when nothing refers to them anymore). There are a few specific things it will free. This is explained in more detail later. *not*
Scope
Each class usually has a and a section. These correspond somewhat to the ideas of global and local scope in functions, but with a few distinctions. Firstly and most importantly, while a function default to global scope for newly defined variables, a class will default to private for newly defined variables and functions. So to be able to access anything from outside the class, it must have a public section. Otherwise, trying to access anything will pop up an error. Here's how it's done: *public* *private* *can* *always*
```
SomeClass
1
2
3
4
5
6
7
class public // Public data resides here. private // Private data resides here.
```
Some random tidbits:
- It doesn't matter if or comes first. *public* *private*
- You can have more than one public and private section in a single class, but it makes no sense to.
- Different objects of the same class can share private data with each other (more on this in a moment).
- Since classes default to private, you don't have to use the keyword if you put the private data first (but it's good to be explicit, so better to use anyway). private: private:
Sharing between objects
Private data is usually not accessible from the outside of an object. There is one exception! If an object is used within a method and they both share the same type of class, the private data is freely accessible. If that didn't make a lot of sense, here's an easier example to understand:
```
Example Example data _data data share Example p p _data _data objA Example objB Example objA share objB objB share objA
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
class public function function show "The data is: " private var "I love cookies" "cookies love me" wait ();
```
Here, two objects are instantiated from the same class. The class has a method, , that does one thing: Take an object of the same type and show its private data. If you run this code, you'll see that shows the message from and vice versa. share() objA objB
Parameters and members
If a method's parameters are named after member variables of the class, the parameters will be introduced as new variables inside the method's scope. If a situation like this arises, it becomes necessary to use to refer to the member variables (otherwise, the parameters will be used). this
```
ParameterTest ParameterTest x y x x y y x y obj ParameterTest obj x obj y
1
2
3
4
5
6
7
8
9
10
11
12
13
14
class public function this this var show show wait ();
```
This
Internally, every class method takes at least one argument that is assigned by the engine (implicitly) when the method is called from an object. The "implicit first parameter" is called in code, and it is a reference to the object that the method was called from. You can use like any other variable within a function. Because it's a reference to the calling object (ie., it "is" the calling object), you can treat it the same way: this this
```
ThisTest ThisTest _x countdown n n countdown n showX _x _x obj ThisTest obj obj countdown obj showX
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
class public function print "Creating object #" this this 153749 function print "Counted down!" return return this function print "The value of X is " this private var text "Demonstrating 'this'" print (); print "Object #" " created!" (); wait ();
```
There are a few spots to point out. On line 4, is appended to the end of a string. When you print the value of an object, it appears as a number. (The corresponding on line 29 is there to show that and do indeed have the same value.) On line 5, is used to access the member variable (and once again on line 18). On line 14, is used to call the method . this print() obj this this _x this countdown()
Of course, the use of is optional for calling functions or accessing variables. this
Objects
Objects are implementations—called "instances"—of the functionality described by classes (and structs). In other words, a class is a general description of how an object (an instance of the class) should behave. Each instance is unique: Changes made to one object do not effect any other objects that share the same class ("type"). Objects are instantiated by calling a class' constructor. Functions and variables are accessed with an operator that looks like it might be part of a sign that has "that way" written on it: . ->
```
SomeClass SomeClass someField obj SomeClass obj someField obj2 SomeClass obj2 someField obj someField obj2 someField
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
class public function show "Creating an instance of SomeClass" var (); (); "Hello world!" show show wait ();
```
Object variables are references
When one variable is used in an assignment to another—as in —the assignee normally gets a copy of the assigned value. However, if an object is assigned to another variable, then both variables will refer to the same object (again, each instance is unique, but any number of variables can reference a single object). Here's an example: x = y
```
ReferenceTest value obj ReferenceTest obj value obj value ref obj ref value ref value obj value obj ref value
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
class public var // Create a unique instance of ReferenceTest. (); 5.1 show // Create a second reference to it. // This'll change obj's "value" member. "references!!!" show show // You can kill either variable; it won't touch the actual object. kill show wait ();
```
Copying objects
If you ever wish to make a copy of an object instead of obtaining a reference, you will have to create your own (or or some other name that hopefully conveys what you want to do) method. That should be straightforward, but I'll provide a quick example that gives you two options for copying. copy() clone()
```
CopyTest copy new CopyTest new _x _x new _y _y new copy CopyTest obj _x obj _x _y obj _y _x _y
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
class public /**
* Return a copy of the object.
*/ function (); return /**
* Copy another instance of CopyTest into this one.
*/ function private var
```
Garbage collection
RPGCode's (abbreviated GC) is a mechanism which frees memory that is no longer referenced by a variable. It is not directly related to the subject matter, but it has some implications for how objects are managed. *garbage collector*
So, how does it work? Every ten minutes, the garbage collector runs (whether during normal play or when an RPGCode program is running) and determines which data is not being referenced—ie., any variables that have gone out of scope. Whatever data it finds is freed so the memory it used can be given to some other resource. For example, if you have a function that creates a local variable , and you call that function several times, will be created each time using new memory. When the function call ends, goes out of scope—it is unreachable by any identifier. When the garbage collector runs, it will free the memory used by however many variables were created. The same goes for variables local to program files and, of course, objects. x x x x
Objects get a little more thorough cleaning. When an object goes out of scope, the garbage collector will free the unused memory including member variables of the object (even arrays and other objects). As a side effect of the way unreachable objects are managed, it's usually unnecessary to call a local object's destructor.
There are two caveats: Firstly, the garbage collector will not free certain resources (canvases, cursor maps, threads, resources allocated by plugins, et cetera). Secondly, it won't call an object's destructor. So if your class needs to hold on to special resources, you must clean them up yourself. Thankfully, there's a rule of thumb you can use so that you don't have to remember just what isn't caught: If you've created some resource that has an ID or handle associated with it (except objects), you need to clean it up yourself.
Here's a commented code example of what exactly the above paragraphs mean:
```
GarbageTest junk garbage SecondGarbageTest SecondGarbageTest _cnv SecondGarbageTest _cnv _cnv allocateMemory i i i memoryWaster i i obj GarbageTest obj junk obj garbage obj SecondGarbageTest obj release allocateMemory longLasting
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
// Create local variables unless I say otherwise. autolocal true // Remember: structs are classes with default public scope. struct var class public function createCanvas function killCanvas private var function 100 // This object only allocates memory for regular variables; no // destructor is needed and the GC will free it. (); "in the trunk" "goes in the trashcan" // The constructor here allocates a special resource (a canvas), so if we leave // it up to the GC, we'll have a memory leak (it won't free the canvas). We // have to call the destructor ourselves. // Also note that when we reassign "obj," the old memory stored in it will // no longer be referenced by an identifier. (); (); // Allocate an array with 100 elements. When the function ends, the array will // go out of scope. The GC will free all the memory allocated by this function. (); // This is global and will live on after the script ends: The GC won't free it. global
```
Inheritance
I'm going to warn you now that inheritance is "broken"[ ] in version 3.1.0 (if you're really curious about the brainy details, you can check and then ). , there is one situation where it does work, so I will include this section for the sake of completeness.1 [this post](http://rpgtoolkit.net/community/post/484222) [this topic](http://rpgtoolkit.net/community/discussion/44202) *However*
Inerhitance is just as it sounds: It allows one class to inherit or the members (variables and methods) of another. The deriving class is often called the or , and the one being derived from is often called the or . The syntax to derive one class from another looks a bit like this: *derive* *child* *subclass* *parent* *base class*
```
ChildClass ParentClass
1
2
3
class ...
```
A single colon is written after the name of the deriving class followed by the name of the class that's being derived from.
One important thing to remember is that when an instance of a derived class is created, only the derived class' constructor is called. If you need to call the base class' constructor, you can do so manully within the constructor of the derived class. For example:
```
Parent Parent _importantData _importantData Child Parent Child Parent _importantData obj Child
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
class public function true private var class public function // Need the important data initialized correctly! this (); show (); wait ();
```
Note one potential pitfall: When calling the constructor of the base class, you must use to call it to ensure that the inherited function is called. Otherwise, the engine won't resolve it correctly and an error will be raised. this
[1] What's this inheritance bug?
Inheritance only behaves properly when both classes are in the same file and all the code that uses the classes is also in that same file. Basically, if you have to include a class that uses inheritance (or you have to include the class it's inheriting from), you'll get some bad results when using inherited functions.
Operator overloading
Operator overloading allows you to specify custom behavior for operators used in conjunction with objects. Most operators can be overloaded, with few exceptions ( and , for example). If you wanted to overload the increment operator, you would do something like this: -> ::
```
OperatorTest OperatorTest _count operator _count showCount _count _count obj OperatorTest obj obj obj obj showCount
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
class public function // Keep track of the count. function ++() function show private var (); (); wait ();
```
On line 8, the increment operator (this includes pre- and post-increment) is overloaded by defining the method . It increments the member variable each time the increment operator is used on the object. On lines 21 to 23, it is called three times, and then the value of is shown. operator++() _count _count
Other operators can be overloaded by replacing the ++ with the proper symbol. The following operators can be overloaded:
- Arithmetic: , , , , , , , + - * / ^ % ++ --
- Logic: , , , , , , , , == ~= > >= < <= && || !
- Bitwise: , , , , , & | ~ ` >> <<
- Other: , = []
Arithmetic and bitwise assignment operators that were omitted from the list, like , can also be overloaded. For any operator that requires two operands, a parameter is required for the operator method. In those cases, the calling object is treated as the left-hand operand and the parameter is the right-hand operand ("rhs" or in the next example). Likewise, the few operators ( , , ) that only have one operand (the object) should not have any parameters (like the above example). += *right-hand side* ! ++ --
```
operator rhs _someData rhs operator index index index _size _data index
1
2
3
4
5
6
7
8
9
10
11
12
13
... function return ... function []( debugger "Array index out of bounds!" return null return ...
```
Chaining operators
Anyone who was curious enough to implement the previous example may have noticed odd behavior upon chaining it into a longer expression (such as ). On closer examination, it's not hard to see why: The return value of is something other than the object (or an object of the same type). The ability to "chain" operators can be achieved by either returning a new object or . For example, one might want to allow writes to a custom message window with the left shift operator ( ): operator+ obj1 + something + something operator+ this <<
```
operator str _lines _lineCount str _lineCount msgwin
1
2
3
4
5
6
7
function <<( ++; return this ... "first line" "second line"
```
Time for RPGCode 101: is evaluated first and returns a reference to the calling object. Then the resulting value (the object ) becomes the left-hand side of , allowing the chain to continue. msgwin << "first line" msgwin << "second line"
Appendix A: A concise look at updating your code
If you are looking to update old code from 3.0.6 to 3.1.0 (or later), there are a few things that need to be changed and features that are no longer implemented. Here's a quick list to get you on your way.
Declare member variables with var
While still possible to declare members of a class just by writing their names (in most cases), it is now preferred to use the new keyword. var
Class methods can conflict with global functions
Because of the way function calls are handled in 3.1.0, you cannot name a method after a built-in function (eg., ). show()
The object is always a reference
In 3.0.6, , where is an object, would create a copy of . In 3.1.0, objects are always references, so and refer to the same object in memory. Because of that... obj2 = obj1 obj1 obj1 obj2 obj1
There are no copy constructors
In 3.0.6, copy constructors were called when a situation like the one above occurred. But because no copying takes place now, there are no copy constructors. If you need a copy, implement a copy() function. Because of that...
You should reconsider overloading =
Because the default behavior of object assignment has changed and copy constructors no longer exist, you should probably not overload the assignment operator unless you have a very specific reason to. Speaking of overloading operators...
No overloading type characters
RPGCode in 3.1.0 silently ignores type characters in favor of dynamic typing, so it is no longer possible (or meaningful) to overload types.
Broken or unimplemented features
- Inheritance is mostly broken.
- Multiple inheritance is broken even when single inheritance works.
- Pure virtual functions were not implemented in 3.1.0.
That's all, folks...
...or is it?!
Thanks for reading! Any suggestions , mistakes , or complaints may be sent to me (Occasionally_Correct) via PM on the forums. :) :O :'(
