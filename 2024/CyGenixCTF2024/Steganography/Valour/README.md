# Valour
## Description
> Brave men rejoice in adversity, just as brave soldiers triumph in war. Remember, bravery is not just merely the absence of fear, its the capacity to perform properly even when half scared to death.

## Solution
- Run binwalk on ```courage.png, extract all files```
![image](https://github.com/user-attachments/assets/8322da8d-21b7-4633-9994-90295289d70d)
- ```hidden.zip``` is password-locked, use ```zip2john``` to crack the zip files
```bash
zip2john hidden.zip > zip.hash
```
```bash
john --wordlist=/usr/share/wordlists/rockyou.txt zip.hash
```
- Get the password and unlock the zip file
## Flag
```CyGenixCTF{J0hn_7h3_b1N4ry-W4lK1n6_z1Pp3R!!}```
