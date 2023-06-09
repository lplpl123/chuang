from tkinter import Tk
from config import app
from surfaces.main_surface import MainSurface
from surfaces.text_surface import TextSurface
from surfaces.photo_surface import PhotoSurface
from surfaces.video_surface import VideoSurface
from surfaces.audio_surface import AudioSurface


class Run():
    def __init__(self):
        self.setup()

    def setup(self):
        # 就是一些配置的东西
        self.root = Tk()
        self.root.config(background=app["background"])
        self.root.title(app["name"])
        self.root.geometry('{}x{}'.format(app["width"], app["height"]))
        x = int((self.root.winfo_screenwidth() - 800) / 2)
        y = int((self.root.winfo_screenheight() - 600) / 2)
        self.root.geometry("+{}+{}".format(x, y))
        self.setup_surfaces()

    def run(self):
        self.blit_main_surface()
        self.root.mainloop()

    def setup_surfaces(self):
        self.text_surface = TextSurface(self.root)
        self.photo_surface = PhotoSurface(self.root)
        self.video_surface = VideoSurface(self.root)
        self.audio_surface = AudioSurface(self.root)
        self.surfaces = [self.text_surface,
                         self.photo_surface,
                         self.video_surface,
                         self.audio_surface]
        self.main_surface = MainSurface(self.root, self.surfaces)

    def blit_main_surface(self):
        self.main_surface.blit_widgets()