# bad packets
## Description
> Our SOC says that there seem to be some curious activities within one of our servers. They provided a pcap file but I can't find what they're talking about.
## Challenge Overview
We were given a pcap file called `chall.pcap`. First of all, I tried to look into Protocol Hirerechy to see what are the contents of the packet file. We can see that there are a lot of TCP packets which consists of several HTTP packets. We'll look into that first.

There are two endpoints which are `/` and `/images`. 

![image](https://github.com/user-attachments/assets/fad06550-59cb-4bab-a281-3665cb6255c3)

When we follow the HTTP stream, we see that the HTML contents are obfuscated. 

![image](https://github.com/user-attachments/assets/0fd4497d-3304-49dd-bb93-fa390676292c)

Trying to export the HTML and open it in a browser. It is the front page of a Google Search.

![image](https://github.com/user-attachments/assets/016f3906-56bd-4d50-8059-c5c209682eb1)

The traffic activity can be recognised as TrevorC2 framework. 
> TrevorC2 is a client/server model for masking command and control through a normally browsable website. Detection becomes much harder as time intervals are different and does not use POST requests for data exfil.

### How to Identify TrevorC2
1. User-Agent: Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko
2. URLpath
   - http(s)://[C2_IP]/
   - http(s)://[C2_IP]/images?guid=[Encrypted_Base64_String]
3. Response header : “Server : IIS”
4. Default Cookie : “sessionid”
5. Default STUB inside the cloned page : “oldcss=”

References:
https://nasbench.medium.com/understanding-detecting-c2-frameworks-trevorc2-2a9ce6f1f425

## Solution
Use this script from <a href="https://github.com/Abdelrahme/Trevorc2_decrypt/blob/main/trevorc2_decrypt.py">Github</a> to decrypt the `oldcss` content. 

```
python3 trevorc2_decrypt.py -i chall.pcap
```
We can see the decrypted client and server response of TrevorC2.
![image](https://github.com/user-attachments/assets/a0dbed5b-0ed3-43b5-be41-ca28ff35dcd4)

## Flag
```
CSCTF{chang3_y0ur_variab13s_b3for3_d3pl0ying}
```
