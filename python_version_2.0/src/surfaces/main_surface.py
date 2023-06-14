from tkinter import *
from PIL import Image
from PIL import ImageTk
from config import app, button_label
from tools.select_task_randomly import select_task_randomly
from tools.check_if_task_completed import check_if_task_completed
from tools.decomposepics import decomposePics


class MainSurface:
    def __init__(self, root, surfaces):
        # init params
        self.root = root
        self.play_index = 1
        self.surfaces = surfaces
        self.surface = select_task_randomly(self.surfaces)
        self.completed_tasks = 0
        self.total_tasks = 5
        self.original_img = "./resources/originals/jijian02.gif" # todo 使用os读文件夹里面的东西
        self.output_imgs = "./resources/surfaces_imgs/main_surface_imgs/background"

        # init widgets
        self.main_frame = Frame(root, width=app["width"], height=app["height"])
        root.bind("<Configure>", lambda event: self.main_frame_auto_resize(event, root), add="+")
        self.background = Label(self.main_frame, bd=0, width=app["width"], height=app["height"])
        self.lb = Label(self.main_frame, text='请开始你的创作......', bd=0, bg="#00B66D", fg="white")
        self.start_button = Label(self.main_frame, text='start', relief=FLAT, bd=0, cursor='hand2',
                                  bg="#00B66D", fg="white")
        self.start_button.bind('<Button-1>', self.start_button_function)
        self.main_frame.bind("<Configure>", lambda event: self.widgets_auto_resize(event))
        # 处理各组件gif图片 todo 这里需要做一个判别条件
        decomposePics(self.original_img, self.output_imgs)

    def blit_widgets(self):
        self.main_frame.place(relx=0.0, rely=0.0, anchor='nw')
        self.main_frame.tkraise()
        self.background.place(relx=0.0, rely=0.0, anchor='nw')
        self.lb.place(relx=0.5, rely=0.0, anchor='n')
        self.start_button.place(relx=0.5, rely=0.15, anchor='center')
        self.play_gif(self.play_index, self.root, self.background, self.output_imgs)

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

    def main_frame_auto_resize(self, event, root):
        self.main_frame['width'] = root.winfo_width()
        self.main_frame['height'] = root.winfo_height()

    def widgets_auto_resize(self, event):
        frame_width = self.main_frame.winfo_width()
        frame_height = self.main_frame.winfo_height()
        ratio = min(frame_height, frame_width) / 300
        # auto resize widgets
        lb_config = button_label["text_size"]
        self.lb['font'] = ('方正舒体', int(lb_config + lb_config * ratio), 'normal')
        self.start_button['font'] = ('方正舒体', int(lb_config + lb_config * ratio), 'normal')
        self.background['width'] = frame_width
        self.background['height'] = frame_height

    def play_gif(self, index, root, widget, path, time=30):
        global loop
        with Image.open(path + "/frame{}.png".format(index)) as img:
            img = img.resize((int(widget['width']), int(widget['height'])))
            image = ImageTk.PhotoImage(img)
        widget.config(image=image)
        widget.img = image
        index += 1
        if index == 101:
            index = 1
        loop = root.after(time, self.play_gif, index, root, widget, path, time)
