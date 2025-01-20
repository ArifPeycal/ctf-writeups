# Lost Password
> I've already set up my web server, but I accidentally lost a Russian roulette from a Python script which then executed rm -rf / --no-preserve-root with root privileges. By the way, I also had a short-term lapse in memory and put my cloud account password inside the web folder. The last thing I remember is that I had a backup of my web folder and it was running a fresh installation of Nginx with no modifications yet. Please help me recover the password.
> 
> Author: vicevirus

## Overview
We were give a zip file that required a password, but there is no password provided. From the description, it is hinted that the password is inside `Nginx` web folder and it had no modifications. This challenge is similar to challenge from <a href="https://github.com/ArifPeycal/ABOH2023/tree/main/Crack%20Store">ABOH2023</a>.

We need to use the Biham and Kocher plaintext attack to crack the zip file, which is effective against ZIP files using the ZipCrypto Store compression method. `bkcrack` (https://github.com/kimci86/bkcrack/tree/master) can be used for password cracking. 

![image](https://github.com/user-attachments/assets/ace9f887-84b9-46bc-8378-3bf01226afb3)

In order to use this attack, it requires at least 12 bytes of known plaintext, with 8 bytes needing to be contiguous. We can see that there is index.html inside of `html.zip` which can be used as plaintext. Since `index.html` is default page of Nginx, we can go to `/usr/share/nginx/html/` to see its content. 

![image](https://github.com/user-attachments/assets/ee8efb17-c944-44ff-a991-1dff1002f98c)

We need at least 12 bytes for this attack, but for this case I used around 32 bytes. 
![image](https://github.com/user-attachments/assets/6424aff9-8aa0-4312-b72a-1b2d495fba75)

```bash
bkcrack -C html.zip -c index.html -x 0 3c21444f43545950452068746d6c3e0a3c68746d6c3e0a3c686561643e0a3c74
```
![image](https://github.com/user-attachments/assets/a14d1e86-d1dd-4ae5-bc68-6b84980fa20e)

After getting the key, we can create a zip file from the original zip, but now without any password.

```
bkcrack -C html.zip -c index.html -k 1d63e85a b3b66126 33619315 -D deciphered.zip
```

Unzip `deciphered.zip` and get the flag.

# Flag
```
EQCTF{bkkkkkcracckkkk_issss_useffulll_for_known_plaintextt}
```
