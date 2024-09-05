
# Hidden Discord

In this challenge, we were provided with a Discord link. Within the Discord server, the goal was to find different parts of a flag hidden across various locations.
![image](https://github.com/ReikuzoSennin/CTF-Writeups/blob/main/assets/discord1.png)

The first part was discovered in the voice channel chat.


![image](https://github.com/ReikuzoSennin/CTF-Writeups/blob/main/assets/discord2.PNG)

The second part was concealed in a hidden channel. To access it, I used the ShowHiddenChannels plugin with BetterDiscord. Once installed, the hidden channels became visible, revealing parts 2 and 4 of the flag.

![image](https://github.com/ReikuzoSennin/CTF-Writeups/blob/main/assets/discord3.PNG)

Part 3 was easy to spot, as it was located in the event description.


![image](https://github.com/ReikuzoSennin/CTF-Writeups/blob/main/assets/discord4.PNG)

For the final part, the hint pointed to the server icon. The image was initially too small to read, so I manipulated the size parameter in the URL to enlarge it, making the text legible.
![image](https://github.com/ReikuzoSennin/CTF-Writeups/blob/main/assets/discord5.PNG)

Flag: 
```RWSC{r34d_d15c0rd_d3v3l0p3r_API_r3f3r3nc3}```
