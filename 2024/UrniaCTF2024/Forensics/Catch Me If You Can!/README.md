# Catch Me If You Can!

## Description
> In the bustling bazaars of ancient Persia, where merchants traded silk and spices, a secret message has been intercepted. Legend has it that this message holds the key to discovering the whereabouts of a hidden treasure deep within the ancient emperor of Persia. However, the message has been cunningly encrypted and is hidden within a sea of network traffic. Can you decode it before the secret slips through your fingers?
> 
> Reminder: Remember to submit the flag in this format: UCTF{flag}

## Challenge Overview
We were given `capture.pcap` to analyze. We can see that HTTP contains the most percentage of bytes so we can start analyzing HTTP packets.

![image](https://github.com/user-attachments/assets/29c4df42-d5fc-45ae-95f6-e3c8b7cff635)

## Solution

Follow the HTTP stream and we can see a long hex string on `<p>` tag. 
![image](https://github.com/user-attachments/assets/8d6febfa-ce35-4c3b-b8c5-87cfe231bbd0)

Send it to CyberChef and convert it from hex. We can see that it is a PNG file. There is an encrypted string on the bottom right of the image. 

![image](https://github.com/user-attachments/assets/bee99243-f5d8-40e0-a2d7-b345fd30cd96)

```
Xefvmd_Kverh_Fedeev
```
The picture of salad suggests that this is `Caesar Cipher`. CyberChef allows us to use `ROT13 Bruteforce` for the decryption. You can also use `Caeser Cipher Decoder` from <a href="https://www.dcode.fr/caesar-cipher">dcode</a>.

## Flag
```
UCTF{Tabriz_Grand_Bazaar}
```
