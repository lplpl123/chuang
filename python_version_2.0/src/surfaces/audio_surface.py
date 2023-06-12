import os
from tkinter import *
from tkinter import filedialog
from PIL import Image
from config import app, button_label


class AudioSurface:
    def __init__(self, root):
        self.audio_frame = Frame(root, width=app["width"], height=app["height"])
        root.bind("<Configure>", lambda event: self.audio_frame_auto_resize(event, root), add="+")
        self.lb = Label(self.audio_frame, text='请录下一段声音......', bd=0, bg="#171841",
                        fg="white")  # todo 要从任务库抽取任务
        self.upload_button = Label(self.audio_frame, text='upload', bg="#171841", fg="white", cursor='hand2')
        self.upload_button.bind('<Button-1>', self.upload_audio)
        self.exit_button = Label(self.audio_frame, text='exit', bg="#171841", fg="white", cursor='hand2')
        self.exit_button.bind('<Button-1>', self.exit)
        self.audio_frame.bind("<Configure>", lambda event: self.widgets_auto_resize(event))

    def blit_widgets(self):
        self.audio_frame.place(relx=0.0, rely=0.0, anchor='nw')
        self.audio_frame.tkraise()
        self.lb.place(relx=0.5, rely=0.0, anchor='n')
        self.upload_button.place(anchor='center', relx=0.5, rely=0.5)
        self.exit_button.place(anchor='center', relx=0.2, rely=0.9)

    def upload_audio(self, event):
        # todo 得做个判断，是和任务相匹配的才能上传成功
        file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser('H:/')))
        if file_path:
            # 保存文件
            image = Image.open(file_path)
            image.save("")
            # todo 如果保存成功的话，需要退出这个界面，直接调用退出函数就好了exit

    def exit(self, event):
        self.audio_frame.place_forget()

    def audio_frame_auto_resize(self, event, root):
        self.audio_frame['width'] = root.winfo_width()
        self.audio_frame['height'] = root.winfo_height()

    def widgets_auto_resize(self, event):
        frame_width = self.audio_frame.winfo_width()
        frame_height = self.audio_frame.winfo_height()
        ratio = min(frame_height, frame_width) / 300
        # auto resize widgets
        lb_config = button_label["text_size"]
        self.lb['font'] = ('方正舒体', int(lb_config + lb_config * ratio), 'normal')
        self.upload_button['font'] = ('方正舒体', int(lb_config + lb_config * ratio), 'normal')
        self.exit_button['font'] = ('方正舒体', int(lb_config + lb_config * ratio), 'normal')