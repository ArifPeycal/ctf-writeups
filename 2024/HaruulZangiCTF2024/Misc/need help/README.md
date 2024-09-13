# need help

We were give `registration.mrf` file that contains some text strings. There are some readable strings that are related to the flag. 

![image](https://github.com/user-attachments/assets/f0ba698f-a2d9-46e7-81da-5e146cc82255)

First, we can remove whitespace and null bytes using CyberChef. 

![image](https://github.com/user-attachments/assets/72c0300d-4ce8-4251-a894-be64556eb034)

When we look at the pattern, we can see repeating `$END` and `$END2` throughout the text. Between this two `$END`, there will be some readable strings. Remove any garbage strings and you will get the flag.
## Flag
```
HZ2024{HARUUL_ZANGIIIII_2024_EASY_CHALL}
```
