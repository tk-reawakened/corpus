---
kind: forum-thread
id: "toolkitzone-forums/6984"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "6984"
title: "In VB, how do copy a Directory into a text box???"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=6984"
written: "2004-08-11T00:31:00"
last_post: "2004-08-13T15:16:00"
date_confidence: "exact"
captured: ["20040818050354", "20040923105355"]
author: "Master Tamer"
repliers: ["KSNiloc", "Marc", "Woozy"]
authors: ["Master Tamer", "KSNiloc", "Marc", "Woozy"]
posts_present: 12
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_73018_amp_", captured: "20040818050354", sha256: "7784b6e4513088a1c442a1388ac768eb954fd7895f77526bf822c2fbbee57ec6", wayback_url: "https://web.archive.org/web/20040818050354/http://www.toolkitzone.com/forums/viewtopic.php?p=73018&amp="}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_74682_amp_", captured: "20040923105355", sha256: "5155c04b818565bc692cf2cf67d09f334d8fa46df262a2910cd5c61c26f06f2f", wayback_url: "https://web.archive.org/web/20040923105355/http://www.toolkitzone.com/forums/viewtopic.php?p=74682&amp="}
links:
  - {url: "http://img21.exs.cx/img21/3906/Me1.jpg", status: "external", local: null}
  - {url: "http://thanian-nation.com/", status: "external", local: null}
  - {url: "http://thanian-nation.com/dwd/", status: "external", local: null}
  - {url: "http://thanian-nation.com/tkland/", status: "external", local: null}
  - {url: "http://www.danasoft.com/sig/LH21222.jpg", status: "external", local: null}
  - {url: "http://www.qtk.ip3.com", status: "external", local: null}
  - {url: "http://www.rpgadev.com", status: "external", local: null}
  - {url: "http://www.rpgadev.com/header1.jpg", status: "external", local: null}
  - {url: "http://www.thanian-nation.com/temp/tklandbannerad.jpg", status: "external", local: null}
  - {url: "http://www.toolkitzone.com/blog.php?id=380", status: "captured", local: "wayback/toolkitzone.com/blog.php__id_380"}
---

# In VB, how do copy a Directory into a text box???

### Master Tamer · 2004-08-11 00:31 · #B72958

What I want to happen is:
1) A open File dialog opens
2) User chooses a file
3) The Directory of the file is copied into the text box.
This is what I got:

**Code:**

```

Dim FN as String

OpenFileDialog1.Filter = "bitmap (*.bmp)|*.bmp*|Jpeg (*.jpg)|*.jpg*|GIF (*.gif)|*.gif*|PNG (*.png)|*.png*"

        OpenFileDialog1.FilterIndex = 1

        FN = OpenFileDialog1.ShowDialog()

        TextBox4.Text = FN
```

So what's wrong?
_________________
MMORPG creation
[![](http://www.rpgadev.com/header1.jpg)](http://www.rpgadev.com)

### KSNiloc · 2004-08-11 02:03 · #B73015

**Code:**

```
        With New OpenFileDialog

            .Filter = "bitmap (*.bmp)|*.bmp*|Jpeg (*.jpg)|*.jpg*|GIF (*.gif)|*.gif*|PNG (*.png)|*.png*"

            .ShowDialog()

            If .FileName <> "" Then

                'There's no easy way to obtain the directory of the file, but you

                'probably meant the full path anyway. .FileName now contains it.

            End If

        End With
```

_________________
I xeroxed a mirror - now I have an extra xerox machine.

### Marc · 2004-08-11 02:06 · #B73018

Niloc, your coding habbits are quite odd. Nothing wrong with it, but sheesh!
*cough* How do you make it print what's entered in a RichTextBox? *cough*
Razz.
_________________
![](http://img21.exs.cx/img21/3906/Me1.jpg)
[my blog](http://www.toolkitzone.com/blog.php?id=380)
![](http://www.danasoft.com/sig/LH21222.jpg)
The mouse that knows every thing about your comp! Razz
DeathFlame
Favorite mods (in order)
1)Xavier, 2) Dan, 3)Spyder, 4) Asimir, 5)Doc_wellsy, 6) Woozy, 6) Indy, 7)Seafroggies, 8)R048482, 9)Nick.
Watch the moon every night you can... for Xedret... For him the night will just not arrive.

### KSNiloc · 2004-08-11 03:12 · #B73062

I fail to see what's 'odd' about that. Sheesh.
That's not an easy task in VB.NET...

**Code:**

