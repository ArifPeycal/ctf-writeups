# Flag Holding

## Description
> Hopefully you know how web works...
> 
> http://18.184.219.56:8080/

## Solution
The server prompts us the requirements to get the flag by modifying request header. 

> You are not coming from "http://flagland.internal/”
- Use `Referer` header to http://flagland.internal/

```
GET / HTTP/1.1
Host: 18.184.219.56:8080
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.216 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://flagland.internal/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close
```
> Unspecified "secret"
- Looks like we have to send `secret` parameter. Just assign any value.
```
GET /?secret=a HTTP/1.1
Host: 18.184.219.56:8080
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.216 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://flagland.internal/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close
```

> Incorrect secret. <!-- hint: secret is ____ which is the name of the protocol that both this server and your browser agrees on... —>
- We need to change `secret` value. The answer is `http`.
```
GET /?secret=http HTTP/1.1
Host: 18.184.219.56:8080
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.216 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://flagland.internal/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close
```

> Sorry we don't have "GET" here but we might have other things like "FLAG”.
- We need to change `GET` method to `FLAG`.
```
FLAG /?secret=http HTTP/1.1
Host: 18.184.219.56:8080
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.216 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://flagland.internal/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close
```
```html
<body>
	<div class="msg" style="">
		MAPNA{533m5-l1k3-y0u-kn0w-h77p-1836a2f}	</div>
</body>
```
## Flag
```
MAPNA{533m5-l1k3-y0u-kn0w-h77p-1836a2f}
```
