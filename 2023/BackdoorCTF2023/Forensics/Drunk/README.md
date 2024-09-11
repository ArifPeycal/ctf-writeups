# Drunk
## Description
> I was offered a famous Italian drink along with a message, but it affected me in such a way that I couldn’t decipher it. Need your help and please don’t make excuse if you can’t.

## Challenge Overview
In this challenge, we were provided with two files:

- ```something.txt```: Contains a series of octal values.
- ```encoded.bin```: Contains encrypted binary data.

Our task was to decode the something.txt file to get a key and use this key to decrypt ```encoded.bin```.


The something.txt file contains octal values separated by spaces. We can use CyberChef for decryption. <br>

Once we have the Base64 key, we can use the Fernet library to decrypt the encoded.bin file. Here’s a script to perform decryption:

```python
from cryptography.fernet import Fernet

# The provided Fernet key
key = b'zlMg5K3TobbFh_8l7doDT_408rH7Md_W3Oc1yKX1FrA='

# Create a Fernet object using the key
cipher = Fernet(key)

# Path to the file containing the encrypted binary data
input_file_path = 'encoded.bin'
output_file_path = 'decoded_output.bin'
error_file_path = 'error_log.txt'

# Function to write error message to the output file
def log_error(message):
    with open(error_file_path, 'a') as error_file:
        error_file.write(message + '\n')

# Read the encrypted data from the file
try:
    with open(input_file_path, 'rb') as file:
        encrypted_data = file.read()
        
    # Decrypt the data
    decrypted_data = cipher.decrypt(encrypted_data)
    
    # Write the decrypted data to a new file
    with open(output_file_path, 'wb') as file:
        file.write(decrypted_data)
    
    print(f"Decryption successful. The decrypted data has been saved to '{output_file_path}'.")
except Exception as e:
    error_message = f"An error occurred during decryption: {str(e)}"
    print(error_message)
    log_error(error_message)

```

Opening the output file in Notepad, we can see the ```PNG``` header. So, we can change the file extension to see the image.
![image](https://github.com/user-attachments/assets/4aae02af-b389-4969-8ddf-063220b2ff66)

## Flag
```flag{Th1s_time_n0t_cURs1v3}```
