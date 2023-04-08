from tkinter import *
from surfaces.text_surface import textInputsSurface
from surfaces.photograph_surface import photographSurface
from surfaces.video_surface import videoSurface
from surfaces.audio_surface import audioSurface
from tools import play_gif


class mainSurface:
    def __init__(self, root):
        self.lb = Label(root, text='请开始你的创作......')
        self.lb.pack()
        self.start_button = Button(root, text='start', relief=FLAT, bd=0)
        # 初始化各界面
        self.text_surface = textInputsSurface(self.lb, self.start_button, root)
        self.photograph_surface = photographSurface(self.lb, self.start_button, root)
        self.video_surface = videoSurface(self.lb, self.start_button, root)
        self.audio_surface = audioSurface(self.lb, self.start_button, root)
        self.surfaces = [self.text_surface,
                    self.photograph_surface,
                    self.video_surface,
                    self.audio_surface]     # todo 随机取函数
        # start按钮
        self.start_button.config(command=lambda: self.surfaces[1].create_surface())  # todo 还在开发测试阶段，暂时只用一个功能
        self.start_button.place(relx=0.5, rely=0.5, anchor='center')
        self.decoration(root)

    def decoration(self, root):
        # test 分解gif
        play_gif.decomposePics("./resources/start.gif")
        # test
        i = 1
        play_gif.playgif(i, root, self.start_button)