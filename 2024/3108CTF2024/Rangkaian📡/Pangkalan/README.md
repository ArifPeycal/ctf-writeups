# Pangkalan 📡
## Description
> Kami menerima transmisi dari pangkalan port pulau pinang bernombor 55663. Mohon segera untuk memberi bantuan.

## Challenge Overview
3108{mikealphalimabravoalphatangotango}
```
tshark -r transmisi_rahsia.pcap -Y "tcp.dstport == 55663" -T fields -e data > extracted_data.txt
```
## Flag
```
3108{malbatt}
```
