---
kind: forum-thread
id: "toolkitzone-forums/10596"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "10596"
title: "Help with Visual Basic"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=10596"
written: "2004-10-24T17:39:00"
last_post: "2004-10-25T02:57:00"
date_confidence: "exact"
captured: ["20041226085922"]
author: "blackpanther6389"
repliers: ["Colin", "Compugeek"]
authors: ["blackpanther6389", "Colin", "Compugeek"]
posts_present: 14
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_116571_amp_", captured: "20041226085922", sha256: "78de385ca8b02b91f5e49c5cd9bd4a10efd6a7a8776343bf782d9ca29726fb3c", wayback_url: "https://web.archive.org/web/20041226085922/http://www.toolkitzone.com/forums/viewtopic.php?p=116571&amp="}
links: []
---

# Help with Visual Basic

### blackpanther6389 · 2004-10-24 17:39 · #B116258

Heres the code

**Code:**

```
For t = 0 To shpobstacle.UBound

        If shpyou.Left + shpyou.Width < shpobstacle(t).Left Or _

            shpobstacle(t).Left + shpobstacle(t).Width > shpyou.Left Or _

            shpyou.Top + shpyou.Height < shpobstacle(t).Top Or _

            shpobstacle(t).Top + shpobstacle(t).Height > shpyou.Top Then

        Else

            MsgBox ("You lost game over")

            End

        End If

    Next t
```

This will check for every obstacle and if you collide with one of the boxes, then a message box will appear saying the you lost and then ends the game. The problem is that my collision isnt working right. Thats a problem.

### Colin · 2004-10-24 17:43 · #B116261

The context would be nice!
People, pic boxes on forms don't make games *sigh* Wink

### blackpanther6389 · 2004-10-24 17:45 · #B116263

What do you mean, you want all of it including the actual interface?

### Compugeek · 2004-10-25 00:01 · #B116461

Well, telling us what happens would be helpful. Does the message box appear when it shouldn't, or does the collision not respond at all? When is this code executed?

### blackpanther6389 · 2004-10-25 00:06 · #B116470

Oh, ok. Anyways, when the game starts, all of a sudden, the message box just shows up. Its ticking me off.

### Colin · 2004-10-25 00:08 · #B116472

Context, bloody context!
Post the whole program (please, please tell me it's not all on a form).

### blackpanther6389 · 2004-10-25 00:14 · #B116473

Ok heres all of it. I will add more when I get this problem fixed.

**Code:**

```
Option Explicit

Dim intcounter As Integer

Dim intpoints As Integer

Dim intscore As Integer

Dim intspeed As Integer

Dim z As Integer

Dim t As Integer

Dim m As Integer

Dim r As Integer

Private Sub Form_Load()

    Randomize

    intspeed = 30

    intpoints = 0

    r = 0

    lblready.Caption = "Get Ready"

    tmrcheck.Enabled = False

    tmrobstacle.Enabled = False

    For z = 0 To shpobstacle.UBound

        shpobstacle(z).Left = Int(5040 * Rnd + 0)

    Next z

End Sub

Private Sub Form_MouseMove(Button As Integer, Shift As Integer, X As Single, Y As Single)

    shpyou.Left = X

    If shpyou.Left <= 0 Then

        shpyou.Left = 0

    ElseIf shpyou.Left >= 5280 Then

        shpyou.Left = 5280

    End If

End Sub

Private Sub tmrcheck_Timer()

    For t = 0 To shpobstacle.UBound

        If shpyou.Left + shpyou.Width < shpobstacle(t).Left Or _

            shpobstacle(t).Left + shpobstacle(t).Width > shpyou.Left Or _

            shpyou.Top + shpyou.Height < shpobstacle(t).Top Or _

            shpobstacle(t).Top + shpobstacle(t).Height > shpyou.Top Then

        Else

            MsgBox ("You lost game over")

            End

        End If

    Next t

End Sub

Private Sub tmrobstacle_Timer()

    For m = 0 To shpobstacle.UBound

        shpobstacle(m).Top = shpobstacle(m).Top + intspeed

        If shpobstacle(m).Top >= 3600 Then

            shpobstacle(m).Top = 0

            intpoints = intpoints + 1

            shpobstacle(m).Left = Int(5040 * Rnd + 0)

            If intspeed = 70 Then

            Else

                intspeed = intspeed + 1

            End If

        End If

    Next m

End Sub

Private Sub tmrready_Timer()

    r = r + 1

    If r = 60 Then

        lblready.Caption = "Get Set"

    ElseIf r = 120 Then

        lblready.Caption = "GO!"

    ElseIf r = 180 Then

        lblready.Caption = ""

        lblready.Visible = False

        tmrcheck.Enabled = True

        tmrobstacle.Enabled = True

        tmrready.Enabled = False

    End If

End Sub
```

### blackpanther6389 · 2004-10-25 01:20 · #B116513

Can you see the problem with it. Sorry for double posting but it seemed like that you guys had forgot.

### Colin · 2004-10-25 01:24 · #B116514

Well, I'm noticing a few things.
Use "Private" outside of procedure for starters (NOT Dim). And what the heck kind of var names are z, t, m, and r !?
If you hate declaring loop vars every time, do this:
DefLng A-Z
Then in procedure, any single letter vars will be longs at your disposal.
"
If intspeed = 70 Then
Else
intspeed = intspeed + 1
End If
"
How about if (intSpeed <> 70) then ? Also note the ()s... I like them.
The statement "Randomize" does nothing. Try this...
Call Randomize(Timer())
I also notice you referring to many values in many places, this is why we have the 'const' keyword.
Once you take the game off the form we'll delve into why it doesn't work.

### blackpanther6389 · 2004-10-25 01:32 · #B116521

I always do that. Theres no problem with anything else, its just my collision algorithm. The message box is just supposed to pop up when i collided with one of the blocks, but just as soon as the game starts, it shows up for no reason.

### Colin · 2004-10-25 01:35 · #B116523

Your "collision algorithm", eh? Please...

### blackpanther6389 · 2004-10-25 01:41 · #B116527

**KSNiloc wrote:**

> Your "collision algorithm", eh? Please...
>

Well, um, collision thing, now youre making me nervous, I'm not even on your level. I just wanted to know what was wrong with my collision thing, then i get all of this other stuff, Ive never had problems with, but I learned from it. But anyways theres nothing wrong with anything else, just the stuff under the Private Sub tmrcheck_Timer().

### Compugeek · 2004-10-25 02:55 · #B116570

You need to rewrite your If statement, because it tests if you are below the top, above the bottom, to the right of the left, or to the left of the right edge of each block, which will almost always return True.
Try testing whether the left edge of your character is within your character's width of the top edge each block, and the top edge of your character is within your character's height of the top of each block.
Hope that helps! (Hope that you can understand the first sentence Razz )

### blackpanther6389 · 2004-10-25 02:57 · #B116571

**Compugeek wrote:**

> You need to rewrite your If statement, because it tests if you are below the top, above the bottom, to the right of the left, or to the left of the right edge of each block, which will almost always return True.
> Try testing whether the left edge of your character is within your character's width of the top edge each block, and the top edge of your character is within your character's height of the top of each block.
> Hope that helps! (Hope that you can understand the first sentence )
>

Yeah I understood that. Thanks
