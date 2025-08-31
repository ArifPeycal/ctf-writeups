# Maznah Legacy

> Iron Lady? Adakah itu Iron Man versi wanita? 🤔 Ataupun sebenarnya tokoh lain yang cukup terkenal di Malaysia?
> 
> Hanya dengan bedah program ini, anda akan tahu kebenarannya disbalik sosok misteri tersebut...

## Solution
Decompile using Ghidra, the program iterates over each character of the flag:
```
uVar4 = ((byte)__s[uVar5] + 0x2a + uVar5) % 0x7f;
```
- Adds 42 (0x2a) and the character’s index (uVar5) to the ASCII value of the character.
- Takes modulo 127 (% 0x7f).
- Prints the values as an integer array.

Reverse the operation to get the flag
```
nums = [93, 92, 92, 101, 42, 0, 100, 29, 18, 9, 35, 29, 34, 45, 24, 10, 45, 107, 35, 112, 50, 111, 51, 33, 7, 45, 55, 121, 49, 123, 40, 15, 54, 123, 59, 125, 60, 57, 78]

secret = ""
for i, n in enumerate(nums):
    c = (n - 42 - i) % 127
    secret += chr(c)

print(secret)
```

## Flag
```
3108{P4k_Ungku_Pr0f3s0r_Dir4j4_Ek0n0mi}
```
