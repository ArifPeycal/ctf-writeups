# Social Distancing
## Description
> We all remember the time of social distancing and quarantines. How about some quarantined malware? Bet you can't understand what it entails!

## Challenge Overview
We receive a zip that contains a folder named `Quarantine` with several subfolders named `Resources`, `Resource Data` and `Entries`. There are files inside the subfolders but I do not recognize the file format. By searching the first magic bytes of each file, I found a website that contains the file format for one of the files. (https://hexacorn.com/d/DeXRAY.pl)

`dexray.pl` is a Perl script that has several functionalities, one of which is that it can decrypt files that are placed in quarantine by antivirus or security products. These files are often encrypted or obfuscated to prevent malicious code from running.

## Solution
We need to run the script and it will give us a decrypted file. But, Windows Defender quickly detects it as malicious if we try to open it. So, I send the file to CyberChef to read the file content. I found out that the file inside `ResourceData` contains some Powershell script.
```powershell
$hidden = @"
UEsDBAoAAAAAAOCYuCg8z1FoRAAAAEQAAAAJABwAZWljYXIuY29tVVQJAAOUYCw5y1zNZnV4CwAB
BAAAAAAEAAAAAFg1TyFQJUBBUFs0XFBaWDU0KFBeKTdDQyk3fSRFSUNBUi1TVEFOREFSRC1BTlRJ
VklSVVMtVEVTVC1GSUxFISRIK0gqUEsDBAoAAAAAAE8HG1mJ3nc0MQAAADEAAAAEABwAZmxhZ1VU
CQAD9VzNZtVczWZ1eAsAAQQAAAAABAAAAABDU0NURnt5MHVfdW4tcXU0cmFudDFuM2RfbXlfc2Ny
MVB0IV8weDkxYTNlZGZmNn0KUEsBAh4DCgAAAAAA4Ji4KDzPUWhEAAAARAAAAAkAGAAAAAAAAQAA
AKSBAAAAAGVpY2FyLmNvbVVUBQADlGAsOXV4CwABBAAAAAAEAAAAAFBLAQIeAwoAAAAAAE8HG1mJ
3nc0MQAAADEAAAAEABgAAAAAAAEAAACkgYcAAABmbGFnVVQFAAP1XM1mdXgLAAEEAAAAAAQAAAAA
UEsFBgAAAAACAAIAmQAAAPYAAAAAAA==
"@

$decodedBytes = [System.Convert]::FromBase64String($hidden)

$zipFilePath = "malicious.zip"
[System.IO.File]::WriteAllBytes($zipFilePath, $decodedBytes)

Write-Output "File saved as $zipFilePath"
```
Decode the base64 string and get the flag.
## Flag
```
CSCTF{y0u_un-qu4rant1n3d_my_scr1Pt!_0x91a3edff6}
```
