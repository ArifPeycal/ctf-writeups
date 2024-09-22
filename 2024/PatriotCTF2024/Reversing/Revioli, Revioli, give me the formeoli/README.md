# Revioli, Revioli, give me the formeoli

## Description
> Can you unlock the secret formula?

```c
int64_t gen_correct_flag(char* arg1)
{
    void* fsbase;
    int64_t rax = *(fsbase + 0x28);
    void var_1b8;
    
    for (int32_t i = 0; i <= 0xe; i += 1)
        *(&var_1b8 + (i << 3)) = calc(i);
    
    int64_t s_1;
    __builtin_memset(&s_1, 0, 0x100);
    
    for (int32_t i_1 = 0; i_1 <= 0xe; i_1 += 1)
    {
        void s;
        snprintf(&s, 0x14, "%llu", *(&var_1b8 + (i_1 << 3)));
        strcat(&s_1, &s);
    }
    
    snprintf(arg1, 0x100, "ITALY_%s", &s_1);
    
    if (rax == *(fsbase + 0x28))
        return (rax - *(fsbase + 0x28));
    
    __stack_chk_fail();
    /* no return */
}

int64_t assemble_flag(int64_t arg1, char* arg2)
{
    return snprintf(arg2, 0x100, "PCTF{%s}", arg1);
}

int32_t main(int32_t argc, char** argv, char** envp)
{
    void* fsbase;
    int64_t rax = *(fsbase + 0x28);
    void var_218;
    gen_correct_flag(&var_218);
    void var_118;
    assemble_flag(&var_218, &var_118);
    printf("Enter-a the password-a: ");
    void buf;
    fgets(&buf, 0x100, __TMC_END__);
    *(&buf + strcspn(&buf, &data_2038)) = 0;
    
    if (strcmp(&buf, &var_218) != 0)
        puts("No toucha my spaget!");
    else
        printf("Congratulations! The flag is: %s…", &var_118);
    
    *(fsbase + 0x28);
    
    if (rax == *(fsbase + 0x28))
        return 0;
    
    __stack_chk_fail();
    /* no return */
}

int64_t _fini() __pure
{
    return;
}
```
```py
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
