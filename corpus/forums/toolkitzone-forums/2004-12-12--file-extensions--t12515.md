---
kind: forum-thread
id: "toolkitzone-forums/12515"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "12515"
title: "File Extensions"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12515"
written: "2004-12-12T17:56:00"
last_post: "2004-12-14T02:31:00"
date_confidence: "exact"
captured: ["20041228072726"]
author: "Talyn"
repliers: ["sivart", "Akura_TheDragonBlader", "saberknight", "Colin", "Levi", "Marc"]
authors: ["Talyn", "sivart", "Akura_TheDragonBlader", "saberknight", "Colin", "Levi", "Marc"]
posts_present: 11
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_139310_amp_", captured: "20041228072726", sha256: "d0f207454ac4da4793df7f0778a20e20fb51fb2f2290c8a46671c5240759d971", wayback_url: "https://web.archive.org/web/20041228072726/http://www.toolkitzone.com/forums/viewtopic.php?p=139310&amp="}
links: []
---

# File Extensions

### Talyn · 2004-12-12 17:56 · #B138483

Ok, say you want to make a RPGCode Editor in VB.NET. How would you be able to save programs with the .prg file extension?
VB.NET's probably not the best thing to make a code editor in is it? Lol

### sivart · 2004-12-12 18:03 · #B138489

I'm not sure about .NET , VB6 i could help.. making this a usless post.... Confused

### Talyn · 2004-12-12 18:06 · #B138492

Try it! I don't mind. You'd quickly find out if it was wrong when you run the program! lol

### sivart · 2004-12-12 18:09 · #B138494

The only problem is im getting .NET for X-Mas so i dont have it yet .... Sad

### Talyn · 2004-12-12 18:21 · #B138503

I have the opposite problem. I'm trying to find a copy of VB6!

### Akura_TheDragonBlader · 2004-12-12 18:38 · #B138512

**Twin Keyblade wrote:**

> Ok, say you want to make a RPGCode Editor in VB.NET. How would you be able to save programs with the .prg file extension?
> VB.NET's probably not the best thing to make a code editor in is it? Lol
>

Uhh, I think this would be a good start:

**Code:**

```
dim objFile as IO.Streamwriter = New IO.Streamwriter("C:\The code editor\program.prg")

objFile.Write(the actual RPGCoding text here from wherever it is typed)

objFile.Close()
```

Note the .prg extension I gave program.prg. That's all you have to do to give it an extension, put it there when you create the file.

### saberknight · 2004-12-12 19:26 · #B138535

if you were making a code editor the program code would probly be typed into a richtextbox so for a "save as" type function you would use something like
Dim filename As String
Dim sw As StreamWriter
Try
sdlgTextFile.AddExtension = True
sdlgTextFile.CheckPathExists = True
sdlgTextFile.CreatePrompt = False
sdlgTextFile.OverwritePrompt = True
sdlgTextFile.ValidateNames = True
sdlgTextFile.ShowHelp = True
sdlgTextFile.DefaultExt = "txt"
sdlgTextFile.FileName = filename
sdlgTextFile.Filter = _
"RPG Code(*.prg)|*.prg|" & _
"All files|*.*"
sdlgTextFile.FilterIndex = 1
If sdlgTextFile.ShowDialog() = DialogResult.OK Then
filename = sdlgTextFile.FileName
sw = New StreamWriter(filename)
sw.Write(richtextbox1.Text)
End If
' End With
'Catch exp As Exception
' MessageBox.Show(exp.Message, form1.Text)
Finally
If Not (sw Is Nothing) Then
sw.Close()
End If
End Try
of course replacing the richtextbox1 with what ever is holding the code i recommend a richtextbox they are easier to manipulate also the error handling can be changed to what ever you want in this case it is changing the forms title bar to reflect the error you may want to use a dialog box to display the error or not display it at all possibly even log it or send it do a error report server
PS. if it can be done in vb6 vb.net can do it better you just have to know how Cool

### Colin · 2004-12-12 19:33 · #B138538

What he wants is to associate a file with his program. Use this, note that I DID NOT WRITE IT, but it does work well:

**Code:**

