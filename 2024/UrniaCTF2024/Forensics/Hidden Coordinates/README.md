# Hidden Coordinates

## Description
> Jack Sparrow may be searching for treasure, but he’ll never find the map if he can't decipher the signals. Buried within a seemingly ordinary pcap file are hidden details encoded in ICMP packets. Unearth the secrets concealed in these packets to reveal the flag.

## Challenge Description
We were given `plan.pcapng` to analyze. The challenge description gives a hint to search for flag in `ICMP` packets. 

![image](https://github.com/user-attachments/assets/3821f396-965b-4773-904b-7a7432b0633a)


## Solution
Upon inspection, we can see ICMP packets with the same `IP Identification` number (0x00001). The `ip.src` is `192.168.1.50` and `ip.dst` is `192.168.1.1`.

![image](https://github.com/user-attachments/assets/f45697f2-b2eb-451c-a7e5-42946d47fb51)

If we look further in the `IP` headers, we can see some pattern in `Time-To-Live (TTL)` header. TTL value is the ASCII number of the flag, starting with `u` (117). We can create a Python script that extract this value and convert it to string.

```py
from scapy.all import rdpcap, IP, ICMP
packets = rdpcap("plan.pcapng")

extracted_chars = []

for packet in packets:
    if packet.haslayer(IP) and packet.haslayer(ICMP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        ttl = packet[IP].ttl
        
        if src_ip == "192.168.1.50" and dst_ip == "192.168.1.1":
            char = chr(ttl)  
            extracted_chars.append(char)  

flag = ''.join(extracted_chars)

print(f"Extracted Flag: {flag}")
```
## Flag
```
uctf{Iran_K4run_River}
```
