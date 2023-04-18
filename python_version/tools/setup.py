from tkinter import Tk
from surfaces.text_surface import textInputsSurface
from surfaces.photograph_surface import photographSurface
from surfaces.video_surface import videoSurface
from surfaces.audio_surface import audioSurface


def setup():
    # 生成root窗口
    root = Tk()
    root.config(background="#171841")
    root.title('窗')
    root.geometry('480x240')
    return root

def run(root):
    root.mainloop()

def setup_surfaces(lb, start_button, root):
    # 初始化各界面
    text_surface = textInputsSurface(lb, start_button, root)
    photograph_surface = photographSurface(lb, start_button, root)
    video_surface = videoSurface(lb, start_button, root)
    audio_surface = audioSurface(lb, start_button, root)
    surfaces = [text_surface,
                photograph_surface,
                video_surface,
                audio_surface]
    return surfaces