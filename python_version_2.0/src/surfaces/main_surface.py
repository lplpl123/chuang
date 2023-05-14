from tkinter import *
from config import app


class MainSurface:
    def __init__(self, root):
        self.main_frame = Frame(root, width=app["width"], height=app["height"])
        self.lb = Label(self.main_frame, text='请开始你的创作......', bd=0, bg="#171841", fg="white")
        self.start_button = Label(self.main_frame, text='start', relief=FLAT, bd=0, cursor='hand2',
                                  height=60, width=80, bg="#171841")

    def blit_widgets(self):
        self.main_frame.place(relx=0.0, rely=0.0, anchor='nw')
        self.lb.place(relx=0.5, rely=0.0, anchor='n')
        self.start_button.place(relx=0.5, rely=0.5, anchor='center')