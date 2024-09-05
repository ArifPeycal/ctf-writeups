# Novel reader 2
## Description
> Submit the second flag of “Novel Reader” here

## Challenge Overview

Same website as `Novel reader`where we have to read inside `private/A-Secret-Tale.txt`

## Solution
```python
buf = ' '.join(buf[0:session['words_balance']])+'... Charge your account to unlock more of the novel!'
```
We need to set `session['words_balance']` as negative value. This will cause the readNovel() code to read from buf[0:-1] meaning it will read from the start to the end of the file. 

## Flag
```
MAPNA{uhhh-y0u-607-m3-4641n-3f4b38571}
```