```
'==========================================================================================

'YOU MAY NOT REMOVE THIS NOTICE

'==========================================================================================

'VB.NET Printing Example

'All Contents Copyright 2004, Colin James Fitzpatrick

'==========================================================================================

'YOU MAY NOT REMOVE THIS NOTICE

'==========================================================================================

Option Strict On

Option Explicit On

Option Compare Binary

Imports System.Drawing.Printing

Friend Class clsMain

    Private Shared WithEvents cmdPrint As New Button

    Private Shared rtfBox As New RichTextBox

    Private Shared currentLine As Integer

    Public Shared Sub Main()

        'Create a new form

        With New Form

            'With that form's control collection

            With .Controls

                'Add the rtfBox and the print button

                .Add(cmdPrint)

                .Add(rtfBox)

            End With

            'With the print button

            With cmdPrint

                .Text = "Print"

                .Location = New Point(100, 1)

                .Size = New Size(80, 20)

            End With

            'With the rtfBox

            With rtfBox

                .Text = "Some text"

                .Location = New Point(0, 0)

                .Size = New Size(100, 500)

            End With

            'Setup the form

            .Size = New Size(200, 500)

            .StartPosition = FormStartPosition.CenterScreen

            .Text = "Printing Example"

            .MinimizeBox = False

            .MaximizeBox = False

            .SizeGripStyle = SizeGripStyle.Hide

            'Show the form

            .ShowDialog()

            'Free up memory used by the form

            .Dispose()

        End With 'new form

    End Sub 'main

    Private Shared Sub cmdPrint_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles cmdPrint.Click

        'The print button was clicked

        With New PrintDocument

            'Note the document name for print queues

            .DocumentName = "Example Print Job"

            'Create a delegate

            AddHandler .PrintPage, AddressOf printPage

            'Try to print the document

            Try

                .Print()

            Catch theException As Exception

                MsgBox(theException.Message, , "Error!")

            End Try 'try to print

        End With 'new printDocument

    End Sub 'cmdPrint_click

    Private Shared Sub printPage(ByVal sender As Object, ByVal theEvent As PrintPageEventArgs)

        'Set the font

        Dim printFont As New Font("Comic Sans MS", 12)

        'Calculate lines per page

        Dim linesPerPage As Single = theEvent.MarginBounds.Height / printFont.GetHeight(theEvent.Graphics)

        'Default to re-calling this sub

        theEvent.HasMorePages = True

        'Split up the text

        Dim lines() As String

        lines = Split(rtfBox.Text, vbCrLf)

        'Loop over each line

        For a As Single = 0 To linesPerPage

            'Calculate y position of this line on page

            Dim y As Single = theEvent.MarginBounds.Top + a * printFont.GetHeight(theEvent.Graphics)

            'Read a line from the rtfBox

            Dim theLine As String

            Try

                'Try to read the current line from the array

                theLine = lines(currentLine)

                currentLine += 1

            Catch

                'End of the box

                theLine = ""

                theEvent.HasMorePages = False

                Return

            Finally

                'Try to print the line

                Try

                    theEvent.Graphics.DrawString(theLine, printFont, Brushes.Black, theEvent.MarginBounds.Left, y, New StringFormat)

                Catch theException As Exception

                    MsgBox(theException.Message, , "Error!")

                End Try 'print the line

            End Try 'read a line

        Next 'a

    End Sub 'printPage

End Class 'clsMain
```

### Woozy · 2004-08-11 11:09 · #B73150

**Word2 wrote:**

> Niloc, your coding habbits are quite odd. Nothing wrong with it, but sheesh!
> *cough* How do you make it print what's entered in a RichTextBox? *cough*
> Razz.
>

