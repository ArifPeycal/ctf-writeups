# HexHex
## Description
> Hexhex , Yes that's it! hehe

## Challenge Overview
We were give a text file contains hex strings. We can copy and pasting the text into CyberChef to convert the strings from Hex to readable content.

![image](https://github.com/user-attachments/assets/ec3b31e2-11c3-47ef-a6bb-d161e8de2b39)

Unfortunately, we cant find `csawctf{` inside the decrypted text. 

## Solution
Upon further inspection, we can see some strange strings that are not readable even after decryption. 
![image](https://github.com/user-attachments/assets/e1a0d857-99d6-4a7c-8b4c-d4b021c9ab74)
![image](https://github.com/user-attachments/assets/a5da70ea-35bb-40d9-81d3-10b4f4c6d240)

Search for the hex string in the original text file. We found these two strings are responsible for the unreadable strings.

```
50z4vr5105975dx6j75335fb4qf1gs1r35gu5u169r5dx5dx6w0
58s4vb6sm4vf55r58s4vb4q05605605605605605606w0 
```
I tried to use <a href="https://www.dcode.fr/cipher-identifier">dcode Cipher Identifier</a> and the cipher identified is `Twin Hex Cipher`. The results after decryption are:

```
csawctf{hex3d_i7_w3l7_innit_hehe} 
flag{fake_flag_heheheheheheh} 
```

## Flag
```
csawctf{hex3d_i7_w3l7_innit_hehe} 
```
