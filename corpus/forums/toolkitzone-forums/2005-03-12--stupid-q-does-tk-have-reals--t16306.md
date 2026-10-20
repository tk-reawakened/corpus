---
kind: forum-thread
id: "toolkitzone-forums/16306"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "16306"
title: "stupid Q...does TK have Reals???"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=16306"
written: "2005-03-12T23:53:00"
last_post: "2005-03-19T21:20:00"
date_confidence: "exact"
captured: ["20050317184331", "20050326002651"]
author: "Dredogol"
repliers: ["Serge", "Colin", "HamsterBob", "Xavier", "joao_foscarini", "Janus", "Pests", "Akura_TheDragonBlader", "Dont_Think_So"]
authors: ["Dredogol", "Serge", "Colin", "HamsterBob", "Xavier", "joao_foscarini", "Janus", "Pests", "Akura_TheDragonBlader", "Dont_Think_So"]
posts_present: 18
pages_present: [1, 3]
pages_total: 3
posts_per_page: 15
complete: false
encoding: latin-1
converter_version: "1"
gaps:
  - {page: 2, start: 16, end: 30, url: "http://toolkitzone.com/forums/viewtopic.php?t=16306&start=15", reason: "never-captured"}
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_179713_amp_", captured: "20050317184331", sha256: "14e8f5db3f88567110479c856a434766c485391e2442e74741e09efe69ca04ed", wayback_url: "https://web.archive.org/web/20050317184331/http://www.toolkitzone.com:80/forums/viewtopic.php?p=179713&amp"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_182795_amp_", captured: "20050326002651", sha256: "7ddd3efdf80c0b29e44c893190a8360702ed03fc7303a466a6ad522b7dcd3faf", wayback_url: "https://web.archive.org/web/20050326002651/http://toolkitzone.com/forums/viewtopic.php?p=182795&amp="}
links: []
---

# stupid Q...does TK have Reals???

### Dredogol · 2005-03-12 23:53 · #B179711

By the way...I've always been wondering...does RPGCode have Real numbers...if not, is there a way to import any standard C++ .h files???
If not...is there any way to make the INT numbers go higher than 999 trillion? Because I know the 16th BIT slot is reserved for +/- indicator
Also...do "Natural" numbers exist in C++ ...or is that just in our RESOLVE language?
That would be really cool...then I can add RESOLVE C++ into my codes and do HW while programming in it...LOL ...j/k
*note ...RESOLVE is the worst C++ modified program EVER...even as a learning tool for client/implementer views LOL*
hey, you guys should read our 221 RESOLVE book...makes you feel like you're going to be retarted while you're reading....that's how stupid some questions in the book are.

### Serge · 2005-03-12 23:56 · #B179713

RPGCode has real numbers in it.
Like 1, 2, 3, 4, etc..

### Colin · 2005-03-13 00:09 · #B179714

Dredogol, do you even know what real numbers are? Apparently you don't either, Serge. A quick review for us all:
Natural numbers are the simplest in our number system. They form the following sequence:
1, 2, 3...
There is no 0 is the natural number system. However, the need for a 'nothing' number was soon realized, thus creating the whole number system:
0, 1, 2...
Indeed, there are still gaps between the numbers, and no way to represent fractional data. So we have the rational number system. This is two whole numbers in a ratio:
a / b
Meanwhile, there is also no way to express numbers less than zero (debt, if you will). Indeed, we have the integral number system:
..., -3, -2, -1, 0, 1, 2, 3...
Combine them both and you have real number system:
+- a / b
However, a gap still exists where numbers like sqrt(-1) lie. This is the imaginary number system:
sqrt(-1) = i
Combine both real and imaginary (unreal), and you have the complex number system:
a + bi
***
In other words, the TK already supports both natural and real numbers.

### HamsterBob · 2005-03-13 02:27 · #B179753

WOW.
Xavier said youre only like 15 years old.
He must be lying.
Or are you one of those super smart kids who goes to college when there 12 and graduates with a PHD in Quantum Neutrino Field Dynamics when there 16

### Xavier · 2005-03-13 02:30 · #B179754

I never lie!
He's just someone with a very, very keen interest in programming and as a result knows a lot about it. Obviously an intelligent person to learn it as such a rate, and an appetite to learn more. But it's not that amazing, trust me, I know loads of kiddy programmer extraordinaires. It's a new generation which grow up on computers as opposed to us older users (I didn't get my first PC until I was like 15).
I wish I had that kind of "thirst to learn" attitude while I sit here with a huge University report to write in a couple of days and absolutely no starting point or motivation. Yay.
I'm telling you, he's yet to hit the mid-teen education rot of booze, fags (as in the cigerrettes Wink) and endless attempts to get laid....then we'll see where programming priorities are in his life...

### joao_foscarini · 2005-03-13 02:38 · #B179758

I think he's 13 or 14.

### Janus · 2005-03-13 02:38 · #B179759

**HamsterBob wrote:**

