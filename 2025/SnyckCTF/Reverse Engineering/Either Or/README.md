# Either Or

> Author: @Kkevsterrr
>
> Either or, but probably not both.

## Solution

We were given an ELF file, where the encrypted flag bytes are stored in local_38. Each byte is XORed with 0x42 (66 in decimal). In order to retrieve the original flag, we need to XORed the encoded flag with 0x42 again.

```c

void decode_flag(long param_1)
{
  long in_FS_OFFSET;
  uint local_3c;
  byte local_38 [40];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_38[0] = 0x24;
  local_38[1] = 0x72;
  local_38[2] = 0x75;
  local_38[3] = 0x76;
  local_38[4] = 0x26;
  local_38[5] = 0x71;
  local_38[6] = 0x7a;
  local_38[7] = 0x7b;
  local_38[8] = 0x71;
  local_38[9] = 0x70;
  local_38[10] = 0x73;
  local_38[0xb] = 0x74;
  local_38[0xc] = 0x76;
  local_38[0xd] = 0x20;
  local_38[0xe] = 0x70;
  local_38[0xf] = 0x75;
  local_38[0x10] = 0x7a;
  local_38[0x11] = 0x23;
  local_38[0x12] = 0x77;
  local_38[0x13] = 0x72;
  local_38[0x14] = 0x7a;
  local_38[0x15] = 0x26;
  local_38[0x16] = 0x24;
  local_38[0x17] = 0x73;
  local_38[0x18] = 0x73;
  local_38[0x19] = 0x20;
  local_38[0x1a] = 0x77;
  local_38[0x1b] = 0x27;
  local_38[0x1c] = 0x24;
  local_38[0x1d] = 0x24;
  local_38[0x1e] = 0x7a;
  local_38[0x1f] = 0x7b;
  for (local_3c = 0; local_3c < 0x20; local_3c = local_3c + 1) {
    *(byte *)(param_1 + (int)local_3c) = local_38[(int)local_3c] ^ 0x42;
  }
  *(undefined *)(param_1 + 0x20) = 0;
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    // WARNING: Subroutine does not return
    __stack_chk_fail();
  }
  return;
}
```

Create python script to solve.
```py
def decode_flag():
    encrypted_bytes = [
        0x24, 0x72, 0x75, 0x76, 0x26, 0x71, 0x7a, 0x7b,
        0x71, 0x70, 0x73, 0x74, 0x76, 0x20, 0x70, 0x75,
        0x7a, 0x23, 0x77, 0x72, 0x7a, 0x26, 0x24, 0x73,
        0x73, 0x20, 0x77, 0x27, 0x24, 0x24, 0x7a, 0x7b
    ]

    decoded_flag = "".join(chr(b ^ 0x42) for b in encrypted_bytes)
    print(f"Decoded Flag: flag{{{decoded_flag}}}")

decode_flag()

```
## Flag
```
flag{f074d38932164b278a508df11b5eff89}
```
