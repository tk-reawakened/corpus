---
kind: forum-thread
id: "toolkitzone-forums/23360"
site: "toolkitzone.com"
board: "toolkitzone.com forums (phpBB2)"
forum: "Programming"
skin: "phpbb2"
thread_id: "23360"
title: "More Simple PHP"
original_url: "http://toolkitzone.com/forums/viewtopic.php?t=23360"
written: "2005-09-09T19:16:00"
last_post: "2005-09-11T01:07:00"
date_confidence: "exact"
captured: ["20051031005602"]
author: "lavarock09"
repliers: ["Caliber Mengsk", "zyrshnikashnu", "matt72186"]
authors: ["lavarock09", "Caliber Mengsk", "zyrshnikashnu", "matt72186"]
posts_present: 13
pages_present: [1]
pages_total: 1
posts_per_page: 15
complete: true
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forums/viewtopic.php__p_255758_amp_3Bsid_9cb115aff7d3b8ba5814f106b2283f26", captured: "20051031005602", sha256: "fee0b3cf7445a8db1fc25b713ff3373b1eb62bf7e0bbc76b3d3472f871f02e89", wayback_url: "https://web.archive.org/web/20051031005602/http://www.toolkitzone.com/forums/viewtopic.php?p=255758&amp%3Bsid=9cb115aff7d3b8ba5814f106b2283f26"}
links:
  - {url: "http://www.m3xvv.co.uk/PHP%20Tutorial/index2.php", status: "external", local: null}
  - {url: "http://yoursite.com/mypage.php?month=January", status: "external", local: null}
---

# More Simple PHP

### lavarock09 · 2005-09-09 19:16 · #B255684

Hey again,
Ok, I'm on the same basic principal as on the other topic I made, but I'm doing it the other way round,
You put your DOB in and It tells you your Starsign
so, this is my code,
index2.php

**Code:**

```
<form action="action2.php" method="post">

<p>Your Date Of Birth:<br>

Day: &nbsp;&nbsp;<select name="day">

<option>01</option>

<option>02</option>

<option>03</option>

<option>04</option>

<option>05</option>

<option>06</option>

<option>07</option>

<option>09</option>

<option>10</option>

<option>11</option>

<option>12</option>

<option>13</option>

<option>14</option>

<option>15</option>

<option>16</option>

<option>17</option>

<option>18</option>

<option>19</option>

<option>20</option>

<option>21</option>

<option>22</option>

<option>23</option>

<option>24</option>

<option>25</option>

<option>26</option>

<option>27</option>

<option>28</option>

<option>29</option>

<option>30</option>

<option>31</option>

</select>

Month: &nbsp;&nbsp;<select name="month">

<option>January</option>

<option>February</option>

<option>March</option>

<option>April</option>

<option>May</option>

<option>June</option>

<option>July</option>

<option>August</option>

<option>September</option>

<option>October</option>

<option>November</option>

<option>December</option>

</select>

<input name="Submit" type="submit" value="Submit">

</form>
```

action2.php

**Code:**

```
Your star sign is...<?

if ($_POST['day' && 'month'] == '1' && 'January') {

echo 'Capricorn';

}

elseif ($_POST['day' && 'month'] == '2' && 'January') {

echo 'Capricorn';

}

?>
```

I know it's small, but the output of this is 'Your star sign is...'
with no Starsign, so what is the problem here, please don't say it is the '&&'

### Caliber Mengsk · 2005-09-09 19:26 · #B255688

**Code:**

```
Your star sign is...<?

if ($_POST['month'] == 'January') {

   If($_POST['day'] == '1'){

      echo 'Capricorn';

   }

   elseif($_POST['day'] == '2'){

      echo 'Capricorn';

   }

}

?>
```

Keep it simple... If you are going to do every day in one month in a row. Also, you can modify the if statement to do two things. (AKA if you want a collection of days instead of just one day at a time. View below for an example.)

**Code:**

```
//I don't know the eaxct days, so I am going to guess here.

if ($_POST['month'] == 'January') {

   If($_POST['day']  >= '1'  and $_Post['day'] <= 23)

    //begining day first, ending day second.

   {

      echo 'Capricorn';

   }

}
```

EDIT:
Also, for the days, it would be simpler to do a while loop I think.
Example:

**Code:**

```
<?

unset($daylist);

$Day = 0;

$maxdays = 31;

While($day < 31)

{

   $day += 1;

   $daylist .= "<option>$day</option>";

}

Echo $daylist;

?>
```

That way, depending on what month you have selected, you can set it to change the $maxdays to the correct number.
a .= means add to. So, you could set all of your info into $daylist and have it all show still.
EDIT AGAIN:
So, all of the code I ammended to would be like this to get the same thing you wanted.

**Code:**

```
<form action="action2.php" method="post">

<p>Your Date Of Birth:<br>

Day: &nbsp;&nbsp;<select name="day">

<?

unset($daylist);

$Day = 0;

$maxdays = 31;

While($day < 31)

{

   $day += 1;

   $daylist .= "<option>$day</option>";

}

Echo $daylist;

?>

</select>

Month: &nbsp;&nbsp;<select name="month">

<option>January</option>

<option>February</option>

<option>March</option>

<option>April</option>

<option>May</option>

<option>June</option>

<option>July</option>

<option>August</option>

<option>September</option>

<option>October</option>

<option>November</option>

<option>December</option>

</select>

<input name="Submit" type="submit" value="Submit">

</form>
```

That should just about do it.

### lavarock09 · 2005-09-09 19:45 · #B255692

**Caliber Mengsk wrote:**

