# Pretty Malicious Log
## Description
> I was trying to install the adobe crack and many weird things happened to my PC. Can you analyze the log and figure out what's going on?
> 
> https://drive.google.com/file/d/1ucky78xmJZBxoEYQJq9y6ayRfNWvilBk/view?usp=sharing
> 
> nc pretty-malicious-log.challs.csc.tf 1337

## Solution
```
ncat pretty-malicious-log.challs.csc.tf 1337
== proof-of-work: enabled ==
please solve a pow first
You can run the solver with:
    python3 <(curl -sSL https://goo.gle/kctf-pow) solve s.AE5X.AACsIe2E64c1uYg0pOTjN894
===================

Solution? s.AABov2k9+PgGDGX1J++ZsQ7CgTuqhEen0wJDVsqvgOle3eqXWZ2XEXiTkllyIuO1yy1qIPsK5vjErP0VehJ0OgkPUptb6JXql2boZlWwXuiDNueEikK5HU058qMiZ70Cip7hzHtAgoyB/oxLtjta/vZMrehka64zpuG+bN4bOG8o/uzF9wRIxYCyYfLL+UfLe7vejKLqP+vRqgcMnQ5Dnzxe
Correct
```
### Question 1
```
What program produced this log file?
Your answer: Process Monitor
```
You can ask ChatGPT for the answer.
> A .PML file is typically produced by Process Monitor, a system monitoring tool from Microsoft. Process Monitor is part of the Sysinternals suite and is used for real-time monitoring of file system, registry, and process/thread activity on a Windows system.

### Question 2
```
How many registry keys got successfully modified by the malware?
Your answer: 13
```
We know that the malware will be related to the cracked Adobe program. From Process Tree, we can see `adobe.exe` program with PID `1184`, being called by Explorer.exe (PID 3440) and have two executables mOkkYMEs.exe (PID 6988), pcgsoUwQ.exe (PID 6776)

![image](https://github.com/user-attachments/assets/4bb6938b-e8b5-4d9d-946e-9a5de102b85c)

Filter:
- Operation is RegSetValue
- Result is SUCCESS
- PPID is 1184
- plus 1 for adobe.exe

![image](https://github.com/user-attachments/assets/3045d059-9b1e-4b56-ac9b-43f00d9594ac)
![image](https://github.com/user-attachments/assets/3d9768df-4c40-4d54-9ce2-78e130d2b6c9)

### Question 3:

```
What is the MITRE ID of the persistence technique used by the malware?
Your answer: T1547.001
```
![image](https://github.com/user-attachments/assets/f1d2ab60-e13f-4b00-b684-c69c6162104b)

The registry path `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\` is often used by malware to achieve persistence on a system. According to MITRE, the technique is `Registry Run Keys / Startup Folder (T1547.001)`. This technique involves adversaries using the Windows registry to store entries under Run keys, ensuring that their malicious software is executed every time the user logs in.

References:
https://attack.mitre.org/techniques/T1547/001/
```
Question 4:
What is the name of the file that is added to autoruns by the malware?
Your answer: mOkkYMEs.exe
```
`adobe.exe` has two executables but only one is successful which is `mOkkYMEs.exe`. 
```
Question 5:
Which thread ID is responsible to create the environment for malware to run?
Your answer: 5352
```

![image](https://github.com/user-attachments/assets/26f4c8dd-0e83-43e0-a973-06078fd19595)

We need to analyze `Explorer.exe` since that is the program called `adobe.exe`. Upon inspection, there is one log that is bold which is related to Virtual Desktop.
## Flag
```
CSCTF{Pr0cm0n_1s_4_h3lpFul_sy5int3rn4l!_0x22defba1}
```
