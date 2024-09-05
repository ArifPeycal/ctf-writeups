# Merdeka 🕸️
## Description
> Ayuh nyanyikan lagu patriotik bersama sempena hari kemerdekaan Malaysia.

## Challenge Overview
![image](https://github.com/user-attachments/assets/2ff34352-91f7-4dc2-bf7a-92433a1441a8)

<details> 
  
  <summary>Source code for <code>index.php</code></summary>
  
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lagu Merdeka</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-image: url('bg.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }
        .navbar {
            margin: 20px;
        }
        .navbar a {
            padding: 10px 20px;
            margin: 0 10px;
            text-decoration: none;
            border: 2px solid black;
            background-color: rgba(255, 255, 255, 0.8);
        }
        .content {
            margin-top: 20px;
            width: 80%;
            height: auto;
            margin-left: auto;
            margin-right: auto;
            border: 2px solid black;
            padding: 20px;
            text-align: left;
            white-space: pre-wrap;
            background-color: rgba(255, 255, 255, 0.8);
        }
        .audio-player {
            margin-top: 20px;
            width: 80%;
            margin-left: auto;
            margin-right: auto;
        }
    </style>
    <script>
        function setPage(page) {
            const encodedPage = btoa(page);
            document.cookie = "page=" + encodedPage + ";path=/";
            location.reload();
        }
    </script>
</head>
<body>

<h1>Lagu Patriotik Malaysia</h1>
<a>Adakah anda tahu lagu-lagu merdeka</a>

<div class="navbar">
    <a href="javascript:void(0)" onclick="setPage('tanggal31.html')">Tanggal 31</a>
    <a href="javascript:void(0)" onclick="setPage('keranamu.html')">Keranamu Malaysia</a>
    <a href="javascript:void(0)" onclick="setPage('jalurgemilang.html')">Jalur Gemilang</a>
</div>

<div class="content">
    <pre>Buruh, nelayan dan juga petani
Gaya hidup kini dah berubah
Anak-anak terasuh mindanya
Lahir generasi bijak pandai
Pakar IT, pakar ekonomi
Jaguh sukan dan juga jutawan
Berkereta jenama negara
Megah menyusur di jalan raya
Alam cyber teknologi terkini
Kejayaan semakin hampiri
Biar di kota ataupun desa
Kita semua pasti merasa bangga
Keranamu kami mendakap tuah
Keranamu kami bangsa berjaya
Keranamu kami hidup selesa
Limpah budi kemakmuran negara
Keranamu kami bebas merdeka
Keranamu myawa dipertaruhkan
Keranamu rela kami berjuang
Demi bangsa kedaulatan negara
( ulang dari mula )
Keranamu Negara Malaysia
Malaysia...
Terima kasih Malaysia !</pre></div>

<div class="audio-player">
            <audio controls autoplay>
            <source src="audio/keranamu.mp3" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
    </div>

</body>
</html>
```
</details>

```js
    <script>
        function setPage(page) {
            const encodedPage = btoa(page);
            document.cookie = "page=" + encodedPage + ";path=/";
            location.reload();
        }
    </script>
```
The function encodes a provided string into Base64, stores it in a cookie named page, and then reloads the current page.

![image](https://github.com/user-attachments/assets/993fc600-70e5-43bd-9cdf-b123ab29b6bc)
![image](https://github.com/user-attachments/assets/c71609f3-0fbe-41b1-8887-0b627011fc2d)

```php
<?php

$page = 'keranamu.html';

if (isset($_COOKIE['page'])) {
    $page = base64_decode($_COOKIE['page']);
}

$audio_file = "";
switch ($page) {
    case 'tanggal31.html':
        $audio_file = "audio/tanggal31.mp3";
        break;
    case 'keranamu.html':
        $audio_file = "audio/keranamu.mp3";
        break;
    case 'jalurgemilang.html':
        $audio_file = "audio/jalurgemilang.mp3";
        break;
    default:
        $audio_file = "";
}

$content = "";

if (strpos($page, 'php://') === 0) {
    // Handle special PHP wrappers like php://filter
    $content = file_get_contents($page);
    $content = "<pre>" . htmlspecialchars($content) . "</pre>";
} elseif (file_exists($page)) {
    ob_start();
    if (pathinfo($page, PATHINFO_EXTENSION) === 'php') {
        // Execute the PHP file
        include($page);
    } else {
        // Render non-PHP files as plain text
        $content = htmlspecialchars(file_get_contents($page));
        echo "<pre>$content</pre>";
    }
    $content = ob_get_clean();
} else {
    $content = "Page not found.";
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lagu Merdeka</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-image: url('bg.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }
        .navbar {
            margin: 20px;
        }
        .navbar a {
            padding: 10px 20px;
            margin: 0 10px;
            text-decoration: none;
            border: 2px solid black;
            background-color: rgba(255, 255, 255, 0.8);
        }
        .content {
            margin-top: 20px;
            width: 80%;
            height: auto;
            margin-left: auto;
            margin-right: auto;
            border: 2px solid black;
            padding: 20px;
            text-align: left;
            white-space: pre-wrap;
            background-color: rgba(255, 255, 255, 0.8);
        }
        .audio-player {
            margin-top: 20px;
            width: 80%;
            margin-left: auto;
            margin-right: auto;
        }
    </style>
    <script>
        function setPage(page) {
            const encodedPage = btoa(page);
            document.cookie = "page=" + encodedPage + ";path=/";
            location.reload();
        }
    </script>
</head>
<body>

<h1>Lagu Patriotik Malaysia</h1>
<a>Adakah anda tahu lagu-lagu merdeka</a>

<div class="navbar">
    <a href="javascript:void(0)" onclick="setPage('tanggal31.html')">Tanggal 31</a>
    <a href="javascript:void(0)" onclick="setPage('keranamu.html')">Keranamu Malaysia</a>
    <a href="javascript:void(0)" onclick="setPage('jalurgemilang.html')">Jalur Gemilang</a>
</div>

<div class="content">
    <?php echo $content; ?>
</div>

<div class="audio-player">
    <?php if ($audio_file): ?>
        <audio controls autoplay>
            <source src="<?php echo $audio_file; ?>" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
    <?php endif; ?>
</div>

</body>
</html>
```
It then sanitizes the content with `htmlspecialchars` to convert special characters to HTML entities, preventing potential XSS attacks.
```php
<?php
$host = "localhost";
$username = "cubaan mengehack ka itu";
$password = "3108{m4r1_k1t4_w4rg4_n3g4r4}";
$database = "flag";

$conn = new mysqli($host, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

echo "Connected successfully";
?>
```

## Flag
```
3108{m4r1_k1t4_w4rg4_n3g4r4}
```
