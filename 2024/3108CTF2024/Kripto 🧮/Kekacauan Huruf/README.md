# Kekacauan Huruf
## Description
> Balikkan proses penyulitan untuk mendedahkan bendera tersembunyi. Bolehkah anda menyahkod bendera dan menyelesaikan teka-teki? ~By GoogleTranslate :)

## Challenge Overview

The code is essentially encrypting the flag by:
1. Padding it with random data. A random padding length between 5 and 10 bytes is chosen.
2. Converting it into a base-64-like sequence.
3. Shuffling the sequence randomly.
4. Adding a random offset to each element between 1 and 64.
5. The encrypted data and the information needed to reverse the encryption are saved to ```secret_key.txt```.
## Solution

```py
from Crypto.Util.number import bytes_to_long, long_to_bytes
q = 64
offset = 50
padding_length = 9
original_order = [9, 20, 6, 12, 22, 38, 14, 24, 53, 52, 61, 29, 45, 11, 57, 44, 8, 46, 55, 59, 31, 2, 51, 43, 21, 27, 17, 40, 15, 58, 0, 26, 19, 36, 60, 28, 48, 39, 34, 50, 7, 16, 56, 30, 10, 49, 13, 3, 5, 42, 41, 47, 37, 4, 32, 33, 62, 1, 18, 23, 25, 35, 54]
shuffled_secret_key = [54, 38, 12, 47, 37, 37, 53, 22, 6, 38, 62, 22, 10, 54, 19, 41, 43, 53, 0, 62, 63, 28, 63, 63, 22, 10, 7, 37, 63, 53, 44, 8, 10, 42, 35, 43, 42, 63, 37, 21, 4, 19, 45, 21, 19, 18, 3, 62, 53, 24, 2, 62, 18, 35, 41, 14, 53, 3, 37, 63, 55, 62, 5]

# Reverse the offset addition
original_secret_key = [(x - offset) % q for x in shuffled_secret_key]

# Reverse the shuffling
secret_key = [0] * len(original_secret_key)
for i, pos in enumerate(original_order):
    secret_key[pos] = original_secret_key[i]

# Convert the secret key back to an integer
flag_int = 0
for value in reversed(secret_key):
    flag_int = (flag_int * q) + value

# Remove padding
padding_bits = padding_length * 8
flag_int >>= padding_bits

# Convert back to bytes
flag = long_to_bytes(flag_int)
print("Flag:", flag.decode())

```
To decrypt the flag, you'll need to reverse the operations applied during encryption: 

1. **Reverse the Offset Addition:** Subtract the offset from each element in the shuffled secret key and take modulo q to get back to the original key values.

2. **Reverse the Shuffle:** Use the original_order list to reverse the shuffling process and get back the original secret key.

3. **Reverse Padding:** The flag was padded with bits, so you'll need to remove the padding to retrieve the original flag. 
## Flag
```
3108{9546880676d3788377699aad794c5a44}
```
