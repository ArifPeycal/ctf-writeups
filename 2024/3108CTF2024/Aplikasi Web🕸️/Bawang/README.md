# Bawang 🕸️+🔍
## Description
> Kami nak makan nasi kandaq ja, member kami bagi natang ni, nak buat apa tak tau? Dia kata cari kat bawang?
>
> tmdjl5kyfzimrsrkkjisxybwb7664epxizxfz6hbivkg6k4a3x2svrad

## Challenge Overview
![image](https://github.com/user-attachments/assets/af4260ce-1773-4bc1-8f98-fae717229b8b)
![image](https://github.com/user-attachments/assets/d3197c65-801b-4d36-aadf-006134307ee7)

## Solution
```
function validateForm() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // The correct username and password (base64 encoded)
    var correctUsername = "bawang";
    var correctPassword = "bWVtYmF3YW5namVrZWpl"; // base64 encoded password

    // Check if the username matches
    if (username !== correctUsername) {
        alert("Invalid username or password");
        return false;
    }

    // Encode the input password to base64
    var encodedPassword = btoa(password);

    // Check if the password matches
    if (encodedPassword !== correctPassword) {
        alert("Invalid username or password");
        return false;
    }

    return true; // Allow the form to submit
}

```
bawang:membawangjekeje
![image](https://github.com/user-attachments/assets/dc6ee9e5-786a-4a8a-a501-6d77626bcfb8)
https://www.google.com/maps/place/Restoran+Nasi+Kandar+Line+Clear/@5.4198046,100.3326324,19z/data=!4m12!1m5!3m4!2zNcKwMjUnMTEuNyJOIDEwMMKwMTknNTcuMSJF!8m2!3d5.4199167!4d100.3325278!3m5!1s0x304ac3974ed8f2bd:0xb925fa81eb1b5041!8m2!3d5.419695!4d100.332504!16s%2Fg%2F1tttj4cm?entry=ttu&g_ep=EgoyMDI0MDgyOC4wIKXMDSoASAFQAw%3D%3D


![image](https://github.com/user-attachments/assets/a13361b7-5454-4228-b168-7af8b3df5026)


## Flag
```
3108{surrr_punya_tobat_jumpa}
```
