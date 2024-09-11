# Headache

## Description
> Created by: Sl4y3r_07 <br>
> I’ve had a headache since last evening. Is there a magic spell that can cure it immediately?

We start with a seemingly ‘corrupt’ file, chal.png which doesn’t open. Files have ‘signatures’ (magic numbers). PNGs magic numbers are 89 50 4e 47 0d 0a 1a 0a. This does not match our files magic numbers (ae 71 00 ff 3d 62 24 6d)

We are using <a href="https://github.com/sherlly/PCRT">PCRT</a> to automate the fix of corrupt file header. 
![image](https://github.com/user-attachments/assets/63df1859-d565-4ce4-b599-19732dae0ac2)

## Flag
```flag{sp3ll_15_89_50_4E_47}```
