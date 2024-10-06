# Fire in the Base Camp
## Description
> I was playing with the dice when I heard about the fire in the base camp. Can you get there on time?

Solution:
jadx the .apk
found the firebase. start search string keyword 'flag'
found the uri
crafting the substring. enter the .json

![image](https://github.com/user-attachments/assets/ff2f7da7-a219-468d-9781-e2754f7f2e1d)


To get the full Firebase database path used in this Android app, the code references several string resources (`fb1`, `fb2`, `fb3`, `fb4`) and concatenates parts of them to build the path dynamically. Here's how the path is constructed and how you can retrieve all parts:

### Steps to Retrieve the Full Path

1. **String Resources Referenced in Code**:
   - `path1 = getResources().getString(R.string.fb4).substring(0, 7);`
   - `path2 = getResources().getString(R.string.fb3).substring(10, 15);`
   - `path3 = getResources().getString(R.string.fb4).substring(18, 21);`
   - `path4 = getResources().getString(R.string.fb2).substring(16, 20);`
   - `path5 = getResources().getString(R.string.fb1).substring(12, 17);`

   Each `pathX` is derived from a substring of the string resource. To find these values:
   
   - `R.string.fb1` corresponds to a string resource in the app's `res/values/strings.xml` file.
   - Similarly, `R.string.fb2`, `R.string.fb3`, and `R.string.fb4` are other string resources defined in that file.


2. **Locate the `strings.xml` File**:
   - Inside your Android project, go to the directory `res/values/strings.xml`.
   - Look for the string definitions for `fb1`, `fb2`, `fb3`, and `fb4`. They will look something like this:

![image](https://github.com/user-attachments/assets/771ae895-5f44-4da4-bc2a-d686c15fcfe8)


3. **Extract Substrings**:
   The code is taking substrings from these values to create the final path. Here's how each substring is extracted:
   - `path1 = fb4.substring(0, 7);` – the first 7 characters of `fb4`.
   - `path2 = fb3.substring(10, 15);` – characters 10 to 15 from `fb3`.
   - `path3 = fb4.substring(18, 21);` – characters 18 to 21 from `fb4`.
   - `path4 = fb2.substring(16, 20);` – characters 16 to 20 from `fb2`.
   - `path5 = fb1.substring(12, 17);` – characters 12 to 17 from `fb1`.

4. **Concatenate the Values**:
   Once you have the full values from `fb1`, `fb2`, `fb3`, and `fb4`, use the substring logic described above to extract the parts and concatenate them to form the complete Firebase database path:

   ```java
   String fullPath = path1 + path2 + path3 + path4 + path5;
   ```



```py
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
## Flag
```
ironCTF{y0u_pu7_0u7_th3_f1r3_1n_th3_b4s3_c4mp_1f84a5c66ff5}
```
