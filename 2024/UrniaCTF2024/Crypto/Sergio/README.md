# Sergio
## Description
> In the heart of Tehran, a cunning spy organization has been using a flawed implementation of RSA to secure its secret communications. Sergio, an ace cryptographer, has intercepted an encrypted message, but only has the public key to work with. Can you assist Sergio in decrypting the message and uncovering the hidden secrets?
>
> Reminder: Remember to submit the flag in this format: UCTF{flag}

## Challenge Overview

The code encrypts `m1` and `m2` with a small exponent `e=3` and encrypts `flag` with two different exponents, `e1` (65537) and `e2` (32769). All equation were using the same modulus, `n` which can lead to `Common Modulus Attack`. 

> Common Modulus Attack is a vulnerability that arises when the same modulus `n` is used with different public exponents to encrypt the same message or related messages. 

```py
from Crypto.Util.number import bytes_to_long as b2l, getPrime

flag = b'uctf{test_flag}'

p = getPrime(1024)
q = getPrime(1024)

n = p*q

m1 = b2l(b'There were a mysterious underground cemetery found in Tabriz about 10 years ago near Blue Mosque while worker were digging in nearby locations')
m2 = b2l(b'It is an unknown cemetry which no historical records have registered it so far and it still remains a mystery for everyone. Can you help recover the secrets behind it?')
c1 = pow(m1, 3, n)
c2 = pow(m2, 3, n)

m = b2l(flag)
e1 = 0x10001
e2 = 0x8001

c3 = pow(m, e1, n)
c4 = pow(m, e2, n)

print(f"c1 = {c1}")
print(f"c2 = {c2}")
print(f"c3 = {c3}")
print(f"c4 = {c4}")
```

## Solution
In order to solve this challenge, we need to know the modulus, `n` first. We can find it by exploiting small exponents of `c1 = pow(m1, 3, n)` and `c2 = pow(m2, 3, n)`. Since both `c1` and `c2` are congruent to `m1^3` and `m2^3` modulo `n`, their difference will be divisible by `n`. Therefore, by computing the GCD, you can recover `n`.

```py
m1_cubed = pow(m1, 3)
m2_cubed = pow(m2, 3)

diff1 = c1 - m1_cubed
diff2 = c2 - m2_cubed

n = gcd(diff1, diff2)

print(f"Recovered modulus n: {n}")
```

Once you've successfully recovered `n`, you can now proceed to decrypt `c3` and `c4`.  We use the extended Euclidean algorithm to find integers a and b such that a⋅e1+b⋅e2=1. This is necessary for the common modulus attack to work.

If `a` or `b` is negative, we compute the modular inverse of the corresponding ciphertext (c3 or c4) modulo n. We calculate m as the product of c3**a mod n and c4**b mod n. Once m is computed, it's converted back to the original flag using long_to_bytes.

## Flag
```
uctf{TABRIZ_myst3r1ous_c3meterY_near_Blue_Mosque}
```
