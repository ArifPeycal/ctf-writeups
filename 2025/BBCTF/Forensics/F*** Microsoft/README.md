# F*** Microsoft
> OMG. I HATE WINDOWS UPDATE. HOW CAN YOU AUTO UPDATE WHEN IM 80% DONE WITH MY ASSIGNMENT. I DIDN’T SAVE ANYTHING, IT BETTER AUTO RECOVERS.
> Author: Identities

## Solution
We get an AD1 file to investigate. From the description looks like we are going to focus on Microsoft Office software like Words or Excel. So just Google, where is the location for autosaved files.

![image](https://github.com/user-attachments/assets/9d8dc6de-aaa1-4512-8f39-f10ecb5aa08c)

Go to this path and you can find the AutoRecovery (.asd) file for `CTF Assignment.docx`. But, if you only export this folder, you will get an error that says you need to open in its original location, something like that.
![image](https://github.com/user-attachments/assets/bb1e61d4-41fe-47b1-a7dc-0bf9a4e97e44)


Make sure to export the original `CTF Assignment.docx` which you can found in `C://Users/kali/Desktop/Assignment`.

![image](https://github.com/user-attachments/assets/0a501047-538d-404a-96eb-9a36b0951959)

Then, just follow what Gemini said just now, open `CTF Assignment.docx`, go to File > Info > Manage Document > Recover Unsaved Documents. 

![image](https://github.com/user-attachments/assets/ae42548f-15f5-4228-b51c-ddb8d3074622)

## Flag
```
bbctf{TH@NkS_FOr_tHi$_Fea7uR3_,_mY_AS5iGnMeNT_IsNt_G0nE}
```
