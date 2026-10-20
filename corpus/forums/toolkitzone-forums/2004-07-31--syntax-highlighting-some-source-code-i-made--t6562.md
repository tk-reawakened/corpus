---
kind: forum-thread
id: "toolkitzone-forums/6562"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "6562"
title: "Syntax Highlighting...some source code I made..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=6562"
written: "2004-07-31T04:16:00"
last_post: "2004-08-02T14:28:00"
date_confidence: "exact"
captured: ["20040921165435"]
author: "Levi"
repliers: ["Marc", "computerdude800", "Xavier", "KSNiloc", "Dragonmaster"]
authors: ["Levi", "Marc", "computerdude800", "Xavier", "KSNiloc", "Dragonmaster"]
posts_present: 14
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_68948_amp_", captured: "20040921165435", sha256: "288dfb955e7e7d1a48e2a035d25dfd78f596fe732c80c2a6e17e458bbb1d2c40", wayback_url: "https://web.archive.org/web/20040921165435/http://www.toolkitzone.com/forums/viewtopic.php?p=68948&amp="}
links:
  - {url: "http://img76.exs.cx/img76/421/Muahahahaha.jpg", status: "external", local: null}
  - {url: "http://sinnovations.toolkitzone.com", status: "captured", local: "wayback/toolkitzone.com/sinnovations.toolkitzone.com/index"}
  - {url: "http://www.toolkitzone.com/blog.php?id=73", status: "captured", local: "wayback/toolkitzone.com/blog.php__id_73"}
  - {url: "http://www.toolkitzone.com/mygames/images/86/946.gif", status: "never-captured", local: null}
  - {url: "http://www.toolkitzone.com/site.php?mode=stats", status: "captured", local: "wayback/toolkitzone.com/site.php__mode_stats"}
  - {url: "http://www.your-poetry.com/modules.php?name=News&file=article&sid=39971", status: "external", local: null}
---

# Syntax Highlighting...some source code I made...

### Levi · 2004-07-31 04:16 · #B67677

Okay at the moment this source code, sucks. It does teh general information it will only highlight a command in blue if the command is recognized. If you have a ! or $ to signify a variable it transforms the color into the qbcolor 3. It also colors ( ) < > red. But it doesn''t recognize when you are changing something, it doesn't accept spacing in between a command name as a cancelation of the command or variable and so the colors don't change. It does do comment coloring. But it is the basic start and I give it here for others to improve upon. It is programmed in VB. I used the frontpage macro creater to do it so don't expect perfection.

**Quote:**

