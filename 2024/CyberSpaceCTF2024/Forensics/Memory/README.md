# Memory
## Description
> I left the image of the flag in the desktop but somehow it disappeared, can you help me recover it?
> 
> https://drive.google.com/file/d/1OqrNosho2yYFSu05sNKamQ1VeQcDzRVn/view?usp=sharing
>
> Incase you cannot download using the link given above, <a href="https://drive.google.com/file/d/1hGiy8z73YPDV5E0OnZYA-MJZ5WcBzskT/view?usp=sharing">here</a> is a mirror link.

## Challenge Overview
We were given a `mem.dmp` file which is a memory dump files. We can use Volatility to do memory analysis. The challenge description is hinting to search for the flag in `Desktop` and it also mention something about the flag has disappeared. Probably it had been deleted or something else. The flag is an image file so it can be `flag.jpg`, `flag.png`, etc.

### `pslist`
```bash
vol.exe" -f mem.dmp windows.pslist.PsList
```
Not many things to explore other than the Notepad program that is running. 
```
3212 2776 notepad.exe 0xe50761cde4c0 5 - 1 False 2024-08-26 20:07:44.000000  N/A Disabled 
```
### `cmdline`
There is a note.txt inside `C:\Users\gg\Desktop`. Probably the same directory as the flag.
```
3212 notepad.exe "C:\Windows\system32\NOTEPAD.EXE" C:\Users\gg\Desktop\note.txt 
```
### `filescan`
Flag image file is not available using `filescan`, so we can not dump the file. 
### `mftparser`
I tried to use mftparser in Volatility2 to see if the flag file content was saved in the MFT records. Unfortunately, we only found the fake flag which is the content of `note.txt`. We found out that the flag file is named `flag.enc`, maybe due to some encryption algorithm.
```
MFT entry found at offset 0x7208dc00
Attribute: In Use & File
Record Number: 26783
Link count: 1


$STANDARD_INFORMATION
Creation                       Modified                       MFT Altered                    Access Date                    Type
------------------------------ ------------------------------ ------------------------------ ------------------------------ ----
2024-08-26 02:06:25 UTC+0000 2024-08-26 02:06:25 UTC+0000   2024-08-26 02:06:25 UTC+0000   2024-08-26 19:58:48 UTC+0000   Archive

$FILE_NAME
Creation                       Modified                       MFT Altered                    Access Date                    Name/Path
------------------------------ ------------------------------ ------------------------------ ------------------------------ ---------
2024-08-26 02:06:25 UTC+0000 2024-08-26 02:06:25 UTC+0000   2024-08-26 02:06:25 UTC+0000   2024-08-26 02:06:25 UTC+0000   Users\gg\Desktop\note.txt

$OBJECT_ID
Object ID: 77b25782-9063-ef11-b930-0800279a5d3b
Birth Volume ID: 80000000-4800-0000-0000-180000000100
Birth Object ID: 30000000-1800-0000-4e6f-7468696e6720
Birth Domain ID: 68657265-2c20-736f-7272-792e20637363

$DATA
0000000000: 4e 6f 74 68 69 6e 67 20 68 65 72 65 2c 20 73 6f   Nothing.here,.so
0000000010: 72 72 79 2e 20 63 73 63 74 66 7b 6e 6f 74 5f 72   rry..csctf{not_r
0000000020: 65 61 6c 6c 6c 79 5f 74 68 65 5f 66 6c 61 67 7d   eallly_the_flag}


***************************************************************************
***************************************************************************
MFT entry found at offset 0x3edf5800
Attribute: In Use & File
Record Number: 4534
Link count: 1


$STANDARD_INFORMATION
Creation                       Modified                       MFT Altered                    Access Date                    Type
------------------------------ ------------------------------ ------------------------------ ------------------------------ ----
2024-08-26 20:06:32 UTC+0000 2024-08-26 20:06:32 UTC+0000   2024-08-26 20:06:32 UTC+0000   2024-08-26 20:06:32 UTC+0000   Archive

$FILE_NAME
Creation                       Modified                       MFT Altered                    Access Date                    Name/Path
------------------------------ ------------------------------ ------------------------------ ------------------------------ ---------
2024-08-26 20:06:32 UTC+0000 2024-08-26 20:06:32 UTC+0000   2024-08-26 20:06:32 UTC+0000   2024-08-26 20:06:32 UTC+0000   Users\gg\Desktop\flag.enc
```
## Solution
I tried to search for "flag" inside the `mem.dmp` using `strings` and output it to a text file. Since the output is too big, I need to filter to specific keyword such as `flag`. I found a Powershell script that related to `flag.jpg`.

```powershell
$ifPath = [System.IO.Path]::Combine([System.Environment]::GetFolderPath('Desktop'), 'flag.jpg')
$efPath = [System.IO.Path]::Combine([System.Environment]::GetFolderPath('Desktop'), 'flag.enc')
$aes = New-Object System.Security.Cryptography.AesManaged
$aes.KeySize = 256
$aes.BlockSize = 128
$aes.GenerateKey()
$aes.GenerateIV()
$cee = [System.Convert]::ToBase64String($aes.Key)
$vee = [System.Convert]::ToBase64String($aes.IV)
$content = [System.IO.File]::ReadAllBytes($ifPath)
$encryptor = $aes.CreateEncryptor($aes.Key, $aes.IV)
$encryptedData = $encryptor.TransformFinalBlock($content, 0, $content.Length)
$encryptedBase64 = [System.Convert]::ToBase64String($encryptedData)
[System.IO.File]::WriteAllText($efPath, $encryptedBase64)
[System.Environment]::SetEnvironmentVariable("ENCD", $encryptedBase64, [System.EnvironmentVariableTarget]::User)
[System.Environment]::SetEnvironmentVariable("ENCK", $cee, [System.EnvironmentVariableTarget]::User)
[System.Environment]::SetEnvironmentVariable("ENCV", $vee, [System.EnvironmentVariableTarget]::User)
if (Test-Path $ifPath) {
    Remove-Item $ifPath -Force
```

- This PowerShell script is used to encrypt `flag.jpg` on the user's desktop using AES (Advanced Encryption Standard) with a 256-bit key and a 128-bit block size.
- After encryption, the script saves the encrypted content as a Base64 string in another file on the desktop and stores the encryption key, initialization vector (IV), and the encrypted data as environment variables
    - ENCD = encrypted data
    - ENCK = encryption key
    - ENCV = initialization vector (IV)
- If the original image file exists on the desktop, it is deleted using Remove-Item -Force.

![image](https://github.com/user-attachments/assets/9bd4ff48-668d-4a20-8626-22f92cf2b7c9)

![image](https://github.com/user-attachments/assets/a219e6c1-c71b-40a0-8093-ca11f6afa910)

## Flag
```
csctf{p0w3r$h3ll_$@v3d_3v3ry7h1ng_1n_3nv@r$!_Congr@tul@t10n$!}
```
