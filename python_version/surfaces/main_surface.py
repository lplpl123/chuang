from tkinter import *
from tools import play_gif
from tools.random_task import random_task
from tools.setup import setup_surfaces


class mainSurface:
    def __init__(self, root, task_num):
        self.root = root
        self.task_num = task_num
        self.count = 1
        self.setup_mainsurface()
        self.surfaces = setup_surfaces(self.lb, self.start_button, self.root)

    def setup_mainsurface(self):
        play_gif.decomposePics("./resources/start.gif")
        self.lb = Label(self.root, text='请开始你的创作......', bg="#171841", fg="white",
                        font=('方正舒体', '14', 'normal'))
        self.lb.pack()
        self.start_button = Button(self.root, text='start', relief=FLAT, bd=1)
        self.start_button.place(relx=0.5, rely=0.5, anchor='center')
        self.start_button.config(command=lambda: self.choose_task())
        # 动画效果
        self.decoration(self.root)

    def choose_task(self):
        if self.count == self.task_num:
            self.lb.config(text='今日创作已完成......')
        if 用户创建了数据: # todo- 这里肯定是要写一个函数的
            self.surface = random_task(self.surfaces)
            self.surface.create_surface()
            self.count += 1
        else:
            self.surface.create_surface()

    def decoration(self, root):
        # test
        i = 1
        play_gif.playgif(i, root, self.start_button)