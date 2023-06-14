import os
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
from config import app, button_label
from data.task_database import TASKS
from tools.decomposepics import decomposePics


class TextSurface:
    def __init__(self, root):
        # init params
        self.root = root
        self.play_index = 1
        self.original_img = "./resources/originals/decoration01.gif"  # todo 使用os读文件夹里面的东西
        self.output_imgs = "./resources/surfaces_imgs/text_surface_imgs/decoration01"
        # init widgets
        self.text_frame = Frame(root, width=app["width"], height=app["height"], bg='#f1f1b8')
        root.bind("<Configure>", lambda event: self.text_frame_auto_resize(event, root), add="+")
        self.lb = Label(self.text_frame, text='请写下你此时的心情......', bd=0, bg="#f1f1b8", fg="#f1707d") # todo 要从任务库抽取任务
        self.upload_button = Label(self.text_frame, text='upload', bg="#f1f1b8", fg="#f1707d", cursor='hand2')
        self.upload_button.bind('<Button-1>', self.upload_text)
        self.exit_button = Label(self.text_frame, text='exit', bg="#f1f1b8", fg="#f1707d", cursor='hand2')
        self.exit_button.bind('<Button-1>', self.exit)
        self.text_frame.bind("<Configure>", lambda event: self.widgets_auto_resize(event))
        self.decoration = Label(self.text_frame, bd=0, width=80, height=114)
        decomposePics(self.original_img, self.output_imgs)

    def blit_widgets(self):
        self.text_frame.place(relx=0.0, rely=0.0, anchor='nw')
        self.text_frame.tkraise()
        self.lb.place(relx=0.5, rely=0.0, anchor='n')
        self.upload_button.place(anchor='center', relx=0.5, rely=0.5)
        self.exit_button.place(anchor='center', relx=0.2, rely=0.9)
        self.decoration.place(relx=0.90, rely=0.95, anchor='se')
        self.play_gif(self.play_index, self.root, self.decoration, self.output_imgs)

    def upload_text(self, event):
        # todo 得做个判断，是和任务相匹配的才能上传成功
        file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser('H:/')))
        if file_path:
            # 保存文件
            image = Image.open(file_path)
            image.save("")
            # todo 如果保存成功的话，需要退出这个界面，直接调用退出函数就好了exit

    def exit(self, event):
        self.text_frame.place_forget()

    def text_frame_auto_resize(self, event, root):
        self.text_frame['width'] = root.winfo_width()
        self.text_frame['height'] = root.winfo_height()

    def widgets_auto_resize(self, event):
        frame_width = self.text_frame.winfo_width()
        frame_height = self.text_frame.winfo_height()
        ratio = min(frame_height, frame_width) / 300
        # auto resize widgets
        lb_config = button_label["text_size"]
        self.lb['font'] = ('方正舒体', int(lb_config + lb_config * ratio), 'normal')
        self.upload_button['font'] = ('方正舒体', int(lb_config + lb_config * ratio), 'normal')
        self.exit_button['font'] = ('方正舒体', int(lb_config + lb_config * ratio), 'normal')
        self.decoration['width'] = int(40 + 40 * ratio)
        self.decoration['height'] = int(57 + 57 * ratio)

    def play_gif(self, index, root, widget, path, time=30):
        global loop
        with Image.open(path + "/frame{}.png".format(index)) as img:
            img = img.resize((int(widget['width']), int(widget['height'])))
            image = ImageTk.PhotoImage(img)
        widget.config(image=image)
        widget.img = image
        index += 1
        if index == 21:
            index = 1
        loop = root.after(time, self.play_gif, index, root, widget, path, time)
