# Execution
## Description
> Can you unlock the secrets hidden in the echoes of ancient code?

## Challenge Overview
```c++
undefined8 FUN_140001110(int param_1,longlong param_2)

{
  longlong *outputpointer;
  byte *datapointer;
  
  if (param_1 != 2) {
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  datapointer = *(byte **)(param_2 + 8);
  if (((((((((((*datapointer ^ 18) + 5 >> 5 | (*datapointer ^ 18) * 8 + 40) == 610) &&
            (((datapointer[1] ^ 0x23) + 7 >> 5 | (datapointer[1] ^ 0x23) * 8 + 0x38) == 827)) &&
           (((datapointer[2] ^ 0x34) + 3 >> 5 | (datapointer[2] ^ 0x34) * 8 + 0x18) == 795)) &&
          ((((datapointer[3] ^ 0x45) + 2 >> 5 | (datapointer[3] ^ 0x45) * 8 + 0x10) == 40 &&
           (((datapointer[4] ^ 0x56) + 9 >> 5 | (datapointer[4] ^ 0x56) * 8 + 0x48) == 0x1b1)))) &&
         (((datapointer[5] ^ 0x67) + 4 >> 5 | (datapointer[5] ^ 0x67) * 8 + 0x20) == 0x1d9)) &&
        (((((datapointer[6] ^ 0x78) + 6 >> 5 | (datapointer[6] ^ 0x78) * 8 + 0x30) == 0xf8 &&
          (((datapointer[7] ^ 0x89) + 1 >> 5 | (datapointer[7] ^ 0x89) * 8 + 8) == 1517)) &&
         ((((datapointer[8] ^ 0x9a) + 3 >> 5 | (datapointer[8] ^ 0x9a) * 8 + 0x18) == 0x58d &&
          (((((datapointer[9] ^ 0xab) + 5 >> 5 | (datapointer[9] ^ 0xab) * 8 + 0x28) == 0x6f6 &&
            (((datapointer[10] ^ 0xbc) + 2 >> 5 | (datapointer[10] ^ 0xbc) * 8 + 0x10) == 0x6ee)) &&
           (((datapointer[11] ^ 0xcd) + 7 >> 5 | (datapointer[11] ^ 0xcd) * 8 + 0x38) == 0x585))))))
        )) && (((((((datapointer[12] ^ 0xde) + 4 >> 5 | (datapointer[12] ^ 0xde) * 8 + 0x20) ==
                   0x61e && (((datapointer[13] ^ 0xef) + 3 >> 5 |
                             (datapointer[13] ^ 0xef) * 8 + 0x18) == 0x6fe)) &&
                 ((((datapointer[14] ^ 240) + 5 >> 5 | (datapointer[14] ^ 240) * 8 + 0x28) == 0x5a5
                  && (((((datapointer[15] ^ 1) + 2 >> 5 | (datapointer[15] ^ 1) * 8 + 0x10) == 0x2aa
                       && (((datapointer[16] ^ 0x12) + 9 >> 5 | (datapointer[16] ^ 0x12) * 8 + 0x48)
                           == 0x151)) &&
                      ((((datapointer[17] ^ 0x23) + 4 >> 5 | (datapointer[17] ^ 0x23) * 8 + 0x20) ==
                        0x2ca && (((((datapointer[18] ^ 0x34) + 6 >> 5 |
                                    (datapointer[18] ^ 0x34) * 8 + 0x30) == 0x2ba &&
                                   (((datapointer[19] ^ 0x45) + 1 >> 5 |
                                    (datapointer[19] ^ 0x45) * 8 + 8) == 0x1c1)) &&
                                  (((datapointer[20] ^ 0x56) + 3 >> 5 |
                                   (datapointer[20] ^ 0x56) * 8 + 0x18) == 0x141)))))))))) &&
                ((((datapointer[21] ^ 0x67) + 5 >> 5 | (datapointer[21] ^ 0x67) * 8 + 0x28) == 0x2ca
                 && (((datapointer[0x16] ^ 0x78) + 2 >> 5 | (datapointer[0x16] ^ 0x78) * 8 + 0x10)
                     == 0x149)))) &&
               (((datapointer[23] ^ 0x89) + 7 >> 5 | (datapointer[23] ^ 0x89) * 8 + 0x38) == 0x61e))
              )) &&
      (((((((datapointer[24] ^ 0x9a) + 4 >> 5 | (datapointer[24] ^ 0x9a) * 8 + 0x20) == 0x73f &&
          (((datapointer[25] ^ 0xab) + 6 >> 5 | (datapointer[25] ^ 0xab) * 8 + 0x30) == 0x666)) &&
         ((((datapointer[26] ^ 0xbc) + 1 >> 5 | (datapointer[26] ^ 0xbc) * 8 + 8) == 0x6fe &&
          ((((((datapointer[0x1b] ^ 0xcd) + 3 >> 5 | (datapointer[0x1b] ^ 0xcd) * 8 + 0x18) == 0x52d
             && (((datapointer[0x1c] ^ 0xde) + 5 >> 5 | (datapointer[0x1c] ^ 0xde) * 8 + 0x28) ==
                 0x5bd)) &&
            (((datapointer[0x1d] ^ 0xef) + 2 >> 5 | (datapointer[0x1d] ^ 0xef) * 8 + 0x10) == 0x444)
            ) && ((((datapointer[0x1e] ^ 0xf0) + 7 >> 5 | (datapointer[0x1e] ^ 0xf0) * 8 + 0x38) ==
                   0x4d4 && (((datapointer[0x1f] ^ 1) + 4 >> 5 | (datapointer[0x1f] ^ 1) * 8 + 0x20)
                             == 0x313)))))))) &&
        (((datapointer[0x20] ^ 0x12) + 6 >> 5 | (datapointer[0x20] ^ 0x12) * 8 + 0x30) == 0x2ea)) &&
       (((((datapointer[0x21] ^ 0x23) + 1 >> 5 | (datapointer[0x21] ^ 0x23) * 8 + 8) == 0x2e2 &&
         (((datapointer[0x22] ^ 0x34) + 3 >> 5 | (datapointer[0x22] ^ 0x34) * 8 + 0x18) == 0x2a2))
        && ((((datapointer[0x23] ^ 0x45) + 5 >> 5 | (datapointer[0x23] ^ 0x45) * 8 + 0x28) == 0x58
            && (((((datapointer[0x24] ^ 0x56) + 2 >> 5 | (datapointer[0x24] ^ 0x56) * 8 + 0x10) ==
                  0x129 && (((datapointer[0x25] ^ 0x67) + 7 >> 5 |
                            (datapointer[0x25] ^ 0x67) * 8 + 0x38) == 0xd0)) &&
                (((datapointer[0x26] ^ 0x78) + 4 >> 5 | (datapointer[0x26] ^ 0x78) * 8 + 0x20) ==
                 0xa8)))))))))) &&
     ((((((datapointer[0x27] ^ 0x89) + 6 >> 5 | (datapointer[0x27] ^ 0x89) * 8 + 0x30) == 0x767 &&
        (((datapointer[0x28] ^ 0x9a) + 3 >> 5 | (datapointer[0x28] ^ 0x9a) * 8 + 0x18) == 0x7bf)) &&
       (((datapointer[0x29] ^ 0xab) + 5 >> 5 | (datapointer[0x29] ^ 0xab) * 8 + 0x28) == 1999)) &&
      ((((((datapointer[0x2a] ^ 0xbc) + 2 >> 5 | (datapointer[0x2a] ^ 0xbc) * 8 + 0x10) == 0x777 &&
         (((datapointer[0x2b] ^ 0xcd) + 7 >> 5 | (datapointer[0x2b] ^ 0xcd) * 8 + 0x38) == 0x828))
        && ((((((datapointer[0x2c] ^ 0xde) + 4 >> 5 | (datapointer[0x2c] ^ 0xde) * 8 + 0x20) ==
               0x56d && (((((datapointer[0x2d] ^ 0xef) + 6 >> 5 |
                           (datapointer[0x2d] ^ 0xef) * 8 + 0x30) == 0x484 &&
                          (((datapointer[0x2e] ^ 0xf0) + 1 >> 5 | (datapointer[0x2e] ^ 0xf0) * 8 + 8
                           ) == 0x41c)) &&
                         (((datapointer[0x2f] ^ 1) + 3 >> 5 | (datapointer[0x2f] ^ 1) * 8 + 0x18) ==
                          0x30b)))) &&
             ((((datapointer[0x30] ^ 0x12) + 5 >> 5 | (datapointer[0x30] ^ 0x12) * 8 + 0x28) ==
               0x129 && (((datapointer[0x31] ^ 0x23) + 2 >> 5 |
                         (datapointer[0x31] ^ 0x23) * 8 + 0x10) == 0xa8)))) &&
            (((datapointer[0x32] ^ 0x34) + 7 >> 5 | (datapointer[0x32] ^ 0x34) * 8 + 0x38) == 0x68))
           )) && (((((datapointer[0x33] ^ 3) + 5 >> 5 | (datapointer[0x33] ^ 3) * 8 + 0x28) == 0x1e1
                   && (((datapointer[0x34] ^ 0xbe) + 3 >> 5 | (datapointer[0x34] ^ 0xbe) * 8 + 0x18)
                       == 0x515)) &&
                  (((datapointer[0x35] ^ 0xfe) + 6 >> 5 | (datapointer[0x35] ^ 0xfe) * 8 + 0x30) ==
                   0x44c)))))))) {
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
