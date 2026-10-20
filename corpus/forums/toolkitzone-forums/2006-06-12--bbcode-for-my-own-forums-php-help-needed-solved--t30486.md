---
kind: forum-thread
id: "toolkitzone-forums/30486"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Programming, Computing &amp; Technology"
skin: "phpbb2"
thread_id: "30486"
title: "BBcode for my own forums (php help needed) **Solved"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=30486"
written: "2006-06-12T18:48:00"
last_post: "2006-06-15T14:17:00"
date_confidence: "exact"
captured: ["20060627020639"]
author: "Caliber Mengsk"
repliers: ["Zap!", "zzz", "OBCT", "Xavier", "Colin"]
authors: ["Caliber Mengsk", "Zap!", "zzz", "OBCT", "Xavier", "Colin"]
posts_present: 10
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_327370_amp_3Bsid_4a6f1d5a00106d33697c82f76115a18b", captured: "20060627020639", sha256: "614ccb69449401a15b9db6305f88be09c54f21d1d2ce3c4bbbd7f780f9471ca3", wayback_url: "https://web.archive.org/web/20060627020639/http://toolkitzone.com/forums/viewtopic.php?p=327370&amp%3Bsid=4a6f1d5a00106d33697c82f76115a18b"}
links:
  - {url: "http://toolkitzone.com/forums/.*?", status: "never-captured", local: null}
  - {url: "http://www.calibermengsk.com/test/new_profile/forum.php?mode=view&topicid=4&catid=2&forum=3#23", status: "external", local: null}
---

# BBcode for my own forums (php help needed) **Solved

### Caliber Mengsk · 2006-06-12 18:48 · #B326866

Ok, I have an issue where the BBcode works fine if it is on a single line of text, but, but if it's over multiple lines, it doesn't work right. O-o anyone know why? I have coded my own BBcode part, and my own forums, but I think this is all that is needed.

**Code:**

```
<?

function bbcode($string)

{

   $string = mystriptags($string);

   $string = nl2br($string);

   $string = str_replace(" />", ">", $string);

//Start Code Checks

   $string = NEST('/(\[img\])(.+)(\[\/img\])/'         , '<img src="\\2">'                                       , $string);

   $string = NEST('/(\[url=)(.+)(\])(.+)(\[\/url\])/'      , '<a href="\\2" target="_blank">\\4</a>'                              , $string);

   $string = NEST('/(\[center\])(.+)(\[\/center\])/'      , '<center>\\2</center>'                                    , $string);

   $string = NEST('/(\[b\])(.+)(\[\/b\])/'            , '<b>\\2</b>'                                          , $string);

   $string = NEST('/(\[i\])(.+)(\[\/i\])/'            , '<i>\\2</i>'                                          , $string);

   $string = NEST('/(\[u\])(.+)(\[\/u\])/'            , '<u>\\2</u>'                                          , $string);

   $string = NEST('/(\[url\])(.+)(\[\/url\])/'         , '<a href="\\2" target="_blank">\\2</a>'                              , $string);

   $string = NEST('/(\[quote=)(.+)(\])(.+)(\[\/quote\])/'      , '<center><table class="quote"><tr><td>Quote:<center><hr width="80%"></center>\\2</td></tr></table></center>'      , $string);

   $string = NEST('/(\[quote\])(.+)(\[\/quote\])/'         , '<center><table class="quote"><tr><td>Quote:<center><hr width="80%"></center>\\2</td></tr></table></center>'      , $string);

   $string = NEST('/(\[size=)(.+)(\])(.+)(\[\/size\])/'      , '<font style="font-size: \\2px;">\\4</font>'                              , $string);

//End Code Checks

   RETURN $string;

}

function NEST( $origonal, $replace, $open)

{

   $lastopen = "";

   while($open != $lastopen)

   {

      $lastopen = $open;

      $open = preg_replace($origonal, $replace, $open);

   }

   return $open;

   unset($lastopen);

   unset($open);

   unset($origonal);

   unset($replace);

}

function strip_html($data)

{

   $data=preg_replace("/(\\t|\\r|\\n)/","",$data);  // remove new lines \\n, tabs and \\r

   return $data;

}

function myStripTags($string)

{

// Function by xyexz at yahoo dot com

// it was found on PHP.net.

   //while there are tags left to remove

   while(strstr($string, '>'))

   {

       //find position of first carrot

       $currentBeg = strpos($string, '<');

       //find position of end carrot

       $currentEnd = strpos($string, '>');

       //find out if there is string before first carrot

       //if so save it in $tmpstring

       $tmpStringBeg = @substr($string, 0, $currentBeg);

       //find out if there is string after last carrot

       //if so save it in $tmpStringEnd

       $tmpStringEnd = @substr($string, $currentEnd + 1, strlen($string));

       //cut the tag from the string

       $string = $tmpStringBeg.$tmpStringEnd;

   }

   return $string;

}

?>
```