> So, all of the code I ammended to would be like this to get the same thing you wanted.
>
> **Code:**
>
> ```
> <form action="action2.php" method="post">
>
>
> <p>Your Date Of Birth:<br>
>
>
> Day: &nbsp;&nbsp;<select name="day">
>
>
> <?
>
>
> unset($daylist);
>
>
> $Day = 0;
>
>
> $maxdays = 31;
>
>
> While($day < 31)
>
>
> {
>
>
>    $day += 1;
>
>
>    $daylist .= "<option>$day</option>";
>
>
> }
>
>
> Echo $daylist;
>
>
> ?>
>
>
> </select>
>
>
> Month: &nbsp;&nbsp;<select name="month">
>
>
> <option>January</option>
>
>
> <option>February</option>
>
>
> <option>March</option>
>
>
> <option>April</option>
>
>
> <option>May</option>
>
>
> <option>June</option>
>
>
> <option>July</option>
>
>
> <option>August</option>
>
>
> <option>September</option>
>
>
> <option>October</option>
>
>
> <option>November</option>
>
>
> <option>December</option>
>
>
> </select>
>
>
> <input name="Submit" type="submit" value="Submit">
>
>
> </form>
> ```
>
> That should just about do it.
>

using this though would still give february 31 days in the dropdown list which is imposible, would I just do this code in action2.php when a user di d a non existant day e.g. February 30th and 31st,

**Code:**

```
Your starsign is<?

if ($_POST['month'] == 'February') {

   if($_POST['day']  >= '30' and $_POST['day'] <= '31')

   {

      echo 'none existant as it is impossible to have a birthday on this date';

   }

}
```

### Caliber Mengsk · 2005-09-09 19:52 · #B255697

Or... you could not have the days, and send it to the page after the select the month.

**Code:**

```
<select name='month' onChange='window.location.href=month.value;'>
```

That "should" send you to the same page... then you can just do if/ifelse statements to say how many days.

**Code:**

```
$month = $_GET['month'];

If($month = "January")

{

   $Maxdays = 31;

}ElseIf($month = "February"){

   $Maxdays = 28;

}
```

EDIT:
((The first thing should give you an url like
<http://yoursite.com/mypage.php?month=January>
Or whatever month was selected. That is why you use the $_GET option... to get the variable from the url.))

### lavarock09 · 2005-09-09 20:02 · #B255698

I'm gonna do the

**Code:**

```
if ($_POST['month'] == 'May') {

   if($_POST['day']  >= '1' and $_POST['day'] <= '20')

   {

      echo 'Taurus';

   }

}
```

code,
and I might try the other one once I've done this, thanks for all your help

### Caliber Mengsk · 2005-09-09 20:26 · #B255700

No problem. I started out in PHP recently too, (a few months ago) and I know it is a pain to try to figure stuff out in the begining.

### lavarock09 · 2005-09-09 20:45 · #B255706

you can see the current version here,
<http://www.m3xvv.co.uk/PHP%20Tutorial/index2.php>

### zyrshnikashnu · 2005-09-09 23:09 · #B255758

Sagittarius (3 Dec) doesn't work. Sad

### matt72186 · 2005-09-10 08:48 · #B255895

Just to help you out a little bit:

**Code:**

```
$output = 'Day: &nbsp;&nbsp;<select name="day">'."\n";

for ($tmp = 1; $tmp <= 31; $tmp++) {

   $output .= '<option>' . $tmp . '</option>'."\n";

}

$output .= 'Month: &nbsp;&nbsp;<select name="month">'."\n";

for ($tmp = 1; $tmp <= 12; $tmp++) {

   $output .= '<option>' . date('F', mktime(0, 0, 0, $tmp)) . '</option>' . "\n";

}

$output .= '</select>'."\n";

print $output;
```

### lavarock09 · 2005-09-10 10:40 · #B255913

**zyrshnikashnu wrote:**

> Sagittarius (3 Dec) doesn't work. Sad
>

I think I have figured out the problem,
The last statement was an elseif on, so I changed it to just else so the code is this,

**Code:**

```
else ($_POST['month'] == 'December') {

   if($_POST['day']  >= '1' and $_POST['day'] <= '21')

   {

      echo 'Sagittarius <img src="images/icons_sagittarius_01.gif" align="middle"';

   }

}
```

But there is something wrong with this, I get this error, 'unexpected '{'' on line 149,
Line 149 is this line,

**Code:**

```
else ($_POST['month'] == 'December') {
```

EDIT: I've changed the code fo Sagittarius,
It's now,

**Code:**

```
if ($_POST['month'] == 'December') {

   if($_POST['day']  >= '1' and $_POST['day'] <= '21')

   {

      echo 'Sagittarius <img src="images/icons_sagittarius_01.gif" align="middle"';

   }

}
```

It seems to work,
Please Test it and give me comments, please tell me if you find any more bugs

### Caliber Mengsk · 2005-09-10 17:57 · #B256036

Might want to change the border color to something besides default. (aka, bordercolor='darkred' inside of all td tags.) Because it is just odd to have so many darks, then have a light gray border.

### zyrshnikashnu · 2005-09-11 01:00 · #B256181

I have found that bordercolor isn't the proper attribute to use in the <table> tag. Instead, use CSS to set border-color to a color.

### matt72186 · 2005-09-11 01:07 · #B256185

Learn:
[coe]if (condition1) {
statement1;
} else if (condition2) {
statement2;
} else if (condition3) {
statement3;
} else if ...
else
{
statementn;
}
it's more efficient since this interprets to one single instruction. You probably lacked a space between else and if, a common mistake.
