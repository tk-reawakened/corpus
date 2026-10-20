---
kind: forum-thread
id: "toolkitzone-forums/12651"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "12651"
title: "I'm new at programming."
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12651"
written: "2004-12-15T08:26:00"
last_post: "2004-12-16T04:23:00"
date_confidence: "exact"
captured: ["20041228072537"]
author: "Montai"
repliers: ["Levi", "matt72186", "khin"]
authors: ["Montai", "Levi", "matt72186", "khin"]
posts_present: 6
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_140075_amp_", captured: "20041228072537", sha256: "27fd2e798511859db3d131f2a0aa0e00b6723a6533704df039f7b36af401440f", wayback_url: "https://web.archive.org/web/20041228072537/http://www.toolkitzone.com/forums/viewtopic.php?p=140075&amp="}
links:
  - {url: "http://msdn.microsoft.com/library/en-us/script56/html/vtoriVBScript.asp", status: "external", local: null}
  - {url: "http://www.w3schools.com/vbscript/default.asp", status: "external", local: null}
---

# I'm new at programming.

### Montai · 2004-12-15 08:26 · #B140070

I just wanted to know where I can find a nice tutorial that can help me to learn VBscript. Not sites that just gives off examples. Thanks anyway.

### Levi · 2004-12-15 08:36 · #B140072

<http://www.w3schools.com/vbscript/default.asp>
That's a good place to start. I belive that MSDN might have something as well.
<http://msdn.microsoft.com/library/en-us/script56/html/vtoriVBScript.asp>
I just hope you realize that VBScript is not as widely supported as JavaScript and won't work on some browsers. Being a client side script that is.

### matt72186 · 2004-12-15 08:47 · #B140073

VBScript is useful for much more than Javascript though as it can be used to create batch-type scripts that you can run on your computer to accomplish simple tasks, you can (sorta) develop small simple applicatoins with VBScript.
Also Fury^2 uses VBScript, so that's another good reason to use it.
My advice to you is all modern day good programming languages are almost the exact same but use different names or syntax to accomplish the same things.
For example:

**Code:**

```
Method CheckA()

{

        #If(a! == 1)

        {

                a!++

        }

}
```

can look like this in another language

**Code:**

```
SUB CHECKA

        IF A = 1

        THEN, BEGIN

                SET A + 1, A

        END

ENDSUB
```

or like this

**Code:**

```
namespace Example

{

        class MyClass

        {

                private a;

                public void CheckA()

                {

                        if(a == 1) a++

                }

        }

}
```

I think when starting programming it's good to relate it to what you already know, then slowly branch off into recognizing it as it's own thing. With the new RPG Code, if people learn it, I'm sure they can fairly easily move over to better languages like C++.
Or if you have no programming experience you can relate programming to real life things.
A function is like a verb, it's something that happens, an object is like a noun, it's describes a thing, an object's attribute is an adjective, it describes the object.

### Montai · 2004-12-15 09:02 · #B140075

Thanks Matt, and Levi. At first I was thinking; whats the point in spending time learning something like rpgcode, when I can learn something better. I might just take your advice and learn rpgcode first, and then try something a lot more advanced.

### khin · 2004-12-15 10:43 · #B140082

I totally agree with Matt. All you need to do is develop your logic and you can take on any programming languages you want.
BTW Matt, the last example you made (Java/Javascript) you intentionally lose the if(){} part in the function?

### matt72186 · 2004-12-16 04:23 · #B140467

Smile fixed, the syntax was more to match C# actually
