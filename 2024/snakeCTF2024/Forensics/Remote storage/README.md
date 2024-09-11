# Remote storage
## Description
> All my homies hate cloud storage.

## Challenge Overview
We were given `capture.pcap` to analyze. We can see big portion of iCSCI packets. Since it is my first time seiing this protocol, I want to know what it does.

> iSCSI (Internet Small Computer Systems Interface) is an Internet Protocol (IP)-based storage networking standard that allows data transfer over IP networks. It is used to link data storage facilities, such as storage area networks (SANs), and enables clients (initiators) to access remote storage devices  as if they were locally attached.

![image](https://github.com/user-attachments/assets/1a2d46ae-1126-44ec-b82f-5b4a1a81e964)

## Solution
Filter iSCI and follow `TCP` stream. There is base64 encoded string after `dont_open_me.txt`.

![image](https://github.com/user-attachments/assets/efff7221-a3d7-4a1d-90c9-959b89781561)
# Flag
```
snakeCTF{st0rag3_0ver_tcp_d9547163fc4c8868}
```
