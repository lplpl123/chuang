import os
from tkinter import PhotoImage
from PIL import Image
from PIL import ImageSequence


def decomposePics(image_path):
    i = 0
    img = Image.open(image_path)
    folder = "./tem/tem_storage"
    if not os.path.isdir(folder):
        os.mkdir('./tem/tem_storage')
    for frame in ImageSequence.Iterator(img):
        frame = frame.resize((80, 60))
        frame.save(os.path.join("./tem/tem_storage", "frame{}.png".format(i+1)))
        i += 1

def playgif(i, tk, btn, time=50, play_or_not=True):
    global loop
    try:
        if not play_or_not:
            tk.after_cancel(loop)
            return
        img = PhotoImage(file="./tem/tem_storage/frame{}.png".format(i))
        btn.config(image=img)
        btn.img = img
        i += 1
        loop = tk.after(time, playgif, i, tk, btn, time, play_or_not)
    except:
        pass

