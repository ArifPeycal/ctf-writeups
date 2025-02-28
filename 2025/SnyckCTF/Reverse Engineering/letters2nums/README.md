
# letters2nums

> Author: @Soups71
> 
> This is Letters2Nums, a new data encryption format I came up with. Use the attached binary to figure out how to decrypt the encoded flag.

## Solution

### Decoding Steps
- Read each encoded number from encflag.txt.
- Extract the two characters:
  - char1 = (encoded_value >> 8) & 0xFF (upper 8 bits)
  - char2 = encoded_value & 0xFF (lower 8 bits)
- Reconstruct the original string.

```py
def decode_flag(file_path):
    decoded_flag = ""

    with open(file_path, "r") as f:
        for line in f:
            encoded_value = int(line.strip())  # Convert each line to an integer
            char1 = (encoded_value >> 8) & 0xFF  # Extract upper 8 bits
            char2 = encoded_value & 0xFF  # Extract lower 8 bits
            decoded_flag += chr(char1) + chr(char2)  # Convert to characters

    print("Decoded flag:", decoded_flag)

# Example usage:
decode_flag("encflag.txt")
# Decoded flag: This is a long and convoluded way to try and hide the flag:flag{3b050f5a716e51c89e9323baf3a7b73b}
```

## Flag
```
flag{3b050f5a716e51c89e9323baf3a7b73b}
```
