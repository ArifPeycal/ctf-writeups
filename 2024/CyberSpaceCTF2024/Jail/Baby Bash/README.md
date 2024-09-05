# Baby Bash
> I made a very secure bash terminal in Python. I don't think anyone can break in!
> 
> nc baby-pybash.challs.csc.tf 1337
## Challenge Overview
The script allows users to execute bash commands with some restrictions on the input. It seems that any command with letters (`A-Z, a-z`), symbols such as ```,,;\\!@/#?%`"\'&()-+``` will cause the program to call Value Error.  

```py
#!/usr/local/bin/python3 -u
import subprocess
import re


def restrict_input(command):
    pattern = re.compile(r'[a-zA-Z*^\,,;\\!@/#?%`"\'&()-+]|[^\x00-\x7F]')
    if pattern.search(command):
        raise ValueError("that's not nice!")
    return command


def execute_command(command):
    safe = restrict_input(command)
    result = subprocess.run(safe, stdout=True, shell=True)
    return result.stdout


print("Welcome to Baby PyBash!\n")
cmd = input("Enter a bash command: ")
output = execute_command(cmd)
print(output)

```
## Solution
We can use `$0` to launch bash without using the traditional method. Then, we can use `cat` to read the flag.

Reference:
https://www.commandlinefu.com/commands/view/11969/launch-bash-without-using-any-letters

![image](https://github.com/user-attachments/assets/d72dc2fe-6ceb-47bf-b661-d3ef11aa4785)

## Flag
```
CSCTF{b4sH_w1z4rd_0r_ju$t_ch33s3_m4st3r?_c1d4eeb2a}
```
