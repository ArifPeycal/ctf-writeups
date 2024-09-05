# Ilmu Hisab 🔧
## Description
> Mampukah tuan hamba mengira?
>
> Connection 1: nc 103.28.91.24 10012
> 
> Connection 2: nc 103.28.91.24 10014
## Challenge Overview

Upon decompiling given `perhitungan` file, we discover 3 functions worth to look into:
1. `main()`:

    - The program starts by printing a message and then calls the `addtwonumber()` function.
2. ```addtwonumber()``` :

    - It prompts the user to input two integers.
    - It checks if the input is valid (ensuring that the input is an integer and within a specific range).
    - It then sums the two numbers and performs certain checks to decide whether to call the merdeka function.

3. ```merdeka()``` :
   
    - Print the flag
      
### Conditions to Trigger merdeka()

There are two specific conditions where the merdeka function is called:

1. First number is 0x539 (1337 in decimal), the second number is greater than 0x1ca3 (7331 in decimal), and their sum is negative.

```cpp
if (__n == 0x539 && __n_1 > 0x1ca3 && __n_2 < 0)
    merdeka();
```

2. Both input numbers are negative and their sum is positive.
```cpp
else if (__n < 0 && __n_1 < 0 && __n_2 > 0)
    merdeka();
```
## Solution


Addition overflow occurs when the result of adding two numbers exceeds the maximum value that can be stored in the data type used to hold the result. This is particularly relevant in programming languages and systems where data types have fixed sizes, such as int32_t (32-bit integer) or int64_t (64-bit integer).

### Understanding Integer Addition Overflow
Consider a 32-bit signed integer, which can hold values from `-2147483648` to `2147483647`. If you try to add a positive number with the largest 32-bit integer value, the sum might exceed the maximum positive value that a 32-bit integer can represent. When this happens, the result "wraps around" and becomes a large negative number due to the way binary arithmetic works.

Example of Overflow:
```cpp
int32_t a = 1337;
int32_t b = 2147483647;
int32_t sum = a + b;
// sum = -2147483647
```

If we add a large enough positive number to `1337`, the sum could exceed `2147483647`, causing an overflow and resulting in a large negative number. This negative sum could then satisfy the condition to trigger the merdeka() function.

## Flag
```
3108{n0mb0r_k3r4mat}
```
