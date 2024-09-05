import random
from Crypto.Util.number import bytes_to_long, long_to_bytes

q = 64

# Read the flag from a file
flag = open("flag.txt", "rb").read()
flag_int = bytes_to_long(flag)

# Add random padding
padding_length = random.randint(5, 10)
padding = random.getrandbits(padding_length * 8)
flag_int = (flag_int << (padding_length * 8)) + padding

# Generate the secret key
secret_key = []
while flag_int:
    secret_key.append(flag_int % q)
    flag_int //= q

# Shuffle the secret key
original_order = list(range(len(secret_key)))
random.shuffle(original_order)
shuffled_secret_key = [secret_key[i] for i in original_order]

# Add a random offset to each value in the secret key
offset = random.randint(1, q)
shuffled_secret_key = [(x + offset) % q for x in shuffled_secret_key]

# Save the secret key and offset
with open("secret_key.txt", "w") as f:
    f.write(f"secret_key = {shuffled_secret_key}\n")
    f.write(f"offset = {offset}\n")
    f.write(f"padding_length = {padding_length}\n")
    f.write(f"original_order = {original_order}\n")

print("Secret key, offset, and original order saved to secret_key.txt")
