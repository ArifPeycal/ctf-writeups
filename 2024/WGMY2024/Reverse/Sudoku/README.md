# Sudoku 

> Easy stuff, frfr. You dont need to brute force or guess anything.
> 
> The final flag don't have any dot (.)
> 
> Author: Trailbl4z3r
> 
> View Hint
> Flag format: wgmy{md5 hash}

## Solution

First, I tried to see if the ELF file is also built using Python. Turns out it is, similar to the Stones.

```
strings sudoku | findstr "python"
```
```
Failed to pre-initialize embedded python interpreter!
Failed to allocate PyConfig structure! Unsupported python version?
Failed to set python home path!
Failed to start embedded python interpreter!
blib-dynload/_bz2.cpython-311-x86_64-linux-gnu.so
blib-dynload/_codecs_cn.cpython-311-x86_64-linux-gnu.so
blib-dynload/_codecs_hk.cpython-311-x86_64-linux-gnu.so
blib-dynload/_codecs_iso2022.cpython-311-x86_64-linux-gnu.so
blib-dynload/_codecs_jp.cpython-311-x86_64-linux-gnu.so
blib-dynload/_codecs_kr.cpython-311-x86_64-linux-gnu.so
blib-dynload/_codecs_tw.cpython-311-x86_64-linux-gnu.so
blib-dynload/_contextvars.cpython-311-x86_64-linux-gnu.so
blib-dynload/_decimal.cpython-311-x86_64-linux-gnu.so
blib-dynload/_hashlib.cpython-311-x86_64-linux-gnu.so
blib-dynload/_lzma.cpython-311-x86_64-linux-gnu.so
blib-dynload/_multibytecodec.cpython-311-x86_64-linux-gnu.so
blib-dynload/_typing.cpython-311-x86_64-linux-gnu.so
blib-dynload/resource.cpython-311-x86_64-linux-gnu.so
blibpython3.11.so.1.0
7libpython3.11.so.1.0
```
We can extract contents of the ELF file using `pyinstxtractor.py`

```py
python3 pyinstxtractor.py <filename>
```

![image](https://github.com/user-attachments/assets/a895707d-1085-4ca8-8cc0-dfc3a90bf75e)

There is one interesting file called `sudoku.pyc`. We can decompile using Pylingual.io.

TLDR;
The script generates a random substitution cipher key by shuffling the characters of a given alphabet. It then encrypts a plaintext message by replacing each character with its corresponding character from the shuffled key.

```
import random
alphabet = 'abcdelmnopqrstuvwxyz1234567890.'
plaintext = '0 t.e1 qu.c.2 brown3 .ox4 .umps5 over6 t.e7 lazy8 do.9, w.my{[REDACTED]}'

def makeKey(alphabet):
    alphabet = list(alphabet)
    random.shuffle(alphabet)
    return ''.join(alphabet)
key = makeKey(alphabet)

def encrypt(plaintext, key, alphabet):
    keyMap = dict(zip(alphabet, key))
    return ''.join((keyMap.get(c.lower(), c) for c in plaintext))
enc = encrypt(plaintext, key, alphabet)
```

There is also `out.enc` that contains the encrypted flag.

```
z v7o1 an7570 9d.tl3 7.4b 7n2pws .qodx v7oc ye68u m.7r, t728{09er1bzbs9sx5sosu7719besr39zscbx}
```
Basically, we need to iterate each char in plaintext and map it with the coresponing char in ciphertext. For example, `z` in ciphertext is `0` in plaintext, `v` is `t` in plaintext and so on. 

```
plaintext = '0 t.e1 qu.c.2 brown3 .ox4 .umps5 over6 t.e7 lazy8 do.9, w.my{[REDACTED]}'
ciphertext = 'z v7o1 an7570 9d.tl3 7.4b 7n2pws .qodx v7oc ye68u m.7r, t728{09er1bzbs9sx5sosu7719besr39zscbx}'
```

For this challenge, I only do manual mapping (skill issues xD).

```py
# The reverse mapping from encrypted text to plaintext
reverse_key_map = {
    't': 'w',
    '7': 'g',
    '2': 'm',
    '8': 'y',
    'z': '0',
    'v': 't',
    'g': '.',
    'o': 'e',
    '1': '1',
    'r': '9',
    'm': 'd',
    '8': 'y',
    '6': 'z',
    'e': 'a',
    'u': '8',
    'c': '7',
    'y': 'l',
    'o': 'e',
    '7': '.',
    'x': '6',
    'd': 'r',
    'q': 'v',
    '.': 'o',
    's': '5',
    'w': 's',
    'n': 'u',
    'b': '4',
    '4': 'x',
    'l': 'n',
    '9': 'b',
    '0': '2',
    '5': 'c',
    'a': 'q'
}

def decrypt(encrypted_text, reverse_key_map):
    return ''.join(reverse_key_map.get(c, c) for c in encrypted_text)
# Encrypted text
encrypted_text = 'z v7o1 an7570 9d.tl3 7.4b 7n2pws .qodx v7oc ye68u m.7r, t728{09er1bzbs9sx5sosu7719besr39zscbx}'

decrypted_text = decrypt(encrypted_text, reverse_key_map)

print("Decrypted message:", decrypted_text)
# Decrypted message: 0 t.e1 qu.c.2 brown3 .ox4 .umps5 over6 t.e7 lazy8 do.9, w.my{2ba914045b56c5e58..1b4a593b05746}
```

As you noticed `w.my{2ba914045b56c5e58..1b4a593b05746}` have 2 dots in the flag. We can deduce `w.my` is `wgmy` as in flag format. But since flag should be in md5 hash, it is not possible to have `g` in the flag. MD5 hash only have letter `a` until `f` and numbers from `0` to `9`

If you look closely at the alphabet list `alphabet = 'abcdelmnopqrstuvwxyz1234567890.`, there are missing alphabets which are `fghijk`. So I assume that the dots must be either one of this alphabets. You can check with the previous words such as `t.e1` (the), `qu.c.` (quick), `.ox4` (fox), `.umps5` (jumps), `t.e7` (the), `do.9` (dog).

So which one from `fghijk` should be in the flag? It should be `f` because `f` is the only valid char in MD5 hash. 

## Flag
```
wgmy{2ba914045b56c5e58ff1b4a593b05746}
```

