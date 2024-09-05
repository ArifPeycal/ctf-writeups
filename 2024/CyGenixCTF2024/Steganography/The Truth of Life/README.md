# The Truth of Life
## Description
> I've left you a message and another file. Find out what truly lies within and you shall get your answer...

## Solution
- We get two files, ```message.txt``` and ```challenge.wav```.
- At first, I taught this is spectogram challenge but there is no hidden string in the spectral wave.
- Open message.txt in nano and we see a lot of whitespace, hinting  to stegsnow
> This utility can conceal messages in ASCII text by appending whitespaces to the end of lines. Because spaces and tabs are generally not visible in text viewers, the message is  effectively hidden from casual observers. And if the built-in encryption is used, the message cannot be read even if it is detected.
```
stegsnow -C  message.txt
Noice! Here is a secret: theinfinityblue!
```
- Open ```challenge.wav``` in DeepSound and use ```theinfinityblue``` as password.
- Extract flag.txt

## Flag
```CyGenixCTF{Th3_d33p_50Und_4Nd_wh1t3_n01s3_0f_St3g0}```
