---
kind: forum-thread
id: "toolkitzone-forums/12254"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "12254"
title: "Pure Virtual Functions"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12254"
written: "2004-12-07T01:04:00"
last_post: "2004-12-07T03:51:00"
date_confidence: "exact"
captured: ["20041215093210", "20050116084211", "20050116084347", "20050116084528", "20050116084532"]
author: "Colin"
repliers: ["TheCPPFreak220"]
authors: ["Colin", "TheCPPFreak220"]
posts_present: 4
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_135773_amp_", captured: "20050116084211", sha256: "d2c3cc2f8d4fa421ecee724de8c818d6ca52807153d2ac507d227922bb6bff2e", wayback_url: "https://web.archive.org/web/20050116084211/http://www.toolkitzone.com/forums/viewtopic.php?p=135773&amp="}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_135777", captured: "20050116084347", sha256: "380d23e8a5bae49878d29d34486c0a5cdd1685e16dc1fe1a302a1ab88c97becf", wayback_url: "https://web.archive.org/web/20050116084347/http://www.toolkitzone.com/forums/viewtopic.php?p=135777"}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_135777_amp_", captured: "20041215093210", sha256: "7d7b58e92b38302de1da0d8d8043d78be537eeea69ec9e38222cb0b826a98bcc", wayback_url: "https://web.archive.org/web/20041215093210/http://www.toolkitzone.com/forums/viewtopic.php?p=135777&amp="}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_135909_amp_", captured: "20050116084528", sha256: "968978b6fe0b6db981ca2d71733231f3b5f503b8d6591a6e0b471aa60f1e9818", wayback_url: "https://web.archive.org/web/20050116084528/http://www.toolkitzone.com/forums/viewtopic.php?p=135909&amp="}
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_135915_amp_", captured: "20050116084532", sha256: "b40200cce7503414817da64618c505cc017613e94269229bfde082d8a009e580", wayback_url: "https://web.archive.org/web/20050116084532/http://www.toolkitzone.com/forums/viewtopic.php?p=135915&amp="}
links: []
---

# Pure Virtual Functions

### Colin · 2004-12-07 01:04 · #B135773

Pure virtual functions are functions that have no implementation. If a class contains even one pure virtual function, you cannot create it. If a class is composed entirely of pure virtual functions, I suggest you use an 'I' rather than 'C' for "interface".

**Code:**

```
class ITest // Use 'I' when the class is entirely pure virtual

{

public:

   method test() = 0 // " = 0" is the "pure specifier"

}

class COne: ITest

{

public: // Not actually required as ITest is already exposing test()

     // in the public scope

   method test()

   {

      mwin("In COne!")

   }

}

class CTwo: ITest

{

public: // Not actually required as ITest is already exposing test()

     // in the public scope

   method test()

   {

      mwin("In CTwo!")

   }

}

method test(ITest p)

{

   p->test()

}

p = COne()

j = CTwo()

test(p) // Shows "In COne!"

test(j) // Shows "In CTwo!"

p->release()

j->release()

wait()

mwincls()
```

### TheCPPFreak220 · 2004-12-07 01:13 · #B135777

Could you give a better definition for pure, virtual functions.
Thanx

### Colin · 2004-12-07 03:46 · #B135909

Pure virtual functions are functions that have "no code". In other words, when you inherit a class a contains them--an abstract class--you have to provide code for every last one of them.
A good example is COM itself. All COM objects derive from IUnknown which has three methods to manipulate COM objects. Every COM class you code will want to do radically different things for these methods so you provide your own code for them. Another example is MFC's CObject - it has several pure virtual functions so that any class deriving from CObject and be used tightly with MFC.
For a simpler example, consider an IRealNumber interface. Every kind of real number has the common property have being possible to express (though sometimes requires rounding) as a double so IRealNumber might have an operator! (or operator double in C++). But integers, whole numbers, natural numbers, rational numbers and irrational numbers have very different things that are specific to them. Moral of the story is, you derive all the real numbers from IRealNumber and you pass it to functions that take IRealNumbers. Those functions know that they are getting real numbers and they know they can be cast to a double. They don't care about the details of the cast.
Hopefully that helps.

### TheCPPFreak220 · 2004-12-07 03:51 · #B135915

Yes that does help. So basically it gerneralizes all classes derived from that one class by makeing it so that all derived classes must have those functions. That's a nice feature to have in any language that supports derived classes.
