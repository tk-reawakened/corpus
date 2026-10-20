---
kind: forum-thread
id: "toolkitzone-forums/10433"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "programming"
skin: "phpbb2"
thread_id: "10433"
title: "PHP: HTML in a string"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=10433"
written: "2004-10-21T01:37:00"
last_post: "2004-10-25T01:19:00"
date_confidence: "exact"
captured: ["20041226085519"]
author: "zyrshnikashnu"
repliers: ["Ersuis", "Zap!", "Woozy", "Colin", "Levi"]
authors: ["zyrshnikashnu", "Ersuis", "Zap!", "Woozy", "Colin", "Levi"]
posts_present: 12
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_116512_amp_", captured: "20041226085519", sha256: "f1a1546337a24d4a17e55c0aa063b14c8829ef96cf6f0c39c3112ef20c79fddd", wayback_url: "https://web.archive.org/web/20041226085519/http://www.toolkitzone.com/forums/viewtopic.php?p=116512&amp="}
links:
  - {url: "http://www.cywh.com/ot", status: "external", local: null}
---

# PHP: HTML in a string

### zyrshnikashnu · 2004-10-21 01:37 · #B114099

I've got a PHP script that takes text from my forum and puts it on a seperate page. This works quite well. The trouble is, if I put HTML in the text, it won't execute that HTML. It simply displays the tags. My question is, how can I make that HTML work? I know it's possible in some way, as can be seen [here](http://www.cywh.com/ot). Please help me out!
Here are the important parts of the code, though I doubt you'll need them (and yes, I did connect to the database beforehand.):

**Code:**

```
<?

$toptitle = mysql_query("SELECT topic_title FROM phpbb_topics WHERE forum_id = '24'");

$titlerow[0] = mysql_fetch_row($toptitle);

$titlerow[1] = mysql_fetch_row($toptitle);

$titlerow[2] = mysql_fetch_row($toptitle);

$titlerow[3] = mysql_fetch_row($toptitle);

$titlerow[4] = mysql_fetch_row($toptitle);

$numrows = mysql_num_rows($toptitle);

$postid = mysql_query("SELECT topic_first_post_id FROM phpbb_topics WHERE forum_id = '24'");

$idrow0 = mysql_fetch_row($postid);

$idrow1 = mysql_fetch_row($postid);

$idrow2 = mysql_fetch_row($postid);

$idrow3 = mysql_fetch_row($postid);

$idrow4 = mysql_fetch_row($postid);

$posttext[0] = mysql_query("SELECT post_text FROM phpbb_posts_text WHERE post_id = $idrow0[0]");

$posttext[1] = mysql_query("SELECT post_text FROM phpbb_posts_text WHERE post_id = $idrow1[0]");

$posttext[2] = mysql_query("SELECT post_text FROM phpbb_posts_text WHERE post_id = $idrow2[0]");

$posttext[3] = mysql_query("SELECT post_text FROM phpbb_posts_text WHERE post_id = $idrow3[0]");

$posttext[4] = mysql_query("SELECT post_text FROM phpbb_posts_text WHERE post_id = $idrow4[0]");

$textrow[0] = mysql_fetch_row($posttext[0]);

$textrow[1] = mysql_fetch_row($posttext[1]);

$textrow[2] = mysql_fetch_row($posttext[2]);

$textrow[3] = mysql_fetch_row($posttext[3]);

$textrow[4] = mysql_fetch_row($posttext[4]);

$id = $numrows;

$lowerid = $id - 5;

while ( $id > $lowerid )

{

   ?>

   <font size="4">

   <?

   echo $titlerow[$id][0];

   ?>

   <font size="3">

   <?

   echo $textrow[$id][0];

   $id = $id - 1;

   ?>

   </font>

   </font>

   <p>

   <hr>

   <p>

   <?

}

?>
```

### Ersuis · 2004-10-21 04:11 · #B114227

Remember to save your pages with a php extension (like .php), and use <?php ?> instead of <? ?>.

### zyrshnikashnu · 2004-10-21 20:14 · #B114544

???
I don't understand how this solves my problem, but I suppose I can use the <?php tag instead of <?. But I don't see how that will help me. Question
EDIT: No, that didn't help me at all. I was under the impression that <? was the same as <?php, anyway. What is the difference?

### Zap! · 2004-10-21 21:30 · #B114673

None that I know of, prehaps it is just a browser based thing?

### Woozy · 2004-10-21 21:41 · #B114693

It can't be a browser based thing since PHP is server-side. I always use <? since it's shorter than <?php.

### Zap! · 2004-10-21 22:14 · #B114753

Oh duh....
Well I dont know what I was thinking I dont use PHP much....
I always use <? too.. [shrug] Maybe Ersuis just wants him to wear out his typing power! EVIL!

### Colin · 2004-10-21 22:17 · #B114755

<? defaults to different things depending on the server.

### zyrshnikashnu · 2004-10-21 22:20 · #B114759

I suppose I should just ask Cyra, then.

### Levi · 2004-10-22 07:28 · #B115123

Well I use ASP instead of PHP but programming techniques should be the same.
First, I originally thought that you meant the HTML tags we see in the code didn't execute. Now I see you mean that if someone enters text with HTML, that HTML won't execute. I don't know if anyone else did, but that may have been for that post about the <? and <?php.
Second, that link. Does it show a page that demonstrates where the code didn't execute correctly? Because the only thing I saw like that, was some image tags what weren't entered correctly.
Also the method you use to post the entered text, have you tried it with regular text and HTML maybe its how you are printing the text that is haulting the HTML.

### zyrshnikashnu · 2004-10-24 03:28 · #B116055

**Levi wrote:**

> Second, that link. Does it show a page that demonstrates where the code didn't execute correctly? Because the only thing I saw like that, was some image tags what weren't entered correctly.
> Also the method you use to post the entered text, have you tried it with regular text and HTML maybe its how you are printing the text that is haulting the HTML.
>

What link are you talking about? I'm confused... please explain, Levi.
As to the method used to post text, I'll have to look into that. You see, I'm using phpBB, so I don't know all of the specs.

### Levi · 2004-10-24 04:34 · #B116089

"as can be seen here. "
The word here is a link to some sort of forums. I was wondering if this showed the result of a failed attempt or if it showed what you hoped to accomplish. At the time I was confused, but looking at it and seeing that pictures are posted, it seems that this is the result you hope to achieve.

### zyrshnikashnu · 2004-10-25 01:19 · #B116512

Yes. That page takles text from a forum and puts it on a seperate page. I've figured that much out. I've also managed to enable most HTML, but I still don't have line breaks. I have an idea to create my own, though. Thank you everyone for your support.
