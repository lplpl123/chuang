import os
import time
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
from config import app, button_label
from data.task_database import TASKS
from tools.decomposepics import decomposePics
from tools.micro_cartoon import *
from tools.select_task_randomly import select_task_randomly
from tools.blite_task_level_img import blite_task_level_img
from surfaces.sub_surfaces.text_edit_surface import TextEditSurface


class TextSurface:
    def __init__(self, root):
        # init params
        self.root = root
        self.play_index = 1
        self.tol_frames = 27
        self.path = './data/user_private_data/text_surface_data/'
        self.original_img = "./resources/originals/text.gif"  # todo 使用os读文件夹里面的东西
        self.output_imgs = "./resources/surfaces_imgs/text_surface_imgs/decoration01"
        self.task, self.level = select_task_randomly("text_surface")
        # init widgets
        root.bind("<Configure>", lambda event: self.text_frame_auto_resize(event, root), add="+")
        self.text_frame = Frame(root, width=app["width"], height=app["height"], bg='#FDBB58')
        self.text_frame.bind("<Configure>", lambda event: self.widgets_auto_resize(event), add='+')
        self.lb = Label(self.text_frame, text=self.task, bd=0, bg="#FDBB58", fg="white") # todo 要从任务库抽取任务
        # 任务稀有度标识
        self.task_level_img = Canvas(self.text_frame, width=30, height=30, bd=0, bg="#FDBB58", highlightthickness=0)
        self.upload_button = Label(self.text_frame, text='upload', bg="#FDBB58", fg="white", cursor='hand2')
        self.upload_button.bind('<Button-1>', self.upload_button_function)
        self.upload_button.bind('<Enter>', lambda event: mouse_slip_on_widget(event, self.upload_button, 'black'))
        self.upload_button.bind('<Leave>', lambda event: mouse_slip_off_widget(event, self.upload_button, 'white'))
        # edit_button
        self.edit_button = Label(self.text_frame, text='edit', bg="#FDBB58", fg="white", cursor='hand2')
        self.edit_button.bind('<Button-1>', self.edit_button_function)
        self.edit_button.bind('<Enter>', lambda event: mouse_slip_on_widget(event, self.edit_button, 'black'))
        self.edit_button.bind('<Leave>', lambda event: mouse_slip_off_widget(event, self.edit_button, 'white'))
        # exit_button
        self.exit_button = Label(self.text_frame, text='exit', bg="#FDBB58", fg="white", cursor='hand2')
        self.exit_button.bind('<Button-1>', self.exit)
        self.exit_button.bind('<Enter>', lambda event: mouse_slip_on_widget(event, self.exit_button, 'black'))
        self.exit_button.bind('<Leave>', lambda event: mouse_slip_off_widget(event, self.exit_button, 'white'))
        self.decoration = Label(self.text_frame, bd=0, width=34, height=20, bg='#FDBB58')
        decomposePics(self.original_img, self.output_imgs)

    def blit_widgets(self):
        self.text_frame.place(relx=0.0, rely=0.0, anchor='nw')
        self.text_frame.tkraise()
        self.lb.place(relx=0.5, rely=0.0, anchor='n')
        self.task_level_img.place(relx=0.0, rely=0.0, anchor='nw')
        blite_task_level_img(self.level, self.task_level_img)
        self.upload_button.place(anchor='center', relx=0.4, rely=0.5)
        self.edit_button.place(anchor='center', relx=0.6, rely=0.5)
        self.exit_button.place(anchor='center', relx=0.2, rely=0.9)
        self.decoration.place(relx=0.90, rely=0.95, anchor='se')
        self.play_gif(self.play_index, self.root, self.decoration, self.output_imgs, self.tol_frames)

    def upload_button_function(self, event):
        # todo 得做个判断，是和任务相匹配的才能上传成功
        file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser('H:/')))
        if file_path:
            # 保存文件
            with open(file_path, mode='r', encoding='utf-8') as file:
                text_data = file.read()
            current_time = time.ctime().split(" ")
            current_time.pop(3)
            current_time = "-".join(current_time)
            if not os.path.isdir(self.path + current_time):
                os.mkdir(self.path + current_time)
            with open(self.path + '{}/{}.txt'.format(current_time, self.task),
                      mode='w', encoding='utf-8') as file:
                file.write(text_data)
            self.record_task_info()

    def exit(self, event):
        self.text_frame.place_forget()

    def text_frame_auto_resize(self, event, root):
        self.text_frame['width'] = root.winfo_width()
        self.text_frame['height'] = root.winfo_height()

    def widgets_auto_resize(self, event):
        frame_width = self.text_frame.winfo_width()
        frame_height = self.text_frame.winfo_height()
        if frame_width <= frame_height:
            ratio = frame_width / 800
        else:
            ratio = frame_height / 600
        # auto resize widgets
        lb_config = button_label["text_size"]
        self.lb['font'] = ('微软雅黑', int(lb_config + lb_config * ratio), 'normal')
        self.upload_button['font'] = ('微软雅黑', int(lb_config + lb_config * ratio), 'normal')
        self.edit_button['font'] = ('微软雅黑', int(lb_config + lb_config * ratio), 'normal')
        self.exit_button['font'] = ('微软雅黑', int(lb_config + lb_config * ratio), 'normal')
        self.decoration['width'] = int(34 + 34 * ratio)
        self.decoration['height'] = int(20 + 20 * ratio)

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

    def edit_button_function(self, event):
        # init sub surfaces
        text_edit_surface = TextEditSurface(self.root, self.task)
        self.root.withdraw()
        text_edit_surface.blit_widgets()

    def record_task_info(self):
        pass