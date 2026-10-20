---
kind: file
id: "toolkitzone.com/95"
site: "toolkitzone.com"
title: "By Luke Scott (Cy)"
original_url: "http://www.toolkitzone.com/fileman.php?id=10&file=95"
written: null
date_confidence: "unknown"
updated: null
captured: ["20041108111045", "20041113122058"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/fileman.php__id_3_file_95", captured: "20041108111045", sha256: "c88082d0fcd8823b3f3b20780623e2d13fbce52d9f4f006a64cfa89e6f75db8f", wayback_url: "https://web.archive.org/web/20041108111045/http://www.toolkitzone.com/fileman.php?id=3&file=95"}
  - {path: "wayback/toolkitzone.com/fileman.php__id_10_file_95", captured: "20041113122058", sha256: "ef47158a6d96a9febde58547452a2f241068834dabffa2b038fb8a4ec4e639d3", wayback_url: "https://web.archive.org/web/20041113122058/http://www.toolkitzone.com/fileman.php?id=10&file=95"}
---

# By Luke Scott (Cy)

Saving & Loading the Tile-Set Format
**By Luke Scott (Cy)**
Introduction
The Tile-Set format is one of the simplest formats there is. People have a problem understanding how it works because they have limited programming knowledge. When starting out in Visual Basic, they might learn how to save/load a file in ASCII format (which is what *.prg files are saved as). ASCII is a normal text format. If you were to open up an ASCII file in word, you would see exactly what you typed in. Tile-Sets are saved in binary, which most people have no clue how to do this. In binary you may save multiple variable types: arrays, strings, integers, bytes, words.
Tile-Set Makeup
```
Header (6 bytes)
Variable Type Description
WORD tile version (i.e 20 for v2.0)
WORD Number of Tiles (since limit is 255, dont trust this)
Max Tile # = 65536
WORD Detail
Or
Variable Type Description
BYTE tile version (i.e 20 for v2.0)
BYTE (empty)
BYTE Number of Tiles (since limit is 255, dont trust this)
Max Tile # = 65536
BYTE Overflow (0=no, 1=yes) [theory, may not be correct]
BYTE Detail Level
BYTE (empty)
Tile Pixels (RGB)
Variable Type Description
BYTE red
BYTE green
BYTE blue
```
Followed by the header (made up of 3 word variables) is a tile. After each tile is another tile etc There is no separation between tiles. You know how many bytes each tile is by the detail level.
```
Detail Level
1 All tiles are 32x32 pixels x 16.7 million colors
Each tile is made up of 3072 bytes (32x32x3, 3 = RGB)
Each pixel is made up of the RGB structure (3 bytes)
Transparent Color: Red = 0;Green = 1;Blue = 2
2 All tiles are 16x16 pixels x 16.7 million colors
Each tile is made up of 768 bytes (16x16x3, 3 = RGB)
Each pixel is made up of the RGB structure (3 bytes)
Transparent Color: Red = 0;Green = 1;Blue = 2
3 All tiles are 32x32 pixels x 256 colors
Each tile is made up of 1024 bytes (32x32x1)
Each pixel is made up of 1 byte (DOS 13h VGA palette)
Transparent Color: 255
4 All tiles are 16x16 pixels x 256 colors
Each tile is made up of 256 bytes (16x16x1)
Each pixel is made up of 1 byte (DOS 13h VGA palette)
Transparent Color: 255
5 All tiles are 32x32 pixels x 256 colors
Each tile is made up of 1024 bytes (32x32x1)
Each pixel is made up of 1 byte (DOS 13h VGA palette)
Uses only first 16 colors of the DOS 13h VGA palette
Transparent Color: 255
6 All tiles are 16x16 pixels x 256 colors
Each tile is made up of 256 bytes (16x16x1)
Each pixel is made up of 1 byte (DOS 13h VGA palette)
Uses only first 16 colors of the DOS 13h VGA palette
Transparent Color: 255
```
Detail level 1 and 2 are practically the only detail levels used. Detail level 2 is becoming more rare than ever because TK3 doesnt let you make 16x16 tiles like TK2. Detail levels 3-6 isnt used since the release of TK2, most people want the best quality possible, and most ripped tiles need more colors than the DOS 13h VGA palette can support.
Using For Loops
When the right amount of bytes is obtained, you must use two for loops to draw each pixel.
C++/PHP for Loop Example
```
(x=0; x // Replace TILE_SIZE with 32 or 16 // Replace TILE_SIZE with 32 or 16 // Grab necessary colors, Draw pixel.
```
Visual Basic for Loop Example
```
x y x = 0 TILE_SIZE y = 0 TILE_SIZE Dim as integer Dim as integer ' Replace TILE_SIZE with 31 or 15 ' Replace TILE_SIZE with 31 or 15 ' Grab necessary colors, Draw Pixel Next
Next
```
Reading Binary
Being able to read binary files is the key when working with tile-sets. If you cant read binary, forget about saving/loading tile-sets.
Reading Binary in Visual Basic
Reading binary in Visual Basic is as easy as eating ice cream. You can open a binary file directly and start working with the values.
Example:
```
Filename TileVersion TileCount DetailLevel Filename = App.path & "tileset.tst" filename As #1 #1, 1, TileVersion #1, 3, TileCount #1, 5, DetailLevel #1 "Tile Version: " & cStr(TileVersion) & vbCrlf & "Tile Count(dont trust it): " & cStr(TileCount) & vbCrlf & "DetailLevel: " & cStr(DetailLevel) Dim as String Dim as byte Dim as byte Dim as byte Open For Binary Get Get Get Close MsgBox
```
Saving Binary in Visual Basic
Saving binary in Visual Basic is just as easy. You save to a file directly.
Example:
```
Filename TileVersion TileCount DetailLevel Filename = App.path & "tileset.tst" filename As #1 #1, 1, 20 #1, 3, 139 #1, 5, 1 #1 Dim as String Dim as byte Dim as byte Dim as byte Open For Binary Put ' Version. 20 means v2.0 Put ' # of tiles Put ' Detail Level = 1 Close
```
Reading Binary in PHP
Reading binary in PHP is a little difficult. PHP only opens files in ASCII, but you can tell it to be "binary safe". After you have the contents of the file loaded you must use "unpack" to read the bytes. Most people that know PHP either dont know of unpack, or have no clue how to use it. To see how it works, see . [here](http://fooassociates.com/phpfer/html/rn45re878.html)
Example:
```
$file= ;
$fw = ($file, );
$contents = ($fw, ($fw)); $TileVersion = ( , ( ,$contents)); $TileCount = ( , ( ,$contents)); $DetailLevel = ( , ( ,$contents)); $tst = ( ,$contents); ($fw); $TileCount $DetailLevel; "tileset.tst" fopen "rb" fread filesize // Read file as binary safe. implode unpack "Cbyte" // Get version implode unpack "@2/Cbyte" // Tile Count implode unpack "@4/Cbyte" // D-Level unpack "@7/C*byte" // Bytes for all tiles fclose echo "Tile Version: " "Tile Count: " $TileVersion "Detail Level:"
```
Saving Binary in PHP
Saving binary in PHP is just little difficult. PHP only saves files in ASCII, but you can tell it to be "binary safe". Before you have the you must "pack" the file into binary format. Most people that know PHP either dont know of "pack", or have no clue how to use it. To see how it works, see . [this](http://fooassociates.com/phpfer/html/rn45re877.html)
Example:
```
$file= ;
$TileVersion = 0;
$TileCount = 139;
$DetailLevel = 1;
$tst = $tilebytes $packed = ( , $TileVersion, $TileCount, $DetailLevel, $tst);
$fw = ($file, );
$contents = ($fw, $packed); ($fw); "tileset.tst" 'This is where tile bytes would go. pack "C" fopen "wb" fwrite // Write file as binary safe. fclose
```
"Dont Trust Tile-Count"
Throughout this tutorial notes like "dont trust tile-count" have been placed. Tile-Count cant be trusted because a bytes maximum value is 255, and Tile-sets may contain the maximum amount 65536 tiles. A way to get a correct amount of tiles is the Dividend of the File Size and The number of bytes per tile, rounded up.
PHP Example:
```
$TileCount = (filesize( )/3072); ceil "tileset.tst" // for DetailLevel=1
```
Visual Basic Example:
```
one two TileCount one = ( (app.path & "tileset.tst") / 3072) two = (two) two < one TileCount = two + 1 TileCount = two Dim as integer Dim as integer Dim as integer FileLen 'Get decimal int ' Get integer Then ' Round the decimal up when you have a decimal 'one had a decimal, round up Else 'two wasnt less than one. Dont round up. End If
```
Drawling Pixels In Visual Basic
Example:
```
Picturebox.line (x,y)-(x,y), color, Picturebox.line (x,y)-((x+1),(y+1)), color, ' Draw one pixel ' Draw 2x2 pixels.
```
Drawling Pixels In PHP
```
In PHP you create an image, draw on it, output it. In the following example, PHP creates a png image 32x32 in size, and draws a red pixel at the top-left corner.
```
PHP Example:
```
$width=32;
$height=32; ( ); $image = ($width, $height);
$bkg_color = ($image, 255, 255, 255); $r=255;
$g=0
$b=0;
$x=0;
$y=0;
$color = ($image, $r, $g, $b); ($image, $x, $y, $color); ($image); ($image); header "Content-type: image/png" // Tell browser type of file is png imagecreatetruecolor imagecolorallocate // color to var // The first time you use imagecolorallocate,
// it sets the background color to that color imagecolorallocate imagesetpixel imagepng // Put image on screen imagedestroy // Cleanup
```
Drawling your first tile in Visual Basic
Its time to draw a tile in VB! Open VB and start a new project. Add one button (named Command1) and one PictureBox (named Picture1). Then add the following code:
```
Command1_Click() TileVersion TileCount TileDetail R G B pos Long h w x y TileSize filename OffSet filename = App.Path & "\tileset.tst" OffSet = 0 filename #1 #1, 1, TileVersion #1, 5, TileDetail TileDetail = 1 TileCount = (filename) / 3072 TileSize = 32
pos = 6 + (3072 * OffSet) TileDetail = 2 TileCount = (filename) / 768 TileSize = 16
pos = 6 + (768 * OffSet) TileDetail = 1 TileDetail = 2 x = 0 (TileSize - 1) y = 0 (TileSize - 1)
pos = pos + 1 #1, pos, R pos = pos + 1 #1, pos, G pos = pos + 1 #1, pos, B TileSize = 32 Picture1.Line (x, y)-(x, y), (R, G, B), Picture1.Line ((x * 2), (y * 2))-(((x * 2) + 2), ((y * 2) + 2)), RGB(R, G, B), BF #1 Private Sub Dim Byte Dim Integer Dim Byte Dim Byte Dim Byte Dim Byte Dim Dim Integer Dim Integer Dim Integer Dim Integer Dim Integer Dim String Dim Integer ' change this to the filename of your tileset. ' This is the tile number. Starting with 0 Open For Binary As Get Get Then ' 32x32 16 mil FileLen ' Get file size (32x32) ' Add bytes to starting possition for offset End If Then ' 16x16 16 mil FileLen ' Get file size (32x32) ' Add bytes to starting possition for offset End If Then ' Next Byte Get ' Get Color Red ' Next Byte Get ' Get Color Green ' Next Byte Get ' Get Color Blue Then ' 32x32 16 mil RGB ' Draw pixel Else ' 16x16 16 mil ' Draw 2x2 pixels End If Next
Next
End If
Close End Sub
```
Drawling your first tile in PHP
Its time to draw a tile in PHP! Open Notepad. Save the file, and upload it to a PHP compatible server. Upload a tile-set along with your file. Then add the following code:
```
$file= ; $fw = ($file, ); $contents = ($fw,filesize($file));
$TileVersion = ( , ( ,$contents)); $DetailLevel = ( , ( ,$contents)); $offset=0; ($DetailLevel==1)
{
$tile_size= ;
$pixel_size= ;
$TileCount = (( ($file)-6)/$tile_size); $pos = 6+(3072*$offset);
} ($DetailLevel==2)
{
$tile_size= ;
$pixel_size= ;
$TileCount = (( ($file)-6)/$tile_size); $pos = 6+(768*$offset);
}
$tst = ( ,$contents); ($fw); ( ); $image = (32, 32); $bkg_color = ($image, 255, 255, 255); ($i=0; $i<$pixel_size; $i++)
{ ($e=0; $e<$pixel_size; $e++)
{ $pos=$pos+1;
$r = $tst[ .$pos];
$pos=$pos+1;
$g = $tst[ .$pos];
$pos=$pos+1;
$b = $tst[ .$pos]; ($r==0 && $g==1 && $b==2)
{
$color = $bkg_color } {
$color = ($image, $r, $g, $b); } ($DetailLevel==1) { ($image, ($i + (32 * $w)), ($e + (32 * $h)), $color);
} ($DetailLevel==2) { ($image, ($i*2), ($e*2), $color); ($image, (($i*2)+1), ($e*2), $color); ($image, ($i*2), (($e*2)+1), $color); ($image, (($i*2)+1), (($e*2)+1), $color);
}
}
} ($image); ($image); "tileset.tst" // change this to your tile-set fopen "rb" // Open File for binary use fread implode unpack "Cbyte" // Get TileSet version implode unpack "@4/Cbyte" // Get Detail Level // This is the tile number. Starting with 0 "3072" "32" filesize // Get Tile Count "768" "16" filesize // Get Tile Count unpack "C*byte" // Construct Bytes fclose header "Content-type: image/png" // Specify that the display output is a png file. imagecreatetruecolor //Create image imagecolorallocate // Set bkg color // Draw Pixel "byte" "byte" "byte" // Transparent color else imagecolorallocate // Get pixel color // Draw Pixel //32x32 imagesetpixel // 16x16 imagesetpixel imagesetpixel imagesetpixel imagesetpixel imagepng // Put image on screen imagedestroy // Cleanup
```
Conclusion
I hope this has helped many of you understand the tile-set format. Have fun!
PS: Next edition of this tutorial will have some c++ examples.
Credits
Thank you Pests for helping me figure out how to read binary in php.
