# VeLoCiraptor
> Kelvin has been acting suspiciously lately when I walk past him. I wonder what kind of videos he’s been watching on his laptop...
>
> Author: warlocksmurf

## Challenge Overview
We were given a folder contains multiple subfolders and files replicating C drive.

![image](https://github.com/user-attachments/assets/bbf12996-e8eb-4db7-ae0f-2017e0fb054c)

## Solution
Since the title hints toward VLC (uppercase letters), we need to know where VLC folder is. Upon further inspection, there is a folder called `vlc` at `C\Users\kelvin\AppData\Roaming`. Inside it is a file `vlc-qt-interface.ini` which is a configuration file used by VLC Media Player to store settings related to the Qt interface (the graphical user interface or GUI) of VLC.

Open the config file and we can see several files, some have base64 encoded names. Decode it and get the flag. 
```
list=file:///C:/Users/kelvin/Videos/real%20homework/Garrys_Mod_2022.02.28_-_00.41.28.17.DVR_Trim.mp4,
file:///C:/Users/kelvin/Videos/real%20homework/marci%201%20shot.mp4,
file:///C:/Users/kelvin/Videos/real%20homework/Garrys_Mod_2022.02.28_-_00.31.14.16.DVR_Trim.mp4,
file:///C:/Users/kelvin/Videos/real%20homework/MG1ldzBya190UnVTdF9tMyF9.mp4,
file:///C:/Users/kelvin/Videos/real%20homework/RVFDVEZ7MXRzX3IzNExseV9o.mp4
```

## Flag
```
EQCTF{1ts_r34Lly_h0mew0rk_tRuSt_m3!}
```