> WOW.
> Xavier said youre only like 15 years old.
> He must be lying.
> Or are you one of those super smart kids who goes to college when there 12 and graduates with a PHD in Quantum Neutrino Field Dynamics when there 16
>

What Colin just explained is basic level algebra. If you don't know that stuff, you need to pay more attention in school. Smile

### Pests · 2005-03-13 04:06 · #B179793

In 9th grade I was 13.

### Dredogol · 2005-03-13 04:36 · #B179801

haha...yeah...wonder how a 20 year old guy feels....ME..LOL
But you sure NATURAL numbers doesn't support ZERO? Because just last week, we were using them in C++ and it supported 0, just not negative numbres Shocked
What I "really" mean is...I KNOW what they are, just in ...umm...BINARY or BIT perspectives...don't INTEGERS have the lowest possible range or numbers, then REAL/NATURAL numbers can support higher ammounts?
I remember we had to do a POWER test like 1,000^10,000 power and see how long the system took to proccess it and try to reduce the system calc time...we used NATURAL numbers...just wondering.
My main reason was because INT! in RPGCode only supports up to X999,999,999,999,999 == 999 Trillion == 15 BIT, meaning the 16th BIT where the X is a 1 or 0 for either a +/- sign.
Remember that FLORIDA talk about voting last year saying the count got messed up...well, that's why. The system only supported 16-BIT INTEGER, which screwed up the numbers after it went past it's maximum threshold.
...sorry going little off topic...does RPGCode support numbers HIGHER than 999 trillion...because INT sure doesn't...

### Colin · 2005-03-13 04:59 · #B179803

The RPGCode number is a double (8 bit floating point).
Pests, my birthday is November 14th, so I'm 14.

### Pests · 2005-03-13 05:22 · #B179806

Ha! Mine is November 9th. I generally consider the age I was at the start of the school year to be the age I attended thoughout the year. Thinking back now how old was I in a grade I would just add 4 and be done with it, gets complicated after you consider the birthday aspect.

### Janus · 2005-03-13 05:59 · #B179809

**Colin wrote:**

> The RPGCode number is a double (8 bit floating point).
> Pests, my birthday is November 14th, so I'm 14.
>

If it's a double, then you mean 8 byte.

### Colin · 2005-03-13 06:08 · #B179813

Yeah, I do.
The TK's number type can hold slightly larger than 255. ;)

### Dredogol · 2005-03-13 16:07 · #B179894

well...is there any way you guys can increase that max limit???
Just wondering, because if you go over 999 trillion, you start back at 17 for some reason...LOL
I wish I still had my book that kept all the types with their max holding limits...but I had to return it to our library =/
our freekin campus has 24 libraries....6 are 24 hours...LOL...yeah, one hell of a large campus LOL
EDIT:
tell me if I forget any of the numbers for C++:
Integer, Double, Real, Natural...(these are object calls to tell which number system to use)

### Akura_TheDragonBlader · 2005-03-13 16:45 · #B179913

**Janus wrote:**

>
> **HamsterBob wrote:**
>
> > WOW.
> > Xavier said youre only like 15 years old.
> > He must be lying.
> > Or are you one of those super smart kids who goes to college when there 12 and graduates with a PHD in Quantum Neutrino Field Dynamics when there 16
> >
>
> What Colin just explained is basic level algebra. If you don't know that stuff, you need to pay more attention in school. Smile
>

My teacher didn't explain that. Then again, I do go to one of the worst schools in the state.

> [!missing] gap:16-30 · http://toolkitzone.com/forums/viewtopic.php?t=16306&start=15 · never-captured
> Page 2 of 3 was not recovered.

### HamsterBob · 2005-03-15 21:21 · #B180906

**Quote:**

> very very laaaaaaaaaaaaaaaarge overcomplication of a very simple concept.
>

Exactly.
I know how to do math, im in algebra 2, i just havent ever heard those terms used like that. And The way their teaching us maybe it wont matter until next year anyways.

### Xavier · 2005-03-15 21:25 · #B180907

**Plasmius wrote:**

>
> **Xavier wrote:**
>
> > I'm telling you, he's yet to hit the mid-teen education rot of booze, fags (as in the cigerrettes Wink) and endless attempts to get laid....then we'll see where programming priorities are in his life...
> >
>
> First off, getting laid is easy.
>

Unfortunately, not everyone can pay for it like you or having such willing mothers.
Oooooooh....diss.
I take it all back, kiddo....I'm sure your mother's very nice.

### Dont_Think_So · 2005-03-19 21:20 · #B182795

**Dredogol wrote:**

> Just wondering, because if you go over 999 trillion, you start back at 17 for some reason...LOL
>

The reason it starts at 17 is because it goes into scientific notation, then you only get the exponent of 10. That means your number is:
x*10^17
Where x is some number you don't know Razz
I only know this because I recently tried to do something that involved large amounts of experience to level up, but eventually the numbers went to 17, 18, etc. So, the experience required to level up to level 50 became 18. Yay.
