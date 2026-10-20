---
kind: forum-thread
id: "toolkitzone-forums/10765"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "10765"
title: "VB winsock help NEEDED"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=10765"
written: "2004-10-29T00:52:00"
last_post: "2004-10-30T00:49:00"
date_confidence: "exact"
captured: ["20041226085704"]
author: "t0m"
repliers: ["nova11", "sivart", "Levi", "Akura_TheDragonBlader"]
authors: ["t0m", "nova11", "sivart", "Levi", "Akura_TheDragonBlader"]
posts_present: 8
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_118920_amp_", captured: "20041226085704", sha256: "b96f241224f9e7863cddb52847f5f8c74061fa3cd8bd5a7d5fbf0227b9e19bcc", wayback_url: "https://web.archive.org/web/20041226085704/http://www.toolkitzone.com/forums/viewtopic.php?p=118920&amp="}
links:
  - {url: "http://mire.alt-man.co.uk/errorwinsock.JPG", status: "external", local: null}
---

# VB winsock help NEEDED

### t0m · 2004-10-29 00:52 · #B118537

hey, i was messing round with winsock today and looking through serveral examples i put together a basic server/client program. However, i encountered problems when compiling. for some reason, it doesnt want t accept that 'Winsock1.close' and 'Winsock1.State = sckConnected' arnt... defined or something, here is a screenie:
![](http://mire.alt-man.co.uk/errorwinsock.JPG)
The same thing happens with the 'winsock1.close' bit. i would be very grateful if someone would tell me exactly what i am doing wrong, as im very confused :/ thankyou in advance for your time.

### nova11 · 2004-10-29 00:59 · #B118546

Euix will know. He walked me through a Winsock tut, and i didn't even have VB. Ya need some central server, that's all i remember.

### sivart · 2004-10-29 10:44 · #B118691

I used an entierly different method for Trying to send when its not connected

**Code:**

```
 If Not Winsock1.State = sckConnected Then

    MsgBox "You Are Not Connected To A Chat Server"

    Exit Sub
```

I'm not sure whats wrong with yours though ...

### t0m · 2004-10-29 14:12 · #B118712

i sorted out the 'winsock1.state = sckConnected' bit, but im still having trouble closing it, ie. winsock1.close is still coming up as an error
[img]www.mire.alt-man.co.uk/winsockerror.JPG[/img]

### Levi · 2004-10-29 16:28 · #B118738

Yeah, I'm sorry but that makes absolutly no sense. I've checked for spelling errors and code misusage. I can't find anything. Could you post the actual code instead of an image? Maybe I'm missing something.

### t0m · 2004-10-29 23:22 · #B118889

**Code:**

```
Const sckConnected = 7

Option Explicit

Private Sub cmdClose_Click()

Winsock1.Close

shpGo.Visible = False

shpWait.Visible = False

shpError.Visible = True

End Sub

Private Sub cmdConnect_Click()

Winsock1.RemoteHost = "81.145.234.68" 'Change this to your host IP

Winsock1.RemotePort = 1007

Winsock1.Connect

shpGo.Visible = True

txtItem.SetFocus

End Sub

Private Sub cmdSend_Click()

If Winsock1.State = sckConnected Then

    Winsock1.SendData txtItem.Text

    shpGo.Visible = True

    Label3.Caption = "Sending Data"

Else

    shpGo.Visible = False

    shpWait.Visible = False

    shpError.Visible = True

    Label3.Caption = "Not currently connected to host"

End If

End Sub

Private Sub Winsock1_DataArrival(ByVal bytesTotal As Long)

Dim sData As String

Winsock1.GetData sData, vbString

Label1.Caption = sData

txtPrice.Text = sData

Label3.Caption = "Received Data"

shpGo.Visible = True

shpWait.Visible = False

shpError.Visible = False

End Sub

Private Sub Winsock1_SendComplete()

Label3.Caption = "Completed Data Transmission"

End Sub
```

that is all the code in my client program, most of which is from an example i found on the net. the declared variable at the top fixed my first problem, although i know it shouldnt have to be there, but it doesnt work without it.

### Akura_TheDragonBlader · 2004-10-29 23:26 · #B118890

I might be an idiot to this stuff, but isn't an Option Explicit statement supposed to be at the very top of the code?

### Levi · 2004-10-30 00:49 · #B118920

Yes Option Explicit is usually at the top but so long as its not in like a function or something and near the top that usually doesn't make a difference. It just means it enforces variable decleration.
Yeah, I'm not seeing the problem. It makes no sense. The only reason would be if you weren't connected or trying to connect already. Becaue you can't close a winsock that isn't open. So I'm clueless.