> Public MySyntaxLength As Integer, MyCommand As Integer, MyStartStr As Integer, MyEndStr As Integer
> Private Syntax(200) As String
> Public MyQuote As Integer, MyComment As Integer
> Private Sub CommandButton1_Click()
> Dim MyKeyCode As Integer
> Dim MyShift As Integer
> RichTextBox1.LoadFile ("M:\programming\rqbeta\rpgcode.txt")
> Dim MyText As String
> MyText = RichTextBox1.Text
> RichTextBox1.Text = ""
> For y = 1 To Len(MyText)
> MyKey$ = Mid$(MyText, y, 1)
> If MyKey$ = "#" Then
> MyKeyCode = Asc("3")
> MyShift = 1
> ElseIf MyKey$ = "(" Or MyKey$ = ")" Or MyKey$ = "<" Or MyKey$ = ">" Then
> Select Case MyKey$
> Case "("
> MyKeyCode = Asc("(")
> MyShift = 1
> Case ")"
> MyKeyCode = Asc(")")
> MyShift = 1
> Case "<"
> MyKeyCode = Asc(",")
> MyShift = 1
> Case ">"
> MyKeyCode = Asc(".")
> MyShift = 1
> Case "!"
> MyKeyCode = Asc("1")
> MyShift = 1
> Case "$"
> MyKeyCode = Asc("4")
> MyShift = 1
> Case Else
> MyKeyCode = Asc(MyKey$)
> MyShift = 0
> End Select
> End If
> RichTextBox1_MyKeyDown MyKeyCode, MyShift
> RichTextBox1.Text = RichTextBox1.Text + MyKey$
> Next
> End Sub
> Private Sub RichTextBox1_KeyDown(KeyCode As Integer, ByVal Shift As Integer)
> If KeyCode = 8 Or KeyCode = 46 Then
> Exit Sub
> ElseIf KeyCode = Asc("3") And Shift = 1 Then
> MyCommand = 1
> MyStartStr = RichTextBox1.SelStart
> 'RichTextBox1.SelColor = vbBlue
> ElseIf KeyCode = Asc("9") Or KeyCode = Asc("0") Or KeyCode = 188 Or KeyCode = 190 Then
> If Shift = 1 Then
> MyCommand = 0
> RichTextBox1.SelColor = vbRed
> End If
> ElseIf KeyCode = Asc("1") Or KeyCode = Asc("4") Then
> If Shift = 1 Then
> If MyCommand = 1 Then
> MyCommand = 2
> MyEndStr = RichTextBox1.SelStart + 1
> End If
> End If
> Else
> If Chr$(KeyCode) = " " Then
> MyCommand = 0
> End If
> MyEndStr = RichTextBox1.SelStart + 1
> RichTextBox1.SelStart = MyStartStr
> RichTextBox1.SelLength = MyEndStr - MyStartStr
> NewText = RichTextBox1.SelText
> For x = 1 To MySyntaxLength
> If UCase(NewText) = UCase(Syntax(x)) Then
> RichTextBox1.SelColor = vbBlue
> Exit For
> End If
> Next
> RichTextBox1.SelStart = MyEndStr
> RichTextBox1.SelColor = vbBlack
> End If
> End Sub
> Private Sub RichTextBox1_KeyUp(KeyCode As Integer, ByVal Shift As Integer)
> If MyCommand = 0 Then
> RichTextBox1.SelColor = vbBlack
> ElseIf MyCommand = 2 Then
> MyCommand = 0
> RichTextBox1.SelStart = MyStartStr
> RichTextBox1.SelLength = MyEndStr - MyStartStr
> RichTextBox1.SelColor = QBColor(3)
> RichTextBox1.SelStart = MyEndStr
> End If
> End Sub
> Private Sub UserForm_Initialize()
> Open "M:\programming\rqbeta\rpgcode.lst" For Input As #1
> While Not EOF(1)
> x = x + 1
> Input #1, Syntax(x)
> Wend
> MySyntaxLength = x
> Close #1
> End Sub
> Sub RichTextBox1_MyKeyDown(KeyCode As Integer, Shift As Integer)
> If KeyCode = 8 Or KeyCode = 46 Then
> Exit Sub
> ElseIf KeyCode = Asc("3") And Shift = 1 Then
> MyCommand = 1
> MyStartStr = RichTextBox1.SelStart
> 'RichTextBox1.SelColor = vbBlue
> ElseIf KeyCode = Asc("9") Or KeyCode = Asc("0") Or KeyCode = 188 Or KeyCode = 190 Then
> If Shift = 1 Then
> MyCommand = 0
> RichTextBox1.SelColor = vbRed
> End If
> ElseIf KeyCode = Asc("1") Or KeyCode = Asc("4") Then
> If Shift = 1 Then
> If MyCommand = 1 Then
> MyCommand = 2
> MyEndStr = RichTextBox1.SelStart + 1
> End If
> End If
> Else
> If Chr$(KeyCode) = " " Then
> MyCommand = 0
> End If
> MyEndStr = RichTextBox1.SelStart + 1
> RichTextBox1.SelStart = MyStartStr
> RichTextBox1.SelLength = MyEndStr - MyStartStr
> NewText = RichTextBox1.SelText
> For x = 1 To MySyntaxLength
> If UCase(NewText) = UCase(Syntax(x)) Then
> RichTextBox1.SelColor = vbBlue
> Exit For
> End If
> Next
> RichTextBox1.SelStart = MyEndStr
> RichTextBox1.SelColor = vbBlack
> End If
> End Sub
>

