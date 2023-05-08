from tkinter import Tk
from config import app
from surfaces.main_surface import MainSurface
from surfaces.text_surface import TextSurface
from surfaces.photo_surface import PhotoSurface
from surfaces.video_surface import VideoSurface
from surfaces.audio_surface import AudioSurface


def setup():
    root = Tk()
    root.config(background=app["background"])
    root.title(app["name"])
    root.geometry('{}x{}'.format(app["width"], app["height"]))
    setup_surfaces()
    return root

def run(root):
    root.mainloop()

def setup_surfaces():
    main_surface = MainSurface()
    text_surface = TextSurface()
    photo_surface = PhotoSurface()
    video_surface = VideoSurface()
    audio_surface = AudioSurface()