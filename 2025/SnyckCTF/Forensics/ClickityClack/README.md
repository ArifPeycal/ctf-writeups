# ClickityClack

> Author: @Soups71
> 
> My friend said that he kept trying to message me the flag but it wouldn't work. He sent me a packet capture of his USB Bus to prove he was typing the flag, can you help me figure out what the flag is?

## Solution
We were given a PCAP file that contains several USB packets. Immediately, I realised that this challenge needed us to decode the USB HID data either from a keyboard or a mouse. 

![image](https://github.com/user-attachments/assets/c99cc3ff-183d-4003-be9b-6dd1684f7e64)

In order to check it, we can use this filter in Wireshark:
```
usb.transfer_type == 2 && usb.endpoint_address.direction == 1 && usb.bDescriptorType == 4 && usb.bInterfaceClass == 3
```

We can see there are two sources of USB packets, from `7.2.0` and `7.3.0`. Under Interface Descriptor, we can see that USB packets from `7.3.0` is a keyboard meanwhile, the other one is mouse. Since the description mentioned about 'typing', the solution must be related to keyboard. 

![image](https://github.com/user-attachments/assets/a9a34c09-b471-4216-8ca5-aa9feea83d56)

### **Understanding HID Keyboard Report Format**
A standard HID keyboard report typically consists of the following bytes:

| Byte Index | Description                     |
|------------|---------------------------------|
| 0          | Modifier keys (Ctrl, Shift, Alt, etc.) |
| 1          | Reserved (Always 0)            |
| 2-7        | Keycodes (Up to 6 keys at once) |

**HID Data: `0000080001000000`**  
- `00` → Modifier keys (None pressed)  
- `00` → Reserved (Always 0)  
- `08` → First key pressed (Keycode `0x08`)  
- `00` → Second key (None)  
- `01` → Third key (Keycode `0x01`)  
- `00` → Fourth key (None)  
- `00` → Fifth key (None)  
- `00` → Sixth key (None)  

### **Keycode Interpretation**
According to **HID Usage Tables (USB HID Usage Tables 1.12, Section 10, "Keyboard/Keypad Page")**, `0x08` is equivalent to **"e" key**. Since there is no modifier like ALT or CAPS LOCK, the letter will be lowercase.

![image](https://github.com/user-attachments/assets/e1d6d87f-0ab5-4672-b45d-ee740a3ece91)

Use this tool to decode the HID data from PCAP. https://github.com/5h4rrk/CTF-Usb_Keyboard_Parser

```bash
python3 Usb_Keyboard_Parser.py click.pcapng
```
```
[-] Found Modifier in 10 packets [-]

[+] Using filter "usbhid.data" Retrived HID Data is :

aaaaacaaaaaaaaaabaaaaaababadaaaabaaaaaacaaaabaaaaaaadabbacbabccabcccabcgccccccgccdcdcgccdfccdccdfccddccfccfdbccaccbacbbcbbcbbbcbbcbbbbbcbbcbbcgbcbbbcbbbccbacbcbbbcbbcbbbbbbcbbafbbbababaaeabaaaaaaacaaaaaaaacaaaaaaeabaaaaaaabaaababbbbacbbabbbbbbbbbbbebbbabbbcbebbcbbcbbebbcacbbbbbfbbbcacbgcababbdbbdbababbabbcbbababbbaebabaabbbaeabbaababbabaebabbabbaeabaaabaaaabaabaabaaabaaaaebaaaaaaabacaabaaaaaaaaaaaaeaaaaaaaaaaaaaaaaaaaaaaacaaaaaaaaaaabaabaaafaabababbabaaaacaababaaacabaababbbbbbbebcbdcccccccfdceddceddcddefeeheeefeaeeeeiefeefefnefefeiefeeiefefefeeieefaeeeejeedfedhdedbdegddcdgdddcdcdacdfdccccdfcccbbbcbbbbbbbbbadaaaaaaaaaaflag{a3ce310e9a0dc53bc030847192e2f585}

↑↑Thhis iis a ppreetty ccool thhing tthatt I hhave ffigguredd ooutt.
Yoou can capturre thhe chharacteers yyouuu type in PCAPs.aa↑↑
mmmmmmmmmm↑↑
mmmmmmmmmm↑↑
mmmmmmmmmm↑↑
mmmmmmmmmm↑↑
mmmmmmmmmm↑↑
mmmmmmmmmmaaaaaaabdbaaaaaaaaabaaaaaa
```

## Flag
```
flag{a3ce310e9a0dc53bc030847192e2f585}
```
