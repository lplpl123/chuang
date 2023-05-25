from tkinter import *
from config import app
from tools.select_task_randomly import select_task_randomly


class MainSurface:
    def __init__(self, root):
        self.completed_tasks = 0
        self.total_tasks = 5
        self.main_frame = Frame(root, width=app["width"], height=app["height"])
        self.lb = Label(self.main_frame, text='请开始你的创作......', bd=0, bg="#171841", fg="white")
        self.start_button = Label(self.main_frame, text='start', relief=FLAT, bd=0, cursor='hand2',
                                  bg="#171841", fg="white")
        self.start_button.bind('<Button-1>', self.select_task)

    def blit_widgets(self):
        self.main_frame.place(relx=0.0, rely=0.0, anchor='nw')
        self.lb.place(relx=0.5, rely=0.0, anchor='n')
        self.start_button.place(relx=0.5, rely=0.5, anchor='center')

    def select_task(self, event):
        if self.completed_tasks == 0:
            self.surface = select_task_randomly()
        elif self.completed_tasks == self.total_tasks:
            self.lb.config(text='今日创作已完成......')