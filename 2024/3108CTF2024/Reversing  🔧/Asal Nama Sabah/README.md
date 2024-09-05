# Asal Nama Sabah
## Description
> Setiap negeri mempunyai asal nama negeri tersebut. Begitu juga dengan negeri Sabah. Sabah juga mempunyai nama asal negeri tersebut yang popular di kalangan masyarakat tempatan.

## Challenge Overview
```c
  int64_t check_flag(char* arg1)

  {
      int64_t var_38;
      __builtin_strcpy(&var_38, "5d505d591a20552e47293d325c3e3159291c");
      int64_t var_46;
      __builtin_strcpy(&var_46, "namaasalsabah");
      int32_t rax = strlen(&var_46);
      
      for (int32_t i = 0; i <= 0x24; i += 1)
          *(uint8_t*)(&var_38 + ((int64_t)i)) ^= *(uint8_t*)(&var_46 + ((int64_t)(((int64_t)i) % rax)));
      
      if (strcmp(arg1, &var_38) != 0)
          return puts("Wrong! Try again.");
      
      return printf("Correct! The flag is: %s\n", &var_38);
  }

```
### Operation:
- The hardcoded string `5d505d591a20552e47293d325c3e3159291c` is XORed with the repeated string `namaasalsabah`.
- The result is compared against the user's input.

## Solution
```py
def xor_strings(input_string, key):
    # Convert the input string from hexadecimal to bytes
    input_bytes = bytes.fromhex(input_string)
    
    # Perform the XOR operation with the repeating key
    key_length = len(key)
    output_bytes = bytearray(len(input_bytes))
    
    for i in range(len(input_bytes)):
        output_bytes[i] = input_bytes[i] ^ ord(key[i % key_length])
    return output_bytes.decode()

# Given strings
input_string = "5d505d591a20552e47293d325c3e3159291c"
key = "namaasalsabah"

# Perform the XOR operation
result = xor_strings(input_string, key)

print(f"Correct! The flag is: {result}")
```
### Explanation

- Converts the input_string from a hexadecimal string to a byte array.
- Performs an XOR operation between each byte of input_bytes and the corresponding character in the key, which repeats as necessary.
- Print the flag

## Flag
```
3108{S4B4H_S4PP4H}
```
