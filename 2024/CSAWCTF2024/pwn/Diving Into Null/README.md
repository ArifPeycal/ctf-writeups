# Diving Into Null
## Description
> Oops, I rm -rf 'ed my binaries
>  
> nc null.ctf.csaw.io 9191

## Challenge Description
When we connected to the server, we found out that some of the commands cannot be executed such as `ls`, `cat` and `dir`. 

![image](https://github.com/user-attachments/assets/ed08adb2-e8b4-42b3-aefa-9da38fa8a2d0)

We can see the list of commands that we can use by typing `help`. These commands are also known as `shell built-in`. 

> A shell built-in is a command or function that is directly integrated into the shell itself, rather than being an external executable file. These commands are part of the shell’s internal code, meaning they don't require a separate process to run.
 

![image](https://github.com/user-attachments/assets/7c397b31-fb31-4356-bc55-7911864fde3a)

So, we need to use only the commands above to search for the flag.
## Solution

Upon inspection, we found out that there is a user `groot` in `/home` directory. The flag most probably be in this directory. Now, we need to find a way to list files and directories in `/home/groot`. 

I found out that `compgen` can be used to list directories, files and commands. 
- `-c`: Generate command names.
- `-d`: Generate directory names.
- `-e`: Generate environment variable names.
- `-f`: Generate file names.

![image](https://github.com/user-attachments/assets/95eb2c5e-f6e9-492c-91d8-dac8f078580d)

We found `.flag` file that may contain the flag. Now, we need to read the file. I tried to use `source` but it didnt give the flag. 

So, I refered to <a href="https://book.hacktricks.xyz/linux-hardening/bypass-bash-restrictions">this cheatsheet</a> by Hactricks to bypass Linux bash restrictions. We can use this command to read every line in a file. I tried it with `/etc/passwd` and it gives the expected result. Now, we can read `.flag` file. 

```
# Read file with read
while read -r line; do echo $line; done < /etc/passwd
```
![image](https://github.com/user-attachments/assets/64f2990d-1bfc-4218-a15f-aa2c6b136f75)

## Flag
```
csawctf{penguins_are_just_birds_with_tuxedos}
```
