# Windows of Opportunity
## Challenge Overview

We were given `windows` ELF file to reverse engineer. Decompile the file inside Ghidra and we can start analyzing `main` function.

This a simple C program that request password from user and calculate sum of `local_38[index]` and `local_38[index+1]`. Then, the sum will be compared to an array index, if it not equal then the program will break and vice versa.
```c
int main(void)

{
  char local_38 [43];
  char local_d;
  uint index;
  
  puts("A voice comes from the window... \'Password?\'");
  fgets(local_38,0x2a,stdin);
  index = 0;
  while( true ) {
    if (0x24 < index) {
      puts("The window opens to allow you passage...");
      return 0;
    }
    local_d = local_38[(int)(index + 1)] + local_38[(int)index];
    if (local_d != arr[(int)index]) break;
    index = index + 1;
  }
  puts("The window slams shut...");
  return -1;
}
```
We can see the content of array, it contains hexadecimals which are the sum of each char in flag with the char next to it. I extracted the array using ChatGPT so I can use it for my Python script.

```py
arr = [
    0x9c, 0x96, 0xbd, 0xaf, 0x93, 0xc3, 0x94, 0x60, 
    0xa2, 0xd1, 0xc2, 0xcf, 0x9c, 0xa3, 0xa6, 0x68, 
    0x94, 0xc1, 0xd7, 0xac, 0x96, 0x93, 0x93, 0xd6, 
    0xa8, 0x9f, 0xd2, 0x94, 0xa7, 0xd6, 0x8f, 0xa0, 
    0xa3, 0xa1, 0xa3, 0x56, 0x9e
]
```
## Solution
This Python script starts with the first character of the flag (`H`), then derives subsequent characters using the difference between values in `sums` and the previous character's ASCII value.
```py
sums = [
    0x9c, 0x96, 0xbd, 0xaf, 0x93, 0xc3, 0x94, 0x60, 
    0xa2, 0xd1, 0xc2, 0xcf, 0x9c, 0xa3, 0xa6, 0x68, 
    0x94, 0xc1, 0xd7, 0xac, 0x96, 0x93, 0x93, 0xd6, 
    0xa8, 0x9f, 0xd2, 0x94, 0xa7, 0xd6, 0x8f, 0xa0, 
    0xa3, 0xa1, 0xa3, 0x56, 0x9e
]

flag = [ord('H')]

for i in range(len(sums)):
    next_char = sums[i] - flag[-1]
    flag.append(next_char)

flag_string = ''.join([chr(c) for c in flag])
print("Decrypted flag:", flag_string)
```
## Flag
```
HTB{4_d00r_cl0s35_bu7_4_w1nd0w_0p3n5!}
```
