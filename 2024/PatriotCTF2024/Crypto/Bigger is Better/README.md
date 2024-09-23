# Bigger is Better
## Description
> I heard choosing a small value for e when creating an RSA key pair is a bad idea. So I switched it up!

```
N = 0xa0d9f425fe1246c25b8c3708b9f6d7747dd5b5e7f79719831c5cbe19fb7bab66ed62719b3fc6090120d2cfe1410583190cd650c32a4151550732b0fc97130e5f02aa26cb829600b6ab452b5b11373ec69d4eaae6c392d92da8bcbea85344af9d4699e36fdca075d33f58049fd0a9f6919f3003512a261a00985dc3d9843a822974df30b81732a91ce706c44bde5ff48491a45a5fa8d5d73bba5022af803ab7bd85250e71fc0254fcf078d21eaa5d38724014a85f679e8a7a1aad6ed22602465f90e6dd8ef95df287628832850af7e3628ad09ff90a6dbdf7a0e6d74f508d2a6235d4eae5a828ac95558bbdf72f39af5641dfe3edb0cdaab362805d926106e2af
e = 0x5af5dbe4af4005564908a094e0eabb0a921b7482483a753e2a4d560700cb2b2dc9399b608334e05140f54d90fcbef70cec097e3f75395d0c4799d9ec3e670aca41da0892a7b3d038acb7a518be1ced8d5224354ce39e465450c12be653639a8215afb1ba70b1f8f71fc1a0549853998e2337604fca7edac67dd1e7ddeb897308ebf26ade781710e6a2fe4c533a584566ea42068d0452c1b1ecef00a781b6d31fbab893de0c9e46fce69c71cefad3119e8ceebdab25726a96aaf02a7c4a6a38d2f75f413f89064fef14fbd5762599ca8eb3737122374c5e34a7422ea1b3d7c43a110d3209e1c5e23e4eece9e964da2c447c9e5e1c8a6038dc52d699f9324fd6b9
c = 0x731ceb0ac8f10c8ff82450b61b414c4f7265ccf9f73b8e238cc7265f83c635575a9381aa625044bde7b34ad7cce901fe7512c934b7f6729584d2a77c47e8422c8c0fe2d3dd12aceda8ef904ad5896b971f8b79048e3e2f99f600bf6bac6cad32f922899c00fdc2d21fcf3d0093216bfc5829f02c08ba5e534379cc9118c347763567251c0fe57c92efe0a96c8595bac2c759837211aac914ea3b62aae096ebb8cb384c481b086e660f0c6249c9574289fe91b683609154c066de7a94eafa749c9e92d83a9d473cc88accd9d4c5754ccdbc5aa77ba9a790bc512404a81fc566df42b652a55b9b8ffb189f734d1c007b6cbdb67e14399182016843e27e6d4e5fca

```
```py
def rational_to_contfrac(x, y):
    # Converts a rational x/y fraction into a list of partial quotients [a0, ..., an]
    a = x // y
    pquotients = [a]
    while a * y != x:
        x, y = y, x - a * y
        a = x // y
        pquotients.append(a)
    return pquotients

def convergents_from_contfrac(frac):
    # Computes the list of convergents using the list of partial quotients
    convs = []
    for i in range(len(frac)):
        convs.append(contfrac_to_rational(frac[0:i + 1]))
    return convs

def contfrac_to_rational(frac):
    # Converts a finite continued fraction [a0, ..., an] to an x/y rational.
    if len(frac) == 0:
        return (0, 1)
    num = frac[-1]
    denom = 1
    for _ in range(-2, -len(frac) - 1, -1):
        num, denom = frac[_] * num + denom, num
    return (num, denom)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, x, y = egcd(b % a, a)
    return (g, y - (b // a) * x, x)

def mod_inv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return (x + m) % m

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def crack_rsa(e, n):
    frac = rational_to_contfrac(e, n)
    convergents = convergents_from_contfrac(frac)
    
    for (k, d) in convergents:
        if k != 0 and (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            s = n - phi + 1
            # Check if x*x - s*x + n = 0 has integer roots
            D = s * s - 4 * n
            if D >= 0:
                sq = isqrt(D)
                if sq * sq == D and (s + sq) % 2 == 0:
                    return d

# Given values
N = 0xa0d9f425fe1246c25b8c3708b9f6d7747dd5b5e7f79719831c5cbe19fb7bab66ed62719b3fc6090120d2cfe1410583190cd650c32a4151550732b0fc97130e5f02aa26cb829600b6ab452b5b11373ec69d4eaae6c392d92da8bcbea85344af9d4699e36fdca075d33f58049fd0a9f6919f3003512a261a00985dc3d9843a822974df30b81732a91ce706c44bde5ff48491a45a5fa8d5d73bba5022af803ab7bd85250e71fc0254fcf078d21eaa5d38724014a85f679e8a7a1aad6ed22602465f90e6dd8ef95df287628832850af7e3628ad09ff90a6dbdf7a0e6d74f508d2a6235d4eae5a828ac95558bbdf72f39af5641dfe3edb0cdaab362805d926106e2af
e = 0x5af5dbe4af4005564908a094e0eabb0a921b7482483a753e2a4d560700cb2b2dc9399b608334e05140f54d90fcbef70cec097e3f75395d0c4799d9ec3e670aca41da0892a7b3d038acb7a518be1ced8d5224354ce39e465450c12be653639a8215afb1ba70b1f8f71fc1a0549853998e2337604fca7edac67dd1e7ddeb897308ebf26ade781710e6a2fe4c533a584566ea42068d0452c1b1ecef00a781b6d31fbab893de0c9e46fce69c71cefad3119e8ceebdab25726a96aaf02a7c4a6a38d2f75f413f89064fef14fbd5762599ca8eb3737122374c5e34a7422ea1b3d7c43a110d3209e1c5e23e4eece9e964da2c447c9e5e1c8a6038dc52d699f9324fd6b9
c = 0x731ceb0ac8f10c8ff82450b61b414c4f7265ccf9f73b8e238cc7265f83c635575a9381aa625044bde7b34ad7cce901fe7512c934b7f6729584d2a77c47e8422c8c0fe2d3dd12aceda8ef904ad5896b971f8b79048e3e2f99f600bf6bac6cad32f922899c00fdc2d21fcf3d0093216bfc5829f02c08ba5e534379cc9118c347763567251c0fe57c92efe0a96c8595bac2c759837211aac914ea3b62aae096ebb8cb384c481b086e660f0c6249c9574289fe91b683609154c066de7a94eafa749c9e92d83a9d473cc88accd9d4c5754ccdbc5aa77ba9a790bc512404a81fc566df42b652a55b9b8ffb189f734d1c007b6cbdb67e14399182016843e27e6d4e5fca

# Call the crack_rsa function
d = crack_rsa(e, N)

if d:
    m = hex(pow(c, d, N))[2:]  # Decrypt the message
    # Convert hex to bytes
    message = bytes.fromhex(m).decode('utf-8', errors='ignore')
    print(f"Decrypted message: {message}")
    print(f"Private key d: {d}")
else:
    print("Failed to crack RSA.")
```
```
pctf{fun_w1th_l4tt1c3s_f039ab9}
```
