# Exclusivity
## Description
> Welcome back, Space Cowboy. The Minutemen have intercepted a corrupted data stream from the Frontier Board. Hidden within the stream are critical coordinates, buried under duplicate entries caused by the Board's sabotage.

## Overview 
Your mission is to sift through this chaotic stream and extract the unique entries. These coordinates must be preserved in the order they were received to maintain their integrity. Any duplicates are remnants of the Board's sabotage—eliminate them swiftly.

Example
Input
String Input: 7 3 7 9 1 3 5 9

Output
String Expected Output: 7 3 9 1 5

## Solution
```python
# take in the number
n = input()

# Split the input string into a list of numbers
numbers = n.split()

# Remove duplicates while preserving order using dict.fromkeys()
unique_numbers = list(dict.fromkeys(numbers))

# Join the unique numbers into a space-separated string
result = ' '.join(unique_numbers)

# Print the result
print(result)
```

## Flag
```
HTB{r3m0v1ng_dup5_15_s0_345y_1F_y0u_kn0w_h0w_t0_c0d3!_e6afac6a4455ed1bf1752f1d6c68b904}
```
