# Baby Rev
## Description
> I stashed the flag under a rock. Still don't get all the grumbling about "Security Through Obscurity!"

## Solution

Use `strings` on the binary file and we get base64 strings. Remove 'H' from the end of each line.

![image](https://github.com/user-attachments/assets/afcc42a8-5360-4a50-84df-0be22012fea6)

```
Y3Nhd2N0
ZntOM3Yz
cl9wcjA3
M2M3X3Mz
bnMxNzF2
M18xbmYw
cm00NzEw
bl91czFu
Z19qdXM3
XzNuYzBk
MW5nIV8j
M25jMGQx
bmdfMXNf
bjB0XzNu
Y3J5cDcx
MG4hfQ==
```

## Flag
```
csawctf{N3v3r_pr073c7_s3ns171v3_1nf0rm4710n_us1ng_jus7_3nc0d1ng!_#3nc0d1ng_1s_n0t_3ncryp710n!}
```
