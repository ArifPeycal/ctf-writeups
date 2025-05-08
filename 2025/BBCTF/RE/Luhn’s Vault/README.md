# Luhn’s Vault

> The mysterious cryptographer Luhn created a safe vault that verifies numerical inputs using a technique he knows. For years, the vault has guaranteed its secrets, now is your time to crack the secret to unlock the vault.
> 
> Author: sREe

## Solution

There are two encrypted sections were stored in the `.rdata` section of the binary:

* `0x404044`: Encrypted first part of the flag
* `0x404050`: Encrypted second part of the flag

The decryption function (`_decryptFlagPart`) applied the following operations:

1. XOR each byte with `0xAA`
2. Rotate the result 6 bits to the left (i.e., a circular bitwise shift)

```
def decrypt_flag_part(data):
    def rol(val, r_bits, max_bits=8):
        return ((val << r_bits) & 0xFF) | (val >> (max_bits - r_bits))
    
    decrypted = []
    for b in data:
        xored = b ^ 0xAA
        rotated = rol(xored, 6)
        decrypted.append(rotated)
    return bytes(decrypted)

# Encrypted flag parts
encrypted_first_part = bytes([0x9b, 0xff, 0x26, 0x93, 0xd7, 0xb7, 0x97, 0xfb, 0xd7])
encrypted_second_part = bytes([0xBF, 0xEB, 0xA3, 0xAF, 0x97, 0xA7, 0x9F, 0xEF])

# Decrypt and combine
flag_part1 = decrypt_flag_part(encrypted_first_part).decode()
flag_part2 = decrypt_flag_part(encrypted_second_part).decode()

# Output full flag
full_flag = f"bbctf{{{flag_part1}{flag_part2}}}"
print(full_flag)

```
## Flag
```
bbctf{LU#N_GOT_EPBAOCMQ}
```
