# Komik
> Dalam ni ada Flag, tinggal copy paste dan ____ je.
>
> https://www.dcode.fr/

## Solution
 At first glance, the text looks innocent, but further check in the hex editor, I noticed that there is pattern of hex bytes `e2 80 8b`	which is ZERO WIDTH SPACE. A kind of Unicode that famous for steganography.
 
<img width="676" height="551" alt="image" src="https://github.com/user-attachments/assets/07bf2efa-606e-47f1-a9d2-5bd500710f43" />

Use this tool to decode, https://330k.github.io/misc_tools/unicode_steganography.html

## Flag
```
3108{e1sner_r1c3_b00k}
```
