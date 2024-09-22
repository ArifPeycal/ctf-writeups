# Bad Blood
## Description
> Nothing is more dangerous than a bad guy that used to be a good guy. Something's going on... please talk with our incident response team.
>
> nc chal.competitivecyber.club 10001

## Challenge Overview
We were given `suspicious.evtx` to analyze. You can directly open the `evtx` file if you are using Windows but, I prefer to use `EvtxCmd` to extract data from `evtx` into `csv` file. 

```bash
EvtxECmd.exe -f "suspicious.evtx" --csv "c:\Downloads"
```


## Solution
```bash
Answer the following questions for the flag:
Q1. Forensics found post exploitation activity present on system, network and security event logs. What post-exploitation script did the attacker run to conduct this activity?
        Example answer: PowerView.ps1
>> Invoke-P0wnedshell.ps1
That makes sense.
```
You can use Timeline Explorer to open CSV file.
![image](https://github.com/user-attachments/assets/ea8f287a-3772-4332-b1a6-392a13fb7123)

![image](https://github.com/user-attachments/assets/903463d9-6ec0-473d-8377-6d01e8615903)

```bash
Q2. Forensics could not find any malicious processes on the system. However, network traffic indicates a callback was still made from his system to a device outside the network. We believe jack used process injection to facilitate this. What script helped him accomplish this?
        Example answer: Inject.ps1
>> Invoke-UrbanBishop.ps1
That makes sense.
```
![image](https://github.com/user-attachments/assets/61a323d8-7e5f-422e-bb68-2412bcfd215c)

```bash
Q3. We believe Jack attempted to establish multiple methods of persistence. What windows protocol did Jack attempt to abuse to create persistence?
        Example answer: ProtoName
>> WinRM
That makes sense.
```
![image](https://github.com/user-attachments/assets/762ff967-73b9-4246-b527-16fff2303e8e)

```bash
Q4. Network evidence suggest Jack established connection to a C2 server. What C2 framework is jack using?
        Example answer: C2Name
>> Covenant
That makes sense.
```
## Flag
```
pctf{3v3nt_l0gs_reve4l_al1_a981eb}
```
