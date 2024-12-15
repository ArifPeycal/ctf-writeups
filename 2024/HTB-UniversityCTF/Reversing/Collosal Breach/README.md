# Collosal Breach
## Description
> A devastating data breach has occurred, in a remote satellite on the edge of the Frontier Cluster. You'll need to investigate the satellite, discover how the data was stolen, and finally discover what was stolen in order to prevent it falling into the wrong hands.

## Solution
```py
def decode_xor(data, key=0x19):
    # Decode the log data by XORing each byte with the key
    return ''.join(chr(ord(c) ^ key) for c in data)

# Replace this with your actual log content as a string
log_data = "ujin}zu|xkp}nqvxtpz}96vimujz}96kvvm6uj94ux|zqv9FKJQP_MFFKJQP_MFFKJQP_MF;FUJQP_MFFUJQP_MFFUJQP_MFFUJQP_MFQFUJQP_MFPFKJQP_MF;9FKJQP_MFFKJQP_MFFKJQP_MF'9q|`7mamzxm9q|`7mamz}96qvt|6ujz}9qm{ujz}9FUJQP_MF]|jrmviuj|zqv9FKJQP_MF;`vv9jli9{vppppFKJQP_MF;9FKJQP_MF'9q|uuv7mamzxm9q|uuv7mamz}96kvvm6x}xtwxwv9ixjj7mamx}xt9FKJQP_MFFKJQP_MFFKJQP_MFFKJQP_MFFKJQP_MF#9FKJQP_MFFKJQP_MFFKJQP_MFFKJQP_MFFKJQP_MFFKJQP_MFFKJQP_MF;jli|kj*zlk*ixjjn)k}FKJQP_MF;FUZMKUFFUZMKUFa`zu|xk{`|9{`|7"
decoded_data = decode_xor(log_data)

print("Decoded Data:")
print(decoded_data)

```

```
    
Decoded Data:
ls
pwd
clear
id
whoami
cd /opt
ls
cd /root/
ls -la
echo _RSHIFT__RSHIFT__RSHIFT_"_LSHIFT__LSHIFT__LSHIFT__LSHIFT_H_LSHIFT_I_RSHIFT_" _RSHIFT__RSHIFT__RSHIFT_> hey.txt
cat hey.txt
cd /home/
ls
cd htb
ls
cd _LSHIFT_Desktop
ls
echo _RSHIFT_"yoo sup boiiii_RSHIFT_" _RSHIFT_> hello.txt
cat hello.txt
cd /root/adam
nano pass.txt
adam _RSHIFT__RSHIFT__RSHIFT__RSHIFT__RSHIFT_: _RSHIFT__RSHIFT__RSHIFT__RSHIFT__RSHIFT__RSHIFT__RSHIFT_"supers3cur3passw0rd_RSHIFT_"_LCTRL__LCTRL_xy
clear
bye bye
```


1. Who is the module's author?
2. What is the name of the function used to register keyboard events?
3. What is the name of the function that convers keycodes to strings?
4. What file does the module create to store logs? Provide the full path
5. What message does the module print when imported?
6. What is the XOR key used to obfuscate the keys? (e.g. 0x01, 0x32)
7. What is the password entered for 'adam'?
