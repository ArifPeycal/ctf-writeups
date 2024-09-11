# Math Geniuses
## Description
> Hehey, you good at meth eih? If you good how about you try this challenge. Lets see you are really good or you need to get good 🤯
> 
> Use nc to connect to the challenge
> 
> author: @cicakberlari
> 
> nc ice-training.syamilyusof.com 30788

## Challenge Overview
We were give a server to connect via `nc`. The server wants us to solve 100 math questions to get the flag within a specific time frame. It is hard to solve it manually so we need to use script to solve and send the answer automatically.  

![image](https://github.com/user-attachments/assets/ef21c47a-10e7-436c-9087-10a17bdcdc6c)

## Solution
This script will receive questions from server, using regex to extract numbers and operation. Then, the script uses `eval` to calclulate the equation and sends the answer back to server. 

```py
from pwn import *
import re

def conn(): #connect to server
    r = remote("ice-training.syamilyusof.com", 30788) 
    r.recvline() # Welcome to the Math Challenge!
    r.recvline() # Are you ready to begin? (y/n)
    r.sendline(b'y')
    return r

r = conn()
count = 1
math_exp_regex =  re.compile(r"^Question \d+: What is (\d+ [+\-*/] \d+)\?$");

for i in range(100):
    try:
        r.recvline()  # Great! Answer 100 questions correctly to win.
        output = r.recvline().decode()
        if match := math_exp_regex.match(output):
            question = match.group(1)
            answer = str((eval(question)))
            log.info(f"Question {i}: {question}, answer: {answer}")
            r.sendline(answer)
        else:
            print(output)
    except EOFError:
       r = conn() # Server side TIMEOUT 
       count = 1 # restart 
```

![image](https://github.com/user-attachments/assets/86900151-d9e0-4595-ab0c-98b8caef0630)

## Flag
```
ICE{t1r3d_0f_w@1t1ng?_try_w@1t_f@st3r}
```
