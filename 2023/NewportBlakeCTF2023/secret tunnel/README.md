# secret tunnel

## Website Link
https://secret-tunnel.chal.nbctf.com/

## Solution
From the source code files, we understand that there are 2 ports available, port ```80``` is for main and port ```1337``` for flag. So we need to access ```/flag``` at port ```1337```.

However, there are some restrictions in the URL:
* No "127" is present in the URL.
* Count of dots in the URL must be less than 2.
* No character "x" is present in the URL.
* No "flag" is present in the URL.

```python
@app.route("/fetchdata", methods=["POST"])
def fetchdata():
    url = request.form["url"]

    if "127" in url:
        return Response("No loopback for you!", mimetype="text/plain")
    if url.count('.') > 2:
        return Response("Only 2 dots allowed!", mimetype="text/plain")
    if "x" in url:
        return Response("I don't like twitter >:(" , mimetype="text/plain") 
    if "flag" in url:
        return Response("It's not gonna be that easy :)", mimetype="text/plain")

```

We can bypass the restriction using ```http://localhost:1337/%66lag```
* localhost instead of 127.0.0.0. (http://0:1337 is also valid)
* /%66lag instead of /flag (use URL encode for letter 'f' which is %66)

## Flag 
The flag for this challenge is ```nbctf{s3cr3t_7uNN3lllllllllll!}```
