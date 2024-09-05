# Unmask
## Description
> A crucial file has been tampered with in a way in order to conceal its true contents. Your mission is to unmask the data and retrieve the hidden information. Lets find out your worth and if you have what it takes to uncover and extract the forensic evidence. And if you do, I assure you, the return will be rewarding. All the best Agent!

## Solution
- We get a challenge.dat that contains hexadecimal numbers, the number is similar to PNG magic bytes but they are all reversed in each line.
```
52 44 48 49 0d 00 00 00 0a 1a 0a 0d 47 4e 50 89
29 f7 16 00 00 00 03 08 40 06 00 00 d0 07 00 00
32 3c 37 18 6d 6a 37 45 54 4c 50 00 03 00 00 bc
                    [SNIPPED]
```
- Create a python script to read all numbers, reverse for each line and convert to bytes.
```python
# Define the input and output filenames
input_filename = 'challenge.dat'
output_filename = 'output.png'

# Open the input file for reading and the output file for writing in binary mode
with open(input_filename, 'r') as infile, open(output_filename, 'wb') as outfile:
    # Read each line from the input file
    for line in infile:
        # Split the line into a list of byte values (as strings)
        byte_list = line.strip().split()
        
        # Convert each string byte to an actual byte value
        byte_list = [int(byte, 16) for byte in byte_list]
        
        # Reverse the list of byte values
        reversed_byte_list = byte_list[::-1]
        
        # Convert the reversed list back to bytes and write to the output file
        outfile.write(bytes(reversed_byte_list))

```
## Flag
![output1](https://github.com/user-attachments/assets/4155aea0-8296-4a8a-97e1-486cf5b6965a)
