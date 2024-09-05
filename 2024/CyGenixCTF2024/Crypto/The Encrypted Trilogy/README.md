# The Encrypted Trilogy
## Description

> In this multi-part cryptographic challenge, you are presented with a series of encrypted messages, each protected by different keys and methodologies.
> 
> Your task is to decrypt the ciphertexts provided in three distinct parts.
>
> The challenge requires a deep understanding of number theory, RSA encryption, and clever manipulation of cryptographic principles.Each part of the challenge increases in complexity
> 
> Only those with a sharp mind for cryptography will be able to decode this trilogy and retrieve the hidden flag. Are you ready to break the cipher?

## Solution

### Part 1: Standard RSA Decryption
- Given: e, p, q, and ct.
- Approach:
  1. Calculate the modulus n as p * q.
  2. Compute φ(n) (Euler's totient) as (p-1) * (q-1).
  3. Find the private key d as the modular inverse of e modulo φ(n).
  4. Decrypt the ciphertext by raising it to d modulo n.

```python
def rsa_decrypt_part1(e, p, q, ct):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    d = inverse(e, phi_n)
    pt = pow(ct, d, n)
    return long_to_bytes(pt)
```
Outcome: ```CyGenixCTF{r```
### Part 2: Low Exponent Attack (Cube Root)
- Given: e, n, and ct.
- Approach:
  1. Since e = 3, and the message is small, it was encrypted without padding, allowing the ciphertext to be directly decrypted using an integer cube root.
  2. Calculate the integer cube root of the ciphertext to recover the plaintext.
```python
from Crypto.Util.number import inverse, long_to_bytes

def integer_cube_root(x):
    # Calculate the integer cube root using binary search
    low = 0
    high = x
    while low < high:
        mid = (low + high) // 2
        if mid**3 < x:
            low = mid + 1
        else:
            high = mid
    return low

def rsa_decrypt_part2(e, n, ct):
    # Compute the cube root of the ciphertext
    pt = integer_cube_root(ct)
    
    # Convert the plaintext integer to bytes
    pt_bytes = pt.to_bytes((pt.bit_length() + 7) // 8, 'big')
    
    return pt_bytes
```
Outcome: ```sa_c1ph3r_dec```.
### Part 3: Factorization and Decryption
- Given: e, n, and multiple ciphertexts.
- Approach:
  1. Factorize n by brute-forcing small primes.
  2. Compute φ(n) and derive the private key d.
  3. Decrypt each ciphertext using d to get the corresponding plaintexts.
```python
def rsa_decrypt_part3(e, n, cts):
    # Brute-force all small primes to factorize n
    for i in range(2, n):
        if n % i == 0:
            p = i
            q = n // i
            break
    phi_n = (p - 1) * (q - 1)
    d = inverse(e, phi_n)
    
    plaintexts = []
    for ct in cts:
        pt = pow(ct, d, n)
        plaintexts.append(long_to_bytes(pt))
    
    return plaintexts

```
Outcome: ```rypt_succ3ss}```

## Flag
```CyGenixCTF{rsa_c1ph3r_decrypt_succ3ss}```
