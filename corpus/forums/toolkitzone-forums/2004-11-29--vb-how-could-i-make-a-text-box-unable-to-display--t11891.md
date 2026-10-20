---
kind: forum-thread
id: "toolkitzone-forums/11891"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "11891"
title: "VB How could I make a text box unable to display..."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=11891"
written: "2004-11-29T02:01:00"
last_post: "2004-11-29T17:29:00"
date_confidence: "exact"
captured: ["20041226222640"]
author: "TK Apprentice"
repliers: ["Levi", "Mike", "Colin"]
authors: ["TK Apprentice", "Levi", "Mike", "Colin"]
posts_present: 5
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_131635_amp_", captured: "20041226222640", sha256: "ffff598d205a18bcb1fe27651cc7d1e9eb5027b03f622c69ff876fc7172096da", wayback_url: "https://web.archive.org/web/20041226222640/http://www.toolkitzone.com/forums/viewtopic.php?p=131635&amp="}
links: []
---

# VB How could I make a text box unable to display...

### TK Apprentice · 2004-11-29 02:01 · #B131372

VB How could I make a text box unable to display... anything but numbers?

### Levi · 2004-11-29 06:13 · #B131505

In the KeyPress event use something like the following
Private Sub txtEnterNums_KeyPress (KeyAscii As Integer)
If KeyAscii < Asc("0") Or KeyAscii > Asc("9") Then
KeyAscii = 0 ' Cancel the character.
Beep ' Sound error signal.
End If
End Sub

### Mike · 2004-11-29 14:49 · #B131571

Ah!
Take out that annoying beep! Razz

### Colin · 2004-11-29 16:16 · #B131616

That won't work too well, Levi, for a number of reasons.

**Code:**

```
Private Sub txtTheBox_KeyPress(ByRef KeyAscii As Integer)

    On Error GoTo letter

    Dim ret As Double

    ret = CDbl(txtTheBox.Text & chr$(KeyAscii))

    Exit Sub

letter:

    If (KeyAscii <> 8) Then

        ' Bad key

        KeyAscii = 0

    End If

End Sub
```

### Levi · 2004-11-29 17:29 · #B131635

I copied that code from my MDSN help files. Blame microsoft.
I'm not sure I copy your code though Colin. Not being advanced beyond regular coding of course that's not suprising. Smile
I mean let me see if I've got this right. On error goto letter. On the letter see if the Ascii code doesn't equal 8. If I remember correctly 8 is the backspace so any other key is a bad key.
Then you create a double variable, this will obviously hold the numbers entered both into the textbox and the current key. You in fact set this ret variable equal to the Conversion function CDbl() with TextBox1.Text & the actual character of AsciiKey. Basically converting anything they type into a number. Instead of using Val of course which I suppose is done simply to be a little more world wide in the conversion process?
If no error then exit the sub. An error occuring if they try to convert a character to a double.
Of course this is where I'm confused. Where does TextBox1.Text actually recieve the new data. And doesn't a double return a #.# format? Though that wouldn't be a bad thing, oh. Nope, sorry. Again my beginner's stupidity. Decimal not double does that. Double simply allows for floating points. Gotchya. But that first problem is a valid thing. Smile
Darn it. Even thats not valide because I forgot that you're not removing the result from the textbox. You're simply testing the value. If the value is numeric then the keyAscii won't be removed. If it isn't then it will be. Otherwise allow the KeyPress to continue and work correctly.
Mine haulted all but the numeric keys. Including the backspace. I understand now. I'm not as totally dense as I thought. Never mind then.
