# DH-9000
## Description
> The robots just introduced this supposedly unbreakable crypto scheme that allows them to share secrets over insecure channels, DH-9000. I'm pretty sure this isn't anything new though, so we should still be able to find their shared secret.
>
> p = 8089
>
> g = 823
>
> A = 7608
>
> B = 5796
>
> Note: submit the shared secret wrapped in CyGenixCTF{}

## Solution

In this Diffie-Hellman key exchange scenario, the goal is to find Alice's secret key using brute-force. The known values are:

- p (a public modulus)
- g (a public base)
- A (Alice's public key)
- B (Bob's public key)

The script iterates through all possible values of Alice's secret key (a_secret). For each possible value, it calculates g^a_secret mod p and compares it with Alice's public key (A). When a match is found, it means the correct secret key has been identified.
Once Alice's secret key is discovered, it is used to calculate the shared secret by computing B^a_secret mod p, which both Alice and Bob would use for secure communication.

```python
p = 8089  # Public modulus (known)
g = 823   # Public base (known)
A = 7608  # Alice's public key (known)
B = 5796  # Bob's public key (known)

# Attempt to brute-force Alice's secret key
for a_secret in range(p):
    if pow(g, a_secret, p) == A:
        print(f"Found Alice's secret: {a_secret}")
        shared_secret = pow(B, a_secret, p)
        print(f"Shared secret: {shared_secret}")
        break
```
## Flag
```CyGenixCTF{2293}```
