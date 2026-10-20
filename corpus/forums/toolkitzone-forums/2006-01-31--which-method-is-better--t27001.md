---
kind: forum-thread
id: "toolkitzone-forums/27001"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Code"
skin: "phpbb2"
thread_id: "27001"
title: "Which method is better?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=27001"
written: "2006-01-31T04:13:00"
last_post: "2006-01-31T18:20:00"
date_confidence: "exact"
captured: ["20060218205648"]
author: "TK Game Boy"
repliers: ["Dont_Think_So"]
authors: ["TK Game Boy", "Dont_Think_So"]
posts_present: 3
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_294028_amp_3Bsid_9afb1aadacac22be95b0e992e62414a6", captured: "20060218205648", sha256: "66fd7c78f33c8b44b7963455abfe19869c10391ae71571b0e26a151a63a082c8", wayback_url: "https://web.archive.org/web/20060218205648/http://www.toolkitzone.com/forums/viewtopic.php?p=294028&amp%3Bsid=9afb1aadacac22be95b0e992e62414a6"}
links: []
---

# Which method is better?

### TK Game Boy · 2006-01-31 04:13 · #B293922

I wrote a class which changes stats. For reference, here it is:

**Code:**

```
class tops()

{

   Public:

      method tops(name$,cock$,image$,location$)

      method stats()

      method display()

   Private:

      m_name$

      m_cock$

      m_image$

      m_location$

      m_level[m_name$]!

      m_health[m_name$]!

      m_adrenal[m_name$]!

      m_fight[m_name$]!

      m_defend[m_name$]!

      m_strength[m_name$]!

      m_agility[m_name$]!

      m_jump[m_name$]!

      m_experience[m_name$]!

      m_rage[m_name$]!

      m_weight[m_name$]!

      m_plumage[m_name$]!

      m_beak[m_name$]!

      m_claws[m_name$]!

}

method tops::tops(name$,cock$,image$,location$)

{

   m_name$=name$

   m_cock$=cock$

   m_image$=image$

   m_location$=location$

}

method tops::stats()

{

   m_level[m_name$]!=L[m_name$]!

   m_health[m_name$]!=H[m_name$]!

   m_healthx[m_name$]!=H[m_name$]!

   m_adrenal[m_name$]!=A[m_name$]!

   m_adrenalx[m_name$]!=A[m_name$]!

   m_fight[m_name$]!=F[m_name$]!

   m_defend[m_name$]!=D[m_name$]!

   m_strength[m_name$]!=S[m_name$]!

   m_agility[m_name$]!=G[m_name$]!

   m_jump[m_name$]!=jump[m_name$]!

   m_experience[m_name$]!=E[m_name$]!

   m_rage[m_name$]!=R[m_name$]!

   m_weight[m_name$]!=W[m_name$]!

   m_plumage[m_name$]!=P[m_name$]!

   m_beak[m_name$]!=B[m_name$]!

   m_claws[m_name$]!=C[m_name$]!

}

method tops::display()

{

   KillCanvas(go!)

   go!=CreateCanvas(600,311)

   ColorRGB(255,0,255)

   FillRect(0,0,600,311,go!)

   ColorRGB(255,255,255)

   SetImage(m_image$,0,0,170,312,go!)

   ColorRGB(255,255,255)

   PixelText(183,19,"<m_cock$>-<m_level[m_name$]!>",go!)

   PixelText(183,36,"Health-<m_health[m_name$]!>",go!)

   PixelText(183,53,"Adrenal-<m_adrenal[m_name$]!>",go!)

   PixelText(183,70,"Fight-<m_fight[m_name$]!> Defend-<m_defend[m_name$]!>",go!)

   PixelText(183,87,"Strength-<m_strength[m_name$]!> Agility-<m_agility[m_name$]!> Jump-<m_jump[m_name$]!>",go!)

   PixelText(183,104,"Experience-<m_experience[m_name$]!>",go!)

   ColorRGB(255,0,0)

   PixelText(183,138,"Rage-<m_rage[m_name$]!>",go!)

   ColorRGB(255,255,255)

   PixelText(455,19,"Origin-<m_location$>",go!)

   PixelText(455,36,"Weight-<m_weight[m_name$]!>",go!)

   PixelText(455,53,"Plumage-<m_plumage[m_name$]!>",go!)

   PixelText(455,70,"Beak-<m_beak[m_name$]!>",go!)

   PixelText(455,87,"Claws-<m_claws[m_name$]!>",go!)

   Switch(m_location$)

   {

      Case ("Mexico") {SetImage("flag_mexico.gif",356,19,60,31,go!)}

      Case ("China") {SetImage("flag_china.gif",356,19,60,31,go!)}

      Case ("England") {SetImage("flag_england.gif",356,19,60,31,go!)}

   }

   DrawCanvasTransparent(go!,22,13,255,0,255)

}
```

So with this, I decided to make an object to makes the stats. When the player presses LEFT or RIGHT, the object is destroyed and a new object is created to add new stats.
What I am trying to accomplish is to create a char selection screen where an object is created with the chars stats (HP, MP, DP, etc) and when you scroll the menu (by pressing LEFT or RIGHT), the object is released() and created anew to have different stats, thus a differnt char.
Though I think this is good but another method would be to make different objects with different names (the first method used the same name for the object) and when you scroll throught he chars list, depending on which char is selected, the appropriate object would be displayed. When you selected that char, all other objects not selected would released().
Which one sounds better.

### Dont_Think_So · 2006-01-31 05:52 · #B293948

Well, it depends on how fast it runs; preloading all of the objects would make the menu run smoother when you select your cock, with the drawback of having loading time before (and possibly after) selection.
Also, looking at your code, you don't need to kill that canvas and recreate it every time - simply drawing over it would suffice. Smile

### TK Game Boy · 2006-01-31 18:20 · #B294028

**Dont_Think_So wrote:**

> Well, it depends on how fast it runs; preloading all of the objects would make the menu run smoother when you select your cock, with the drawback of having loading time before (and possibly after) selection.
>

Well it does run slow with the first method. I'll try the second method to see if it does goes smootly.
