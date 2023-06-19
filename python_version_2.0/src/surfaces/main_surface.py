from tkinter import *
from PIL import Image
from PIL import ImageTk
from config import app, button_label
from tools.select_task_randomly import select_surface_randomly
from tools.check_if_task_completed import check_if_task_completed
from tools.decomposepics import decomposePics
from tools.micro_cartoon import *


class MainSurface:
    def __init__(self, root, surfaces):
        # init params
        self.root = root
        self.play_index = 1
        self.surfaces = surfaces
        self.surface = select_surface_randomly(self.surfaces)
        self.completed_tasks = 0
        self.total_tasks = 5
        self.tol_frames = 101
        self.original_img = "./resources/originals/jijian02.gif" # todo 使用os读文件夹里面的东西
        self.output_imgs = "./resources/surfaces_imgs/main_surface_imgs/background"

        # init widgets
        self.main_frame = Frame(root, width=app["width"], height=app["height"], bg="#00B66D")
        self.main_frame.bind("<Configure>", lambda event: self.widgets_auto_resize(event))
        root.bind("<Configure>", lambda event: self.main_frame_auto_resize(event, root), add="+")
        self.background = Label(self.main_frame, bd=0, width=app["width"], height=app["height"], bg='#00B66D')
        self.lb = Label(self.main_frame, text='请开始你的创作......', bd=0, bg="#00B66D", fg="white")
        # start_button
        self.start_button = Label(self.main_frame, text='start', relief=FLAT, bd=0, cursor='hand2',
                                  bg="#00B66D", fg="white")
        self.start_button.bind('<Button-1>', self.start_button_function)
        self.start_button.bind('<Enter>', lambda event: mouse_slip_on_widget(event, self.start_button, 'black'), add="+")
        self.start_button.bind('<Enter>', lambda event: expand(event, self.start_button), add="+")
        self.start_button.bind('<Leave>', lambda event: mouse_slip_off_widget(event, self.start_button, 'white'), add="+")
        self.start_button.bind('<Leave>', lambda event: reduce(event, self.start_button), add="+")
        # 处理各组件gif图片 todo 这里需要做一个判别条件
        decomposePics(self.original_img, self.output_imgs)

    def blit_widgets(self):
        self.main_frame.place(relx=0.0, rely=0.0, anchor='nw')
        self.main_frame.tkraise()
        self.background.place(relx=0.5, rely=0.5, anchor='center')
        self.lb.place(relx=0.5, rely=0.0, anchor='n')
        self.start_button.place(relx=0.5, rely=0.15, anchor='center')
        self.play_gif(self.play_index, self.root, self.background, self.output_imgs, self.tol_frames)

    def select_task(self):
        if self.completed_tasks == self.total_tasks:
            self.lb.config(text='今日创作已完成......')
        elif check_if_task_completed(self.surface):
            self.completed_tasks += 1
            self.surface = select_surface_randomly(self.surfaces)

    def start_button_function(self, event):
        # self.select_task()
        self.surface = self.surfaces[0] # test code
        self.surface.blit_widgets()

    def main_frame_auto_resize(self, event, root):
        self.main_frame['width'] = root.winfo_width()
        self.main_frame['height'] = root.winfo_height()

    def widgets_auto_resize(self, event):
        frame_width = self.main_frame.winfo_width()
        frame_height = self.main_frame.winfo_height()
        if frame_width <= frame_height:
            ratio = frame_width / 800
        else:
            ratio = frame_height / 600
        # auto resize widgets
        lb_config = button_label["text_size"]
        self.lb['font'] = ('微软雅黑', int(lb_config + lb_config * ratio), 'normal')
        self.start_button['font'] = ('微软雅黑', int(lb_config + lb_config * ratio), 'normal')
        self.background['width'] = int(800 * ratio)
        self.background['height'] = int(600 * ratio)

    def play_gif(self, index, root, widget, path, tol_frames, time=30):
        global loop
        with Image.open(path + "/frame{}.png".format(index)) as img:
            img = img.resize((int(widget['width']), int(widget['height'])))
            image = ImageTk.PhotoImage(img)
        widget.config(image=image)
        widget.img = image
        index += 1
        if index == tol_frames:
            index = 1
        loop = root.after(time, self.play_gif, index, root, widget, path, tol_frames, time)
