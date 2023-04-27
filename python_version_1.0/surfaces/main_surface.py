import os
import time
from tkinter import *
from tools import play_gif
from tools.random_task import random_task
from tools.setup import setup_surfaces
from tools.auto_resize import auto_resize
from surfaces.text_surface import textInputsSurface
from surfaces.photograph_surface import photographSurface
from surfaces.video_surface import videoSurface
from surfaces.audio_surface import audioSurface


class mainSurface:
    def __init__(self, root, task_num):
        self.root = root
        self.task_num = task_num
        self.count = 0
        self.setup_mainsurface()
        self.surfaces = setup_surfaces(self.lb, self.start_button, self.root)

    def setup_mainsurface(self):
        play_gif.decomposePics("./resources/start.gif")
        self.lb = Label(self.root, text='请开始你的创作......', bd=0, bg="#171841", fg="white")
        self.lb.place(relx=0.5, rely=0.0, anchor='n')
        self.start_button = Label(self.root, text='start', relief=FLAT, bd=0, cursor='hand2',
                                  height=60, width=80, bg="#171841")
        self.start_button.place(relx=0.5, rely=0.5, anchor='center')
        self.start_button.bind('<Button-1>', self.choose_task)
        self.root.bind("<Configure>", lambda event: auto_resize(event, self.root, self.lb,
                                                                self.start_button,
                                                                self.surfaces))
        # 动画效果
        self.decoration(self.root)

    def choose_task(self, event):
        if self.count == 0:
            self.surface = random_task(self.surfaces)
            self.count += 1
        if self.count == self.task_num:
            self.lb.config(text='今日创作已完成......')
        if self.check_if_task_completed():
            self.count += 1
            self.surface = random_task(self.surfaces)
            self.surface.create_surface()
        else:
            self.surface.create_surface()

    def decoration(self, root):
        # test
        i = 1
        play_gif.playgif(i, root, self.start_button)

    def check_if_task_completed(self):
        # 定位到是哪个模块的
        if type(self.surface) == textInputsSurface:
            self.user_data_path = './user data/texts'
        elif type(self.surface) == photographSurface:
            self.user_data_path = './user data/photos'
        elif type(self.surface) == videoSurface:
            self.user_data_path = './user data/videos'
        elif type(self.surface) == audioSurface:
            self.user_data_path = './user data/audios'
        # 检查用户数据里面是否存在今天修改的数据
        files = os.listdir(self.user_data_path)
        for file in files:
            file_path = self.user_data_path + "/" + file
            create_time = time.ctime(os.path.getctime(file_path))
            create_time = create_time[:11] + create_time[20:24]
            current_time = time.ctime()
            current_time = current_time[:11] + current_time[20:24]
            if create_time == current_time:
                return True
        return False