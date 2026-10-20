---
kind: forum-thread
id: "toolkitzone-forums/12266"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "12266"
title: "A worthless Editor...I'm happy"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12266"
written: "2004-12-07T03:55:00"
last_post: "2004-12-07T05:10:00"
date_confidence: "exact"
captured: ["20041227100044"]
author: "Levi"
repliers: ["Colin"]
authors: ["Levi", "Colin"]
posts_present: 5
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_135952_amp_", captured: "20041227100044", sha256: "cc203b0d7b58e2d1806010a6811733158701f4b00c8fc1c94c1f82150f90d3c1", wayback_url: "https://web.archive.org/web/20041227100044/http://www.toolkitzone.com/forums/viewtopic.php?p=135952&amp="}
links: []
---

# A worthless Editor...I'm happy

### Levi · 2004-12-07 03:55 · #B135919

Oh I've just come up with an idea for probably the most worthless editor to ever exist. I've always wondered if RPGCode could resemble Basic more than it does C++. And so in an attempt to keep myself programming in Basic instead of RPGCode I basically created a Basic pseudo code that I would write out on paper. This included RPGCode methods and commands as well as Basic syntax. Well then it occurred to me, in VB.NET it is easy to convert VB to C++ because VB now no longer requires the VB runtimes. This is because it went OO.
What if I could make an editor that used my Basic Pseudo code to program RPGCode and then when it saved the code it would convert it into regular RPGCode.
Its a wonderful idea to test the limits of my ability to solve problems. If but worthless becasue then you'd have to learn how to use Basic isntead of regular RPGCode which seems rather useless don't you think?

### Colin · 2004-12-07 03:57 · #B135920

Well, I don't really know what you plan to do, but one thing's for certain - RPGCode's OOP has more features than VB (even VB.NET), so there is no current VB [syntax] way of implementing many of them.

### Levi · 2004-12-07 04:06 · #B135926

Oh I know. There is more of a general syntax type that seperates Basic from C.
Like with if you start it and you end it with english.
If condition Then
End if
and in C as you know if(condition) { }
There will be a general overflow of RPGCode commands and syntaxing into it. Lets take a look at your classes.
class ITest // Use 'I' when the class is entirely pure, virtual
{
public:
method test() = 0 // " = 0" is the "pure specifier"
}
In VB this same type of thing is done like this
[public:private] Class ClassName
Sub test ()
End Sub
End Class
The sub part is extremely generalized. I'm not sure of the exact copy from VB to this type of coding. I actually won't use Sub but will use method.
REM and ' will take the place of // and /* */
It's just a pseudo code based around the concept of Basic. and its syntax nesting and things will require certian ways of looking of course. I'll figure everything out as it comes along. but right now I'm looking only at 2.2 not 3.0.4 or 3.0.5.
Though those will come next.

### Colin · 2004-12-07 05:03 · #B135948

No, VB does classes like this:
Class CThing
Implements IBase
Inherits CBase
Public Sub New(...)
' C-tor
End Sub
Public Sub This()
' Stuff
End Sub
Private Sub That()
' Stuff
End Sub
Overrides Sub Thingy()
' Thingy() is a virtual function'
End Sub
End Class

### Levi · 2004-12-07 05:10 · #B135952

Tell my text book that. I've noticed they've gotten things a bit wrong every now and again. Oh well.
Again its only pseudo code not an actual scripting thing. It'll just be very general in its syntax following many of the exact same lines that the RPGCode does. When I get to stuff like that.
