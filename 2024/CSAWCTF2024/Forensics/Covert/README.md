# Covert
## Description
> It appears there's been some shady communication going on in our network...
## Challenge Overview
We were given `keys.log` and `cchall.pcapng` to analyze. `chall.pcapng` conatains several TLS, ARP and QUIC IETF packets. And the `keys.log` contains some sort of communication handshake between server and client. By giving the log to ChatGPT, I found out that the log is `TLS traffic secret` specifically `TLSv1.3`. 

In recent versions, Wireshark supports decrypting `TLS 1.3` traffic, but only if it has access to these TLS traffic secrets. When you provide these secrets to Wireshark, it can use them to decrypt the encrypted communication between a client and a server, allowing you to analyze the data inside those packets (which is usually hidden when encrypted with TLS). 

### How to Use These Secrets in Wireshark:

- Go to Edit -> Preferences.

- Under Protocols, select TLS.

- In the (Pre)-Master-Secret log filename field, provide a path to a file that contains the traffic secrets.

![image](https://github.com/user-attachments/assets/685199fc-06b0-4d99-ad48-002958f20121)


After giving the secret log to Wireshark, we can see some HTTP/HTTP2 packets.

![image](https://github.com/user-attachments/assets/eefbbf2a-9c68-458a-9179-4c0239e4a172)

## Solution

We can start analyzing HTTP packets first by following HTTP stream. There is some Python script at Stream 2. 


This Python code leverages Scapy to create a covert channel by encoding a message into the IP header of TCP packets. The goal is to send a hidden message by encoding each character into the `IP.id` field of the IP packet

For each letter in the flag The ASCII value of the letter is calculated using ord(letter).
This ASCII value is multiplied by key to generate a new value, which is stored in the id field of the IP header. The `IP.id` field is typically used to identify IP packets, but here it is being repurposed for covert communication.

```py
<html><body>
    # ez covert transfer...
    from scapy.all import IP, TCP, send

    key = ??

    dst_ip = &#34;X.X.X.X&#34;
    dst_port = ?????

    src_ip = &#34;X.X.X.X&#34;
    src_port = ?????

    def encode_message(message):
        for letter in message:
            ip = IP(dst=dst_ip, src=src_ip, id=ord(letter)*key)

            tcp = TCP(sport=src_port, dport=dst_port)

            send(ip/tcp)

    encode_message(&#34;????????????&#34;)
        </body></html>
```
Filter out the `TCP` protocols and include `IP.id` as one of the columns. We can see that `IP.id` from `172.20.10.5` to `172.57.57.57` potentially becomes the flag since packet number `265` and `269` contain the same identification number (5445). Since the flag starts with letter "c", we can conclude that `ord('c')*key = 5445`. With some quick math, the key would be `55`.

![image](https://github.com/user-attachments/assets/d97ba92b-0684-4822-80a1-4f48fcc02011)

We created a Python script to extract `IP.id` from `172.20.10.5` to `172.57.57.57` and decode it using the key that we got. 

```py
from scapy.all import rdpcap, IP, TCP

key = 55

def decode_message(ip_ids, key):
    message = ''
    for ip_id in ip_ids:
        char = chr(ip_id // key)
        message += char
    return message

packets = rdpcap('chall.pcapng') 

ip_ids = []

for packet in packets:
    if IP in packet and TCP in packet:
        if packet[IP].src == "172.20.10.5" and packet[IP].dst == "172.57.57.57":
            ip_ids.append(packet[IP].id)

flag = decode_message(ip_ids, key)

print(f"Decoded flag: {flag}")

```
## Flag
```
csawctf{licen$e_t0_tr@nsmit_c0vertTCP$$$}
```
