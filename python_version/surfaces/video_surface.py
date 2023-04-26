import os
from tkinter import *
from tkinter import filedialog
from PIL import Image
from tools import play_gif


class videoSurface():

    def __init__(self, lb, btn, root):
        self.lb = lb
        self.btn = btn
        self.root = root
        self.exit_button = Label(self.root, text='exit', bg="#171841", fg="white", cursor='hand2')
        self.exit_button.bind('<Button-1>', self.exit_video)
        self.upload_button = Label(self.root, text='upload', bg="#171841", fg="white", cursor='hand2')
        self.upload_button.bind('<Button-1>', self.upload_video)

    def create_surface(self):
        # 停止播放动画
        play_gif.playgif(1, self.root, self.btn, play_or_not=False)
        # 隐藏主界面的组件
        self.btn.place_forget()
        self.lb.config(text='请录下一段视频......')
        self.upload_button.place(anchor='center', relx=0.5, rely=0.5)
        self.exit_button.place(anchor='center', relx=0.2, rely=0.9)

    def upload_video(self, event):
        file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser('H:/')))
        if file_path:
            self.upload_button.place_forget()
            image = Image.open(file_path)
            image.save("./user data/photos/1.png")
            # 然后就是显现一些其他的部件

    def exit_video(self, event):
        # 更改提示语
        self.lb.config(text='请开始你的创作......')
        # 隐藏组件
        self.exit_button.place_forget()
        self.upload_button.place_forget()
        # 显示组件，一旦展示这个组件，就会播放动画
        self.btn.place(relx=0.5, rely=0.5, anchor='center')
        i = 1
        play_gif.playgif(i, self.root, self.btn)