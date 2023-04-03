import os
from tkinter import *
from tkinter import filedialog
from PIL import Image


class photographSurface():

    def __init__(self, lb, btn, root):
        self.lb = lb
        self.btn = btn
        self.root = root

    def create_surface(self):
        # 隐藏主界面的组件
        self.btn.place_forget()
        # 更改提示语
        self.lb.config(text='请拍下一张照片......')
        # upload
        self.save_button = Button(self.root, text='upload', command=self.upload_photo)
        self.save_button.place(anchor='center', relx=0.5, rely=0.5)

    def upload_photo(self):
        file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser('H:/')))
        image = Image.open(file_path)
        image.save("./user data/photos/1.png")