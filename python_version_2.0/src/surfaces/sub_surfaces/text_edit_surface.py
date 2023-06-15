from tkinter import *
from config import app, button_label


class TextEditSurface():
    def __init__(self, frame):
        self.root = frame

        self.text_frame = Frame(frame, width=app["width"], height=app["height"], bg='white')

    def blit_widgets(self):
        pass
