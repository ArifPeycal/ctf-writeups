# Coding Mountains

> Author: @Soups71
>
> I like mountains and I like coding, so I made this game. I hope you also like both of those things, or else you probably won't have a ton of fun...

## Solution

For this challenge, we were given an instance to deploy. By connecting through `netcat`, we were required to answer several questions about mountains' heights and first ascent year. The answers were given in a JSON file. 

```cmd
Welcome! I've recently gotten into mountaineering, so I came up with this fun little quiz game.
Just answer 50 questions for me!

Note: Height is measured in feet with no comma (e.g., 28129).
If the peak has not been summited, write none; otherwise, specify the year of the first ascent.
Answer with comma-separated values, (e.g., `height,year`)

Do you want to give it a chance? (Y/n): y
Awesome, good luck!
What is the height and first ascent year of Batura Sar:
```
It will be a hassle to manually typing the answer, so we can create a script that extract which mountain we need to look for from the question, find the answer in JSON file and send the answer back to the server. 

```py
from pwn import *
import json

# Enable verbose mode
context.log_level = 'debug'

# Load mountain data from a JSON file
with open("mountains.json", "r") as file:
    mountains = json.load(file)

def get_mountain_answer(name):
    for mountain in mountains:
        if mountain["name"].lower() == name.lower():
            return f"{mountain['height'].replace(',', '')},{mountain['first']}\n"
    return "none\n"  # Default if mountain not found

# Connect to the challenge server
host, port = "challenge.ctf.games", 30110
conn = remote(host, port)

# Receive the welcome message
conn.recvuntil(b"Do you want to give it a chance? (Y/n): ")

# Send 'y' to start the quiz
your_response = b"y\n"
conn.send(your_response)

while True:
    try:
        # Receive the next question
        question = conn.recvuntil(b": ").decode().strip()
        print(f"[QUESTION] {question}")
        
        # Extract mountain name from the question
        mountain_name = question.split("the height and first ascent year of ")[-1].strip(" :")
        
        # Get the answer
        answer = get_mountain_answer(mountain_name)
        print(f"[ANSWER] {answer.strip()}")
        
        # Send the answer
        conn.send(answer.encode())
    except EOFError:
        print("[INFO] Connection closed.")
        break

# Keep the connection open for further interaction
conn.interactive()

```

![image](https://github.com/user-attachments/assets/8a025afe-d13e-44a5-9699-469d6c1d72d4)

## Flag
```
flag{33e043f76c3ba0fe9265749dbe650940}
```
