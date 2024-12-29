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

### Inspecting SMB Packets
Upon opening the PCAP file in Wireshark, we identified several encrypted SMB packets. 

![image](https://github.com/user-attachments/assets/e578dd9e-8f89-450b-9da2-ae4684cb7677)

By following a TCP stream, the presence of "NTLM 0.12" and "SMB 2.002" confirmed that NTLM authentication was used over the SMB protocol.

![image](https://github.com/user-attachments/assets/55b1e2a0-cdaf-4b29-8766-53e3014e6ad6)

---

### Extracting NTLM Hashes
We used the `NTLMRawUnhide.py` script from https://github.com/mlgualtieri/NTLMRawUnHide to extract NTLM hashes from the PCAP file:

```bash
python3 NTLMRawUnhide.py -i capture.pcap -o hash.txt
```

**Output:**
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
```
Each line in the dump consists of:
- **Username:** `Administrator`
- **Machine Name:** `DESKTOP-PMNU0JK`
- **LM Hash**
- **NTLM Hash**
- **Additional Data**

---

### Cracking NTLM Hashes
Using `hashcat`, we decrypted the NTLM hashes:

```bash
hashcat -m 5600 -a 0 hash.txt /usr/share/dirbuster/wordlists/rockyou.txt
```

**Password Found:** `password<3`

---

### Decrypting SMB Packets

In order to decrypt SMB packets, we need to have Session ID and Session Key. 

![image](https://github.com/user-attachments/assets/9b8b6c84-5c67-4404-959d-605045f72da1)

To find Session ID,use ntlmssp filter in Wireshark and look up for Session Setup Request packet. The Session ID is under SMB2 Header.

![image](https://github.com/user-attachments/assets/4a25edaa-f723-4497-838c-13db51d991fa)

We also found the Session Key in the same packet.

![image](https://github.com/user-attachments/assets/51759f1a-bd3f-4543-b03d-f9caffa69116)

But if you enter the Session Key and Session ID, the SMB packets still not decrypt yet. It is because the Session Key from PCAP file is Encrypted Session Key. We need to calculate Random Session Key in order to decrypt properly.

![image](https://github.com/user-attachments/assets/11433eae-6610-4d35-b018-2a98b4830751)

*Random Session Key and Encrypted Session Key in SMB*
1. **Encrypted Session Key**: This is a key generated during the NTLM authentication process. It is encrypted using the Key Exchange Key and is used to protect the session setup and key exchange process.
2.**Random Session Key**: Decrypted version of the Encrypted Session Key. Once decrypted, it is used to encrypt and decrypt the actual SMB session data (such as file requests and responses). 

To calculate Random Session Key, we can use script from https://medium.com/maverislabs/decrypting-smb3-traffic-with-just-a-pcap-absolutely-maybe-712ed23ff6a2. We needed:
1. **Username**
2. **Domain**
3. **Password**
4. **NTProofStr**
5. **Encrypted Session Key**

The NTProofStr and Encrypted Session Key were extracted from an NTLMv2 Session Setup Request packet (same as Session ID). These were copied as a hex stream.

NTProofStr = `ae62a57caaa5dd94b68def8fb1c192f3`

![image](https://github.com/user-attachments/assets/81497142-2437-45c0-b4e3-f7fd73c3d03f)

Encrypted Session Key = `12140eb776cb74a339c9c75b152c52fd`

![image](https://github.com/user-attachments/assets/51759f1a-bd3f-4543-b03d-f9caffa69116)

Download the Python script from <a href="https://medium.com/maverislabs/decrypting-smb3-traffic-with-just-a-pcap-absolutely-maybe-712ed23ff6a2">here</a> and include the parameter. 
```bash
python3 ntlm.py -u Administrator -d DESKTOP-PMNU0JK -p password<3 -n ae62a57caaa5dd94b68def8fb1c192f3 -k 12140eb776cb74a339c9c75b152c52fd
```
**Output:**
```
Random Session Key: 4147454a48564a4373437649574e504c
```

Now we have our Random Session Key for decryption. 

### Configuring Wireshark

To decrypt SMB traffic:
1. Navigate to `Edit` -> `Preferences` -> `Protocols` -> `SMBv2`.
2. Enter the **Session ID** (from the Session Setup Request packet).
3. Enter the **Random Session Key**.

![image](https://github.com/user-attachments/assets/575ac9cb-fad4-492a-8a69-7b12846c90aa)

After configuration, the SMB packets were decrypted successfully.

![image](https://github.com/user-attachments/assets/3df36a46-8a10-4f21-9045-115cf36026e8)

---

### Exporting Files
The decrypted SMB packets contained file requests. Using `Export Objects` in Wireshark, we exported the files.

![image](https://github.com/user-attachments/assets/8e9f6e5a-2770-4081-a1b3-0ad111c98670)

- **File:** `nano.exe` (Flagged as malicious, identified as a `lsassdump` executable).
  ![image](https://github.com/user-attachments/assets/28328ad7-53ff-41f3-b895-c3266eccf6f3)

- **File:** `20241225_1939.log` (Minidump file containing secrets).
- **File:** `RxHmEj` (Contains hint for next step, stated that the log file has invalid signature and we can restore it by using `scripts/restore_signature 20241225_1939.log`) 
```
The minidump has an invalid signature, restore it running:
scripts/restore_signature 20241225_1939.log
Done, to get the secretz run:
python3 -m pypykatz lsa minidump 20241225_1939.log
```
---

### Restoring and Analyzing the Minidump
Since we dont know where is the script for restoring signature, we tried to search Google for the script. Luckily, we found it and used the `restore_signature` script from the [nanodump repository](https://github.com/fortra/nanodump):

```bash
git clone https://github.com/fortra/nanodump.git
cd nanodump
scripts/restore_signature ../20241225_1939.log
```
![image](https://github.com/user-attachments/assets/37fd8eba-aa0d-40f8-a2b9-d3d3b4da13b6)

Next, we used `pypykatz` to extract secrets from the minidump:

```bash
python3 -m pypykatz lsa minidump ../20241225_1939.log
```

**Output:**

![image](https://github.com/user-attachments/assets/26d1d95b-3612-44d5-9319-2fd576fa1207)

---

### Final Flag
```
wgmy{fbba48bee397414246f864fe4d2925e4}
```

