# reader
## Description
> Salam jumaat @everyone, here jumaats challenge. It is privilege escalation based on CVE-2019-14287. Feel free to check it out :).
> 
> Privilege escalation is the process by which a user gains elevated access to resources that are normally protected from that user's standard capabilities. This can occur in two main forms:
> 
> Vertical Privilege Escalation: A lower-privileged user gains the permissions of a higher-privileged user, such as a regular user becoming an administrator.
> 
> Horizontal Privilege Escalation: A user gains the permissions of another user with the same privilege level, often to access information or resources they are not authorized to access.
> 
> Privilege escalation can happen due to system vulnerabilities, misconfigurations, or through exploitation of application bugs. It's a critical security issue as it can allow unauthorized users to compromise the entire system or network.
> 
> Creds : ssh ctf-player@ice-training.syamilyusof.com -p 2222 Password : verysecure
> 
> Flags Location : /root/flag.txt
> 
> ssh ctf-player@ice-training.syamilyusof.com -p 2222

## Challenge Overview
We were connected as `ctf-user` and we need to read file in `/root/flag.txt`. But, we cant access to `/root` directory (obviously). 

![image](https://github.com/user-attachments/assets/398cb797-9bb5-4fa8-aaa3-24f6aa157dc7)



## Solution
Intended solution is to do exploit based on `CVE-2019-14287`.

> CVE-2019-14287 is a security vulnerability in the `sudo` command that allows users to run commands with elevated privileges.

The issue arises when the sudoers configuration file allows a user to execute a command as another user, but the target user is specified as `-1` or `4294967295` (the unsigned representation of -1). In Unix systems, a user ID of `-1` or `4294967295` is interpreted as the UID `0`, which is the root user.

The command `sudo -l` used to show the commands a user is allowed (or not allowed) to execute as another user (usually root) without providing their password again. This means that `ctf-user` can run `base64` as any user except root.

![image](https://github.com/user-attachments/assets/a6ea9b60-6a5e-41e7-aed3-c16723e02548)

However, by running this command, we can run `base64` as root:
```bash
sudo -u#-1 /bin/base64
```
The `-1` is interpreted as UID `0` (root), so `ctf-user` is effectively running the command as the root user, even though it should not have this privilege.

Now, we can use `base64` to read flag file located at `/root` directory.

![image](https://github.com/user-attachments/assets/3e4a45a4-91a2-4111-9a29-903ac21cfb9f)

## Flag
```
ICE{th@nkfu11y_th1s_CVE_are_p@tch3d}
```
