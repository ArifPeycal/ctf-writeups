# Fire in the Base Camp
## Description
> I was playing with the dice when I heard about the fire in the base camp. Can you get there on time?

Solution:
jadx the .apk
found the firebase. start search string keyword 'firebase'
found the uri
crafting the substring. enter the .json

```
import os
import json

resources = {
    "fb1": "/is/this/the/flag",
    "fb2": "/i/think/this/is/the/one",
    "fb3": "/seriously/give/me/the/flag/now",
    "fb4": "/please/give/it/to/me"
}

path1 = resources["fb4"][0:7]
path2 = resources["fb3"][10:15]
path3 = resources["fb4"][18:21]
path4 = resources["fb2"][16:20]
path5 = resources["fb1"][12:17]

result = path1 + path2 + path3 + path4 + path5 + '.json'

url = 'https://app3-7d107-default-rtdb.firebaseio.com' + result

print("Final URL:", url)

response = os.popen(f"curl {url}").read()

data = json.loads(response)

extracted_values = [value for key, value in data.items()]
final_result = ''.join(extracted_values)

print("Combined Result:", final_result)
```
