# The DCM Meta

> "[25, 10, 0, 3, 17, 19, 23, 27, 4, 13, 20, 8, 24, 21, 31, 15, 7, 29, 6, 1, 9, 30, 22, 5, 28, 18, 26, 11, 2, 14, 16, 12]"
>
> Author: Yes
> 
> View Hint
> The element is the number in the list, combine for the flag. Wrap in wgmy{}

## First Blood
![image](https://github.com/user-attachments/assets/a5f73308-ef0f-42ea-a4de-698cc1ae79d3)

## Solution

If you read the file using pydicom, you can see the char in the file. So, we need to extract the first letters from private tag data, rearrange them according to the provided index list and print the result as wgmy{<arranged_letters>}.

```
(0011,0010) Private Creator                     LO: 'WGMY'
(0011,1000) Private tag data                    UN: b'f\x00\x00\x00'
(0011,1001) Private tag data                    UN: b'6\x00\x00\x00'
(0011,1002) Private tag data                    UN: b'3\x00\x00\x00'
(0011,1003) Private tag data                    UN: b'a\x00\x00\x00'
(0011,1004) Private tag data                    UN: b'c\x00\x00\x00'
(0011,1005) Private tag data                    UN: b'd\x00\x00\x00'
(0011,1006) Private tag data                    UN: b'3\x00\x00\x00'
(0011,1007) Private tag data                    UN: b'b\x00\x00\x00'
(0011,1008) Private tag data                    UN: b'7\x00\x00\x00'
(0011,1009) Private tag data                    UN: b'8\x00\x00\x00'
```

```py
import pydicom

# Provided indices to arrange the letters
indices = [25, 10, 0, 3, 17, 19, 23, 27, 4, 13, 20, 8, 24, 21, 31, 15, 7, 29, 6, 1, 9, 30, 22, 5, 28, 18, 26, 11, 2, 14, 16, 12]

# List to store extracted letters
extracted_letters = []

try:
    # Read the DICOM file
    dicom_data = pydicom.dcmread("challenge.dcm", force=True)
    
    for elem in dicom_data.iterall():
        # Check if the tag is a private tag (i.e., starts with (0011,xxxx))
        if elem.tag.group == 0x0011:
            raw_data = elem.value
            # If the data is bytes (UN type), decode it to get the letter after 'b'
            if isinstance(raw_data, bytes):
                decoded_data = raw_data.decode('utf-8', errors='ignore')
                if decoded_data:
                    extracted_letters.append(decoded_data[0])

    arranged_letters = [''] * len(indices)  

    for i, index in enumerate(indices):
        if index < len(extracted_letters):  # Ensure the index is within the range of extracted letters
            arranged_letters[i] = extracted_letters[index]

    result = ''.join(arranged_letters)
    print("Flag: wgmy{"+result+"}")

except Exception as e:
    print(f"Error reading DICOM file: {e}")
```
## Flag
```
wgmy{51fadeb6cc77504db336850d53623177}
```
