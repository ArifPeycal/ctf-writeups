# Oh Man
## Description
> We received a PCAP file from an admin who suspects an attacker exfiltrated sensitive data. Can you analyze the PCAP file and uncover what was stolen?
>
> Zip Password: wgmy
> 
> Author: h0j3n
> 
> View Hint
> Investigate the tool used by the attacker

## Solution
We see several encrypted SMB packets.  
![image](https://github.com/user-attachments/assets/e578dd9e-8f89-450b-9da2-ae4684cb7677)

When you follow a TCP stream in Wireshark and see "NTLM 0.12" and "SMB 2.002," it indicates that there is network communication involving the NTLM authentication protocol over an SMB (Server Message Block) connection

![image](https://github.com/user-attachments/assets/55b1e2a0-cdaf-4b29-8766-53e3014e6ad6)

We need to extract NTLM hages from the pcap file. 
```py
python3 NTLMRawUnhide.py -i capture.pcap -o hash.txt
```
Output: 

This is a captured NTLM authentication hash from an SMB (Server Message Block) negotiation, specifically an NTLMv2 hash.

```
Administrator::DESKTOP-PMNU0JK:7aaff6ea26301fc3:ae62a57caaa5dd94b68def8fb1c192f3:01010000000000008675779b2e57db01376f686e57504d770000000002001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0001001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0004001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0003001e004400450053004b0054004f0050002d0050004d004e00550030004a004b00070008008675779b2e57db010900280063006900660073002f004400450053004b0054004f0050002d0050004d004e00550030004a004b000000000000000000
Administrator::DESKTOP-PMNU0JK:a1adc9d0bfe2c7c1:d43050f791ffabb9000c94bc5261ec52:0101000000000000fffb809b2e57db015569395a4c546b720000000002001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0001001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0004001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0003001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0007000800fffb809b2e57db010900280063006900660073002f004400450053004b0054004f0050002d0050004d004e00550030004a004b000000000000000000
Administrator::DESKTOP-PMNU0JK:e9cc7c3171bb95b9:4dd18b7e39dfe0538da53182e84a2f7c:010100000000000035878a9b2e57db0179363032797135620000000002001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0001001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0004001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0003001e004400450053004b0054004f0050002d0050004d004e00550030004a004b000700080035878a9b2e57db010900280063006900660073002f004400450053004b0054004f0050002d0050004d004e00550030004a004b000000000000000000
Administrator::DESKTOP-PMNU0JK:ce1e228fd442539e:f1de649eca87cd4430df45334ede036b:0101000000000000c312949b2e57db01514b36414d6e6b6f0000000002001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0001001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0004001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0003001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0007000800c312949b2e57db010900280063006900660073002f004400450053004b0054004f0050002d0050004d004e00550030004a004b000000000000000000
Administrator::DESKTOP-PMNU0JK:87c2136c9e0cfc7c:6035de8eeaaccc30c4d0cf61c2ff1857:0101000000000000e3479b9b2e57db015630475a6e64616a0000000002001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0001001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0004001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0003001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0007000800e3479b9b2e57db010900280063006900660073002f004400450053004b0054004f0050002d0050004d004e00550030004a004b000000000000000000
Administrator::DESKTOP-PMNU0JK:ad2f8a3f8191cfd6:d3b84a34cd713b950bae5dd8a9fb1523:0101000000000000e68df29c2e57db01436a6e6a5a5763420000000002001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0001001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0004001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0003001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0007000800e68df29c2e57db010900280063006900660073002f004400450053004b0054004f0050002d0050004d004e00550030004a004b000000000000000000
Administrator::DESKTOP-PMNU0JK:e3badcd0e2b0bde3:e840e74381ba416e3388006dce09a68d:0101000000000000cb78fe9c2e57db0134436f45673271510000000002001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0001001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0004001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0003001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0007000800cb78fe9c2e57db010900280063006900660073002f004400450053004b0054004f0050002d0050004d004e00550030004a004b000000000000000000
Administrator::DESKTOP-PMNU0JK:fec80d9eb9c0249b:7e3b131e980a621eddb57dd19c7565ba:0101000000000000c303089d2e57db0163597878514a54790000000002001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0001001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0004001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0003001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0007000800c303089d2e57db010900280063006900660073002f004400450053004b0054004f0050002d0050004d004e00550030004a004b000000000000000000
Administrator::DESKTOP-PMNU0JK:fd50cb1c5db59df1:e0e5937fef061d32f900e88d4d646b31:0101000000000000bf390f9d2e57db0159584666475750510000000002001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0001001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0004001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0003001e004400450053004b0054004f0050002d0050004d004e00550030004a004b0007000800bf390f9d2e57db010900280063006900660073002f004400450053004b0054004f0050002d0050004d004e00550030004a004b000000000000000000
````

Each line in your dump consists of four parts:

1. Username: `Administrator`
2. Machine Name: `DESKTOP-PMNU0JK`
3. LM Hash: The second part after the colon (e.g., `7aaff6ea26301fc3`)
4. NTLM Hash: The third part after the colon (e.g., `ae62a57caaa5dd94b68def8fb1c192f3`)
5. Additional Data: The last part seems to contain additional data related to the Windows domain and other user-specific information.

```
<username>::<machine_name>:<LM_Hash>:<NTLM_hash>:<additional_data>
```

We can use hash cat tod ecrypt teh NTLM. 

```bash
hashcat -m 5600 -a 0 hash.txt /usr/share/dirbuster/wordlists/rockyou.txt
```
The password is password<3
```
ADMINISTRATOR::DESKTOP-PMNU0JK:<NTLH Hash>:password<3
```
![image](https://github.com/user-attachments/assets/bb55559f-e181-46fc-834d-c7b0a83e3c61)

In order to decrypt the SMB packets, we need to have session id and session key.

![image](https://github.com/user-attachments/assets/9b8b6c84-5c67-4404-959d-605045f72da1)

 how to calculate the needed Random Session Key. Provided the following, the Random Session Key could be calculated:

-User’s password or NTLM hash
-User’s domain
-User’s username
-NTProofStr
-Key Exchange Key (Also known as the NTLMv2 Session Base Key)
-Encrypted Session Key

Most of what was required did not need computation and was provided clearly in the PCAP (domain, username, NTProofStr, and Encrypted Session Key). The other promising news is that the Key Exchange Key could be computed with knowledge of the password and/or hash of the user.

We alraady found sername, domain and password from previous NTLM Hash dump. 

In order to find -NTProofStr and -Key Exchange Key, we need to filteer ntlssp traffic. You can find it in one of the Session Setup Request packet specifically inside NTLMv2 field. Remember to copy as hex stream. 

![image](https://github.com/user-attachments/assets/81497142-2437-45c0-b4e3-f7fd73c3d03f)

Sssion key also in the same packet. 

![image](https://github.com/user-attachments/assets/51759f1a-bd3f-4543-b03d-f9caffa69116)

I refer script from this Medium blog. https://medium.com/maverislabs/decrypting-smb3-traffic-with-just-a-pcap-absolutely-maybe-712ed23ff6a2

```
python3 ntlm.py -u Administrator -d DESKTOP-PMNU0JK -p password<3 -n ae62a57caaa5dd94b68def8fb1c192f3 -k 12140eb776cb74a339c9c75b152c52fd
# Random SK: 4147454a48564a4373437649574e504c
```

Now we have Random Sesion Key, we need to find sessionn id to decrypt SMB packets. Luckily Ssession ID also in the same acket as Session Key and NTPProofSTR
65000000000c0000
![image](https://github.com/user-attachments/assets/4a25edaa-f723-4497-838c-13db51d991fa)


Goto Edir -> Preferneces -> Protocol -> SMBv2, inser session id (make sure copy as hex stream) and random ession key. 

![image](https://github.com/user-attachments/assets/575ac9cb-fad4-492a-8a69-7b12846c90aa)

You will see decrypted SMB packets, there are several reuest for files. 
![image](https://github.com/user-attachments/assets/3df36a46-8a10-4f21-9045-115cf36026e8)

We can export those file using Export Objects.
![image](https://github.com/user-attachments/assets/8e9f6e5a-2770-4081-a1b3-0ad111c98670)

nano.exe flagged as malicious, turnso ut it is a lsassdump executable fiel. 
![image](https://github.com/user-attachments/assets/28328ad7-53ff-41f3-b895-c3266eccf6f3)


`RxHmEj` contains hint for next step. Looks like 20241225_1939.log is a minidump file and we can use pypykatz to get secret. But the log file has invalid signature and we can resyotr by using `scripts/restore_signature 20241225_1939.log`.
```
The minidump has an invalid signature, restore it running:
scripts/restore_signature 20241225_1939.log
Done, to get the secretz run:
python3 -m pypykatz lsa minidump 20241225_1939.log
```

So i wonder eher is the restore_sognature script. simple seacrh will give ypu github page https://github.com/fortra/nanodump. 
```
git clone https://github.com/fortra/nanodump.git
cd nanodump
```
Run the ccript
```
scripts/restore_signature ../20241225_1939.log
```
![image](https://github.com/user-attachments/assets/37fd8eba-aa0d-40f8-a2b9-d3d3b4da13b6)

Run pypykatz
```
python3 -m pypykatz lsa minidump ../20241225_1939.log
```

![image](https://github.com/user-attachments/assets/26d1d95b-3612-44d5-9319-2fd576fa1207)


## Flag 
wgmy{fbba48bee397414246f864fe4d2925e4}
