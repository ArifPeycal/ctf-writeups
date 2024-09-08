# ZipZipZip
## Description
> Brighten up at last with the flag

## Challenge Overview
We were given a `challenge.zip` that contains a zip file, `chunk_0.zip` in it. If we extract that zip file, we will receive a text file, `chunk_0.txt` and another zip file, `chunk_1.zip`. Each text file contains a base64 string. So, it is obvious that we need to extract all zip files and decrypt base64 strings in each text file.

## Solution
The script iterates over chunk files (zip and text), extracts the zip files, reads and writes the text file contents to the output file, and then cleans up by deleting processed files. The loop continues until no more zip files are found, as indicated by the absence of the zip file for the current chunk.

Why do we need to delete the files after extracting them? It is because the total zip files for this challenge are **MASSIVE** (almost 32000+, can be up to 50 GB of storage). 

```py
import zipfile
import os

def unzip_and_read_chunks(output_file, start=0, base_dir="."):
    current_chunk = start

    with open(output_file, 'w') as output:
        while True:
            zip_filename = f"chunk_{current_chunk}.zip"
            txt_filename = f"chunk_{current_chunk}.txt"
            zip_path = os.path.join(base_dir, zip_filename)
            txt_path = os.path.join(base_dir, txt_filename)

            # Check if the zip file exists
            if not os.path.exists(zip_path):
                print(f"No more zip files found. Stopping at chunk_{current_chunk}.")
                break

            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(base_dir)

            if os.path.exists(txt_path):
                with open(txt_path, 'r') as txt_file:
                    content = txt_file.read()
                    output.write(content)
                # Delete the text file after reading
                os.remove(txt_path)
            else:
                print(f"{txt_filename} not found after unzipping {zip_filename}.")

            os.remove(zip_path)

            current_chunk += 1

unzip_and_read_chunks('all_chunks.txt')

```

After the extraction complete, we can read the output file and decrypt it using CyberChef. Turns out it is a PNG file. The flag is inside the image.

![output](https://github.com/user-attachments/assets/32a20378-d143-47c7-a9c9-401bb6024bae)

## Flag
```
csawctf{ez_r3cur5iv3ne55_right7?}
```
