# Mesej Rahsia

## Description
> Tak susah pun, run je script

## Solution
```py
mapping = {
    'a': 'j', 'b': 'b', 'c': 'a', 'd': 'c', 'e': 'm', 'f': 'n', 'g': 'i', 'h': 'p', 'i': 'o', 'j': 'q',
    'k': 'r', 'l': 't', 'm': 'x', 'n': 'z', 'o': 'v', 'p': 's', 'q': 'u', 'r': 'y', 's': 'h', 't': 'g',
    'u': 'd', 'v': 'e', 'w': 'f', 'x': 'k', 'y': 'l', 'z': 'w'
}

# Given reversed flag tuple
flag_tuple = (3108, "{", 'p', 'q', 'b', 'p', 'l', 'g', 'l', 'q', 'l', 'v', "_", 'd', 'g', 'h', 's', 'v', 'k', "_", 'l', 'v', 'm', 'l', "}")

# Extract the flag part (excluding the integer)
flag_part = flag_tuple[1:]

# Translate the flag
flag = "".join(mapping.get(char, char) for char in flag_part)

print(flag)
```

## Flag
```
3108{substitute_cipher_text}
```
