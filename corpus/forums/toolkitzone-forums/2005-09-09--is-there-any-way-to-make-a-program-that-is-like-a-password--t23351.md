---
kind: forum-thread
id: "toolkitzone-forums/23351"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Toolkit Discussion"
skin: "phpbb2"
thread_id: "23351"
title: "IS there any way to make a program that is like a password"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=23351"
written: "2005-09-09T11:15:00"
last_post: "2005-10-03T19:46:00"
date_confidence: "exact"
captured: ["20051112100433"]
author: "corim123"
repliers: ["Tao-Kun", "Colin", "Shapechanger", "CG-I", "p90m16mp5a4", "Caliber Mengsk", "Mr Picso"]
authors: ["corim123", "Tao-Kun", "Colin", "Shapechanger", "CG-I", "p90m16mp5a4", "Caliber Mengsk", "Mr Picso"]
posts_present: 15
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_256011_amp_3Bsid_3fbefe8bbeb7e326407723096016219a", captured: "20051112100433", sha256: "d60c847a63cd7dd9e9d2e1438ffaab6deadb5c3e4e7c870ec7d57c45edc00c02", wayback_url: "https://web.archive.org/web/20051112100433/http://www.toolkitzone.com/forums/viewtopic.php?p=256011&amp%3Bsid=3fbefe8bbeb7e326407723096016219a"}
links:
  - {url: "http://tk3.toolkitzone.com/help/?page=19#itemcount", status: "captured", local: "wayback/toolkitzone.com/tk3.toolkitzone.com/help__page_19"}
---

# IS there any way to make a program that is like a password

### corim123 · 2005-09-09 11:15 · #B255576

It uses someway to see if there is a specific item in their inventory and then if yes it allows them through, if no it doesn't allow them through, I think if I get this working then my other topic, about a kill code after 10 minutes will work.

### Tao-Kun · 2005-09-09 13:42 · #B255595

you mean like a program to open a door?
i

### corim123 · 2005-09-10 15:08 · #B255961

sort of, it is used to travel to different villages and you must have a certain item to go there so thats why I need a program to check and see if they have an item to either grant them access or not

### Tao-Kun · 2005-09-10 16:39 · #B255998

// Goes to Village, Bob land
if(boblandkey!~=1) // if he doesn't have the item that carries the varible boblandkey
{
mwin("I can't go there without the key!")
end
}
send("bobby_land.brd", 1, 1, 1) //if he does
Use Varibles.

### Colin · 2005-09-10 16:56 · #B256011

You could also use physical items and the [itemCount()](http://tk3.toolkitzone.com/help/?page=19#itemcount) function.
In the program that gives you the item:

**Code:**

```
giveItem("someItem.itm")
```

In the program that checks for the item:

**Code:**

```
if (itemCount("someItem.itm") > 0)

{

   // stuff if player has the item

}
```

### corim123 · 2005-09-24 14:02 · #B259930

Tao-Kun, do you want credit for this????????

### Shapechanger · 2005-09-24 14:25 · #B259938

You're giving him credit for something that simple?

### corim123 · 2005-09-24 19:01 · #B259971

I just wanted to make sure no one got mad if I sold it.

### CG-I · 2005-09-28 10:12 · #B260800

If you have to ask to use someone's advice after they give it to you, what's the point?

### corim123 · 2005-09-28 12:01 · #B260815

What do you mean? Cg-I?
I tried the code and it doesn't work anymore. It justs sits there and does nothing.Can someone figure out the problem?

**Code:**

```
if(scroll!~=1)

{

mwin("I can't go there without the scroll of entry!")

end

}

if(scroll!~=0)

{

send("forest.brd", 19, 9, 1)

end

}
```

### p90m16mp5a4 · 2005-09-28 16:05 · #B260860

I don't like BobLand.

### CG-I · 2005-09-29 02:19 · #B261056

**corim123 wrote:**

> What do you mean? Cg-I?
>

What I'm trying to say is that if Tao-Kun supplied you with some code over the forums to help you with your scroll of entry program, he's assuming you might use it.
I'm sure he's also aware that you might not be the only one to ape that little line of code. It's not exactly copyrighted, plus I'm willing to bet that someone who wished to write a program like that would do something sort of in that vein.
Plus, you're not even using the same BobLand variables he is, I assume.

### Caliber Mengsk · 2005-09-30 14:58 · #B261387

In TK2, you have to put # 's in front of code... except for the { }

### Mr Picso · 2005-09-30 19:49 · #B261455

**corim123 wrote:**

> What do you mean? Cg-I?
> I tried the code and it doesn't work anymore. It justs sits there and does nothing.Can someone figure out the problem?
>

Um... try replacing the "~=" with "==".

### corim123 · 2005-10-03 19:46 · #B262105

I've done all that, and it works when I hit the test button, but in the game it doesn't do squat. Let me try re-setting the variables.
