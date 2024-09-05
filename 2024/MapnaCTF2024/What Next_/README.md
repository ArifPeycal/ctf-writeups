```python
from random import *
from Crypto.Util.number import *
from flag import flag

def encrypt(msg, KEY):
	m = bytes_to_long(msg)
	c = KEY ^ m
	return c

n = 80
TMP = [getrandbits(256) * _ ** 2 for _ in range(n)]
KEY = sum([getrandbits(256 >> _) for _ in range(8)])

enc = encrypt(flag, KEY)

print(f'TMP = {TMP}')
print(f'KEY = {KEY}')
print(f'enc = {enc}')
```
```txt
TMP = [0, 60532113298156934035006892408508955361282411773999112364347341111075018147927, 389708033651020865401865717693397865196213972164600460902422823183461779915980, ...]
KEY = 23226475334448992634882677537728533150528705952262010830460862502359965393545
enc = 2290064970177041546889165766737348623235283630135906565145883208626788551598431732
```
```
print(long_to_bytes(KEY ^ enc).decode())
```
```MAPNA{R_U_MT19937_PRNG_Predictor?}```
