# Cheat Code
## Description
> Created by: it4ch1 <br>
> Enough of Cheat Codesss , this is no GTA SA where you can win using Cheats.Let’s see if you can win without it……

The provided C code has two interesting functions: ```main``` and ```fun_1```. The main purpose of this program is to validate a "cheat code" input by the user. 

## Summary of the Code
1. Main Function:

- The main function initializes a set of values (stored in variables like local_b8, local_b4, etc.).
- It prompts the user to enter a "cheat code" using fgets.
- The input is then passed to the ```fun_1``` function along with the initialized values.
- If ```fun_1``` returns 0, the program exits with a failure message. If it returns 1, the program prints a success message.

2. fun_1 Function:

- This function performs two key checks on the user input:
- Length Check: The input length must be 32 characters (0x20 bytes).
- Validation Check: The input undergoes two validation checks:
    - First Validation: It compares the XOR of characters at mirrored positions in the input with the corresponding value from the initialized variables.
    - Second Validation: It checks if the first 16 characters match a specific string stored in local_28 and local_20.

## Approach to Solve the Challenge
1. Start with the Known Prefix:
- The first 16 characters of the input should be: flag{c4n_t_HESOY}.
2. Determine the Remaining 16 Characters:
- The remaining 16 characters need to pass the XOR check against the predefined values in local_b8 to local_7c.
3. Brute-force or Analyze the XOR Operation:
- Since the XOR operation depends on mirrored positions, the last 16 characters can be deduced based on the first 16 characters and the corresponding values in the initialized variables.

```python
# Known part of the flag
prefix = "flag{c4n't_HESOY"

# Values from local_b8 to local_7c in decimal
values = [
    27, 25, 81, 30, 36, 13, 0, 13,
    120, 65, 110, 32, 114, 12, 2, 24
]

# Calculate the remaining 16 characters
suffix = ""
for i in range(16):
    suffix += chr(values[i] ^ ord(prefix[i]))
    c = ''.join(x for x in suffix)
# Combine the prefix and suffix to get the full cheat code
print(prefix+c[::-1])
```

## Flag 
```flag{c4n't_HESOYAM_7h15_c4n_y0u}```
