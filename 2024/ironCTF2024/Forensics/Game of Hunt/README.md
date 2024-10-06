# Game of Hunt
## Description
> A Cryptic Voyage
## Solution
Use CyberChef to convert from binary to hex. Reverse by bytes (not characters).

![image](https://github.com/user-attachments/assets/5ef5af23-633b-4bd9-8ad1-2dea53d7a6f5)

Upon inspection, `document_83.pdf` contains different sizes and date. There is a black line covering the code, just highlight the text and copy. 

![image](https://github.com/user-attachments/assets/9dd7f75d-9bdc-4e49-b18a-28061180a13a)

```
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>+++++.++++++++  
+.---.-.<---.+++++++++++++++++.--------------.>+++++++++++++.<+++++++++++++++++  
++.>------------.+++++  
+.<++++++.++.>---.<++++.------.>++.<+++++++++.---.------.+++++++.+  
++.+++++.---------.>-.  
+.+++++++++.
```
Use https://www.dcode.fr/brainfuck-language to decode. 

![image](https://github.com/user-attachments/assets/cd88e2be-3b81-45f4-a98e-a00cfd8644db)
## Flag
```
ironCTF{You_are_the_finest}
```
