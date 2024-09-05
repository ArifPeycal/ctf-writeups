# Tanpa Nama 3
## Description
> ![image](https://github.com/user-attachments/assets/ea3f9085-b195-44aa-83cd-5bc1bea55ad6)
## Challenge Overview

## Solution
```py
def xor_with_binary(binary_str, xor_str):
    binaries = binary_str.split()  # Split the binary string into individual binary numbers
    xor_num = int(xor_str, 2)  # Convert the XOR string to a decimal number
    xor_results = []
    
    for b in binaries:
        num = int(b, 2)  # Convert each binary number to a decimal number
        result_num = num ^ xor_num  # XOR operation with the XOR number
        xor_results.append(format(result_num, '08b'))  # Convert the result back to an 8-bit binary string
    
    return ' '.join(xor_results)  # Join all binary strings into a single string

def binary_to_text(binary_str):
    # Split the binary string into 8-bit segments
    binary_segments = binary_str.split()
    # Convert each binary segment to a decimal number and then to a character
    text = ''.join(chr(int(b, 2)) for b in binary_segments)
    return text

# Provided binary string and XOR string
binary_str = "01010110 01010100 01010101 01011101 00011110 00110110 01010100 00101000 00110101 00101001 01010110 00111010 00100110 00110111 00110101 00111100 00110001 01010101 00111010 00100110 00101101 00100100 00101001 00101001 00100000 00101011 00100010 00100000 00011000"
xor_str = "01100101"

# Decrypt the binary string
decrypted_binary = xor_with_binary(binary_str, xor_str)

# Convert the binary string to text
text_result = binary_to_text(decrypted_binary)
print(text_result)
```
### Solution Steps

1. XOR Decryption
   
To decrypt the binary string, you need to apply the XOR operation with the provided XOR string to each 8-bit segment of the binary string. The XOR operation is applied between each 8-bit binary number and the XOR string.

2. Convert Binary to Text

After obtaining the decrypted binary string, convert it into readable text by converting each 8-bit binary segment into its ASCII character equivalent.

## Flag
```
3108{S1MPL3_CRPYT0_CHALLENGE}
```
