# Silent Watcher

## Description
> Beware, pirates. Every step you take is being carefully logged. Your actions are under constant surveillance, and your next move might reveal more than you intend. Start your investigation from here, but tread carefully.
> 
> https://simple.uctf.ir/

## Challenge Overview
We were given a simple website that shows a message and our User-Agent. Maybe we can do some code execution on `User-Agent` header. 

![image](https://github.com/user-attachments/assets/69aa1d71-e095-4c9f-9d74-195c9d0ca3d9)

## Solution
Just need to inject Javascript at the User-Agent header. I tried to use `<script>alert(1)</script>` and it gave us the popup message. The flag will be shown after that. 


![image](https://github.com/user-attachments/assets/a80e1c02-47ee-4a53-831e-920239d4c01f)

![image](https://github.com/user-attachments/assets/15fe3e66-5e25-4278-a9b0-fd2fb3eddd9a)

![image](https://github.com/user-attachments/assets/bbd7f81a-e910-42c4-b808-3da155b86c8b)

## Flag
```
uctf{Ir4n_Masal_County}
```