I don't really see what is odd about it, if you're talking about the With, it's just to make the rest easier to type.
Sheesh Razz
_________________
[Thanian Nation](http://thanian-nation.com/)
[DarkwinterDreams](http://thanian-nation.com/dwd/)
[Quintessential](http://www.qtk.ip3.com)
[![](http://www.thanian-nation.com/temp/tklandbannerad.jpg)](http://thanian-nation.com/tkland/)

### Master Tamer · 2004-08-11 15:18 · #B73200

hmmmmmmmmmmmm....
TK can do it, so...
_________________
MMORPG creation
[![](http://www.rpgadev.com/header1.jpg)](http://www.rpgadev.com)

### Marc · 2004-08-11 15:20 · #B73203

**KSNiloc wrote:**

> I fail to see what's 'odd' about that. Sheesh.
> That's not an easy task in VB.NET...
>
> **Code:**
>
> ```
> '==========================================================================================
>
>
> 'YOU MAY NOT REMOVE THIS NOTICE
>
>
> '==========================================================================================
>
>
> 'VB.NET Printing Example
>
>
> 'All Contents Copyright 2004, Colin James Fitzpatrick
>
>
> '==========================================================================================
>
>
> 'YOU MAY NOT REMOVE THIS NOTICE
>
>
> '==========================================================================================
>
>
>
>
>
> Option Strict On
>
>
> Option Explicit On
>
>
> Option Compare Binary
>
>
>
>
>
> Imports System.Drawing.Printing
>
>
>
>
>
> Friend Class clsMain
>
>
>
>
>
>     Private Shared WithEvents cmdPrint As New Button
>
>
>     Private Shared rtfBox As New RichTextBox
>
>
>     Private Shared currentLine As Integer
>
>
>
>
>
>     Public Shared Sub Main()
>
>
>
>
>
>         'Create a new form
>
>
>         With New Form
>
>
>
>
>
>             'With that form's control collection
>
>
>             With .Controls
>
>
>                 'Add the rtfBox and the print button
>
>
>                 .Add(cmdPrint)
>
>
>                 .Add(rtfBox)
>
>
>             End With
>
>
>
>
>
>             'With the print button
>
>
>             With cmdPrint
>
>
>                 .Text = "Print"
>
>
>                 .Location = New Point(100, 1)
>
>
>                 .Size = New Size(80, 20)
>
>
>             End With
>
>
>
>
>
>             'With the rtfBox
>
>
>             With rtfBox
>
>
>                 .Text = "Some text"
>
>
>                 .Location = New Point(0, 0)
>
>
>                 .Size = New Size(100, 500)
>
>
>             End With
>
>
>
>
>
>             'Setup the form
>
>
>             .Size = New Size(200, 500)
>
>
>             .StartPosition = FormStartPosition.CenterScreen
>
>
>             .Text = "Printing Example"
>
>
>             .MinimizeBox = False
>
>
>             .MaximizeBox = False
>
>
>             .SizeGripStyle = SizeGripStyle.Hide
>
>
>
>
>
>             'Show the form
>
>
>             .ShowDialog()
>
>
>
>
>
>             'Free up memory used by the form
>
>
>             .Dispose()
>
>
>
>
>
>         End With 'new form
>
>
>
>
>
>     End Sub 'main
>
>
>
>
>
>     Private Shared Sub cmdPrint_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles cmdPrint.Click
>
>
>
>
>
>         'The print button was clicked
>
>
>         With New PrintDocument
>
>
>
>
>
>             'Note the document name for print queues
>
>
>             .DocumentName = "Example Print Job"
>
>
>
>
>
>             'Create a delegate
>
>
>             AddHandler .PrintPage, AddressOf printPage
>
>
>
>
>
>             'Try to print the document
>
>
>             Try
>
>
>                 .Print()
>
>
>             Catch theException As Exception
>
>
>                 MsgBox(theException.Message, , "Error!")
>
>
>             End Try 'try to print
>
>
>
>
>
>         End With 'new printDocument
>
>
>
>
>
>     End Sub 'cmdPrint_click
>
>
>
>
>
>     Private Shared Sub printPage(ByVal sender As Object, ByVal theEvent As PrintPageEventArgs)
>
>
>
>
>
>         'Set the font
>
>
>         Dim printFont As New Font("Comic Sans MS", 12)
>
>
>
>
>
>         'Calculate lines per page
>
>
>         Dim linesPerPage As Single = theEvent.MarginBounds.Height / printFont.GetHeight(theEvent.Graphics)
>
>
>
>
>
>         'Default to re-calling this sub
>
>
>         theEvent.HasMorePages = True
>
>
>
>
>
>         'Split up the text
>
>
>         Dim lines() As String
>
>
>         lines = Split(rtfBox.Text, vbCrLf)
>
>
>
>
>
>         'Loop over each line
>
>
>         For a As Single = 0 To linesPerPage
>
>
>
>
>
>             'Calculate y position of this line on page
>
>
>             Dim y As Single = theEvent.MarginBounds.Top + a * printFont.GetHeight(theEvent.Graphics)
>
>
>
>
>
>             'Read a line from the rtfBox
>
>
>             Dim theLine As String
>
>
>
>
>
>             Try
>
>
>                 'Try to read the current line from the array
>
>
>                 theLine = lines(currentLine)
>
>
>                 currentLine += 1
>
>
>
>
>
>             Catch
>
>
>                 'End of the box
>
>
>                 theLine = ""
>
>
>                 theEvent.HasMorePages = False
>
>
>                 Return
>
>
>
>
>
>             Finally
>
>
>                 'Try to print the line
>
>
>                 Try
>
>
>                     theEvent.Graphics.DrawString(theLine, printFont, Brushes.Black, theEvent.MarginBounds.Left, y, New StringFormat)
>
>
>                 Catch theException As Exception
>
>
>                     MsgBox(theException.Message, , "Error!")
>
>
>                 End Try 'print the line
>
>
>
>
>
>             End Try 'read a line
>
>
>
>
>
>         Next 'a
>
>
>
>
>
>     End Sub 'printPage
>
>
>
>
>
> End Class 'clsMain
> ```
>

The thing I ment by loopieness is this: .dispose
1) you have to have a perticular form to dispose.
2) You make everything so compleatly long. People in a VB helpforum I am getting help at showed me about 10 line code. (although it just made it print one line I'm sure a for loop could goto EOF).
Allthough I definatly will try your code.
_________________
![](http://img21.exs.cx/img21/3906/Me1.jpg)
[my blog](http://www.toolkitzone.com/blog.php?id=380)
![](http://www.danasoft.com/sig/LH21222.jpg)
The mouse that knows every thing about your comp! Razz
DeathFlame
Favorite mods (in order)
1)Xavier, 2) Dan, 3)Spyder, 4) Asimir, 5)Doc_wellsy, 6) Woozy, 6) Indy, 7)Seafroggies, 8)R048482, 9)Nick.
Watch the moon every night you can... for Xedret... For him the night will just not arrive.

