---
kind: forum-thread
id: "toolkitzone-forums/6627"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "6627"
title: "Dumb Visual Basic Question"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=6627"
written: "2004-08-01T20:05:00"
last_post: "2004-08-01T22:39:00"
date_confidence: "exact"
captured: ["20040921165421"]
author: "Master Tamer"
repliers: ["Levi", "Marc", "KSNiloc", "Eternal EoN"]
authors: ["Master Tamer", "Levi", "Marc", "KSNiloc", "Eternal EoN"]
posts_present: 10
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_68581_amp_", captured: "20040921165421", sha256: "d89fc1f27c703e21da53df51073ca10b62ea8764485a632a7360bec92da59ba3", wayback_url: "https://web.archive.org/web/20040921165421/http://www.toolkitzone.com/forums/viewtopic.php?p=68581&amp="}
links:
  - {url: "http://eon.ssxh.net", status: "external", local: null}
  - {url: "http://eon.ssxh.net/expo_ffurybanner.png", status: "external", local: null}
  - {url: "http://img76.exs.cx/img76/421/Muahahahaha.jpg", status: "external", local: null}
  - {url: "http://img85.exs.cx/img85/3596/Niloc.gif", status: "external", local: null}
  - {url: "http://www.geocities.com/tamexplayer/antimastertamer.PNG", status: "external", local: null}
  - {url: "http://www.hilaryduff.com", status: "external", local: null}
  - {url: "http://www.rpgadev.com", status: "external", local: null}
  - {url: "http://www.rpgadev.com/header1.jpg", status: "external", local: null}
  - {url: "http://www.your-poetry.com/modules.php?name=News&file=article&sid=39971", status: "external", local: null}
---

# Dumb Visual Basic Question

### Master Tamer · 2004-08-01 20:05 · #B68473

How do I make Save and open files? It's stupid but I'm a VB newbie, and tutorials explains how.
_________________
MMORPG creation
[![](http://www.rpgadev.com/header1.jpg)](http://www.rpgadev.com)
[![](http://www.geocities.com/tamexplayer/antimastertamer.PNG)](http://www.hilaryduff.com)
![](http://img85.exs.cx/img85/3596/Niloc.gif)

### Levi · 2004-08-01 20:16 · #B68477

I don't know how VB has changed from 6.0 to .net framework but if you're working in VBExpress I believe it is .net.
This is for standard basic, I only hope VB hasn't gone to filesteam objects.
Open filename for mode as handle
Open "Text.txt" for Input as #1
Input #1, strHello
print strHello
Close #1
modes come int: Input, Output, and one other I forgot. Append is one also. That allows for adding text to a file without deleting the contents. Output, deletes the stuff in the file when you output info to the file.
print #1, text to print
for output
or Write #1, text to print
I haven't done most of this in a long time.
Open filename For output as handle will create a file if it doesn't exist.
_________________
Levi
"Darkness hides the light
Darkness keeps me from it
Darkness is my life
Darkness I am in it"
"Light and Darkness my life is filled with thee
Light and Darkness my life my destiny
Light and Darkness both my life they share
Light and Darkness does no one care"
Quotes from "Who I am" by Levi
<http://www.your-poetry.com/modules.php?name=News&file=article&sid=39971>

### Marc · 2004-08-01 20:27 · #B68482

I will have to test this, I don't think it works (as I took CBM's for trial and never worked). I will try diffrent things though. Thanks for the help Levi Wink .
_________________
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### KSNiloc · 2004-08-01 21:11 · #B68504

VB has gone to IO stream, Levi.
But the old commands are still there for backwards compatability. They have different names though.
_________________
Pawn.

### Marc · 2004-08-01 21:35 · #B68525

And the new way to save is?
_________________
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### KSNiloc · 2004-08-01 22:12 · #B68553

First, you have to make a stream like so:

**Code:**

```
Friend MustInherit Class theStream

    Inherits System.IO.Stream

    Public Overrides ReadOnly Property CanRead() As Boolean

        Get

        End Get

    End Property

    Public Overrides ReadOnly Property CanSeek() As Boolean

        Get

        End Get

    End Property

    Public Overrides ReadOnly Property CanWrite() As Boolean

        Get

        End Get

    End Property

    Public Overrides Sub Flush()

    End Sub

    Public Overrides ReadOnly Property Length() As Long

        Get

        End Get

    End Property

    Public Overrides Property Position() As Long

        Get

        End Get

        Set(ByVal Value As Long)

        End Set

    End Property

    Public Overrides Function Read(ByVal buffer() As Byte, ByVal offset As Integer, ByVal count As Integer) As Integer

    End Function

    Public Overrides Function Seek(ByVal offset As Long, ByVal origin As System.IO.SeekOrigin) As Long

    End Function

    Public Overrides Sub SetLength(ByVal value As Long)

    End Sub

    Public Overrides Sub Write(ByVal buffer() As Byte, ByVal offset As Integer, ByVal count As Integer)

    End Sub

End Class
```

You'll probably want to fill in those things to be specific to your project.
Then an interface to the class:

**Code:**

```
Friend Class streamInterface

    Inherits theStream

End Class
```

To use the stream:

**Code:**

```
With New System.IO.StreamReader(New streamInterface)

'Code here

End With
```

StreamReader for reading, StreamWriter for writing.
Good luck, then. =)
_________________
Pawn.

### Eternal EoN · 2004-08-01 22:34 · #B68575

Holy crap. Why would anyone use something like that when they could just do this?!

**Code:**

```
'To write to files

Open "file.whatever" for Output as #1

Print #1, "I am a stupid man's idiot's retard."

Close #1

'To read from files

Open "file.whatever" for Input as #1

Input #1, retard$

Close #1

MsgBox retard$
```

_________________
[![](http://eon.ssxh.net/expo_ffurybanner.png)](http://eon.ssxh.net)
Here's the weight of the world on my shoulders...
Estuans interius ira vehementi...

### Marc · 2004-08-01 22:35 · #B68576

Thanks. You could have done that from the beginning ya know.
_________________
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### KSNiloc · 2004-08-01 22:35 · #B68577

EON: Because that doesn't work in vb.net.
_________________
Pawn.

### KSNiloc · 2004-08-01 22:39 · #B68581

Since you're here, I might as well mention how you can open a specific file:
In our theStream class, you'd want to replace the inherit with:

**Code:**

```
Inherits System.IO.FileStream
```

Then, add a sub like this (in theStream):

**Code:**

```
    Public Sub New()

        MyBase.New("C:\boo.txt", FileMode.Open)

    End Sub
```

Edit: It HAS to be sub new.
_________________
Pawn.
