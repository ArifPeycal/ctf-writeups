# Tampered
## Description
> Our MAPNA flags repository was compromised, with attackers introducing one invalid flag. Can you identify the counterfeit flag? Note: Forgot the flag format in the rules pages, just find the tampered one. You are not allowed to brute-force the flag in scoreboard, this will result in your team being blocked.
## Challenge Overview
We were given text files contains many flag-formatted strings. We need to find the outlier among the flags. 
## Solution
The script reads the entire content of the file as bytes and splits the content by `\r\r\n`.  Any strings that didnt have 47 chars, then it is an outlier.
```py
with open('flags.txt','rb+') as f:
    d=f.read().split(b'\r\r\n')
    for x in d:
        if x != b'':
            if len(x) != 47:
                print(x)
```
The flag contains `\r\n\r`  instead of `\r\r\n` and have 49 chars.
```
b'MAPNA{Tx,D51otN\\eUf7qQ7>ToSYQ\\;5P6jTIHH#6TL+uv}\r\n\rMAPNA{R6Z@//\\>caZ%%k)=ci3$IyOkSGK%w<"V7kgesY&k}'
```
## Flag
```
MAPNA{Tx,D51otN\\eUf7qQ7>ToSYQ\\;5P6jTIHH#6TL+uv}
```
