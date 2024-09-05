# Rabbit Hole
## Description
> "In the heart of the binary, a secret slumbers."
> 
> Remember submit flag in CyGenixCTF{} format

## Solution
The challenge provided a binary named packed, which hinted that it might be packed using UPX. Running the strings command confirmed this suspicion:
> UPX stands for Ultimate Packer for Executables. It is a popular open-source executable packer that compresses and reduces the size of executables, including Windows .exe files, Linux ELF binaries, and more. UPX achieves this by compressing the code, data, and resources within an executable and then adding a small decompression stub that unpacks the code at runtime, allowing the program to run as if it were never compressed.
> 
> Key Points about UPX:
> 
> - Packer: It compresses the executable to reduce its size.
> - Unpacker: UPX can also decompress packed executables, provided they were originally packed with UPX and the header is not corrupted.
> - Common Usage: It's widely used for legitimate purposes, such as reducing the size of executables for distribution. However, it’s also commonly used by malware authors to obfuscate their malicious code, making static analysis more difficult.
```bash
strings packed | grep UPX
$Info: This file is packed with the UPX executable packer http://upx.sf.net
```

- We attempted to unpack the binary using UPX:

```bash
upx -d packed
upx: packed: CantUnpackException: l_info corrupted
```
- The unpacking failed due to a corrupted UPX header. To fix this, we opened the binary in a hex editor and found that the UPX identifier was corrupted (expected UPX!, but it showed UPY$). We manually corrected the header.

In the hex editor, we changed the incorrect bytes 55505924 (UPY$) at offsets EEh and EFh to 55505821 (UPX!). After saving the changes, the unpacking process worked as expected:

```bash
upx -d packed
Unpacked 1 file.
```

After unpacking, we loaded the binary into Binary Ninja. The decompiler showed a main function that copied suspicious strings to the stack and then printed "error". However, further analysis showed that this was a red herring. The real action was hidden behind a jump instruction in the assembly code.
```bash
./packed         
> error
```

By patching out the jump instruction with NOPs and running the binary in a debugger, we were able to intercept the final output on the stack. The stack contained the string ```Malware_Analysis```.
```bash
──────────────────────────────────────────────────────────────────────────────[ STACK ]───────────────────────────────────────────────────────────────────────────────
00:0000│ rsp 0x7fffffffdd70 ◂— 0x5f657261776c6106
01:0008│-088 0x7fffffffdd78 ◂— 0x736973796c616e41 ('Analysis')
```
Swap the endianness and change from Hex to UTF-8.
![image](https://github.com/user-attachments/assets/18eb4dd5-fb03-4881-9528-6a2c01a5a0a1)

## Flag
```CyGenixCTF{Malware_Analysis}```
