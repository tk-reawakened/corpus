---
kind: forum-thread
id: "toolkitzone-forums/12291"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "suggestions, bugs and general questions"
skin: "phpbb2"
thread_id: "12291"
title: "Will TK3.0.5 have this? (Not sre what it's called)"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=12291"
written: "2004-12-07T21:38:00"
last_post: "2004-12-08T00:31:00"
date_confidence: "exact"
captured: ["20050116234907"]
author: "Angel of Death"
repliers: ["TheCPPFreak220", "Colin", "Occasionally_Correct", "Dont_Think_So"]
authors: ["Angel of Death", "TheCPPFreak220", "Colin", "Occasionally_Correct", "Dont_Think_So"]
posts_present: 6
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_136230_amp_", captured: "20050116234907", sha256: "3dd65e944282d5049ea3221d92fdd55117bf14bb59d2f9dd09ae5246ccf2a0bc", wayback_url: "https://web.archive.org/web/20050116234907/http://www.toolkitzone.com/forums/viewtopic.php?p=136230&amp="}
links:
  - {url: "http://www.toolkitzone.com/forums/viewtopic.php?t=12144", status: "never-captured", local: null}
---

# Will TK3.0.5 have this? (Not sre what it's called)

### Angel of Death · 2004-12-07 21:38 · #B136152

Where you can use an infinite number of parameters, get how many have been used, and so on? It's pissing me off making a shop program that has like, sixteen different parameters when only nine or so are used in most of them.

### TheCPPFreak220 · 2004-12-07 21:43 · #B136154

Yes. Colin posted that somewhere.

### Colin · 2004-12-07 22:55 · #B136180

Well, I didn't.
But, I do have a solution. You can pass just one array object to your functions.

### TheCPPFreak220 · 2004-12-07 23:03 · #B136184

Ahhh. Sorry, Colin did not, my bad. I was refering to this:
<http://www.toolkitzone.com/forums/viewtopic.php?t=12144>
Which might work for what you need.

### Occasionally_Correct · 2004-12-07 23:30 · #B136195

**TheCPPFreak220 wrote:**

> Ahhh. Sorry, Colin did not, my bad. I was refering to this:
> <http://www.toolkitzone.com/forums/viewtopic.php?t=12144>
> Which might work for what you need.
>

That would work, yes. However, that'd be a bit tedius if you're going to have a shop with the probability of a large amount of items. I'd say go with what Colin suggested; use an array object (you can use the Array class Colin made - I think it's in his system.prg).
Example;

**Code:**

```
method ShopThing(CArray array)

{

    //Get the bound of the array...

    bound! = array->getBound()

    //Loop through the array...

    for(idx! = 0; idx! <= bound!; idx!++)

    {

        //Set the item information stuff

    }

}
```

That sort of thing. Razz

### Dont_Think_So · 2004-12-08 00:31 · #B136230

Or you could combine the best of both worlds and make it use either an array class OR parse the items from one string Smile.
