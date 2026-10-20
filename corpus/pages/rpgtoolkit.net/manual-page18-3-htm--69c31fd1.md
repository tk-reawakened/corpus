---
kind: page
id: "rpgtoolkit.net/rpgtoolkit.net/manual/page18.3.htm"
site: "rpgtoolkit.net"
title: "Contents"
original_url: "http://rpgtoolkit.net/manual/page18.3.htm"
written: null
date_confidence: "unknown"
updated: null
captured: ["20150716000408"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/rpgtoolkit.net/manual/page18.3.htm", captured: "20150716000408", sha256: "25900f1e421ad46fae2581452f4aaadc998aaa62b1aade6c4438ebe2da8c343a", wayback_url: "https://web.archive.org/web/20150716000408/http://rpgtoolkit.net/manual/page18.3.htm"}
---

# Contents

Functions
Functions
In RPGCode, and all other modern scripting and programming languages, a programmer may define their own functions to facilitate performing certain tasks wherever it is needed with a single line of code. Learning to take advantage of this will help you structure your code more clearly, shorten your code where a few function calls might be more appropriate than a few blocks of code that all do the same thing, and it will make your life less complicated (at least when coding).
The Basics:
The definition of a function consists of multiple parts: The declaration keyword , the name of the function followed by the parameter list, an opening curly brace, the body of the function, and a closing curly brace. Here is an example of what a function might look like: function
```
function name( , , )
{
// Code to execute is inserted here.
} parameter1 parameter2 etc
```
Perhaps a little more involved than previous constructs we've explored, but it is simple enough! The above function would do nothing, so let's create a very basic one that do something. *does*
```
function test()
{
mwin("This is a test!");
wait();
mwinCls();
}
```
This function shows the string "This is a test!" in the message window, waits for the user to press a key, and then clears the message window from the screen. But how do you call the function? The exact same way you would call a built-in function if its name were : *test*
```
test()
```
Returning Values:
Just as we saw that some built-in functions return values, user-defined functions may also return values. This is done with a statement inside the function. A return statement takes on the following form: return
```
return expression
```
The is, as with the control structures discussed earlier, any valid expression that can be made in RPGCode, and the resulting value is returned. When the return statement of a function is reached, execution of the function stops and any code inside the function after the return statement will not be run. Here is an example that returns the result of the expression : *expression* 5 + 5
```
function add()
{
return 5 + 5;
}
x = add();
mwin(x);
wait();
```
Parameters and Arguments:
Expanding on where we left off in the basics section of this manual, an argument is data that is passed to a parameter; a parameter is a variable which recieves an argument (the data). (Sometimes people use the two terms interchangeably.) You may define your functions with any number of parameters, each of which is given a unique name and separated by commas. Here is the same function we used earlier, except that it takes two parameters, and , and adds them together, instead of two constant values. x y
```
function add(x, y)
{
return x + y;
}
z = add(2, 3);
mwin(z);
wait();
```
The function is declared with the two aforementioned parameters. In the body of the function, the two parameter variables are added together and the result is passed on to the construct. When the function is called, the result is stored in the variable . is then displayed via the function. add return z z mwin
Parameter variables are automatically deleted from memory when the function finishes executing, and you do not need to worry about parameter names conflicting with variable names in your code (ie., if you have defined a variable called and a function parameter with the same name, they will effectively be different variables). x
Including Files:
Up to this point all of our functions have been defined and called in the same file, but if a function has to be defined in whatever file it is called in, it isn't very useful (but it isn't useless either). Thankfully, functions may be saved into different files and included where they are needed. This makes them much more accessible. You can include an rpgcode file into another file with the directive: #include
```
// Include the file "math.prg", which defines the add() function.
#include "math.prg"
mwin(add(7, 9));
wait();
```
This assumes that the function was saved in the file . Several functions may be defined in the same file. (Note that if an included file contains "loose" code outside of a function, it will not be run.) You may also use the function, as in: add *math.prg* include()
```
include("math.prg");
```
RPGCode also supports "implicit" inclusion, where the function is called in the format . For example, using implicit inclusion the above program can be written as: fileName.functionName()
```
mwin(math.add(7, 9));
wait();
```
When a function is called with implicit inclusion, the file is automatically included so you do not need to keep prefixing function calls with the file name and dot (but you can if you want to).
Overloading Functions:
Function overloading allows you to define multiple functions that have the same name and a different parameter list. This is an especially useful feature when you are implementing a function that may not require all of the parameters each time it is called: Instead you would like to be able to define what the function should do depending on what arguments it recieves.
```
function add(a, b)
{
return a + b;
}
function add(a, b, c)
{
return a + b + c;
}
function add(a, b, c, d)
{
return a + b + c + d;
}
// etc...
```
In this example we have written three functions. The first one adds two numbers, the second adds three numbers, and the third adds four numbers. It is certainly much cleaner than writing one function with many parameters and expecting the programmer using the function to work around the parameters that aren't needed. However, it is sometimes more beneficial to call one of the overloaded functions inside of another to circumvent reimplementing the same function multiple times. For example, you could write the above three functions like this: add
```
function add(a, b)
{
return add(a, b, 0, 0);
}
function add(a, b, c)
{
return add(a, b, c, 0);
}
function add(a, b, c, d)
{
return a + b + c + d;
}
```
When using these rewritten functions, you would not notice a difference. The advantage is that if you want to change the behavior of the third function, you would not have to change the others to behave the same way since they are just calling that one function. add
Inline Expansion:
An inline function is a function whose body is semantically inserted into the program where it is called. This can be achieved with functions by placing the keyword before the keyword. Going back to the function again, we can further improve it by inlining it. inline function add
```
inline function add(x, y)
{
return x + y;
}
z = add(2, 3);
mwin(z);
wait();
```
The function call site will be transformed at run-time into this:
```
z = x + y;
```
By inlining simple functions, an increase in performance can be gained where a normal function call might be slower. A larger, more complex function, especially if it is called multiple times, may not gain any significant increase in performance, so it's best to only inline simpler functions.
References
As of version 3.1.0, RPGCode supports passing arguments by reference. When you pass an argument by reference into a function, you are not copying the value of the argument; the parameter is rather turned into an alias of the argument (ie., any operations made on the reference variable will also affect the variable that was passed in as the argument). You can make a parameter take arguments by reference by prefixing the parameter name with an ampersand ( ). &
For example, using references we can implement a function that swaps the values of two variables:
```
function swap(&x, &y)
{
temp = x;
x = y;
y = temp;
}
a = "hello";
b = "world";
mwin(a + " " + b);
swap(a, b);
mwin(a + " " + b);
wait();
```
Try running that example. You should see that it shows "hello world", waits for a key press, then swaps the values of and and shows "world hello". a b
When you pass an argument into a function by reference, the argument must not be an expression like , , or ; it must always be an actual variable. An error will be raised otherwise. 5 1 + 1 "hello!"
But RPGCode does not only support parameter references: it also allows functions to return references. You might think of functions returning references as synonymous with the reference variable that they return, and they may even be on the left-hand side of an assignment operation (eg., ). To return a reference variable from a function, you need to prefix it with an ampersand, like you would with parameters: func() = someValue
```
function someRef()
{
return &ref;
}
someRef() = "References galore!";
mwin(someRef());
wait();
```
