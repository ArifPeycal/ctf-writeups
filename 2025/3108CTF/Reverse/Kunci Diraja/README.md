# Kunci Diraja

> Di balik angka dan aturan sederhana, tersembunyi kisah seorang insan yang pernah mengangkat martabat bangsa. Kod ini bukan sekadar semakan, tetapi kunci untuk membuka lembaran sejarahnya.

## Solution

For each character in the flag, it will add 0x2a (42 in decimal), add the index of character and take modulo 0x7f (127). You can create a Python script to reverse the output result that you get in text file.

```
uVar4 = ((byte)__s[uVar5] + 0x2a + (int)uVar5) % 0x7f;
```
```py
target = [93, 92, 92, 101, 42, 0, 100, 29, 18, 9, 35, 29, 34, 45, 24, 10, 45, 107, 
          35, 112, 50, 111, 51, 33, 7, 45, 55, 121, 49, 123, 40, 15, 54, 123, 59, 125, 60, 57, 78]

result = ""
for i, val in enumerate(target):
    orig = (val - 42 - i) % 127
    result += chr(orig)

print(result)
```

## Flag
```
3108{P4k_Ungku_Pr0f3s0r_Dir4j4_Ek0n0mi}
```
