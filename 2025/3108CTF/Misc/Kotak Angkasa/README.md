# Kotak Angkasa

> “Di dalam ruang angkasa, di tengah gelap galaksi, tersembunyi sebuah kotak misteri. Kotak ini tidak sekadar permainan biasa – ia menyimpan rahsia yang hanya dapat dipecahkan oleh minda tajam dan tangan yang cekap.
> 
> Sebagai pewaris ilmu Dr. Sheikh Muszaphar Shukor, angkasawan pertama Malaysia, Perwira ditugaskan untuk menyelesaikan teka-teki ini. Hanya mereka yang mampu menyusun Kotak Angkasa ke bentuk asalnya akan menemui koordinat rahsia untuk membuka kunci bendera kejayaan.”
> 
> http://5.223.66.228:3001/

## Solution

We were given a website that shows a Rubik's Cube being scrambled, and we need to solve the cube. Not sure if it is possible to get the flag by manually solving it, but the easiest way is to bypass the checking condition.

<img width="1333" height="683" alt="image" src="https://github.com/user-attachments/assets/e7d0ba31-6a54-4d22-ac97-91466800e855" />

There is Index.js that contains obfuscated JS code. Paste the code here to deobfuscate, https://obf-io.deobfuscate.io/

From the code, we can conclude that the website will connect to a server via WebSockets and create a scrambled cube on load. It will check if all faces are the same color and display the flag when solved.

```js
socket.on('flag', _0x38a0cf => {
    addSuccessLog("🏴 FLAG: " + _0x38a0cf.flag);
    showFlag(_0x38a0cf.flag, _0x38a0cf.message, _0x38a0cf.solveTime);
});
```

checkIfSolved() checks each face; each face must have all 9 stickers the same colour.

```js
for (let face = 0; face < 6; face++) {
    const firstColor = getFaceColor(face, 0);
    for (let sticker = 0; sticker < 9; sticker++) {
        if (getFaceColor(face, sticker) !== firstColor) return false;
    }
}
return true;
```

Steps to bypass

1. Open the browser console (F12 → Console).

2. Run this to get the current cube object:
```
getCurrentCubeState()
```
<img width="731" height="158" alt="image" src="https://github.com/user-attachments/assets/f9f5ff5a-82dc-470d-a023-e970d9c579a0" />


3. Modify it to a solved state, where each face has all 9 stickers the same color:
```
const solvedState = {
    front: Array(9).fill('blue'),
    back: Array(9).fill('green'),
    left: Array(9).fill('white'),
    right: Array(9).fill('yellow'),
    top: Array(9).fill('orange'),
    bottom: Array(9).fill('red')
};
```
4. Send it to the server:
```
socket.emit('cubeState', solvedState)
```
<img width="1332" height="649" alt="image" src="https://github.com/user-attachments/assets/e00f6f4b-72f5-4f08-9004-dff075dde778" />

## Flag

```
3108{Sh31kh_MuZ4ph4r_5p4c3_73219}
```
