# KinderGarten
## Description
> A little warm-up for a kindergarten challenge. -zjzoloo

```py
from sage.all import *
import string, base64

CHILDREN = string.printable[:62] + '\\='
Z = list(GF(64))

def maptokindergarten(c):
    assert c in CHILDREN
    return Z[CHILDREN.index(c)]

def decrypt(enc, key):
    pkey = key**5 + key**3 + key**2 + 1
    m64 = ''
    
    for e in enc:
        enc_char = maptokindergarten(e)
        original = enc_char / pkey  # Divide by pkey to reverse the multiplication
        m64 += CHILDREN[Z.index(original)]
    
    decoded = base64.b64decode(m64.encode()).decode()
    return decoded

# Given encrypted output
encrypted = "HudnBsx03TGdBIK4NS50=vlo=8NoMouoMSCdBLm9yoK41vl03M0Q"

# Now we need to find the correct key (brute force or otherwise)
# Assuming we can brute-force the key
for possible_key in GF(64):
    try:
        flag = decrypt(encrypted, possible_key)
        print(f"Possible flag: {flag}")
    except Exception as e:
        # Ignore errors due to invalid decryption attempts
        pass

```

## Flag
```
HZ2024{th15_ch4ll3n63_1s_ch1ld'5_pl4y}
```
