# Stones
## Description
> When Thanos snapped his fingers, half of the flag was blipped. We need the Avengers to retrieve the other half.
> 
> There's no flag in the movie, but there is a slash flag on the server
> 
> (Please do not perform any brute forcing, enumeration, or scanning. Not useful nor needed)
> 
> Author: KD_Kasturi
> 
> View Hint
> You don't need to change the script. You need to travel back in time to the flag.

## Solution

I found out two ways to get the initial step. First by using online malware analysis tool like Hybrid Analysis and ANY.run and the other one is extract contents from the executable file using `pyinstxtractor.py` 

## Using Hybrid Analysis

Upload the file and get the report.

![image](https://github.com/user-attachments/assets/9de9a697-f3a6-45af-ba57-2ca7bb150b5b)

Look under Network Analysis -> HTTP Traffic, you can see the URL contains first flag. 

![image](https://github.com/user-attachments/assets/f49175e9-bdd4-4e5e-a837-3b65ad450ece)

### Using `pyinstxtractor.py`

Make sure you installed pyinstxtractor.py from https://github.com/extremecoders-re/pyinstxtractor. Run the command.

```
python3 pyinstxtractor.py >filename>
```

![image](https://github.com/user-attachments/assets/3b4502b8-9783-4891-b942-05e5f3b9976a)

You will get a folder contains the extracted content from `stones.exe`. There will be a lot of library files but the only interesting file is `CHAL-stones.pyc`.

![image](https://github.com/user-attachments/assets/e8fe93fd-7477-4e5c-b5ce-6f4b98966dba)

Since `.pyc` is compiled Python script, you need to decompile it first. You can use uncompyle6 or https://pylingual.io/ if you prefer online tools. 

The script retrieves the current date from http://just-the-time.appspot.com/ and compares it with the local machine's date. If they match, it sends a GET request to a server (http://3.142.133.106:8000/) with a flag and the date as parameters. If the server responds successfully, it prints the flag; otherwise, it prints an error message. 

The script only shows the first part of flag, we need to find a way to get the full flag by modifying the date (hint said that we need to time travel).

```
import requests
from datetime import datetime
from urllib.request import urlopen
from datetime import datetime
server_url = 'http://3.142.133.106:8000/'
current_time = urlopen('http://just-the-time.appspot.com/')
current_time = current_time.read().strip()
current_time = current_time.decode('utf-8')
current_date = current_time.split(' ')[0]
local_date = datetime.now().strftime('%Y-%m-%d')
if current_date == local_date:
    print("We're gonna need a really big brain; bigger than his?")
first_flag = 'WGMY{1d2993'
user_date = current_date
params = {'first_flag': first_flag, 'date': user_date}
response = requests.get(server_url, params=params)
if response.status_code == 200:
    print(response.json()['flag'])
else:
    print(response.json()['error'])
```

If you include today's date, it will give you error. 

![image](https://github.com/user-attachments/assets/7a98daa1-0879-4057-a094-46cdebc0a8f6)

There is a hint in description said that there is a slash flag in the server. So, we need to access `/flag` from the server http://3.142.133.106:8000/flag. It will gives you the JSON response with a Youtube link.
```json
{
"Upload Date": "https://www.youtube.com/watch?v=V0zJb2K4Yi8&t=75s"
}
```
It will redirect you to a Yooutube video shows a scene in Avengers Endgame. We get the upload date as `Jul 25, 2022` (2022-07-25)

![image](https://github.com/user-attachments/assets/5436bbc3-6580-48f2-ac9f-8099b799cb2e)

Modify the date in URL with the upload date of the video.

![image](https://github.com/user-attachments/assets/112aea1d-92ff-4822-81d7-ed5006dd445d)

## Flag

```
WGMY{1d2993fc6327746830cd374debcb98f5}
```
