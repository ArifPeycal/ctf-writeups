# ADI RaSA...

> Adi Putra terkenal dengan kehebatan matematik dia sejak kecil lagI. Hasil inspirasi daripada beliau, saya telah menghasilkan formula baharu untuk menyulitkan maklumat misteri. Sebelum anda dapat selesaikan cabaran ini, anda harus buktikan dulu sejauh mana anda mengenali Adi Putra.

## Solution

Connect to the server using nc, answer some questions and get the values for `N` and `ciphertext`. Let ChatGPT generate do a script to solve RSA equation.
```py
from sympy import factorint, mod_inverse

# Given values
N = 293492960412007278668808616766320338991219616990905534338059009987
c = 145104198865749436686383467165820612598723883288622970363127633064
e = 65537

# Step 1: Factorize N into primes
factors = factorint(N)  # returns dict {prime: exponent}
primes = list(factors.keys())

if len(primes) != 3:
    raise ValueError("Expected 3 primes, got something else.")

p, q, r = primes
print(f"Factors found:\np = {p}\nq = {q}\nr = {r}")

phi = (p - 1) * (q - 1) * (r - 1)

d = mod_inverse(e, phi)
m = pow(c, d, N)
flag = m.to_bytes((m.bit_length() + 7) // 8, "big")
print("Decrypted flag:", flag)

```

## Flag
```
3108{g3n1uS_m4th3MAT1K_D1lUp4k4N}
```
