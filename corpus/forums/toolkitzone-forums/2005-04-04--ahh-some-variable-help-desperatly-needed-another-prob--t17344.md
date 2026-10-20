---
kind: forum-thread
id: "toolkitzone-forums/17344"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Legacy Support"
skin: "phpbb2"
thread_id: "17344"
title: "Ahh, some variable help desperatly needed!!! + another prob"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=17344"
written: "2005-04-04T12:46:00"
last_post: "2005-04-06T12:08:00"
date_confidence: "exact"
captured: ["20050406065703", "20050408223941", "20050414101541", "20051031001648", "20051031001808", "20051108175351", "20051112084737"]
author: "Night_Elf"
repliers: ["tr|ex", "Mr_Janglez_", "RDemusX"]
authors: ["Night_Elf", "tr|ex", "Mr_Janglez_", "RDemusX"]
posts_present: 7
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_190158", captured: "20050414101541", sha256: "e6f1b0ee000c91838db3ecc05f7d58454fdc893a39365fb3de4794a6d5e1325c", wayback_url: "https://web.archive.org/web/20050414101541/http://www.toolkitzone.com/forums/viewtopic.php?p=190158"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_190158_amp_", captured: "20050408223941", sha256: "faec5abaf4974741f311754bbabe73ee8f2a3e0269307301a582b481f2298a09", wayback_url: "https://web.archive.org/web/20050408223941/http://www.toolkitzone.com/forums/viewtopic.php?p=190158&amp="}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_190356_amp_3Bsid_31082e3f02b7478752171b5134c1eed1", captured: "20051112084737", sha256: "cc68699be9b50e339ef185603b06319cb07272e073343902d8ddd18759c8dca0", wayback_url: "https://web.archive.org/web/20051112084737/http://www.toolkitzone.com/forums/viewtopic.php?p=190356&amp%3Bsid=31082e3f02b7478752171b5134c1eed1"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_190601_amp_3Bsid_31082e3f02b7478752171b5134c1eed1", captured: "20051031001648", sha256: "f622b8320020c6474e977ade4669d3da6e0ab79176959412adad00fc2560797b", wayback_url: "https://web.archive.org/web/20051031001648/http://www.toolkitzone.com/forums/viewtopic.php?p=190601&amp%3Bsid=31082e3f02b7478752171b5134c1eed1"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_190751_amp_", captured: "20050406065703", sha256: "5ba91303fcc3f64def1bab363eae6fff50c12d266522e2a41425e18d9aa72c99", wayback_url: "https://web.archive.org/web/20050406065703/http://www.toolkitzone.com/forums/viewtopic.php?p=190751&amp="}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_190751_amp_3Bsid_31082e3f02b7478752171b5134c1eed1", captured: "20051108175351", sha256: "2e70626c3afb76d1bd2e71a4eda27d8d98f8156e86440f087d66461a8d83944d", wayback_url: "https://web.archive.org/web/20051108175351/http://www.toolkitzone.com/forums/viewtopic.php?p=190751&amp%3Bsid=31082e3f02b7478752171b5134c1eed1"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_191127_amp_3Bsid_31082e3f02b7478752171b5134c1eed1", captured: "20051031001808", sha256: "b401a6a784f1d9c6918d3d26444b929600a5af6a0f73663379c237fff73f3b2e", wayback_url: "https://web.archive.org/web/20051031001808/http://www.toolkitzone.com/forums/viewtopic.php?p=191127&amp%3Bsid=31082e3f02b7478752171b5134c1eed1"}
links: []
---

# Ahh, some variable help desperatly needed!!! + another prob

### Night_Elf · 2005-04-04 12:46 · #B190158

Ok..
Problem No 1.
Suppose i have a literal variable.
Is it possible for me to either make this literal variable into an array
OR
is it possible for me to include a carriage return in a literal variable?
Plz plz plz tell me one of the above is possible Very Happy
Problem No 2.
Why is it a blank Mwin appears when i run my code even though there is no mwin command in it?

### tr|ex · 2005-04-04 21:03 · #B190335

**Night_Elf wrote:**

> Problem No 2.
> Why is it a blank Mwin appears when i run my code even though there is no mwin command in it?
>

Did you try #mwincls()?

### Night_Elf · 2005-04-04 21:40 · #B190356

no ... never thot to try that seeing as i havent put in an #mwin command yet.
Hm that makes the mwin flash on and off again v quicky. The mwin only stays on the screen for a fraction of a second but this code is getting used frequently throughout the game - if anyone knows how to get rid of completely that'd be great.
N i still need to make an array or carriage return

### Mr_Janglez_ · 2005-04-04 23:17 · #B190399

Could you put your code on so I could see it?

### Night_Elf · 2005-04-05 12:03 · #B190601

Sure...

**Code:**

```
#Method PixelText(ptx!,pty!)

{

   #getfontsize(ptfontsize!)

   #ptx!=pixelx!/ptfontsize!+1.5

   #pty!=pixely!/ptfontsize!+1.5

}

#method speech()

{

   #TargetLocation(posx!,posy!)

   #posx2!=posx!+1

   #posy2!=posy!-2

   #Pixelx!=posx2!*32-32

   #Pixely!=posy2!*32-32

   #pixelx!=pixelx!-27

   #SpeechBubble$="speech"+Direction$+".gif"

   #SetImageTransparent(SpeechBubble$,pixelx!,pixely!,wide!,high!,0,255,0)

   #txtposx!=ptx!

   #txtposy!=pty!

   #PixelText(ptx!,pty!)

   #Color(0)

   #Text(ptx!,pty!,"<dia$>")

   #Color(15)

}
```

### RDemusX · 2005-04-05 22:04 · #B190751

In TK 2 ... there is a bug that for some reason ... in the program editor ... you need to type all your code. Then position your cursor at the end of every line and see if there is a space in between the end of your code. You won't see this ... and that is why you must place your cursor at the end. Find where it is ... and just backspace that shit right off there. Then save itand run it again.
I hope you understand what I am talking about. I ran into this all the time ... and could not stand it.
The ultimate way to solve ignorant problems the editor has ... is to just go ahead and get TK 3.0.6 ... There is no comparison.
RDX

### Night_Elf · 2005-04-06 12:08 · #B191127

i have got tk3 its been giving me problem after problem Very Happy
Anyway i think i know what u mean - will try that
