# Secret of Jackal
## Description
> Created by: j4ck4l <br>
> I left a message for you. You will love it definitely
## Code Breakdown
```python
def ignore_it(file_param):
	yoooo = file_param.replace('.', '').replace('/', '')
	if yoooo != file_param:
		return "Illegal characters detected in file parameter!"
	return yoooo

def another_useless_function(file_param):
	return urllib.parse.unquote(file_param)

def useless (file_param):
	file_param1 = ignore_it(file_param)
	file_param2 = another_useless_function(file_param1)
	file_param3 = ignore_it(file_param2)
	file_param4 = another_useless_function(file_param3)
	file_param5 = another_useless_function(file_param4)
	return file_param5
```
## Endpoints:

The / route redirects to /read_secret_message with a default file parameter set to message.
The /read_secret_message route reads a file from the message/ directory based on the file parameter provided in the URL.

## Sanitization Functions:

```ignore_it(file_param)```: Removes periods and slashes from the file_param, intending to prevent directory traversal attacks. <br>
```another_useless_function(file_param)```: Decodes URL-encoded characters in the file_param. <br>
```useless(file_param)```: Chains the sanitization functions multiple times in an attempt to clean the file_param.

## Potential Vulnerabilities
1. Inadequate Directory Traversal Protection:

The ```ignore_it``` function is meant to remove periods and slashes to prevent directory traversal, but this protection might not be sufficient. Attackers could try bypassing this by using double-encoded characters, Unicode encodings, or other bypass techniques.

Testing: You can test this vulnerability by trying to access files outside the message/ directory using various encoding techniques.

Example payloads to test:

```%25252e%25252e%25252fflag%25252etxt``` <br>

## Flag
```flag{s1mp13_l0c4l_f1l3_1nclus10n_0dg4af52gav```
