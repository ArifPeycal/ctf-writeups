# Sandiwara Pena

> Sebuah karya pena agung kini beralih wajah menjadi baris-baris kod. Setiap bait huruf diselindung menanti untuk dibaca.
>
> Awalnya tampak di sebalik susunan yang teratur. Akhirnya hanya terungkai apabila engkau mengenalinya.
> 
> Satukanlah untuk menjadi bendera sebenar.

## Solution
This binary is a simple XOR encryption. In order to get the flag, you need to dump all 3 arrays from the binary(`modul_alpha`, `modul_sigma`, `modul_omega`) and XORed it by 0x42.

```py
undefined8 pemeriksaan_lapisan(long param_1)
{
  byte bVar1;
  byte bVar2;
  int local_14;

  local_14 = 0;
  while (true) {
    if (0x1e < local_14) {   // loop until index 30 (0..30 = 31 chars)
      return 1;              // ✅ flag is correct
    }
    bVar1 = *(byte *)(param_1 + local_14);   // take flag[i]
    bVar2 = ekstrak_modul(local_14);         // expected byte from tables
    if ((bVar1 ^ 0x42) != bVar2) break;      // check fails
    local_14 = local_14 + 1;
  }
  return 0;   // ❌ wrong flag
}
```


```py
# Arrays from your dump
modul_alpha = [0x73, 0x5a, 0x5b, 0x59, 0x4f, 0x71, 0x1f, 0x65, 0x5c, 0x7d]
modul_sigma = [0x63, 0x64, 0x4b, 0x4f, 0x4e, 0x62, 0x4f, 0x68, 0x47, 0x55]
modul_omega = [0x70, 0x47, 0x48, 0x44, 0x57, 0x60, 0x58, 0x52, 0x55, 0x4e, 0x57]

# Concatenate the three modules (just like ekstrak_modul would)
modules = modul_alpha + modul_sigma + modul_omega

flag_chars = []
for i, val in enumerate(modules):
    flag_chars.append(chr(val ^ 0x42))  # XOR with 0x42

flag = "".join(flag_chars)
print(flag)
```

## Flag
```
3108{P4k_S4m4d_P3ju4ng_S4st3r4}
```
