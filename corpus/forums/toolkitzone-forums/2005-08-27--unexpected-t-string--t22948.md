---
kind: forum-thread
id: "toolkitzone-forums/22948"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Programming"
skin: "phpbb2"
thread_id: "22948"
title: "Unexpected T_STRING"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=22948"
written: "2005-08-27T21:56:00"
last_post: "2005-08-30T17:55:00"
date_confidence: "exact"
captured: ["20051029105618"]
author: "zzz"
repliers: ["Caliber Mengsk", "zyrshnikashnu", "jello", "Sander", "Colin"]
authors: ["zzz", "Caliber Mengsk", "zyrshnikashnu", "jello", "Sander", "Colin"]
posts_present: 8
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_252272_amp_3Bsid_9cb115aff7d3b8ba5814f106b2283f26", captured: "20051029105618", sha256: "cf2d650f0faa45fc94e0fbd44ca08e284309a9fba960ba0b28f82b1f85fd95ea", wayback_url: "https://web.archive.org/web/20051029105618/http://www.toolkitzone.com/forums/viewtopic.php?p=252272&amp%3Bsid=9cb115aff7d3b8ba5814f106b2283f26"}
links: []
---

# Unexpected T_STRING

### zzz · 2005-08-27 21:56 · #B251061

Yea, getting that error on

**Code:**

```
<input type="hidden" value=$_POST['p1'] name="nm1">
```

Colin said that this would fix it:

**Code:**

```
<input type="hidden" value={$_POST['p1']} name="nm1">
```

But it didn't.
Oh, if Colin reads this, I didn't wanna spam it agian in the chat Razz.

### Caliber Mengsk · 2005-08-29 13:39 · #B251678

O-o.... Didn't I help you with this already in chat??
Anyway, If it is in an echo, you can't use both "s and 's. You have to have a containment around all of your information using one of those, so if you use quotes as the echo containment(or string containment) use something like this...

**Code:**

```
ECHO "<input type='hidden' value='$_POST[p1]' name='nm1'>";
```

That will get the results as you want it. You don't have to have containing quotes inside the Session and post strings contrary to popular belife. So, session and post arrays can look like this...

**Code:**

```
$_POST[p1]

$_SESSION[p1]
```

and I have no clue why you had { and } in your code. Those are just like parenthesis.
Anyway, I suggest quotes (") for containers. If you need quotes (") in your text, simply use two apostrathes (') getting something like this ''. Looks the same, so people get what you mean, and it doesn't mess up the code at all.
EDIT:
Also, to use the info from the hidden item, I belive you need to have the ID=nm1 not Name=nm1. I don't know if either way will work, but I know for certain ID works with PHP. That is what I use.

### zyrshnikashnu · 2005-08-29 16:48 · #B251740

Name has always worked for me. I usually do something like this:

**Code:**

```
<input type="hidden" value="<?=$_POST[pl] ?>" name="nm1">
```

Call me crazy, but I prefer it that way. Razz

### zzz · 2005-08-29 21:01 · #B251866

@Caliber
Yea, I posted this before you helped me Wink
and zy: It wouldn't work for what I was doing Wink.

### Caliber Mengsk · 2005-08-30 13:31 · #B252181

**zzz wrote:**

> @Caliber
> Yea, I posted this before you helped me Wink
> and zy: It wouldn't work for what I was doing Wink.
>

He probably meant something like that, but he forgot an echo and put in an =. As well, he forgot the end code semicolon(Wink. Should be like this to work:

**Code:**

```
<input type="hidden" value="<? Echo $_POST[pl]; ?>" name="nm1">
```

That would work too.
EDIT:
It does the same exact thing as Echoing all of it... so it doesn't really matter which you use.
You could also set it all to a string (personally I do this for easier template manipulation.) then just echo the string. VERY usefull in templates.

**Code:**

```
$Poll = "<input type='hidden' value='<? Echo $_POST[pl]; ?>' name='nm1'>";

/* At this point, instead of keeping multiple strings, you can simply add to the above string like this. */

if(isset($_SESSION[option1]))

{

$Poll .="<input type='radio' value='<? Echo $_SESSION[option1]; ?>";

}

if(isset($_SESSION[option2]))

{

$Poll .="<input type='radio' value='<? Echo $_SESSION[option2]; ?>";

}

if(isset($_SESSION[option3]))

{

$Poll .="<input type='radio' value='<? Echo $_SESSION[option3]; ?>";

}

if(isset($_SESSION[option4]))

{

$Poll .="<input type='radio' value='<? Echo $_SESSION[option4]; ?>";

}

/* In your other program (the template) you would just put something like this */

Echo $poll;
```

The above code would make it so that it only adds the options if there is something set to them. You can just open your file or connect to the database to get the options and so on.
((That is if I remember right, you were making a poll with this.))

### jello · 2005-08-30 17:08 · #B252263

**Caliber Mengsk wrote:**

> He probably meant something like that, but he forgot an echo and put in an =. As well, he forgot the end code semicolon(Wink. Should be like this to work:
>
> **Code:**
>
> ```
> <input type="hidden" value="<? Echo $_POST[pl]; ?>" name="nm1">
> ```
>
> That would work too.
> EDIT:
> It does the same exact thing as Echoing all of it... so it doesn't really matter which you use.
>

Indeed. I used to think the same thing... until I tried to correct someone who did it with the <?=$var ?> and was proved wrong.

### Sander · 2005-08-30 17:32 · #B252267

You can do that line in a few ways, zzz:

**Code:**

```
echo '<input type="hidden" value="' . {$_POST['p1']} . '" name="nm1">';
```

**Code:**

```
echo "<input type='hidden' value='{$_POST['p1']}' name='nm1'>";
```

**Code:**

```
<input type="hidden" value="<={$_POST['p1']}?> name="nm1">
```

### Colin · 2005-08-30 17:55 · #B252272

Sander, zzz's intentionally confusing here, but what he's showing is actually part of something inside a quote.
I realize another problem now too. That string is inside single quotes, isn't it, zzz? You have to do the first thing Sander shows with the dots, only without the echo.
