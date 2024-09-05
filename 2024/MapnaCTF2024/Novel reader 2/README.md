
```python
@app.post('/api/charge')
def buyWord():
    nwords = request.args.get('nwords')
    if(nwords):
        nwords = int(nwords[:10])
        price = nwords * 10
        if(price <= session['credit']):
            session['credit'] -= price
            session['words_balance'] += nwords
            return {'success': True, 'msg': 'Added to your account!'}
        return {'success': False, 'msg': 'Not enough credit.'}, 402
    else:
        return {'success': False, 'msg': 'Missing parameteres.'}, 400
```
This will cause the readNovel() code to read from buf[0:-1] meaning it will read from the start to the end of the file. 
```
buf = ' '.join(buf[0:session['words_balance']])+'... Charge your account to unlock more of the novel!'
```
```MAPNA{uhhh-y0u-607-m3-4641n-3f4b38571}```
