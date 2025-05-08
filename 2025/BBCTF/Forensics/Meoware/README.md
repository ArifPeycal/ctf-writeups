# Meoware
> My friend made a malware and asked me to evaluate it. After running it, my computer crashed, and I suspect the malware is to blame. Fortunately, I had a backup before the crash occurred. Could you investigate this further?
>
> This challenge has been distributed via Gdrive link previously.
>
> Author: Identities

## Solution
Same as ICECTF Chapter 1: Giff Me Arcana 01 and kashiCTF 2025 with RE:UN1ON.

Basically, search Discord Cache file location, use `ChromeCacheViewer` to view Discrod cache, read the message JSON file, there will be conversation between two peoples. One will send a GDrive Link that you can download the malware. Malware is compiled using Python, so you can use pyinstraxtoe and pylingual or uncompyle6 if you want. Flag is hardcoded. 

```py
# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: challenge.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import os
import sys
import tkinter as tk
from PIL import Image, ImageTk

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)
window = tk.Tk()
window.title('Meowware')
window.geometry('1000x440')
window.configure(bg='#121212')
cat_images = ['cat1.jpg', 'cat2.jpg', 'cat3.jpg', 'cat4.jpg', 'cat5.jpg']
for i, image_path in enumerate(cat_images):
    try:
        full_path = resource_path(image_path)
        img = Image.open(full_path)
        img = img.resize((200, 200), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        label = tk.Label(window, image=img_tk, bg='#121212')
        label.image = img_tk
        label.grid(row=i // 3, column=i % 3, padx=10, pady=10)
    except Exception as e:
        pass
else:
    window.mainloop()
    new_window = tk.Tk()
    new_window.title('Meowware')
    new_window.geometry('200x200')
    text_field = tk.Entry(new_window)
    text_field.pack()
    text_field.insert(0, 'bbctf{1ba8a5f798e16c442d91841e33091cb2355a4c5f}')

    def close_window():
        new_window.destroy()
    new_window.after(0, close_window)
    new_window.mainloop()
    print(f'Error loading image {image_path}: {e}')
```

## Flag
```
bbctf{1ba8a5f798e16c442d91841e33091cb2355a4c5f}
```
