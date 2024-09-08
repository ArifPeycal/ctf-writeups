# Sergio
## Description
> In the heart of Tehran, a cunning spy organization has been using a flawed implementation of RSA to secure its secret communications. Sergio, an ace cryptographer, has intercepted an encrypted message, but only has the public key to work with. Can you assist Sergio in decrypting the message and uncovering the hidden secrets?
>
> Reminder: Remember to submit the flag in this format: UCTF{flag}

## Challenge Overview

We were given text files containing encrypted text, `c` exponent, `e` and public key, `n`.

```
c = 70886407371304490355797613974913658205
e = 65537
n = 139551725550533062709001988886045836849
```
## Solution
Since `c` and `n` is quiet small, I tried to use RSA Calculator from code. 

![image](https://github.com/user-attachments/assets/3c2cc374-166e-4c48-8081-e3915338c0cd)

We get the private key, `d` and we can complete the decryption. 

![image](https://github.com/user-attachments/assets/797241ab-767a-46dc-a46d-2b435d4e54c7)

## Flag
```
UCTF{b4b4k_fort}
```