Yes unfortunatly I don't comment my code so I hope it's easy enough to figure out. it should be. Well good luck to you all, I'm done. I give up. I'm outta here, I program for fun never to finish.
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

### Marc · 2004-07-31 04:24 · #B67686

**Levi wrote:**

> I program for fun never to finish.
>

So that's why the plugin I needed never got fineshed.
Oh well Razz I can do it now.
Anyway, back to topic. I'm going to test that out and see if I can learn from it.
_________________
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### Levi · 2004-07-31 04:31 · #B67690

When I first met you I said I could only offer minimal service and abilities. I never promised much, I said I would try but would probably fail. Besides all of you never needed me, I was simply there for support and to help all of you learn and excell. That's my job, I don't make, I help. That's all I do.
I also said I didn't want to be mentioned but you disreguarded that.
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

### Marc · 2004-07-31 04:51 · #B67708

I did? Oh sorry. When?
We did learn and ecell, but your moral support is still valued Razz.
Also, when I compiled with VB it gave me about 70 errors. And I tryed everything. Buggy, buggy. Might be why it doesn't work *shrug*.
_________________
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### computerdude800 · 2004-07-31 09:00 · #B67750

Ahh the source code is..... its okay. If you need help with it why don't you go and look at the TK3's source code system. Or here why dont you look at my Phoenix's color sytem.

**Code:**

