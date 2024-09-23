# Structured Annuity

## Description
> These J.G. Wentworth ads are getting out of hand! Now we're evem getting reports that they're using malware to try and get people cash for their structured settlements! Luckily, we were able to capture some network traffic of this c2 beacon, along with the binary and a memory capture of the running process. Unfortunately, it seems like the c2 agent contains no static keys and instead generates them at run time. Can you decrypt their comms?

![image](https://github.com/user-attachments/assets/050760c2-4e3a-46a5-b43a-134fc0cb18e7)

![image](https://github.com/user-attachments/assets/98926c78-d6c9-4ce8-8c8e-9e566d48aa9d)


```
N1:e = 56048657891568470071072200352453435307145615629716429378285176310839997106837:65537
N2:e = 34052883331862194561588316384768805552479914185714526668665063402813300904421:65537

c1 = 26837762086290757052486642102560852925225702609872568979330654281329444894706
c2 = 29977567988592954316835508906387630123424709642590239142264084540225085777016
```

These values are around 256 bits, meaning p and q will be 128 bits, or rather 16 bytes.

We need to recover the private key. The challenge description says that its generated during runtime. 
We also have a binary copy of the c2 server. Nothing much happens when we run it, but we can investigate the crash report in gdb and take a look at the memory during it's runtime

```
gdb structured_annuity structured_annuity.dump
```

Always start by disassembling main. 

We see mentions of `<rsa_decrypt>` and `<rsa_encrypt>` in main. 

We see a whole bunch of values passed into ``<rsa_decrypt>``

```
   0x000055d83de3cdc9 <+682>:   push   QWORD PTR [rbp-0x1090]
   0x000055d83de3cdcf <+688>:   push   QWORD PTR [rbp-0x1098]
   0x000055d83de3cdd5 <+694>:   push   QWORD PTR [rbp-0x10a0]
   0x000055d83de3cddb <+700>:   push   QWORD PTR [rbp-0x10a8]
   0x000055d83de3cde1 <+706>:   push   QWORD PTR [rbp-0x10b0]
   0x000055d83de3cde7 <+712>:   push   QWORD PTR [rbp-0x10b8]
   0x000055d83de3cded <+718>:   push   QWORD PTR [rbp-0x10c0]
   0x000055d83de3cdf3 <+724>:   push   QWORD PTR [rbp-0x10c8]
   0x000055d83de3cdf9 <+730>:   push   QWORD PTR [rbp-0x10d0]
   0x000055d83de3cdff <+736>:   push   QWORD PTR [rbp-0x10d8]
   0x000055d83de3ce05 <+742>:   push   QWORD PTR [rbp-0x10e0]
   0x000055d83de3ce0b <+748>:   push   QWORD PTR [rbp-0x10e8]
   0x000055d83de3ce11 <+754>:   push   QWORD PTR [rbp-0x10f0]
   0x000055d83de3ce17 <+760>:   mov    rsi,rdx
   0x000055d83de3ce1a <+763>:   mov    rdi,rax
   0x000055d83de3ce1d <+766>:   call   0x55d83de3c6bf <rsa_decrypt>
```

We can see what is being pushed to the stack:

```
pwndbg> x/14gx $rbp-0x10f0
0x7ffc433b6e10: 0x0079656b76697270      0x0000000200000003
0x7ffc433b6e20: 0x000055d83f75d010      0x0000000200000003
0x7ffc433b6e30: 0x000055d83f75bc70      0x0000000100000001
0x7ffc433b6e40: 0x000055d83f75bd70      0x0000000400000005
0x7ffc433b6e50: 0x000055d83f75bd90      0x0000000400000004
0x7ffc433b6e60: 0x000055d83f75bd00      0x0000000400000004
0x7ffc433b6e70: 0x000055d83f75bcd0      0x0000000000000044
```

The first line `0x0079656b76697270` says `\x00yekvirp` or rather `privkey`. This is promising!

Let's continue by dereferencing the next couple of pointers

```
pwndbg> x/2gx 0x000055d83f75d010
0x55d83f75d010: 0xda5d28fa653fd41d      0xf9fdd04a062c533b
pwndbg> x/2gx 0x000055d83f75bc70
0x55d83f75bc70: 0x6467957633a1d6d9      0x7ee4dd28cba569f5
pwndbg> x/2gx 0x000055d83f75bd70
0x55d83f75bd70: 0x0000000000010001      0x00007f17b4622ce0


We see `0x0000000000010001` which is our e value! The two other values are 16 bytes. By reconstructing them we get:


0xf9fdd04a062c533bda5d28fa653fd41d
0x7ee4dd28cba569f56467957633a1d6d9


We can check them out to see if they are around 128 bits and prime (requirements for p and q)


sage: 0xf9fdd04a062c533bda5d28fa653fd41d.nbits()
128
sage: 0x7ee4dd28cba569f56467957633a1d6d9.nbits()
127
sage: 0xf9fdd04a062c533bda5d28fa653fd41d.is_prime()
True
sage: 0x7ee4dd28cba569f56467957633a1d6d9.is_prime()
True


Let's try to use these to decrypt the ciphertext from the pcapng!


from Crypto.Util.number import long_to_bytes
N = 56048657891568470071072200352453435307145615629716429378285176310839997106837
e = 65537
p = 332295646661645445201577206886078338077 # this is 0xf9fdd04a062c533bda5d28fa653fd41d
q = 168671056797319678404059216640521393881 # this is 0x7ee4dd28cba569f56467957633a1d6d9
c = 26837762086290757052486642102560852925225702609872568979330654281329444894706

phi = (p-1)*(q-1)
d = pow(e, -1, phi)
m = pow(c, d, N)
print(long_to_bytes(m))


And we get our flag!


b'echo PCTF{8U7_I_N33D_C@5H_N0W}'

```
