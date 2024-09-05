# Selangor Tourism 🔧
## Description
> Jalan jalan selangor lagi
> 
> Hint:
> 1. Namakan semula file
> 2. pestudio

## Challenge Overview
This code displays a welcome message indicating that the application has started. It calls the `x0ef52747b6e3918b4b9cfc9e674ebde5` method to decrypt a message and display it as "Authenticated".
```c#
if (xb7d13bb26d3fa51cf94e377cc9db330b.xd23dd6f9e1210c6bdc7b053a0c6550d3(text, text2))
	{
		MessageBoxHelper.ShowMessage("Welcome to Selangor Tourism!", "Application Started");
		MessageBoxHelper.ShowMessage(MessageBoxHelper.x0ef52747b6e3918b4b9cfc9e674ebde5(), "Authenticated");
		Application.Run(new Form1());
		return;
	}
	MessageBoxHelper.ShowMessage("Invalid credentials. The application will now exit.", "Authentication Failed");
```

<br>

 1. `x0ef52747b6e3918b4b9cfc9e674ebde5`
    
- Converts the base64-encoded string to its byte representation and then to UTF-8 string.
```c#
public static string x0ef52747b6e3918b4b9cfc9e674ebde5()
{
			string xef75604e159f08f98d778e4e95a8f55d = "33:31:30:38";
			string s = "UQEGCwVXVQsLUgQPAwEICQZTCAhVVFUNUAIHW1EJBA9RUAldVlcBDlADAgBSBwYIV1QDAFYIU1lSBVQMVQc=";
			byte[] key = MessageBoxHelper.xeae169610fc37eba83c0768cd20bcba8(xef75604e159f08f98d778e4e95a8f55d);
			byte[] bytes = MessageBoxHelper.x3e7a2e73b9b83b091d676910aff1f58b(Convert.FromBase64String(s), key);
			return Encoding.UTF8.GetString(bytes);
}
```
<br>

2. `xeae169610fc37eba83c0768cd20bcba8`
   
- Converts a colon-separated hexadecimal string into a byte array (key for XOR).
- A byte array that represents the hexadecimal values. For "33:31:30:38", the output is [51, 49, 48, 56].
```c#
private static byte[] xeae169610fc37eba83c0768cd20bcba8(string xef75604e159f08f98d778e4e95a8f55d)
		{
			xef75604e159f08f98d778e4e95a8f55d = xef75604e159f08f98d778e4e95a8f55d.Replace(":", "");
			int length = xef75604e159f08f98d778e4e95a8f55d.Length;
			byte[] array = new byte[length / 2];
			for (int i = 0; i < length; i += 2)
			{
				array[i / 2] = Convert.ToByte(xef75604e159f08f98d778e4e95a8f55d.Substring(i, 2), 16);
			}
			return array;
		}
```
<br>

3. `x3e7a2e73b9b83b091d676910aff1f58b`
- Applies an XOR operation between each byte of the input data and a key.

```c#
private static byte[] x3e7a2e73b9b83b091d676910aff1f58b(byte[] data, byte[] key)
		{
			byte[] array = new byte[data.Length];
			int num = key.Length;
			for (int i = 0; i < data.Length; i++)
			{
				array[i] = (data[i] ^ key[i % num]);
			}
			return array;
		}
	}
}
```
## Solution
Create a Python script that reverses all of the encryption and prints the result.
```py
import base64

def xeae169610fc37eba83c0768cd20bcba8(hex_string):
    hex_string = hex_string.replace(":", "")
    return bytes.fromhex(hex_string)

def x3e7a2e73b9b83b091d676910aff1f58b(data, key):
    key_length = len(key)
    return bytes([data[i] ^ key[i % key_length] for i in range(len(data))])

def x0ef52747b6e3918b4b9cfc9e674ebde5():
    xef75604e159f08f98d778e4e95a8f55d = "33:31:30:38"
    s = "UQEGCwVXVQsLUgQPAwEICQZTCAhVVFUNUAIHW1EJBA9RUAldVlcBDlADAgBSBwYIV1QDAFYIU1lSBVQMVQc="
    key = xeae169610fc37eba83c0768cd20bcba8(xef75604e159f08f98d778e4e95a8f55d)
    data = base64.b64decode(s)
    result = x3e7a2e73b9b83b091d676910aff1f58b(data, key)
    return result.decode('utf-8')

if __name__ == "__main__":
    print(x0ef52747b6e3918b4b9cfc9e674ebde5())
```
## Flag
```
3108{b0636fe38c4700815b80fee5c37cb847ba9eef16c228a660de38e9caa4d4f6}
```
