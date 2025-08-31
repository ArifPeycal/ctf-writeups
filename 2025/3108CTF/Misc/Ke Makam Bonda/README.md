# Ke Makam Bonda

> Sebuah puisi agung dari Almarhum Dato' Usman Awang kini bersemadi dalam bentuk alunan suara. Irama dan kata menyimpan dua bahagian rahsia :–
>
> Yang awal terzahir jika dipandang, bukan didengar; Yang akhir terkunci dalam gema yang lebih dalam, hanya dibuka oleh nama pena seorang sasterawan negara.
>
> Temui kedua-dua bahagian bendera, dan satukanlah.

## Solution
We were given a WAV file with a hint that there will be 2 parts of the flag. This challenge is obviously another stego chall with spectrogram and steghide using a password.

First part can be found using Audacity.
<img width="1329" height="363" alt="image" src="https://github.com/user-attachments/assets/c621b9a5-2c0a-423b-b50a-d5f6e00b3071" />

Second part needs to use steghide. The password is `Tongkat Warrant`. You will get a PDF, and the second part is in this file.

<img width="733" height="334" alt="image" src="https://github.com/user-attachments/assets/a9c2d9a5-3249-4b3d-a3cc-59dfe5a1a68e" />

## Flag
```
3108{Bondaku_Y4ng_Disayangi_Sem0ga_Dirahmati}
```
