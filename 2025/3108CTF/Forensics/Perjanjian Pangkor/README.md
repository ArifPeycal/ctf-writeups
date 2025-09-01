# Perjanjian Pangkor

> Tahun 1874 menyaksikan satu titik perubahan besar dalam sejarah Perak — termeterainya Perjanjian Pangkor antara pihak British dan pembesar Melayu. Di sebalik dokumen rasmi, wujud khabar angin bahawa satu komunikasi rahsia turut berlaku antara pihak tertentu, dihantar melalui saluran tersembunyi.
>
> Satu fail .pcap telah ditemui, dipercayai mengandungi serpihan maklumat penting berkaitan detik bersejarah ini. Kandungannya masih belum diketahui, namun ada pihak mendakwa ia menyimpan rahsia yang boleh mengubah tafsiran kita terhadap sejarah yang sedia ada.
>
> Mampukah anda menelusuri jejak-jejak digital dan membongkar kebenaran yang tersembunyi di sebalik arus masa?
>
> file = PERJANJIAN_PANGKOR.pcap = Clue - Perjanjian Pangkor.txt

## Solution
We were given a clue in text file and PCAP file. The answer for the clue is Raja Ismail.
```
KANDUNGAN PERJANJIAN PANGKOR 1874

2. Raja _______ dibenarkan memakai gelaran Sultan Muda dan diberikan sebuah jajahan kecil untuk ditadbir
```
Follow TCP stream in PCAP file, you will find a stream that have bytes for ZIP file (starting with `PK`), the zip file has a `docm` file called `PERJANJIAN_PANGKOR.docm`. Export raw data and put the correct extension.
<img width="894" height="701" alt="image" src="https://github.com/user-attachments/assets/0d2b93e0-cebd-48cf-9a98-406fb76096a3" />

The password is Ismail.

<img width="610" height="445" alt="image" src="https://github.com/user-attachments/assets/7a28c966-ce1c-4b48-9e2f-1bd6f7615b30" />

Since we are working with Macro, it is best to use oletools.
<img width="745" height="454" alt="image" src="https://github.com/user-attachments/assets/40969140-252a-462f-b762-aac456e6390e" />

## Flag
```
3108{perjanjian_pangkor_mesej_rahsia} 
```
