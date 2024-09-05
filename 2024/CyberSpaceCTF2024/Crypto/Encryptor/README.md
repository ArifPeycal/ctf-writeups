# Encryptor
> My friend sent me this app with an encoded flag, but he forgot to implement the decryption algorithm! Can you help me out?

## Challenge Overview
The MainActivity class contains several functions that we need to look into:

<details>
  <summary>Source Code</summary>
  
```java
/* loaded from: classes.dex */
public class MainActivity extends AppCompatActivity {
    private String getKey() {
        return new String(Base64.decode("ZW5jcnlwdG9yZW5jcnlwdG9y".getBytes(), 0));
    private String encryptText(String str) throws InvalidKeyException, UnsupportedEncodingException, NoSuchPaddingException, NoSuchAlgorithmException, IllegalBlockSizeException, BadPaddingException {
        SecretKeySpec secretKeySpec = new SecretKeySpec(getKey().getBytes("UTF-8"), "Blowfish");
        Cipher cipher = Cipher.getInstance("Blowfish");
        if (cipher == null) {
            throw new Error();
        }
        cipher.init(1, secretKeySpec);
        return Build.VERSION.SDK_INT >= 26 ? new String(Base64.encode(cipher.doFinal(str.getBytes("UTF-8")), 0)) : "";
    }

    public void encrypt_onClick(View view) throws UnsupportedEncodingException, NoSuchPaddingException, IllegalBlockSizeException, NoSuchAlgorithmException, BadPaddingException, InvalidKeyException {
        this.builder.setMessage(encryptText(((TextView) findViewById(R.id.input)).getText().toString())).setCancelable(true);
        AlertDialog create = this.builder.create();
        create.setTitle("Here's your encrypted text:");
        create.show();
        View findViewById = create.findViewById(android.R.id.message);
        if (findViewById instanceof TextView) {
            ((TextView) findViewById).setTextIsSelectable(true);
        }
    }

    public static String readAssetFile(Context context, String str) {
        AssetManager assets = context.getAssets();
        StringBuilder sb = new StringBuilder();
        try {
            InputStream open = assets.open(str);
            try {
                BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(open));
                while (true) {
                    try {
                        String readLine = bufferedReader.readLine();
                        if (readLine == null) {
                            break;
                        }
                        sb.append(readLine).append('\n');
                    } finally {
                    }
                }
                bufferedReader.close();
                if (open != null) {
                    open.close();
                }
            } finally {
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return sb.toString();
    }

    public void getflag_onClick(View view) {
        this.builder.setMessage(readAssetFile(this, "enc.txt")).setCancelable(true);
        AlertDialog create = this.builder.create();
        create.setTitle("Here's the encrypted flag:");
        create.show();
        View findViewById = create.findViewById(android.R.id.message);
        if (findViewById instanceof TextView) {
            ((TextView) findViewById).setTextIsSelectable(true);
        }
    }
```
</details>


### Explanation
1. `getKey`: This method returns the encryption key for the `Blowfish` cipher. The key is decoded from a Base64-encoded string (`ZW5jcnlwdG9yZW5jcnlwdG9y`), which decodes to the string "`encryptorencryptor`"
2. `encryptText`: Encrypts the input text (str) using the `Blowfish` algorithm.
3. `getflag_onClick`: Reads the content of enc.txt file from the assets using readAssetFile.

## Solution
We need to read enc.txt which is located in /asset folder.
```
OIkZTMehxXAvICdQSusoDP6Hn56nDiwfGxt7w/Oia4oxWJE3NVByYnOMbqTuhXKcgg50DmVpudg=
```

Use this <a href="https://sladex.org/blowfish.js/">online tool</a> to do `Blowfish` decryption, provide the encrypted string and key. The cipher mode is ECB.
## Flag
```
CSCTF{3ncrypt0r_15nt_s4Fe_w1th_4n_h4Rdc0d3D_k3y!}
```
