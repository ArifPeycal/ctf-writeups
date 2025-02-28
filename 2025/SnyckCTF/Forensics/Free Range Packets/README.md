# Free Range Packets
> Author: @Soups71
>
> My friend recently has decided to stop trusting WiFi, so he decided to send me information over Bluetooth. In order to prove that you can capture data from Bluetooth without being the intended recipient, I took this packet capture with a 2 dollar bluetooth adapter.
>
## Solution
Filter Bluetooth packets, the flag will be underthe  payload section. Iterate until the end of packets.
```
_ws.col.info == "Sent Connection oriented channel"
```
![image](https://github.com/user-attachments/assets/f09a1409-d194-4e4c-b4af-edb0ba788ce4)
