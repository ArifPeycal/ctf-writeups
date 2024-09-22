# Simple Exfiltration
## Description
> We've got some reports about information being sent out of our network. Can you figure out what message was sent out.

## Challenge Overview

We were given `exfiltration_activity_pctf_challenge.pcapng` to analyze. From `Protocol Hierarchy`, we can see a huge percentage of HTTP packets. We can start with that first.

![image](https://github.com/user-attachments/assets/002990d7-bff1-4b34-b935-718ff0d1272a)

Unfortunately, all the packets are just the same. I tried to look into the ports but no solution. 

![image](https://github.com/user-attachments/assets/3cd3cdcb-dcc9-4752-926f-54355e60b206)

```
GET / HTTP/1.1
Accept-Encoding: identity
Host: 192.168.237.1:52301
User-Agent: Python-urllib/3.11
Connection: close

HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.11.1
Date: Thu, 04 Jul 2024 15:37:15 GMT
Content-type: text/html; charset=utf-8
Content-Length: 187

<!DOCTYPE HTML>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Directory listing for /</title>
</head>
<body>
<h1>Directory listing for /</h1>
<hr>
<ul>
</ul>
<hr>
</body>
</html>
```

## Solution

There were some ICMP packets with the same IP identification number. When investigating further, Time-to-Live contains decimal numbers that can be interpreted as ASCII value. 

![image](https://github.com/user-attachments/assets/cebb30d3-16fe-427a-bde4-fc90da79abe4)

So, we can create a Python script that extract the TTL value. 

```py
from scapy.all import rdpcap, IP, ICMP

pcap_file = 'exfiltration_activity_pctf_challenge.pcapng'

packets = rdpcap(pcap_file)

ttl_values = []

for packet in packets:
    if IP in packet and ICMP in packet:
        if packet[IP].src == "192.168.237.132":
            ttl_ascii = chr(packet[IP].ttl) if 32 <= packet[IP].ttl <= 126 else ''
            ttl_values.append(ttl_ascii)

ttl_string = ''.join(ttl_values)

print(f"Extracted TTL string: {ttl_string}")

```
## Flag
```
pctf{time_to_live_exfiltration}
```
