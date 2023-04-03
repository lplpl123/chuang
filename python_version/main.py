from tkinter import *
from surfaces.text_surface import textInputsSurface
from surfaces.photograph_surface import photographSurface
from surfaces.video_surface import videoSurface
from surfaces.audio_surface import audioSurface


def setup():
    # 生成root窗口
    root = Tk()
    root.title('窗')
    root.geometry('480x240')
    lb = Label(root, text='请开始你的创作......')
    lb.pack()
    # start按钮
    btn = Button(root, text='start', relief=FLAT)
    # 初始化各界面
    text_surface = textInputsSurface(lb, btn, root)
    photograph_surface = photographSurface(lb, btn, root)
    video_surface = videoSurface(lb, btn, root)
    audio_surface = audioSurface(lb, btn, root)
    surfaces = [text_surface, photograph_surface, video_surface, audio_surface]
    # start按钮
    btn.config(command=lambda : surfaces[1].create_surface()) # todo 还在开发测试阶段，暂时只用一个功能
    btn.place(relx=0.5, rely=0.5, anchor='center')
    # 运行程序
    root.mainloop()

if  __name__ == '__main__':
    # todo 随机取函数
    setup()