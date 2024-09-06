# Espionage
## Description
> In the world of digital espionage, intelligence is the most valuable currency. A high-profile hacker group has intercepted confidential communication from a top-secret government network. Your mission, should you choose to accept it, is to sift through the captured network traffic in a pcap file to uncover the hidden password. The fate of classified information rests in your hands. Analyze the packets carefully; the adversaries are clever, and the password is well-concealed within the data stream. Can you crack the code before time runs out? <br>
>
> Format : CyGenixCTF{Password_here}

## Solution
- Open ```Wireshark``` -> ```Statistics``` -> ```Protocol Hierarchy``` -> ```TCP```
- Follow TCP stream (stream 3)
- pswrd=UEFwZHNqUlRhZQ%3D%3D
- URL Decode and Base64, we get the password as ```PApdsjRTae```

## Flag
```CyGenixCTF{PApdsjRTae}```
