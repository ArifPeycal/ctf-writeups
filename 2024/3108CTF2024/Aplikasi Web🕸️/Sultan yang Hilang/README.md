# Sultan yang Hilang 🕸️
## Description
> Berikut merupakan senarai pemerintahan Sultan-Sultan Kelantan, yang telah memimpin negeri ini sejak abad ke-18. Setiap Sultan membawa kisah dan peranannya yang tersendiri dalam membentuk sejarah Kelantan. Namun, terdapat Sultan yang hilang dari senarai ini.
>
> https://f2add8dd3a.bahterasiber.my/

## Challenge Overview
![image](https://github.com/user-attachments/assets/47454b61-995c-4a3a-9d24-5cc8663369b0)
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Senarai Sultan Kelantan</title>
    </head>
    <body>
        <h1>Senarai Sultan Kelantan</h1>
        <ul id="sultan-list"></ul>

        <script>
            const sultanYears = [1763, 1795, 1800, 1835, 1837, 1886, 1890, 1899, 1920, 1944, 1960, 1979, 2010];
            
            sultanYears.forEach(year => {
                fetch(`/api/v1/sultan/${year}`)
                    .then(response => response.json())
                    .then(data => {
                        const list = document.getElementById('sultan-list');
                        const listItem = document.createElement('li');
                        if (data.error) {
                            listItem.textContent = `${data.error}`;
                        } else {
                            listItem.textContent = `${data.nama}`;
                        }
                        list.appendChild(listItem);
                    })
                    .catch(error => console.error('Error:', error));
            });
        </script>
    </body>
</html>
```
![image](https://github.com/user-attachments/assets/7a88a20c-cc28-449d-8656-08e7ee113458)

```json
{
    "flag": "3108{putera_sulong_Sultan_Ahmad}",
    "id": 1889,
    "nama": "Sultan Muhammad III",
    "tahun_pemerintahan": "1889-1890"
}
```

## Flag
```
3108{putera_sulong_Sultan_Ahmad}
```
