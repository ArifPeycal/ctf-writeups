# Kapla Harimau Selatan 🕸️
## Description
> Dalam zaman kuno Harimau Selatan, dikatakan bahawa, kadang-kadang kunci kepada masa depan tersembunyi di tempat yang jelas.
>
> https://8303a1befe.bahterasiber.my/
## Challenge Overview
![image](https://github.com/user-attachments/assets/1511e481-bf90-43ea-b875-b95c0a264d99)
```html
<div class="container">
    <div class="header">Admin Access</div>
    <div class="message">
Denied!
    </div>
</div>
<!-- reveal.txt -->
</body>
```
```php
<?php

header("Access-Control-Allow-Origin: https://127.0.0.1");

$headerName = 'Origin';
$headerValue = 'https://127.0.0.1';
$secondaryHeaderName = 'X-Custom-Header';
$secondaryHeaderValue = 'Sm9ob3IganVnYSBkaWtlbmFsaSBzZWJhZ2FpIEdfX19fX19fIG9sZWggb3JhbmcgU2lhbQ==';

$headerKey = 'HTTP_' . strtoupper(str_replace('-', '_', $headerName));
$secondaryHeaderKey = 'HTTP_' . strtoupper(str_replace('-', '_', $secondaryHeaderName));

if (isset($_SERVER[$headerKey]) && isset($_SERVER[$secondaryHeaderKey])) {
    $actualValue = $_SERVER[$headerKey];
    $actualSecondaryValue = $_SERVER[$secondaryHeaderKey];

    if ($actualValue === $headerValue && $actualSecondaryValue === $secondaryHeaderValue) {
        echo "The flag is 3108{this-is-fake-flag}";
    } else {
        echo "Close enough";
    }
} else {
    echo "Denied!";
}
?>
```
## Solution
```bash
curl -H "Origin: https://127.0.0.1" -H "X-Custom-Header: Gangganu " https://8303a1befe.bahterasiber.my/
```
## Flag
```
3108{d941697cea9e3f341864780b68416961}
```
