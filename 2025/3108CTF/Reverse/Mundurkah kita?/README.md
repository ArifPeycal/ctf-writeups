# Mundurkah kita?

> Apakah rahsia yang tersembunyi di alam sebalik mata ini.
>
> File: simple_calculator.zip MD5: a4ed109e7a58b2538fee130127352c22 SHA1: 8de104194af3cb1899631735503fe2d8b69b6fde

## Solution

Just `strings` and grep.
```
strings simple_calculator.exe | findstr "3108"
```
## Flag
```
3108{nothing_beats_the_string_method}
```
