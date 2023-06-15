import os
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
from config import app, button_label
from tools.decomposepics import decomposePics


class VideoSurface:
    def __init__(self, root):
        # init params
        self.root = root
        self.play_index = 1
        self.tol_frames = 121
        self.original_img = "./resources/originals/film.gif"  # todo 使用os读文件夹里面的东西
        self.output_imgs = "./resources/surfaces_imgs/video_surface_imgs/decoration01"

        self.video_frame = Frame(root, width=app["width"], height=app["height"], bg='black')
        root.bind("<Configure>", lambda event: self.video_frame_auto_resize(event, root), add="+")
        self.lb = Label(self.video_frame, text='请拍下一段视频......', bd=0, bg="black",
                        fg="white")  # todo 要从任务库抽取任务
        self.upload_button = Label(self.video_frame, text='upload', bg="black", fg="white", cursor='hand2')
        self.upload_button.bind('<Button-1>', self.upload_video)
        self.exit_button = Label(self.video_frame, text='exit', bg="black", fg="white", cursor='hand2')
        self.exit_button.bind('<Button-1>', self.exit)
        self.video_frame.bind("<Configure>", lambda event: self.widgets_auto_resize(event))
        self.decoration = Label(self.video_frame, bd=0, width=60, height=60)
        decomposePics(self.original_img, self.output_imgs)

    def blit_widgets(self):
        self.video_frame.place(relx=0.0, rely=0.0, anchor='nw')
        self.video_frame.tkraise()
        self.lb.place(relx=0.5, rely=0.0, anchor='n')
        self.upload_button.place(anchor='center', relx=0.5, rely=0.5)
        self.exit_button.place(anchor='center', relx=0.2, rely=0.9)
        self.decoration.place(relx=0.90, rely=0.95, anchor='se')
        self.play_gif(self.play_index, self.root, self.decoration, self.output_imgs, self.tol_frames)

    def upload_video(self, event):
        # todo 得做个判断，是和任务相匹配的才能上传成功
        file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser('H:/')))
        if file_path:
            # 保存文件
            image = Image.open(file_path)
            image.save("")
            # todo 如果保存成功的话，需要退出这个界面，直接调用退出函数就好了exit

    def exit(self, event):
        self.video_frame.place_forget()

    def video_frame_auto_resize(self, event, root):
        self.video_frame['width'] = root.winfo_width()
        self.video_frame['height'] = root.winfo_height()

    def widgets_auto_resize(self, event):
        frame_width = self.video_frame.winfo_width()
        frame_height = self.video_frame.winfo_height()
        ratio = min(frame_height, frame_width) / 300
        # auto resize widgets
        lb_config = button_label["text_size"]
        self.lb['font'] = ('方正舒体', int(lb_config + lb_config * ratio), 'normal')
        self.upload_button['font'] = ('方正舒体', int(lb_config + lb_config * ratio), 'normal')
        self.exit_button['font'] = ('方正舒体', int(lb_config + lb_config * ratio), 'normal')

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