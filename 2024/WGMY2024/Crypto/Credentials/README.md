# Credentials
## Description
> We found a leak of a blackmarket website's login credentials. Can you find the password of the user osman and successfully decrypt it?
> 
> Author: Alhfs
> 
> View Hint
> The first user in user.txt corresponds to the first password in passwords.txt

## Solution

We were give 2 txt files, `user.txt` and `passwd.txt`. I tried to make educated guess that each line of user relate to each line of password (before the hint came).

So I search for `osman` and which line it is. Osman is in line 337.

```
findstr /n /i "osman" user.txt
337:osman
```

Now, we need to search password in line 337. 
```
for /f "skip=336 tokens=* delims=" %a in (passwd.txt) do @echo %a & goto :done
ZJPB{e6g180g9f302g8d8gddg1i2174d0e212}
mRuTNPuN3xNvyPb4XQqqXcteN4d6ba9953fgd
2d4fe01bfd9e5c4e939183d2381bda91c3cfv
3d3d5ea17550b31144995138200bc3cfd796b
847267c9e28e869518d0fdebc26259fe6901l
```
Line 337 is `ZJPB{e6g180g9f302g8d8gddg1i2174d0e212}` which looks like it have been encrypted using ROT. We can use ROT Bruteforce in Cyberchef to get the flag.

![image](https://github.com/user-attachments/assets/aad9d8d3-b16c-4d67-888b-c6ef389f09ed)

## Flag
```
WGMY{b6d180d9c302d8a8daad1f2174a0b212}
```
