import os
from PIL import Image
from PIL import ImageTk
from PIL import ImageSequence


def decomposePics(image_path):
    i = 0
    img = Image.open(image_path)
    folder = "./tem/tem_storage"
    if not os.path.isdir(folder):
        os.mkdir('./tem/tem_storage')
    for frame in ImageSequence.Iterator(img):
        frame.save(os.path.join("./tem/tem_storage", "frame{}.png".format(i+1)))
        i += 1

def playgif(i, tk, btn, time=50, play_or_not=True):
    global loop
    try:
        if not play_or_not:
            tk.after_cancel(loop)
            return
        with Image.open("./tem/tem_storage/frame{}.png".format(i)) as img:
            img = img.resize((int(btn['width']), int(btn['height']))) # todo 这个resize的大小就是需要配置的东西
            image = ImageTk.PhotoImage(img)
        btn.config(image=image)
        btn.img = image
        i += 1
        loop = tk.after(time, playgif, i, tk, btn, time, play_or_not)
    except:
        with Image.open("./tem/tem_storage/frame30.png") as img:
            img = img.resize((int(btn['width']), int(btn['height'])))
            image = ImageTk.PhotoImage(img)
        btn.config(image=image)
        btn.img = image
        loop = tk.after(time, playgif, i, tk, btn, time, play_or_not)

