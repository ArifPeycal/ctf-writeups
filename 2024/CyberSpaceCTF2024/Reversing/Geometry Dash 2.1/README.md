# Geometry Dash 2.1
## Description
> I would give you the flag but I can't let go (haha get it). use GDBrowser for the last step btw.
> 
> Note: You do NOT need Geometry Dash purchased to solve this challenge.

## Challenge Overview
We received a `CCLocalLevels.dat` file. 
> CCLocalLevels.dat is a file associated with the game Geometry Dash, a popular rhythm-based platformer game. This file is typically found in the game's save directory and contains information about locally saved levels that players have created or downloaded.

## Solution
In order to analyze the file, we need to decrypt it first. You can use Python script in this <a href="https://gist.github.com/FaltoGH/b7563b425e10de41c56bf7af0dc4c864">Github page</a> to decrypt it into XML code.
```py
python3 gdcrypt.py CCLocalLevels.dat
```
You will receive a.txt as output, containing the XML code for the saved data file. For better readability, we can use XML viewer to see the code structure. We can see several base64 string.
```
ZmxhZyBpcyBpbiB0aGUgbGV2ZWwgc29tZXdoZXJl → flag is in the level somewhere
dGhlIHRleHQgYmVsb3cgY29uc2lzdHMgb2YgbXVsdGlwbGUgdGV4dCBvYmplY3Rz → the text below consists of multiple text objects
c3RvcCBwbGF5aW5nIHRoZSBnYW1lIQ== → stop playing the game!
```
We also get a string that is similar to the flag format without the curly braces, `CSCTFa52de5`. The description also stated that <a href="https://gdbrowser.com/search">GDBrowser</a> must be used for the last step. GDBrowser is a website that allows us to search for Geometry Dash related such as Users and Levels. Bybusing the website search engine, we know that `CSCTFa52de5` is a user. The flag is located at the user's comment.

![image](https://github.com/user-attachments/assets/c3f5d5ec-4703-42a0-89a3-dcf08fe6503a)

## Flag 
```
CSCTF{geometry_dash_d0895c120d671b}
```
