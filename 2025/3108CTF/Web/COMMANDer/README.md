# COMMANDer

> Terminal lama ini menyimpan biodata seseorang bersama rahsianya. Namun, rahsia itu hanya akan terbuka kepada mereka yang tahu menggunakan arahan yang tepat. Mampukah anda menguasai terminal ini untuk membongkar kebenaran?
>
> https://komander.bahterasiber.my


## Solution

We were given 4 questions to answer correctly, however, it is not as straightforwrd as you think. In order to get the flag, you need to send a secret command. You can check the options by checking the response for `/api/pilihan`.

```js
const fetchOptions = () => {
    fetch('/api/pilihan')
        .then((data) => data.json())
        .then((res) => {
            availableOptions = res.allPossibleCommands;

        })
        .catch(() => {
            availableOptions = undefined;
        })
}
```
We can see that there is a secret option called `RAHSIA: OperationOatmeal`.
<img width="1354" height="336" alt="image" src="https://github.com/user-attachments/assets/837882fe-f840-44c9-8554-9e101b4222e5" />


<img width="985" height="408" alt="image" src="https://github.com/user-attachments/assets/09124c51-3f35-4f26-b9e2-36457eff03e2" />

## Flag
```
3108{0p3R4T10n_O@Tm34l_1bR4h1M_1sM@1L}
```
