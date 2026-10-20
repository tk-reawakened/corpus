---
kind: forum-thread
id: "toolkitzone-forums/22720"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Programming"
skin: "phpbb2"
thread_id: "22720"
title: "Keeping information displayed (PHP 'gin)"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=22720"
written: "2005-08-21T03:38:00"
last_post: "2005-08-22T00:44:00"
date_confidence: "exact"
captured: ["20051031003559"]
author: "zzz"
repliers: ["matt72186", "Sander", "zyrshnikashnu"]
authors: ["zzz", "matt72186", "Sander", "zyrshnikashnu"]
posts_present: 10
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_248763_amp_3Bsid_9cb115aff7d3b8ba5814f106b2283f26", captured: "20051031003559", sha256: "0f6f7a17ec06f99fad09a453f57d11ebf00c763e2058b84ea35c92b58fed4308", wayback_url: "https://web.archive.org/web/20051031003559/http://www.toolkitzone.com/forums/viewtopic.php?p=248763&amp%3Bsid=9cb115aff7d3b8ba5814f106b2283f26"}
links: []
---

# Keeping information displayed (PHP 'gin)

### zzz · 2005-08-21 03:38 · #B248561

Mkay, I am making a "Chat" thing for a lil project I'm gonna do...but I can only get it to display the last part displayed...
Any help?

**Code:**

```
Command the sever (Type help for help):

<form action="chat.php" method="post">

Name: <input type="text" name="chat"><br>

<input type="submit" value="Submit">

</form>

</form>

<HR>

<?php

$res=$_POST['chat'];

$c1=help;

$c2=yell;

echo '<font color=red>';

echo "user>";

echo $name;

echo "<BR>";

echo '</font><font color=green>';

if ($res==$c1) {

echo "server>Helping!";

}

if($res==$c2) {

echo "server>Yelling!";

}

else

{

echo "server>Unknown command!";

}

?>
```

If you don't get what I'm saying, I mean, like keep a log of what the user/"server" says.

### matt72186 · 2005-08-21 04:15 · #B248569

save it to a database... or do you even know what that is?

### zzz · 2005-08-21 06:41 · #B248586

Yes, I know what a Database is Wink.
Long story short: I don't have em anymore.
But what I'm meaning, you don't need one. It doesn't stay there forever, just keep 20 or so of the messages displayed, and only displays them when they are staying there, that time only...right now, it just displays 2 messages, 1 from "user", and 1 from "server".

### matt72186 · 2005-08-21 09:43 · #B248613

Well here's the thing, PHP starts a new, unique process every page load, meaning it doesn't remember anything from previous page loads from yourself or any other user. Every page load is unique and shares no connection with the last unless you program a system for it to remember. There are a few ways to do this, you can use a database to store the messages, or you can save it to a text file, or save it however you want, it's not going to save itself.
But of course, you knew that right? I mean it was obvious enough, page 1 or 2 on the PHP Manual.

### Sander · 2005-08-21 11:01 · #B248621

Just store it in a text file and get the last x messages.
Or perhaps use sessions.

### zzz · 2005-08-21 17:25 · #B248651

**matt72186 wrote:**

> But of course, you knew that right? I mean it was obvious enough, page 1 or 2 on the PHP Manual.
>

There you go agian, being an ass.

**Sander wrote:**

> Just store it in a text file and get the last x messages.
>

That wouldn't work :\ (well it would work, but not for my purposes...

**Sander wrote:**

> Or perhaps use sessions.
>

::googles::
I think I have an idea, however, so I'm gonna go try somthing Razz.

### zyrshnikashnu · 2005-08-21 23:08 · #B248735

I think the text file idea would be best. I doubt sessions would work, unless you managed to somehow exchange session variables between users (I assume there's more than one user).

### zzz · 2005-08-21 23:34 · #B248745

Its not a chat, though. I figured it out, via sessions.

**Code:**

```
<?php

session_start();

$lstmsg = $_SESSION['lstmsg'];

$lstres = $_SESSION['lstres'];

$res=$_POST['chat'];

$save=save;

$about=about;

$help=help;

$helpres="server>List of commands:<BR>help-Brings up help menu<BR>save-Gives you a save code<BR>about-gives you information'<font color=white>'";

$saveres="server>Generating save code...<BR>Save code:";

$errorres="server>Unknown command!!!'</font>'";

echo "user>";

echo $lstmsg;

echo "<BR>";

echo $lstres;

echo "<BR>";

$_SESSION['lstmsg']=$res;

echo '<font color=red>';

echo "user>";

echo $res;

echo "<BR>";

echo '</font><font color=green>';

if ($res==$help) {

echo $helpres;

  session_unregister (lstres );

$_SESSION['lstres']=$helpres;

 }

if($res==$save) {

echo $saveres;

echo base64_encode($login);

session_unregister (lstres );

$_SESSION['lstres']=$saveres;

}

else

{

        echo $errorres;

          session_unregister (lstres );

        $_SESSION['lstres']="server>List of commands:<BR>help-Brings up help menu<BR>save-Gives you a save code<BR>about-gives you information'<font color=white>'";

}

?>

<HR>

<font color=black>

Command the sever (Type help for help):

<form action="chat.php" method="post">

Name: <input type="text" name="chat"><br>

<input type="submit" value="Submit">

</form>
```

### matt72186 · 2005-08-22 00:35 · #B248756

**zzz wrote:**

> Mkay, I am making a "Chat" thing for a lil project I'm gonna do...but I can only get it to display the last part displayed...
>

**zzz wrote:**

> Its not a chat, though. I figured it out, via sessions.
>

Make up your damn mind. For the purpose of a "chat" thing as you originally requested our solutions (database or text) are the only plausible implementations. If you had been more specific I wouldn't have to attack your ignorance so much.

### zzz · 2005-08-22 00:44 · #B248763

Its not a chat in the sense he was saying.
I was as clear as I could be.
