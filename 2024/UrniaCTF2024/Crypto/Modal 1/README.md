# Modal 1
## Description
> Mathematical operations can hide more than they reveal. Can you decrypt the secret hidden within these numbers? Pay attention to the sequence, and you may find that the answer lies in simplicity.

 ## Challenge Overview
 We were given `challenge.py` that contains the encryption script and `output.txt` that contains the output.
```py
from secret import flag

size = len(flag)
for i in range(size-1):
    print(ord(flag[i]) + ord(flag[i+1]), end=",")
```
```
216,215,218,225,206,187,153,163,166,174,217,167,169,199,153,173,227,156,155,199,203,156,96,155,222,210,207,163,148,196,200,171,187,225,233,
```

The code iterates over the flag string, computes the sum of the ASCII values of each pair of consecutive characters, and prints these sums separated by commas.

## Solution
We'll make an educated guess for the first character of the flag, which might be u for "uctf{...}".
Using that, we can deduce the second character by subtracting the ASCII value of the first character from the first sum, and so on.

```py
sums = [216, 215, 218, 225, 206, 187, 153, 163, 166, 174, 217, 167, 169, 199, 153, 173, 
        227, 156, 155, 199, 203, 156, 96, 155, 222, 210, 207, 163, 148, 196, 200, 171, 
        187, 225, 233]

flag = [ord('u')]

# Now calculate the rest of the flag based on the sums
for i in range(len(sums)):
    next_char = sums[i] - flag[-1]
    flag.append(next_char)

# Convert ASCII values back to characters to get the flag string
flag_string = ''.join([chr(c) for c in flag])
print("Decrypted flag:", flag_string)
# Decrypted flag: uctf{Sh1r4z_Haf3zi3h_l00ks_p3aceFul}
```

## Flag
```
uctf{Sh1r4z_Haf3zi3h_l00ks_p3aceFul}
```
