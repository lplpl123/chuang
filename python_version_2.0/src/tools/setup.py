from tkinter import Tk
from config import app
from surfaces.main_surface import MainSurface
from surfaces.text_surface import TextSurface
from surfaces.photo_surface import PhotoSurface
from surfaces.video_surface import VideoSurface
from surfaces.audio_surface import AudioSurface


class Run():
    def setup(self):
        root = Tk()
        root.config(background=app["background"])
        root.title(app["name"])
        root.geometry('{}x{}'.format(app["width"], app["height"]))
        self.setup_surfaces(root)
        return root

    def run(self, root):
        self.blit()
        root.mainloop()

    def setup_surfaces(self, root):
        main_surface = MainSurface(root)
        text_surface = TextSurface()
        photo_surface = PhotoSurface()
        video_surface = VideoSurface()
        audio_surface = AudioSurface()

    def blit(self):
        pass