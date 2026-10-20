---
kind: forum-thread
id: "toolkitzone-forums/11890"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "11890"
title: "What is the easiest method of saving to a file in VB?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11890"
written: "2004-11-29T01:20:00"
last_post: "2004-11-29T06:22:00"
date_confidence: "exact"
captured: ["20041226222702"]
author: "TK Apprentice"
repliers: ["joao_foscarini", "nova11", "sivart", "Akura_TheDragonBlader", "Colin", "Levi"]
authors: ["TK Apprentice", "joao_foscarini", "nova11", "sivart", "Akura_TheDragonBlader", "Colin", "Levi"]
posts_present: 8
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_131507_amp_", captured: "20041226222702", sha256: "5e2e5cac436312f771db6da799d28f8d96f82d7194b387300d4ec5d3def640e7", wayback_url: "https://web.archive.org/web/20041226222702/http://www.toolkitzone.com/forums/viewtopic.php?p=131507&amp="}
links: []
---

# What is the easiest method of saving to a file in VB?

### TK Apprentice · 2004-11-29 01:20 · #B131355

What is the easiest method of saving to a file in VB?

### joao_foscarini · 2004-11-29 01:25 · #B131360

err... what do you mean?

### nova11 · 2004-11-29 01:27 · #B131362

Compile and .exe it?

### TK Apprentice · 2004-11-29 01:32 · #B131364

I mean saving the contents of a text box etc to a file like c:\text.text

### sivart · 2004-11-29 01:47 · #B131369

Damit i hit preview and exited ok ill just show the basics an dif you need help ill go into detail
First you need Common Dialog controls Enabled (Ctrl+T) and find it then make on name it CD1 and try this...
Private Sub mnuFileOpen_Click()
Dim fs As New FileSystemObject
cd1.ShowOpen
Me.Caption = "ProgramNote - " & cd1.FileTitle
Me.Refresh
Open cd1.FileName For Input As #1
text1.Text = Input(LOF(1), 1)
Close #1
Else
MsgBox "File not found!", vbExclamation + vbOKOnly, "Error"
End If
End Sub
I think thats it..

### Akura_TheDragonBlader · 2004-11-29 02:03 · #B131373

I did it using Streamwriter in .Net.

**Code:**

```
'Whatever statements you put at top

Imports System.IO 'probably not neccessary

'Whatever else

dim objFile as IO.Streamwriter = New IO.Streamwriter("C:\text\text.txt")

objFile.Write("Some text")

objFile.Writeline("Some more text")
```

Simple, eh? I may have messed up something, but I've got some working code in a zip file that does it. Of course, this creates a new file. I'm not entirely sure how to open and change an existing file at the moment.

### Colin · 2004-11-29 04:16 · #B131457

"Imports" is like "using namespace". Since you typed IO. anyway, you defeat its point.

### Levi · 2004-11-29 06:22 · #B131507

Go figure Colin but that's how a lot of people are taught to do it. My own text book says to do it that way.
But yeah, depnding on your version of VB 6.0 or lower, or .NET you will do it different ways. In fact I belive VB 6 also has another method of file opening. Can't remember what it is though. Been such a long time. Oh, that's right. FileSystemObject. Stupid me.
Sivart, why did you declare fs to be a FileSystemObject if you weren't going to use it in this example? That's a waste of memory.
To take Sivart's example to a more simplistic look. You can use the Open statement to open the file in three modes. Output, for file creation and writing. Input, for file reading. And Append for both reading and writing. Though Append will add text to the end of the file. I think there's another way like Random Access files use it but I don't know.
Open filename For Mode as Filehandle.
Usually File handle is a number preceeded by a # but the most efficient way if you're opening many files is to use the FreeFile function in conjunction with a variable.
MyOpenFile = FreeFile
Open filename For Input as MyOpenFile
Then anything that has to deal with that file you can call using MyOpenFile.
Like in Sivart's example. LOF(1) is LengthOfFile(filehandle) in his example he gave a handle of 1 to his file. We would say LOF(MyOpenFile)
And don't forget to close your file when you're done using it
Close(MyOpenFile) or Close (1)
Hope that along with these others helps.
