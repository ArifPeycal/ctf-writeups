# Password Protector

## Description
> We've been after a notorious skiddie who took the "Is it possible to have a completely secure computer system" question a little too literally. After he found out we were looking for them, they moved to live at the bottom of the ocean in a concrete box to hide from the law. Eventually, they'll have to come up for air...or get sick of living in their little watergapped world. They sent us this message and executable. Please get their password so we can be ready.
> 
> "Mwahahaha you will nOcmu{9gtufever crack into my passMmQg8G0eCXWi3MY9QfZ0NjCrXhzJEj50fumttU0ympword, i'll even give you the key and the executable:::: Zfo5ibyl6t7WYtr2voUEZ0nSAJeWMcN3Qe3/+MLXoKL/p59K3jgV"

```py
import os
import secrets
from base64 import *

def promptGen():
    flipFlops = lambda x: chr(ord(x) + 1)
    with open('topsneaky.txt', 'rb') as f:
        first = f.read()
    bittys = secrets.token_bytes(len(first))
    onePointFive = int.from_bytes(first) ^ int.from_bytes(bittys)
    second = onePointFive.to_bytes(len(first))
    third = b64encode(second).decode('utf-8')
    bittysEnc = b64encode(bittys).decode('utf-8')
    fourth = ''
    for each in third:
        fourth += flipFlops(each)
    fifth = f"Mwahahaha you will n{fourth[0:10]}ever crack into my pass{fourth[10:]}word, i'll even give you the key and the executable:::: {bittysEnc}"
    return fifth

def main():
    print(promptGen())
if __name__ == '__main__':
    main()
```
```py
 import base64

def reverse_flip_flops(s):
    return ''.join(chr(ord(c) - 1) for c in s)

def decode_message():
    # Extract the key and the encoded portion
    key_b64 = "Zfo5ibyl6t7WYtr2voUEZ0nSAJeWMcN3Qe3/+MLXoKL/p59K3jgV"
    transformed_b64 = "Ocmu{9gtufMmQg8G0eCXWi3MY9QfZ0NjCrXhzJEj50fumttU0ymp"

    # Step 1: Reverse the character shift
    reversed_b64 = reverse_flip_flops(transformed_b64)
    
    # Step 2: Base64 decode the reversed string to get the XORed result
    decoded_bytes = base64.b64decode(reversed_b64)
    
    # Step 3: Base64 decode the key
    key = base64.b64decode(key_b64)

    # Step 4: XOR the decoded bytes with the key to recover the original file content
    original_bytes = bytes([b ^ k for b, k in zip(decoded_bytes, key)])
    
    return original_bytes

# Decode the message
original_file_content = decode_message()
print(original_file_content)
```
```
PCTF{I_<3_$3CUR1TY_THR0UGH_0B5CUR1TY!!}
```
