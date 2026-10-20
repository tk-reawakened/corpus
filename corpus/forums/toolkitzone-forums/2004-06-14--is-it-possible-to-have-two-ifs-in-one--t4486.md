---
kind: forum-thread
id: "toolkitzone-forums/4486"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Advanced Coding"
skin: "phpbb2"
thread_id: "4486"
title: "Is it possible to have two ifs in one?"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=4486"
written: "2004-06-14T12:22:00"
last_post: "2004-06-14T18:00:00"
date_confidence: "exact"
captured: ["20051113133942"]
author: "William"
repliers: ["Xavier", "Marc", "Asimir"]
authors: ["William", "Xavier", "Marc", "Asimir"]
posts_present: 10
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_45479", captured: "20051113133942", sha256: "f161c32541c08d6ec813bc2c68286b5ccbd68f8566a8924959cc32c0868b7602", wayback_url: "https://web.archive.org/web/20051113133942/http://www.toolkitzone.com/forums/viewtopic.php?p=45479"}
links:
  - {url: "http://www.toolkitzone.com/fileman.php?id=3&file=157", status: "captured", local: "wayback/toolkitzone.com/fileman.php__id_3_file_157"}
---

# Is it possible to have two ifs in one?

### William · 2004-06-14 12:22 · #B45321

Like this:

**Code:**

```
#if(item!=1,armor!=1)

{

*run this is item equals to 1 and armor equals to 1

}

#if(item!=2,armor!=0)

{

*run this is item equals to 2 and armor equals to 0

}
```

Is that possible, because I don't want to do this:

**Code:**

```
#if(item!=1)

{

#if(armor!=1)

{

*code here

}

}
```

### Xavier · 2004-06-14 12:43 · #B45336

At the moment you'd have to use a plugin to gain such functionality, such as AND, OR commands.
Check out [this](http://www.toolkitzone.com/fileman.php?id=3&file=157) plugin.
Read it's ReadMe.txt carefully, as it's annoying when ppl just come back and ask how to use plugins.

### Marc · 2004-06-14 16:43 · #B45404

I hope we oncorperate that plugin into TK3.

### William · 2004-06-14 17:06 · #B45422

Thanks a lot. And it would be really good if you added that into tk3.

### Asimir · 2004-06-14 17:18 · #B45438

I haven't used that plugin, but knowing how plugins work, It can't use AND and OR properly, although I'm sure it provides a great alternative Razz
It'd be great if && and || were incorperated properly.

### Xavier · 2004-06-14 17:20 · #B45442

Like I said, #And and #Or commands.
So #And(var!, var!) will return 0 or 1 depending on the result.
Not pretty, but he asked for an alternative...

### Marc · 2004-06-14 17:31 · #B45449

**Asimir wrote:**

> I haven't used that plugin, but knowing how plugins work, It can't use AND and OR properly, although I'm sure it provides a great alternative Razz
> It'd be great if && and || were incorperated properly.
>

I have, quite stupid. THe idea is good. But I prefer the && || way of doing it.
Im sure you all know but for those who don't.
(C++ mind you)

**Code:**

```
cout << "press 1 for go and 2 for no";

cin >> choice;

if(choice !=1 && choice !=2)

{

system("cls");

//do the first cout and cin over again

}

if(choice ==1)

{

//do choice

}

if(choice ==2)

{

exit(1);

}
```

I would think it would be easier then #and(blahh,blahh)

### Xavier · 2004-06-14 17:36 · #B45455

I never said it were preferable, you fool. I was talking about the plugin.
You really post for posting sake, don't you? I should reset your count like everyone suggests.

### Marc · 2004-06-14 17:44 · #B45468

Actualy I posted that for the people that don't know how to do the && || thing. I guess for educational perpouses then *shrugs* now he knows somthing more.

### Asimir · 2004-06-14 18:00 · #B45479

Yes, now he knows you're a spamming retard Wink