### KSNiloc · 2004-08-11 17:18 · #B73304

You don't have to have a form to dispose.
You can dispose ANYTHING.
My code is long because I don't DEPEND ON A FORM. My code makes the form and displays it all with code.
_________________
I xeroxed a mirror - now I have an extra xerox machine.

### KSNiloc · 2004-08-11 17:23 · #B73308

**Woozy wrote:**

>
> **Word2 wrote:**
>
> > Niloc, your coding habbits are quite odd. Nothing wrong with it, but sheesh!
> > *cough* How do you make it print what's entered in a RichTextBox? *cough*
> > Razz.
> >
>
> I don't really see what is odd about it, if you're talking about the With, it's just to make the rest easier to type.
> Sheesh Razz
>

Actually the with in that case also enables my to instance a class without using an object variable. And it's faster.
Many reasons, Word2.

### Marc · 2004-08-13 01:58 · #B74423

**KSNiloc wrote:**

> I fail to see what's 'odd' about that. Sheesh.
> That's not an easy task in VB.NET...
>
> **Code:**
>
> ```
> '==========================================================================================
>
>
> 'YOU MAY NOT REMOVE THIS NOTICE
>
>
> '==========================================================================================
>
>
> 'VB.NET Printing Example
>
>
> 'All Contents Copyright 2004, Colin James Fitzpatrick
>
>
> '==========================================================================================
>
>
> 'YOU MAY NOT REMOVE THIS NOTICE
>
>
> '==========================================================================================
>
>
>
>
>
> Option Strict On
>
>
> Option Explicit On
>
>
> Option Compare Binary
>
>
>
>
>
> Imports System.Drawing.Printing
>
>
>
>
>
> Friend Class clsMain
>
>
>
>
>
>     Private Shared WithEvents cmdPrint As New Button
>
>
>     Private Shared rtfBox As New RichTextBox
>
>
>     Private Shared currentLine As Integer
>
>
>
>
>
>     Public Shared Sub Main()
>
>
>
>
>
>         'Create a new form
>
>
>         With New Form
>
>
>
>
>
>             'With that form's control collection
>
>
>             With .Controls
>
>
>                 'Add the rtfBox and the print button
>
>
>                 .Add(cmdPrint)
>
>
>                 .Add(rtfBox)
>
>
>             End With
>
>
>
>
>
>             'With the print button
>
>
>             With cmdPrint
>
>
>                 .Text = "Print"
>
>
>                 .Location = New Point(100, 1)
>
>
>                 .Size = New Size(80, 20)
>
>
>             End With
>
>
>
>
>
>             'With the rtfBox
>
>
>             With rtfBox
>
>
>                 .Text = "Some text"
>
>
>                 .Location = New Point(0, 0)
>
>
>                 .Size = New Size(100, 500)
>
>
>             End With
>
>
>
>
>
>             'Setup the form
>
>
>             .Size = New Size(200, 500)
>
>
>             .StartPosition = FormStartPosition.CenterScreen
>
>
>             .Text = "Printing Example"
>
>
>             .MinimizeBox = False
>
>
>             .MaximizeBox = False
>
>
>             .SizeGripStyle = SizeGripStyle.Hide
>
>
>
>
>
>             'Show the form
>
>
>             .ShowDialog()
>
>
>
>
>
>             'Free up memory used by the form
>
>
>             .Dispose()
>
>
>
>
>
>         End With 'new form
>
>
>
>
>
>     End Sub 'main
>
>
>
>
>
>     Private Shared Sub cmdPrint_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles cmdPrint.Click
>
>
>
>
>
>         'The print button was clicked
>
>
>         With New PrintDocument
>
>
>
>
>
>             'Note the document name for print queues
>
>
>             .DocumentName = "Example Print Job"
>
>
>
>
>
>             'Create a delegate
>
>
>             AddHandler .PrintPage, AddressOf printPage
>
>
>
>
>
>             'Try to print the document
>
>
>             Try
>
>
>                 .Print()
>
>
>             Catch theException As Exception
>
>
>                 MsgBox(theException.Message, , "Error!")
>
>
>             End Try 'try to print
>
>
>
>
>
>         End With 'new printDocument
>
>
>
>
>
>     End Sub 'cmdPrint_click
>
>
>
>
>
>     Private Shared Sub printPage(ByVal sender As Object, ByVal theEvent As PrintPageEventArgs)
>
>
>
>
>
>         'Set the font
>
>
>         Dim printFont As New Font("Comic Sans MS", 12)
>
>
>
>
>
>         'Calculate lines per page
>
>
>         Dim linesPerPage As Single = theEvent.MarginBounds.Height / printFont.GetHeight(theEvent.Graphics)
>
>
>
>
>
>         'Default to re-calling this sub
>
>
>         theEvent.HasMorePages = True
>
>
>
>
>
>         'Split up the text
>
>
>         Dim lines() As String
>
>
>         lines = Split(rtfBox.Text, vbCrLf)
>
>
>
>
>
>         'Loop over each line
>
>
>         For a As Single = 0 To linesPerPage
>
>
>
>
>
>             'Calculate y position of this line on page
>
>
>             Dim y As Single = theEvent.MarginBounds.Top + a * printFont.GetHeight(theEvent.Graphics)
>
>
>
>
>
>             'Read a line from the rtfBox
>
>
>             Dim theLine As String
>
>
>
>
>
>             Try
>
>
>                 'Try to read the current line from the array
>
>
>                 theLine = lines(currentLine)
>
>
>                 currentLine += 1
>
>
>
>
>
>             Catch
>
>
>                 'End of the box
>
>
>                 theLine = ""
>
>
>                 theEvent.HasMorePages = False
>
>
>                 Return
>
>
>
>
>
>             Finally
>
>
>                 'Try to print the line
>
>
>                 Try
>
>
>                     theEvent.Graphics.DrawString(theLine, printFont, Brushes.Black, theEvent.MarginBounds.Left, y, New StringFormat)
>
>
>                 Catch theException As Exception
>
>
>                     MsgBox(theException.Message, , "Error!")
>
>
>                 End Try 'print the line
>
>
>
>
>
>             End Try 'read a line
>
>
>
>
>
>         Next 'a
>
>
>
>
>
>     End Sub 'printPage
>
>
>
>
>
> End Class 'clsMain
> ```
>