(O-o... looks better and cleaner in notepad.)
To see what I mean by it's not working with multiple lines, look here:
<http://www.calibermengsk.com/test/new_profile/forum.php?mode=view&topicid=4&catid=2&forum=3#23>
Please... don't comment on the layout and color scheme... I know, I suck at it... If anyone wants to help me with that too, I would appreciate it.

### Zap! · 2006-06-12 19:37 · #B326876

IMO the site looks great, other than two things:
1: The MECHACIDE text looks out of place
2: The rectangle bit under "Post Reply" looks a bit too wide, though that may just be because I run in really high resolution, but I doubt it.
Other than that, my compliments, and those are just nit-picky things anyhow.
As for you're BBCode not working when it spans multiple lines.. hm.. IMO, you might want to just change every instance of into <b>, that WOULD fix it, and ofc, when you change a [b] into a <b> just set a varible thats says you have an open [b] and then whenever you find your next you make it say that the tag is closed, and if you get to the end of the post, and you havn't found a [/b], add one.
I don't know exactly what you are doing, atm, becuase my php is very limited, if you're already doing the above, then sorry for wasting your time to read it, but if not, I think it might be worth a shot.

### zzz · 2006-06-12 20:27 · #B326899

Sorta off topic...I don't realy think it's considered BBcode if it's not running on phpBB...
You could just make it simple, and use HTML formating, as my site uses...

### Caliber Mengsk · 2006-06-12 20:31 · #B326904

That's what I am doing with the preg_replace.
For example

**Code:**

```
'/(\[img\])(.+)(\[\/img\])/'

This is the equivilent of

([img]) (.+) ([/img])

The first parenthesis is \\1

The second parenthesis is \\2

The third parenthesis is \\3

So, the next section is:

<img src="\\2">

\\2 would be the area between [img] and [/img].

Makes things pretty simple to understand right?

Because it does it all in one line, it only replaces the bbcode tags of things like [b] bold [/b]

[b]but it wouldn't

replace

something

like this.[/b]

Doesn't make sense in my view, but whatever the server says, I can't force it to do otherwise.
```

The only problem is, evidentally preg_replace only does it on one line's worth of information. This is quite bothersome as you can see.
EDIT:
Crap... I figured it out.... Thanks to php.net.
'/\[b\](http://toolkitzone.com/forums/.*?)\[\/b\]/ims'
instead of
'/(\[b\])(.+)(\[\/b\])/'
the ims is what allows multiple lines... Sorry for bothering everyone.
Oh, and as for the BBcode thing, That be like making and RPGcode editor and saying it's Bobscode instead of RPGcode. It's still the same programming language, weather I made the engine that runs it or not.

### OBCT · 2006-06-13 01:37 · #B327032

BBCode is actually Bulletin Board Code, so it isn't phpBB dependent.

### Caliber Mengsk · 2006-06-13 13:34 · #B327149

@Zap!: Image of Mechacide has been replaced... I made that before anything else for the site XD
As for the other part of your 2 things, O-o are you talking about where the username of the poster is?
O-o if so, well, there will be the image of your mech there eventually. It will look right afterwards. If you aren't talking about there... I don't know what you are talking about.
Also, it doesn't matter how large or small your screen resolution is, the site has been designed for an 800x600 view, just because..... uh..... XD It seems to me that most people in the world like 800x600 over 1024x768(I use this one).
@OBCT: Thanks for backing me up.

### Zap! · 2006-06-13 14:05 · #B327155

Oh wow, the new image looks soooooooo much better!
Nice work, and I run in 1280x1024. Razz

### Xavier · 2006-06-13 14:08 · #B327157

The majority run 1024x768 or above, Calib. But the 800x600 users moan a lot whenever a site doesn't "fit" for them, so it seems like there's more of them Wink. The next site I do will cater for 1024x768+ primarily.

### Colin · 2006-06-14 01:21 · #B327370

Think of Delano and his 8 MB graphics card!

### Caliber Mengsk · 2006-06-15 14:17 · #B327829

I design mine for 800x600... I suppose I could make it change depending on your screenres (There's some way to get it if I remember right) But, that's to much work for me...
O-o I could have had it do a 100% width also... but I don't like it that much, Besides, my layout seems to work pretty good, wether in forums or not.
