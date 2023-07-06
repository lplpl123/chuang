import time
import os
from tkinter import *
from PIL import Image
from PIL import ImageTk
from config import app, button_label, main_surface_data, loading_surface
from tools.select_task_randomly import select_surface_randomly
from tools.check_if_task_completed import check_if_task_completed
from tools.decomposepics import decomposePics
from tools.micro_cartoon import *


class MainSurface:
    def __init__(self, root, surfaces):
        # init params
        self.root = root
        self.play_index = 1
        self.total_tasks = 5
        self.surfaces = surfaces
        self.init_task()
        # init widgets
        self.main_frame = Frame(root, width=app["width"], height=app["height"], bg="#00B66D")
        self.main_frame.bind("<Configure>", lambda event: self.widgets_auto_resize(event))
        root.bind("<Configure>", lambda event: self.main_frame_auto_resize(event, root), add="+")
        self.background = Label(self.main_frame, bd=0, width=app["width"], height=app["height"], bg='#00B66D')
        self.lb = Label(self.main_frame, text='请开始你的创作......', bd=0, bg="#00B66D", fg="white")
        # start_button
        self.start_button = Label(self.main_frame, text='start', relief=FLAT, bd=0, cursor='hand2',
                                  bg="#00B66D", fg="white", font=('微软雅黑', int(10), 'normal'))
        self.start_button.bind('<Button-1>', self.start_button_function, add="+")
        self.start_button.bind('<Button-1>', lambda event: expand(event, self.start_button), add="+")
        self.start_button.bind('<Enter>', lambda event: mouse_slip_on_widget(event, self.start_button, 'black'), add="+")
        self.start_button.bind('<Enter>', lambda event: expand(event, self.start_button), add="+")
        self.start_button.bind('<Leave>', lambda event: mouse_slip_off_widget(event, self.start_button, 'white'), add="+")
        self.start_button.bind('<Leave>', lambda event: reduce(event, self.start_button), add="+")
        # zip widgets with img
        self.widgets_with_img = [self.background]
        # init imgs
        self.imgs = main_surface_data.get("imgs")
        for img, config in self.imgs.items():
            original_img = config.get("original_img")
            output_imgs = config.get("output_imgs")
            # 处理各组件gif图片 todo 这里需要做一个判别条件
            decomposePics(original_img, output_imgs)
        # init loading surface
        self.loading_surface_frame = Frame(self.main_frame, width=app["width"], height=app["height"])
        self.loading = Label(self.loading_surface_frame, bd=0, width=app["width"], height=app["height"])
        loading_original_img = loading_surface.get("imgs").get("loading").get("original_img")
        loading_output_imgs = loading_surface.get("imgs").get("loading").get("output_imgs")
        decomposePics(loading_original_img, loading_output_imgs)

    def init_task(self):
        with open("./data/current_tasks", mode='r', encoding='utf-8') as file:
            current_tasks_info = file.read()
            current_tasks_info = current_tasks_info.split('\n')
        if len(current_tasks_info) == 0:
            self.surface = select_surface_randomly(self.surfaces)
            self.completed_task_num = 0
        elif len(current_tasks_info) < 5:
            last_task = current_tasks_info[-1]
            last_task = last_task.split(" ")
            task_completed_or_not = last_task[1]
            surface_name = last_task[2]
            if task_completed_or_not == "1":
                self.surface = select_surface_randomly(self.surfaces)
                self.completed_task_num = len(current_tasks_info) - 1
            else:
                if surface_name == "text_surface":
                    self.surface = self.surfaces[0]
                elif surface_name == "photo_surface":
                    self.surface = self.surfaces[1]
                elif surface_name == "video_surface":
                    self.surface = self.surfaces[2]
                elif surface_name == "audio_surface":
                    self.surface = self.surfaces[3]
                self.completed_task_num = len(current_tasks_info)

    def blit_widgets(self):
        # todo 当第二次以后进行绘制的时候，就需要重新选择任务了
        self.main_frame.place(relx=0.0, rely=0.0, anchor='nw')
        self.main_frame.tkraise()
        self.background.place(relx=0.5, rely=0.5, anchor='center')
        self.lb.place(relx=0.5, rely=0.0, anchor='n')
        self.start_button.place(relx=0.5, rely=0.15, anchor='center')
        i = 0
        for img, config in self.imgs.items():
            tol_frames = config.get("tol_frames")
            output_imgs = config.get("output_imgs")
            self.play_gif(self.play_index, self.root, self.widgets_with_img[i], output_imgs, tol_frames)
            i += 1

    def select_task(self):
        if self.completed_task_num == self.total_tasks:
            self.lb.config(text='今日创作已完成......')
            with open("./data/current_tasks", mode="r", encoding="utf-8") as file:
                file.write("")
        elif check_if_task_completed(self.surface):
            self.completed_task_num += 1
            self.surface = select_surface_randomly(self.surfaces)
            # 任务完成之后，更改数据库
            with open("./data/current_tasks", mode="r", encoding="utf-8") as file:
                current_tasks_info = file.read()
                current_tasks_info = current_tasks_info.split('\n')
                last_task = current_tasks_info[-1]
                last_task = last_task.split(" ")
                last_task[1] = "1"
                last_task = " ".join(last_task)
                current_tasks_info.pop()
                current_tasks_info.append(last_task)
                current_tasks_info = "\n".join(current_tasks_info)
            with open("./data/current_tasks", mode="r", encoding="utf-8") as file:
                file.write(current_tasks_info)

    def start_button_function(self, event):
        # button还原
        # self.select_task()
        self.surface = self.surfaces[1]
        self.enter_next_surface()

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
        self.loading_surface_frame['width'] = frame_width
        self.loading_surface_frame['height'] = frame_height
        self.loading['width'] = int(800 * ratio)
        self.loading['height'] = int(600 * ratio)

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

    def enter_next_surface(self):
        # 绘制loading界面
        self.loading_surface_frame.place(relx=0.5, rely=0.5, anchor='center')
        self.loading_surface_frame.tkraise()
        self.loading.place(relx=0.0, rely=0.0, anchor='nw')
        # 播放一段加载动画
        index = 1
        output_imgs = loading_surface.get("imgs").get("loading").get("output_imgs")
        tol_frames = loading_surface.get("imgs").get("loading").get("tol_frames")
        self.loading_play_gif(index, self.root, self.loading, output_imgs, tol_frames)

    def loading_play_gif(self, index, root, widget, path, tol_frames, time=30):
        global loading_loop
        with Image.open(path + "/frame{}.png".format(index)) as img:
            img = img.resize((int(widget['width']), int(widget['height'])))
            image = ImageTk.PhotoImage(img)
        widget.config(image=image)
        widget.img = image
        index += 1
        if index == tol_frames-1:
            self.surface.blit_widgets()
        if index == tol_frames:
            self.loading_surface_frame.place_forget()
            return
        loading_loop = root.after(time, self.loading_play_gif, index, root, widget, path, tol_frames, time)
