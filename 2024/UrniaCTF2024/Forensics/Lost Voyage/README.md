# Lost Voyage
## Description
> Curse those pirates! I should've taken better precautions to hide my travel plans. The secret is now out there, but it's still within reach—if you know where to look. Remember, the answer lies within uctf{}...

## Challenge Description
We were give `Alice.pcapng` to analyze. We found several common protocols inside the `pcap` file such as `TCP`, `ICMP` and `DNS`. But, there is one protocol that is quite interesting due to percentage of bytes which is `Real-Time Transport Protocol`.

> RTP (Real-time Transport Protocol) is a network protocol used for delivering audio and video over IP networks in real time. It is widely used in streaming media, telephony (VoIP), video conferencing, and other real-time multimedia applications.
 
![image](https://github.com/user-attachments/assets/4ce73579-badb-448c-9889-876585dcb31f)

Filter the `RTP` packets and we can see the audio being transported.

![image](https://github.com/user-attachments/assets/c4e2c79d-47e5-4822-8dec-7cd790d77edc)

## Solution

So, we need to find a way to listen to the audio. I found out <a href="https://support.yeastar.com/hc/en-us/articles/360007606533-How-to-Analyze-SIP-Calls-in-Wireshark"> this page </a> where it shows how to listen to the `RTP` stream.

### How to Play RTP Stream: 
- Use 'rtp' as the expression to filter RTP packets.
- Use the menu 'Telephony > RTP > RTP Streams'.
-  Select and Play Stream in the call list

Listen to the audio and we get the flag.

![image](https://github.com/user-attachments/assets/24185b13-5a6f-4b05-8cf5-1c47f6e2599b)

## Flag
```
uctf{iran_lut_desert}
```