```
Function ColorSyntax(Source As String)

If Replace(Source, " ", "") = "" Then Exit Function

Dim rtbS As RichTextBox

Set rtbS = frmMain.ActiveForm.rtbDummy

Dim rtbMain As RichTextBox

Set rtbMain = frmMain.ActiveForm.rtbReal

frmMain.ActiveForm.rtbMain.Locked = True

frmMain.ActiveForm.rtbMain.MousePointer = 11

Dim CodeArray() As String

Dim CurrentLine As String

Dim Line As String

Dim I As Integer

CodeArray = Split(Source, vbCrLf)

For I = LBound(CodeArray) To UBound(CodeArray)

CurrentLine = CodeArray(I)

Line = LTrim(Replace(Replace(CurrentLine, " ", ""), vbTab, ""))

Select Case Left(Line, 1)

Case "*"

rtbS.Text = CurrentLine

rtbS.SelStart = 0

rtbS.SelLength = Len(CurrentLine)

rtbS.SelBold = False

rtbS.SelColor = RGB(100, 200, 100) 'Change color

rtbMain.SelRTF = rtbS.TextRTF & Chr(10) & Chr(13)

Case "{"

rtbS.Text = CurrentLine

rtbS.SelStart = rtbS.Find("{")

rtbS.SelLength = 1

rtbS.SelColor = RGB(0, 0, 0) 'Change color

rtbS.SelBold = True

If InStr(1, CurrentLine, "*") > 0 Then

rtbS.SelStart = InStr(1, CurrentLine, "*") - 1

rtbS.SelLength = Len(CurrentLine)

rtbS.SelBold = False

rtbS.SelColor = RGB(100, 200, 100) 'Change color

End If

rtbMain.SelRTF = rtbS.TextRTF & Chr(10) & Chr(13)

rtbS.SelBold = False

Case "}"

rtbS.Text = CurrentLine

rtbS.SelStart = rtbS.Find("}")

rtbS.SelLength = 1

rtbS.SelColor = RGB(0, 0, 0) 'Change color

rtbS.SelBold = True

If InStr(1, CurrentLine, "*") > 0 Then

rtbS.SelStart = InStr(1, CurrentLine, "*") - 1

rtbS.SelLength = Len(CurrentLine)

rtbS.SelBold = False

rtbS.SelColor = RGB(100, 200, 100) 'Change color

End If

rtbMain.SelRTF = rtbS.TextRTF & Chr(10) & Chr(13)

rtbS.SelBold = False

Case ":"

rtbS.Text = CurrentLine

rtbS.SelStart = rtbS.Find(":")

rtbS.SelLength = Len(CurrentLine)

rtbS.SelColor = RGB(0, 0, 0) 'Change color

rtbS.SelBold = True

If InStr(1, CurrentLine, "*") > 0 Then

rtbS.SelStart = InStr(1, CurrentLine, "*") - 1

rtbS.SelLength = Len(CurrentLine)

rtbS.SelBold = False

rtbS.SelColor = RGB(100, 200, 100) 'Change color

End If

rtbMain.SelRTF = rtbS.TextRTF & Chr(10) & Chr(13)

rtbS.SelBold = False

Case Else

If InStr(1, CurrentLine, "(") > 0 Then

rtbS.Text = CurrentLine

Dim Para As Long

Para = InStr(1, CurrentLine, "(") - 1

rtbS.SelStart = Para

rtbS.SelLength = Len(CurrentLine)

rtbS.SelBold = False

rtbS.SelColor = RGB(200, 100, 100) 'change color

rtbS.SelStart = 0

rtbS.SelLength = Para

rtbS.SelBold = False

rtbS.SelColor = RGB(100, 100, 200) 'change color

Dim comment As Long

comment = InStr(InStr(1, CurrentLine, ")"), CurrentLine, "*")

If comment > 0 Then

rtbS.SelStart = comment - 1

rtbS.SelLength = Len(CurrentLine)

rtbS.SelBold = False

rtbS.SelColor = RGB(100, 200, 100)

End If

rtbMain.SelRTF = rtbS.TextRTF & Chr(10) & Chr(13)

Else

If InStr(1, CurrentLine, "!") > 0 Or InStr(1, CurrentLine, "$") > 0 Then

rtbS.Text = CurrentLine

rtbS.SelStart = 0

rtbS.SelLength = Len(CurrentLine)

rtbS.SelBold = False

rtbS.SelColor = RGB(168, 81, 200) 'Change color

rtbMain.SelRTF = rtbS.TextRTF & Chr(10) & Chr(13)

Else

rtbS.Text = CurrentLine

rtbS.SelStart = 0

rtbS.SelLength = Len(CurrentLine)

rtbS.SelBold = False

rtbS.SelColor = RGB(100, 100, 200) 'Change color

rtbMain.SelRTF = rtbS.TextRTF & Chr(10) & Chr(13)

End If

End If

End Select

Next I

frmMain.ActiveForm.rtbMain.TextRTF = rtbMain.TextRTF

frmMain.ActiveForm.rtbMain.Locked = False

frmMain.ActiveForm.rtbMain.MousePointer = 0

End Function
```

