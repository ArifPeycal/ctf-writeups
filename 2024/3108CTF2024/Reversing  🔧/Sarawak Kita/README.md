# Sarawak Kita 🔧
## Description
> Ada pendapat yang menyatakan bahawa Kuching mendapat nama sempena sebatang sungai kecil, Sungai Kuching yang mengalir di antara Muzium Cina dan Kuil Tua Pek Kong. Sungai Kuching pula barangkali memperoleh nama daripada Kucing Hutan yang kerap mengunjunginya. Sungai tersebut juga berhampiran dengan sebuah bukit yang banyak ditumbuhi oleh pokok Buah Mata Kucing. Lantaran tersebut ianya diberi nama Bukit Mata Kucing. Tapi ini bukan tentang kisah Kuching, ini kisah bagaimana ingin mendapatkan 'flag' di dalam document yang berbahaya.

## Challenge Overview
![image](https://github.com/user-attachments/assets/5fc1cea0-4154-4f08-baee-e09bb5c98b83)

## Solution
```bash
olevba --deobf Sarawak_KITA.doc
```
```vba
Rem Attribute VBA_ModuleType=VBADocumentModule
Option VBASupport 1
Option Explicit

Private Declare Function ShellExecute Lib "shell32.dll" Alias "ShellExecuteA" ( _
         ByVal hwnd As Long, _
         ByVal lpOperation As String, _
         ByVal lpFile As String, _
         ByVal lpParameters As String, _
         ByVal lpDirectory As String, _
         ByVal lpShowCmd As Long) As Long
         
 Dim command
  command = "MwAxADAAOAB7AEsAdQBjAGgAMQBuAGcAXwAxAGIAdQBfAE4AMwBnADMAcgAxAF8AUwA0AHIANAB3ADQAawB9AA=="""""
  Shell.Run command, 0, True

Sub AutoOpen()
Call ShellExecute(0, "Open", "calc.exe", "", "", 1)

End Sub
```
## Flag
```
3108{Kuch1ng_1bu_N3g3r1_S4r4w4k}
```
