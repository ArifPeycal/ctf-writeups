# Seniman Agung

> "Di sebalik kehebatan filem-filem P. Ramlee, ada satu rahsia tersembunyi yang hanya peminat tegar mampu temui. Laman web penghormatan ini kelihatan biasa sahaja, tetapi seni dan nostalgia yang terpampang sebenarnya menyimpan sesuatu yang bernilai. Adakah anda mampu menghayati karya agung beliau dan membongkar rahsianya?"

## Solution
We were given a website that allows us to query blogs but the catch is only 4 chars allowed, not more not less. Querying `3108` gives us a blog that hints about flag, but it has been censored. 

<img width="1303" height="635" alt="image" src="https://github.com/user-attachments/assets/52d621ce-f2ba-42c2-8af3-c5a87d325fda" />

When you query `108{`, it will still show the flag post, so this should be `Blind SQLi` where you need to iterate all possible chars and numbers until you get all the flag. Reminder that you can only query 4 chars at one time. You can use Burpsuite Intruder or create own script.

## Flag
```
3108{Buj4ng_l4p0k_ (tak ingat flag :( )
```
