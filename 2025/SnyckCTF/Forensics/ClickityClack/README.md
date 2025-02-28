# ClickityClack

> Author: @Soups71
> 
> My friend said that he kept trying to message me the flag but it wouldn't work. He sent me a packet capture of his USB Bus to prove he was typing the flag, can you help me figure out what the flag is?

## Solution

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
