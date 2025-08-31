# Pemimpin

> Perdana Menteri merupakan ketua kerajaan Malaysia dan memainkan peranan penting dalam menentukan hala tuju negara dan memastikan tanah air terus melangkah ke arah pembangunan serta kesejahteraan rakyat sejak detik kemerdekaan. Persoalannya, adakah anda kenal siapa mereka semua?
>
> https://pemimpin.bahterasiber.my

## Solution
We were given a website that requires us to sort the Prime Ministers' list from 1957 until current. 

```js
// Initialize cookies when page loads
window.onload = function() {
    document.cookie = "tahun_merdeka=false; path=/";
    document.cookie = "bulan_merdeka=false; path=/";
    document.cookie = "hari_merdeka=false; path=/";
    
    // Start server-side flag checking
    startFlagValidation();
};

// Correct sequence of Prime Ministers
const correctSequence = ['Tunku', 'Razak', 'Hussein', 'Mahathir', 'Abdullah', 'Najib', 'Mahathir2', 'Muhyiddin', 'Ismail', 'Anwar'];
let selectedSequence = [];
let quizCompleted = false;
let flagValidationActive = false;
```
<img width="1053" height="543" alt="image" src="https://github.com/user-attachments/assets/ca72562f-45c2-4082-9817-9b2f45e7430a" />

## Flag
```
3108{p3m1mp1n_m4l4y5I4}
```
