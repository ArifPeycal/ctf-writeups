# Emoji Stack
## Description
> Welcome to Emoji Stack, the brand new stack based emoji language! Instead of other stack based turing machines that use difficult to read and challenging characters like + - and [], Emoji Stack uses our proprietary patent pending emoji system.
> 
> The details of our implentation is below:
> 
> 👉: Move the stack pointer one cell to the right
>👈: Move the stack pointer one cell to the lef
> 👍: Increment the current cell by one, bounded by 255
> 👎: Decrement the current cell by one, bounded by 0
> 💬: Print the ASCII value of the current cell
> 🔁##: Repeat the previous instruction 0x## times
> The Emoji Stack is 256 cells long, with each cell supporting a value between 0 - 255.
>
> As an example, the program "👍🔁47💬👉👍🔁68💬👉👍🔁20💬" Would output "Hi!" with the following execution flow:
>
> [0, 0, 0, 0] 👍🔁47
>
> [0x48, 0, 0, 0] 💬👉: H
> 
> [0x48, 0, 0, 0] 👍🔁68
>
> [0x48, 0x69, 0, 0] 💬👉: i
>
> [0x48, 0x69, 0, 0] 👍🔁20
>
> [0x48, 0x69, 0x21, 0] 💬: !
>
> Flag format: CACI{.*}

```py
def emoji_stack_interpreter(program):
    stack = [0] * 256  # Initialize the stack with 256 cells
    pointer = 0         # Stack pointer starts at position 0
    output = []         # To store the printed ASCII values
    i = 0               # Program counter

    while i < len(program):
        instr = program[i]

        if instr == '👉':
            pointer = (pointer + 1) % 256  # Move right, wrap around at 256
        elif instr == '👈':
            pointer = (pointer - 1) % 256  # Move left, wrap around at 0
        elif instr == '👍':
            stack[pointer] = (stack[pointer] + 1) % 256  # Increment, bounded by 255
        elif instr == '👎':
            stack[pointer] = (stack[pointer] - 1) % 256  # Decrement, bounded by 0
        elif instr == '💬':
            output.append(chr(stack[pointer]))  # Print the ASCII value
        elif instr == '🔁':
            # Handle repeat instruction 🔁##, where ## is a hex number
            repeat_count = int(program[i+1:i+3], 16)  # Parse hex number
            last_instr = program[i-1]  # Repeat the last instruction
            for _ in range(repeat_count):
                if last_instr == '👍':
                    stack[pointer] = (stack[pointer] + 1) % 256
                elif last_instr == '👎':
                    stack[pointer] = (stack[pointer] - 1) % 256
                elif last_instr == '👉':
                    pointer = (pointer + 1) % 256
                elif last_instr == '👈':
                    pointer = (pointer - 1) % 256
                elif last_instr == '💬':
                    output.append(chr(stack[pointer]))
            i += 2  # Skip the two hex digits after 🔁
        i += 1

    return ''.join(output)

# Read the program from input.txt and decode the flag
with open('input.txt', 'r', encoding='utf-8') as f:
    program = f.read().strip()

flag = emoji_stack_interpreter(program)
print(f"Decoded flag: {flag}")
```
## Flag
```
CACI{TUR!NG_!5_R011!NG_!N_H!5_GR@V3}
```
