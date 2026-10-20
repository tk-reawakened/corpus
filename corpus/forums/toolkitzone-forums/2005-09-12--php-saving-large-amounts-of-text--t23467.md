---
kind: forum-thread
id: "toolkitzone-forums/23467"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Programming"
skin: "phpbb2"
thread_id: "23467"
title: "PHP, Saving large amounts of text"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=23467"
written: "2005-09-12T23:03:00"
last_post: "2005-09-14T00:53:00"
date_confidence: "exact"
captured: ["20051107035654"]
author: "TheCPPFreak220"
repliers: ["matt72186", "Colin", "Dan"]
authors: ["TheCPPFreak220", "matt72186", "Colin", "Dan"]
posts_present: 9
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_257069_amp_3Bsid_cc194ea384cda74cd58b441534454b34", captured: "20051107035654", sha256: "3a49a47e1c77bfdb88c620c0d72776ba9a94bcbc9a15f66b066a98ddf8689f5d", wayback_url: "https://web.archive.org/web/20051107035654/http://www.toolkitzone.com/forums/viewtopic.php?p=257069&amp%3Bsid=cc194ea384cda74cd58b441534454b34"}
links: []
---

# PHP, Saving large amounts of text

### TheCPPFreak220 · 2005-09-12 23:03 · #B256679

Ok, i have a php page with a form on it.
In this for there is a text box, and a submit button
Now, how would i send the text to a different page or save the text in this box to a file when the user presses submit?

### matt72186 · 2005-09-13 00:22 · #B256694

**Code:**

```
<html>

       <head>

              <title>Save a File</title>

       </head>

       <body>

              <form action="save.php" method="post">

                     <textarea name="source"></textarea>

                     <input type="submit" />

              </form>

       </body>

</html>
```

**Code:**

```
<html>

       <head>

              <title>Save a File</title>

       </head>

       <body>

              <?php

$source = isset($_POST['source'])? $_POST['source']: '';

$fp = fopen('file.txt', 'w');

if (fwrite($fp, $source))

       print 'File Saved Successfully';

else

       print 'File Not Saved';

fclose($fp);

?>

       </body>

</html>
```

### TheCPPFreak220 · 2005-09-13 02:19 · #B256725

Wouldn't there be a finite limit on the amount of text passed through $_POST?

### Colin · 2005-09-13 02:34 · #B256729

No, there's no limit.

### Dan · 2005-09-13 13:14 · #B256796

Actually, there's a hard-limit set in php.ini, by default it's set to 8mb.

### Colin · 2005-09-13 13:15 · #B256797

There's no limit to the amount you can post. :p
Maybe there's a limit set in php.ini, but there's no practical limit on how high it can be set.

### matt72186 · 2005-09-14 00:34 · #B257049

Well I suppose you're limited by your bandwidth cap (if it exists) in your ISP, and the bandwidth cap in the host receiving the data...
actually there is a limit, without one there would be the potential for exploitation of overflow errors in the server. Typically a server will timeout after so much time of receiving data.

### Colin · 2005-09-14 00:47 · #B257059

There is not a limit. The HTTP standard does not define one.

### matt72186 · 2005-09-14 00:53 · #B257069

Well let's try thinking realistically rather than idealistically.
