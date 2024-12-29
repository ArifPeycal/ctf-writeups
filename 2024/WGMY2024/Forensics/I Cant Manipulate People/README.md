# I Cant Manipulate People
## Description
> Partial traffic packet captured from hacked machine, can you analyze the provided pcap file to extract the message from the packet perhaps by reading the packet data?
>
> Author: Ap0k4L1p5
>
> Unlock Hint for 0 points
> Attacker too noob to ping not in sequence

## First Blood!
![image](https://github.com/user-attachments/assets/c6d9471b-9a3c-4cde-8aa5-2a915e23f1eb)

## Solution

Since it is hinted in the title about ICMP (first letter of each word), we can filter the packets that have ICMP protocols.

![image](https://github.com/user-attachments/assets/443cc68d-a5f5-4488-8403-d70e2ad94ceb)

If you look closely at the data, you can found ASCII number for the flag starting from 57 (W in ASCII).

![image](https://github.com/user-attachments/assets/9510a2fa-f6b5-4204-87c0-892e0d8ce48e)

Create a script to extract data from each ICMP packets.

```python
from scapy.all import rdpcap, ICMP, IP

def extract_icmp_from_pcap(pcap_file):
    try:
        packets = rdpcap(pcap_file) 
        icmp_packets = [pkt for pkt in packets if ICMP in pkt and pkt[IP].src == "192.168.68.117"]

        if not icmp_packets:
            print("No ICMP packets found in the PCAP file from source 192.168.68.117.")
            return

        print(f"Found {len(icmp_packets)} ICMP packet(s) from source 192.168.68.117:\n")

        combined_data = "".join([bytes(packet[ICMP].payload).decode(errors="ignore") for packet in icmp_packets])
        print("Combined Data:")
        print(combined_data)

    except FileNotFoundError:
        print("Error: File not found. Please provide a valid PCAP file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    pcap_file_path = "traffic.pcap"
    extract_icmp_from_pcap(pcap_file_path)
```

## Flag
```
WGMY{1e3b71d57e466ab71b43c2641a4b34f4}
```


