# Modal 2
## Description
> The path to uncovering the secret is tangled in numbers—only the sharpest minds will find clarity.

## Challenge Overview
We were given `challenge.py` and `output.txt`.
```py
from secret import flag

p = 4066351909

for f in flag:
    print((ord(f)*2022684581 - 127389238) % p, end=",")
```
```
678296017,867140740,2721963345,2868842574,615347776,1035002716,2847859827,1391709415,2784911586,636330523,909106234,2763928839,1223847439,699278764,1223847439,2742946092,825175246,3393411249,2889825321,3393411249,1370726668,594365029,
```
The code iterates over each character in the flag string. It multiplies the ASCII value by `2022684581`, subtracts `127389238`, and then computes the result modulo `4066351909`. Then, it prints the results separated by commas.

## Solution
```py
encrypted_values = [678296017,867140740,2721963345,2868842574,615347776,1035002716,2847859827,1391709415,
                    2784911586,636330523,909106234,2763928839,1223847439,699278764,1223847439,2742946092,
                    825175246,3393411249,2889825321,3393411249,1370726668,594365029]

p = 4066351909
multiplier = 2022684581
offset = 127389238

def decrypt(encrypted_value):
    # First, we undo the modulo operation by trying different values.
    for candidate_ord in range(256): 
        if (candidate_ord * multiplier - offset) % p == encrypted_value:
            return chr(candidate_ord)
    return '?'  # If no valid ASCII character is found

decrypted_flag = ''.join([decrypt(value) for value in encrypted_values])
print(decrypted_flag)
# uctf{Sh1ny_pAsArg4d43}
```
Basically we are trying to brute force each character in the flag. For each possible ASCII value (`candidate_ord` from 0 to 255), it checks if `(candidate_ord * multiplier - offset) % p` matches the `encrypted_value`.
If a match is found, it returns the corresponding character `(chr(candidate_ord))`.
If no match is found, it returns '`?`'.

## Flag
```
uctf{Sh1ny_pAsArg4d43}
```
