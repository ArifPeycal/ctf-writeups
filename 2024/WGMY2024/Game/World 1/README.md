# World 1

**credits to @manno593 for solving**

## Description
> Game hacking is back!
> 
> Can you save the princess?
> 
> White screen? That is a part of the challenge, try to overcome it.
> 
> Author: Trailbl4z3r & Monaruku
> 
> File: http://files.wargames.my/2024/World%20I.zip
> View Hint
> The category stand for Game Hacking, hack it!

## Solution
We were given an executable file which actually is a game created using RPG Maker MZ. You can play it as usual but you will not be able to defeat one enemy because it can one shot kill you. You need to find a way to modify the value of your character's attribute so you can withstand that attack or kill him before it kills you.

When you save your file, you can see a folder called `save`. There will be file with `.rmmzsave` extension which means it is a save file for RPG Maker MZ games. Since save file contains all info about your character, you can try modify the value in the save file.

Use save file editor like https://saveeditor.online/ to modify you character health and attack. Put any amount that you like. Download the new save file and replace the old one.

![image](https://github.com/user-attachments/assets/a66cb346-00c9-4842-bf7b-aee6e8f951fe)

If you currently playing, go to Main Menu and select Continue. Choose save file that you had edited and voila, you are basically immortal.

![image](https://github.com/user-attachments/assets/44f8c1cc-fb0d-4550-9146-393ee5154c95)

### Flag 1
You get flag 1 after defeating Tarnak. 

![image](https://github.com/user-attachments/assets/7e99391e-3a85-48cf-8b8a-03f355d30ec7)

### Flag 2
You get flag 2 after defeating Sillad.

![image](https://github.com/user-attachments/assets/0f1a36df-d8dc-487a-8524-d319dddf0a82)

### Flag 3 
You get flag 3 after defeating Rakan. The flag is in the chest at the back.

![image](https://github.com/user-attachments/assets/a436831a-af77-4118-bfff-4e90a9bbc208)

## Flag 4
You get flag 4 after defeating Baran. The flag is in the volcano. Flag 4 is (`43effd`).

![image](https://github.com/user-attachments/assets/32de1494-3462-4b40-81ec-6c5bf1c3543f)


### Flag 5
You get flag 5 after giving correct password the castle. The password is `wgmy` (the sequence of alphabet)

![image](https://github.com/user-attachments/assets/360d6fb1-e312-434a-acf1-802b20951069)

You will get a QR code that you can scan. Flag 5 is `3fcaac2}`
![image](https://github.com/user-attachments/assets/3cad214e-fb82-4ee8-b58e-6e0535b07c6c)


## Flag
```
wgmy{5ce7d7a7140ebabf5cd43effd3fcaac2}
```
