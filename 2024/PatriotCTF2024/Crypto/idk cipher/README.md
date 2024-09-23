# idk cipher
## Description
> I spent a couple of hours with ???; now I am the world's best cryptographer!!! note: the flag contents will just random chars-- not english/leetspeak

```py

import base64
"""
********************************************
*                                          *
*                                          *
********************************************
"""
# WARNING: This is a secret key. Do not expose it.
srt_key = 'secretkey' # // TODO: change the placeholder
usr_input = input("\t:"*10)
if len(usr_input) <= 1:
    raise ValueError("PT must be greater than 1")
if len(usr_input) % 2 != 0:
    raise ValueError("PT can only be an even number")
if not usr_input.isalnum():
    raise ValueError("Only alphabets and numbers supported")
# WARNING: Reversing input might expose sensitive information.
rsv_input = usr_input[::-1]
output_arr = []
for i in range(16):
    c1 = ord(usr_input[i])
    c2 = ord(rsv_input[i])
    enc_p1 = chr(c1 ^ ord(srt_key[i % len(srt_key)]))
    enc_p2 = chr(c2 ^ ord(srt_key[i % len(srt_key)]))
    output_arr.append(enc_p1)
    output_arr.append(enc_p2)
# WARNING: Encoded text should not be decoded without proper authorization.
encoded_val = ''.join(output_arr)
b64_enc_val = base64.b64encode(encoded_val.encode())
R = "R"*20
E = "E"*5
EXCLAMATION = "!"*5
print(f"ULTRA SUPE{R} SECUR{E} Encoded Cipher Text{EXCLAMATION}:", b64_enc_val.decode())

```
```py
import base64

# The secret key used during encryption
srt_key = 'secretkey'  # This should match the key used in the original code

# The encoded cipher text
encoded_cipher_text = "QRVWUFdWEUpdXEVGCF8DVEoYEEIBBlEAE0dQAURFD1I="

# Step 1: Base64 decode the encoded cipher text
decoded_bytes = base64.b64decode(encoded_cipher_text)
decoded_val = decoded_bytes.decode()

# Step 2: XOR decryption
output_arr = []
p1_arr = []
p2_arr = []

for i in range(int(len(decoded_val) / 2)):
    c1 = decoded_val[i * 2]  # Take the first character of the pair
    c2 = decoded_val[i * 2 + 1]  # Take the second character of the pair
    # Reverse the XOR operation
    dec_p1 = chr(ord(c1) ^ ord(srt_key[i % len(srt_key)]))
    dec_p2 = chr(ord(c2) ^ ord(srt_key[i % len(srt_key)]))
    p1_arr.append(dec_p1)
    p2_arr.append(dec_p2)


# Step 3: Reverse the input to get the original user input
# original_input = ''.join(output_arr)[::-1]

print("Original User Input:", p1_arr)
print("Original User Input:", p2_arr[::-1])
```
