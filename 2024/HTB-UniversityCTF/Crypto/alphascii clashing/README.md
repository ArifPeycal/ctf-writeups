# alphaascii clashing
https://www.johndcook.com/blog/2024/03/20/md5-hash-collision/
```
    Welcome to my login application scaredy cat ! I am using MD5 to save the passwords in the database.
                          I am more than certain that this is secure.
                                   You can't prove me wrong!

    [1] Login
    [2] Register
    [3] Exit

    Option (json format) :: {"option": "register"}
enter credentials (json format) :: {"username": "TEXTCOLLBYfGiJUETHQ4hAcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak", "password": "123"}

    Welcome to my login application scaredy cat ! I am using MD5 to save the passwords in the database.
                          I am more than certain that this is secure.
                                   You can't prove me wrong!

    [1] Login
    [2] Register
    [3] Exit

    Option (json format) :: {"option": "login"}
enter credentials (json format) :: {"username": "TEXTCOLLBYfGiJUETHQ4hEcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak", "password": "123"}
[+] what?! this was unexpected. shutting down the system ::  ≡ƒæ╜
```

## Flag 
```
HTB{finding_alphanumeric_md5_collisions_for_fun_https://x.com/realhashbreaker/status/1770161965006008570_26558aa8f7c706bd264c5ad09b8c024c}
```
