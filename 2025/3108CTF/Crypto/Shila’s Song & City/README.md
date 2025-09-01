# Shila’s Song & City

> Shila Amzah dikenali sebagai salah satu penyanyi Malaysia yang berjaya di pentas antarabangsa. Dia lahir di sebuah bandar ibu negara Malaysia dan pernah menghasilkan sebuah lagu popular yang menjadi titik permulaannya di luar negara.

## Solution
I noticed flag format characters are 14 chars away from each other so I just created I script that take the first character, then skip 14 characters, then take the next one, and so on.
```py
text = """3e r air SeiaM1rmctnmctemt u0ciie piemoa'n8amprhiprur kg{hptpa-tpai'akSaiaitmain knihy-
sii
syta naamWa
mWaaent H
iahSpah r ed1Pml
eil
bctrilepaKi
aKaiep 4riuerTuegpris_t
 nii nitpsiSeSsanasakaianhmuengdenu
shi1ukkgaakg Wa
 laaean eatahKk4nrtn ptnel
ei_  i mui raKnt4hdkbenkbiueaamaiaen aen nn zrp rct rdsag'4aetsaetsaenakhprearreahkgna_acrmidrm
ea n1naja ujaKtnb 4 ya hga ui etKpaltaaltikbreLe iil iinaesr}rpnaupnag rap
ti dai datsmi
ankannkateaasmta  ta irm
aauskbusk jaKh niueniuba e
kyhlryhlultnKaa usa uaiiael kpe kptnannitiantia  dganet
iet
skaanyraM
raYea ngab
eBb
alsk a
"""

flag_chars = []
i = 0
while i < len(text):
    flag_chars.append(text[i])  # take current character
    i += 14
flag = ''.join(flag_chars)
print(flag)
```
## Flag
```
3108{ShaH1l4_Sh1l4_4mz4h_14KL}
```

