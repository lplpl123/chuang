import os
from tkinter import *
from tkinter import filedialog
from PIL import Image
from config import app
from data.task_database import TASKS


class TextSurface:
    def __init__(self, root):
        self.text_frame = Frame(root, width=app["width"], height=app["height"], bg='blue')
        self.lb = Label(self.text_frame, text='请写下你此时的心情......', bd=0, bg="#171841", fg="white") # todo 要从任务库抽取任务
        self.upload_button = Label(self.text_frame, text='upload', bg="#171841", fg="white", cursor='hand2')
        self.upload_button.bind('<Button-1>', self.upload_text)
        self.exit_button = Label(self.text_frame, text='exit', bg="#171841", fg="white", cursor='hand2')
        self.exit_button.bind('<Button-1>', self.exit)

    def blit_widgets(self):
        self.text_frame.place(relx=0.0, rely=0.0, anchor='nw')
        self.text_frame.tkraise()
        self.lb.place(relx=0.5, rely=0.0, anchor='n')
        self.upload_button.place(anchor='center', relx=0.5, rely=0.5)
        self.exit_button.place(anchor='center', relx=0.2, rely=0.9)

    def upload_text(self, event):
        # todo 得做个判断，是和任务相匹配的才能上传成功
        file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser('H:/')))
        if file_path:
            # 保存文件
            image = Image.open(file_path)
            image.save("")
            # todo 如果保存成功的话，需要退出这个界面，直接调用退出函数就好了exit

    def exit(self, event):
        self.text_frame.place_forget()