# The Road of Redemption
> The key to redemption lies in the hands of those who know the deep secrets of the church. Do you have the courage to uncover them and find your way to the light?
>
> Hint:
> 
> Are you familiar with the Blowfish protocol? Analyze the DNS packets directed towards uctf.ir. Pay attention to the return paths.
>
> Make sure to pay attention to the different modes of encryption in Blowfish.
>
> tshark -r The-Road-of-Redemption.pcap -Y "dns.qry.name contains uctf.ir" -T fields -e dns.qry.name | uniq | sed 's/.uctf.ir//g' | tr -d '\n'

There are two HTTP endpoints, `/` and `/key`. 


`/` contains hex strings that can be rendered into an image. At the bottom of the image there is a string `Do you know Paul Mockapetris?`

![image](https://github.com/user-attachments/assets/7b372512-9977-4e43-8ba3-9881c83d6dc4)

`/key` contains a key, probably for Blowfish decryption. The key was encrypted in base64.

![image](https://github.com/user-attachments/assets/c86feab6-1f61-44e0-a88a-40a443053603)

```html
key : QXJhc1ZhbGxleV9NZWRpZXZhbFNocmluZV8xMjk3X3VjdGY=
decoded_key: ArasValley_MedievalShrine_1297_uctf
```
I tried run the command given and the output is in <a href="https://github.com/ArifPeycal/ctf-writeups/blob/main/2024/UrniaCTF2024/Forensics/The%20Road%20of%20Redemption/output.txt">output.txt</a>

Use CyberChef version 9.0, the newer version of CyberChef didn't give the result. 
![image](https://github.com/user-attachments/assets/babb0c39-96f3-4f19-a490-c312ff30e1bc)

![image](https://github.com/user-attachments/assets/385e9f27-6b71-4c67-a8b3-98a6b6b6a3f1)
