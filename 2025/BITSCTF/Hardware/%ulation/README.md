# %ulation

> Shifting keys or something idk.
> 
> d4y0n3

## Solution
We were given a data file called `signal`. There is no file header so I didnt know what type of file it is. 

Looking at the challenge title, the percent sign can be interpreted as modulo, so my educated guess is that this challenge is about modulation of radio frequencies (RF). Modulation is the process of encoding information in radio communications, networking, and telecommunications to allow that data to travel long distances efficiently.

When searching for answer, I stumbled upon a tool called `Universal Radio Hacker` that is capable to analyze RF signal (https://github.com/jopohl/urh?tab=readme-ov-file). Just upload the file and copy the binaries, then convert it to text.

![image](https://github.com/user-attachments/assets/d7b819b6-296c-4bc2-a42e-1c6d565cc1fb)

```
010000100100100101010100010100110100001101010100010001100111101101000001010111110110001001110010001100010011001101100110010111110011010001101110011001000101111101100111001100110110111001110100011011000011001101011111001100010110111001110100011100100011000001100100011101010110001100110111001100010011000001101110010111110011011100110000010111110111001000110100011001000110100100110000010111110110100000110100011000110110101100110001011011100110011101011111011000110011010101100011001100110011001100110101001101010011100001111101
```
![image](https://github.com/user-attachments/assets/fc44bdfb-5d83-49b2-8c3f-27bd4c95498e)


## Flag
```
BITSCTF{A_br13f_4nd_g3ntl3_1ntr0duc710n_70_r4di0_h4ck1ng_c5c33558}
```