```
Option Explicit

Private Const REG_SZ As Long = &H1

Private Const REG_DWORD As Long = &H4

Private Const HKEY_CLASSES_ROOT As Long = &H80000000

Private Const HKEY_CURRENT_USER As Long = &H80000001

Private Const HKEY_LOCAL_MACHINE As Long = &H80000002

Private Const HKEY_USERS As Long = &H80000003

Private Const ERROR_SUCCESS As Long = 0

Private Const ERROR_BADDB As Long = 1009

Private Const ERROR_BADKEY As Long = 1010

Private Const ERROR_CANTOPEN As Long = 1011

Private Const ERROR_CANTREAD As Long = 1012

Private Const ERROR_CANTWRITE As Long = 1013

Private Const ERROR_OUTOFMEMORY As Long = 14

Private Const ERROR_INVALID_PARAMETER As Long = 87

Private Const ERROR_ACCESS_DENIED As Long = 5

Private Const ERROR_MORE_DATA As Long = 234

Private Const ERROR_NO_MORE_ITEMS As Long = 259

Private Const KEY_ALL_ACCESS As Long = &H3F

Private Const REG_OPTION_NON_VOLATILE As Long = 0

Private Declare Function RegCloseKey Lib "advapi32.dll" _

    (ByVal hKey As Long) As Long

Private Declare Function RegCreateKeyEx _

    Lib "advapi32.dll" Alias "RegCreateKeyExA" _

    (ByVal hKey As Long, _

    ByVal lpSubKey As String, _

    ByVal Reserved As Long, _

    ByVal lpClass As String, _

    ByVal dwOptions As Long, _

    ByVal samDesired As Long, _

    ByVal lpSecurityAttributes As Long, _

    phkResult As Long, _

    lpdwDisposition As Long) As Long

Private Declare Function RegOpenKeyEx _

    Lib "advapi32.dll" Alias "RegOpenKeyExA" _

    (ByVal hKey As Long, _

    ByVal lpSubKey As String, _

    ByVal ulOptions As Long, _

    ByVal samDesired As Long, _

    phkResult As Long) As Long

Private Declare Function RegSetValueExString _

    Lib "advapi32.dll" Alias "RegSetValueExA" _

    (ByVal hKey As Long, _

    ByVal lpValueName As String, _

    ByVal Reserved As Long, _

    ByVal dwType As Long, _

    ByVal lpValue As String, _

    ByVal cbData As Long) As Long

Private Declare Function RegSetValueExLong _

    Lib "advapi32.dll" Alias "RegSetValueExA" _

    (ByVal hKey As Long, _

    ByVal lpValueName As String, _

    ByVal Reserved As Long, _

    ByVal dwType As Long, _

    lpValue As Long, _

    ByVal cbData As Long) As Long

Public Sub CreateAssociation(sExtension As String, sApplication As String, sAppPath As String)

    Dim sPath As String

    Dim sAppExe As String

    sAppExe = sApplication

    CreateNewKey "." & sExtension, HKEY_CLASSES_ROOT

    SetKeyValue "." & sExtension, "", sApplication & ".Document", REG_SZ

    CreateNewKey sApplication & ".Document\shell\open\command", HKEY_CLASSES_ROOT

    SetKeyValue sApplication & ".Document", "", sApplication, REG_SZ

    sPath = sAppPath & " %1"

    SetKeyValue sApplication & ".Document\shell\open\command", "", sPath, REG_SZ

    CreateNewKey "Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\." _

    & sExtension, HKEY_CURRENT_USER

    SetKeyValue "Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\." _

    & sExtension, "Application", sAppExe, REG_SZ

    CreateNewKey "Applications\" & sAppExe & "\shell\open\command", HKEY_CLASSES_ROOT

    SetKeyValue "Applications\" & sAppExe & "\shell\open\command", "", sPath, REG_SZ

End Sub

Private Function SetValueEx(ByVal hKey As Long, _

    sValueName As String, _

    lType As Long, _

    vValue As Variant) As Long

    Dim nValue As Long

    Dim sValue As String

    Select Case lType

        Case REG_SZ

        sValue = vValue & chr$(0)

        SetValueEx = RegSetValueExString(hKey, _

        sValueName, _

        0&, _

        lType, _

        sValue, _

        Len(sValue))

        Case REG_DWORD

        nValue = vValue

        SetValueEx = RegSetValueExLong(hKey, _

        sValueName, _

        0&, _

        lType, _

        nValue, _

        4)

    End Select

End Function

Private Sub CreateNewKey(sNewKeyName As String, _

    lPredefinedKey As Long)

    Dim hKey As Long

    Dim result As Long

    Call RegCreateKeyEx(lPredefinedKey, _

    sNewKeyName, 0&, _

    vbNullString, _

    REG_OPTION_NON_VOLATILE, _

    KEY_ALL_ACCESS, 0&, hKey, result)

    Call RegCloseKey(hKey)

End Sub

Private Sub SetKeyValue(sKeyName As String, _

    sValueName As String, _

    vValueSetting As Variant, _

    lValueType As Long)

    Dim hKey As Long

    Call RegOpenKeyEx(HKEY_CLASSES_ROOT, _

    sKeyName, 0, _

    KEY_ALL_ACCESS, hKey)

    Call SetValueEx(hKey, _

    sValueName, _

    lValueType, _

    vValueSetting)

    Call RegCloseKey(hKey)

End Sub
```

### Talyn · 2004-12-12 20:57 · #B138594

Thanks everyone. That's answered my question perfectly.
Thanks for the association code as well Colin, that's something I'd dreaded asking for!
Just a general question: it is possible to create a RPGCode Editor in VB isn't it? I can seee how everything would work, colour-coding may be a problem, but I could create a basic one for practise ok I reckon.

### Levi · 2004-12-13 19:11 · #B139083

It is indeed possible. I myself, along with a few others, either have or are hoping to use VB to make such a thing easier.
I've taken extreme wrong turns in my implimentation but it is definatly possible. In .NET and 6.0. I have both so I have a general knowledge of their differences.

### Marc · 2004-12-14 02:31 · #B139310

**Akura_TheDragonBlader wrote:**

>
> **Code:**
>
> ```
> dim objFile as IO.Streamwriter = New IO.Streamwriter("C:\The code editor\program.prg")
>
>
> objFile.Write(the actual RPGCoding text here from wherever it is typed)
>
>
> objFile.Close()
> ```
>
> Note the .prg extension I gave program.prg. That's all you have to do to give it an extension, put it there when you create the file.
>

I think:

**Code:**

```
Dim objFile as IO.Streamwriter = new IO.Streamwriter("C:\The code editor\program.prg")

objFile.Write = textbox1.txt

objFile.close()
```

I think that would work better and easily changeable rather then adding it to the program everytime it's ran Razz.