I only wish it worked. YOu should download VB2005. Heh. I can't actualy print the text in the RichTextBox. Seeing as it cannot convert to string.
_________________
![](http://img21.exs.cx/img21/3906/Me1.jpg)
[my blog](http://www.toolkitzone.com/blog.php?id=380)
![](http://www.danasoft.com/sig/LH21222.jpg)
The mouse that knows every thing about your comp! Razz
DeathFlame
Favorite mods (in order)
1)Xavier, 2) Dan, 3)Spyder, 4) Asimir, 5)Doc_wellsy, 6) Woozy, 6) Indy, 7)Seafroggies, 8)R048482, 9)Nick.
Watch the moon every night you can... for Xedret... For him the night will just not arrive.

### KSNiloc · 2004-08-13 03:01 · #B74444

Oh for pete's sake, that is perfectly working vb.net code. You have vb express which is simplified beyond belief. I don't even know why I bother providing you with help.

### Marc · 2004-08-13 15:16 · #B74682

Try providing help for expresss Wink.
_________________
![](http://img21.exs.cx/img21/3906/Me1.jpg)
[my blog](http://www.toolkitzone.com/blog.php?id=380)
![](http://www.danasoft.com/sig/LH21222.jpg)
The mouse that knows every thing about your comp! Razz
DeathFlame
Favorite mods (in order)
1)Xavier, 2) Dan, 3)Spyder, 4) Asimir, 5)Doc_wellsy, 6) Woozy, 6) Indy, 7)Seafroggies, 8)R048482, 9)Nick.
Watch the moon every night you can... for Xedret... For him the night will just not arrive.
