# mini RSA
## Description
## Challenge Overview
In this challenge, we are provided with a ciphertext c and a modulus n. The encryption was performed using RSA with a public exponent e = 3. Our task is to decrypt the ciphertext and recover the original flag. <br>

### Key Details:
- Public Exponent (e): 3
- Ciphertext (c): (provided in the challenge)
- Modulus (n): (provided in the challenge)

### Observations
Given that the public exponent 𝑒=3 is small and the modulus 𝑛 is large, there is a possibility that the plaintext message 𝑚 is small enough that m**3<n. If this condition holds true, no wrapping (modulus operation) occurs during encryption, making the cube root of 
𝑐 directly equal to the plaintext message.

### Decryption Strategy
To decrypt the message, we can compute the integer cube root of the ciphertext. This gives us the plaintext message 𝑚, which can then be converted back to the original flag.
1. Calculate the Cube Root <br>
If 𝑚**3 < 𝑛, then 𝑚**3=𝑐. We can take the cube root of 𝑐 to find 𝑚
2. Convert to Bytes <br>
The integer 𝑚 is then converted back to its original byte representation, which reveals the flag.
3. Output the Flag <br>
The resulting bytes are decoded to reveal the plaintext flag.
```python
from Crypto.Util.number import long_to_bytes
from sympy import Integer
import gmpy2

# Provided ciphertext and modulus
c =  5926440800047066468184992240057621921188346083131741617482777221394411358243130401052973132050605103035491365016082149869814064434831123043357292949645845605278066636109516907741970960547141266810284132826982396956610111589
n =  155735289132981544011017189391760271645447983310532929187034314934077442930131653227631280820261488048477635481834924391697025189196282777696908403230429985112108890167443195955327245288626689006734302524489187183667470192109923398146045404320502820234742450852031718895027266342435688387321102862096023537079

# Calculate the integer cube root
m = gmpy2.iroot(c, 3)[0]  # Computes the integer cube root

# Convert the resulting number to bytes and decode it
flag = long_to_bytes(m).decode('utf-8')

print("Recovered flag:", flag)
```

## Flag
```flag{S0_y0u_c4n_s0lv3_s0m3_RSA}```
