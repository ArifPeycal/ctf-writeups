# Sembunyi V2
## Description
> Tahniah, perwira! Anda telah berjaya menyelesaikan cabaran pertama dan membuat Sultan Pahang berbangga. Namun, cabaran sebenar belum berakhir. Kini, anda dihadapkan dengan ujian yang lebih sukar. Ini adalah peluang untuk membuktikan kebolehan anda dalam menghadapi cabaran yang lebih mencabar!
>
> ini pesanan dari sultan:
>
> "Selamat datang ke cabaran seterusnya, perwira. Saya percaya anda mempunyai kemahiran untuk mengatasi segala halangan. Teruskan usaha anda, dan tunjukkan kehebatan dalam menyelesaikan cabaran ini."

## Challenge Overview

## Solution
```py
def process_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Convert tabs to '1' and spaces to '0'
        processed_content = ''.join('1' if char == '\t' else '0' if char == ' ' else '' for char in content)

        # Write the processed content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(processed_content)

        print(f"Processing complete. Output written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except IOError as e:
        print(f"Error reading or writing file: {e}")

# Example usage
input_filename = 'bendera.txt'
output_filename = 'output.txt'
process_file(input_filename, output_filename)
```
![image](https://github.com/user-attachments/assets/71d57cb3-2044-418a-acd3-018e1ff0007d)

## Flag
```
3108{putih_dan_hitam_dalam_negeri_pahang}
```
