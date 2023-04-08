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

def playgif(i, tk, btn, time=50):
    try:
        img = PhotoImage(file="./tem/tem_storage/frame{}.png".format(i))
        btn.config(image=img)
        btn.img = img
        i += 1
        tk.after(time, playgif, i, tk, btn, time)
    except:
        pass

