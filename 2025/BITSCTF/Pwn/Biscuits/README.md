# Biscuits
> Momma, can I have cookie..?
>
> No....
>
> nc 20.244.40.210 6000
>
> d4y0n3

## Solution

```py
import time
from ctypes import CDLL
from pwn import *

libc = CDLL("libc.so.6")

HOST = "20.244.40.210"
PORT = 6000

cookies = ["Chocolate Chip", "Sugar Cookie", "Oatmeal Raisin", "Peanut Butter", "Snickerdoodle",
           "Shortbread", "Gingerbread", "Macaron", "Macaroon", "Biscotti",
           "Butter Cookie", "White Chocolate Macadamia Nut", "Double Chocolate Chip", "M&M Cookie", "Lemon Drop Cookie",
           "Coconut Cookie", "Almond Cookie", "Thumbprint Cookie", "Fortune Cookie", "Black and White Cookie",
           "Molasses Cookie", "Pumpkin Cookie", "Maple Cookie", "Espresso Cookie", "Red Velvet Cookie",
           "Funfetti Cookie", "S'mores Cookie", "Rocky Road Cookie", "Caramel Apple Cookie", "Banana Bread Cookie",
           "Zucchini Cookie", "Matcha Green Tea Cookie", "Chai Spice Cookie", "Lavender Shortbread", "Earl Grey Tea Cookie",
           "Pistachio Cookie", "Hazelnut Cookie", "Pecan Sandies", "Linzer Cookie", "Spritz Cookie",
           "Russian Tea Cake", "Anzac Biscuit", "Florentine Cookie", "Stroopwafel", "Alfajores",
           "Polvor", "Springerle", "Pfeffern", "Speculoos", "Kolaczki",
           "Rugelach", "Hamantaschen", "Mandelbrot", "Koulourakia", "Melomakarona",
           "Kourabiedes", "Pizzelle", "Amaretti", "Cantucci", "Savoiardi (Ladyfingers)",
           "Madeleine", "Palmier", "Tuile", "Langue de Chat", "Viennese Whirls",
           "Empire Biscuit", "Jammie Dodger", "Digestive Biscuit", "Hobnob", "Garibaldi Biscuit",
           "Bourbon Biscuit", "Custard Cream", "Ginger Nut", "Nice Biscuit", "Shortcake",
           "Jam Thumbprint", "Coconut Macaroon", "Chocolate Crinkle", "Pepparkakor", "Sandbakelse",
           "Krumkake", "Rosette Cookie", "Pinwheel Cookie", "Checkerboard Cookie", "Rainbow Cookie",
           "Mexican Wedding Cookie", "Snowball Cookie", "Cranberry Orange Cookie", "Pumpkin Spice Cookie", "Cinnamon Roll Cookie",
           "Chocolate Hazelnut Cookie", "Salted Caramel Cookie", "Toffee Crunch Cookie", "Brownie Cookie", "Cheesecake Cookie",
           "Key Lime Cookie", "Blueberry Lemon Cookie", "Raspberry Almond Cookie", "Strawberry Shortcake Cookie", "Neapolitan Cookie"]

# Step 1: Sync srand() with server
now = int(time.time())
libc.srand(now)

# Step 2: Predict first cookie
first_cookie_index = libc.rand() % 100
first_cookie = cookies[first_cookie_index]

print(f"[+] Predicting First Cookie: {first_cookie}")

# Step 3: Connect to server
p = remote(HOST, PORT)
print("[+] Connected to", HOST)

# Step 4: Read welcome message
server_msg = p.recv(timeout=5).decode(errors="ignore")
print("[DEBUG] Full Server Response:\n", server_msg)

# Step 5: Send first correct cookie
p.sendline(first_cookie.encode())

# Step 6: Loop through 100 rounds
for i in range(99):  # 1 already sent, 99 left
    response = p.recv(timeout=5).decode(errors="ignore")
    print(f"[DEBUG] Server Response:\n{response}")

    if "Wrong" in response:
        print("[!] Failed! Incorrect guess.")
        break
    if "Congrats!" in response:
        print("[+] FLAG:", response)
        break

    # Generate the next cookie
    next_cookie_index = libc.rand() % 100
    next_cookie = cookies[next_cookie_index]
    print(f"[+] Sending cookie [{next_cookie_index}]: {next_cookie}")
    p.sendline(next_cookie.encode())

flag = p.recv(timeout=5).decode(errors="ignore")
if flag:
    print("[+] FLAG:", flag)

p.close()

```
## Flag
```
BITSCTF{7h4nk5_f0r_4ll_0f_th3_c00ki3s_1_r34lly_enjoy3d_th3m_d31fa51e}
```
