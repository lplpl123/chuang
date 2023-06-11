from tkinter import *
from config import app
from tools.select_task_randomly import select_task_randomly
from tools.check_if_task_completed import check_if_task_completed


class MainSurface:
    def __init__(self, root, surfaces):
        self.surfaces = surfaces
        self.surface = select_task_randomly(self.surfaces)
        self.completed_tasks = 0
        self.total_tasks = 5
        self.main_frame = Frame(root, width=app["width"], height=app["height"], bg='red')
        self.lb = Label(self.main_frame, text='请开始你的创作......', bd=0, bg="#171841", fg="white")
        self.start_button = Label(self.main_frame, text='start', relief=FLAT, bd=0, cursor='hand2',
                                  bg="#171841", fg="white")
        self.start_button.bind('<Button-1>', self.start_button_function)

    def blit_widgets(self):
        self.main_frame.place(relx=0.0, rely=0.0, anchor='nw')
        self.lb.place(relx=0.5, rely=0.0, anchor='n')
        self.start_button.place(relx=0.5, rely=0.5, anchor='center')

    def select_task(self):
        if self.completed_tasks == self.total_tasks:
            self.lb.config(text='今日创作已完成......')
        elif check_if_task_completed(self.surface):
            self.completed_tasks += 1
            self.surface = select_task_randomly(self.surfaces)

    def start_button_function(self, event):
        # self.select_task()
        self.surface = self.surfaces[0] # test code
        self.surface.blit_widgets()
