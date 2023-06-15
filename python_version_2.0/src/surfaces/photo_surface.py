import os
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
from config import app, button_label


class PhotoSurface:
    def __init__(self, root):
        # init params
        self.root = root
        self.play_index = 1
        self.output_imgs = "./resources/surfaces_imgs/photo_surface_imgs/camera.png"
        # init widgets
        self.photo_frame = Frame(root, width=app["width"], height=app["height"], bg='#F6F6F6')
        root.bind("<Configure>", lambda event: self.photo_frame_auto_resize(event, root), add="+")
        self.lb = Label(self.photo_frame, text='请拍下一张照片......', bd=0, bg="#F6F6F6",
                        fg="#b8d38f")  # todo 要从任务库抽取任务
        self.upload_button = Label(self.photo_frame, text='upload', bg="#F6F6F6", fg="#b8d38f", cursor='hand2')
        self.upload_button.bind('<Button-1>', self.upload_photo)
        self.exit_button = Label(self.photo_frame, text='exit', bg="#F6F6F6", fg="#b8d38f", cursor='hand2')
        self.exit_button.bind('<Button-1>', self.exit)
        self.photo_frame.bind("<Configure>", lambda event: self.widgets_auto_resize(event))
        self.decoration = Label(self.photo_frame, bd=0, width=60, height=60)
        with Image.open(self.output_imgs) as img:
            img = img.resize((int(self.decoration['width']), int(self.decoration['height'])))
            image = ImageTk.PhotoImage(img)
        self.decoration.config(image=image)
        self.decoration.img = image

    def blit_widgets(self):
        self.photo_frame.place(relx=0.0, rely=0.0, anchor='nw')
        self.photo_frame.tkraise()
        self.lb.place(relx=0.5, rely=0.0, anchor='n')
        self.upload_button.place(anchor='center', relx=0.5, rely=0.5)
        self.exit_button.place(anchor='center', relx=0.2, rely=0.9)
        self.decoration.place(relx=0.90, rely=0.95, anchor='se')

    def upload_photo(self, event):
        # todo 得做个判断，是和任务相匹配的才能上传成功
        file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser('H:/')))
        if file_path:
            # 保存文件
            image = Image.open(file_path)
            image.save("")
            # todo 如果保存成功的话，需要退出这个界面，直接调用退出函数就好了exit

    def exit(self, event):
        self.photo_frame.place_forget()

    def photo_frame_auto_resize(self, event, root):
        self.photo_frame['width'] = root.winfo_width()
        self.photo_frame['height'] = root.winfo_height()

    def widgets_auto_resize(self, event):
        frame_width = self.photo_frame.winfo_width()
        frame_height = self.photo_frame.winfo_height()
        ratio = min(frame_height, frame_width) / 300
        # auto resize widgets
        lb_config = button_label["text_size"]
        self.lb['font'] = ('方正舒体', int(lb_config + lb_config * ratio), 'normal')
        self.upload_button['font'] = ('方正舒体', int(lb_config + lb_config * ratio), 'normal')
        self.exit_button['font'] = ('方正舒体', int(lb_config + lb_config * ratio), 'normal')