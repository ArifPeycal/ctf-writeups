# No Name

> Cari rahsia tersembunyi dalam file tersebut:
>
> Nama File: noname.tar.gz MD5: a59eb92607da961336509ff128eb808b SHA1: fc7976e2d9a184e4b9ce0aa3961100d3226ef5c8

## Solution

Decompile binary using Ghidra, found some strange naming functions, most of them just print a character from the flag. Combine all to get the flag.

```c
undefined8 __5d41402abc4b2a76b9719d911017c592(void)

{
  std::__ostream_insert<>((basic_ostream *)std::cout,"3",1);
  return 0;
}
```
```c
                             DAT_0010201c                                    XREF[1]:     __5d41402abc4b2a76b9719d911017c5
        0010201c 33              ??         33h    3
        0010201d 00              ??         00h
                             DAT_0010201e                                    XREF[1]:     __c4ca4238a0b923820dcc509a6f7584
        0010201e 31              ??         31h    1
        0010201f 00              ??         00h
                             DAT_00102020                                    XREF[1]:     __c81e728d9d4c2f636f067f89cc1486
        00102020 30              ??         30h    0
        00102021 00              ??         00h
                             DAT_00102022                                    XREF[1]:     __eccbc87e4b5ce2fe28308fd9f2a7ba
        00102022 38              ??         38h    8
        00102023 00              ??         00h
                             DAT_00102024                                    XREF[1]:     __a87ff679a2f3e71d9181a67b754212
        00102024 7b              ??         7Bh    {
        00102025 00              ??         00h
                             DAT_00102026                                    XREF[1]:     __e4da3b7fbbce2345d7772b0674a318
        00102026 70              ??         70h    p
        00102027 00              ??         00h
                             DAT_00102028                                    XREF[1]:     __1679091c5a880faf6fb5e6087eb1b2
        00102028 72              ??         72h    r
        00102029 00              ??         00h
                             DAT_0010202a                                    XREF[2]:     __8f14e45fceea167a5a36dedd4bea25
                                                                                          __08a4415e9d594ff960030b921d42b9
        0010202a 65              ??         65h    e
        0010202b 00              ??         00h
                             DAT_0010202c                                    XREF[1]:     __c9f0f895fb98ab9159f51fd0297e23
        0010202c 64              ??         64h    d
        0010202d 00              ??         00h
                             DAT_0010202e                                    XREF[1]:     __45c48cce2e2d7fbdea1afc51c7c6ad
        0010202e 69              ??         69h    i
        0010202f 00              ??         00h
                             DAT_00102030                                    XREF[1]:     __f970e2767d0cfe75876ea857f92e31
        00102030 63              ??         63h    c
        00102031 00              ??         00h
                             DAT_00102032                                    XREF[1]:     __cc8c0a97c2dfcd73caff160b65aa39
        00102032 74              ??         74h    t
        00102033 00              ??         00h
                             DAT_00102034                                    XREF[1]:     __b2b04af9f8f3ab06229e03ac8d3c24
        00102034 61              ??         61h    a
        00102035 00              ??         00h
                             DAT_00102036                                    XREF[1]:     __b787d22d9cb06342658bf546039117
        00102036 62              ??         62h    b
        00102037 00              ??         00h
                             DAT_00102038                                    XREF[1]:     __b6bb43df4525b928a105fb5741bddb
        00102038 6c              ??         6Ch    l
        00102039 00              ??         00h
                             DAT_0010203a                                    XREF[1]:     __071bf94d562f56075180027e6fff5a
        0010203a 7d              ??         7Dh    }
        0010203b 00              ??         00h
```

## Flag
```
3108{predictable}
```
