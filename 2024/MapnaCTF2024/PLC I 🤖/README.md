# PLC I 🤖
## Description
> The MAPNA CERT team has identified an intrusion into the plant’s PLCs, discovering a covert message transferred to the PLC. Can you uncover this secret message?
## Solution
We were given a pcap file to investigate. We can find the flag in the Ethernet trailer.

![image](https://github.com/user-attachments/assets/8e4b6f1c-b1c6-4db2-af9b-06d17ea23ca3)

- `3:Ld_4lW4` (Packet 19)

- `5:3__PaAD` (Packet 31)

- `1:MAPNA{y` (Packet 35)

- `4:yS__CaR` (Packet 39)

- `6:d1n9!!}` (Packet 46)

- `2:0U_sHOu` (Packet 50)

## Flag
```
MAPNA{y0U_sHOuLd_4lW4yS__CaR3__PaADd1n9!!}
```
