# Forenscript
## Description

In this challenge, we were provided with a corrupted PNG file. The goal was to recover the embedded images within the file. Given the nature of the file corruption, our task was to reverse the bytes within the file to restore its structure and then extract any hidden images.

PNG files start with an 8-byte signature: ```89 50 4E 47 0D 0A 1A 0A```. This helps us recognize the file format. However, in this challenge, the file seemed to have the byte order reversed in 4-byte chunks, which corrupted the PNG structure. <br>
To correct the file, we wrote a Python script that reads the binary content, reverses the order of each 4-byte chunk, and saves the corrected file.

```python
def reverse_4byte_chunks(file_path, output_path):
    try:
        # Open the input file in binary read mode
        with open(file_path, 'rb') as input_file:
            # Read the entire file content
            data = input_file.read()

        # Initialize an empty byte array to store the modified data
        modified_data = bytearray()

        # Process the file in 4-byte chunks
        for i in range(0, len(data), 4):
            # Reverse each 4-byte chunk
            chunk = data[i:i+4][::-1]
            modified_data.extend(chunk)

        # Write the modified data to the output file
        with open(output_path, 'wb') as output_file:
            output_file.write(modified_data)

        print(f"File processed successfully. Output saved to: {output_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

reverse_4byte_chunks(input_file_path, output_file_path)
```
This script corrected the byte order in the file. After running it, the output was a valid PNG file with the correct header.
![image](https://github.com/user-attachments/assets/b3b02a02-55ba-4114-8828-f83c750ac90b)

## Extracting Hidden Images with Binwalk
With the PNG structure restored, we used Binwalk, a tool for analyzing and extracting files from binary data, to check for any hidden images or files within the corrected PNG.

```bash
binwalk -e fixed.png
```
The -e option in Binwalk extracts any embedded files found in the binary data. Running this command revealed that there were indeed additional images hidden within the PNG.
Here, we found multiple image files that were extracted from the original corrupted PNG. These images were part of the challenge and contained the flag.
![image](https://github.com/user-attachments/assets/79a29836-d9ec-4c4d-9bc1-98912f72b4cb)

## Flag
```flag{scr1pt1ng_r34lly_t0ugh_a4n't_1t??}```
