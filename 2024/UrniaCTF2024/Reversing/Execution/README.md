# Execution
## Description
> Can you unlock the secrets hidden in the echoes of ancient code?

## Challenge Overview

This code appears to be part of a function that validates whether an input contains a specific sequence of byte values. 

Each byte of datapointer is processed by:

- XOR operation: The byte is XORed with a constant (e.g., *flag ^ 18).
- Arithmetic and shifting: The result of the XOR is added to a constant, right-shifted by 5 bits, and combined with other operations such as multiplying by 8 and adding constants.
- Comparison: The final result of these operations is compared to predefined constants.

```c++

undefined8 FUN_140001110(int param_1,longlong param_2)

{
  longlong *outputpointer;
  byte *flag;
  
  if (param_1 != 2) {
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  flag = *(byte **)(param_2 + 8);
  if (((((((((((*flag ^ 18) + 5 >> 5 | (*flag ^ 18) * 8 + 40) == 610) &&
            (((flag[1] ^ 0x23) + 7 >> 5 | (flag[1] ^ 0x23) * 8 + 0x38) == 827)) &&
           (((flag[2] ^ 0x34) + 3 >> 5 | (flag[2] ^ 0x34) * 8 + 0x18) == 795)) &&
          ((((flag[3] ^ 0x45) + 2 >> 5 | (flag[3] ^ 0x45) * 8 + 0x10) == 40 &&
           (((flag[4] ^ 0x56) + 9 >> 5 | (flag[4] ^ 0x56) * 8 + 0x48) == 0x1b1)))) &&
         (((flag[5] ^ 0x67) + 4 >> 5 | (flag[5] ^ 0x67) * 8 + 0x20) == 0x1d9)) &&
        (((((flag[6] ^ 0x78) + 6 >> 5 | (flag[6] ^ 0x78) * 8 + 0x30) == 0xf8 &&
          (((flag[7] ^ 0x89) + 1 >> 5 | (flag[7] ^ 0x89) * 8 + 8) == 1517)) &&
         ((((flag[8] ^ 0x9a) + 3 >> 5 | (flag[8] ^ 0x9a) * 8 + 0x18) == 0x58d &&
          (((((flag[9] ^ 0xab) + 5 >> 5 | (flag[9] ^ 0xab) * 8 + 0x28) == 0x6f6 &&
            (((flag[10] ^ 0xbc) + 2 >> 5 | (flag[10] ^ 0xbc) * 8 + 0x10) == 0x6ee)) &&
           (((flag[11] ^ 0xcd) + 7 >> 5 | (flag[11] ^ 0xcd) * 8 + 0x38) == 0x585)))))))) &&
       (((((((flag[12] ^ 0xde) + 4 >> 5 | (flag[12] ^ 0xde) * 8 + 0x20) == 0x61e &&
           (((flag[13] ^ 0xef) + 3 >> 5 | (flag[13] ^ 0xef) * 8 + 0x18) == 0x6fe)) &&
          ((((flag[14] ^ 240) + 5 >> 5 | (flag[14] ^ 240) * 8 + 0x28) == 0x5a5 &&
           (((((flag[15] ^ 1) + 2 >> 5 | (flag[15] ^ 1) * 8 + 0x10) == 0x2aa &&
             (((flag[16] ^ 0x12) + 9 >> 5 | (flag[16] ^ 0x12) * 8 + 0x48) == 0x151)) &&
            ((((flag[17] ^ 0x23) + 4 >> 5 | (flag[17] ^ 0x23) * 8 + 0x20) == 0x2ca &&
             (((((flag[18] ^ 0x34) + 6 >> 5 | (flag[18] ^ 0x34) * 8 + 0x30) == 0x2ba &&
               (((flag[19] ^ 0x45) + 1 >> 5 | (flag[19] ^ 0x45) * 8 + 8) == 0x1c1)) &&
              (((flag[20] ^ 0x56) + 3 >> 5 | (flag[20] ^ 0x56) * 8 + 0x18) == 0x141)))))))))) &&
         ((((flag[21] ^ 0x67) + 5 >> 5 | (flag[21] ^ 0x67) * 8 + 0x28) == 0x2ca &&
          (((flag[0x16] ^ 0x78) + 2 >> 5 | (flag[0x16] ^ 0x78) * 8 + 0x10) == 0x149)))) &&
        (((flag[23] ^ 0x89) + 7 >> 5 | (flag[23] ^ 0x89) * 8 + 0x38) == 0x61e)))) &&
      (((((((flag[24] ^ 0x9a) + 4 >> 5 | (flag[24] ^ 0x9a) * 8 + 0x20) == 0x73f &&
          (((flag[25] ^ 0xab) + 6 >> 5 | (flag[25] ^ 0xab) * 8 + 0x30) == 0x666)) &&
         ((((flag[26] ^ 0xbc) + 1 >> 5 | (flag[26] ^ 0xbc) * 8 + 8) == 0x6fe &&
          ((((((flag[0x1b] ^ 0xcd) + 3 >> 5 | (flag[0x1b] ^ 0xcd) * 8 + 0x18) == 0x52d &&
             (((flag[0x1c] ^ 0xde) + 5 >> 5 | (flag[0x1c] ^ 0xde) * 8 + 0x28) == 0x5bd)) &&
            (((flag[0x1d] ^ 0xef) + 2 >> 5 | (flag[0x1d] ^ 0xef) * 8 + 0x10) == 0x444)) &&
           ((((flag[0x1e] ^ 0xf0) + 7 >> 5 | (flag[0x1e] ^ 0xf0) * 8 + 0x38) == 0x4d4 &&
            (((flag[0x1f] ^ 1) + 4 >> 5 | (flag[0x1f] ^ 1) * 8 + 0x20) == 0x313)))))))) &&
        (((flag[0x20] ^ 0x12) + 6 >> 5 | (flag[0x20] ^ 0x12) * 8 + 0x30) == 0x2ea)) &&
       (((((flag[0x21] ^ 0x23) + 1 >> 5 | (flag[0x21] ^ 0x23) * 8 + 8) == 0x2e2 &&
         (((flag[0x22] ^ 0x34) + 3 >> 5 | (flag[0x22] ^ 0x34) * 8 + 0x18) == 0x2a2)) &&
        ((((flag[0x23] ^ 0x45) + 5 >> 5 | (flag[0x23] ^ 0x45) * 8 + 0x28) == 0x58 &&
         (((((flag[0x24] ^ 0x56) + 2 >> 5 | (flag[0x24] ^ 0x56) * 8 + 0x10) == 0x129 &&
           (((flag[0x25] ^ 0x67) + 7 >> 5 | (flag[0x25] ^ 0x67) * 8 + 0x38) == 0xd0)) &&
          (((flag[0x26] ^ 0x78) + 4 >> 5 | (flag[0x26] ^ 0x78) * 8 + 0x20) == 0xa8)))))))))) &&
     ((((((flag[0x27] ^ 0x89) + 6 >> 5 | (flag[0x27] ^ 0x89) * 8 + 0x30) == 0x767 &&
        (((flag[0x28] ^ 0x9a) + 3 >> 5 | (flag[0x28] ^ 0x9a) * 8 + 0x18) == 0x7bf)) &&
       (((flag[0x29] ^ 0xab) + 5 >> 5 | (flag[0x29] ^ 0xab) * 8 + 0x28) == 1999)) &&
      ((((((flag[0x2a] ^ 0xbc) + 2 >> 5 | (flag[0x2a] ^ 0xbc) * 8 + 0x10) == 0x777 &&
         (((flag[0x2b] ^ 0xcd) + 7 >> 5 | (flag[0x2b] ^ 0xcd) * 8 + 0x38) == 0x828)) &&
        ((((((flag[0x2c] ^ 0xde) + 4 >> 5 | (flag[0x2c] ^ 0xde) * 8 + 0x20) == 0x56d &&
           (((((flag[0x2d] ^ 0xef) + 6 >> 5 | (flag[0x2d] ^ 0xef) * 8 + 0x30) == 0x484 &&
             (((flag[0x2e] ^ 0xf0) + 1 >> 5 | (flag[0x2e] ^ 0xf0) * 8 + 8) == 0x41c)) &&
            (((flag[0x2f] ^ 1) + 3 >> 5 | (flag[0x2f] ^ 1) * 8 + 0x18) == 0x30b)))) &&
          ((((flag[0x30] ^ 0x12) + 5 >> 5 | (flag[0x30] ^ 0x12) * 8 + 0x28) == 0x129 &&
           (((flag[0x31] ^ 0x23) + 2 >> 5 | (flag[0x31] ^ 0x23) * 8 + 0x10) == 0xa8)))) &&
         (((flag[0x32] ^ 0x34) + 7 >> 5 | (flag[0x32] ^ 0x34) * 8 + 0x38) == 0x68)))) &&
       (((((flag[0x33] ^ 3) + 5 >> 5 | (flag[0x33] ^ 3) * 8 + 0x28) == 0x1e1 &&
         (((flag[0x34] ^ 0xbe) + 3 >> 5 | (flag[0x34] ^ 0xbe) * 8 + 0x18) == 0x515)) &&
        (((flag[0x35] ^ 0xfe) + 6 >> 5 | (flag[0x35] ^ 0xfe) * 8 + 0x30) == 0x44c)))))))) {
    FUN_1400018d0((longlong *)cout_exref,
                  "Congrats, you\'ve cracked it! Now, go claim your victory! \n");
    outputpointer = FUN_1400018d0((longlong *)cout_exref,"BTW your flag is: ");
    outputpointer = FUN_1400018d0(outputpointer,*(char **)(param_2 + 8));
    std::basic_ostream<>::operator<<((basic_ostream<> *)outputpointer,FUN_140001aa0);
  }
  return 0;
}



```
## Solution

We create a Python script that attempts to reverse the operations applied to each datapointer value using brute force. It tries all possible byte values (0-255) and checks if, when processed with the same operations (XOR, addition, shift, multiplication), it matches the target_value.

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
