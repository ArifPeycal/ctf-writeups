# Sudirman Microphone Tuner

> Sudirman? Mikrofon pun boleh jadi senjata.

## Solution

We’re given a binary that looks like a simple program, but the description hints at a classic binary exploitation task.

Checking the binary in Ghidra shows a hidden function which will print the flag.

```
void secret_song(void) {
    system("cat /app/flag.txt");
    return;
}
```

This is a ret2win challenge. The plan:

1. Find the buffer overflow offset.

2. Overwrite the return address with the address of secret_song.

3. Get the flag.

## Step 1: Finding the Offset

You can use cyclic from pwntools. For my case, I already have a script that automates that task. The offset is 72 bytes.
<img width="802" height="468" alt="image" src="https://github.com/user-attachments/assets/b03ed977-d7aa-4b0e-aef5-52d64b6a6d89" />

### Step 2: Getting the Function Address

From `objdump -d` or Ghidra, the address of secret_song is `0x401196`.

### Step 3: Crafting the Payload

Payload structure:

[A * 72] + [address of secret_song]

### Step 4: Getting the Flag

Running the exploit prints the contents of `/app/flag.txt`, which gives the flag.

<img width="888" height="433" alt="image" src="https://github.com/user-attachments/assets/16f78902-71f8-413e-8f14-5e4e24816356" />

## Flag
```
3108{sud1rm4n_p3ny4ny1_t3rs0h0r} 
```
