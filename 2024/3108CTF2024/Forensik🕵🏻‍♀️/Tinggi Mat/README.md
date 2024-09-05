# Tinggi Mat 🕵🏻‍♀️
## Description
> Kalau kat KL je mesti ingat KLCC. Alang-alang kita cerita pasal bangunan tinggi ni. Kenal tak Warisan Merdeka Tower?


## Solution


First, unzip the `WMT.rar` file, which provides two files: `WarisanMerdekaTower.png` and `flag2.rar.`. To find the password for `flag2.rar`, we can use `exiftool` to  see the image description. We get the password as `MERDEKA118`. This password unlocks `flag2.rar`, which contains a `flag2.txt` file. 

![image](https://github.com/user-attachments/assets/5bf02320-fdef-44b8-b911-09296e90c0fa)

```
// First part
3108{th3_t4ll3st
```

Opening flag2.txt in a normal text editor shows just a description of the building. However, when opened with vim, it appears different, suggesting the use of `Unicode Steganography`.

![image](https://github.com/user-attachments/assets/c8e5f1d0-1ecf-4fa5-b86f-34c9ec10df36)


Use a <a href="https://330k.github.io/misc_tools/unicode_steganography.html">Unicode Steganography tool</a> to decode the hidden message in flag2.txt. After decoding, the second part of the flag is revealed.
```
// Second part
_0n3_1n_M4l4ys14!}
```

## Flag
```
3108{th3_t4ll3st_0n3_1n_M4l4ys14!}.
```
