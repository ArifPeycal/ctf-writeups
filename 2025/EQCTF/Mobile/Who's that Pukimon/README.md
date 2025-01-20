# Who's that Pukimon

> Guess the correct pukimon
> 
> All 3 challenge share the same APK file.
> 
> Author: ks


## Overview
We were give an APK file to analyze. From `AndroidManifest.xml`, I see that there is MainActivity function at `io.eqctd.pukimon`. 

![image](https://github.com/user-attachments/assets/766a4f32-e284-47ea-9cca-b994c2f37265)

But, `MainActivity` didnt contain anything interesting so I change focus to `MainActivityKt`. Upon inspection, there is a base64 string that we can decode.

![image](https://github.com/user-attachments/assets/ebccf233-54a0-4f46-9ae6-421a04755a40)

## Flag
```
EQCTF{1Ts_Shr0oMr1sHiE!!!!}
```
