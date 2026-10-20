---
kind: forum-thread
id: "toolkitzone-forums/12541"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "rpg code"
skin: "phpbb2"
thread_id: "12541"
title: "adding stats in a fight via special move."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12541"
written: "2004-12-13T02:01:00"
last_post: "2004-12-14T02:14:00"
date_confidence: "exact"
captured: ["20041228072621"]
author: "jake54"
repliers: ["Dont_Think_So", "Akura_TheDragonBlader", "Village Idiot"]
authors: ["jake54", "Dont_Think_So", "Akura_TheDragonBlader", "Village Idiot"]
posts_present: 11
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_139296_amp_", captured: "20041228072621", sha256: "296762ec1d6f32f085d08413bac6cd6ba37771fb8e6d6414d00e52ee26ec5c7b", wayback_url: "https://web.archive.org/web/20041228072621/http://www.toolkitzone.com:80/forums/viewtopic.php?p=139296&amp"}
links: []
---

# adding stats in a fight via special move.

### jake54 · 2004-12-13 02:01 · #B138841

what RPGcodes do i have to use to temporarily boost up a characters stat in a battle.
I.E.
Golden dragon's spirit boosts up FP by 5, and Dp by 5 for 9 rounds.
would it require me to use a BS other than the original one?

### Dont_Think_So · 2004-12-13 02:04 · #B138843

Apply it as a status effect. Make the RPGCode program count down until the last round, and then remove the effect.

### jake54 · 2004-12-13 02:09 · #B138849

**Dont_Think_So wrote:**

> Apply it as a status effect. Make the RPGCode program count down until the last round, and then remove the effect.
>

but what are the lines of code that i have to input? it doesn't effect stats, but it does effect helth and smp, i am looking for DP and FP addition, at least it explains how i am gonna make it run for a few rounds.
EDIT: tried this:
#If(timer > 0)
{
#FP!=FP!*3
#DP!=DP!83
}
#If(timer=0)
#End
would that work? or did i do something wrong, the timer is supposed to be the status effect timer, but is that unnessicary? i saw no change in the subject that that was tested on, so i think i did something wrong.

### Akura_TheDragonBlader · 2004-12-13 02:51 · #B138876

Unfortunately, the problem with modifying stats as a result of a status affect won't change back when the effect ends. It shouldn't anyway. You could probably do it if you have the victory programs of every enemy set it back, but you're better off going custom.

### jake54 · 2004-12-13 02:54 · #B138877

hmm... i usually have tons of trouble with custom battle systems.
ah well thanks for your help anyways. i'll try to find out how to make one.

### Dont_Think_So · 2004-12-13 03:43 · #B138914

I thought programs for status effects were run every round the status effect was in... effect.

### Village Idiot · 2004-12-13 17:11 · #B139067

In the status effect menu, there isn't a Dp or Fp increase or decrease text box... either that, or i'm blind, which is highly possible...

### jake54 · 2004-12-13 22:47 · #B139152

**Village Idiot wrote:**

> In the status effect menu, there isn't a Dp or Fp increase or decrease text box... either that, or i'm blind, which is highly possible...
>

der there is no DP/FP decrease (negative numbers mean increase.) that is why i am gonna have to use RPGcode, but... it apparently wont work, or something.

### Dont_Think_So · 2004-12-13 23:43 · #B139185

It will work if the program is run every round of the status effect...
If it is, tell me! Then I'll write you a simple program...

### jake54 · 2004-12-14 01:49 · #B139271

**Dont_Think_So wrote:**

> It will work if the program is run every round of the status effect...
> If it is, tell me! Then I'll write you a simple program...
>

i have tried, no effect.
i just need to find out what code command gives the bonus to FP or DP.
i've tried DP = DP!*2, but that didn't work., although it is conciveable i did something wrong.

### Dont_Think_So · 2004-12-14 02:14 · #B139296

Targ$ = GetTargetHandle()
RPGCode(Targ$ + "[DP]! += 2")
