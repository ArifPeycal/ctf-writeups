# Execution
## Description
> Can you unlock the secrets hidden in the echoes of ancient code?

## Solution
```py
def decrypt_datapointer(index, value, xor_value, add_shift, shift_right, mult_value, add_const, target_value):
    # Reverse the comparison (value ^ xor_value + add_shift >> shift_right | value ^ xor_value * mult_value + add_const)
    for possible_value in range(256):  # Try all possible byte values (0-255)
        result = ((possible_value ^ xor_value) + add_shift >> shift_right | (possible_value ^ xor_value) * mult_value + add_const)
        if result == target_value:
            return possible_value
    return None

def decrypt(datapointer):
    decrypted_values = []
    
    conditions = [
        (1, 0x23, 7, 5, 8, 0x38, 827),
        (2, 0x34, 3, 5, 8, 0x18, 795),
        (3, 0x45, 2, 5, 8, 0x10, 40),
        (4, 0x56, 9, 5, 8, 0x48, 0x1b1),
        (5, 0x67, 4, 5, 8, 0x20, 0x1d9),
        (6, 0x78, 6, 5, 8, 0x30, 0xf8),
        (7, 0x89, 1, 5, 8, 8, 1517),
        (8, 0x9a, 3, 5, 8, 0x18, 0x58d),
        (9, 0xab, 5, 5, 8, 0x28, 0x6f6),
        (10, 0xbc, 2, 5, 8, 0x10, 0x6ee),
        (11, 0xcd, 7, 5, 8, 0x38, 0x585),
        (12, 0xde, 4, 5, 8, 0x20, 0x61e),
        (13, 0xef, 3, 5, 8, 0x18, 0x6fe),
        (14, 0xf0, 5, 5, 8, 0x28, 0x5a5),
        (15, 0x01, 2, 5, 8, 0x10, 0x2aa),
        (16, 0x12, 9, 5, 8, 0x48, 0x151),
        (17, 0x23, 4, 5, 8, 0x20, 0x2ca),
        (18, 0x34, 6, 5, 8, 0x30, 0x2ba),
        (19, 0x45, 1, 5, 8, 8, 0x1c1),
        (20, 0x56, 3, 5, 8, 0x18, 0x141),
        (21, 0x67, 5, 5, 8, 0x28, 0x2ca),
        (22, 0x78, 2, 5, 8, 0x10, 0x149),
        (23, 0x89, 7, 5, 8, 0x38, 0x61e),
        (24, 0x9a, 4, 5, 8, 0x20, 0x73f),
        (25, 0xab, 6, 5, 8, 0x30, 0x666),
        (26, 0xbc, 1, 5, 8, 8, 0x6fe),
        (27, 0xcd, 3, 5, 8, 0x18, 0x52d),
        (28, 0xde, 5, 5, 8, 0x28, 0x5bd),
        (29, 0xef, 2, 5, 8, 0x10, 0x444),
        (30, 0xf0, 7, 5, 8, 0x38, 0x4d4),
        (31, 0x01, 4, 5, 8, 0x20, 0x313),
        (32, 0x12, 6, 5, 8, 0x30, 0x2ea),
        (33, 0x23, 1, 5, 8, 8, 0x2e2),
        (34, 0x34, 3, 5, 8, 0x18, 0x2a2),
        (35, 0x45, 5, 5, 8, 0x28, 0x58),
        (36, 0x56, 2, 5, 8, 0x10, 0x129),
        (37, 0x67, 7, 5, 8, 0x38, 0xd0),
        (38, 0x78, 4, 5, 8, 0x20, 0xa8),
        (39, 0x89, 6, 5, 8, 0x30, 0x767),
        (40, 0x9a, 3, 5, 8, 0x18, 0x7bf),
        (41, 0xab, 5, 5, 8, 0x28, 1999),
        (42, 0xbc, 2, 5, 8, 0x10, 0x777),
        (43, 0xcd, 7, 5, 8, 0x38, 0x828),
        (44, 0xde, 4, 5, 8, 0x20, 0x56d),
        (45, 0xef, 6, 5, 8, 0x30, 0x484),
        (46, 0xf0, 1, 5, 8, 8, 0x41c),
        (47, 0x01, 3, 5, 8, 0x18, 0x30b),
        (48, 0x12, 5, 5, 8, 0x28, 0x129),
        (49, 0x23, 2, 5, 8, 0x10, 0xa8),
        (50, 0x34, 7, 5, 8, 0x38, 0x68),
        (51, 0x03, 5, 5, 8, 0x28, 0x1e1),
        (52, 0xbe, 3, 5, 8, 0x18, 0x515),
        (53, 0xfe, 6, 5, 8, 0x30, 0x44c)
    ]
    
    for cond in conditions:
        index, xor_value, add_shift, shift_right, mult_value, add_const, target_value = cond
        decrypted_value = decrypt_datapointer(index, datapointer[index], xor_value, add_shift, shift_right, mult_value, add_const, target_value)
        decrypted_values.append(decrypted_value)
    
    decrypted_string = ''.join(chr(value) for value in decrypted_values if value is not None)
    
    return decrypted_string

datapointer = [0] * 54  # Populate with actual encrypted values
decrypted_string = decrypt(datapointer)
print("U" + decrypted_string)

```
## Flag
```
UCTF{Pa54rgda3_R3vers3_5ymbolic_ExeCution_P0wer_2024!}
```
