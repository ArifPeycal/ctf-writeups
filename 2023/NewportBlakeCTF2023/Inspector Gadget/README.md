# Inspector Gadget

## Description 
> While snooping around this website, inspector gadet lost parts of his flag. Can you help him find it?

## Solution
We need to search 4 parts of the flag.

* Part 1/4

Between the ```<title>``` tag
<p align="center">
  <img width="80%" height="300" src="solution/gadget1.PNG">
</p>

* Part 2/4

Access to ```/supersecrettopsecret.txt``` using the URL

<p align="center">
  <img width="80%" height="300" src="solution/gadget2.PNG">
</p>

* Part 3/4

<p align="center">
  <img width="80%" height="300" src="solution/gadget3.PNG">
</p>

* Part 4/4

By using Gobuster, you can see that ```robots.txt``` is available.
<p align="center">
  <img width="80%" height="250" src="solution/gadget4.PNG">
</p>
<p align="center">
  <img width="80%" height="300" src="solution/gadget5.PNG">
</p>

## Flag 
```
nbctf{G00d_J06_D3tect1v3_G4dg3t352}
```



