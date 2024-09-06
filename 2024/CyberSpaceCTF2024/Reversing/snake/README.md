# snake
## Description
> Can you slither to the win?

## Challenge Description
We were given an ELF file which is a CLI snake game. Every time we eat an apple, we get 10 points. But, we need exactly 16525 points in order to get the flag.

![image](https://github.com/user-attachments/assets/38307ab4-2d13-4f0b-bfaa-6cc659c21ca1)

## Solution

We can use program such as Cheat Engine to change the value of score in memory. There are several alternatives, one of it is PINCE.
https://github.com/korcankaraokcu/PINCE?tab=readme-ov-file

In order to change score value, we need to attach snake program into PINCE. Search for value 0 in the first scan, you can pause using SPACEBAR to avoid your snake from dying. 

Eat an apple to increase the score into 10 points. Then, search for value 10 in the next scan.

![image](https://github.com/user-attachments/assets/c4831e25-7e32-4eec-ac8b-01e5df0dc107)

Change the value into 16525.

![image](https://github.com/user-attachments/assets/137d1d85-be10-4507-bdea-ea0d505bf552)

![image](https://github.com/user-attachments/assets/97805c25-a777-46aa-9480-e6f337f4eceb)

## Flag
```
CSCTF{Y0u_b34T_My_Sl1th3r_G4m3!}
```
