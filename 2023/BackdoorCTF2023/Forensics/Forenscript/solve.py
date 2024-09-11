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

# Example usage:
input_file_path = 'a.bin'  # Replace with your input file path
output_file_path = 'output.bin'  # Replace with your desired output file path

reverse_4byte_chunks(input_file_path, output_file_path)
