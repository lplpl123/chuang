import os
from tkinter import *
from tkinter import filedialog
from PIL import Image
from tools import play_gif


class photographSurface():

    def __init__(self, lb, btn, root):
        self.lb = lb
        self.btn = btn
        self.root = root

    def create_surface(self):
        # 停止播放上一个界面的动画
        self.root.after_cancel(play_gif.playgif)
        # 隐藏主界面的组件
        self.btn.place_forget()
        self.lb.config(text='请拍下一张照片......')
        # upload
        self.upload_button = Button(self.root, text='upload', command=self.upload_photo)
        self.upload_button.place(anchor='center', relx=0.5, rely=0.5)
        # exit
        self.exit_button = Button(self.root, text='exit', command=lambda: self.exit_photograph())
        self.exit_button.place(anchor='center', relx=0.2, rely=0.9)

    def upload_photo(self):
        file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser('H:/')))
        if file_path:
            self.upload_button.place_forget()
            image = Image.open(file_path)
            image.save("./user data/photos/1.png")
            # 然后就是显现一些其他的部件

    def exit_photograph(self):
        # 更改提示语
        self.lb.config(text='请开始你的创作......')
        # 隐藏组件
        self.exit_button.place_forget()
        self.upload_button.place_forget()
        # 显示组件，一旦展示这个组件，就会播放动画
        self.btn.place(relx=0.5, rely=0.5, anchor='center')
        i = 1
        play_gif.playgif(i, self.root, self.btn)
