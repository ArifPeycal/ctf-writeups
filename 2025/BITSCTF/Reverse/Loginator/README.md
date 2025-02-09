# Loginator

> Dr. Doofenshmirtz has invented a Loginator, which as usual doesn't work as intended. He has a concept of a plan to assert his rule over the Tristate Area. He simply cannot afford to get stopped by Agent Perry this time.
> 
> 02 92 a8 06 77 a8 32 3f 15 68 c9 77 de 86 99 7d 08 60 8e 64 77 be ba 74 26 96 e7 4e
> 
> Author: !llusion545

## Solution

The given C code obfuscates an input string by applying a sequence of transformations to each character in a cyclic manner. 

### **Step 1: Memory Allocation and Initialization**
The function allocates three key arrays used in the obfuscation:
- `local_28 = [0x57, 0x21, 0x43, 0x99]` → Used in XOR transformation.
- `local_20 = [0xAA, 0xBB, 0xCC, 0xDD]` → Used in bitwise NOT-XOR transformation.
- `local_18 = [1, 3, 5, 7]` → Used in bitwise rotation.

A counter `local_54` cycles through four stages (0 to 3), determining which transformation is applied to each character in the input string.

### **Step 2: Obfuscation Functions**
The obfuscation process follows a four-step cycle:

1. **`FUN_001011a9` (Stage 0):**
   - Transforms `byte = (byte + 0x13) ^ key` where `key` is taken from `local_28`.

2. **`FUN_001011f7` (Stage 1):**
   - Multiplies the byte by 2.

3. **`FUN_00101208` (Stage 2):**
   - Applies a bitwise rotation:
     - `byte = (byte >> (8 - key)) | (byte << key)`
     - `key` is taken from `local_18`.

4. **`FUN_0010126e` (Stage 3):**
   - Applies a NOT-XOR operation:
     - `byte = ~(byte ^ key)` where `key` is taken from `local_20`.

After obfuscating each byte, the process repeats for the next byte.

### **Step 3: Reversing the Obfuscation**
To retrieve the original string, we must reverse each transformation in the correct order:

1. **Reverse `FUN_0010126e`**:
   - `original_byte = (~obf_byte) ^ key`

2. **Reverse `FUN_00101208`**:
   - `original_byte = ((obf_byte << (8 - key)) & 0xFF) | (obf_byte >> key)`

3. **Reverse `FUN_001011f7`**:
   - `original_byte = obf_byte / 2` (assuming the obfuscated value was even)

4. **Reverse `FUN_001011a9`**:
   - `original_byte = (obf_byte - 0x13) ^ key`

Below is the Python script to reverse the obfuscation:

```python
# Reverse Functions
def reverse_fun_0010126e(obf_byte, key, index):
    return (~obf_byte & 0xFF) ^ key[index]

def reverse_fun_00101208(obf_byte, key, index):
    shift = key[index]
    return ((obf_byte << (8 - shift)) & 0xFF) | (obf_byte >> shift)

def reverse_fun_001011a9(obf_byte, key, index):
    return (obf_byte ^ key[index]) - 0x13 & 0xFF

def reverse_fun_001011f7(obf_byte):
    return obf_byte // 2  # Assuming even values

def reverse_obfuscation(obfuscated_bytes):
    key1 = [0x57, 0x21, 0x43, 0x99]
    key2 = [0xAA, 0xBB, 0xCC, 0xDD]
    key3 = [1, 3, 5, 7]

    original_bytes = bytearray()
    cycle = 0
    index1, index2, index3 = 0, 0, 0

    for obf_byte in obfuscated_bytes:
        if cycle == 0:
            original_byte = reverse_fun_001011a9(obf_byte, key1, index1)
            index1 = (index1 + 1) % 4
        elif cycle == 1:
            original_byte = reverse_fun_001011f7(obf_byte)
        elif cycle == 2:
            original_byte = reverse_fun_00101208(obf_byte, key3, index3)
            index3 = (index3 + 1) % 4
        elif cycle == 3:
            original_byte = reverse_fun_0010126e(obf_byte, key2, index2)
            index2 = (index2 + 1) % 4
        
        original_bytes.append(original_byte)
        cycle = (cycle + 1) % 4

    return original_bytes.decode("utf-8", errors="ignore")

# Given obfuscated hex string
obfuscated_hex = "02 92 a8 06 77 a8 32 3f 15 68 c9 77 de 86 99 7d 08 60 8e 64 77 be ba 74 26 96 e7 4e"
obfuscated_bytes = bytes.fromhex(obfuscated_hex)

# Reverse the obfuscation
original_string = reverse_obfuscation(obfuscated_bytes)
print("Original String:", original_string)
```
## Flag
```
BITSCTF{C4ND4C3_L0G1C_W0RK?}
```
