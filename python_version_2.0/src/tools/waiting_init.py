from tkinter import *
from PIL import Image
from PIL import ImageTk


class WaitingInit:
    def __init__(self):
        # init
        self.output_imgs = "./resources/originals/init.png"
        # 根窗口
        self.root = Tk()
        self.root.overrideredirect(True)
        self.root.geometry("400x200")
        x = int((self.root.winfo_screenwidth() - 400) / 2)
        y = int((self.root.winfo_screenheight() - 200) / 2)
        self.root.geometry("+{}+{}".format(x, y))
        # frame
        self.waiting_init_frame = Frame(self.root, width=400, height=200)
        self.background = Label(self.waiting_init_frame, bd=0, width=400, height=200)
        with Image.open(self.output_imgs) as img:
            img = img.crop((95, 200, 495, 400))
            image = ImageTk.PhotoImage(img)
        self.background.config(image=image)
        self.background.img = image

    def run(self):
        self.blit_widgets()
        self.root.mainloop()

    def blit_widgets(self):
        self.waiting_init_frame.place(relx=0.0, rely=0.0, anchor='nw')
        self.waiting_init_frame.tkraise()
        self.background.place(relx=0.0, rely=0.0, anchor='nw')