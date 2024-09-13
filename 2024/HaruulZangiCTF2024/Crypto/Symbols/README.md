# Symbols
## Description
> Digital matrix rain contains some strange symbols. What are they trying to convey? -zjzoloo

## Challenge Overview
We were given `Chall` binary file to analyze. When I looked up its content, it had a `PDF` header which hinted that we needed to change the file extension.  

Looks like we need to interpret the symbols and provide the first letter of the symbol's name. 

![image](https://github.com/user-attachments/assets/3d3372ec-ea47-4bf5-b390-671a526d6d08)

## Solution

Following the flag format, we know that the first two symbols are `H/h` (heart, ♡) and `Z/z` (Zeta, ζ). But, how to know whether we need to use lowercase or upper case? 

Greek alphabets such as Alpha, Beta and Zeta also have uppercase and lowercase symbols. In this case, `ζ` is lowercase so it is equivalent to `z`. Since we know `z` will be lowercase, the letter `h` will also follow the same format. 

![image](https://github.com/user-attachments/assets/f91fc854-3bfe-494b-9170-bcd3ce073682)

Repeat the same process of searching the symbol name, and determine whether it is uppercase or lowercase. 
```
λ = l (lambda lowercase)
ℵ = a (aleph lowercase)
△ = t (triangle lowercase)
η = e (eta lowercase)
Ξ = X (xi uppercase)
∫ = i (integral lowercase)
Σ = S (sigma uppercase)
∀ = f (for all lowercase)
Υ = U (upsilon uppercase)
∇ = n (nabla lowercase)
ρ = r (rho lowercase)
∞ = I (infinity lowercase)
Γ = G (gamma uppercase)
♡ = h (heart lowercase)
θ = t (theta lowercase)
```
## Flag
```
hz2024{lateX_iSfUn_riGht_?}
```
