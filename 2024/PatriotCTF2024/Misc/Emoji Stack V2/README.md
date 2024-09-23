# Emoji Stack V2
## Description
> Back by popular demand, V2 of EmojiStack is ready to release! Following user feedback, we've made some changes to how things work:
> 
> It was pointed out that EmojiStack wasn't actually turing complete, and was instead just "A really dumb markup language." To remedy this, we've added three new commands for execution control, please see details below. Sticking with our philosophy of readability, we figured that hex numbers are too complicated and have decided to switch to easily read emoji representations. Numbers will now be encoded in base 12 from 🕛 to 🕚. Example: 🔁5f --> 🔁🕛🕖🕚 For our second release, it only seemed fair to add a second stack dimension! Emoji Stack now supports a 255x255 grid of cells. With the addition of two dimensional stacks, a good idea fairy said it might be cool to represent stack states using images. The state of the stack is now saved as a 255x255 8 bit grey scale image to allow for the pre-initialization of the stack. Images are stored raster-scan order with 0,0 being the top left of the image.
> 
> Commands
> 
> 👉: Move the stack pointer one cell to the right
> 👈: Move the stack pointer one cell to the left
> 👆: Move the stack pointer one cell upwards
> 👇: Move the stack pointer one cell downwards
> 👍: Increment the current cell by one, bounded by 255
> 👎: Decrement the current cell by one, bounded by 0
> 💬: Print the ASCII value of the current cell
> 👂: Read one character of ASCII and store it in the current cell
> 🫸: If the current cell is zero, jump to the next instruction after the respective 🫷
> 🫷: If the current cell is non-zero, jump back to the respective 🫸
> 🔁###: Repeat the previous instruction ## times


```py
from PIL import Image
import numpy as np
import sys

# Read the 255x255 8-bit grayscale PNG image and initialize the stack
image = Image.open('initial_state.png').convert('L')  # Convert image to 8-bit grayscale
if image.size != (255, 255):
    raise ValueError("Image must be 255x255 pixels.")
grid = np.array(image, dtype=np.uint8)

# Read the program code from 'program.txt'
with open('program.txt', 'r', encoding='utf-8') as f:
    program_code = f.read()

# Define the mappings for clock emojis to base-12 digits
clock_to_digit = {
    '🕛': 0,
    '🕐': 1,
    '🕑': 2,
    '🕒': 3,
    '🕓': 4,
    '🕔': 5,
    '🕕': 6,
    '🕖': 7,
    '🕗': 8,
    '🕘': 9,
    '🕙': 10,
    '🕚': 11,
}

# Define the valid tokens
single_char_tokens = {'👉', '👈', '👆', '👇', '👍', '👎', '💬', '👂', '🫸', '🫷'}
repeat_token = '🔁'
clock_emojis = set(clock_to_digit.keys())

# Tokenize the program code
tokens = []
i = 0
while i < len(program_code):
    c = program_code[i]
    if c in single_char_tokens:
        tokens.append(c)
        i += 1
    elif c == repeat_token:
        i += 1
        repeat_clocks = ''
        while i < len(program_code) and program_code[i] in clock_emojis:
            repeat_clocks += program_code[i]
            i += 1
        if not repeat_clocks:
            raise ValueError('Invalid repeat instruction: no clock emojis after 🔁')
        tokens.append(('repeat', repeat_clocks))
    else:
        raise ValueError(f'Invalid token in program code: {c}')

# Build loop mappings for '🫸' and '🫷'
loop_stack = []
loop_mapping = {}
for position, token in enumerate(tokens):
    if token == '🫸':
        loop_stack.append(position)
    elif token == '🫷':
        if not loop_stack:
            raise ValueError("Loop closing '🫷' found without matching opening '🫸'")
        start = loop_stack.pop()
        loop_mapping[start] = position
        loop_mapping[position] = start
if loop_stack:
    raise ValueError("Loop opening '🫸' without matching closing '🫷'")

# Function to convert clock emojis to an integer
def clocks_to_int(clock_sequence):
    value_str = ''
    for clock in clock_sequence:
        digit = clock_to_digit[clock]
        if digit < 10:
            value_str += str(digit)
        else:
            value_str += chr(ord('A') + digit - 10)
    return int(value_str, 12)

# Initialize the pointer position
x = 0
y = 0

# Function to execute a single token
def execute_token(token, ip):
    global x, y, grid
    if token == '👉':
        x = (x + 1) % 255
        return ip + 1
    elif token == '👈':
        x = (x - 1) % 255
        return ip + 1
    elif token == '👆':
        y = (y - 1) % 255
        return ip + 1
    elif token == '👇':
        y = (y + 1) % 255
        return ip + 1
    elif token == '👍':
        grid[y][x] = (grid[y][x] + 1) % 256
        return ip + 1
    elif token == '👎':
        grid[y][x] = (grid[y][x] - 1) % 256
        return ip + 1
    elif token == '💬':
        sys.stdout.write(chr(grid[y][x]))
        sys.stdout.flush()
        return ip + 1
    elif token == '👂':
        user_input = sys.stdin.read(1)
        if user_input:
            grid[y][x] = ord(user_input[0]) % 256
        else:
            grid[y][x] = 0
        return ip + 1
    elif token == '🫸':
        if grid[y][x] == 0:
            return loop_mapping[ip] + 1  # Jump to instruction after matching '🫷'
        else:
            return ip + 1
    elif token == '🫷':
        if grid[y][x] != 0:
            return loop_mapping[ip] + 1  # Jump back to instruction after matching '🫸'
        else:
            return ip + 1
    else:
        raise ValueError(f'Unknown token: {token}')

# Interpreter loop
ip = 0  # Instruction pointer
while ip < len(tokens):
    token = tokens[ip]
    if isinstance(token, tuple) and token[0] == 'repeat':
        repeat_clocks = token[1]
        repeat_count = clocks_to_int(repeat_clocks)
        if ip == 0:
            raise ValueError('Repeat instruction at beginning of program with no previous instruction')
        previous_token = tokens[ip - 1]
        for _ in range(repeat_count):
            # For repeat, we don't change ip
            execute_token(previous_token, ip - 1)
        ip += 1
    else:
        ip = execute_token(token, ip)

# Save the finalized grid as a PNG image
final_image = Image.fromarray(np.array(image, dtype=np.uint8)-grid, mode='L')
final_image.save('finalized_state.png')

```
![finalized_state](https://github.com/user-attachments/assets/00fe12e9-2ae2-490c-89ae-13fa2f8930a9)
