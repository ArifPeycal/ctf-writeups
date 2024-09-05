# key
## Description
> GDB is cool! Ghidra or IDA is helpful

## Challenge Overview
The description gives us a hint that we need to decompile the `key` file. You can use Ghidra, Binary Ninja or IDA Pro but because of the small size, I prefer to use online tool such as <a href="https://dogbolt.org/">DogBolt</a>.
```c
#include "out.h"

undefined8 main(void)

{ 
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_b8[0] = 0x43;
  local_b8[1] = 0xa4;
  local_b8[2] = 0x41;
  local_b8[3] = 0xae;
  local_a8 = 0x42;
  local_a4 = 0xfc;
  local_a0 = 0x73;
  local_9c = 0xb0;
  local_98 = 0x6f;
  local_94 = 0x72;
  local_90 = 0x5e;
  local_8c = 0xa8;
  local_88 = 0x65;
  local_84 = 0xf2;
  local_80 = 0x51;
  local_7c = 0xce;
  local_78 = 0x20;
  local_74 = 0xbc;
  local_70 = 0x60;
  local_6c = 0xa4;
  local_68 = 0x6d;
  local_64 = 0x46;
  local_60 = 0x21;
  local_5c = 0x40;
  local_58 = 0x20;
  local_54 = 0x5a;
  local_50 = 0x2c;
  local_4c = 0x52;
  local_48 = 0x2d;
  local_44 = 0x5e;
  local_40 = 0x2d;
  local_3c = 0xc4;
  printf("Enter the key: ");
  __isoc99_scanf(&DAT_00102014,local_38);
  sVar1 = strlen(local_38);
  if ((int)sVar1 == 0x20) {
    for (local_140 = 0;
        ((int)local_140 < 0x20 &&
        (aiStack_138[(int)local_140] =
              ((int)local_38[(int)local_140] ^ local_140) * ((int)local_140 % 2 + 1),
        aiStack_138[(int)local_140] == local_b8[(int)local_140])); local_140 = local_140 + 1) {
      if (local_140 == 0x1f) {
        printf("Success!");
      }
    }
  }
  else {
    printf("Denied Access");
  }
```
### Explanation
- It checks if the length of the user input is 32 characters (0x20).
- If the input length is correct, the program enters a loop where each character of the input is XORed with its index (local_140)
    - the index is even =  multiplied by  1
    - the index is odd = multiplied by 2 
- The result is then compared against the corresponding value in local_b8.
## Solution
To find the correct key, we need to reverse the XOR operation for each character. The operation performed on each character depends on whether its index is even or odd:

- Even Index: The character is XORed with its index.
- Odd Index: The character is XORed with its index and then multiplied by 2.
```py
# Known values from the challenge (converted to decimal)
local_b8 = [
    67, 164, 65, 174, 66, 252, 115, 176, 111, 114, 94, 168,
    101, 242, 81, 206, 32, 188, 96, 164, 109, 70, 33, 64,
    32, 90, 44, 82, 45, 94, 45, 196
]

key = []

for i in range(32):
    value = local_b8[i]
    if i % 2 == 0:
        # If index is even
        original_char = (value // 1) ^ i
    else:
        # If index is odd
        original_char = (value // 2) ^ i
    key.append(chr(original_char))

print("".join(key))
```

## Flag
```
CSCTF{u_g0T_it_h0OrAy6778462123}
```