Might be a little confusing, hope it helps some.
_________________
Ultimecia: SeeD, SeeD, SeeD, swarming through generations like locust! You shall pay for your meddling with a pain worst than death, I shall send you to a dimension where I rule you shall be my servants for enternity! I shall exterminate you 3 first!!
[Visit my Blog on the Development of Dragon Tales](http://www.toolkitzone.com/blog.php?id=73)

### Marc · 2004-07-31 17:22 · #B67864

What is with no one commenting on they're programs? I learn by example, and if I don't know what does where I can't learn. Ahh well, it's pretty straight forward.
_________________
![](http://img76.exs.cx/img76/421/Muahahahaha.jpg)

### Xavier · 2004-07-31 17:25 · #B67867

All this colouring code seems frightfully long, it shouldn't really be more than 50-70 lines and still be perfectly good. Geoff's colouring code in TK3 is pretty good.
_________________
toolkit zone :: [number crunch](http://www.toolkitzone.com/site.php?mode=stats)

### Levi · 2004-08-01 04:42 · #B68125

As for my errors...I have simply a button, a richtextbox(using the richedit control) and my form. I didn't change their names only their values so if you want to use this please make changes to the code itself or make your form accordingly.
Second I forgot to add a file I made called rpgcode.lst. This lists all of TK2's commands #Ai, #Mwin and so on. in the file I just copied and pasted the reference list from help3. THen I removed each blank line and left only the command name
*
@
#AI
And so on in that format. You'll need that.
As for fifty or seventy lines. My code would work fine doing just regular syntax coloring that is found in many editors that simply colors # ! $ ( ) < and >. It can be very simplistic. This is the starting point for more advanced coloring. It allows for the coloring of text and numbers as one color, variables as another, and commands as still another.
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

### KSNiloc · 2004-08-01 21:27 · #B68516

The only syntax coloring like the one you described is computerDude's.
Everyone else's does what you say you would like yours to do. Even the native TK3 editor.
_________________
Pawn.

### Levi · 2004-08-02 05:27 · #B68822

Phenoix is ver simplistic in its coloring. * stats everything after it is green. # states that everything after it is blue and () <> states everything after them is red.
RedRose only uses red coloring on ()<> and *
EuixCode the original carries a similar code to Phenoix except that colors only return to true normal black when you move to the next line. Otherwise it keeps track of the color you had before you changed colors. So changing form blue to red will only revert it to blue
EuixCode 2 is very interesting. It won't coloring anything another color after its colored something red, its very slow, and there is no coloring for commands only for comments and symbols.
Vortex v1 has many of the same problems as mentioned above. I won't go into detail. IT does however have that excellent VB quality to it with the popup dropdown box and hints for recognized commands.
I'd say so far my code matches that of most of the coding capabilities we've seen so far. With the exception of variable color coding that I added.
But I also haven't seen the source code for TK3. Or even tried it. maybe I will though, maybe I will.
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

### KSNiloc · 2004-08-02 06:00 · #B68827

Ah, then take a look at the TK3 syntax coloring when 3.04 comes out-- my real-time is pretty good to go with Geoff's excellent base.
_________________
Pawn.

### Dragonmaster · 2004-08-02 13:32 · #B68927

I created my own editor. My code is much smaller than what you have posted. It also takes the scroll bar into consideration, unlike Vortex.
_________________
Sit Erubu Sit ... Good Dragon.
[![](http://www.toolkitzone.com/mygames/images/86/946.gif)](http://sinnovations.toolkitzone.com)

### computerdude800 · 2004-08-02 14:14 · #B68940

hmmm, I should said something, that code your seeing is from my new version of Phoenix which is 3/4 done, that is a real time syntax system. Phoenix 3 is quite different than its predecessors, better GUI more features, quite stable, new plugin system (Not using VorteX's anymore), etc. But it probally wont be finished becuase I am making my own game maker now.
_________________
Ultimecia: SeeD, SeeD, SeeD, swarming through generations like locust! You shall pay for your meddling with a pain worst than death, I shall send you to a dimension where I rule you shall be my servants for enternity! I shall exterminate you 3 first!!
[Visit my Blog on the Development of Dragon Tales](http://www.toolkitzone.com/blog.php?id=73)

### Levi · 2004-08-02 14:28 · #B68948

Did I also mention that this is a rough draft code? That this code sucks? I think I did in my first one. Don't badger me about the length, it was made in the visual Basic editor of Frontpage 2000. Originally made to integrate with RapidQ's RichTextBox. However VB has a few more options that Rapid Q doesn't so it never fully worked. I leave this here for those who wish to look at it and learn a few things and maybe make it that much better. I did it in my spare time which I have very little of. I didn't over think it, i didn't look for shortcuts, I didn't try to figure out how to make it shorter. I simply made it to accept all code and do tiny little things based upon that alone. Sorry if you don't approve.
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
