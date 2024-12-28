# Unwanted Meow
## Description
> Uh.. Oh.. Help me, I just browsing funny cats memes, when I click download cute cat picture, the file that been download seems little bit wierd. I accidently run the file making my files shredded. Ughh now I hate cat meowing at me.
>
> Author: 4jai
> 
> View Hint
> We don't want meow here.


## Solution

Upon examining the corrupted file using a hex editor, it became clear that the file was a JPG that contained the string "meow" embedded in its byte structure. The challenge was to find and remove all occurrences of this "meow" sequence, which is represented as 6d 65 6f 77 in hexadecimal (the ASCII values for "m", "e", "o", "w").

![image](https://github.com/user-attachments/assets/85bfed52-7700-454b-b131-af94a4c2c1f0)

The following Python script can be used to clean up the file:

```py
def remove_all_bytes_from_jpg(input_file, output_file, bytes_to_remove):
    # Convert the bytes to remove from hex to a byte sequence
    bytes_to_remove = bytes.fromhex(bytes_to_remove)
    
    with open(input_file, 'rb') as f:
        file_data = f.read()
    
    modified_data = file_data
    while bytes_to_remove in modified_data:
        modified_data = modified_data.replace(bytes_to_remove, b'')
    
    with open(output_file, 'wb') as f:
        f.write(modified_data)

    print(f"Modified file saved as {output_file}")

input_file = "flagshredded.jpg"  
output_file = "unshred.jpg"  
bytes_to_remove = "6d 65 6f 77"  # The byte sequence to remove (m e o w in hex)

remove_all_bytes_from_jpg(input_file, output_file, bytes_to_remove)
```
## Flag

![unshred](https://github.com/user-attachments/assets/3695e28e-6b9f-4b44-a95b-090ec0f6e53a)

```
WGMY{4a4be40c96ac6314e91d93f38043a634}
```
