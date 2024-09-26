# No Paste
## Description
> "If you spend too much time thinking about a thing, you'll never get it done. Paste it up, cut it out, and just do it" — Unknown
>
> https://paste.h7tex.com/

![image](https://github.com/user-attachments/assets/ee0953f4-ee29-423a-9a20-39066e5c91ce)

![image](https://github.com/user-attachments/assets/f9d42b53-a0b9-455a-9a96-9ec4339e020b)

```js
function submitInput() {
    const input = document.getElementById('challengeInput').value;
    const submitUrl = '/submit?input=' + encodeURIComponent(input);
    
    fetch(submitUrl, { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            const resultElement = document.getElementById('result');
            if (data.success) {
                resultElement.textContent = 'Flag: ' + data.flag;
            } else {
                resultElement.textContent = data.message;
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

document.getElementById('challengeInput').addEventListener('paste', event => event.preventDefault());
document.getElementById('challengeInput').addEventListener('keydown', event => event.preventDefault());
```

```js
const _0x4c3e23 = [
    '1324128AFJEVv', '7068GqiGjD', 'challengeInput', '2125DmXkHA',
    'result', 'textContent', 'value', 'POST', '5588288xDHxaF', 
    'bypass123', 'then', 'addEventListener', 'getElementById', 
    '/submit?input=', 'Flag: ', 'error', '1026jodAtA', '393500Fwnrwo', 
    'paste', '793504lbHmgC', '32613VrGzuS', 'flag', '801iQqFPw', 
    'success', 'keydown', '965970xJmNwA'
];
```
![image](https://github.com/user-attachments/assets/bd54ed79-5e1e-42b9-b71e-d8cf929b6552)

## Flag
```
H7CTF{h@ck_th3_sy$t3m}
```
