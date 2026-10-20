---
kind: forum-thread
id: "toolkitzone-forums/27289"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Programming"
skin: "phpbb2"
thread_id: "27289"
title: "Simple MFC Timer refusing to work...:/"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=27289"
written: "2006-02-11T03:05:00"
last_post: "2006-02-15T00:38:00"
date_confidence: "exact"
captured: ["20060307044024"]
author: "Zap!"
repliers: ["Dominea"]
authors: ["Zap!", "Dominea"]
posts_present: 6
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_297322_amp_3Bsid_40935223b093a968c6e24c3a365290cb", captured: "20060307044024", sha256: "a247e2b625a62c76f9dca138480523233a2b5b2e27dd01d589217973df638bdc", wayback_url: "https://web.archive.org/web/20060307044024/http://toolkitzone.com/forums/viewtopic.php?p=297322&amp%3Bsid=40935223b093a968c6e24c3a365290cb"}
links: []
---

# Simple MFC Timer refusing to work...:/

### Zap! · 2006-02-11 03:05 · #B296707

Ok, to begin with I've *never* used a timer in MFC before in my entire life.
But now I have need for a simple Timer, recurring at a user set interval, so I set one up. But the code inside of my OnTimer() wasn't working, at all. Even though all I had put in there was a display text function ( that works everywhere else. )
I figure the code just isn't getting run, and I've been trying to find a solution for the past week and a half googling, msdn'ing, asking online..noone has been able to tell me anything I don't already know.
Basically though, here is my code related to the timer. ( I dumbed it down to just a normal timer, which still isn't working, so it isn't my input method. )
[ Note: This is a classwizard MFC project, so these are moved all over a few different files, but their all in the same class, CCobraChatDlg ]

**Code:**

```
void CCobraChatDlg::OnTimer(UINT nIDEvent)

{

   SendText("Timer fired.", 0);

   OnTimer(1);

}

..

class CCobraChatDlg : public CDialog

{

// Construction

public:

   ..

   //

   // Timer

   //

   void OnTimer(UINT nIDEvent);

   UINT m_Timer;

   ..

};

..

/////////////////////////////////////////////////////////////////////////////

// OnConnect

int CCobraChatDlg::OnConnect()

{

   ..

      //

      // Timer

      //

      m_Timer = SetTimer(1, 200, 0);

   ..

}

..

/////////////////////////////////////////////////////////////////////////////

// OnDisconnect

void CCobraChatDlg::OnDisconnect()

{

   ..

   KillTimer(1);

   ..

}
```

That is basically what I have, which according to all the documentation I can find, tutorials, people I've asked, is exactly what I should have.
I'm not sure WHY the timer isn't being fired, please, please pleaseeeeeeee explain to me.
I've spent at least a week and a half on this, and I'm about to give up.

### Dominea · 2006-02-12 23:25 · #B297322

Are you just trying to leanr timers or are you just trying to get somethign to run? Cause the only reason for you to create a timer in MFC is to trigger an overridden event. I usually go with QueryPreformancyCounter timer and a bool to do pretty much anything I want in MFC. THe only time ive used MFC timers is for a CImage auto-refresh. All I remember is that it was a pain int he arse to set up.

### Zap! · 2006-02-13 18:24 · #B297550

I have a reason for the timer, my program is a telnet bot and the timer is going to help with games/anti-idle messages.
The program is mutli-threaded so I'm not trying to use a timer to recv the messages, just in case anyone cared to know. Razz

### Dominea · 2006-02-14 22:01 · #B298159

Gross dude. To make networking work nice wiht games use a seperate thread. _beginthreadEx is the function to call. But its simple just define a seperate function that handles all the messages and recvs. I would suggest you also look into the select function. Also use a mutex to protect ur data.
Good luck.
MFC Timers suck. - They are slow and unreliable.

### Zap! · 2006-02-14 22:58 · #B298184

Oh shit...
I feel stupid, I was already using threads for the games and everything, and I don't even know why I Was wanting to use a timer. Blah...
Such a huge waste of time, all I needed was to use that wait function I wrote...
( I write the function at the very start of the project...forget I have it...then end up not using it for what I wrote it for and go off on some stupid tangent that sets me back sooooo much time. boo Sad. )

### Dominea · 2006-02-15 00:38 · #B298234

Ya When I do networking I create one thread for the gui and one for the networking. I sync them using Mutexs (rarely Critical Sections) and then use the select function to handle send and recvs all in the same function. This works for me 99% of the time without me having to do some funcky stuff.
Anyways GL.
