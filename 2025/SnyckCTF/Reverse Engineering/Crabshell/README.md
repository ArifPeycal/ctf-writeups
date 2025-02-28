# Crabshell

> Author: @Kkevsterrr
>
> Crabshells can be pretty tough stuff.

## Solution
We were given an ELF file to analyze. Open it in Ghidra, and we can see that this code is compiled using Rust. The ELF requires you to send 16 bytes key to the server and it will give you the flag.
```c
/* crabshell::main */

void crabshell::main(void)

{
  char *pcVar1;
  undefined auVar2 [16];
  long local_f0;
  undefined8 local_e8;
  undefined8 local_e0;
  undefined **local_d8;
  undefined8 uStack_d0;
  undefined *local_c8;
  undefined auStack_c0 [8];
  undefined8 uStack_b8;
  undefined4 uStack_b0;
  undefined4 uStack_ac;
  undefined4 local_a8;
  undefined4 uStack_a4;
  undefined4 uStack_a0;
  undefined4 uStack_9c;
  undefined4 local_98;
  undefined4 uStack_94;
  undefined4 uStack_90;
  undefined4 uStack_8c;
  undefined8 local_88;
  undefined local_78 [16];
  undefined local_68 [16];
  undefined local_58 [8];
  undefined4 uStack_50;
  undefined4 uStack_4c;
  undefined local_48 [8];
  undefined4 uStack_40;
  undefined4 uStack_3c;
  undefined4 local_38;
  undefined4 uStack_34;
  undefined4 uStack_30;
  undefined4 uStack_2c;
  undefined8 local_28;
  undefined local_20 [16];
  
  local_78._8_8_ = local_78._0_8_;
  local_d8 = &PTR_DAT_00157db8;
  uStack_d0 = 1;
  local_c8 = (undefined *)0x8;
  _auStack_c0 = ZEXT816(0);
  std::io::stdio::_print(&local_d8);
  local_f0 = 0;
  local_e8 = 1;
  local_e0 = 0;
                    /* try { // try from 001079d6 to 00107a0d has its CatchHandler @ 00107c47 */
  local_78._0_8_ = std::io::stdio::stdin();
  auVar2 = std::io::stdio::Stdin::read_line(local_78,&local_f0);
  if ((auVar2 & (undefined  [16])0x1) == (undefined  [16])0x0) {
    auVar2 = core::str::<impl_str>::trim_matches(local_e8,local_e0);
    pcVar1 = auVar2._0_8_;
    if (auVar2._8_8_ == 0x10) {
      if ((((*pcVar1 == '1') && (*(long *)(pcVar1 + 1) == 0x1f221731232d1f26)) &&
          (*(int *)(pcVar1 + 9) == 0x64681332)) &&
         (((pcVar1[13] == 'd' && (pcVar1[14] == 'h')) && (pcVar1[15] == 'h')))) {
        _local_48 = ZEXT816(0);
        _local_58 = ZEXT816(0);
        local_68 = ZEXT816(0);
        local_78 = ZEXT816(0);
        local_28 = 0;
        local_38 = 0x67452301;
        uStack_34 = 0xefcdab89;
        uStack_30 = 0x98badcfe;
        uStack_2c = 0x10325476;
                    /* try { // try from 00107aa8 to 00107ac4 has its CatchHandler @ 00107c2e */
        md5::consume(local_78,&DAT_0014940b,0x27);
        local_88 = local_28;
        local_98 = local_38;
        uStack_94 = uStack_34;
        uStack_90 = uStack_30;
        uStack_8c = uStack_2c;
        local_a8 = local_48._0_4_;
        uStack_a4 = local_48._4_4_;
        uStack_a0 = uStack_40;
        uStack_9c = uStack_3c;
        uStack_b8._0_4_ = local_58._0_4_;
        uStack_b8._4_4_ = local_58._4_4_;
        uStack_b0 = uStack_50;
        uStack_ac = uStack_4c;
        local_c8 = local_68._0_8_;
        auStack_c0 = local_68._8_8_;
        local_d8 = local_78._0_8_;
        uStack_d0 = local_78._8_8_;
                    /* try { // try from 00107b13 to 00107b76 has its CatchHandler @ 00107c30 */
        md5::Context::compute(local_20,&local_d8);
        local_78._8_8_ = <>::fmt;
        local_78._0_8_ = local_20;
        local_d8 = &PTR_DAT_00157df0;
        uStack_d0 = 2;
        _auStack_c0 = ZEXT816(1);
        local_c8 = local_78;
        std::io::stdio::_print(&local_d8);
      }
      else {
        local_d8 = &PTR_DAT_00157de0;
        uStack_d0 = 1;
        local_c8 = &DAT_00000008;
        _auStack_c0 = ZEXT816(0);
                    /* try { // try from 00107bd2 to 00107bdc has its CatchHandler @ 00107c30 */
        std::io::stdio::_print(&local_d8);
      }
    }
    else {
      local_d8 = &PTR_DAT_00157e10;
      uStack_d0 = 1;
      local_c8 = &DAT_00000008;
      _auStack_c0 = ZEXT816(0);
                    /* try { // try from 00107b9f to 00107ba9 has its CatchHandler @ 00107c47 */
      std::io::stdio::_print(&local_d8);
    }
    if (local_f0 != 0) {
      __rust_dealloc(local_e8,local_f0,1);
    }
    return;
  }
                    /* try { // try from 00107c07 to 00107c2b has its CatchHandler @ 00107c32 */
  local_d8 = auVar2._8_8_;
  core::result::unwrap_failed
            (&DAT_001493b0,0x2b,&local_d8,&PTR_drop_in_place<std_io_error_Error>_00157d98,
             &PTR_DAT_00157dc8);
  do {
    invalidInstructionException();
  } while( true );
}
```

In order to get the correct 16 bytes, we need to refer to this code:


```c
if ((((*pcVar1 == '1') && (*(long *)(pcVar1 + 1) == 0x1f221731232d1f26)) &&
          (*(int *)(pcVar1 + 9) == 0x64681332)) &&
         (((pcVar1[13] == 'd' && (pcVar1[14] == 'h')) && (pcVar1[15] == 'h'))))
```

From the code, the expected bytes are:

|Address Offset	| Expected Byte(s)
|---|----
|0	| ('1') 0x31
|1 - 8	| 0x1f221731232d1f26
|9 - 12	| 0x64681332
|13	 | ('d') 0x64
|14	 | ('h') 0x68
| 15	 | ('h') 0x68


When converted to raw bytes (little-endian ordering where needed), the sequence is:
```bash
b'\x31\x26\x1f\x2d\x23\x31\x17\x22\x1f\x32\x13\x68\x64\x64\x68\x68'
```
Create a python script to send the key to ELF file.
```py
import subprocess

# Define the 16-byte key
key = b'\x31\x26\x1f\x2d\x23\x31\x17\x22\x1f\x32\x13\x68\x64\x64\x68\x68'

# Run the binary and send the key
process = subprocess.Popen(["./crabshell"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Send the key
stdout, stderr = process.communicate(input=key)

# Print the output
print(stdout.decode())
print(stderr.decode())

# Enter the 16-byte key: 
# Congratulations! flag{cc811d4486decc3379dd13688a46603f}
```

## Flag
```
flag{cc811d4486decc3379dd13688a46603f}
```
