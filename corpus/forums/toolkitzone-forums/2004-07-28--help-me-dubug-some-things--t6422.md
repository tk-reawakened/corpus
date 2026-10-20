---
kind: forum-thread
id: "toolkitzone-forums/6422"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "6422"
title: "Help me dubug some things"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=6422"
written: "2004-07-28T05:04:00"
last_post: "2004-07-31T04:13:00"
date_confidence: "exact"
captured: ["20040921165154"]
author: "Marc"
repliers: ["KSNiloc", "Ersuis", "Levi"]
authors: ["Marc", "KSNiloc", "Ersuis", "Levi"]
posts_present: 11
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_67676_amp_", captured: "20040921165154", sha256: "d7e473c7063b1e4b189f70b662ce4ca9bc3b6dae37e7b4906561b099e185beb2", wayback_url: "https://web.archive.org/web/20040921165154/http://www.toolkitzone.com/forums/viewtopic.php?p=67676&amp="}
links:
  - {url: "http://img76.exs.cx/img76/421/Muahahahaha.jpg", status: "external", local: null}
  - {url: "http://www.your-poetry.com/modules.php?name=News&file=article&sid=39971", status: "external", local: null}
---

# Help me dubug some things

### Marc · 2004-07-28 05:04 · #B66220

I made some VB programs. And I am getting some errors.
Some of them are "function or method not defined" ect.
Here are my codes. Please help me out with this.

**Code:**

```
Option Explicit

' Fcode program

Private Sub Form_MouseDown(Button As Integer, Shift As Integer, X As Single, Y As Single)

If Button = vbPopupMenuLeftButton Then ' pop up box on left click

PopupMenu (edt) ' open edit menu

End Sub

Private Sub newF_Click()

Dim theForm As New FCode ' call the form a part of Fcode

theForm.Show vbModal ' this form show

Set theForm = Nothing

End Sub

Private Sub opnf_Click()

'doesn't work at the moment

'opnf.Filter = "All Files (*.*)|*.*| Fight Code(*.FPG)|*.FPG|"

'opnf.FilterIndex = 2

'opnf.ShowOpen

'Program = opnf.FileName

End Sub

Private Sub svasf_Click()

'svasff.Filter = "All Files (*.*)|*.*| Fight Code(*.FPG)|*.FPG|"

'svasf.FilterIndex = 2

'svasf.ShowSave

'Program = svasf.FileName

End Sub
```

And the one that does work.

**Code:**

```
Private Sub cls4_Click()

End Sub

Private Sub clse_Click()

End Sub

Private Sub ext_Click()

Unload Frm

End Sub

Private Sub new_Click()

End Sub

Private Sub nw_Click()

Dim theForm As New FCode

theForm.Show vbModal

Set theForm = Nothing

End Sub
```

_________________
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### Marc · 2004-07-28 17:31 · #B66398

Also, the probem is that I can't save (No saveAs dialog) and I can't open (no open dialog).
_________________
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### KSNiloc · 2004-07-29 02:03 · #B66691

"All Files (*.*)|*.*| Fight Code(*.FPG)|*.FPG|" is wrong
"All Files (*.*)|*.*| Fight Code(*.FPG)|*.FPG" is right
No |. Also, don't use the control, use API. Pre-98 doesn't support the control.
_________________
Pawn.

### Marc · 2004-07-29 02:10 · #B66693

The API? Is is that little image that is "supposed" to be in my drawing bar (because if it is, it's not there Crying or Very sad)?
_________________
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### Ersuis · 2004-07-29 02:48 · #B66710

**KSNiloc wrote:**

> Pre-98 doesn't support the control.
>

Yes it (Windows 95, obviously not Win3.1) does. I just wrote a test VB program using the Common Dialog Control, and lo!, it works.

**Quote:**

> Also, don't use the control, use API.
>

'Expert' blanket statements have a lot more punch if you provide rationale.
_________________
-Curt

### Marc · 2004-07-29 02:53 · #B66714

**Ersuis wrote:**

> Yes it (Windows 95, obviously not Win3.1) does. I just wrote a test VB program using the Common Dialog Control, and lo!, it works.
>

So can you find what's wrong and tell me what it is and how to fix it?

**Ersuis wrote:**

>
> **Quote:**
>
> > Also, don't use the control, use API.
> >
>
> 'Expert' blanket statements have a lot more punch if you provide rationale.
>

He's right.
_________________
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### KSNiloc · 2004-07-29 03:03 · #B66722

Ersuis.
I have not argued with you as you are usually right (heh...).
But some versions os 95, AND EVEN 98 DO NOT have the control registered by default. That is why so many people - here alone - cannot use programs that use the control.
Besides, the control is just an interface to the API.
_________________
Pawn.

### Marc · 2004-07-29 03:07 · #B66725

Which I can activate how?
_________________
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### Levi · 2004-07-31 04:08 · #B67672

Check the spellings of all of your commands and functions...make sure objects are fine. Also send me the whole code, maybe I can help a little bit better if I know exactly what's going on.
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

### Levi · 2004-07-31 04:09 · #B67673

As for the API unless someone here will give you the direct answer look for API calling in the MSDN libarary on microsoft's website. Also look up Common Dialog API. This should give you a slight start and a bit of understanding as to what you are doing.
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

### Marc · 2004-07-31 04:13 · #B67676

No worrys Levi, I got the thing figured out.
1) I forgot to make a command dialog box (had to find the dll it was
called)
2) One command was spelled wrong (don't ask how).
Some one lock this; as it has been fixed Razz............
_________________
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)
