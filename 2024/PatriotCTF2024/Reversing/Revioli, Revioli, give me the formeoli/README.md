# Revioli, Revioli, give me the formeoli

## Description
> Can you unlock the secret formula?

```
def calc(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    result_1, result = 0, 1
    for i in range(2, n + 1):
        result_1, result = result, result + result_1
    return result

def gen_correct_flag():
    fibs = [calc(i) for i in range(15)]  # Generate Fibonacci numbers for 0 to 14
    fib_string = ''.join(map(str, fibs))  # Create the string from Fibonacci numbers
    return f"ITALY_{fib_string}"

def assemble_flag(flag):
    return f"PCTF{{{flag}}}"

def main():
    generated_flag = gen_correct_flag()
    final_flag = assemble_flag(generated_flag)
    
    print(f"Generated flag: {generated_flag}")  # Print the generated flag for reference
    print(f"Final flag: {final_flag}")          # Print the final flag

if __name__ == "__main__":
    main()

```
## Flag
```
PCTF{ITALY_01123581321345589144233377}
```
